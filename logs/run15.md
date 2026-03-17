[START] Starting training
Architecture: MLP
max_total_timesteps: 300000
num_parallel_envs: 4

================================================================================
EXPERIMENT 6: MLP Enhanced + TAPE Three-Component
================================================================================
Architecture: MLP
Results root: /content/tcn_tape_vectorized_version_clean/results
Working dir: /content/tcn_tape_vectorized_version_clean
Covariance Features: Yes
🎯 REWARD SYSTEM: TAPE (Three-Component v3)
   Profile: BalancedGrowth
   Daily: Base + DSR/PBRS + Turnover_Proximity
   Terminal: mode=signed | baseline=0.20 | scalar=10.0 (clipped ±10.0)
   Gate A: enabled (Sharpe <= 0.00 or MDD >= 30.0% -> force non-positive terminal bonus)
   Neutral Band: enabled (±0.020 around baseline)
   [CYCLE] Profile Manager: disabled (static profile only)
[RAND] Experiment Seed: 6042 (Base: 42, Offset: 6000)
[OK] Features: Enhanced (includes 2 covariance eigenvalues)
   Eigenvalues: ['Covariance_Eigenvalue_0', 'Covariance_Eigenvalue_1']
   Train shape: (15102, 67)
   Test shape: (5508, 67)
   ℹ️ Actuarial features disabled by config.

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.60, band=±0.20, scalar=0.10 -> 0.15 => 0.20 => 0.25 => 0.30)
      ↳ Schedule: 0.10@0 => 0.15@60,000 => 0.20@140,000 => 0.25@220,000 => 0.30@280,000
   ⚙️  Component 4: Execution Inertia (beta=0.50 -> 0.65 => 0.80 => 1.00, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.50@0 => 0.65@60,000 => 0.80@140,000 => 1.00@220,000
   ⚡ Parallel rollout envs: 4
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 30.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🌊 DSR Regime Scaling: ENABLED | low_mult=0.3 (vol<0.12) | mid_mult=1.0 | high_mult=1.5 (vol>0.25)
   📈 Benchmark Shaping (1/N): ENABLED | scalar=8.0 | mode=signed_clipped | clip=0.0200
   📈 Benchmark Shaping (SPY): ENABLED | scalar=5.0 | mode=signed_clipped | clip=0.0200
   🔐 Lagrangian CVaR: ENABLED | threshold=-0.035 | lr=0.002 | lambda_max=2.0 | penalty_scale=0.75
   Alpha Regularization: hhi_coef=0.005 | dispersion_coef=0.02 | target_std=0.1
   Risk Aux: sharpe_coef=0.0 | mvo_coef=0.0 | cvar_coef=0.0
   🧪 Aux Per-Asset Return Head: ENABLED | coef=0.35
   🔒 Dirichlet Alpha Cap: 16.0
   🔒 Drawdown dual controller (requested): target=27.00%, tolerance=-2.00% (trigger boundary ≈ 25.00%), lr=0.100, λ_init=0.05, λ_floor=0.00, λ_max=5.00, penalty_coef=0.50
   📐 Position constraints: max_single_asset=35%, min_cash=2%
   [DEBUG] Regime-balanced sampling: use_curriculum_learning=True, volatility_regime pre-existing=False
   🎲 Volatility regimes ready for sampling (computed):
      high_vol: 826 dates (32.8%)
      low_vol: 826 dates (32.8%)
      medium_vol: 865 dates (34.4%)
   🧭 Regime start buckets (train env):
      high_vol: 826 dates (32.8%)
      low_vol: 826 dates (32.8%)
      medium_vol: 865 dates (34.4%)
   [OK] Drawdown controller armed in env: target=27.00%, trigger=25.00%, λ_init=0.050, λ_floor=0.000, λ_max=5.00, penalty_coef=0.50
[OK] THREE-COMPONENT TAPE v3 Environments created:
   Training: 2517 days
   Parallel train env instances: 4
   Testing: 918 days

🤖 Creating MLP agent with Dirichlet distribution for Exp 6...
[OK] Agent created: PPOAgentTF
   [RAND] Dirichlet Distribution: ENABLED
   [TOOL] Actor LR schedule: 0.000030@0 => 0.000020@100,000 => 0.000010@220,000
   [TOOL] Critic LR schedule: 0.000150@0 => 0.000120@100,000 => 0.000100@220,000
   State dim: 275
   Action dim: 6
   Actor LR (configured): 3e-05
   Actor LR (active): 0.000030
   Critic LR (active): 0.000150
   🧱 TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   [BRAIN] Recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DNA] State augmentation: enabled=False
   [DOWN] Distributional critic: enabled=False | num_quantiles=1
   🎛️ Dirichlet controls: activation=exp_tanh | temperature=0.8 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Dual-head consistency coef: 0.0
   🧩 Mixture Regularizers: balance_coef=0.005 | separation_coef=0.06 | gate_entropy_coef=0.001 | component_dispersion_coef=0.04 | target_std=0.3 | min_distance=0.18
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0030
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@100,000 => 0.9980@220,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@100,000 => 0.9700@220,000
   🎯 Entropy coef schedule: 0.0030@0 => 0.0030@100,000 => 0.0025@200,000 => 0.0015@280,000
   🧪 Aux-return coef schedule: 0.3500@0 => 0.3000@100,000 => 0.2500@220,000
   🌡️ Temperature schedule: 0.8000@0 => 0.7000@100,000 => 0.6000@220,000
   📐 PPO rollout schedule: 1008@0 => 1512@100,000 => 2016@220,000
   🧺 PPO batch-size schedule: 252@0 => 336@100,000 => 504@220,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/results/logs/Exp6_MLP_Enhanced_TAPE_training_20260317_181347_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/results/logs/Exp6_MLP_Enhanced_TAPE_training_20260317_181347_step_diagnostics.csv

🎯 Starting THREE-COMPONENT TAPE v3 training (with curriculum)...
   Total timesteps: 300,000
   Timesteps per update: scheduled
      0+ steps: timesteps_per_update=1008
      100,000+ steps: timesteps_per_update=1512
      220,000+ steps: timesteps_per_update=2016
   Number of updates: 219
   PPO batch_size: scheduled
      0+ steps: batch_size=252
      100,000+ steps: batch_size=336
      220,000+ steps: batch_size=504
   PPO gamma schedule: 0.9900@0 => 0.9950@100,000 => 0.9980@220,000
   PPO GAE-λ schedule: 0.9200@0 => 0.9500@100,000 => 0.9700@220,000
   📚 Episode Length Curriculum:
      0+ steps: limit=756
      60,000+ steps: limit=1008
      180,000+ steps: limit=1500
      260,000+ steps: limit=full
      ↳ smooth ramp: enabled (overlap=10,000 steps)
   📚 Turnover Scalar Curriculum:
      0+ steps: scalar=0.10
      60,000+ steps: scalar=0.15
      140,000+ steps: scalar=0.20
      220,000+ steps: scalar=0.25
      280,000+ steps: scalar=0.30
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.50
      60,000+ steps: beta=0.65
      140,000+ steps: beta=0.80
      220,000+ steps: beta=1.00
   🏆 Deterministic-validation checkpoints: enabled (every 5 episodes | mode=mode | min_sharpe=0.50 | min_delta=0.000 | alpha_diag=True | horizon=scheduled (0@756 => 100,000@1008 => 250,000@1500 => 400,000@full))
      ↳ Multi-horizon selector: enabled (252:0.35, 504:0.30, 756:0.20, 1008:0.15) | dd_penalty_coef=0.250
      ↳ Stochastic sanity gate: enabled (runs=3, horizon=252, min_mean_sharpe=0.00, max_std=1.50)
      ↳ SPY outperformance gate: enabled (required>0.00% over the same validation horizon)
      ↳ Equal-weight gate: enabled (required>0.00% over the same validation horizon)
   🧷 Legacy checkpoint routes: disabled (high-watermark/step/periodic/tape/rare)
   [OK] Checkpoint selector default: deterministic validation multi-horizon composite score
   💾 High-watermark checkpoints: disabled
   ⏹️ Training early-stop: enabled (warmup=100,000 steps, patience=25 updates, min_delta=0.010, hard_dd=60.0% x 12)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/results/logs/Exp6_MLP_Enhanced_TAPE_training_20260317_181347_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/results/logs/Exp6_MLP_Enhanced_TAPE_training_20260317_181347_metadata.json
[CYCLE] Update 1/219 | Step 1,008/300,000 | Episode 0 | Time: 57.7s
   📊 Metrics: Return=+33.33% | Sharpe=2.128 | DD=5.75% | Turnover=30.72%
   🎚️ Intra-Step TAPE: potential=0.7509 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1335 | critic_loss=1.2288 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.6144 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=0.9929 | balance_loss=0.0003 | separation_loss=0.0029 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1277 | ema=2.1277 | best_ema=2.1277 | no_improve=0
[CYCLE] Update 2/219 | Step 2,016/300,000 | Episode 0 | Time: 105.5s
   📊 Metrics: Return=+28.26% | Sharpe=0.686 | DD=22.55% | Turnover=32.07%
   🎚️ Intra-Step TAPE: potential=0.2124 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0919 | critic_loss=0.7971 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3985 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0038 | balance_loss=0.0003 | separation_loss=0.0027 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6859 | ema=1.9835 | best_ema=1.9835 | no_improve=0
   🔬 Alpha Diversity: mean=9.35 | std=3.70 | range=[0.32, 16.00] | cap_hit=3.8%
   🏷️ Alpha Per-Asset  TOP: NVDA=12.43 | AMZN=10.70 | MSFT=8.78  BOT: XOM=8.37 | CAT=8.07 | JPM=7.59
   🎛️ Mixture Usage: C0=22.1% | C1=44.6% | C2=33.2%
   🧭 Regime Start Dist (train resets): high_vol=2 (50.0%), low_vol=1 (25.0%), medium_vol=1 (25.0%)
[CYCLE] Update 3/219 | Step 3,024/300,000 | Episode 4 | Time: 153.3s
   📊 Metrics: Return=+33.44% | Sharpe=0.608 | DD=12.05% | Turnover=34.25%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0858 | critic_loss=0.7275 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3637 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0238 | balance_loss=0.0002 | separation_loss=0.0030 | component_dispersion_loss=0.0078
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6083 | ema=1.8460 | best_ema=1.8460 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.050) | TAPE=0.3458
   📈 Benchmark Relative: 1/N shaping=-0.028 (EW ret=-0.00134) | SPY shaping=-0.036 (SPY ret=0.00231)
[CYCLE] Update 4/219 | Step 4,032/300,000 | Episode 4 | Time: 200.9s
   📊 Metrics: Return=+16.12% | Sharpe=0.773 | DD=18.11% | Turnover=31.94%
   🎚️ Intra-Step TAPE: potential=0.7166 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0769 | critic_loss=0.3974 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1987 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0010
   🧩 Mixture Head: gate_entropy=1.0379 | balance_loss=0.0002 | separation_loss=0.0030 | component_dispersion_loss=0.0079
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7733 | ema=1.7387 | best_ema=1.7387 | no_improve=0
   🔬 Alpha Diversity: mean=9.50 | std=3.45 | range=[0.41, 16.00] | cap_hit=3.8%
   🏷️ Alpha Per-Asset  TOP: NVDA=11.48 | AMZN=11.10 | CAT=9.18  BOT: JPM=8.69 | XOM=8.41 | MSFT=8.22
   🎛️ Mixture Usage: C0=22.5% | C1=46.2% | C2=31.2%
   🧭 Regime Start Dist (train resets): high_vol=2 (25.0%), low_vol=4 (50.0%), medium_vol=2 (25.0%)
[CYCLE] Update 5/219 | Step 5,040/300,000 | Episode 4 | Time: 248.6s
   📊 Metrics: Return=+65.13% | Sharpe=1.453 | DD=18.11% | Turnover=30.37%
   🎚️ Intra-Step TAPE: potential=0.7189 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0742 | critic_loss=0.4419 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2209 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0010
   🧩 Mixture Head: gate_entropy=1.0397 | balance_loss=0.0002 | separation_loss=0.0034 | component_dispersion_loss=0.0081
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4529 | ema=1.7101 | best_ema=1.7101 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.668 | Return=+74.98% | DD=29.42%
         Multi-horizon: score=0.012 | details=252:-0.839/29.0%, 504:0.348/29.0%, 756:0.866/29.0%, 1008:0.668/29.4%
         SPY relative: spy_return=+41.94% | outperformance=+33.04%
         Equal-weight relative: ew_return=+147.79% | outperformance=-72.81%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-72.81%, required>0.00%).
[CYCLE] Update 6/219 | Step 6,048/300,000 | Episode 8 | Time: 605.0s
   📊 Metrics: Return=+41.72% | Sharpe=0.706 | DD=15.98% | Turnover=32.70%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0782 | critic_loss=0.2540 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1270 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0473 | balance_loss=0.0002 | separation_loss=0.0032 | component_dispersion_loss=0.0079
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7064 | ema=1.6098 | best_ema=1.6098 | no_improve=0
   🔬 Alpha Diversity: mean=9.45 | std=3.63 | range=[0.35, 16.00] | cap_hit=5.2%
   🏷️ Alpha Per-Asset  TOP: NVDA=11.92 | AMZN=10.83 | CAT=9.08  BOT: JPM=8.65 | XOM=7.89 | MSFT=7.57
   🎛️ Mixture Usage: C0=23.0% | C1=43.5% | C2=33.5%
   🧭 Regime Start Dist (train resets): high_vol=4 (33.3%), low_vol=4 (33.3%), medium_vol=4 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3860
   📈 Benchmark Relative: 1/N shaping=-0.033 (EW ret=0.00705) | SPY shaping=-0.011 (SPY ret=0.00509)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02166
[CYCLE] Update 7/219 | Step 7,056/300,000 | Episode 8 | Time: 652.2s
   📊 Metrics: Return=+6.32% | Sharpe=0.323 | DD=14.74% | Turnover=33.79%
   🎚️ Intra-Step TAPE: potential=0.6306 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0704 | critic_loss=0.1222 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0611 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0572 | balance_loss=0.0001 | separation_loss=0.0029 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3226 | ema=1.4811 | best_ema=1.4811 | no_improve=0
[CYCLE] Update 8/219 | Step 8,064/300,000 | Episode 8 | Time: 699.9s
   📊 Metrics: Return=+44.20% | Sharpe=1.128 | DD=14.74% | Turnover=31.99%
   🎚️ Intra-Step TAPE: potential=0.5201 | delta_reward=+0.0018
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0673 | critic_loss=0.2291 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1145 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0540 | balance_loss=0.0001 | separation_loss=0.0030 | component_dispersion_loss=0.0078
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1278 | ema=1.4457 | best_ema=1.4457 | no_improve=0
   🔬 Alpha Diversity: mean=8.59 | std=3.30 | range=[0.54, 16.00] | cap_hit=1.1%
   🏷️ Alpha Per-Asset  TOP: NVDA=10.25 | CAT=9.14 | AMZN=8.88  BOT: XOM=7.71 | MSFT=7.62 | JPM=7.49
   🎛️ Mixture Usage: C0=26.5% | C1=42.8% | C2=30.8%
   🧭 Regime Start Dist (train resets): high_vol=4 (33.3%), low_vol=4 (33.3%), medium_vol=4 (33.3%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02204
      🧪 Deterministic validation: Sharpe=0.412 | Return=+38.81% | DD=34.48%
         Multi-horizon: score=-0.227 | details=252:-1.017/34.5%, 504:0.115/34.5%, 756:0.592/34.5%, 1008:0.412/34.5%
         SPY relative: spy_return=+41.94% | outperformance=-3.13%
         Equal-weight relative: ew_return=+147.79% | outperformance=-108.98%
[CYCLE] Update 9/219 | Step 9,072/300,000 | Episode 12 | Time: 1057.2s
   📊 Metrics: Return=+30.34% | Sharpe=0.523 | DD=14.44% | Turnover=33.76%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0700 | critic_loss=0.1619 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0809 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0441 | balance_loss=0.0002 | separation_loss=0.0027 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5233 | ema=1.3535 | best_ema=1.3535 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3156
   📈 Benchmark Relative: 1/N shaping=-0.014 (EW ret=-0.00133) | SPY shaping=0.002 (SPY ret=-0.00335)
[CYCLE] Update 10/219 | Step 10,080/300,000 | Episode 12 | Time: 1104.6s
   📊 Metrics: Return=+12.67% | Sharpe=0.702 | DD=13.29% | Turnover=33.47%
   🎚️ Intra-Step TAPE: potential=0.5027 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0671 | critic_loss=0.1603 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0802 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0585 | balance_loss=0.0001 | separation_loss=0.0026 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7020 | ema=1.2883 | best_ema=1.2883 | no_improve=0
   🔬 Alpha Diversity: mean=7.51 | std=3.18 | range=[0.30, 16.00] | cap_hit=0.4%
   🏷️ Alpha Per-Asset  TOP: CAT=8.42 | NVDA=8.39 | XOM=8.14  BOT: AMZN=7.83 | MSFT=7.54 | JPM=6.62
   🎛️ Mixture Usage: C0=24.5% | C1=45.7% | C2=29.8%
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=5 (31.2%), medium_vol=7 (43.8%)
[CYCLE] Update 11/219 | Step 11,088/300,000 | Episode 12 | Time: 1152.0s
   📊 Metrics: Return=+28.74% | Sharpe=0.827 | DD=13.29% | Turnover=35.46%
   🎚️ Intra-Step TAPE: potential=0.7305 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0654 | critic_loss=0.1230 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0615 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0590 | balance_loss=0.0001 | separation_loss=0.0027 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8269 | ema=1.2422 | best_ema=1.2422 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.308 | Return=+26.74% | DD=34.48%
         Multi-horizon: score=-0.277 | details=252:-0.975/34.5%, 504:0.049/34.5%, 756:0.448/34.5%, 1008:0.308/34.5%
         SPY relative: spy_return=+41.94% | outperformance=-15.19%
         Equal-weight relative: ew_return=+147.79% | outperformance=-121.04%
[CYCLE] Update 12/219 | Step 12,096/300,000 | Episode 16 | Time: 1510.2s
   📊 Metrics: Return=+91.92% | Sharpe=1.338 | DD=15.60% | Turnover=34.63%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0657 | critic_loss=0.1462 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0731 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0535 | balance_loss=0.0001 | separation_loss=0.0027 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3378 | ema=1.2518 | best_ema=1.2518 | no_improve=0
   🔬 Alpha Diversity: mean=7.50 | std=3.03 | range=[0.50, 16.00] | cap_hit=0.2%
   🏷️ Alpha Per-Asset  TOP: NVDA=8.33 | CAT=8.14 | XOM=8.11  BOT: AMZN=7.46 | MSFT=7.22 | JPM=7.14
   🎛️ Mixture Usage: C0=25.9% | C1=42.7% | C2=31.4%
   🧭 Regime Start Dist (train resets): high_vol=5 (25.0%), low_vol=7 (35.0%), medium_vol=8 (40.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5704
   📈 Benchmark Relative: 1/N shaping=-0.015 (EW ret=-0.00609) | SPY shaping=-0.030 (SPY ret=-0.00205)
[CYCLE] Update 13/219 | Step 13,104/300,000 | Episode 16 | Time: 1557.9s
   📊 Metrics: Return=+50.75% | Sharpe=2.697 | DD=5.30% | Turnover=32.70%
   🎚️ Intra-Step TAPE: potential=0.7202 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0638 | critic_loss=0.1960 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0980 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0612 | balance_loss=0.0001 | separation_loss=0.0028 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.6973 | ema=1.3963 | best_ema=1.3963 | no_improve=0
[CYCLE] Update 14/219 | Step 14,112/300,000 | Episode 16 | Time: 1606.1s
   📊 Metrics: Return=+104.79% | Sharpe=2.642 | DD=5.79% | Turnover=32.35%
   🎚️ Intra-Step TAPE: potential=0.7503 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0645 | critic_loss=0.1738 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0869 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0561 | balance_loss=0.0001 | separation_loss=0.0028 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.6415 | ema=1.5208 | best_ema=1.5208 | no_improve=0
   🔬 Alpha Diversity: mean=7.50 | std=3.06 | range=[0.53, 16.00] | cap_hit=0.3%
   🏷️ Alpha Per-Asset  TOP: NVDA=8.25 | CAT=8.24 | MSFT=7.70  BOT: XOM=7.64 | AMZN=6.83 | JPM=6.50
   🎛️ Mixture Usage: C0=27.6% | C1=41.8% | C2=30.7%
   🧭 Regime Start Dist (train resets): high_vol=5 (25.0%), low_vol=7 (35.0%), medium_vol=8 (40.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02187
      🧪 Deterministic validation: Sharpe=0.386 | Return=+36.03% | DD=35.89%
         Multi-horizon: score=-0.308 | details=252:-1.041/35.9%, 504:-0.001/35.9%, 756:0.442/35.9%, 1008:0.386/35.9%
         SPY relative: spy_return=+41.94% | outperformance=-5.90%
         Equal-weight relative: ew_return=+147.79% | outperformance=-111.75%
[CYCLE] Update 15/219 | Step 15,120/300,000 | Episode 20 | Time: 1964.1s
   📊 Metrics: Return=+23.72% | Sharpe=0.412 | DD=16.32% | Turnover=34.27%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0646 | critic_loss=0.1472 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0736 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0473 | balance_loss=0.0001 | separation_loss=0.0025 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4123 | ema=1.4100 | best_ema=1.4100 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2804
   📈 Benchmark Relative: 1/N shaping=0.034 (EW ret=-0.02804) | SPY shaping=0.001 (SPY ret=-0.02394)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02250
[CYCLE] Update 16/219 | Step 16,128/300,000 | Episode 20 | Time: 2011.5s
   📊 Metrics: Return=+8.72% | Sharpe=0.583 | DD=7.38% | Turnover=33.75%
   🎚️ Intra-Step TAPE: potential=0.2679 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0615 | critic_loss=0.0601 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0301 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0482 | balance_loss=0.0002 | separation_loss=0.0029 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5833 | ema=1.3273 | best_ema=1.3273 | no_improve=0
   🔬 Alpha Diversity: mean=6.92 | std=3.03 | range=[0.49, 16.00] | cap_hit=0.2%
   🏷️ Alpha Per-Asset  TOP: NVDA=8.90 | CAT=7.76 | XOM=6.97  BOT: AMZN=6.86 | MSFT=5.89 | JPM=5.77
   🎛️ Mixture Usage: C0=23.6% | C1=46.7% | C2=29.7%
   🧭 Regime Start Dist (train resets): high_vol=8 (33.3%), low_vol=8 (33.3%), medium_vol=8 (33.3%)
[CYCLE] Update 17/219 | Step 17,136/300,000 | Episode 20 | Time: 2059.0s
   📊 Metrics: Return=+0.73% | Sharpe=-0.061 | DD=15.34% | Turnover=33.77%
   🎚️ Intra-Step TAPE: potential=0.2385 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0624 | critic_loss=0.0987 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0493 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0495 | balance_loss=0.0002 | separation_loss=0.0028 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0613 | ema=1.1884 | best_ema=1.1884 | no_improve=0
[CYCLE] Update 18/219 | Step 18,144/300,000 | Episode 24 | Time: 2107.2s
   📊 Metrics: Return=+119.67% | Sharpe=1.666 | DD=14.53% | Turnover=33.88%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0618 | critic_loss=0.1799 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0900 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0559 | balance_loss=0.0001 | separation_loss=0.0027 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6657 | ema=1.2362 | best_ema=1.2362 | no_improve=0
   🔬 Alpha Diversity: mean=6.46 | std=2.79 | range=[0.48, 15.93] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: NVDA=8.43 | XOM=6.64 | CAT=6.63  BOT: AMZN=6.24 | MSFT=5.82 | JPM=5.79
   🎛️ Mixture Usage: C0=28.0% | C1=42.8% | C2=29.3%
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=9 (32.1%), medium_vol=9 (32.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.6179
   📈 Benchmark Relative: 1/N shaping=0.007 (EW ret=-0.00499) | SPY shaping=-0.000 (SPY ret=-0.00405)
[CYCLE] Update 19/219 | Step 19,152/300,000 | Episode 24 | Time: 2155.1s
   📊 Metrics: Return=+16.71% | Sharpe=0.768 | DD=14.31% | Turnover=29.61%
   🎚️ Intra-Step TAPE: potential=0.2390 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0621 | critic_loss=0.1248 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0624 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0527 | balance_loss=0.0001 | separation_loss=0.0026 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7683 | ema=1.1894 | best_ema=1.1894 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02554
[CYCLE] Update 20/219 | Step 20,160/300,000 | Episode 24 | Time: 2203.1s
   📊 Metrics: Return=+46.41% | Sharpe=1.096 | DD=14.31% | Turnover=32.33%
   🎚️ Intra-Step TAPE: potential=0.2483 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0621 | critic_loss=0.0937 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0468 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0475 | balance_loss=0.0002 | separation_loss=0.0025 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0965 | ema=1.1801 | best_ema=1.1801 | no_improve=0
   🔬 Alpha Diversity: mean=6.44 | std=2.84 | range=[0.38, 15.99] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.97 | CAT=7.02 | XOM=6.26  BOT: MSFT=6.22 | JPM=5.82 | AMZN=5.21
   🎛️ Mixture Usage: C0=27.3% | C1=43.7% | C2=29.1%
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=9 (32.1%), medium_vol=9 (32.1%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02196
      🧪 Deterministic validation: Sharpe=0.397 | Return=+36.76% | DD=31.88%
         Multi-horizon: score=-0.132 | details=252:-0.727/31.9%, 504:0.120/31.9%, 756:0.533/31.9%, 1008:0.397/31.9%
         SPY relative: spy_return=+41.94% | outperformance=-5.18%
         Equal-weight relative: ew_return=+147.79% | outperformance=-111.03%
[CYCLE] Update 21/219 | Step 21,168/300,000 | Episode 28 | Time: 2560.5s
   📊 Metrics: Return=+56.02% | Sharpe=0.845 | DD=22.61% | Turnover=33.49%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0639 | critic_loss=0.1096 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0548 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0435 | balance_loss=0.0002 | separation_loss=0.0024 | component_dispersion_loss=0.0073
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8447 | ema=1.1466 | best_ema=1.1466 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4112
   📈 Benchmark Relative: 1/N shaping=0.064 (EW ret=-0.02361) | SPY shaping=-0.003 (SPY ret=-0.01498)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02818
[CYCLE] Update 22/219 | Step 22,176/300,000 | Episode 28 | Time: 2607.4s
   📊 Metrics: Return=-4.54% | Sharpe=-0.345 | DD=15.49% | Turnover=33.86%
   🎚️ Intra-Step TAPE: potential=0.4190 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0603 | critic_loss=0.1283 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0641 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0636 | balance_loss=0.0001 | separation_loss=0.0028 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3449 | ema=0.9974 | best_ema=0.9974 | no_improve=0
   🔬 Alpha Diversity: mean=6.25 | std=2.78 | range=[0.53, 15.72] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.18 | NVDA=7.12 | XOM=6.15  BOT: JPM=6.09 | MSFT=5.86 | AMZN=5.63
   🎛️ Mixture Usage: C0=29.8% | C1=40.8% | C2=29.5%
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=11 (34.4%), medium_vol=11 (34.4%)
[CYCLE] Update 23/219 | Step 23,184/300,000 | Episode 28 | Time: 2654.5s
   📊 Metrics: Return=+3.51% | Sharpe=0.050 | DD=15.49% | Turnover=34.40%
   🎚️ Intra-Step TAPE: potential=0.5323 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0587 | critic_loss=0.0720 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0360 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0650 | balance_loss=0.0001 | separation_loss=0.0025 | component_dispersion_loss=0.0073
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0500 | ema=0.9027 | best_ema=0.9027 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.466 | Return=+44.68% | DD=29.67%
         Multi-horizon: score=-0.025 | details=252:-0.643/29.7%, 504:0.291/29.7%, 756:0.585/29.7%, 1008:0.466/29.7%
         SPY relative: spy_return=+41.94% | outperformance=+2.75%
         Equal-weight relative: ew_return=+147.79% | outperformance=-103.10%
[CYCLE] Update 24/219 | Step 24,192/300,000 | Episode 32 | Time: 3009.4s
   📊 Metrics: Return=+1.17% | Sharpe=-0.046 | DD=13.57% | Turnover=35.05%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0607 | critic_loss=0.0935 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0468 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0717 | balance_loss=0.0001 | separation_loss=0.0027 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0465 | ema=0.8078 | best_ema=0.8078 | no_improve=0
   🔬 Alpha Diversity: mean=6.03 | std=2.64 | range=[0.38, 15.81] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.86 | XOM=6.38 | AMZN=6.20  BOT: JPM=6.15 | CAT=5.76 | MSFT=5.76
   🎛️ Mixture Usage: C0=30.7% | C1=38.7% | C2=30.7%
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=12 (33.3%), medium_vol=12 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2430
   📈 Benchmark Relative: 1/N shaping=-0.017 (EW ret=0.01396) | SPY shaping=0.037 (SPY ret=0.00449)
[CYCLE] Update 25/219 | Step 25,200/300,000 | Episode 32 | Time: 3056.3s
   📊 Metrics: Return=+15.98% | Sharpe=1.160 | DD=5.29% | Turnover=32.87%
   🎚️ Intra-Step TAPE: potential=0.6350 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0594 | critic_loss=0.0803 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0402 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0722 | balance_loss=0.0001 | separation_loss=0.0025 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1599 | ema=0.8430 | best_ema=0.8430 | no_improve=0
[CYCLE] Update 26/219 | Step 26,208/300,000 | Episode 32 | Time: 3103.5s
   📊 Metrics: Return=+8.46% | Sharpe=0.227 | DD=13.18% | Turnover=33.56%
   🎚️ Intra-Step TAPE: potential=0.2350 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0576 | critic_loss=0.1479 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0739 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0734 | balance_loss=0.0001 | separation_loss=0.0023 | component_dispersion_loss=0.0073
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2265 | ema=0.7813 | best_ema=0.7813 | no_improve=0
   🔬 Alpha Diversity: mean=5.90 | std=2.58 | range=[0.39, 15.29] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=7.33 | NVDA=6.21 | AMZN=6.15  BOT: XOM=5.94 | MSFT=5.67 | CAT=5.07
   🎛️ Mixture Usage: C0=32.6% | C1=38.8% | C2=28.6%
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=12 (33.3%), medium_vol=12 (33.3%)
      🧪 Deterministic validation: Sharpe=0.600 | Return=+60.13% | DD=28.71%
         Multi-horizon: score=-0.018 | details=252:-0.732/28.7%, 504:0.334/28.7%, 756:0.601/28.7%, 1008:0.600/28.7%
         SPY relative: spy_return=+41.94% | outperformance=+18.20%
         Equal-weight relative: ew_return=+147.79% | outperformance=-87.65%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-87.65%, required>0.00%).
[CYCLE] Update 27/219 | Step 27,216/300,000 | Episode 36 | Time: 3460.3s
   📊 Metrics: Return=+47.94% | Sharpe=0.742 | DD=28.66% | Turnover=33.62%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0604 | critic_loss=0.1084 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0542 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0642 | balance_loss=0.0001 | separation_loss=0.0024 | component_dispersion_loss=0.0073
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7418 | ema=0.7774 | best_ema=0.7774 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.009) | TAPE=0.3557
   📈 Benchmark Relative: 1/N shaping=-0.029 (EW ret=0.01879) | SPY shaping=0.029 (SPY ret=0.00935)
[CYCLE] Update 28/219 | Step 28,224/300,000 | Episode 36 | Time: 3509.1s
   📊 Metrics: Return=-15.99% | Sharpe=-0.847 | DD=25.41% | Turnover=35.43%
   🎚️ Intra-Step TAPE: potential=0.2312 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0610 | critic_loss=0.0797 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0398 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0664 | balance_loss=0.0001 | separation_loss=0.0026 | component_dispersion_loss=0.0073
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.8470 | ema=0.6149 | best_ema=0.6149 | no_improve=0
   🔬 Alpha Diversity: mean=6.04 | std=2.80 | range=[0.49, 15.99] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: JPM=6.81 | NVDA=6.63 | XOM=6.60  BOT: AMZN=6.10 | CAT=5.65 | MSFT=4.97
   🎛️ Mixture Usage: C0=33.8% | C1=40.9% | C2=25.3%
   🧭 Regime Start Dist (train resets): high_vol=13 (32.5%), low_vol=15 (37.5%), medium_vol=12 (30.0%)
[CYCLE] Update 29/219 | Step 29,232/300,000 | Episode 36 | Time: 3556.7s
   📊 Metrics: Return=+13.58% | Sharpe=0.298 | DD=29.49% | Turnover=34.07%
   🎚️ Intra-Step TAPE: potential=0.7198 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0595 | critic_loss=0.1031 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0516 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0558 | balance_loss=0.0001 | separation_loss=0.0030 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2985 | ema=0.5833 | best_ema=0.5833 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02308
      🧪 Deterministic validation: Sharpe=0.286 | Return=+23.44% | DD=32.25%
         Multi-horizon: score=-0.195 | details=252:-0.775/32.3%, 504:0.088/32.3%, 756:0.440/32.3%, 1008:0.286/32.3%
         SPY relative: spy_return=+41.94% | outperformance=-18.49%
         Equal-weight relative: ew_return=+147.79% | outperformance=-124.34%
[CYCLE] Update 30/219 | Step 30,240/300,000 | Episode 40 | Time: 3914.3s
   📊 Metrics: Return=+38.53% | Sharpe=0.666 | DD=17.26% | Turnover=32.37%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0610 | critic_loss=0.0650 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0325 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0543 | balance_loss=0.0001 | separation_loss=0.0026 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6664 | ema=0.5916 | best_ema=0.5916 | no_improve=0
   🔬 Alpha Diversity: mean=6.56 | std=2.89 | range=[0.49, 15.86] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: JPM=9.56 | MSFT=6.80 | AMZN=6.37  BOT: CAT=6.28 | NVDA=5.66 | XOM=5.51
   🎛️ Mixture Usage: C0=33.8% | C1=41.6% | C2=24.6%
   🧭 Regime Start Dist (train resets): high_vol=14 (31.8%), low_vol=16 (36.4%), medium_vol=14 (31.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3604
   📈 Benchmark Relative: 1/N shaping=-0.024 (EW ret=0.00207) | SPY shaping=-0.021 (SPY ret=0.00333)
[CYCLE] Update 31/219 | Step 31,248/300,000 | Episode 40 | Time: 3961.3s
   📊 Metrics: Return=+4.03% | Sharpe=0.198 | DD=18.51% | Turnover=32.33%
   🎚️ Intra-Step TAPE: potential=0.6585 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0620 | critic_loss=0.0962 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0481 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0647 | balance_loss=0.0001 | separation_loss=0.0032 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1983 | ema=0.5523 | best_ema=0.5523 | no_improve=0
[CYCLE] Update 32/219 | Step 32,256/300,000 | Episode 40 | Time: 4008.5s
   📊 Metrics: Return=+21.50% | Sharpe=0.426 | DD=28.85% | Turnover=32.15%
   🎚️ Intra-Step TAPE: potential=0.2366 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0582 | critic_loss=0.0806 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0403 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0603 | balance_loss=0.0001 | separation_loss=0.0031 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4261 | ema=0.5397 | best_ema=0.5397 | no_improve=0
   🔬 Alpha Diversity: mean=6.84 | std=2.65 | range=[0.57, 15.96] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: JPM=7.79 | CAT=7.48 | XOM=6.85  BOT: MSFT=6.57 | NVDA=6.46 | AMZN=5.03
   🎛️ Mixture Usage: C0=32.8% | C1=39.8% | C2=27.4%
   🧭 Regime Start Dist (train resets): high_vol=14 (31.8%), low_vol=16 (36.4%), medium_vol=14 (31.8%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02132
[CYCLE] Update 33/219 | Step 33,264/300,000 | Episode 44 | Time: 4055.6s
   📊 Metrics: Return=+69.60% | Sharpe=1.032 | DD=24.66% | Turnover=31.22%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0597 | critic_loss=0.0724 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0362 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0545 | balance_loss=0.0001 | separation_loss=0.0027 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0322 | ema=0.5889 | best_ema=0.5889 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4945
   📈 Benchmark Relative: 1/N shaping=-0.019 (EW ret=0.00558) | SPY shaping=-0.008 (SPY ret=0.00484)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02667
[CYCLE] Update 34/219 | Step 34,272/300,000 | Episode 44 | Time: 4102.7s
   📊 Metrics: Return=+4.58% | Sharpe=0.264 | DD=10.84% | Turnover=33.34%
   🎚️ Intra-Step TAPE: potential=0.2383 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0562 | critic_loss=0.0508 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0254 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0709 | balance_loss=0.0001 | separation_loss=0.0031 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2638 | ema=0.5564 | best_ema=0.5564 | no_improve=0
   🔬 Alpha Diversity: mean=6.23 | std=2.28 | range=[0.64, 15.37] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.60 | JPM=6.41 | AMZN=6.30  BOT: MSFT=6.23 | CAT=5.99 | XOM=5.78
   🎛️ Mixture Usage: C0=32.1% | C1=38.6% | C2=29.3%
   🧭 Regime Start Dist (train resets): high_vol=16 (33.3%), low_vol=16 (33.3%), medium_vol=16 (33.3%)
[CYCLE] Update 35/219 | Step 35,280/300,000 | Episode 44 | Time: 4150.1s
   📊 Metrics: Return=+8.35% | Sharpe=0.211 | DD=15.52% | Turnover=32.35%
   🎚️ Intra-Step TAPE: potential=0.7465 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0582 | critic_loss=0.0589 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0294 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0647 | balance_loss=0.0001 | separation_loss=0.0032 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2112 | ema=0.5219 | best_ema=0.5219 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.743 | Return=+80.43% | DD=28.69%
         Multi-horizon: score=0.195 | details=252:-0.292/28.7%, 504:0.352/28.7%, 756:0.760/28.7%, 1008:0.743/28.7%
         SPY relative: spy_return=+41.94% | outperformance=+38.50%
         Equal-weight relative: ew_return=+147.79% | outperformance=-67.35%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-67.35%, required>0.00%).
[CYCLE] Update 36/219 | Step 36,288/300,000 | Episode 48 | Time: 4507.9s
   📊 Metrics: Return=+62.32% | Sharpe=0.926 | DD=25.83% | Turnover=30.39%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0594 | critic_loss=0.0499 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0250 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0682 | balance_loss=0.0001 | separation_loss=0.0030 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9255 | ema=0.5622 | best_ema=0.5622 | no_improve=0
   🔬 Alpha Diversity: mean=6.19 | std=2.54 | range=[0.54, 15.99] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.44 | MSFT=6.40 | JPM=6.14  BOT: XOM=5.91 | CAT=5.87 | AMZN=5.14
   🎛️ Mixture Usage: C0=30.2% | C1=40.6% | C2=29.3%
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=18 (34.6%), medium_vol=17 (32.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.001) | TAPE=0.4611
   📈 Benchmark Relative: 1/N shaping=-0.013 (EW ret=0.00782) | SPY shaping=-0.013 (SPY ret=0.00876)
[CYCLE] Update 37/219 | Step 37,296/300,000 | Episode 48 | Time: 4554.9s
   📊 Metrics: Return=+35.04% | Sharpe=2.095 | DD=7.33% | Turnover=30.96%
   🎚️ Intra-Step TAPE: potential=0.6304 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0563 | critic_loss=0.0422 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0211 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0713 | balance_loss=0.0001 | separation_loss=0.0029 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.0950 | ema=0.7155 | best_ema=0.7155 | no_improve=0
[CYCLE] Update 38/219 | Step 38,304/300,000 | Episode 48 | Time: 4602.1s
   📊 Metrics: Return=+26.41% | Sharpe=0.614 | DD=26.05% | Turnover=31.09%
   🎚️ Intra-Step TAPE: potential=0.2919 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0569 | critic_loss=0.0622 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0311 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0716 | balance_loss=0.0001 | separation_loss=0.0027 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6144 | ema=0.7054 | best_ema=0.7054 | no_improve=0
   🔬 Alpha Diversity: mean=5.73 | std=2.37 | range=[0.64, 15.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=6.13 | JPM=6.04 | NVDA=5.89  BOT: CAT=5.60 | AMZN=5.32 | XOM=4.68
   🎛️ Mixture Usage: C0=32.8% | C1=38.5% | C2=28.7%
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=18 (34.6%), medium_vol=17 (32.7%)
      🧪 Deterministic validation: Sharpe=0.529 | Return=+50.20% | DD=29.39%
         Multi-horizon: score=-0.105 | details=252:-0.742/29.4%, 504:0.127/29.4%, 756:0.553/29.4%, 1008:0.529/29.4%
         SPY relative: spy_return=+41.94% | outperformance=+8.27%
         Equal-weight relative: ew_return=+147.79% | outperformance=-97.58%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-97.58%, required>0.00%).
[CYCLE] Update 39/219 | Step 39,312/300,000 | Episode 52 | Time: 4959.4s
   📊 Metrics: Return=+8.88% | Sharpe=0.131 | DD=14.56% | Turnover=33.79%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0582 | critic_loss=0.0470 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0235 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0687 | balance_loss=0.0001 | separation_loss=0.0031 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1314 | ema=0.6480 | best_ema=0.6480 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2520
   📈 Benchmark Relative: 1/N shaping=-0.031 (EW ret=0.01111) | SPY shaping=-0.007 (SPY ret=0.00867)
[CYCLE] Update 40/219 | Step 40,320/300,000 | Episode 52 | Time: 5006.1s
   📊 Metrics: Return=+4.44% | Sharpe=0.247 | DD=12.22% | Turnover=31.75%
   🎚️ Intra-Step TAPE: potential=0.2421 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0578 | critic_loss=0.0417 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0208 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0698 | balance_loss=0.0001 | separation_loss=0.0030 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2467 | ema=0.6079 | best_ema=0.6079 | no_improve=0
   🔬 Alpha Diversity: mean=5.84 | std=2.50 | range=[0.57, 15.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=6.12 | AMZN=5.92 | NVDA=5.88  BOT: CAT=5.83 | JPM=5.74 | XOM=5.37
   🎛️ Mixture Usage: C0=30.5% | C1=41.4% | C2=28.2%
   🧭 Regime Start Dist (train resets): high_vol=18 (32.1%), low_vol=19 (33.9%), medium_vol=19 (33.9%)
[CYCLE] Update 41/219 | Step 41,328/300,000 | Episode 52 | Time: 5053.1s
   📊 Metrics: Return=+13.68% | Sharpe=0.362 | DD=15.28% | Turnover=31.52%
   🎚️ Intra-Step TAPE: potential=0.7479 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0574 | critic_loss=0.0455 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0228 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0691 | balance_loss=0.0001 | separation_loss=0.0028 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3622 | ema=0.5833 | best_ema=0.5833 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.04215
      🧪 Deterministic validation: Sharpe=0.471 | Return=+44.85% | DD=38.54%
         Multi-horizon: score=-0.330 | details=252:-1.031/38.5%, 504:-0.110/38.5%, 756:0.445/38.5%, 1008:0.471/38.5%
         SPY relative: spy_return=+41.94% | outperformance=+2.92%
         Equal-weight relative: ew_return=+147.79% | outperformance=-102.93%
[CYCLE] Update 42/219 | Step 42,336/300,000 | Episode 56 | Time: 5408.4s
   📊 Metrics: Return=+55.76% | Sharpe=0.652 | DD=26.31% | Turnover=33.28%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0570 | critic_loss=0.0456 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0228 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0643 | balance_loss=0.0001 | separation_loss=0.0027 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6515 | ema=0.5901 | best_ema=0.5901 | no_improve=0
   🔬 Alpha Diversity: mean=5.80 | std=2.52 | range=[0.52, 15.91] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=7.21 | MSFT=6.50 | XOM=6.13  BOT: AMZN=5.81 | CAT=5.60 | NVDA=5.11
   🎛️ Mixture Usage: C0=36.9% | C1=36.2% | C2=26.9%
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=20 (33.3%), medium_vol=20 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.002) | TAPE=0.3305
   📈 Benchmark Relative: 1/N shaping=-0.011 (EW ret=-0.00002) | SPY shaping=0.021 (SPY ret=-0.00558)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03848
[CYCLE] Update 43/219 | Step 43,344/300,000 | Episode 56 | Time: 5455.4s
   📊 Metrics: Return=-9.88% | Sharpe=-0.719 | DD=17.14% | Turnover=31.36%
   🎚️ Intra-Step TAPE: potential=0.2353 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0565 | critic_loss=0.0868 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0434 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0726 | balance_loss=0.0000 | separation_loss=0.0027 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.7186 | ema=0.4593 | best_ema=0.4593 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03507
[CYCLE] Update 44/219 | Step 44,352/300,000 | Episode 56 | Time: 5502.8s
   📊 Metrics: Return=+6.42% | Sharpe=0.150 | DD=17.14% | Turnover=32.47%
   🎚️ Intra-Step TAPE: potential=0.3869 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0587 | critic_loss=0.0524 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0262 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0696 | balance_loss=0.0000 | separation_loss=0.0025 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1505 | ema=0.4284 | best_ema=0.4284 | no_improve=0
   🔬 Alpha Diversity: mean=6.00 | std=2.45 | range=[0.44, 15.70] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: XOM=6.98 | JPM=6.89 | NVDA=6.76  BOT: AMZN=5.72 | CAT=5.22 | MSFT=5.12
   🎛️ Mixture Usage: C0=34.5% | C1=37.9% | C2=27.6%
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=20 (33.3%), medium_vol=20 (33.3%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.04490
      🧪 Deterministic validation: Sharpe=0.522 | Return=+50.99% | DD=35.18%
         Multi-horizon: score=-0.159 | details=252:-0.715/35.2%, 504:0.050/35.2%, 756:0.430/35.2%, 1008:0.522/35.2%
         SPY relative: spy_return=+41.94% | outperformance=+9.05%
         Equal-weight relative: ew_return=+147.79% | outperformance=-96.80%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-96.80%, required>0.00%).
[CYCLE] Update 45/219 | Step 45,360/300,000 | Episode 60 | Time: 5858.5s
   📊 Metrics: Return=+60.87% | Sharpe=0.671 | DD=29.84% | Turnover=34.77%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0587 | critic_loss=0.0452 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0226 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0604 | balance_loss=0.0001 | separation_loss=0.0025 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6711 | ema=0.4527 | best_ema=0.4527 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.020) | TAPE=0.3313
   📈 Benchmark Relative: 1/N shaping=-0.040 (EW ret=0.01721) | SPY shaping=0.057 (SPY ret=0.00090)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03974
[CYCLE] Update 46/219 | Step 46,368/300,000 | Episode 60 | Time: 5905.7s
   📊 Metrics: Return=+10.55% | Sharpe=0.513 | DD=17.14% | Turnover=33.98%
   🎚️ Intra-Step TAPE: potential=0.7474 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0567 | critic_loss=0.0394 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0197 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0627 | balance_loss=0.0001 | separation_loss=0.0026 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5134 | ema=0.4587 | best_ema=0.4587 | no_improve=0
   🔬 Alpha Diversity: mean=5.84 | std=2.27 | range=[0.85, 13.86] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=6.49 | XOM=6.34 | CAT=6.32  BOT: MSFT=6.00 | NVDA=5.45 | AMZN=4.60
   🎛️ Mixture Usage: C0=36.6% | C1=38.9% | C2=24.5%
   🧭 Regime Start Dist (train resets): high_vol=20 (31.2%), low_vol=22 (34.4%), medium_vol=22 (34.4%)
[CYCLE] Update 47/219 | Step 47,376/300,000 | Episode 60 | Time: 5953.1s
   📊 Metrics: Return=+39.67% | Sharpe=0.994 | DD=17.14% | Turnover=33.52%
   🎚️ Intra-Step TAPE: potential=0.2256 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0578 | critic_loss=0.0317 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0159 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0592 | balance_loss=0.0001 | separation_loss=0.0026 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9936 | ema=0.5122 | best_ema=0.5122 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03144
[CYCLE] Update 48/219 | Step 48,384/300,000 | Episode 64 | Time: 6000.3s
   📊 Metrics: Return=+24.07% | Sharpe=0.387 | DD=27.69% | Turnover=32.19%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0612 | critic_loss=0.0802 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0401 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0515 | balance_loss=0.0001 | separation_loss=0.0026 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3865 | ema=0.4996 | best_ema=0.4996 | no_improve=0
   🔬 Alpha Diversity: mean=6.40 | std=2.56 | range=[0.45, 15.91] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: XOM=7.67 | MSFT=7.52 | CAT=6.47  BOT: JPM=6.14 | NVDA=6.08 | AMZN=5.28
   🎛️ Mixture Usage: C0=35.7% | C1=38.3% | C2=26.0%
   🧭 Regime Start Dist (train resets): high_vol=20 (29.4%), low_vol=24 (35.3%), medium_vol=24 (35.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.003) | TAPE=0.2467
   📈 Benchmark Relative: 1/N shaping=-0.025 (EW ret=-0.00142) | SPY shaping=-0.019 (SPY ret=-0.00083)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02846
[CYCLE] Update 49/219 | Step 49,392/300,000 | Episode 64 | Time: 6047.1s
   📊 Metrics: Return=-6.16% | Sharpe=-0.298 | DD=23.55% | Turnover=32.18%
   🎚️ Intra-Step TAPE: potential=0.2242 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0552 | critic_loss=0.0592 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0296 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0608 | balance_loss=0.0001 | separation_loss=0.0030 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2981 | ema=0.4199 | best_ema=0.4199 | no_improve=0

📚 EPISODE HORIZON UPDATE at 50,400 steps:
   Episode horizon: 766 steps
[CYCLE] Update 50/219 | Step 50,400/300,000 | Episode 64 | Time: 6094.2s
   📊 Metrics: Return=+20.06% | Sharpe=0.473 | DD=23.55% | Turnover=30.20%
   🎚️ Intra-Step TAPE: potential=0.7436 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0571 | critic_loss=0.0689 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0344 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0610 | balance_loss=0.0001 | separation_loss=0.0033 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4730 | ema=0.4252 | best_ema=0.4252 | no_improve=0
   🔬 Alpha Diversity: mean=5.80 | std=2.52 | range=[0.48, 15.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.12 | XOM=6.66 | CAT=5.45  BOT: AMZN=5.38 | JPM=4.81 | MSFT=4.66
   🎛️ Mixture Usage: C0=29.7% | C1=45.2% | C2=25.1%
   🧭 Regime Start Dist (train resets): high_vol=20 (29.4%), low_vol=24 (35.3%), medium_vol=24 (35.3%)

📚 EPISODE HORIZON UPDATE at 51,408 steps:
   Episode horizon: 791 steps
[CYCLE] Update 51/219 | Step 51,408/300,000 | Episode 64 | Time: 6141.3s
   📊 Metrics: Return=+60.87% | Sharpe=0.669 | DD=27.20% | Turnover=30.80%
   🎚️ Intra-Step TAPE: potential=0.6627 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0562 | critic_loss=0.0766 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0383 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0634 | balance_loss=0.0001 | separation_loss=0.0031 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6690 | ema=0.4496 | best_ema=0.4496 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.318 | Return=+26.87% | DD=32.27%
         Multi-horizon: score=-0.246 | details=252:-0.877/32.3%, 504:0.111/32.3%, 756:0.302/32.3%, 1008:0.318/32.3%
         SPY relative: spy_return=+41.94% | outperformance=-15.07%
         Equal-weight relative: ew_return=+147.79% | outperformance=-120.92%

📚 EPISODE HORIZON UPDATE at 52,416 steps:
   Episode horizon: 817 steps
[CYCLE] Update 52/219 | Step 52,416/300,000 | Episode 68 | Time: 6497.3s
   📊 Metrics: Return=+6.85% | Sharpe=0.077 | DD=14.99% | Turnover=30.98%
   🎚️ Intra-Step TAPE: potential=0.3235 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0576 | critic_loss=0.0674 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0337 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0632 | balance_loss=0.0001 | separation_loss=0.0032 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0774 | ema=0.4124 | best_ema=0.4124 | no_improve=0
   🔬 Alpha Diversity: mean=5.39 | std=2.25 | range=[0.64, 14.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.68 | XOM=5.99 | MSFT=5.53  BOT: JPM=5.30 | AMZN=4.63 | CAT=4.55
   🎛️ Mixture Usage: C0=34.0% | C1=39.1% | C2=26.9%
   🧭 Regime Start Dist (train resets): high_vol=24 (33.3%), low_vol=24 (33.3%), medium_vol=24 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 6.73% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2490
   📈 Benchmark Relative: 1/N shaping=0.004 (EW ret=0.00040) | SPY shaping=0.004 (SPY ret=0.00019)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02468

📚 EPISODE HORIZON UPDATE at 53,424 steps:
   Episode horizon: 842 steps
[CYCLE] Update 53/219 | Step 53,424/300,000 | Episode 68 | Time: 6544.7s
   📊 Metrics: Return=+19.84% | Sharpe=0.410 | DD=29.69% | Turnover=29.87%
   🎚️ Intra-Step TAPE: potential=0.6663 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0557 | critic_loss=0.0427 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0214 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0657 | balance_loss=0.0001 | separation_loss=0.0030 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4098 | ema=0.4121 | best_ema=0.4121 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02335

📚 EPISODE HORIZON UPDATE at 54,432 steps:
   Episode horizon: 868 steps
[CYCLE] Update 54/219 | Step 54,432/300,000 | Episode 68 | Time: 6592.2s
   📊 Metrics: Return=+48.44% | Sharpe=0.585 | DD=29.69% | Turnover=32.02%
   🎚️ Intra-Step TAPE: potential=0.4331 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0552 | critic_loss=0.0502 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0251 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0586 | balance_loss=0.0001 | separation_loss=0.0031 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5853 | ema=0.4294 | best_ema=0.4294 | no_improve=0
   🔬 Alpha Diversity: mean=5.50 | std=2.18 | range=[0.55, 15.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=6.77 | XOM=5.77 | JPM=5.73  BOT: CAT=5.64 | AMZN=4.99 | NVDA=4.87
   🎛️ Mixture Usage: C0=38.1% | C1=36.6% | C2=25.3%
   🧭 Regime Start Dist (train resets): high_vol=24 (33.3%), low_vol=24 (33.3%), medium_vol=24 (33.3%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02106
      🧪 Deterministic validation: Sharpe=0.329 | Return=+28.00% | DD=32.93%
         Multi-horizon: score=-0.292 | details=252:-1.038/32.9%, 504:0.105/32.9%, 756:0.367/32.9%, 1008:0.329/32.9%
         SPY relative: spy_return=+41.94% | outperformance=-13.94%
         Equal-weight relative: ew_return=+147.79% | outperformance=-119.79%

📚 EPISODE HORIZON UPDATE at 55,440 steps:
   Episode horizon: 893 steps
[CYCLE] Update 55/219 | Step 55,440/300,000 | Episode 72 | Time: 6948.4s
   📊 Metrics: Return=+102.40% | Sharpe=1.235 | DD=14.42% | Turnover=30.70%
   🎚️ Intra-Step TAPE: potential=0.2650 | delta_reward=-0.0032
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0542 | critic_loss=0.1450 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0725 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0603 | balance_loss=0.0001 | separation_loss=0.0033 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2352 | ema=0.5100 | best_ema=0.5100 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 9.62% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5629
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=0.00327) | SPY shaping=-0.007 (SPY ret=0.00429)

📚 EPISODE HORIZON UPDATE at 56,448 steps:
   Episode horizon: 918 steps
[CYCLE] Update 56/219 | Step 56,448/300,000 | Episode 72 | Time: 6995.6s
   📊 Metrics: Return=+4.17% | Sharpe=0.121 | DD=26.40% | Turnover=30.84%
   🎚️ Intra-Step TAPE: potential=0.2368 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0557 | critic_loss=0.0421 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0211 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0009 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0635 | balance_loss=0.0001 | separation_loss=0.0032 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1213 | ema=0.4711 | best_ema=0.4711 | no_improve=0
   🔬 Alpha Diversity: mean=5.22 | std=2.05 | range=[0.72, 14.49] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.36 | MSFT=5.41 | XOM=5.38  BOT: JPM=5.24 | CAT=5.19 | AMZN=4.06
   🎛️ Mixture Usage: C0=38.1% | C1=36.8% | C2=25.1%
   🧭 Regime Start Dist (train resets): high_vol=26 (34.2%), low_vol=24 (31.6%), medium_vol=26 (34.2%)

📚 EPISODE HORIZON UPDATE at 57,456 steps:
   Episode horizon: 944 steps
[CYCLE] Update 57/219 | Step 57,456/300,000 | Episode 72 | Time: 7043.0s
   📊 Metrics: Return=+29.96% | Sharpe=0.530 | DD=26.40% | Turnover=30.98%
   🎚️ Intra-Step TAPE: potential=0.6861 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0568 | critic_loss=0.0418 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0209 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0556 | balance_loss=0.0001 | separation_loss=0.0029 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5298 | ema=0.4770 | best_ema=0.4770 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.04250

📚 EPISODE HORIZON UPDATE at 58,464 steps:
   Episode horizon: 969 steps
[CYCLE] Update 58/219 | Step 58,464/300,000 | Episode 72 | Time: 7090.3s
   📊 Metrics: Return=+66.62% | Sharpe=0.616 | DD=29.24% | Turnover=31.39%
   🎚️ Intra-Step TAPE: potential=0.7407 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0560 | critic_loss=0.0367 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0184 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0484 | balance_loss=0.0001 | separation_loss=0.0027 | component_dispersion_loss=0.0075
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6164 | ema=0.4909 | best_ema=0.4909 | no_improve=0
   🔬 Alpha Diversity: mean=5.29 | std=2.21 | range=[0.57, 15.29] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=5.92 | NVDA=5.79 | XOM=5.65  BOT: CAT=5.55 | AMZN=5.53 | MSFT=4.92
   🎛️ Mixture Usage: C0=39.8% | C1=37.7% | C2=22.5%
   🧭 Regime Start Dist (train resets): high_vol=26 (34.2%), low_vol=24 (31.6%), medium_vol=26 (34.2%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03794
      🧪 Deterministic validation: Sharpe=0.428 | Return=+40.14% | DD=32.77%
         Multi-horizon: score=-0.273 | details=252:-1.047/32.8%, 504:0.043/32.8%, 756:0.490/32.8%, 1008:0.428/32.8%
         SPY relative: spy_return=+41.94% | outperformance=-1.79%
         Equal-weight relative: ew_return=+147.79% | outperformance=-107.64%

📚 EPISODE HORIZON UPDATE at 59,472 steps:
   Episode horizon: 995 steps
[CYCLE] Update 59/219 | Step 59,472/300,000 | Episode 76 | Time: 7445.6s
   📊 Metrics: Return=+85.47% | Sharpe=0.711 | DD=29.98% | Turnover=32.07%
   🎚️ Intra-Step TAPE: potential=0.5676 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0552 | critic_loss=0.0851 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0426 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0537 | balance_loss=0.0001 | separation_loss=0.0026 | component_dispersion_loss=0.0074
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7106 | ema=0.5129 | best_ema=0.5129 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.12% / trig 25.00%) | terminal=0.000 (peak 0.018) | TAPE=0.3370
   📈 Benchmark Relative: 1/N shaping=-0.037 (EW ret=0.01862) | SPY shaping=-0.008 (SPY ret=0.01563)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03456

📚 TURNOVER CURRICULUM UPDATE at 60,480 steps:
   Turnover penalty scalar: 0.15

🎛️ EXECUTION BETA UPDATE at 60,480 steps:
   action_execution_beta: 0.650 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 60,480 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 60/219 | Step 60,480/300,000 | Episode 76 | Time: 7492.7s
   📊 Metrics: Return=+50.19% | Sharpe=1.360 | DD=16.75% | Turnover=32.87%
   🎚️ Intra-Step TAPE: potential=0.5224 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0551 | critic_loss=0.0381 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0190 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0482 | balance_loss=0.0001 | separation_loss=0.0030 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3598 | ema=0.5976 | best_ema=0.5976 | no_improve=0
   🔬 Alpha Diversity: mean=5.08 | std=1.86 | range=[0.84, 13.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=6.01 | NVDA=5.58 | JPM=5.40  BOT: MSFT=5.05 | XOM=4.79 | AMZN=4.57
   🎛️ Mixture Usage: C0=38.1% | C1=36.6% | C2=25.3%
   🧭 Regime Start Dist (train resets): high_vol=27 (33.8%), low_vol=27 (33.8%), medium_vol=26 (32.5%)
[CYCLE] Update 61/219 | Step 61,488/300,000 | Episode 76 | Time: 7540.2s
   📊 Metrics: Return=+87.23% | Sharpe=1.327 | DD=16.75% | Turnover=36.53%
   🎚️ Intra-Step TAPE: potential=0.2976 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0545 | critic_loss=0.0416 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0208 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0394 | balance_loss=0.0001 | separation_loss=0.0031 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3272 | ema=0.6706 | best_ema=0.6706 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.04383
[CYCLE] Update 62/219 | Step 62,496/300,000 | Episode 76 | Time: 7588.3s
   📊 Metrics: Return=+57.50% | Sharpe=0.638 | DD=29.70% | Turnover=37.21%
   🎚️ Intra-Step TAPE: potential=0.2972 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0590 | critic_loss=0.0276 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0009
   🧩 Mixture Head: gate_entropy=1.0412 | balance_loss=0.0001 | separation_loss=0.0031 | component_dispersion_loss=0.0077
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6384 | ema=0.6673 | best_ema=0.6673 | no_improve=0
   🔬 Alpha Diversity: mean=5.43 | std=2.17 | range=[0.49, 15.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=6.33 | NVDA=6.08 | AMZN=5.70  BOT: XOM=5.33 | MSFT=5.08 | CAT=4.79
   🎛️ Mixture Usage: C0=33.0% | C1=43.3% | C2=23.7%
   🧭 Regime Start Dist (train resets): high_vol=27 (33.8%), low_vol=27 (33.8%), medium_vol=26 (32.5%)
   🔐 Lagrangian CVaR: λ=0.0012 | penalty=-0.0000 | rolling_cvar=-0.03934
      🧪 Deterministic validation: Sharpe=0.499 | Return=+48.21% | DD=35.17%
         Multi-horizon: score=-0.333 | details=252:-1.274/35.2%, 504:0.040/35.2%, 756:0.568/35.2%, 1008:0.499/35.2%
         SPY relative: spy_return=+41.94% | outperformance=+6.28%
         Equal-weight relative: ew_return=+147.79% | outperformance=-99.57%
[CYCLE] Update 63/219 | Step 63,504/300,000 | Episode 80 | Time: 7945.8s
   📊 Metrics: Return=+47.84% | Sharpe=0.448 | DD=37.69% | Turnover=38.51%
   🎚️ Intra-Step TAPE: potential=0.2160 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0541 | critic_loss=0.0433 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0216 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0008
   🧩 Mixture Head: gate_entropy=1.0476 | balance_loss=0.0001 | separation_loss=0.0030 | component_dispersion_loss=0.0076
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4291 | ema=0.6435 | best_ema=0.6435 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 10.37% / trig 25.00%) | terminal=0.000 (peak 0.138) | TAPE=0.2594
   📈 Benchmark Relative: 1/N shaping=0.029 (EW ret=-0.00459) | SPY shaping=0.036 (SPY ret=-0.00825)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03280