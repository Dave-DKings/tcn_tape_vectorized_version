"""
PPO Agent Implementation for Portfolio Optimization

This module implements the Proximal Policy Optimization (PPO) algorithm
specifically designed for portfolio optimization using Dirichlet distributions.

The agent uses:
- Dirichlet distribution for action space (portfolio weights)
- Generalized Advantage Estimation (GAE) for advantage calculation
- Clipped surrogate objective for stable policy updates
- Separate actor and critic networks
"""

import tensorflow as tf
import tensorflow_probability as tfp
import numpy as np
from collections import deque
import logging
import sys
import os
import math
from typing import Any, Dict, List, Optional, Tuple

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.actor_critic_tf import create_actor_critic
from config import is_sequential_architecture

# Set up logging
logger = logging.getLogger(__name__)

tfd = tfp.distributions


def _to_tensor_with_cast(value, dtype=None):
    """Convert to tensor and cast dtype explicitly (safe with mixed precision tensors)."""
    tensor = tf.convert_to_tensor(value)
    if dtype is not None:
        target_dtype = tf.dtypes.as_dtype(dtype)
        if tensor.dtype != target_dtype:
            tensor = tf.cast(tensor, target_dtype)
    return tensor


class RunningMeanStd:
    """
    Track running mean and variance for streaming normalization.

    PERF-FIX #3: Uses exponential moving average (EMA) instead of Welford
    accumulator for faster adaptation to distribution shifts (e.g. when
    episode length or reward scale changes during curriculum learning).
    """

    def __init__(self, epsilon: float = 1e-4, ema_decay: float = 0.999):
        self.mean = 0.0
        self.var = 1.0
        self.count = epsilon
        self.ema_decay = ema_decay

    def update(self, x):
        """Update running statistics with a new batch using EMA."""
        x = np.asarray(x, dtype=np.float64)
        if x.size == 0:
            return

        batch_mean = np.mean(x)
        batch_var = np.var(x)
        batch_count = x.shape[0]

        # EMA adaptation: alpha controls how fast we forget old stats
        # For a batch of size n, effective alpha = 1 - decay^n
        alpha = 1.0 - self.ema_decay ** batch_count

        if self.count < 1.0:
            # First update: initialize directly from batch
            self.mean = float(batch_mean)
            self.var = float(max(batch_var, 1e-8))
        else:
            # EMA update
            self.mean = float((1 - alpha) * self.mean + alpha * batch_mean)
            self.var = float(max(
                (1 - alpha) * self.var + alpha * batch_var,
                1e-8
            ))

        self.count = float(self.count + batch_count)

    @property
    def std(self):
        """Return the running standard deviation."""
        return math.sqrt(self.var + 1e-8)

    def normalize(self, x):
        """Normalize array using current running statistics."""
        return (np.asarray(x) - self.mean) / (self.std)


class PPOAgentTF:
    """
    PPO Agent for Portfolio Optimization using Dirichlet distributions.
    
    This agent is specifically designed for portfolio optimization where:
    1. Actions are portfolio weights that must sum to 1
    2. All weights must be non-negative
    3. The action space is naturally constrained to the probability simplex
    
    The Dirichlet distribution handles these constraints naturally while
    allowing for exploration and smooth policy updates.
    """
    
    def __init__(self, 
                 state_dim,
                 num_assets,
                 config,
                 name="PPOAgent"):
        """
        Initialize the PPO agent with architecture-agnostic design.
        
        Args:
            state_dim (int): Dimension of the state space (features)
            num_assets (int): Number of assets (excluding cash)
            config (dict): Configuration dictionary with all agent parameters
            name (str): Name of the agent
        """
        
        self.state_dim = state_dim
        self.num_assets = num_assets
        self.num_actions = num_assets + 1  # assets + cash
        self.name = name
        
        # Extract architecture type
        self.architecture = config.get('actor_critic_type', 'TCN')
        self.is_sequential = is_sequential_architecture(self.architecture)
        
        # Sequential model parameters
        if self.is_sequential:
            self.sequence_length = config.get('sequence_length', 30)
            logger.info(f"Sequential architecture: {self.architecture}, sequence_length={self.sequence_length}")
            self.state_history = deque(maxlen=self.sequence_length)
        else:
            self.sequence_length = None
            self.state_history = None
            logger.info(f"Non-sequential architecture: {self.architecture}")
        self._latest_sequence = None

        # Optional structured layout metadata for fusion architectures.
        state_layout = config.get("state_layout", {}) if isinstance(config.get("state_layout", {}), dict) else {}
        self.state_layout = state_layout
        self.asset_feature_dim = int(state_layout.get("asset_feature_dim", 0) or 0)
        self.global_feature_dim = int(state_layout.get("global_feature_dim", 0) or 0)
        self.local_flat_dim = int(state_layout.get("local_flat_dim", self.num_assets * max(self.asset_feature_dim, 0)) or 0)
        self.structured_observation = bool(state_layout.get("structured_observation", False))
        self.uses_structured_state_inputs = bool(
            self.is_sequential
            and self.structured_observation
            and self.asset_feature_dim > 0
        )
        # Backward-compatible alias kept for notebook conditionals.
        self.uses_structured_fusion_inputs = self.uses_structured_state_inputs

        # Dirichlet exploration annealing defaults
        epsilon_cfg = config.get("dirichlet_epsilon") or {}
        self.dirichlet_epsilon_max = float(epsilon_cfg.get("max", epsilon_cfg.get("start", 0.5)))
        self.dirichlet_epsilon_min = float(epsilon_cfg.get("min", 0.1))
        self._dirichlet_progress = 0.0
        training_cfg = config.get("training_params")
        training_timesteps = 0
        if isinstance(training_cfg, dict):
            training_timesteps = training_cfg.get("max_total_timesteps", 0)
        self.max_total_timesteps = int(config.get("max_total_timesteps", training_timesteps or 0))
        self._global_step = 0
        
        # PPO hyperparameters
        ppo_params = config.get('ppo_params', {})
        self.gamma = ppo_params.get('gamma', 0.99)
        self.gae_lambda = ppo_params.get('gae_lambda', 0.9)
        self.policy_clip = ppo_params.get('policy_clip', 0.2)
        self.entropy_coef = ppo_params.get('entropy_coef', 0.01)
        self.vf_coef = ppo_params.get('vf_coef', 0.5)
        self.max_grad_norm = ppo_params.get('max_grad_norm', 0.5)
        self.value_clip_range = ppo_params.get('value_clip', 0.2)
        self.target_kl = float(ppo_params.get('target_kl', 0.03))
        self.kl_stop_multiplier = float(ppo_params.get('kl_stop_multiplier', 1.5))
        self.minibatches_before_kl_stop = int(ppo_params.get('minibatches_before_kl_stop', 2))
        # PERF-FIX #4b: Alpha diversity HHI auxiliary loss coefficient
        self.alpha_diversity_coef = float(ppo_params.get('alpha_diversity_coef', 0.0))
        # Run9: penalize near-uniform allocations when cross-asset discrimination collapses.
        self.alpha_dispersion_coef = float(max(ppo_params.get('alpha_dispersion_coef', 0.0), 0.0))
        self.alpha_dispersion_target_std = float(max(ppo_params.get('alpha_dispersion_target_std', 0.05), 0.0))

        # SOTA-FIX Phase 3: Auxiliary per-asset return prediction loss coefficient
        # Forces the backbone to learn asset-discriminative features via supervised signal.
        # Reference: Jaderberg et al. (2017) — UNREAL
        self.aux_return_pred_coef = float(ppo_params.get('aux_return_pred_coef', 0.1))
        self.aux_return_pred_enabled = bool(ppo_params.get('aux_return_pred_enabled', True))

        # SOTA-FIX Phase 3: Lagrangian CVaR constraint
        # Dense step-level constraint that replaces sparse terminal CVaR bonus.
        # Reference: Tessler et al. (2019) — Reward Constrained Policy Optimization
        self.lagrangian_cvar_enabled = bool(ppo_params.get('lagrangian_cvar_enabled', True))
        self.lagrangian_cvar_threshold = float(ppo_params.get('lagrangian_cvar_threshold', -0.017))
        self.lagrangian_cvar_lr = float(ppo_params.get('lagrangian_cvar_lr', 0.01))
        self.lagrangian_cvar_lambda_max = float(ppo_params.get('lagrangian_cvar_lambda_max', 2.0))
        self.lagrangian_cvar_penalty_scale = float(
            max(ppo_params.get('lagrangian_cvar_penalty_scale', 1.0), 0.0)
        )
        self._lagrangian_cvar_lambda = 0.0  # adaptive multiplier, starts at 0

        # Optional risk-aware actor auxiliary losses (disabled by default).
        # These are additive regularizers intended to improve risk-adjusted robustness.
        self.use_risk_aux_loss = bool(ppo_params.get('use_risk_aux_loss', False))
        self.risk_aux_return_feature_index = int(ppo_params.get('risk_aux_return_feature_index', 0))
        self.risk_aux_cash_return = float(ppo_params.get('risk_aux_cash_return', 0.0))
        self.risk_aux_sharpe_coef = float(ppo_params.get('risk_aux_sharpe_coef', 0.0))
        self.risk_aux_mvo_coef = float(ppo_params.get('risk_aux_mvo_coef', 0.0))
        self.risk_aux_cvar_coef = float(max(ppo_params.get('risk_aux_cvar_coef', 0.0), 0.0))
        self.risk_aux_cvar_coef_base = float(self.risk_aux_cvar_coef)
        self.risk_aux_cvar_alpha = float(
            np.clip(ppo_params.get('risk_aux_cvar_alpha', 0.05), 1e-3, 0.5)
        )
        self.risk_aux_cvar_adaptive_enabled = bool(ppo_params.get('risk_aux_cvar_adaptive_enabled', False))
        self.risk_aux_cvar_target = float(ppo_params.get('risk_aux_cvar_target', 0.02))
        self.risk_aux_cvar_adapt_lr = float(max(ppo_params.get('risk_aux_cvar_adapt_lr', 0.05), 0.0))
        self.risk_aux_cvar_min_coef = float(max(ppo_params.get('risk_aux_cvar_min_coef', 0.0), 0.0))
        self.risk_aux_cvar_max_coef = float(
            max(
                ppo_params.get(
                    'risk_aux_cvar_max_coef',
                    max(self.risk_aux_cvar_coef_base * 5.0, self.risk_aux_cvar_coef_base + 1e-6),
                ),
                self.risk_aux_cvar_min_coef,
            )
        )
        self.risk_aux_mvo_cov_ridge = float(ppo_params.get('risk_aux_mvo_cov_ridge', 1e-3))
        self.risk_aux_mvo_long_only = bool(ppo_params.get('risk_aux_mvo_long_only', True))
        self.risk_aux_mvo_risky_budget = float(
            np.clip(ppo_params.get('risk_aux_mvo_risky_budget', 0.95), 0.0, 1.0)
        )
        self.distributional_critic_enabled = bool(config.get('distributional_critic_enabled', False))
        self.distributional_num_quantiles = int(max(2, config.get('distributional_num_quantiles', 17)))
        self.distributional_huber_kappa = float(max(ppo_params.get('distributional_huber_kappa', 1.0), 1e-3))
        self.distributional_mean_loss_coef = float(max(ppo_params.get('distributional_mean_loss_coef', 0.1), 0.0))
        self.critic_use_huber = bool(ppo_params.get('critic_use_huber', True))
        self.critic_huber_delta = float(max(ppo_params.get('critic_huber_delta', 2.0), 1e-3))
        self.advantage_clip_value = float(max(ppo_params.get('advantage_clip_value', 5.0), 0.0))
        self.expert_advantage_clip_value = float(max(ppo_params.get('expert_advantage_clip_value', 3.0), 0.0))
        self.sanitize_nonfinite_gradients = bool(ppo_params.get('sanitize_nonfinite_gradients', True))
        # Run9: blend lower-tail critic estimates into the scalar value used for GAE.
        self.cvar_advantage_weight = float(np.clip(ppo_params.get('cvar_advantage_weight', 0.0), 0.0, 1.0))
        self.cvar_advantage_k = int(max(1, ppo_params.get('cvar_advantage_k', 4)))
        self.popart_enabled = bool(ppo_params.get('popart_enabled', False))
        self.popart_min_std = float(max(ppo_params.get('popart_min_std', 1e-3), 1e-6))
        self.multi_horizon_reward_enabled = bool(ppo_params.get('multi_horizon_reward_enabled', False))
        self.multi_horizon_reward_coef = float(max(ppo_params.get('multi_horizon_reward_coef', 0.0), 0.0))
        raw_mh_horizons = ppo_params.get('multi_horizon_reward_horizons', [21, 63, 126, 252])
        self.multi_horizon_reward_horizons = []
        if isinstance(raw_mh_horizons, (list, tuple)):
            for horizon in raw_mh_horizons:
                try:
                    h = int(horizon)
                except (TypeError, ValueError):
                    continue
                if h > 0:
                    self.multi_horizon_reward_horizons.append(h)
        self.multi_horizon_reward_horizons = sorted(set(self.multi_horizon_reward_horizons))
        raw_mh_weights = ppo_params.get('multi_horizon_reward_weights', [])
        self.multi_horizon_reward_weights = []
        if isinstance(raw_mh_weights, (list, tuple)):
            for w in raw_mh_weights:
                try:
                    self.multi_horizon_reward_weights.append(float(w))
                except (TypeError, ValueError):
                    continue
        if (
            len(self.multi_horizon_reward_weights) != len(self.multi_horizon_reward_horizons)
            or sum(self.multi_horizon_reward_weights) <= 0.0
        ):
            if self.multi_horizon_reward_horizons:
                equal_w = 1.0 / float(len(self.multi_horizon_reward_horizons))
                self.multi_horizon_reward_weights = [equal_w] * len(self.multi_horizon_reward_horizons)
            else:
                self.multi_horizon_reward_weights = []
        else:
            total_w = float(sum(self.multi_horizon_reward_weights))
            self.multi_horizon_reward_weights = [max(0.0, w) / total_w for w in self.multi_horizon_reward_weights]

        # Dual-head action policy:
        #   Dirichlet branch (stochastic exploration) + softmax/projection branch (production-style weights)
        self.dual_head_enabled = bool(config.get('dual_head_enabled', False))
        self.dual_head_consistency_coef = float(max(ppo_params.get('dual_head_consistency_coef', 0.0), 0.0))
        raw_dual_schedule = (
            config.get('dual_head_blend_schedule')
            if config.get('dual_head_blend_schedule') is not None
            else ppo_params.get('dual_head_blend_schedule')
        )
        if not isinstance(raw_dual_schedule, (list, tuple)) or len(raw_dual_schedule) == 0:
            raw_dual_schedule = [
                {"threshold": 0, "rho": 0.35},
                {"threshold": 30_000, "rho": 0.55},
                {"threshold": 60_000, "rho": 0.70},
            ]
        dual_schedule = []
        for entry in raw_dual_schedule:
            if not isinstance(entry, dict):
                continue
            try:
                threshold = int(entry.get('threshold', 0))
                rho = float(entry.get('rho', 0.0))
            except (TypeError, ValueError):
                continue
            dual_schedule.append({"threshold": max(0, threshold), "rho": float(np.clip(rho, 0.0, 1.0))})
        if not dual_schedule:
            dual_schedule = [{"threshold": 0, "rho": 0.0}]
        dual_schedule.sort(key=lambda item: item["threshold"])
        if dual_schedule[0]["threshold"] != 0:
            dual_schedule.insert(0, {"threshold": 0, "rho": dual_schedule[0]["rho"]})
        self.dual_head_blend_schedule = dual_schedule
        self.dual_head_eval_deterministic_rho = float(
            np.clip(config.get('dual_head_eval_deterministic_rho', ppo_params.get('dual_head_eval_deterministic_rho', 0.90)), 0.0, 1.0)
        )
        self.dual_head_eval_stochastic_rho = float(
            np.clip(config.get('dual_head_eval_stochastic_rho', ppo_params.get('dual_head_eval_stochastic_rho', 0.60)), 0.0, 1.0)
        )
        self.dual_head_projection_use_constraints = bool(
            config.get('dual_head_projection_use_constraints', ppo_params.get('dual_head_projection_use_constraints', False))
        )
        self.mixture_dirichlet_enabled = bool(config.get('mixture_dirichlet_enabled', False))
        self.mixture_dirichlet_num_components = int(max(1, config.get('mixture_dirichlet_num_components', 1)))
        self.mixture_dirichlet_eval_mode = str(
            config.get('mixture_dirichlet_eval_mode', 'top_component_mean')
        ).lower().strip()
        self.mixture_dirichlet_balance_coef = float(
            max(ppo_params.get('mixture_dirichlet_balance_coef', 0.0), 0.0)
        )
        self.mixture_dirichlet_separation_coef = float(
            max(ppo_params.get('mixture_dirichlet_separation_coef', 0.0), 0.0)
        )
        self.mixture_dirichlet_entropy_coef = float(
            max(ppo_params.get('mixture_dirichlet_entropy_coef', 0.0), 0.0)
        )
        self.mixture_component_dispersion_coef = float(
            max(ppo_params.get('mixture_component_dispersion_coef', 0.0), 0.0)
        )
        self.mixture_component_target_std = float(
            max(ppo_params.get('mixture_component_target_std', 0.0), 0.0)
        )
        self.mixture_component_min_distance = float(
            max(ppo_params.get('mixture_component_min_distance', 0.0), 0.0)
        )
        self.mixture_dirichlet_balance_schedule = self._parse_threshold_coef_schedule(
            ppo_params.get('mixture_dirichlet_balance_schedule', []),
            fallback_coef=self.mixture_dirichlet_balance_coef,
        )
        self.mixture_dirichlet_entropy_schedule = self._parse_threshold_coef_schedule(
            ppo_params.get('mixture_dirichlet_entropy_schedule', []),
            fallback_coef=self.mixture_dirichlet_entropy_coef,
        )
        raw_max_single = config.get('max_single_position', ppo_params.get('dual_head_projection_max_single_position', 0.20))
        raw_min_cash = config.get('min_cash_position', ppo_params.get('dual_head_projection_min_cash_position', 0.05))
        try:
            max_single = float(raw_max_single)
        except (TypeError, ValueError):
            max_single = 0.20
        if max_single > 1.0:
            max_single /= 100.0
        self.dual_head_projection_max_single_position = float(np.clip(max_single, 0.0, 1.0))
        try:
            min_cash = float(raw_min_cash)
        except (TypeError, ValueError):
            min_cash = 0.05
        self.dual_head_projection_min_cash_position = float(np.clip(min_cash, 0.0, 1.0))
        self.objective_experts_enabled = bool(config.get('objective_experts_enabled', False))
        self.objective_expert_names = [
            str(x).strip().lower()
            for x in config.get('objective_expert_names', ['return', 'risk', 'discipline'])
            if str(x).strip()
        ]
        if not self.objective_expert_names:
            self.objective_expert_names = ['return', 'risk', 'discipline']
        self.num_objective_experts = len(self.objective_expert_names)
        self.objective_head_aux_coef = float(max(ppo_params.get('objective_head_aux_coef', 0.5), 0.0))
        self.objective_head_aux_loss_clip = float(max(ppo_params.get('objective_head_aux_loss_clip', 0.25), 0.0))
        self.objective_head_diversity_coef = float(max(ppo_params.get('objective_head_diversity_coef', 0.02), 0.0))
        self.objective_router_entropy_coef = float(max(ppo_params.get('objective_router_entropy_coef', 0.005), 0.0))
        self.objective_expert_mask = np.ones((self.num_objective_experts,), dtype=np.float32)
        if self.objective_experts_enabled:
            if self.dual_head_enabled:
                raise ValueError("objective_experts_enabled is not compatible with dual_head_enabled.")
            if self.mixture_dirichlet_enabled:
                raise ValueError("objective_experts_enabled is not compatible with mixture_dirichlet_enabled.")
            if self.distributional_critic_enabled:
                raise ValueError("objective_experts_enabled currently requires scalar critics.")

        # Create networks using architecture factory
        logger.info(f"Creating {self.architecture} actor-critic networks...")
        self.actor, self.critic = create_actor_critic(
            architecture=self.architecture,
            input_dim=state_dim,
            num_actions=self.num_actions,
            config=config
        )
        
        # Create optimizers
        actor_lr = ppo_params.get('actor_lr', 3e-3)
        critic_lr = ppo_params.get('critic_lr', 3e-3)
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=actor_lr)
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=critic_lr)
        self._current_actor_lr = float(actor_lr)
        self._current_critic_lr = float(critic_lr)
        
        # Memory for storing trajectory data
        self.memory = {
            'states': [],
            'actions': [],
            'log_probs': [],
            'mixture_components': [],
            'rewards': [],
            'values': [],
            'expert_rewards': [],
            'expert_values': [],
            'expert_log_probs': [],
            'router_probs': [],
            'dones': []
        }
        self._latest_action_metadata = {}
        self._latest_batch_action_metadata = {}
        self._last_policy_debug = {}
        
        logger.info(f"Initialized {name}")
        logger.info(f"  State dim: {state_dim}, Num assets: {num_assets}, Actions: {self.num_actions}")
        logger.info(f"  Architecture: {self.architecture} (Sequential: {self.is_sequential})")
        logger.info(
            "  Dual-head policy: enabled=%s | train_schedule=%s | eval_rho(det=%.2f, sto=%.2f) | projection=%s",
            self.dual_head_enabled,
            self.dual_head_blend_schedule,
            self.dual_head_eval_deterministic_rho,
            self.dual_head_eval_stochastic_rho,
            self.dual_head_projection_use_constraints,
        )
        if self.uses_structured_state_inputs:
            logger.info(
                "  Structured state reshape enabled: assets=%d, asset_feature_dim=%d, global_feature_dim=%d",
                self.num_assets,
                self.asset_feature_dim,
                self.global_feature_dim,
            )
        logger.info(
            f"  PPO params: γ={self.gamma}, λ={self.gae_lambda}, clip={self.policy_clip}, "
            f"value_clip={self.value_clip_range}, target_kl={self.target_kl:.4f}"
        )
        logger.info(
            "  Risk aux: enabled=%s, sharpe_coef=%.4f, mvo_coef=%.4f, cvar_coef=%.4f, cvar_alpha=%.3f, cvar_adaptive=%s, return_feature_idx=%d",
            self.use_risk_aux_loss,
            self.risk_aux_sharpe_coef,
            self.risk_aux_mvo_coef,
            self.risk_aux_cvar_coef,
            self.risk_aux_cvar_alpha,
            self.risk_aux_cvar_adaptive_enabled,
            self.risk_aux_return_feature_index,
        )
        logger.info(
            "  Critic head: distributional=%s, quantiles=%d",
            self.distributional_critic_enabled,
            self.distributional_num_quantiles,
        )
        logger.info(
            "  PopArt: enabled=%s, min_std=%.6f",
            self.popart_enabled,
            self.popart_min_std,
        )
        logger.info(
            "  Multi-horizon reward decomposition: enabled=%s, coef=%.4f, horizons=%s, weights=%s",
            self.multi_horizon_reward_enabled,
            self.multi_horizon_reward_coef,
            self.multi_horizon_reward_horizons,
            [round(float(w), 4) for w in self.multi_horizon_reward_weights],
        )
        logger.info(
            f"  Learning rates (init): actor={self.get_actor_lr():.6f}, critic={self.get_critic_lr():.6f}"
        )
        logger.info(f"  Networks created: {self.actor.name}, {self.critic.name}")

        # Initialize epsilon schedule at maximum exploration
        self.set_dirichlet_progress(0.0)

        # Running statistics for critic target normalization
        self.returns_rms = RunningMeanStd()
        self._returns_mean = 0.0
        self._returns_std = 1.0
        # Running statistics for reward normalization
        self.reward_rms = RunningMeanStd()
        self._reward_mean = 0.0
        self._reward_std = 1.0
        self.expert_reward_rms = [RunningMeanStd() for _ in range(self.num_objective_experts)]
        self._expert_reward_mean = np.zeros((self.num_objective_experts,), dtype=np.float32)
        self._expert_reward_std = np.ones((self.num_objective_experts,), dtype=np.float32)
        # Debug/diagnostic verbosity toggle
        self.debug_prints = bool(config.get('debug_prints', False))

        # PERF-FIX #7: EMA (Polyak-averaged) actor weights for stable evaluation
        self.ema_decay = float(ppo_params.get('ema_actor_decay', 0.995))
        self.actor_ema_weights = None
        self._init_ema_actor()

    def get_actor_lr(self) -> float:
        """Return the actor optimizer learning rate as a python float."""
        try:
            return float(tf.keras.backend.get_value(self.actor_optimizer.learning_rate))
        except Exception:
            return float(self._current_actor_lr)

    def set_actor_lr(self, new_lr: float) -> None:
        """Update the actor optimizer learning rate in-place."""
        new_lr = float(new_lr)
        if hasattr(self.actor_optimizer.learning_rate, "assign"):
            self.actor_optimizer.learning_rate.assign(new_lr)
        else:
            self.actor_optimizer.learning_rate = new_lr
        self._current_actor_lr = new_lr

    # ═════════════════════════════════════════════════════════════════════════
    # PERF-FIX #7: EMA (Polyak-averaged) actor weight tracking
    # ═════════════════════════════════════════════════════════════════════════

    def _init_ema_actor(self):
        """Initialize EMA actor weights as a copy of current actor weights."""
        try:
            self.actor_ema_weights = [w.numpy().copy() for w in self.actor.trainable_weights]
            logger.info("  EMA actor initialized (decay=%.4f, %d weight tensors)",
                       self.ema_decay, len(self.actor_ema_weights))
        except Exception as e:
            logger.warning("  EMA actor init failed: %s", e)
            self.actor_ema_weights = None

    def _update_ema_actor(self):
        """Polyak update: ema_w = decay * ema_w + (1 - decay) * actor_w."""
        if self.actor_ema_weights is None:
            return
        try:
            current_weights = self.actor.trainable_weights
            for i, w in enumerate(current_weights):
                self.actor_ema_weights[i] = (
                    self.ema_decay * self.actor_ema_weights[i]
                    + (1.0 - self.ema_decay) * w.numpy()
                )
        except Exception:
            pass  # Silently skip if weight shape mismatch etc.

    def get_ema_actor_weights(self):
        """Return the EMA-averaged actor weights (for evaluation/checkpointing)."""
        return self.actor_ema_weights

    def get_film_diagnostics(self, state_batch) -> dict:
        """Collect lightweight FiLM diagnostics from the actor when available."""
        actor = getattr(self, "actor", None)
        if actor is None or not hasattr(actor, "get_film_diagnostics"):
            return {}
        try:
            return dict(actor.get_film_diagnostics(state_batch) or {})
        except Exception:
            return {}

    def apply_ema_actor_weights(self):
        """Temporarily apply EMA weights to actor for evaluation."""
        if self.actor_ema_weights is None:
            return None
        # Save current weights to restore later
        backup = [w.numpy().copy() for w in self.actor.trainable_weights]
        for w, ema_w in zip(self.actor.trainable_weights, self.actor_ema_weights):
            w.assign(ema_w)
        return backup

    def restore_actor_weights(self, backup):
        """Restore actor weights from backup (after EMA evaluation)."""
        if backup is None:
            return
        for w, bw in zip(self.actor.trainable_weights, backup):
            w.assign(bw)

    def get_critic_lr(self) -> float:
        """Return the critic optimizer learning rate as a python float."""
        try:
            return float(tf.keras.backend.get_value(self.critic_optimizer.learning_rate))
        except Exception:
            return float(self._current_critic_lr)

    def set_critic_lr(self, new_lr: float) -> None:
        """Update the critic optimizer learning rate in-place."""
        new_lr = float(new_lr)
        if hasattr(self.critic_optimizer.learning_rate, "assign"):
            self.critic_optimizer.learning_rate.assign(new_lr)
        else:
            self.critic_optimizer.learning_rate = new_lr
        self._current_critic_lr = new_lr

    def set_dirichlet_progress(self, progress: float) -> None:
        """Adjust the actor's Dirichlet epsilon according to normalized progress."""
        if not hasattr(self.actor, "update_dirichlet_epsilon"):
            return
        if np.isnan(progress):
            progress = 0.0
        progress = float(np.clip(progress, 0.0, 1.0))
        self._dirichlet_progress = progress
        self.actor.update_dirichlet_epsilon(
            progress,
            self.dirichlet_epsilon_min,
            self.dirichlet_epsilon_max,
        )

    def set_objective_expert_mask(self, mask: List[float]) -> None:
        if not self.objective_experts_enabled:
            return
        arr = np.asarray(mask, dtype=np.float32).reshape(-1)
        if arr.size != self.num_objective_experts:
            raise ValueError(
                f"objective expert mask size mismatch: got {arr.size}, expected {self.num_objective_experts}"
            )
        arr = np.where(arr > 0.0, 1.0, 0.0).astype(np.float32)
        if float(np.sum(arr)) <= 0.0:
            arr[0] = 1.0
        self.objective_expert_mask = arr
        if hasattr(self.actor, "set_objective_expert_mask"):
            self.actor.set_objective_expert_mask(arr.tolist())

    def _split_flat_state_array(self, state_array):
        """
        Split flat states into per-asset and global-context tensors using state_layout metadata.
        """
        if self.asset_feature_dim <= 0:
            raise ValueError("asset_feature_dim must be > 0 for structured fusion input.")

        arr = np.asarray(state_array, dtype=np.float32)
        if arr.ndim < 1:
            raise ValueError(f"Unsupported state array shape for structured split: {arr.shape}")

        expected_dim = self.local_flat_dim + max(0, self.global_feature_dim)
        current_dim = int(arr.shape[-1])
        if current_dim < expected_dim:
            pad_width = [(0, 0)] * arr.ndim
            pad_width[-1] = (0, expected_dim - current_dim)
            arr = np.pad(arr, pad_width, mode="constant", constant_values=0.0)
        elif current_dim > expected_dim:
            arr = arr[..., :expected_dim]

        local = arr[..., :self.local_flat_dim]
        local_shape = local.shape[:-1] + (self.num_assets, self.asset_feature_dim)
        local = np.reshape(local, local_shape)

        if self.global_feature_dim > 0:
            context = arr[..., self.local_flat_dim:self.local_flat_dim + self.global_feature_dim]
        else:
            context = np.zeros(arr.shape[:-1] + (0,), dtype=np.float32)

        return local.astype(np.float32), context.astype(np.float32)

    def _structured_state_to_tensor_input(self, state):
        """
        Convert flat or dict state into fusion-ready tensor dict.
        """
        if isinstance(state, dict):
            asset = state.get("asset")
            context = state.get("context")
            if asset is None:
                raise ValueError("Structured state dict must contain key 'asset'.")
            asset = _to_tensor_with_cast(asset, tf.float32)
            context = _to_tensor_with_cast(context, tf.float32) if context is not None else None
        else:
            if isinstance(state, tf.Tensor):
                state = state.numpy()
            asset_np, context_np = self._split_flat_state_array(state)
            asset = _to_tensor_with_cast(asset_np, tf.float32)
            context = _to_tensor_with_cast(context_np, tf.float32)

        return {"asset": asset, "context": context}

    def _convert_states_for_network(self, states):
        """
        Convert stored rollout states into actor/critic network inputs.
        """
        if not self.uses_structured_state_inputs:
            return tf.constant(states, dtype=tf.float32)

        asset_np, context_np = self._split_flat_state_array(states)
        return {
            "asset": tf.constant(asset_np, dtype=tf.float32),
            "context": tf.constant(context_np, dtype=tf.float32),
        }
    
    def prepare_state_input(self, state):
        """
        Prepare state tensor with architecture-specific handling.
        
        Args:
            state: Input state (numpy array or tensor)
                - Sequential: (timesteps, features) or (batch, timesteps, features)
        
        Returns:
            Tuple of (prepared_state, needs_squeeze)
            - prepared_state: TensorFlow tensor with batch dimension
            - needs_squeeze: Boolean indicating if output should be squeezed
        """
        if self.is_sequential and self.uses_structured_state_inputs:
            structured = self._structured_state_to_tensor_input(state)
            asset = structured["asset"]
            context = structured["context"]

            if len(asset.shape) == 3:
                # (timesteps, assets, features) -> (1, timesteps, assets, features)
                asset = tf.expand_dims(asset, axis=0)
                if context is None:
                    context = tf.zeros((1, tf.shape(asset)[1], self.global_feature_dim), dtype=asset.dtype)
                elif len(context.shape) == 2:
                    context = tf.expand_dims(context, axis=0)
                elif len(context.shape) == 1:
                    context = tf.expand_dims(tf.expand_dims(context, axis=0), axis=0)
                return {"asset": asset, "context": context}, True

            if len(asset.shape) == 4:
                # Already batched
                if context is None:
                    batch = tf.shape(asset)[0]
                    steps = tf.shape(asset)[1]
                    context = tf.zeros((batch, steps, self.global_feature_dim), dtype=asset.dtype)
                elif len(context.shape) == 2:
                    context = tf.expand_dims(context, axis=1)
                return {"asset": asset, "context": context}, False

            raise ValueError(
                f"Structured sequential state expects asset rank 3 or 4, got shape {asset.shape}"
            )
        
        # Convert to tensor if needed
        if not isinstance(state, tf.Tensor):
            state = tf.constant(state, dtype=tf.float32)
        
        current_ndim = len(state.shape)
        
        if self.is_sequential:
            # Sequential models expect: (batch, timesteps, features)
            if current_ndim == 2:
                # (timesteps, features) => (1, timesteps, features)
                return tf.expand_dims(state, axis=0), True  # needs_squeeze
            elif current_ndim == 3:
                # Already batched: (batch, timesteps, features)
                return state, False
            else:
                raise ValueError(
                    f"Sequential architecture expects 2D or 3D input, got {current_ndim}D with shape {state.shape}"
                )
        else:
            # Non-sequential expects: (batch, features)
            if current_ndim == 1:
                # (features,) => (1, features)
                return tf.expand_dims(state, axis=0), True  # needs_squeeze
            elif current_ndim == 2:
                # Already batched: (batch, features)
                return state, False
            else:
                raise ValueError(
                    f"Non-sequential architecture expects 1D or 2D input, got {current_ndim}D with shape {state.shape}"
                )
    
    def reset_state_history(self):
        """Reset the state history (e.g., at the start of a new episode)."""
        if self.state_history is not None:
            self.state_history.clear()
        self._latest_sequence = None

    def _build_sequence(self, state):
        """
        Build a temporal sequence for sequential architectures.
        
        Args:
            state: Current state vector or pre-built sequence.
        
        Returns:
            np.ndarray of shape (sequence_length, state_dim)
        """
        if not self.is_sequential:
            raise RuntimeError("Attempted to build sequence for non-sequential architecture.")
        
        if isinstance(state, tf.Tensor):
            state = state.numpy()
        state = np.asarray(state, dtype=np.float32)
        
        if state.ndim == 2:
            sequence = state
        elif state.ndim == 1:
            self.state_history.append(state)
            sequence = np.array(list(self.state_history), dtype=np.float32)
        else:
            raise ValueError(f"Unsupported state shape for sequential architecture: {state.shape}")
        
        if sequence.shape[0] > self.sequence_length:
            sequence = sequence[-self.sequence_length:]
        elif sequence.shape[0] < self.sequence_length:
            pad_len = self.sequence_length - sequence.shape[0]
            if sequence.shape[0] > 0:
                pad_value = sequence[0:1]
            else:
                pad_value = np.zeros((1, self.state_dim), dtype=np.float32)
            padding = np.repeat(pad_value, pad_len, axis=0)
            sequence = np.vstack([padding, sequence])
        
        # Refresh history to match the returned sequence
        self.state_history.clear()
        for row in sequence:
            self.state_history.append(row)
        
        return sequence

    def build_sequence_from_history(self, history, state, mutate=True):
        """
        Build a sequence using an external history buffer (for vectorized rollouts).

        Args:
            history: Per-environment history buffer (list/deque of state vectors)
            state: Current state vector or pre-built sequence
            mutate: If True, update `history` in-place to reflect returned sequence

        Returns:
            np.ndarray sequence with shape (sequence_length, state_dim)
        """
        if not self.is_sequential:
            raise RuntimeError("build_sequence_from_history() requires sequential architecture.")

        if isinstance(state, tf.Tensor):
            state = state.numpy()
        state = np.asarray(state, dtype=np.float32)

        if state.ndim == 2:
            sequence = state
        elif state.ndim == 1:
            base_rows = [np.asarray(row, dtype=np.float32) for row in list(history)] if history is not None else []
            if mutate and history is not None:
                history.append(state)
                sequence = np.array(list(history), dtype=np.float32)
            else:
                base_rows.append(state)
                sequence = np.array(base_rows, dtype=np.float32)
        else:
            raise ValueError(f"Unsupported state shape for sequential architecture: {state.shape}")

        if sequence.shape[0] > self.sequence_length:
            sequence = sequence[-self.sequence_length:]
        elif sequence.shape[0] < self.sequence_length:
            pad_len = self.sequence_length - sequence.shape[0]
            if sequence.shape[0] > 0:
                pad_value = sequence[0:1]
            else:
                pad_value = np.zeros((1, self.state_dim), dtype=np.float32)
            padding = np.repeat(pad_value, pad_len, axis=0)
            sequence = np.vstack([padding, sequence])

        if mutate and history is not None:
            history.clear()
            for row in sequence:
                history.append(np.asarray(row, dtype=np.float32))

        return sequence

    def _critic_values_to_scalar(self, critic_output):
        """
        Convert critic output to scalar value per sample.
        Supports scalar critic (batch, 1) and distributional critic (batch, num_quantiles).
        """
        values = _to_tensor_with_cast(critic_output, tf.float32)
        if values.shape.rank is None:
            values = tf.reshape(values, (-1,))
            return values
        if values.shape.rank == 1:
            return values
        if values.shape.rank >= 2:
            last_dim = values.shape[-1]
            if self.distributional_critic_enabled or (last_dim is not None and int(last_dim) > 1):
                mean_val = tf.reduce_mean(values, axis=-1)
                if self.distributional_critic_enabled and self.cvar_advantage_weight > 0.0:
                    sorted_q = tf.sort(values, axis=-1)
                    cvar_val = tf.reduce_mean(sorted_q[..., :self.cvar_advantage_k], axis=-1)
                    blend_weight = tf.constant(self.cvar_advantage_weight, dtype=tf.float32)
                    return (1.0 - blend_weight) * mean_val + blend_weight * cvar_val
                return mean_val
        if values.shape.rank >= 2:
            return tf.squeeze(values, axis=-1)
        return tf.squeeze(values, axis=-1)

    def _denormalize_value(self, value, mean=None, std=None):
        """Convert normalized critic output back to unnormalized value when PopArt is enabled."""
        if not self.popart_enabled:
            return value
        if isinstance(value, tf.Tensor):
            if mean is None:
                mean_tf = tf.cast(self._returns_mean, value.dtype)
            else:
                mean_tf = _to_tensor_with_cast(mean, value.dtype)
            if std is None:
                std_tf = tf.cast(max(self._returns_std, self.popart_min_std), value.dtype)
            else:
                std_tf = tf.maximum(_to_tensor_with_cast(std, value.dtype), tf.cast(self.popart_min_std, value.dtype))
            return value * std_tf + mean_tf
        mean = float(self._returns_mean if mean is None else mean)
        std = float(max(self._returns_std if std is None else std, self.popart_min_std))
        return np.asarray(value, dtype=np.float32) * std + mean

    def _get_critic_output_layer(self):
        """Best-effort access to the critic output Dense layer for PopArt rescaling."""
        direct = getattr(self.critic, "output_layer", None)
        if isinstance(direct, tf.keras.layers.Dense):
            return direct
        for layer in reversed(getattr(self.critic, "layers", [])):
            if isinstance(layer, tf.keras.layers.Dense):
                return layer
        return None

    def _apply_popart_rescale(self, old_mean, old_std, new_mean, new_std):
        """Rescale critic output layer so unnormalized value predictions stay consistent."""
        if not self.popart_enabled:
            return
        layer = self._get_critic_output_layer()
        if layer is None:
            return
        try:
            weights = layer.get_weights()
            if len(weights) < 2:
                return
            kernel, bias = weights[0], weights[1]
            scale = float(old_std) / float(max(new_std, self.popart_min_std))
            kernel = np.asarray(kernel, dtype=np.float32) * scale
            bias = (
                float(old_std) * np.asarray(bias, dtype=np.float32)
                + float(old_mean)
                - float(new_mean)
            ) / float(max(new_std, self.popart_min_std))
            layer.set_weights([kernel, bias])
        except Exception as exc:
            logger.debug("PopArt rescale skipped: %s", exc)

    def _update_returns_stats(self, returns):
        """Update return running statistics and apply PopArt rescaling if enabled."""
        std_floor = self.popart_min_std if self.popart_enabled else 1e-6
        old_mean = float(self._returns_mean)
        old_std = float(max(self._returns_std, std_floor))

        self.returns_rms.update(returns)
        new_mean = float(self.returns_rms.mean)
        new_std = float(max(self.returns_rms.std, std_floor))

        self._apply_popart_rescale(old_mean, old_std, new_mean, new_std)
        self._returns_mean = new_mean
        self._returns_std = new_std

    def _apply_multi_horizon_reward_decomposition(self, raw_rewards):
        """
        Add sparse milestone bonuses from multiple sub-episode horizons.
        """
        rewards = np.asarray(raw_rewards, dtype=np.float32).reshape(-1)
        bonus = np.zeros_like(rewards, dtype=np.float32)
        if (
            rewards.size == 0
            or not self.multi_horizon_reward_enabled
            or self.multi_horizon_reward_coef <= 0.0
            or not self.multi_horizon_reward_horizons
        ):
            return rewards, bonus

        csum = np.concatenate(([0.0], np.cumsum(rewards, dtype=np.float64)))
        n = int(rewards.shape[0])
        for horizon, weight in zip(self.multi_horizon_reward_horizons, self.multi_horizon_reward_weights):
            if horizon <= 0 or weight <= 0.0:
                continue
            milestone_indices = list(range(horizon - 1, n, horizon))
            if (n - 1) not in milestone_indices:
                milestone_indices.append(n - 1)
            for idx in milestone_indices:
                start = max(0, idx - horizon + 1)
                window_return = float(csum[idx + 1] - csum[start])
                bonus[idx] += float(weight) * window_return

        shaped_rewards = rewards + float(self.multi_horizon_reward_coef) * bonus
        return shaped_rewards.astype(np.float32), bonus.astype(np.float32)

    def shape_rewards_for_update(self, raw_rewards):
        """Public wrapper used by external rollout collectors for GAE consistency."""
        return self._apply_multi_horizon_reward_decomposition(raw_rewards)

    def normalize_expert_rewards_for_update(self, raw_expert_rewards, prev_mean=None, prev_std=None, update_stats=False):
        """
        Normalize objective-expert reward streams independently.

        The c0/c1/c2 streams operate on different natural scales and their
        curriculum weights change over time, so each stream needs its own
        running statistics.
        """
        rewards = np.asarray(raw_expert_rewards, dtype=np.float32)
        if rewards.size == 0:
            return rewards
        if rewards.ndim == 1:
            rewards = rewards[:, np.newaxis]
        if rewards.shape[-1] != self.num_objective_experts:
            raise ValueError(
                f"expert reward shape mismatch: got {rewards.shape}, expected last dim {self.num_objective_experts}"
            )

        means = np.asarray(
            self._expert_reward_mean if prev_mean is None else prev_mean,
            dtype=np.float32,
        ).reshape(1, -1)
        stds = np.asarray(
            self._expert_reward_std if prev_std is None else prev_std,
            dtype=np.float32,
        ).reshape(1, -1)
        stds = np.maximum(stds, 1e-1)
        rewards_norm = np.clip((rewards - means) / stds, -5.0, 5.0).astype(np.float32)

        if update_stats:
            for expert_idx in range(self.num_objective_experts):
                self.expert_reward_rms[expert_idx].update(rewards[:, expert_idx])
                self._expert_reward_mean[expert_idx] = float(self.expert_reward_rms[expert_idx].mean)
                self._expert_reward_std[expert_idx] = float(max(self.expert_reward_rms[expert_idx].std, 1e-1))

        return rewards_norm

    def _distributional_quantile_loss(self, pred_quantiles, target_values):
        """
        Quantile Huber loss for distributional critic.

        Args:
            pred_quantiles: (batch, num_quantiles) normalized predictions
            target_values: (batch,) normalized scalar returns
        """
        pred_quantiles = _to_tensor_with_cast(pred_quantiles, tf.float32)
        target_values = _to_tensor_with_cast(target_values, tf.float32)
        target_values = tf.reshape(target_values, (-1, 1))

        num_q = tf.maximum(tf.shape(pred_quantiles)[-1], 1)
        tau = (tf.cast(tf.range(num_q), tf.float32) + 0.5) / tf.cast(num_q, tf.float32)
        tau = tf.reshape(tau, (1, -1))

        td_error = target_values - pred_quantiles
        abs_td = tf.abs(td_error)
        kappa = tf.cast(self.distributional_huber_kappa, tf.float32)
        huber = tf.where(
            abs_td <= kappa,
            0.5 * tf.square(td_error),
            kappa * (abs_td - 0.5 * kappa),
        )
        quantile_weight = tf.abs(tau - tf.cast(td_error < 0.0, tf.float32))
        return tf.reduce_mean(quantile_weight * huber)

    def _update_adaptive_cvar_coef(self, observed_cvar_proxy):
        """
        Adapt CVaR auxiliary coefficient toward target tail-risk level.
        """
        if not self.risk_aux_cvar_adaptive_enabled:
            return
        observed = float(observed_cvar_proxy)
        if not np.isfinite(observed):
            return
        error = observed - float(self.risk_aux_cvar_target)
        new_coef = float(self.risk_aux_cvar_coef) + float(self.risk_aux_cvar_adapt_lr) * error
        new_coef = float(np.clip(new_coef, self.risk_aux_cvar_min_coef, self.risk_aux_cvar_max_coef))
        self.risk_aux_cvar_coef = new_coef

    def update_lagrangian_cvar(self, rolling_cvar: float) -> float:
        """Update the Lagrangian CVaR multiplier and return the current penalty.

        The multiplier λ automatically increases when the portfolio's rolling CVaR
        violates the threshold, and decreases when it's satisfied. This provides
        continuous, adaptive pressure toward tail-risk compliance without distorting
        the reward magnitude.

        Reference: Tessler et al. (2019) — Reward Constrained Policy Optimization (RCPO)

        Args:
            rolling_cvar: Current rolling CVaR estimate (negative = bad tail risk)

        Returns:
            cvar_penalty: Dense penalty to add to step rewards (negative when violating)
        """
        if not self.lagrangian_cvar_enabled:
            return 0.0

        rolling_cvar = float(rolling_cvar)
        if not np.isfinite(rolling_cvar):
            return 0.0

        # Positive violation = CVaR worse than threshold
        violation = self.lagrangian_cvar_threshold - rolling_cvar
        # Update λ: increase when violating, decrease when satisfying
        self._lagrangian_cvar_lambda = float(np.clip(
            self._lagrangian_cvar_lambda + self.lagrangian_cvar_lr * violation,
            0.0, self.lagrangian_cvar_lambda_max
        ))

        # Return penalty (only when violating)
        if rolling_cvar < self.lagrangian_cvar_threshold:
            penalty = self._lagrangian_cvar_lambda * (rolling_cvar - self.lagrangian_cvar_threshold)
            return self.lagrangian_cvar_penalty_scale * penalty
        return 0.0

    @property
    def lagrangian_cvar_lambda(self) -> float:
        """Current Lagrangian CVaR multiplier (diagnostic)."""
        return self._lagrangian_cvar_lambda

    def _split_actor_outputs(self, actor_output):
        """Return (alpha, projection_logits or None, aux_return_preds or None) from actor output."""
        parsed = self._parse_actor_outputs(actor_output)
        return parsed["alpha"], parsed["projection_logits"], parsed["aux_return_preds"]

    def _parse_actor_outputs(self, actor_output):
        """Normalize actor outputs into a single dict for both single and mixture policies."""
        projection_logits = None
        aux_return_preds = None
        alpha = actor_output
        mixture_alpha = None
        mixture_gating_logits = None
        expert_alpha = None
        router_logits = None
        router_probs = None
        if isinstance(actor_output, dict):
            alpha = actor_output.get("alpha", actor_output.get("dirichlet_alpha", None))
            projection_logits = actor_output.get("projection_logits", actor_output.get("softmax_logits", None))
            aux_return_preds = actor_output.get("aux_return_preds", None)
            mixture_alpha = actor_output.get("mixture_alpha", None)
            mixture_gating_logits = actor_output.get("mixture_gating_logits", None)
            expert_alpha = actor_output.get("expert_alpha", None)
            router_logits = actor_output.get("router_logits", None)
            router_probs = actor_output.get("router_probs", None)
        elif isinstance(actor_output, (tuple, list)) and len(actor_output) > 0:
            alpha = actor_output[0]
            if len(actor_output) > 1:
                projection_logits = actor_output[1]

        if alpha is None:
            raise ValueError("Actor output does not contain a valid alpha tensor.")

        alpha = _to_tensor_with_cast(alpha, tf.float32)
        alpha = tf.maximum(alpha, tf.constant(1e-6, dtype=alpha.dtype))
        if projection_logits is not None:
            projection_logits = _to_tensor_with_cast(projection_logits, tf.float32)
        if aux_return_preds is not None:
            aux_return_preds = _to_tensor_with_cast(aux_return_preds, tf.float32)
        if mixture_alpha is not None:
            mixture_alpha = _to_tensor_with_cast(mixture_alpha, tf.float32)
            mixture_alpha = tf.maximum(mixture_alpha, tf.constant(1e-6, dtype=mixture_alpha.dtype))
        if mixture_gating_logits is not None:
            mixture_gating_logits = _to_tensor_with_cast(mixture_gating_logits, tf.float32)
        if expert_alpha is not None:
            expert_alpha = _to_tensor_with_cast(expert_alpha, tf.float32)
            expert_alpha = tf.maximum(expert_alpha, tf.constant(1e-6, dtype=expert_alpha.dtype))
        if router_logits is not None:
            router_logits = _to_tensor_with_cast(router_logits, tf.float32)
        if router_probs is not None:
            router_probs = _to_tensor_with_cast(router_probs, tf.float32)

        mixture_probs = None
        if mixture_alpha is not None and mixture_gating_logits is not None:
            mixture_probs = tf.nn.softmax(mixture_gating_logits, axis=-1)
            alpha = tf.reduce_sum(mixture_probs[..., tf.newaxis] * mixture_alpha, axis=1)

        return {
            "alpha": alpha,
            "projection_logits": projection_logits,
            "aux_return_preds": aux_return_preds,
            "mixture_alpha": mixture_alpha,
            "mixture_gating_logits": mixture_gating_logits,
            "mixture_probs": mixture_probs,
            "expert_alpha": expert_alpha,
            "router_logits": router_logits,
            "router_probs": router_probs,
        }

    def _parse_critic_outputs(self, critic_output, router_probs: Optional[tf.Tensor] = None):
        if isinstance(critic_output, dict):
            expert_values = critic_output.get("expert_values", None)
            if expert_values is not None:
                expert_values = _to_tensor_with_cast(expert_values, tf.float32)
                if expert_values.shape.rank == 3 and expert_values.shape[-1] == 1:
                    expert_values = tf.squeeze(expert_values, axis=-1)
                if router_probs is None:
                    if self.objective_experts_enabled:
                        mask = tf.constant(self.objective_expert_mask, dtype=expert_values.dtype)
                        mask = tf.maximum(mask, tf.cast(0.0, expert_values.dtype))
                        mask_sum = tf.reduce_sum(mask)
                        router_probs = mask[tf.newaxis, :] / tf.maximum(mask_sum, tf.cast(1e-8, expert_values.dtype))
                    else:
                        router_probs = tf.ones_like(expert_values, dtype=expert_values.dtype)
                        router_probs = router_probs / tf.cast(tf.shape(expert_values)[-1], expert_values.dtype)
                else:
                    router_probs = _to_tensor_with_cast(router_probs, expert_values.dtype)
                blended_value = tf.reduce_sum(router_probs * expert_values, axis=-1)
                return {
                    "value": blended_value,
                    "expert_values": expert_values,
                }
        value = self._critic_values_to_scalar(critic_output)
        return {
            "value": value,
            "expert_values": None,
        }

    def _gather_component_alpha(self, mixture_alpha: tf.Tensor, component_indices: tf.Tensor) -> tf.Tensor:
        """Select per-sample component alpha from (batch, K, action_dim)."""
        component_indices = tf.cast(component_indices, tf.int32)
        batch_indices = tf.range(tf.shape(mixture_alpha)[0], dtype=tf.int32)
        gather_idx = tf.stack([batch_indices, component_indices], axis=-1)
        selected = tf.gather_nd(mixture_alpha, gather_idx)
        return tf.maximum(selected, tf.constant(1e-6, dtype=selected.dtype))

    def _mixture_component_means(self, mixture_alpha: tf.Tensor) -> tf.Tensor:
        denom = tf.reduce_sum(mixture_alpha, axis=-1, keepdims=True)
        denom = tf.maximum(denom, tf.constant(1e-8, dtype=mixture_alpha.dtype))
        return mixture_alpha / denom

    def _normalize_simplex(self, weights: tf.Tensor) -> tf.Tensor:
        """Enforce strictly-positive simplex weights."""
        weights = _to_tensor_with_cast(weights, tf.float32)
        weights = tf.where(tf.math.is_finite(weights), weights, tf.zeros_like(weights))
        weights = tf.maximum(weights, tf.constant(1e-6, dtype=weights.dtype))
        denom = tf.reduce_sum(weights, axis=-1, keepdims=True)
        denom = tf.maximum(denom, tf.constant(1e-6, dtype=weights.dtype))
        return weights / denom

    def _stabilize_dirichlet_alpha(self, alpha: tf.Tensor) -> tf.Tensor:
        """Keep Dirichlet concentration parameters finite and strictly positive."""
        alpha = _to_tensor_with_cast(alpha, tf.float32)
        alpha = tf.where(tf.math.is_finite(alpha), alpha, tf.ones_like(alpha))
        alpha = tf.maximum(alpha, tf.constant(1e-4, dtype=alpha.dtype))
        alpha_cap = getattr(self.actor, "_alpha_cap", None)
        if alpha_cap is not None and np.isfinite(alpha_cap):
            alpha = tf.minimum(alpha, tf.cast(alpha_cap, alpha.dtype))
        return alpha

    def _stabilize_action_for_log_prob(self, action: tf.Tensor, eps: float = 1e-6) -> tf.Tensor:
        """Move actions away from the simplex boundary before Dirichlet log-prob evaluation."""
        action = _to_tensor_with_cast(action, tf.float32)
        action = tf.where(tf.math.is_finite(action), action, tf.zeros_like(action))
        action = tf.maximum(action, tf.cast(eps, action.dtype))
        denom = tf.maximum(tf.reduce_sum(action, axis=-1, keepdims=True), tf.cast(eps, action.dtype))
        return action / denom

    def _sanitize_log_prob_tensor(self, log_probs: tf.Tensor) -> tf.Tensor:
        """Replace non-finite log-prob entries with a large finite negative fallback."""
        log_probs = _to_tensor_with_cast(log_probs, tf.float32)
        fallback = tf.fill(tf.shape(log_probs), tf.constant(-50.0, dtype=log_probs.dtype))
        return tf.where(tf.math.is_finite(log_probs), log_probs, fallback)

    def _safe_huber(self, error: tf.Tensor, delta: float) -> tf.Tensor:
        error = _to_tensor_with_cast(error, tf.float32)
        abs_error = tf.abs(error)
        delta_t = tf.cast(delta, error.dtype)
        quadratic = tf.minimum(abs_error, delta_t)
        linear = abs_error - quadratic
        return 0.5 * tf.square(quadratic) + delta_t * linear

    def _sanitize_gradients(self, grads):
        sanitized = []
        nonfinite_tensors = 0
        nonfinite_elements = 0
        for grad in grads:
            if grad is None:
                sanitized.append(None)
                continue
            grad_t = _to_tensor_with_cast(grad, tf.float32)
            finite_mask = tf.math.is_finite(grad_t)
            finite_all = bool(tf.reduce_all(finite_mask))
            if not finite_all:
                nonfinite_tensors += 1
                nonfinite_elements += int(tf.size(grad_t).numpy() - tf.math.count_nonzero(finite_mask).numpy())
                grad_t = tf.where(finite_mask, grad_t, tf.zeros_like(grad_t))
            sanitized.append(grad_t)
        return sanitized, nonfinite_tensors, nonfinite_elements

    def _tensor_stat_summary(self, tensor: tf.Tensor) -> dict:
        arr = np.asarray(_to_tensor_with_cast(tensor, tf.float32).numpy(), dtype=np.float64)
        finite_mask = np.isfinite(arr)
        finite_vals = arr[finite_mask]
        summary = {
            "nonfinite": int(np.size(arr) - np.count_nonzero(finite_mask)),
            "shape": tuple(arr.shape),
        }
        if finite_vals.size == 0:
            summary.update({"min": np.nan, "max": np.nan, "mean": np.nan, "near_zero_frac": np.nan})
            return summary
        summary.update(
            {
                "min": float(np.min(finite_vals)),
                "max": float(np.max(finite_vals)),
                "mean": float(np.mean(finite_vals)),
                "near_zero_frac": float(np.mean(finite_vals <= 1e-5)),
            }
        )
        return summary

    def _log_nonfinite_policy_diagnostics(
        self,
        batch_states,
        batch_actions,
        batch_log_probs_old,
        batch_mixture_components_old=None,
    ) -> None:
        """Emit focused diagnostics when the policy loss becomes non-finite."""
        try:
            actor_output = self.actor(batch_states, training=False)
            actor_parts = self._parse_actor_outputs(actor_output)
            alpha = self._stabilize_dirichlet_alpha(actor_parts["alpha"])
            actions_safe = self._stabilize_action_for_log_prob(batch_actions)
            mixture_alpha = actor_parts["mixture_alpha"]
            mixture_probs = actor_parts["mixture_probs"]
            if self.mixture_dirichlet_enabled and mixture_alpha is not None and mixture_probs is not None:
                mixture_components = tf.cast(batch_mixture_components_old, tf.int32)
                alpha_for_policy = self._stabilize_dirichlet_alpha(
                    self._gather_component_alpha(mixture_alpha, mixture_components)
                )
                log_probs_new = self._sanitize_log_prob_tensor(
                    tfd.Dirichlet(alpha_for_policy).log_prob(actions_safe)
                    + tfd.Categorical(probs=mixture_probs).log_prob(mixture_components)
                )
            else:
                alpha_for_policy = alpha
                log_probs_new = self._sanitize_log_prob_tensor(
                    tfd.Dirichlet(alpha_for_policy).log_prob(actions_safe)
                )
            log_probs_old = self._sanitize_log_prob_tensor(batch_log_probs_old)
            ratio = tf.exp(tf.clip_by_value(log_probs_new - log_probs_old, -10.0, 10.0))
            action_stats = self._tensor_stat_summary(actions_safe)
            alpha_stats = self._tensor_stat_summary(alpha_for_policy)
            logp_new_stats = self._tensor_stat_summary(log_probs_new)
            logp_old_stats = self._tensor_stat_summary(log_probs_old)
            ratio_stats = self._tensor_stat_summary(ratio)
            logger.error(
                "[ERROR] Dirichlet diagnostics | action[min=%.3e max=%.3e near0=%.2f%% nonfinite=%d] | "
                "alpha[min=%.3e max=%.3e near0=%.2f%% nonfinite=%d]",
                action_stats["min"],
                action_stats["max"],
                100.0 * action_stats["near_zero_frac"],
                action_stats["nonfinite"],
                alpha_stats["min"],
                alpha_stats["max"],
                100.0 * alpha_stats["near_zero_frac"],
                alpha_stats["nonfinite"],
            )
            logger.error(
                "[ERROR] Log-prob diagnostics | old[min=%.4f max=%.4f nonfinite=%d] | "
                "new[min=%.4f max=%.4f nonfinite=%d] | ratio[min=%.4f max=%.4f nonfinite=%d]",
                logp_old_stats["min"],
                logp_old_stats["max"],
                logp_old_stats["nonfinite"],
                logp_new_stats["min"],
                logp_new_stats["max"],
                logp_new_stats["nonfinite"],
                ratio_stats["min"],
                ratio_stats["max"],
                ratio_stats["nonfinite"],
            )
            if self.objective_experts_enabled and actor_parts.get("router_probs") is not None:
                router_stats = self._tensor_stat_summary(actor_parts["router_probs"])
                logger.error(
                    "[ERROR] Router diagnostics | probs[min=%.4f max=%.4f mean=%.4f nonfinite=%d] | mask=%s",
                    router_stats["min"],
                    router_stats["max"],
                    router_stats["mean"],
                    router_stats["nonfinite"],
                    self.objective_expert_mask.tolist(),
                )
        except Exception as exc:
            logger.exception("[ERROR] Failed to compute non-finite policy diagnostics: %s", exc)

    def _project_weights_np(self, weights_np: np.ndarray) -> np.ndarray:
        """Apply lightweight long-only + cap + min-cash projection on numpy arrays."""
        arr = np.asarray(weights_np, dtype=np.float64)
        if arr.ndim == 1:
            arr = arr.reshape(1, -1)
            squeeze = True
        else:
            squeeze = False

        n_actions = int(arr.shape[-1])
        n_risky = max(0, n_actions - 1)
        max_single = float(self.dual_head_projection_max_single_position)
        min_cash = float(self.dual_head_projection_min_cash_position)

        out = np.zeros_like(arr, dtype=np.float64)
        for i in range(arr.shape[0]):
            w = np.maximum(np.nan_to_num(arr[i], nan=0.0, posinf=0.0, neginf=0.0), 0.0)
            s = float(np.sum(w))
            if s <= 1e-12:
                w = np.ones(n_actions, dtype=np.float64) / float(max(1, n_actions))
            else:
                w = w / s

            risky = w[:n_risky].copy()
            cash = max(float(w[-1]) if n_actions > 0 else 0.0, min_cash)

            max_risky_sum = min(1.0 - min_cash, n_risky * max_single)
            target_risky_sum = min(max(0.0, 1.0 - cash), max_risky_sum)
            risky_sum = float(np.sum(risky))
            if risky_sum <= 1e-12 and n_risky > 0:
                risky = np.ones(n_risky, dtype=np.float64) / float(n_risky)
                risky_sum = 1.0
            if n_risky > 0:
                risky = risky / max(risky_sum, 1e-12) * target_risky_sum
                risky = np.clip(risky, 0.0, max_single)
                risky_sum = float(np.sum(risky))
                if risky_sum > max_risky_sum and risky_sum > 1e-12:
                    risky *= (max_risky_sum / risky_sum)
                    risky_sum = float(np.sum(risky))
            cash = max(min_cash, 1.0 - risky_sum)
            merged = np.concatenate([risky, np.array([cash], dtype=np.float64)], axis=0)
            merged = np.maximum(merged, 1e-8)
            merged /= max(float(np.sum(merged)), 1e-8)
            out[i] = merged

        if squeeze:
            return out[0].astype(np.float32)
        return out.astype(np.float32)

    def _get_dual_head_rho(
        self,
        *,
        deterministic: bool,
        stochastic: bool,
        use_eval_settings: bool,
    ) -> float:
        if not self.dual_head_enabled:
            return 0.0
        if use_eval_settings:
            if deterministic:
                return float(self.dual_head_eval_deterministic_rho)
            if stochastic:
                return float(self.dual_head_eval_stochastic_rho)

        rho = float(self.dual_head_blend_schedule[0]["rho"])
        for entry in self.dual_head_blend_schedule:
            if self._global_step >= int(entry["threshold"]):
                rho = float(entry["rho"])
            else:
                break
        return float(np.clip(rho, 0.0, 1.0))

    def _parse_threshold_coef_schedule(self, schedule_cfg, *, fallback_coef: float) -> list:
        """Parse a simple threshold->coef schedule used by mixture regularizers."""
        parsed = []
        if isinstance(schedule_cfg, (list, tuple)):
            for entry in schedule_cfg:
                if not isinstance(entry, dict):
                    continue
                try:
                    threshold = int(entry.get('threshold', 0))
                    coef = float(entry.get('coef', fallback_coef))
                except (TypeError, ValueError):
                    continue
                parsed.append({"threshold": max(0, threshold), "coef": max(0.0, coef)})
        if not parsed:
            parsed = [{"threshold": 0, "coef": max(0.0, float(fallback_coef))}]
        parsed.sort(key=lambda item: item["threshold"])
        if parsed[0]["threshold"] != 0:
            parsed.insert(0, {"threshold": 0, "coef": parsed[0]["coef"]})
        return parsed

    def _get_threshold_coef(self, schedule: list, fallback_coef: float) -> float:
        coef = float(fallback_coef)
        for entry in schedule:
            if self._global_step >= int(entry["threshold"]):
                coef = float(entry["coef"])
            else:
                break
        return max(0.0, coef)

    def _blend_action_with_projection(
        self,
        dirichlet_action: tf.Tensor,
        projection_logits: Optional[tf.Tensor],
        *,
        deterministic: bool,
        stochastic: bool,
        use_eval_settings: bool,
    ) -> tf.Tensor:
        """Blend Dirichlet action with softmax/projection action using rho schedule."""
        action = _to_tensor_with_cast(dirichlet_action, tf.float32)
        if (not self.dual_head_enabled) or projection_logits is None:
            return self._normalize_simplex(action)

        rho = self._get_dual_head_rho(
            deterministic=deterministic,
            stochastic=stochastic,
            use_eval_settings=use_eval_settings,
        )
        if rho <= 0.0:
            return self._normalize_simplex(action)

        proj_weights = tf.nn.softmax(_to_tensor_with_cast(projection_logits, tf.float32), axis=-1)
        proj_weights = self._normalize_simplex(proj_weights)
        if self.dual_head_projection_use_constraints:
            projected_np = self._project_weights_np(proj_weights.numpy())
            proj_weights = _to_tensor_with_cast(projected_np, tf.float32)

        blended = (1.0 - rho) * self._normalize_simplex(action) + rho * proj_weights
        return self._normalize_simplex(blended)

    def _deterministic_dirichlet_action(self, alpha: tf.Tensor, evaluation_mode: str) -> tf.Tensor:
        """Return deterministic action from Dirichlet alphas."""
        dirichlet = tfd.Dirichlet(alpha)
        if evaluation_mode == 'mean':
            return dirichlet.mean()
        if evaluation_mode == 'mode':
            min_alpha = tf.reduce_min(alpha, axis=-1, keepdims=True)
            use_formula = min_alpha > 1.0
            sum_alpha = tf.reduce_sum(alpha, axis=-1, keepdims=True)
            k = tf.cast(tf.shape(alpha)[-1], alpha.dtype)
            mode_formula = (alpha - 1.0) / (sum_alpha - k)
            max_indices = tf.argmax(alpha, axis=-1)
            mode_vertex = tf.one_hot(max_indices, depth=tf.shape(alpha)[-1], dtype=alpha.dtype)
            return tf.where(use_formula, mode_formula, mode_vertex)
        if evaluation_mode == 'mean_plus_noise':
            mean_val = dirichlet.mean()
            noise = tf.random.normal(shape=tf.shape(mean_val), mean=0.0, stddev=0.005)
            action = mean_val + noise
            action = tf.maximum(action, 1e-6)
            return action / tf.reduce_sum(action, axis=-1, keepdims=True)
        return dirichlet.mean()

    def _select_mixture_component(
        self,
        mixture_probs: tf.Tensor,
        *,
        deterministic: bool,
        stochastic: bool,
    ) -> tf.Tensor:
        """Select component indices for mixture policy."""
        categorical = tfd.Categorical(probs=mixture_probs)
        if stochastic:
            return categorical.sample()
        if deterministic and self.mixture_dirichlet_eval_mode == "weighted_component_mean":
            return tf.argmax(mixture_probs, axis=-1, output_type=tf.int32)
        if deterministic:
            return tf.argmax(mixture_probs, axis=-1, output_type=tf.int32)
        return categorical.sample()
    
    def get_action_and_value(self, state, deterministic=False, stochastic=False, evaluation_mode='mean_plus_noise'):
        """
        Get action and value estimate for a given state.
        
        Args:
            state: Current state (various shapes supported)
            deterministic: If True, use deterministic evaluation strategy
            stochastic: If True, force stochastic sampling (overrides deterministic)
            evaluation_mode: Strategy for deterministic evaluation ('mean', 'mode', 'mean_plus_noise')
            
        Returns:
            Tuple of (action, log_prob, value)
        """
        # Prepare state input and check if we need to squeeze output
        if self.is_sequential:
            sequence = self._build_sequence(state)
            self._latest_sequence = np.array(sequence, copy=True)
            state_input, needs_squeeze = self.prepare_state_input(sequence)
        else:
            self._latest_sequence = None
            state_input, needs_squeeze = self.prepare_state_input(state)
        
        # Get actor outputs (alpha + optional softmax/projection logits)
        actor_output = self.actor(state_input, training=False)
        actor_parts = self._parse_actor_outputs(actor_output)
        alpha = self._stabilize_dirichlet_alpha(actor_parts["alpha"])
        projection_logits = actor_parts["projection_logits"]
        mixture_alpha = actor_parts["mixture_alpha"]
        mixture_probs = actor_parts["mixture_probs"]
        expert_alpha = actor_parts["expert_alpha"]
        if expert_alpha is not None:
            expert_alpha = self._stabilize_dirichlet_alpha(expert_alpha)
        router_probs = actor_parts["router_probs"]

        selected_component = None
        if self.mixture_dirichlet_enabled and mixture_alpha is not None and mixture_probs is not None:
            selected_component = self._select_mixture_component(
                mixture_probs,
                deterministic=bool(deterministic and not stochastic),
                stochastic=bool(stochastic),
            )
            alpha_for_action = self._gather_component_alpha(mixture_alpha, selected_component)
        else:
            alpha_for_action = alpha

        alpha_for_action = self._stabilize_dirichlet_alpha(alpha_for_action)
        dirichlet = tfd.Dirichlet(alpha_for_action)
        if stochastic:
            action = dirichlet.sample()
        elif deterministic:
            action = self._deterministic_dirichlet_action(alpha_for_action, evaluation_mode)
        else:
            action = dirichlet.sample()

        action = self._blend_action_with_projection(
            action,
            projection_logits,
            deterministic=bool(deterministic and not stochastic),
            stochastic=bool(stochastic),
            use_eval_settings=bool(deterministic or stochastic),
        )
        action = self._stabilize_action_for_log_prob(action)
        
        log_prob = self._sanitize_log_prob_tensor(dirichlet.log_prob(action))
        if selected_component is not None and mixture_probs is not None:
            categorical = tfd.Categorical(probs=mixture_probs)
            log_prob = self._sanitize_log_prob_tensor(log_prob + categorical.log_prob(selected_component))
        
        # Get value estimate
        critic_output = self.critic(state_input, training=False)
        critic_parts = self._parse_critic_outputs(critic_output, router_probs=router_probs)
        value = critic_parts["value"]
        value = self._denormalize_value(value)

        expert_log_probs = None
        expert_values = critic_parts["expert_values"]
        if self.objective_experts_enabled and expert_alpha is not None:
            expert_log_probs = self._sanitize_log_prob_tensor(
                tfd.Dirichlet(expert_alpha).log_prob(action[:, tf.newaxis, :])
            )

        # Squeeze batch dimension if needed
        if needs_squeeze:
            action = tf.squeeze(action, 0)
            log_prob = tf.squeeze(log_prob, 0)
            value = tf.squeeze(value, 0)
            if selected_component is not None:
                selected_component = tf.squeeze(selected_component, 0)
            if expert_log_probs is not None:
                expert_log_probs = tf.squeeze(expert_log_probs, 0)
            if expert_values is not None:
                expert_values = tf.squeeze(expert_values, 0)
            if router_probs is not None:
                router_probs = tf.squeeze(router_probs, 0)

        self._latest_action_metadata = {
            "mixture_component": None if selected_component is None else int(np.asarray(selected_component.numpy()).reshape(-1)[0]),
            "expert_log_probs": None if expert_log_probs is None else np.asarray(expert_log_probs.numpy(), dtype=np.float32),
            "expert_values": None if expert_values is None else np.asarray(expert_values.numpy(), dtype=np.float32),
            "router_probs": None if router_probs is None else np.asarray(router_probs.numpy(), dtype=np.float32),
        }
        
        return action, log_prob, value

    def get_action_and_value_batch(
        self,
        states,
        *,
        sequence_histories=None,
        deterministic=False,
        stochastic=False,
        evaluation_mode='mean_plus_noise',
    ):
        """
        Batched action/value inference for multiple environment states.

        Args:
            states: Iterable of state observations
            sequence_histories: Per-env history buffers for sequential models
            deterministic: If True, use deterministic policy mode
            stochastic: If True, force stochastic sampling
            evaluation_mode: Deterministic policy mode

        Returns:
            tuple:
                actions_np: (batch, num_actions)
                log_probs_np: (batch,)
                values_np: (batch,)
                states_for_storage: list of preprocessed states for memory
        """
        states_list = list(states)
        batch_size = len(states_list)
        if batch_size == 0:
            raise ValueError("get_action_and_value_batch() received empty states list.")

        if self.is_sequential:
            if sequence_histories is None or len(sequence_histories) != batch_size:
                raise ValueError(
                    "sequence_histories must be provided with one history per state for sequential batching."
                )
            sequences = [
                self.build_sequence_from_history(sequence_histories[i], states_list[i], mutate=True)
                for i in range(batch_size)
            ]
            prepared_state, _ = self.prepare_state_input(np.asarray(sequences, dtype=np.float32))
            states_for_storage = [np.asarray(seq, dtype=np.float32) for seq in sequences]
        else:
            prepared_state, _ = self.prepare_state_input(np.asarray(states_list, dtype=np.float32))
            states_for_storage = [np.asarray(state, dtype=np.float32) for state in states_list]

        actor_output = self.actor(prepared_state, training=False)
        actor_parts = self._parse_actor_outputs(actor_output)
        alpha = self._stabilize_dirichlet_alpha(actor_parts["alpha"])
        projection_logits = actor_parts["projection_logits"]
        mixture_alpha = actor_parts["mixture_alpha"]
        mixture_probs = actor_parts["mixture_probs"]
        expert_alpha = actor_parts["expert_alpha"]
        if expert_alpha is not None:
            expert_alpha = self._stabilize_dirichlet_alpha(expert_alpha)
        router_probs = actor_parts["router_probs"]

        selected_components = None
        if self.mixture_dirichlet_enabled and mixture_alpha is not None and mixture_probs is not None:
            selected_components = self._select_mixture_component(
                mixture_probs,
                deterministic=bool(deterministic and not stochastic),
                stochastic=bool(stochastic),
            )
            alpha_for_action = self._gather_component_alpha(mixture_alpha, selected_components)
        else:
            alpha_for_action = alpha

        alpha_for_action = self._stabilize_dirichlet_alpha(alpha_for_action)
        dirichlet = tfd.Dirichlet(alpha_for_action)

        if stochastic:
            action = dirichlet.sample()
        elif deterministic:
            action = self._deterministic_dirichlet_action(alpha_for_action, evaluation_mode)
        else:
            action = dirichlet.sample()

        action = self._blend_action_with_projection(
            action,
            projection_logits,
            deterministic=bool(deterministic and not stochastic),
            stochastic=bool(stochastic),
            use_eval_settings=bool(deterministic or stochastic),
        )
        action = self._stabilize_action_for_log_prob(action)

        log_prob = self._sanitize_log_prob_tensor(dirichlet.log_prob(action))
        if selected_components is not None and mixture_probs is not None:
            categorical = tfd.Categorical(probs=mixture_probs)
            log_prob = self._sanitize_log_prob_tensor(log_prob + categorical.log_prob(selected_components))
        critic_output = self.critic(prepared_state, training=False)
        critic_parts = self._parse_critic_outputs(critic_output, router_probs=router_probs)
        value = critic_parts["value"]
        value = self._denormalize_value(value)

        expert_log_probs = None
        if self.objective_experts_enabled and expert_alpha is not None:
            expert_log_probs = self._sanitize_log_prob_tensor(
                tfd.Dirichlet(expert_alpha).log_prob(action[:, tf.newaxis, :])
            )

        self._latest_batch_action_metadata = {
            "mixture_components": None if selected_components is None else np.asarray(selected_components.numpy(), dtype=np.int32),
            "expert_log_probs": None if expert_log_probs is None else np.asarray(expert_log_probs.numpy(), dtype=np.float32),
            "expert_values": None if critic_parts["expert_values"] is None else np.asarray(critic_parts["expert_values"].numpy(), dtype=np.float32),
            "router_probs": None if router_probs is None else np.asarray(router_probs.numpy(), dtype=np.float32),
        }

        return (
            np.asarray(action.numpy(), dtype=np.float32),
            np.asarray(log_prob.numpy(), dtype=np.float32),
            np.asarray(value.numpy(), dtype=np.float32),
            states_for_storage,
        )
    
    def store_transition(
        self,
        state,
        action,
        log_prob,
        reward,
        value,
        done,
        mixture_component=None,
        reward_components=None,
        expert_values=None,
        expert_log_probs=None,
        router_probs=None,
    ):
        """
        Store a transition in memory with shape normalization.
        
        CRITICAL: Parameter order is log_prob BEFORE reward!
        
        Args:
            state: Current state
            action: Action taken  
            log_prob: Log probability of action (BEFORE reward!)
            reward: Reward received (AFTER log_prob!)
            value: Value estimate
            done: Whether episode is done
        """
        # Normalize shapes for storage
        if self.is_sequential:
            if self._latest_sequence is not None:
                state_to_store = np.array(self._latest_sequence, copy=True)
                self._latest_sequence = None
            else:
                state_to_store = self._build_sequence(state)
        else:
            state_to_store = state

        state = self._normalize_state_shape(state_to_store)
        action = self._normalize_action_shape(action)
        
        # Validate types
        assert isinstance(log_prob, (int, float, np.number, tf.Tensor)), \
            f"log_prob must be numeric, got {type(log_prob)}"
        assert isinstance(reward, (int, float, np.number)), \
            f"reward must be numeric, got {type(reward)}"
        assert isinstance(value, (int, float, np.number, tf.Tensor)), \
            f"value must be numeric, got {type(value)}"
        assert isinstance(done, (bool, np.bool_)), \
            f"done must be boolean, got {type(done)}"
        
        # Convert to Python native types
        if isinstance(log_prob, tf.Tensor):
            log_prob = float(log_prob.numpy())
        if isinstance(value, tf.Tensor):
            value = float(value.numpy())
        if mixture_component is None:
            mixture_component = self._latest_action_metadata.get("mixture_component", -1)
        try:
            mixture_component = int(mixture_component)
        except Exception:
            mixture_component = -1
        if expert_values is None:
            expert_values = self._latest_action_metadata.get("expert_values", None)
        if expert_log_probs is None:
            expert_log_probs = self._latest_action_metadata.get("expert_log_probs", None)
        if router_probs is None:
            router_probs = self._latest_action_metadata.get("router_probs", None)
        if reward_components is None:
            reward_components = {}
        expert_reward_vector = np.zeros((self.num_objective_experts,), dtype=np.float32)
        if self.objective_experts_enabled:
            benchmark_total = float(reward_components.get("benchmark_total", 0.0) or 0.0)
            expert_reward_vector = np.asarray(
                [
                    float(reward_components.get("base", 0.0) or 0.0),
                    float(reward_components.get("dsr", 0.0) or 0.0) + benchmark_total,
                    float(reward_components.get("turnover", 0.0) or 0.0),
                ],
                dtype=np.float32,
            )
        expert_values_arr = np.asarray(
            expert_values if expert_values is not None else np.zeros((self.num_objective_experts,), dtype=np.float32),
            dtype=np.float32,
        ).reshape(-1)
        expert_log_probs_arr = np.asarray(
            expert_log_probs if expert_log_probs is not None else np.zeros((self.num_objective_experts,), dtype=np.float32),
            dtype=np.float32,
        ).reshape(-1)
        router_probs_arr = np.asarray(
            router_probs if router_probs is not None else np.zeros((self.num_objective_experts,), dtype=np.float32),
            dtype=np.float32,
        ).reshape(-1)
        if expert_values_arr.size != self.num_objective_experts:
            expert_values_arr = np.resize(expert_values_arr, self.num_objective_experts).astype(np.float32)
        if expert_log_probs_arr.size != self.num_objective_experts:
            expert_log_probs_arr = np.resize(expert_log_probs_arr, self.num_objective_experts).astype(np.float32)
        if router_probs_arr.size != self.num_objective_experts:
            router_probs_arr = np.resize(router_probs_arr, self.num_objective_experts).astype(np.float32)

        # Store in memory
        self.memory['states'].append(state)
        self.memory['actions'].append(action)
        self.memory['log_probs'].append(float(log_prob))
        self.memory['mixture_components'].append(mixture_component)
        self.memory['rewards'].append(float(reward))
        self.memory['values'].append(float(value))
        self.memory['expert_rewards'].append(expert_reward_vector)
        self.memory['expert_values'].append(expert_values_arr)
        self.memory['expert_log_probs'].append(expert_log_probs_arr)
        self.memory['router_probs'].append(router_probs_arr)
        self.memory['dones'].append(bool(done))

        self._global_step += 1
        if self.max_total_timesteps > 0:
            self.set_dirichlet_progress(self._global_step / self.max_total_timesteps)
        
        if done:
            self.reset_state_history()
    
    def _normalize_state_shape(self, state):
        """
        Ensure state has correct shape for storage.
        
        Args:
            state: State tensor or array
            
        Returns:
            Normalized state as numpy array
        """
        if isinstance(state, tf.Tensor):
            state = state.numpy()
        
        if self.is_sequential:
            # Sequential: should be (timesteps, features)
            if state.ndim == 3 and state.shape[0] == 1:
                # Remove batch dimension: (1, timesteps, features) => (timesteps, features)
                state = state.squeeze(0)
            elif state.ndim != 2:
                raise ValueError(
                    f"Invalid state shape for sequential architecture: {state.shape}. "
                    f"Expected (timesteps, features) or (1, timesteps, features)"
                )
        else:
            # Non-sequential: should be (features,)
            if state.ndim == 2 and state.shape[0] == 1:
                # Remove batch dimension: (1, features) => (features,)
                state = state.squeeze(0)
            elif state.ndim != 1:
                raise ValueError(
                    f"Invalid state shape for non-sequential architecture: {state.shape}. "
                    f"Expected (features,) or (1, features)"
                )
        
        return state.astype(np.float32)
    
    def _normalize_action_shape(self, action):
        """
        Ensure action has correct shape for storage.
        
        Args:
            action: Action tensor or array
            
        Returns:
            Normalized action as numpy array
        """
        if isinstance(action, tf.Tensor):
            action = action.numpy()
        
        # Actions should always be (num_actions,)
        if action.ndim == 2 and action.shape[0] == 1:
            # Remove batch dimension: (1, num_actions) => (num_actions,)
            action = action.squeeze(0)
        elif action.ndim != 1:
            raise ValueError(f"Invalid action shape: {action.shape}. Expected (num_actions,) or (1, num_actions)")
        
        assert action.shape[0] == self.num_actions, \
            f"Action size mismatch: got {action.shape[0]}, expected {self.num_actions}"
        
        return action.astype(np.float32)
    
    def clear_memory(self):
        """Clear the memory buffer."""
        for key in self.memory:
            # Handle both lists and numpy arrays
            if isinstance(self.memory[key], list):
                self.memory[key].clear()
            else:
                # For numpy arrays or other types, reinitialize as empty list
                self.memory[key] = []
    
    def compute_gae(self, rewards, values, dones, next_value=0.0):
        """
        Compute Generalized Advantage Estimation (GAE).
        
        Args:
            rewards: List of rewards
            values: List of value estimates
            dones: List of done flags
            next_value: Value estimate for the next state (for bootstrapping)
            
        Returns:
            tuple: (advantages, returns) as numpy arrays
        """
        advantages = []
        gae = 0
        
        # Convert to numpy for easier manipulation
        rewards = np.array(rewards)
        values = np.array(values)
        dones = np.array(dones)
        
        # Add next_value to values for bootstrapping
        values_with_next = np.append(values, next_value)
        
        # Compute GAE backwards
        for t in reversed(range(len(rewards))):
            if t == len(rewards) - 1:
                next_non_terminal = 1.0 - dones[t]
                next_value = next_value
            else:
                next_non_terminal = 1.0 - dones[t]
                next_value = values_with_next[t + 1]
            
            # TD error
            delta = rewards[t] + self.gamma * next_value * next_non_terminal - values[t]
            
            # GAE
            gae = delta + self.gamma * self.gae_lambda * next_non_terminal * gae
            advantages.insert(0, gae)
        
        advantages = np.array(advantages)
        returns = advantages + values
        
        # DIAGNOSTIC: Check TD errors to understand advantage computation
        td_errors = []
        for t in range(len(rewards)):
            if t == len(rewards) - 1:
                next_non_terminal = 1.0 - dones[t]
                next_val = next_value
            else:
                next_non_terminal = 1.0 - dones[t]
                next_val = values_with_next[t + 1]
            delta = rewards[t] + self.gamma * next_val * next_non_terminal - values[t]
            td_errors.append(delta)
        td_errors = np.array(td_errors)
        
        # Print TD error statistics (only if called from update, not every forward pass)
        # We'll check this by seeing if we're computing for multiple timesteps
        if self.debug_prints and len(rewards) > 10:
            print(f"\n🎯 TD ERROR DIAGNOSTICS (GAE computation):")
            print(f"   TD errors: min={td_errors.min():.6f}, max={td_errors.max():.6f}")
            print(f"   TD error mean: {np.mean(td_errors):.6f}, std: {np.std(td_errors):.6f}")
            print(f"   Abs TD error mean: {np.mean(np.abs(td_errors)):.6f}")
            if np.std(td_errors) < 0.01:
                print(f"   [WARN]  WARNING: TD errors have very low variance! Critic may be overfitting.")
        
        return advantages, returns
    
    def _extract_asset_return_proxy(self, states):
        """
        Extract a per-asset return proxy from structured states.

        Uses the latest timestep and configured feature index from the per-asset tensor:
          states['asset'] shape: (batch, timesteps, num_assets, asset_feature_dim)
        """
        if not isinstance(states, dict):
            return None

        asset = states.get("asset")
        if asset is None:
            return None

        asset = _to_tensor_with_cast(asset, tf.float32)
        if asset.shape.rank != 4:
            return None
        if asset.shape[-1] == 0:
            return None

        latest = asset[:, -1, :, :]  # (batch, num_assets, feature_dim)
        feature_dim = tf.shape(latest)[-1]
        safe_idx = tf.clip_by_value(
            tf.constant(self.risk_aux_return_feature_index, dtype=tf.int32),
            0,
            tf.maximum(feature_dim - 1, 0),
        )
        return tf.gather(latest, safe_idx, axis=-1)  # (batch, num_assets)

    def _compute_mvo_target_weights(self, asset_returns: tf.Tensor):
        """
        Compute a simple long-only MVO target from batch return proxies.

        Returns:
            target_risky_weights: (num_assets,)
            target_cash_weight: scalar
        """
        asset_returns = _to_tensor_with_cast(asset_returns, tf.float32)
        n_obs = tf.cast(tf.shape(asset_returns)[0], tf.float32)
        n_assets = tf.shape(asset_returns)[1]

        mu = tf.reduce_mean(asset_returns, axis=0)  # (num_assets,)
        centered = asset_returns - mu
        denom = tf.maximum(n_obs - 1.0, 1.0)
        cov = tf.matmul(centered, centered, transpose_a=True) / denom

        ridge = tf.cast(self.risk_aux_mvo_cov_ridge, tf.float32)
        cov_reg = cov + ridge * tf.eye(n_assets, dtype=tf.float32)
        inv_cov = tf.linalg.pinv(cov_reg)

        raw = tf.linalg.matvec(inv_cov, mu)
        if self.risk_aux_mvo_long_only:
            raw = tf.nn.relu(raw)

        eps = tf.constant(1e-8, dtype=tf.float32)
        raw_sum = tf.reduce_sum(raw)
        equal = tf.ones_like(raw) / tf.cast(n_assets, tf.float32)
        normalized = tf.where(raw_sum > eps, raw / (raw_sum + eps), equal)

        risky_budget = tf.constant(self.risk_aux_mvo_risky_budget, dtype=tf.float32)
        target_risky = normalized * risky_budget
        target_cash = 1.0 - risky_budget
        return target_risky, target_cash

    def _compute_risk_aux_loss(self, states, alpha):
        """
        Compute optional risk-aware actor auxiliaries.

        Components:
          - Sharpe surrogate: maximize batch Sharpe of actor-implied one-step proxy returns.
          - MVO regularizer: pull actor risky weights toward a long-only MVO target.
          - CVaR tail-risk penalty: minimize expected loss in worst alpha-fraction of samples.
        """
        zero = tf.constant(0.0, dtype=tf.float32)
        if not self.use_risk_aux_loss:
            return zero, zero, zero, zero, zero, zero

        asset_returns = self._extract_asset_return_proxy(states)
        if asset_returns is None:
            return zero, zero, zero, zero, zero, zero

        alpha = _to_tensor_with_cast(alpha, tf.float32)
        weights = alpha / tf.maximum(tf.reduce_sum(alpha, axis=-1, keepdims=True), 1e-8)

        # Support both policy output formats:
        #   1) risky-only simplex of size num_assets (cash is residual)
        #   2) risky+cash simplex of size num_assets+1
        asset_dim = tf.shape(asset_returns)[-1]
        weight_dim = tf.shape(weights)[-1]
        shared_dim = tf.minimum(weight_dim, asset_dim)
        risky_weights = weights[:, :shared_dim]
        # If actor emits fewer risky dimensions than asset returns, pad with zeros.
        pad_dim = tf.maximum(asset_dim - shared_dim, 0)
        risky_weights = tf.pad(risky_weights, paddings=[[0, 0], [0, pad_dim]])
        risky_weights = risky_weights[:, :asset_dim]

        def _cash_from_explicit():
            return weights[:, asset_dim]

        def _cash_from_residual():
            return tf.maximum(1.0 - tf.reduce_sum(risky_weights, axis=-1), 0.0)

        cash_weights = tf.cond(weight_dim > asset_dim, _cash_from_explicit, _cash_from_residual)
        cash_ret = tf.constant(self.risk_aux_cash_return, dtype=tf.float32)
        portfolio_proxy_returns = tf.reduce_sum(risky_weights * asset_returns, axis=-1) + cash_weights * cash_ret

        sharpe_proxy = tf.constant(0.0, dtype=tf.float32)
        sharpe_loss = tf.constant(0.0, dtype=tf.float32)
        if self.risk_aux_sharpe_coef > 0.0:
            mu_p = tf.reduce_mean(portfolio_proxy_returns)
            sigma_p = tf.math.reduce_std(portfolio_proxy_returns)
            sharpe_proxy = mu_p / (sigma_p + 1e-6)
            sharpe_loss = -tf.constant(self.risk_aux_sharpe_coef, dtype=tf.float32) * sharpe_proxy

        mvo_loss = tf.constant(0.0, dtype=tf.float32)
        if self.risk_aux_mvo_coef > 0.0:
            target_risky, target_cash = self._compute_mvo_target_weights(asset_returns)
            risky_mse = tf.reduce_mean(tf.square(risky_weights - target_risky[tf.newaxis, :]))
            cash_mse = tf.reduce_mean(tf.square(cash_weights - target_cash))
            mvo_loss = tf.constant(self.risk_aux_mvo_coef, dtype=tf.float32) * (risky_mse + cash_mse)

        cvar_proxy = tf.constant(0.0, dtype=tf.float32)
        cvar_loss = tf.constant(0.0, dtype=tf.float32)
        if self.risk_aux_cvar_coef > 0.0:
            # Tail losses: larger values mean worse outcomes. Penalize expected tail loss (CVaR).
            losses = -portfolio_proxy_returns
            sorted_losses = tf.sort(losses, direction="DESCENDING")
            n_samples = tf.shape(sorted_losses)[0]
            n_samples_safe = tf.maximum(n_samples, 1)
            tail_frac = tf.constant(self.risk_aux_cvar_alpha, dtype=tf.float32)
            tail_count = tf.cast(
                tf.math.ceil(tail_frac * tf.cast(n_samples_safe, tf.float32)),
                tf.int32,
            )
            tail_count = tf.clip_by_value(tail_count, 1, n_samples_safe)
            tail_losses = sorted_losses[:tail_count]
            cvar_proxy = tf.reduce_mean(tail_losses)
            cvar_loss = tf.constant(self.risk_aux_cvar_coef, dtype=tf.float32) * cvar_proxy

        total_aux = sharpe_loss + mvo_loss + cvar_loss
        return total_aux, sharpe_proxy, sharpe_loss, mvo_loss, cvar_proxy, cvar_loss

    # @tf.function  # DISABLED: Causes weight caching issues with PPO ratio stuck at 1.0
    def _actor_loss(
        self,
        states,
        actions,
        log_probs_old,
        advantages,
        mixture_components=None,
        expert_log_probs_old=None,
        expert_advantages=None,
    ):
        """
        Compute the actor loss (PPO clipped objective + entropy bonus).
        
        Args:
            states: Batch of states
            actions: Batch of actions
            log_probs_old: Old log probabilities
            advantages: Advantage estimates
            
        Returns:
            tuple with PPO losses/diagnostics + optional risk-aware auxiliaries
        """
        # Get current policy distribution
        actor_output = self.actor(states, training=True)
        actor_parts = self._parse_actor_outputs(actor_output)
        alpha = self._stabilize_dirichlet_alpha(actor_parts["alpha"])
        projection_logits = actor_parts["projection_logits"]
        aux_return_preds = actor_parts["aux_return_preds"]
        mixture_alpha = actor_parts["mixture_alpha"]
        if mixture_alpha is not None:
            mixture_alpha = self._stabilize_dirichlet_alpha(mixture_alpha)
        mixture_gating_logits = actor_parts["mixture_gating_logits"]
        mixture_probs = actor_parts["mixture_probs"]
        expert_alpha = actor_parts["expert_alpha"]
        if expert_alpha is not None:
            expert_alpha = self._stabilize_dirichlet_alpha(expert_alpha)
        router_probs = actor_parts["router_probs"]
        actions = self._stabilize_action_for_log_prob(actions)
        log_probs_old = self._sanitize_log_prob_tensor(log_probs_old)

        mixture_balance_loss = tf.constant(0.0, dtype=tf.float32)
        mixture_separation_loss = tf.constant(0.0, dtype=tf.float32)
        mixture_component_dispersion_loss = tf.constant(0.0, dtype=tf.float32)
        mixture_gating_entropy = tf.constant(0.0, dtype=tf.float32)

        if self.mixture_dirichlet_enabled and mixture_alpha is not None and mixture_probs is not None:
            if mixture_components is None:
                raise ValueError("mixture_components must be provided when mixture_dirichlet_enabled=True")
            mixture_components = tf.cast(mixture_components, tf.int32)
            alpha_for_policy = self._gather_component_alpha(mixture_alpha, mixture_components)
            alpha_for_policy = self._stabilize_dirichlet_alpha(alpha_for_policy)
            dirichlet = tfd.Dirichlet(alpha_for_policy)
            categorical = tfd.Categorical(probs=mixture_probs)
            log_probs_new = self._sanitize_log_prob_tensor(
                dirichlet.log_prob(actions) + categorical.log_prob(mixture_components)
            )
            component_entropies = tfd.Dirichlet(mixture_alpha).entropy()
            mixture_gating_entropy = tf.reduce_mean(categorical.entropy())
            gating_entropy_coef = tf.constant(
                self._get_threshold_coef(
                    self.mixture_dirichlet_entropy_schedule,
                    self.mixture_dirichlet_entropy_coef,
                ),
                dtype=tf.float32,
            )
            entropy = tf.reduce_mean(
                tf.reduce_sum(mixture_probs * component_entropies, axis=-1)
                + gating_entropy_coef * categorical.entropy()
            )
            mean_probs = tf.reduce_mean(mixture_probs, axis=0)
            uniform_probs = tf.fill(
                tf.shape(mean_probs),
                tf.cast(1.0 / tf.cast(tf.shape(mean_probs)[0], tf.float32), tf.float32),
            )
            balance_coef = tf.constant(
                self._get_threshold_coef(
                    self.mixture_dirichlet_balance_schedule,
                    self.mixture_dirichlet_balance_coef,
                ),
                dtype=tf.float32,
            )
            mixture_balance_loss = (
                balance_coef
                * tf.reduce_sum(
                    mean_probs * (
                        tf.math.log(tf.maximum(mean_probs, 1e-8))
                        - tf.math.log(tf.maximum(uniform_probs, 1e-8))
                    )
                )
            )
            component_means = self._mixture_component_means(mixture_alpha)
            comp_i = tf.expand_dims(component_means, axis=2)
            comp_j = tf.expand_dims(component_means, axis=1)
            pairwise_dist = tf.reduce_mean(tf.abs(comp_i - comp_j), axis=-1)
            num_components = tf.shape(pairwise_dist)[-1]
            off_diag_mask = 1.0 - tf.eye(num_components, dtype=pairwise_dist.dtype)
            mean_pairwise_dist = tf.reduce_sum(pairwise_dist * off_diag_mask, axis=[1, 2]) / tf.maximum(
                tf.reduce_sum(off_diag_mask), 1.0
            )
            mixture_separation_loss = (
                tf.constant(self.mixture_dirichlet_separation_coef, dtype=tf.float32)
                * tf.reduce_mean(
                    tf.maximum(
                        tf.constant(self.mixture_component_min_distance, dtype=tf.float32)
                        - mean_pairwise_dist,
                        0.0,
                    )
                )
            )
            if self.mixture_component_dispersion_coef > 0.0:
                component_std = tf.math.reduce_std(component_means, axis=-1)
                component_shortfall = tf.maximum(
                    tf.constant(self.mixture_component_target_std, dtype=tf.float32) - component_std,
                    0.0,
                )
                mixture_component_dispersion_loss = (
                    tf.constant(self.mixture_component_dispersion_coef, dtype=tf.float32)
                    * tf.reduce_mean(component_shortfall)
                )
        else:
            dirichlet = tfd.Dirichlet(alpha)
            log_probs_new = self._sanitize_log_prob_tensor(dirichlet.log_prob(actions))
            entropy = tf.reduce_mean(dirichlet.entropy())

        objective_expert_loss = tf.constant(0.0, dtype=tf.float32)
        objective_router_entropy = tf.constant(0.0, dtype=tf.float32)
        objective_diversity_loss = tf.constant(0.0, dtype=tf.float32)
        if self.objective_experts_enabled and expert_alpha is not None:
            expert_mask = tf.constant(self.objective_expert_mask, dtype=tf.float32)[tf.newaxis, :]
            active_expert_count = tf.maximum(tf.reduce_sum(expert_mask), 1.0)
            expert_dist = tfd.Dirichlet(expert_alpha)
            if expert_advantages is not None:
                expert_actions = self._stabilize_action_for_log_prob(actions, eps=1e-4)
                expert_log_probs_new = self._sanitize_log_prob_tensor(
                    expert_dist.log_prob(expert_actions[:, tf.newaxis, :])
                )
                expert_advantages = _to_tensor_with_cast(expert_advantages, tf.float32)
                expert_advantages = tf.clip_by_value(expert_advantages, -3.0, 3.0)
                expert_log_probs_new = tf.clip_by_value(expert_log_probs_new, -25.0, 25.0)
                expert_weighted_log_prob = expert_mask * tf.stop_gradient(expert_advantages) * expert_log_probs_new
                objective_expert_loss = (
                    tf.constant(self.objective_head_aux_coef, dtype=tf.float32)
                    * -tf.reduce_sum(expert_weighted_log_prob)
                    / (tf.cast(tf.shape(actions)[0], tf.float32) * active_expert_count)
                )
                if self.objective_head_aux_loss_clip > 0.0:
                    objective_expert_loss = tf.clip_by_value(
                        objective_expert_loss,
                        -tf.constant(self.objective_head_aux_loss_clip, dtype=tf.float32),
                        tf.constant(self.objective_head_aux_loss_clip, dtype=tf.float32),
                    )
            if router_probs is not None and self.objective_router_entropy_coef > 0.0:
                router_probs_safe = tf.maximum(router_probs, tf.constant(1e-8, dtype=router_probs.dtype))
                objective_router_entropy = -tf.constant(
                    self.objective_router_entropy_coef,
                    dtype=tf.float32,
                ) * tf.reduce_mean(-tf.reduce_sum(router_probs_safe * tf.math.log(router_probs_safe), axis=-1))
            if self.objective_head_diversity_coef > 0.0:
                expert_means = expert_alpha / tf.maximum(tf.reduce_sum(expert_alpha, axis=-1, keepdims=True), 1e-8)
                expert_means = tf.math.l2_normalize(expert_means, axis=-1)
                sims = tf.matmul(expert_means, expert_means, transpose_b=True)
                num_experts = tf.shape(sims)[-1]
                off_diag = 1.0 - tf.eye(num_experts, dtype=sims.dtype)
                pair_mask = tf.matmul(expert_mask[:, :, tf.newaxis], expert_mask[:, tf.newaxis, :])
                masked_off_diag = off_diag[tf.newaxis, :, :] * pair_mask
                mean_similarity = tf.reduce_sum(sims * masked_off_diag, axis=[1, 2]) / tf.maximum(
                    tf.reduce_sum(masked_off_diag, axis=[1, 2]),
                    1.0,
                )
                objective_diversity_loss = (
                    tf.constant(self.objective_head_diversity_coef, dtype=tf.float32)
                    * tf.reduce_mean(mean_similarity)
                )

        # Stabilize PPO ratio by clipping the log-probability delta
        log_prob_delta_raw = self._sanitize_log_prob_tensor(log_probs_new - log_probs_old)
        log_prob_delta_raw = tf.clip_by_value(log_prob_delta_raw, -10.0, 10.0)
        ratio_unclipped = tf.where(
            tf.math.is_finite(log_prob_delta_raw),
            tf.exp(log_prob_delta_raw),
            tf.ones_like(log_prob_delta_raw),
        )
        
        lower_clip = tf.math.log(tf.maximum(1.0 - self.policy_clip, 1e-3))
        upper_clip = tf.math.log(1.0 + self.policy_clip)
        log_prob_delta = tf.clip_by_value(log_prob_delta_raw, lower_clip, upper_clip)
        ratio = tf.where(
            tf.math.is_finite(log_prob_delta),
            tf.exp(log_prob_delta),
            tf.ones_like(log_prob_delta),
        )
        
        # DIAGNOSTIC: Compute ratio statistics before clipping to understand instability
        ratio_mean = tf.reduce_mean(ratio_unclipped)
        ratio_std = tf.math.reduce_std(ratio_unclipped)
        
        # Clipped surrogate objective
        surr1 = ratio * advantages
        surr2 = tf.clip_by_value(ratio, 1.0 - self.policy_clip, 1.0 + self.policy_clip) * advantages
        policy_loss = -tf.reduce_mean(tf.where(tf.math.is_finite(tf.minimum(surr1, surr2)), tf.minimum(surr1, surr2), tf.zeros_like(surr1)))
        
        # Entropy bonus for exploration
        entropy_loss = -self.entropy_coef * entropy
        
        (
            risk_aux_total,
            sharpe_aux_proxy,
            sharpe_aux_loss,
            mvo_aux_loss,
            cvar_aux_proxy,
            cvar_aux_loss,
        ) = self._compute_risk_aux_loss(states, alpha)
        consistency_loss = tf.constant(0.0, dtype=tf.float32)
        if (
            self.dual_head_enabled
            and projection_logits is not None
            and self.dual_head_consistency_coef > 0.0
        ):
            projection_weights = tf.nn.softmax(projection_logits, axis=-1)
            projection_weights = self._normalize_simplex(projection_weights)
            dirichlet_mean = self._normalize_simplex(alpha)
            consistency_loss = (
                tf.constant(self.dual_head_consistency_coef, dtype=tf.float32)
                * tf.reduce_mean(tf.square(dirichlet_mean - projection_weights))
            )
        # SOTA-FIX: Alpha diversity HHI auxiliary loss (anti-concentration)
        # Penalizes concentrated allocations by adding HHI as a cost.
        # HHI = 1/N for equal weight (minimum), 1.0 for single-stock (maximum).
        # For 11 assets: uniform HHI = 0.091, max = 1.0.
        diversity_loss = tf.constant(0.0, dtype=tf.float32)
        if self.alpha_diversity_coef > 0.0:
            alpha_weights = alpha / tf.reduce_sum(alpha, axis=-1, keepdims=True)
            hhi = tf.reduce_sum(tf.square(alpha_weights), axis=-1)  # (batch,)
            # Positive sign: PENALIZE high HHI (concentrated), loss = +coef * mean(HHI)
            diversity_loss = tf.constant(self.alpha_diversity_coef, dtype=tf.float32) * tf.reduce_mean(hhi)
        dispersion_loss = tf.constant(0.0, dtype=tf.float32)
        if self.alpha_dispersion_coef > 0.0:
            alpha_weights_disp = alpha / tf.reduce_sum(alpha, axis=-1, keepdims=True)
            alloc_std = tf.math.reduce_std(alpha_weights_disp, axis=-1)
            shortfall = tf.maximum(
                tf.constant(self.alpha_dispersion_target_std, dtype=tf.float32) - alloc_std,
                0.0,
            )
            dispersion_loss = (
                tf.constant(self.alpha_dispersion_coef, dtype=tf.float32)
                * tf.reduce_mean(shortfall)
            )

        # --- SOTA-FIX Phase 3: Auxiliary per-asset return prediction loss ---
        # MSE between predicted per-asset returns and actual per-asset returns
        # extracted from the state features (first feature per asset = return proxy).
        aux_return_loss = tf.constant(0.0, dtype=tf.float32)
        if (
            self.aux_return_pred_enabled
            and self.aux_return_pred_coef > 0.0
            and aux_return_preds is not None
        ):
            actual_returns = None
            # Extract actual per-asset returns from state features (index 0 per asset)
            if isinstance(states, dict):
                # Structured state: asset tensor is (batch, timesteps, num_assets, features)
                asset_tensor = states.get("asset", states)
                if hasattr(asset_tensor, 'shape') and asset_tensor.shape.rank == 4:
                    # Last timestep, feature index 0 = return proxy
                    actual_returns = asset_tensor[:, -1, :, self.risk_aux_return_feature_index]
            if actual_returns is not None:
                # Clip target to prevent outlier gradients
                actual_returns = tf.clip_by_value(actual_returns, -0.1, 0.1)
                aux_return_loss = tf.constant(self.aux_return_pred_coef, dtype=tf.float32) * tf.reduce_mean(
                    tf.square(aux_return_preds - actual_returns)
                )

        total_loss = (
            policy_loss
            + entropy_loss
            + risk_aux_total
            + consistency_loss
            + diversity_loss
            + dispersion_loss
            + aux_return_loss
            + mixture_balance_loss
            + mixture_separation_loss
            + mixture_component_dispersion_loss
            + objective_expert_loss
            + objective_router_entropy
            + objective_diversity_loss
        )
        
        approx_kl = tf.reduce_mean(
            tf.where(
                tf.math.is_finite(log_probs_old - log_probs_new),
                log_probs_old - log_probs_new,
                tf.zeros_like(log_probs_new),
            )
        )
        clip_mask = tf.cast(tf.abs(ratio_unclipped - 1.0) > self.policy_clip, tf.float32)
        clip_fraction = tf.reduce_mean(clip_mask)
        
        return (
            total_loss,
            policy_loss,
            entropy_loss,
            entropy,
            ratio_mean,
            ratio_std,
            approx_kl,
            clip_fraction,
            risk_aux_total,
            sharpe_aux_proxy,
            sharpe_aux_loss,
            mvo_aux_loss,
            cvar_aux_proxy,
            cvar_aux_loss,
            diversity_loss,
            dispersion_loss,
            mixture_balance_loss,
            mixture_separation_loss,
            mixture_component_dispersion_loss,
            mixture_gating_entropy,
            objective_expert_loss,
            objective_router_entropy,
            objective_diversity_loss,
        )
    
    @tf.function(reduce_retracing=True)
    def _critic_loss(self, states, returns, returns_mean, returns_std, old_values=None):
        """
        Compute the critic loss (value function MSE).
        
        Args:
            states: Batch of states
            returns: Target returns
            returns_mean: Running mean of returns
            returns_std: Running std of returns
            old_values: Value predictions collected during rollout (for value clipping)
            
        Returns:
            critic_loss: MSE loss between predicted and target values
        """
        values_raw = self.critic(states, training=True)
        values_raw = _to_tensor_with_cast(values_raw, tf.float32)
        values = self._critic_values_to_scalar(values_raw)

        returns_mean = _to_tensor_with_cast(returns_mean, tf.float32)
        returns_std = _to_tensor_with_cast(returns_std, tf.float32)
        returns_std = tf.maximum(returns_std, 1e-6)

        returns = _to_tensor_with_cast(returns, tf.float32)
        returns_centered = returns - returns_mean
        returns_norm = returns_centered / returns_std

        if self.popart_enabled:
            values_norm = values
            values_unnorm = self._denormalize_value(values_norm, mean=returns_mean, std=returns_std)
        else:
            values_centered = values - returns_mean
            values_norm = values_centered / returns_std
            values_unnorm = values

        clip_fraction = tf.constant(0.0, dtype=tf.float32)
        if self.distributional_critic_enabled:
            if self.popart_enabled:
                pred_quantiles_norm = values_raw
            else:
                pred_quantiles_norm = (values_raw - returns_mean) / returns_std
            if pred_quantiles_norm.shape.rank == 1:
                pred_quantiles_norm = tf.expand_dims(pred_quantiles_norm, axis=-1)
            q_loss = self._distributional_quantile_loss(pred_quantiles_norm, returns_norm)
            scalar_anchor_loss = tf.reduce_mean(tf.square(returns_norm - values_norm))
            loss = q_loss + tf.cast(self.distributional_mean_loss_coef, tf.float32) * scalar_anchor_loss
        else:
            if (
                self.value_clip_range is not None
                and self.value_clip_range > 0.0
                and old_values is not None
            ):
                old_values = _to_tensor_with_cast(old_values, tf.float32)
                old_values = tf.reshape(old_values, tf.shape(values_unnorm))
                values_clipped_unnorm = old_values + tf.clip_by_value(
                    values_unnorm - old_values,
                    -self.value_clip_range,
                    self.value_clip_range
                )
                values_clipped_norm = (values_clipped_unnorm - returns_mean) / returns_std
                clip_fraction = tf.reduce_mean(
                    tf.cast(tf.abs(values_unnorm - old_values) > self.value_clip_range, tf.float32)
                )

                loss_unclipped = tf.square(returns_norm - values_norm)
                loss_clipped = tf.square(returns_norm - values_clipped_norm)
                if self.critic_use_huber:
                    error_unclipped = returns_norm - values_norm
                    error_clipped = returns_norm - values_clipped_norm
                    loss_unclipped = self._safe_huber(error_unclipped, self.critic_huber_delta)
                    loss_clipped = self._safe_huber(error_clipped, self.critic_huber_delta)
                loss = tf.reduce_mean(tf.maximum(loss_unclipped, loss_clipped))
            else:
                # MSE loss on centered values
                error = returns_norm - values_norm
                if self.critic_use_huber:
                    loss = tf.reduce_mean(self._safe_huber(error, self.critic_huber_delta))
                else:
                    loss = tf.reduce_mean(tf.square(error))
        
        return loss, clip_fraction

    def _objective_critic_loss(self, states, expert_returns, old_expert_values=None, expert_mask=None):
        critic_output = self.critic(states, training=True)
        critic_parts = self._parse_critic_outputs(critic_output)
        expert_values = critic_parts["expert_values"]
        if expert_values is None:
            raise ValueError("Objective critic loss requested but critic does not emit expert_values.")
        expert_returns = _to_tensor_with_cast(expert_returns, tf.float32)
        if expert_mask is None:
            expert_mask = tf.constant(self.objective_expert_mask, dtype=tf.float32)
        expert_mask = tf.reshape(_to_tensor_with_cast(expert_mask, tf.float32), (1, -1))
        loss_unclipped = tf.square(expert_returns - expert_values)
        clip_fraction = tf.constant(0.0, dtype=tf.float32)
        if (
            self.value_clip_range is not None
            and self.value_clip_range > 0.0
            and old_expert_values is not None
        ):
            old_expert_values = _to_tensor_with_cast(old_expert_values, tf.float32)
            expert_values_clipped = old_expert_values + tf.clip_by_value(
                expert_values - old_expert_values,
                -self.value_clip_range,
                self.value_clip_range,
            )
            loss_clipped = tf.square(expert_returns - expert_values_clipped)
            clip_flags = tf.cast(tf.abs(expert_values - old_expert_values) > self.value_clip_range, tf.float32)
            clip_fraction = tf.reduce_sum(clip_flags * expert_mask) / tf.maximum(tf.reduce_sum(expert_mask), 1.0)
            if self.critic_use_huber:
                loss_unclipped = self._safe_huber(expert_returns - expert_values, self.critic_huber_delta)
                loss_clipped = self._safe_huber(expert_returns - expert_values_clipped, self.critic_huber_delta)
            loss_matrix = tf.maximum(loss_unclipped, loss_clipped)
        else:
            if self.critic_use_huber:
                loss_matrix = self._safe_huber(expert_returns - expert_values, self.critic_huber_delta)
            else:
                loss_matrix = loss_unclipped
        loss = tf.reduce_sum(loss_matrix * expert_mask) / tf.maximum(
            tf.cast(tf.shape(loss_matrix)[0], tf.float32) * tf.reduce_sum(expert_mask),
            1.0,
        )
        return loss, clip_fraction
    
    def update(self, num_epochs=10, batch_size=64, precomputed_gae=None):
        """
        Update the actor and critic networks using PPO.
        
        This is the baseline version that uses direct log-return rewards
        without the TAPE reward scaling system.
        
        Args:
            num_epochs: Number of optimization epochs
            batch_size: Batch size for updates
            precomputed_gae: Optional tuple(advantages, returns) prepared externally.
            
        Returns:
            dict: Training statistics
        """
        if len(self.memory['states']) == 0:
            logger.warning("No data in memory for update")
            return {}
        
        # Convert memory to numpy arrays
        states_np = np.array(self.memory['states'])
        actions = np.array(self.memory['actions'])
        log_probs_old = np.array(self.memory['log_probs'])
        mixture_components_old = np.array(self.memory.get('mixture_components', []), dtype=np.int32)
        rewards = np.array(self.memory['rewards'])
        values = np.array(self.memory['values'])
        expert_rewards = np.array(self.memory.get('expert_rewards', []), dtype=np.float32)
        expert_values = np.array(self.memory.get('expert_values', []), dtype=np.float32)
        expert_log_probs_old = np.array(self.memory.get('expert_log_probs', []), dtype=np.float32)
        router_probs_old = np.array(self.memory.get('router_probs', []), dtype=np.float32)
        dones = np.array(self.memory['dones'])
        
        if self.debug_prints:
            # DIAGNOSTIC: Check reward and value variance
            print(f"\n📊 REWARD & VALUE DIAGNOSTICS:")
            print(f"   Rewards: min={rewards.min():.4f}, max={rewards.max():.4f}")
            print(f"   Reward mean: {np.mean(rewards):.4f}, std: {np.std(rewards):.4f}")
            print(f"   Values: min={values.min():.4f}, max={values.max():.4f}")
            print(f"   Value mean: {np.mean(values):.4f}, std: {np.std(values):.4f}")

        # Optional multi-horizon sub-episode reward decomposition before normalization.
        raw_rewards = rewards.copy()
        shaped_rewards, mh_bonus = self._apply_multi_horizon_reward_decomposition(raw_rewards)
        # Use previous running stats to normalize current batch
        prev_mean = self._reward_mean
        prev_std = max(self._reward_std, 1e-1)
        rewards = (shaped_rewards - prev_mean) / prev_std
        rewards = np.clip(rewards, -5.0, 5.0)

        # Update running statistics AFTER normalization so the next batch sees updated stats
        self.reward_rms.update(shaped_rewards)
        self._reward_mean = float(self.reward_rms.mean)
        self._reward_std = float(max(self.reward_rms.std, 1e-1))

        if self.debug_prints:
            print(f"   Reward running mean: {self._reward_mean:.6f}, std: {self._reward_std:.6f}")
            print(
                f"   Normalized rewards: min={rewards.min():.6f}, max={rewards.max():.6f}, "
                f"mean={np.mean(rewards):.6f}, std={np.std(rewards):.6f}"
            )
            if self.multi_horizon_reward_enabled and self.multi_horizon_reward_coef > 0.0:
                print(
                    f"   Multi-horizon bonus: mean={np.mean(mh_bonus):.6f}, std={np.std(mh_bonus):.6f}, "
                    f"max={np.max(mh_bonus):.6f}"
                )
        if self.objective_experts_enabled:
            if expert_rewards.size == 0:
                expert_rewards = np.zeros((len(rewards), self.num_objective_experts), dtype=np.float32)
            prev_expert_mean = np.array(self._expert_reward_mean, copy=True)
            prev_expert_std = np.maximum(np.array(self._expert_reward_std, copy=True), 1e-1)
            expert_rewards = self.normalize_expert_rewards_for_update(
                expert_rewards,
                prev_mean=prev_expert_mean,
                prev_std=prev_expert_std,
                update_stats=True,
            )
            if self.debug_prints:
                print(
                    "   Expert reward running mean/std: "
                    f"mean={np.round(self._expert_reward_mean, 6).tolist()}, "
                    f"std={np.round(self._expert_reward_std, 6).tolist()}"
                )
        
        values_old = values.copy()
        expert_values_old = expert_values.copy()
        expert_advantages = None
        expert_returns = None
        if precomputed_gae is not None:
            if isinstance(precomputed_gae, dict):
                try:
                    advantages = np.asarray(precomputed_gae["advantages"], dtype=np.float32)
                    returns = np.asarray(precomputed_gae["returns"], dtype=np.float32)
                    if "expert_advantages" in precomputed_gae:
                        expert_advantages = np.asarray(precomputed_gae["expert_advantages"], dtype=np.float32)
                    if "expert_returns" in precomputed_gae:
                        expert_returns = np.asarray(precomputed_gae["expert_returns"], dtype=np.float32)
                except Exception as exc:
                    raise ValueError(f"Invalid precomputed_gae dict provided to update(): {exc}") from exc
            else:
                try:
                    advantages = np.asarray(precomputed_gae[0], dtype=np.float32)
                    returns = np.asarray(precomputed_gae[1], dtype=np.float32)
                except Exception as exc:
                    raise ValueError(f"Invalid precomputed_gae provided to update(): {exc}") from exc
            if len(advantages) != len(rewards) or len(returns) != len(rewards):
                raise ValueError(
                    "precomputed_gae length mismatch: "
                    f"advantages={len(advantages)}, returns={len(returns)}, rewards={len(rewards)}"
                )
        else:
            # Compute advantages and returns using GAE
            advantages, returns = self.compute_gae(rewards, values_old, dones)
        if self.objective_experts_enabled:
            if expert_advantages is None or expert_returns is None:
                expert_advantages_list = []
                expert_returns_list = []
                if expert_rewards.size == 0 or expert_values_old.size == 0:
                    expert_rewards = np.zeros((len(rewards), self.num_objective_experts), dtype=np.float32)
                    expert_values_old = np.zeros((len(rewards), self.num_objective_experts), dtype=np.float32)
                for expert_idx in range(self.num_objective_experts):
                    adv_i, ret_i = self.compute_gae(
                        expert_rewards[:, expert_idx],
                        expert_values_old[:, expert_idx],
                        dones,
                    )
                    expert_advantages_list.append(np.asarray(adv_i, dtype=np.float32))
                    expert_returns_list.append(np.asarray(ret_i, dtype=np.float32))
                expert_advantages = np.stack(expert_advantages_list, axis=-1)
                expert_returns = np.stack(expert_returns_list, axis=-1)
        
        # Store raw advantages for diagnostics BEFORE normalization
        raw_advantages = advantages.copy()
        
        # DIAGNOSTIC: Check advantage variance BEFORE normalization
        raw_adv_mean = np.mean(raw_advantages)
        raw_adv_std = np.std(raw_advantages)
        if self.debug_prints:
            print(f"\n[SEARCH] ADVANTAGE DIAGNOSTICS:")
            print(f"   Raw advantages: min={raw_advantages.min():.6f}, max={raw_advantages.max():.6f}")
            print(f"   Raw adv mean: {raw_adv_mean:.6f}, std: {raw_adv_std:.6f}")
            if raw_adv_std < 0.01:
                print(f"   [WARN]  WARNING: Very low std! Normalized advantages will be near zero!")
        
        # Normalize advantages
        advantages = (advantages - np.mean(advantages)) / (np.std(advantages) + 1e-8)
        if self.advantage_clip_value > 0.0:
            advantages = np.clip(advantages, -self.advantage_clip_value, self.advantage_clip_value)
        if self.objective_experts_enabled and expert_advantages is not None:
            normalized_cols = []
            for expert_idx in range(self.num_objective_experts):
                col = expert_advantages[:, expert_idx]
                norm_col = (col - np.mean(col)) / (np.std(col) + 1e-8)
                if self.expert_advantage_clip_value > 0.0:
                    norm_col = np.clip(norm_col, -self.expert_advantage_clip_value, self.expert_advantage_clip_value)
                normalized_cols.append(norm_col)
            expert_advantages = np.stack(normalized_cols, axis=-1)

        # DIAGNOSTIC: Check advantages AFTER normalization
        if self.debug_prints:
            print(f"   Normalized advantages: min={advantages.min():.6f}, max={advantages.max():.6f}")
            print(f"   Normalized adv mean: {np.mean(advantages):.6f}, std: {np.std(advantages):.6f}")

        # Update running statistics for critic targets before tensor conversion
        self._update_returns_stats(returns)
        
        # Convert to tensors
        returns_np = returns.copy()

        states = self._convert_states_for_network(states_np)
        actions = tf.constant(actions, dtype=tf.float32)
        log_probs_old = tf.constant(log_probs_old, dtype=tf.float32)
        mixture_components_old = tf.constant(
            mixture_components_old if mixture_components_old.size else np.full(len(actions), -1, dtype=np.int32),
            dtype=tf.int32,
        )
        expert_log_probs_old_tf = tf.constant(
            expert_log_probs_old if expert_log_probs_old.size else np.zeros((len(actions), self.num_objective_experts), dtype=np.float32),
            dtype=tf.float32,
        )
        expert_advantages_tf = tf.constant(
            expert_advantages if expert_advantages is not None else np.zeros((len(actions), self.num_objective_experts), dtype=np.float32),
            dtype=tf.float32,
        )
        expert_returns_tf = tf.constant(
            expert_returns if expert_returns is not None else np.zeros((len(actions), self.num_objective_experts), dtype=np.float32),
            dtype=tf.float32,
        )
        expert_old_values_tf = tf.constant(
            expert_values_old if expert_values_old.size else np.zeros((len(actions), self.num_objective_experts), dtype=np.float32),
            dtype=tf.float32,
        )
        advantages = tf.constant(advantages, dtype=tf.float32)
        returns = tf.constant(returns, dtype=tf.float32)
        old_values_tf = tf.constant(values_old, dtype=tf.float32)
        # Keep these as tensors so tf.function does not retrace on changing Python scalars.
        returns_mean_tf = tf.constant(self._returns_mean, dtype=tf.float32)
        returns_std_tf = tf.constant(self._returns_std, dtype=tf.float32)
        
        # Training statistics
        stats = {
            'actor_loss': 0.0,
            'critic_loss': 0.0,
            'critic_loss_scaled': 0.0,
            'risk_aux_total': 0.0,
            'risk_aux_sharpe_proxy': 0.0,
            'risk_aux_sharpe_loss': 0.0,
            'risk_aux_mvo_loss': 0.0,
            'risk_aux_cvar_proxy': 0.0,
            'risk_aux_cvar_loss': 0.0,
            'risk_aux_cvar_coef': float(self.risk_aux_cvar_coef),
            'alpha_diversity_loss': 0.0,
            'alpha_dispersion_loss': 0.0,
            'policy_loss': 0.0,
            'entropy_loss': 0.0,
            'entropy': 0.0,
            'mean_advantage': float(tf.reduce_mean(advantages)),
            'mean_return': float(tf.reduce_mean(returns)),
            'mean_reward_raw': float(np.mean(raw_rewards)),
            'mean_reward_shaped': float(np.mean(shaped_rewards)),
            'multi_horizon_reward_bonus_mean': float(np.mean(mh_bonus)),
            'multi_horizon_reward_bonus_std': float(np.std(mh_bonus)),
            'multi_horizon_reward_bonus_max': float(np.max(mh_bonus)) if mh_bonus.size > 0 else 0.0,
            'reward_running_mean': self._reward_mean,
            'reward_running_std': self._reward_std,
            # Diagnostic statistics (raw advantages before normalization)
            'adv_min': float(np.min(raw_advantages)),
            'adv_max': float(np.max(raw_advantages)),
            'adv_mean': float(np.mean(raw_advantages)),
            'adv_std': float(np.std(raw_advantages)),
            'actor_grad_norm': 0.0,
            'critic_grad_norm': 0.0,
            'alpha_min': 0.0,
            'alpha_max': 0.0,
            'alpha_mean': 0.0,
            'alpha_std': 0.0,  # Track alpha diversity for TCN learning
            'alpha_cap_hit_frac': 0.0,
            'mixture_balance_loss': 0.0,
            'mixture_separation_loss': 0.0,
            'mixture_component_dispersion_loss': 0.0,
            'mixture_gating_entropy': 0.0,
            'objective_expert_loss': 0.0,
            'objective_router_entropy': 0.0,
            'objective_diversity_loss': 0.0,
            'objective_router_probs': np.zeros(self.num_objective_experts, dtype=np.float64),
            'mixture_component_usage': np.zeros(self.mixture_dirichlet_num_components, dtype=np.float64),
            # Track risky-asset alpha means only; cash is handled separately in actions
            # and would break ticker-aligned diagnostics if included here.
            'alpha_per_asset': np.zeros(self.num_assets, dtype=np.float64),
            'film_seq_gamma_delta_abs_mean': 0.0,
            'film_seq_beta_abs_mean': 0.0,
            'film_seq_gamma_sat_frac': 0.0,
            'film_latent_gamma_delta_abs_mean': 0.0,
            'film_latent_beta_abs_mean': 0.0,
            'film_latent_gamma_sat_frac': 0.0,
            'film_regime_gamma_delta_abs_mean': 0.0,
            'film_regime_beta_abs_mean': 0.0,
            'film_regime_gamma_sat_frac': 0.0,
            'film_asset_gamma_delta_abs_mean': 0.0,
            'film_asset_beta_abs_mean': 0.0,
            'film_asset_gamma_sat_frac': 0.0,
            # NEW: PPO ratio statistics
            'ratio_mean': 0.0,
            'ratio_std': 0.0,
            'approx_kl': 0.0,
            'clip_fraction': 0.0,
            'value_clip_fraction': 0.0,
            # Running statistics for critic normalization
            'returns_running_mean': self._returns_mean,
            'returns_running_std': self._returns_std,
            'popart_enabled': float(self.popart_enabled),
            'num_grad_updates': 0,
            'explained_variance': 0.0,
            'early_stop_kl_triggered': 0.0,
            'early_stop_kl': 0.0,
            'early_stop_epoch': -1.0,
            'nonfinite_actor_loss_detected': 0.0,
            'nonfinite_critic_loss_detected': 0.0,
            'actor_nonfinite_grad_tensors': 0.0,
            'actor_nonfinite_grad_elements': 0.0,
            'critic_nonfinite_grad_tensors': 0.0,
            'critic_nonfinite_grad_elements': 0.0,
        }
        
        # Multiple epochs of optimization
        if isinstance(states, dict):
            dataset_size = int(states["asset"].shape[0])
        else:
            dataset_size = int(states.shape[0])
        early_stop = False
        for epoch in range(num_epochs):
            if early_stop:
                break
            # Shuffle data
            indices = tf.random.shuffle(tf.range(dataset_size))
            
            # Mini-batch updates
            for start_idx in range(0, dataset_size, batch_size):
                end_idx = min(start_idx + batch_size, dataset_size)
                batch_indices = indices[start_idx:end_idx]
                
                if isinstance(states, dict):
                    batch_states = {
                        "asset": tf.gather(states["asset"], batch_indices),
                        "context": tf.gather(states["context"], batch_indices),
                    }
                else:
                    batch_states = tf.gather(states, batch_indices)
                batch_actions = tf.gather(actions, batch_indices)
                batch_log_probs_old = tf.gather(log_probs_old, batch_indices)
                batch_mixture_components_old = tf.gather(mixture_components_old, batch_indices)
                batch_expert_log_probs_old = tf.gather(expert_log_probs_old_tf, batch_indices)
                batch_expert_advantages = tf.gather(expert_advantages_tf, batch_indices)
                batch_advantages = tf.gather(advantages, batch_indices)
                batch_returns = tf.gather(returns, batch_indices)
                batch_expert_returns = tf.gather(expert_returns_tf, batch_indices)
                batch_old_values = tf.gather(old_values_tf, batch_indices)
                batch_old_expert_values = tf.gather(expert_old_values_tf, batch_indices)
                
                # Update actor
                with tf.GradientTape() as tape:
                    (
                        actor_loss,
                        policy_loss,
                        entropy_loss,
                        entropy,
                        ratio_mean,
                        ratio_std,
                        approx_kl,
                        clip_fraction,
                        risk_aux_total,
                        sharpe_aux_proxy,
                        sharpe_aux_loss,
                        mvo_aux_loss,
                        cvar_aux_proxy,
                        cvar_aux_loss,
                        diversity_loss,
                        dispersion_loss,
                        mixture_balance_loss,
                        mixture_separation_loss,
                        mixture_component_dispersion_loss,
                        mixture_gating_entropy,
                        objective_expert_loss,
                        objective_router_entropy,
                        objective_diversity_loss,
                    ) = self._actor_loss(
                        batch_states,
                        batch_actions,
                        batch_log_probs_old,
                        batch_advantages,
                        batch_mixture_components_old,
                        batch_expert_log_probs_old,
                        batch_expert_advantages,
                    )
                
                actor_grads = tape.gradient(actor_loss, self.actor.trainable_variables)
                actor_nonfinite_grad_tensors = 0
                actor_nonfinite_grad_elements = 0
                if self.sanitize_nonfinite_gradients:
                    actor_grads, actor_nonfinite_grad_tensors, actor_nonfinite_grad_elements = self._sanitize_gradients(actor_grads)
                
                # Compute gradient norm BEFORE clipping for diagnostics
                actor_grad_norm = tf.linalg.global_norm(actor_grads).numpy()
                actor_loss_nonfinite = bool(tf.math.is_nan(actor_loss) or tf.math.is_inf(actor_loss))
                actor_grad_nonfinite = (not np.isfinite(actor_grad_norm))
                if actor_loss_nonfinite or actor_grad_nonfinite:
                    stats['nonfinite_actor_loss_detected'] = 1.0
                    logger.error("[ERROR] CRITICAL: NaN/Inf detected in actor_loss! Training unstable.")
                    logger.error("   Policy loss: %.6f, Entropy loss: %.6f", float(policy_loss), float(entropy_loss))
                    logger.error("   Actor grad norm: %s", actor_grad_norm)
                    self._log_nonfinite_policy_diagnostics(
                        batch_states,
                        batch_actions,
                        batch_log_probs_old,
                        batch_mixture_components_old,
                    )
                    early_stop = True
                    break

                if self.max_grad_norm > 0:
                    actor_grads, _ = tf.clip_by_global_norm(actor_grads, self.max_grad_norm)
                self.actor_optimizer.apply_gradients(zip(actor_grads, self.actor.trainable_variables))
                
                # Update critic
                with tf.GradientTape() as tape:
                    if self.objective_experts_enabled:
                        critic_loss_raw, value_clip_fraction = self._objective_critic_loss(
                            batch_states,
                            batch_expert_returns,
                            batch_old_expert_values,
                            self.objective_expert_mask,
                        )
                    else:
                        critic_loss_raw, value_clip_fraction = self._critic_loss(
                            batch_states,
                            batch_returns,
                            returns_mean_tf,
                            returns_std_tf,
                            batch_old_values
                        )
                    # Apply configurable value-function coefficient to critic optimization.
                    # This was previously ignored because actor/critic are updated separately.
                    critic_loss = critic_loss_raw * self.vf_coef
                
                critic_grads = tape.gradient(critic_loss, self.critic.trainable_variables)
                critic_nonfinite_grad_tensors = 0
                critic_nonfinite_grad_elements = 0
                if self.sanitize_nonfinite_gradients:
                    critic_grads, critic_nonfinite_grad_tensors, critic_nonfinite_grad_elements = self._sanitize_gradients(critic_grads)
                
                # Compute gradient norm BEFORE clipping for diagnostics
                critic_grad_norm = tf.linalg.global_norm(critic_grads).numpy()
                critic_loss_nonfinite = bool(tf.math.is_nan(critic_loss_raw) or tf.math.is_inf(critic_loss_raw))
                critic_grad_nonfinite = (not np.isfinite(critic_grad_norm))
                if critic_loss_nonfinite or critic_grad_nonfinite:
                    stats['nonfinite_critic_loss_detected'] = 1.0
                    logger.error(f"[ERROR] CRITICAL: NaN/Inf detected in critic_loss! Training unstable.")
                    logger.error("   Critic grad norm: %s", critic_grad_norm)
                    early_stop = True
                    break
                
                if self.max_grad_norm > 0:
                    critic_grads, _ = tf.clip_by_global_norm(critic_grads, self.max_grad_norm)
                self.critic_optimizer.apply_gradients(zip(critic_grads, self.critic.trainable_variables))
                
                # Get alpha statistics from current batch
                alpha_batch, _, _ = self._split_actor_outputs(self.actor(batch_states, training=False))
                alpha_batch = alpha_batch.numpy()
                alpha_cap = getattr(self.actor, "_alpha_cap", None)
                if alpha_cap is not None and np.isfinite(alpha_cap):
                    cap_tol = max(1e-6, 1e-3 * float(alpha_cap))
                    alpha_cap_hit_frac_batch = float(np.mean(alpha_batch >= (float(alpha_cap) - cap_tol)))
                else:
                    alpha_cap_hit_frac_batch = 0.0
                
                # Accumulate statistics
                stats['actor_loss'] += float(actor_loss)
                stats['critic_loss'] += float(critic_loss_raw)
                stats['critic_loss_scaled'] += float(critic_loss)
                stats['risk_aux_total'] += float(risk_aux_total)
                stats['risk_aux_sharpe_proxy'] += float(sharpe_aux_proxy)
                stats['risk_aux_sharpe_loss'] += float(sharpe_aux_loss)
                stats['risk_aux_mvo_loss'] += float(mvo_aux_loss)
                stats['risk_aux_cvar_proxy'] += float(cvar_aux_proxy)
                stats['risk_aux_cvar_loss'] += float(cvar_aux_loss)
                stats['alpha_diversity_loss'] += float(diversity_loss)
                stats['alpha_dispersion_loss'] += float(dispersion_loss)
                stats['mixture_balance_loss'] += float(mixture_balance_loss)
                stats['mixture_separation_loss'] += float(mixture_separation_loss)
                stats['mixture_component_dispersion_loss'] += float(mixture_component_dispersion_loss)
                stats['mixture_gating_entropy'] += float(mixture_gating_entropy)
                stats['objective_expert_loss'] += float(objective_expert_loss)
                stats['objective_router_entropy'] += float(objective_router_entropy)
                stats['objective_diversity_loss'] += float(objective_diversity_loss)
                if self.risk_aux_cvar_adaptive_enabled:
                    self._update_adaptive_cvar_coef(float(cvar_aux_proxy))
                stats['risk_aux_cvar_coef'] = float(self.risk_aux_cvar_coef)
                stats['policy_loss'] += float(policy_loss)
                stats['entropy_loss'] += float(entropy_loss)
                stats['entropy'] += float(entropy)
                stats['actor_grad_norm'] += float(actor_grad_norm)
                stats['critic_grad_norm'] += float(critic_grad_norm)
                stats['actor_nonfinite_grad_tensors'] += float(actor_nonfinite_grad_tensors)
                stats['actor_nonfinite_grad_elements'] += float(actor_nonfinite_grad_elements)
                stats['critic_nonfinite_grad_tensors'] += float(critic_nonfinite_grad_tensors)
                stats['critic_nonfinite_grad_elements'] += float(critic_nonfinite_grad_elements)
                stats['alpha_min'] += float(np.min(alpha_batch))
                stats['alpha_max'] += float(np.max(alpha_batch))
                stats['alpha_mean'] += float(np.mean(alpha_batch))
                stats['alpha_std'] += float(np.std(alpha_batch))  # Track alpha diversity
                stats['alpha_cap_hit_frac'] += alpha_cap_hit_frac_batch
                risky_alpha_batch = alpha_batch[..., :self.num_assets]
                stats['alpha_per_asset'] += np.mean(risky_alpha_batch, axis=0).astype(np.float64)
                if self.objective_experts_enabled:
                    actor_diag = self._parse_actor_outputs(self.actor(batch_states, training=False))
                    batch_router_probs = actor_diag.get("router_probs", None)
                    if batch_router_probs is not None:
                        stats['objective_router_probs'] += np.mean(batch_router_probs.numpy(), axis=0).astype(np.float64)
                film_diag = self.get_film_diagnostics(batch_states)
                if film_diag:
                    stats['film_seq_gamma_delta_abs_mean'] += float(film_diag.get('seq_gamma_delta_abs_mean', 0.0))
                    stats['film_seq_beta_abs_mean'] += float(film_diag.get('seq_beta_abs_mean', 0.0))
                    stats['film_seq_gamma_sat_frac'] += float(film_diag.get('seq_gamma_sat_frac', 0.0))
                    stats['film_latent_gamma_delta_abs_mean'] += float(film_diag.get('latent_gamma_delta_abs_mean', 0.0))
                    stats['film_latent_beta_abs_mean'] += float(film_diag.get('latent_beta_abs_mean', 0.0))
                    stats['film_latent_gamma_sat_frac'] += float(film_diag.get('latent_gamma_sat_frac', 0.0))
                    stats['film_regime_gamma_delta_abs_mean'] += float(film_diag.get('regime_gamma_delta_abs_mean', 0.0))
                    stats['film_regime_beta_abs_mean'] += float(film_diag.get('regime_beta_abs_mean', 0.0))
                    stats['film_regime_gamma_sat_frac'] += float(film_diag.get('regime_gamma_sat_frac', 0.0))
                    stats['film_asset_gamma_delta_abs_mean'] += float(film_diag.get('asset_gamma_delta_abs_mean', 0.0))
                    stats['film_asset_beta_abs_mean'] += float(film_diag.get('asset_beta_abs_mean', 0.0))
                    stats['film_asset_gamma_sat_frac'] += float(film_diag.get('asset_gamma_sat_frac', 0.0))
                if self.mixture_dirichlet_enabled:
                    valid_components = np.asarray(batch_mixture_components_old.numpy(), dtype=np.int32)
                    valid_components = valid_components[(valid_components >= 0) & (valid_components < self.mixture_dirichlet_num_components)]
                    if valid_components.size > 0:
                        counts = np.bincount(valid_components, minlength=self.mixture_dirichlet_num_components)
                        stats['mixture_component_usage'] += counts.astype(np.float64)
                stats['ratio_mean'] += float(ratio_mean)
                stats['ratio_std'] += float(ratio_std)
                stats['approx_kl'] += float(approx_kl)
                stats['clip_fraction'] += float(clip_fraction)
                stats['value_clip_fraction'] += float(value_clip_fraction)
                stats['num_grad_updates'] += 1                
                # Early-stop PPO update when KL drift is too high (stability guard).
                approx_kl_value = float(approx_kl)
                if (
                    self.target_kl > 0.0
                    and stats['num_grad_updates'] >= max(self.minibatches_before_kl_stop, 1)
                    and approx_kl_value > (self.target_kl * self.kl_stop_multiplier)
                ):
                    stats['early_stop_kl_triggered'] = 1.0
                    stats['early_stop_kl'] = approx_kl_value
                    stats['early_stop_epoch'] = float(epoch)
                    logger.warning(
                        "[WARN] PPO early-stop: approx_kl %.6f exceeded threshold %.6f (target_kl %.6f × %.2f)",
                        approx_kl_value,
                        self.target_kl * self.kl_stop_multiplier,
                        self.target_kl,
                        self.kl_stop_multiplier,
                    )
                    early_stop = True
                    break
        
        # Average statistics over all updates
        num_updates = stats['num_grad_updates']
        if num_updates > 0:
            for key in ['actor_loss', 'critic_loss', 'critic_loss_scaled',
                       'risk_aux_total', 'risk_aux_sharpe_proxy', 'risk_aux_sharpe_loss', 'risk_aux_mvo_loss',
                       'risk_aux_cvar_proxy', 'risk_aux_cvar_loss',
                       'alpha_diversity_loss', 'alpha_dispersion_loss',
                       'mixture_balance_loss', 'mixture_separation_loss',
                       'mixture_component_dispersion_loss', 'mixture_gating_entropy',
                       'objective_expert_loss', 'objective_router_entropy', 'objective_diversity_loss',
                       'policy_loss', 'entropy_loss', 'entropy',
                       'actor_grad_norm', 'critic_grad_norm',
                       'actor_nonfinite_grad_tensors', 'actor_nonfinite_grad_elements',
                       'critic_nonfinite_grad_tensors', 'critic_nonfinite_grad_elements',
                       'alpha_min', 'alpha_max', 'alpha_mean', 'alpha_std',
                       'alpha_cap_hit_frac',
                       'film_seq_gamma_delta_abs_mean', 'film_seq_beta_abs_mean', 'film_seq_gamma_sat_frac',
                       'film_latent_gamma_delta_abs_mean', 'film_latent_beta_abs_mean', 'film_latent_gamma_sat_frac',
                       'film_regime_gamma_delta_abs_mean', 'film_regime_beta_abs_mean', 'film_regime_gamma_sat_frac',
                       'film_asset_gamma_delta_abs_mean', 'film_asset_beta_abs_mean', 'film_asset_gamma_sat_frac',
                       'ratio_mean', 'ratio_std', 'approx_kl', 'clip_fraction', 'value_clip_fraction']:
                stats[key] /= num_updates
            stats['alpha_per_asset'] /= num_updates
            stats['objective_router_probs'] /= num_updates
            usage_total = float(np.sum(stats['mixture_component_usage']))
            if usage_total > 0.0:
                stats['mixture_component_usage'] /= usage_total

        # Remove temporary counter
        del stats['num_grad_updates']
        
        # Clear memory after update
        self.clear_memory()
        
        actor_eval_parts = self._parse_actor_outputs(self.actor(states, training=False))
        values_post = self.critic(states, training=False)
        returns_np = np.asarray(returns_np, dtype=np.float32)
        values_post = self._parse_critic_outputs(values_post, router_probs=actor_eval_parts.get("router_probs", None))["value"]
        values_post = self._denormalize_value(values_post).numpy()
        returns_var = np.var(returns_np)
        if returns_var > 1e-8:
            stats['explained_variance'] = float(
                1.0 - np.var(returns_np - values_post) / (returns_var + 1e-8)
            )
        else:
            stats['explained_variance'] = 0.0

        logger.debug(f"PPO Update completed: {num_updates} mini-batch updates over {num_epochs} epochs")

        # PERF-FIX #7: Update EMA actor weights after each PPO update
        self._update_ema_actor()

        return stats
    
    def save_models(self, filepath_prefix):
        """
        Save the actor and critic networks.
        
        Args:
            filepath_prefix: Prefix for the saved model files
        """
        actor_path = f"{filepath_prefix}_actor.weights.h5"
        critic_path = f"{filepath_prefix}_critic.weights.h5"
        
        self.actor.save_weights(actor_path)
        self.critic.save_weights(critic_path)
        
        logger.info(f"Models saved to {actor_path} and {critic_path}")
    
    def load_models(self, filepath_prefix):
        """
        Load the actor and critic networks.
        
        Args:
            filepath_prefix: Prefix for the saved model files
        """
        actor_path = f"{filepath_prefix}_actor.weights.h5"
        critic_path = f"{filepath_prefix}_critic.weights.h5"
        
        # Create dummy forward pass to build the models
        if self.is_sequential:
            if self.uses_structured_state_inputs:
                dummy_state = {
                    "asset": tf.zeros(
                        (1, int(self.sequence_length), int(self.num_assets), int(self.asset_feature_dim)),
                        dtype=tf.float32,
                    ),
                    "context": tf.zeros(
                        (1, int(self.sequence_length), int(max(self.global_feature_dim, 0))),
                        dtype=tf.float32,
                    ),
                }
            else:
                dummy_state = tf.random.normal((1, int(self.sequence_length), self.state_dim))
        else:
            dummy_state = tf.random.normal((1, self.state_dim))
        _ = self.actor(dummy_state)
        _ = self.critic(dummy_state)
        
        # Load weights
        self.actor.load_weights(actor_path)
        self.critic.load_weights(critic_path)
        
        logger.info(f"Models loaded from {actor_path} and {critic_path}")
    
    @property
    def memory_size(self):
        """Return the current size of memory buffer."""
        return len(self.memory['states'])
    
    def update_last_episode_rewards(self, scaled_rewards):
        """
        Update rewards in memory for the last episode (for TAPE system).
        
        Args:
            scaled_rewards: List of scaled rewards to replace the last N rewards
        """
        episode_length = len(scaled_rewards)
        if episode_length > len(self.memory['rewards']):
            logger.warning(f"Scaled rewards length ({episode_length}) exceeds memory size ({len(self.memory['rewards'])})")
            return
        
        # Replace the last N rewards
        for i, scaled_reward in enumerate(scaled_rewards):
            idx = -(episode_length - i)
            self.memory['rewards'][idx] = scaled_reward
    
    def save(self, directory):
        """
        Save agent models to directory.
        
        Args:
            directory: Directory path to save models
        """
        import os
        os.makedirs(directory, exist_ok=True)
        
        # Save actor and critic weights
        actor_path = os.path.join(directory, 'actor_weights.h5')
        critic_path = os.path.join(directory, 'critic_weights.h5')
        
        self.actor.save_weights(actor_path)
        self.critic.save_weights(critic_path)
        
        logger.info(f"Models saved to {directory}")
    
    def load(self, directory):
        """
        Load agent models from directory.
        
        Args:
            directory: Directory path to load models from
        """
        import os
        
        actor_path = os.path.join(directory, 'actor_weights.h5')
        critic_path = os.path.join(directory, 'critic_weights.h5')
        
        if os.path.exists(actor_path) and os.path.exists(critic_path):
            self.actor.load_weights(actor_path)
            self.critic.load_weights(critic_path)
            logger.info(f"Models loaded from {directory}")
        else:
            logger.error(f"Model weights not found in {directory}")
            raise FileNotFoundError(f"Model weights not found in {directory}")
    
    def get_action(self, state, training=True, evaluation_mode='mean_plus_noise'):
        """
        Get action for compatibility with train_rl.py.
        Same as get_action_and_value but with training flag.
        
        Args:
            state: Current state
            training: Whether in training mode (True) or evaluation mode (False)
            evaluation_mode: Strategy for deterministic evaluation
            
        Returns:
            tuple: (action, log_prob, value)
        """
        return self.get_action_and_value(state, deterministic=not training, evaluation_mode=evaluation_mode)
    
    def predict(self, observation, deterministic=False, evaluation_mode='mode'):
        """
        Compatible interface for notebook backtests and stable-baselines-like usage.
        
        Args:
            observation: State observation (can be batched or single)
            deterministic: If True, use deterministic evaluation (no stochastic sampling)
            evaluation_mode: Strategy for deterministic evaluation
                - 'mean': Use Dirichlet mean (alpha / sum(alpha))
                - 'mode': Use Dirichlet mode (peak of distribution) - RECOMMENDED
                - 'mean_plus_noise': Mean with small Gaussian noise
        
        Returns:
            tuple: (action, state) where state is None (for compatibility)
        """
        # Call get_action with appropriate parameters
        action, _, _ = self.get_action(
            observation,
            training=not deterministic,
            evaluation_mode=evaluation_mode
        )
        
        # Return (action, state) tuple for API compatibility
        # State is None because we're using feedforward policies (not RNN)
        return action, None
