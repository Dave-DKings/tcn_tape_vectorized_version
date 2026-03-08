# src/config.py
import numpy as np # type: ignore
import os
import copy

# --- GENERAL PROJECT SETTINGS ---
PROJECT_NAME = "AdaptivePortfolioRL_Prototype"
RANDOM_SEED = 42
TF_DEVICE = "/gpu:0" if len(os.environ.get("CUDA_VISIBLE_DEVICES", "")) > 0 else "/cpu:0"

# --- DATA PATHS ---
BASE_PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BASE_DATA_PATH = os.path.join(BASE_PROJECT_PATH, 'data')

PATH_DAILY_OHLCV = os.path.join(BASE_DATA_PATH, "daily_ohlcv_assets.csv")  # Cache created on first successful download
PATH_PROCESSED_MACRO_DAILY_ALIGNED = os.path.join(BASE_DATA_PATH, "processed_daily_macro_features.csv")

# --- API KEYS ---
#ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "GETO31F8UHB3OWB3")
ALPHA_VANTAGE_API_KEY = "GETO31F8UHB3OWB3"

# --- DATA DATE RANGES ---
DATA_FETCH_START_DATE = "2003-09-02"  # Paper-aligned start
DATA_FETCH_END_DATE = "2025-09-01"  # Extended test horizon
ANALYSIS_START_DATE = "2003-09-02"
ANALYSIS_END_DATE = "2025-09-01"

# --- TRAIN/TEST SPLIT ---
# Two supported split presets:
# - Benchmark (paper-aligned train cutoff)
# - COVID stress test (test starts 2020-01-01)
TRAIN_TEST_SPLIT_DATE_BENCHMARK = "2021-09-01"     # Train: <= 2021-09-01
TRAIN_TEST_SPLIT_DATE_COVID_STRESS = "2019-12-31"  # Train: <= 2019-12-31
TRAIN_TEST_SPLIT_DATE = TRAIN_TEST_SPLIT_DATE_BENCHMARK

# --- ASSET CONFIGURATION ---
ASSET_TICKERS = ["MSFT", "GOOGL", "JPM", "JNJ", "XOM", "PG", "NEE", "LIN", "CAT", "UNH"] 
NUM_ASSETS = len(ASSET_TICKERS)
CASH_ASSET_NAME = "CASH"

# --- PORTFOLIO INITIALIZATION ---
# Options: 'equal', 'volume_weighted', 'custom'
INITIAL_WEIGHTS_METHOD = "volume_weighted"  # Use volume-based weighting
MARKET_CAP_CASH_ALLOCATION = 0.02  # 2% cash allocation for volume weighting
EQUAL_WEIGHT_CASH_ALLOCATION = 1.0 / (NUM_ASSETS + 1)  # Equal split across assets plus cash

# --- FEATURE ENGINEERING CONFIGURATION (TEMPLATES) ---
TECHNICAL_INDICATORS_CONFIG = [
    # Retained technical indicators only (feature-audit active set).
    {"name": "MACD", "params": {"fast": 12, "slow": 26, "signal": 9}, "output_cols": ["MACDh_12_26_9"]},
    {"name": "RSI", "params": {"length": 14}, "output_cols": ["RSI_14"]},
    {"name": "STOCH", "params": {"k": 14, "d": 3, "smooth_k": 3}, "output_cols": ["STOCHd_14_3_3"]},
    {"name": "ADX", "params": {"length": 14}, "output_cols": ["ADX_14"]},
    {"name": "NATR", "params": {"length": 14}, "output_cols": ["NATR_14"]},
    {"name": "MFI", "params": {"length": 14}, "output_cols": ["MFI_14"]},
]

CANDLESTICK_FEATURES_CONFIG = {
    "enabled": True,
    # Numeric safety epsilon for divide operations (range/body ratios).
    "eps": 1e-8,
    # Winsor-like clipping to keep tails bounded before normalization.
    "clip_abs": 5.0,
    "include_gap_open": True,
}

TEMPORAL_FORECAST_PARAMS = {
    "sequence_length": 20, "epochs": 2, "batch_size": 32, "learning_rate": 0.01,  # Reduced epochs for faster testing "dropout_rate": 0.2
}

DYNAMIC_COVARIANCE_PARAMS = {
    "covariance_window_length": 60, "feature_extraction_methods": ["eigenvalues"],
    # Keep only active covariance channels.
    "num_eigenvalues": min(2, NUM_ASSETS)
}

ACTUARIAL_PARAMS = {
    "enabled": True,
    "severity_buckets": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
    "development_horizons": [10, 20, 30, 60, 90, 120],
    "min_events_for_credibility": 5
}

FUNDAMENTAL_FEATURES_CONFIG = {
    "enabled": False,
    # CSV expected to contain columns: Date, Ticker, FCFE, Revenue, NCFO
    "data_path": os.path.join(BASE_DATA_PATH, "quarterly_fundamentals.csv"),
    "lag_quarters": 8,
    "staleness_days_normalizer": 90.0
}

# Canonical Exp6 feature-audit active set.
# This is enforced via allowlist to keep training/evaluation deterministic.
# Non-actuarial count: 55 (includes 3 regime-buy features)
# Total count: 59 (55 + 4 actuarial)
PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL = [
    # Returns + risk moments
    "LogReturn_1d",
    "LogReturn_5d",
    "LogReturn_10d",
    "LogReturn_21d",
    "RollingVolatility_21d",
    "DownsideSemiVar_21d",
    "RealizedSkew_21d",
    "RealizedKurtosis_21d",
    # Technical indicators
    "MACDh_12_26_9",
    "RSI_14",
    "STOCHd_14_3_3",
    "ADX_14",
    "NATR_14",
    "MFI_14",
    # Candlestick geometry
    "Candle_Body",
    "Candle_UpperWick",
    "Candle_LowerWick",
    "Candle_Range",
    "Candle_BodyToRange",
    "Candle_CloseLocation",
    "Candle_GapOpen",
    # Regime/cross-sectional alpha
    "Regime_Volatility_Ratio",
    "Regime_Price_vs_SMA_Short",
    "Regime_SMA_Short_Slope",
    "Regime_SMA_Long_Slope",
    "Regime_Momentum_Short",
    "Regime_Momentum_Long",
    "Regime_Corr_to_Market",
    "Regime_Breadth_Positive",
    "CrossSectional_ZScore_LogReturn_1d",
    "Residual_Momentum_21",
    "Volume_Percentile_63",
    "ShortTerm_Reversal_5",
    "VolOfVol_63",
    "Beta_to_Market",
    "OBV_Delta_Norm_21",
    # Covariance
    "Covariance_Eigenvalue_0",
    "Covariance_Eigenvalue_1",
    # Yield-curve / rates / inflation / credit / implied vol
    "YieldCurve_Spread",
    "YieldCurve_Inverted_Flag",
    "SOFR_diff",
    "DGS10_level",
    "DGS10_diff",
    "T10Y2Y_level",
    "TIPS10Y_level",
    "TIPS10Y_diff",
    "BreakevenInf10Y_level",
    "BreakevenInf10Y_diff",
    "IG_Credit_zscore",
    "HY_Credit_diff",
    "HY_Credit_zscore",
    "VIX_zscore",
    # Regime-conditioned buy signal block
    "BuyProb_Regime",
    "BuyEdge_Regime",
    "BuyFlag_Regime",
]

PHASE12_AUDIT_ACTIVE_FEATURES_ACTUARIAL = [
    "Actuarial_Expected_Recovery",
    "Actuarial_Prob_30d",
    "Actuarial_Prob_60d",
    "Actuarial_Reserve_Severity",
]

PHASE12_AUDIT_ACTIVE_FEATURES = list(
    dict.fromkeys(
        PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL
        + PHASE12_AUDIT_ACTIVE_FEATURES_ACTUARIAL
    )
)

FEATURES_TO_DISABLE = []

FEATURE_SELECTION_CONFIG = {
    "disable_features": False,
    "disabled_features": FEATURES_TO_DISABLE,
    # Enforce the audit plan globally (Phase 1 and eval paths).
    "enforce_allowlist": True,
    "allowlist_apply_to_phase2": False,
    "active_features_allowlist": copy.deepcopy(PHASE12_AUDIT_ACTIVE_FEATURES),
    "feature_audit_plan_name": "exp6_feature_audit_20260221_v2",
    "feature_audit_expected_non_actuarial_count": len(PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL),
    "feature_audit_expected_total_count": len(PHASE12_AUDIT_ACTIVE_FEATURES),
}

ALPHA_FEATURES_CONFIG = {
    "enabled": True,
    "cross_sectional_column": "LogReturn_1d",
    "residual_momentum_window": 21,
    "volume_percentile_window": 63,
    "reversal_window": 5,
    "vol_of_vol_window": 63,
    "beta_window": 63,
    "obv_window": 21,
    "yield_curve": {
        "long_col": "DGS10_level",
        "short_col": None,
        # Prefer direct spread series when available.
        "spread_source_col": "T10Y2Y_level",
    },
    # Leakage-safe regime-conditioned buy signal features (optional).
    # Produces: BuyProb_Regime, BuyEdge_Regime, BuyFlag_Regime.
    "regime_buy_signal": {
        "enabled": True,
        "lookback_window": 252,
        "min_history": 40,
        "prior_alpha": 5.0,
        "prior_beta": 5.0,
        "buy_threshold": 0.55,
        "use_relative_to_market": True,
        "market_vol_short_window": 21,
        "market_vol_long_window": 126,
        "high_vol_ratio_threshold": 1.05,
    },
    "retain_market_return": False,
    "epsilon": 1e-9,
}

# Cross-Sectional Features Configuration (Asset Differentiation)
CROSS_SECTIONAL_FEATURES_CONFIG = {
    # Disabled by default to keep runtime features strictly on the audit set.
    "enabled": False,
    "momentum_windows": [21, 63, 252],  # Short/medium/long-term momentum rankings
    "zscore_features": [  # Features to standardize cross-sectionally
        "LogReturn_1d",
        "RollingVolatility_21d",
        "RSI_14"
    ],
    # Keep policy surface smooth; avoid extra binary channels by default.
    "include_beta_flags": False,
    "high_beta_threshold": 1.2,
    "low_beta_threshold": 0.8,
}

FRED_API_KEY = "da9d24dd8de4f924dcbc8416e539b4ef" # User's actual FRED API Key
FRED_SERIES_CONFIG = [
    # Keep only macro channels used by the active allowlist.
    {"code": "SOFR", "name": "SOFR", "freq": "d", "calc": ["diff"]},
    {"code": "DGS10", "name": "DGS10", "freq": "d", "calc": ["level", "diff"]},
    {"code": "T10Y2Y", "name": "T10Y2Y", "freq": "d", "calc": ["level"]},
    {"code": "DFII10", "name": "TIPS10Y", "freq": "d", "calc": ["level", "diff"]},
    {"code": "T10YIE", "name": "BreakevenInf10Y", "freq": "d", "calc": ["level", "diff"]},
    {"code": "BAMLC0A4CBBBEY", "name": "IG_Credit", "freq": "d", "calc": ["zscore"]},
    {"code": "BAMLH0A0HYM2", "name": "HY_Credit", "freq": "d", "calc": ["diff", "zscore"]},
    {"code": "VIXCLS", "name": "VIX", "freq": "d", "calc": ["zscore"]},
]

# Explicit global-context routing for structured observations in Phase 1/2.
PHASE12_GLOBAL_FEATURE_COLUMNS = [
    "YieldCurve_Spread",
    "YieldCurve_Inverted_Flag",
    "Regime_Breadth_Positive",
]

PHASE12_GLOBAL_FEATURE_PREFIXES = [
    "Covariance_Eigenvalue_",
    "YieldCurve_",
    "SOFR_",
    "DGS10_",
    "T10Y2Y_",
    "TIPS10Y_",
    "BreakevenInf10Y_",
    "IG_Credit_",
    "HY_Credit_",
    "VIX_",
]

MACRO_DATA_CONFIG = {
    "fred_api_key": FRED_API_KEY,
    "fred_series_config": FRED_SERIES_CONFIG,
    "business_days_only": True,
    "ffill_limit": None,
}

# --- PERFORMANCE CALCULATION PARAMETERS ---
PERFORMANCE_METRICS_CONFIG = {
    "rolling_window_episodes": 20,  # Episodes for rolling performance calculation
    "risk_free_rate": 0.02,  # Annual risk-free rate for Sharpe calculation
    "trading_days_per_year": 252,
    "metrics_to_track": [
        "total_return", "sharpe_ratio", "sortino_ratio", "max_drawdown", 
        "turnover", "skewness", "volatility", "win_rate"
    ]
}

# --- MARKET REGIME DETECTION PARAMETERS ---
MARKET_REGIME_CONFIG = {
    "volatility_regimes": {
        "low": {"vix_threshold": 15.0, "rolling_vol_threshold": 0.15},
        "medium": {"vix_threshold": 25.0, "rolling_vol_threshold": 0.25},
        "high": {"vix_threshold": 35.0, "rolling_vol_threshold": 0.35}
    },
    "trend_detection": {
        "bullish_threshold": 0.05,   # 5% above long-term MA
        "bearish_threshold": -0.05,  # 5% below long-term MA
        "sideways_threshold": 0.02   # Within 2% is sideways
    },
    "recession_indicators": {
        "yield_curve_inversion_threshold": -0.1,  # 10bp inversion
        "unemployment_change_threshold": 0.5      # 0.5% increase in unemployment
    }
}

# --- TAPE REWARD & UTILITY PROFILE DEFINITIONS ---
METRICS_ORDER = ['sharpe', 'sortino', 'mdd', 'turnover', 'skew']

PROFILE_BALANCED_GROWTH = {
    "name": "BalancedGrowth",
    # Asymmetric Sigmoid: mu is the 50% utility midpoint, k controls steepness
    "mu": np.array([1.0, 1.3, -0.15, 0.60, 0.0], dtype=np.float32),
    # k_minus: steepness BELOW target (penalty for increasing, reward for decreasing)
    "k_minus": np.array([4.0, 3.0, 3.0, 1.0, 2.0], dtype=np.float32),
    # k_plus:  steepness ABOVE target (reward for increasing, penalty for decreasing)
    "k_plus":  np.array([1.0, 1.0, 1.0, 4.0, 1.0], dtype=np.float32),
    "weights":   np.array([0.30, 0.25, 0.25, 0.15, 0.05], dtype=np.float32),
    "metrics_order": METRICS_ORDER,
    # MDD stored as negative: higher = less drawdown = better => 'increasing'
    "directions": ['increasing', 'increasing', 'increasing', 'decreasing', 'increasing'],
    "a_bounds": np.array([-2.0, -1.0, -0.30, 0.0, -1.0]),
    "b_bounds": np.array([3.0, 4.0, 0.0, 0.80, 1.0]),
}
PROFILE_AGGRESSIVE_ALPHA_SEEKER = {
    "name": "AggressiveAlphaSeeker",
    "mu": np.array([1.5, 2.5, -0.25, 1.0, 0.15], dtype=np.float32),
    "k_minus": np.array([5.0, 4.0, 3.0, 0.5, 3.0], dtype=np.float32),
    "k_plus":  np.array([0.5, 0.5, 0.5, 2.0, 0.5], dtype=np.float32),
    "weights":   np.array([0.40, 0.30, 0.10, 0.05, 0.15], dtype=np.float32),
    "metrics_order": METRICS_ORDER,
    "directions": ['increasing', 'increasing', 'increasing', 'decreasing', 'increasing'],
    "a_bounds": np.array([-1.0, 0.0, -0.50, 0.0, -1.0]),
    "b_bounds": np.array([4.0, 5.0, 0.0, 2.5, 1.5]),
}
PROFILE_CAPITAL_PRESERVATION = {
    "name": "CapitalPreservation",
    "mu": np.array([0.5, 1.0, -0.08, 0.02, -0.05], dtype=np.float32),
    "k_minus": np.array([3.0, 2.5, 8.0, 0.5, 2.0], dtype=np.float32),
    "k_plus":  np.array([2.0, 2.0, 2.0, 3.0, 1.5], dtype=np.float32),
    "weights":   np.array([0.05, 0.05, 0.60, 0.20, 0.10], dtype=np.float32),
    "metrics_order": METRICS_ORDER,
    "directions": ['increasing', 'increasing', 'increasing', 'decreasing', 'increasing'],
    "a_bounds": np.array([-1.0, -0.5, -0.20, 0.0, -1.0]),
    "b_bounds": np.array([2.0, 3.0, 0.0, 1.0, 1.0]),
}
ALL_PROFILES_LIST = [PROFILE_BALANCED_GROWTH, PROFILE_AGGRESSIVE_ALPHA_SEEKER, PROFILE_CAPITAL_PRESERVATION]

# --- PHASE CONFIGURATIONS ---

# Phase 1: Baseline Enhanced Vanilla PPO
PHASE1_CONFIG = {
    "phase_name": "Phase1_Baseline_PPO",
    #================================================
    "ASSET_TICKERS": ASSET_TICKERS,
    "NUM_ASSETS": NUM_ASSETS,
    "BASE_DATA_PATH": BASE_DATA_PATH,
    "PATH_DAILY_OHLCV": PATH_DAILY_OHLCV,
    "DATA_FETCH_START_DATE": DATA_FETCH_START_DATE,
    "DATA_FETCH_END_DATE": DATA_FETCH_END_DATE,
    "ANALYSIS_START_DATE": ANALYSIS_START_DATE,
    "ANALYSIS_END_DATE": ANALYSIS_END_DATE,
    "feature_params": {
        "technical_indicators": TECHNICAL_INDICATORS_CONFIG,
        "candlestick_features": copy.deepcopy(CANDLESTICK_FEATURES_CONFIG),
        "include_log_returns": True,
        "log_return_col_name": "Daily_LogReturn",
        # Dynamic covariance enabled for portfolio correlation insights
        "dynamic_covariance": DYNAMIC_COVARIANCE_PARAMS,
        "actuarial_params": ACTUARIAL_PARAMS,
        # Advanced features still disabled for Phase 1
        "temporal_forecast": None,
        "macro_data": copy.deepcopy(MACRO_DATA_CONFIG),
        "fundamental_features": copy.deepcopy(FUNDAMENTAL_FEATURES_CONFIG),
        "regime_features": {
            "enabled": True,
            "vol_windows": {"short": 21, "long": 126},
            "trend_windows": {"short": 50, "long": 200},
            "momentum_windows": {"short": 63, "long": 252},
            "correlation_window": 60,
            "breadth_window": 21,
        },
        "feature_selection": copy.deepcopy(FEATURE_SELECTION_CONFIG),
        "alpha_features": copy.deepcopy(ALPHA_FEATURES_CONFIG),
        "cross_sectional_features": copy.deepcopy(CROSS_SECTIONAL_FEATURES_CONFIG),
    },
    #================================================
    "environment_params": {
        "initial_balance": 100000.0,
        "transaction_cost_pct": 0.001,
        "structured_observation": True,
        "global_feature_columns": copy.deepcopy(PHASE12_GLOBAL_FEATURE_COLUMNS),
        "global_feature_prefixes": copy.deepcopy(PHASE12_GLOBAL_FEATURE_PREFIXES),
        "reward_type": "advanced_tape",  # Three-component TAPE reward
        "max_steps_per_episode": None,  # Episode horizon managed dynamically during training
        "done_on_balance_threshold_pct": 0.5,  # PHASE 1: Increased from 0.2 to 0.5 for exploration
        "random_start": True,
        "initial_allocation_mode": "equal_assets_with_min_cash",
        "initial_cash_position": 0.05,
        "tape_terminal_scalar": 10.0,
        "tape_terminal_clip": 10.0,
        "tape_terminal_bonus_mode": "signed",
        "tape_terminal_baseline": 0.20,
        "tape_terminal_neutral_band_enabled": True,
        "tape_terminal_neutral_band_halfwidth": 0.02,
        "tape_terminal_gate_a_enabled": True,
        "tape_terminal_gate_a_sharpe_threshold": 0.0,
        "tape_terminal_gate_a_max_drawdown": 0.25,
        "target_turnover": 0.60,  # Relax early ceiling; tighten via curriculum as policy stabilizes
        "turnover_penalty_scalar": 2.0,
        "turnover_target_band": 0.20,
        "dsr_scalar": 2.0,  # Further reduce PBRS noise while policy is unstable
        "concentration_penalty_scalar": 2.0,
        "concentration_target_hhi": 0.14,
        "top_weight_penalty_scalar": 1.5,
        "target_top_weight": 0.22,
        "action_realization_penalty_scalar": 0.5,
        "penalty_budget_ratio": 1.25,
        "intra_step_tape_delta_enabled": True,
        "intra_step_tape_delta_window": 60,
        "intra_step_tape_delta_min_history": 20,
        "intra_step_tape_delta_beta": 0.01,
        "intra_step_tape_delta_clip": 0.20,
        "dd_regime_scaling": {
            "enabled": True,
            "vol_window": 21,
            "low_vol_threshold": 0.12,
            "high_vol_threshold": 0.25,
            "low_mult": 0.90,
            "mid_mult": 1.00,
            "high_mult": 1.35,
        },
        "drawdown_constraint": {
            "enabled": True,
            "target": 0.18,
            "penalty_coef": 1.5,
            "dual_learning_rate": 0.10,
            "lambda_init": 0.50,
            "lambda_floor": 0.0,
            "lambda_max": 5.0,
            "tolerance": -0.015,
            # Apply penalty as soon as drawdown crosses trigger boundary (target + tolerance).
            "penalty_reference": "trigger_boundary",
            # Avoid cooling lambda too aggressively below trigger.
            "cooling_rate": 0.35,
            "lambda_carry_decay": 0.7,
        }
    },
    #================================================
    "agent_params": {
        # Architecture Selection: 'TCN', 'TCN_ATTENTION', 'TCN_FUSION'
        "actor_critic_type": "TCN_FUSION",
        "use_attention": False,
        "use_fusion": True,
        
        # Network dimensions for TCN architectures
        "actor_hidden_dims": [256, 128],
        "critic_hidden_dims": [256, 128],
        
        # Sequence parameters for sequential models (TCN, TCN, etc.)
        "sequence_length": 60,  # Requested architecture update
        
        # STATE-OF-THE-ART FIX #3: Right-sized TCN dimensions (2x faster, minimal quality loss)
        # TCN-specific parameters for faster training
        
        # TCN-specific parameters
        #"tcn_filters": [64, 128, 256],
        #"tcn_kernel_size": 3,
        #"tcn_dilations": [1, 2, 4, 8, 16],
        #"tcn_dropout": 0.2,

        # IMPROVED TCN ARCHITECTURE (deeper with better receptive field)
        "tcn_filters": [64, 128, 128],  # Upgraded TCN capacity for richer temporal representation
        "tcn_kernel_size": 5,                # Requested architecture update
        "tcn_dilations": [2, 4, 8],       # Requested architecture update
        "tcn_dropout": 0.2,
        
        # Attention-specific parameters
        "attention_heads": 4,
        "attention_dim": 64,
        "attention_dropout": 0.1,

        # Fusion-specific parameters (for TCN_FUSION or TCN with use_fusion=True)
        "fusion_embed_dim": 128,
        "fusion_attention_heads": 4,
        "fusion_dropout": 0.1,
        "fusion_cross_asset_mixer_enabled": True,    # v2: enable multi-layer cross-asset self-attention
        "fusion_cross_asset_mixer_layers": 1,        # PERF-FIX #8: reduced from 2 to 1 — simpler until base is stable
        "fusion_cross_asset_mixer_expansion": 2.0,
        "fusion_cross_asset_mixer_dropout": 0.1,
        "fusion_alpha_head_hidden_dims": [],         # A3 toggle (empty = legacy direct logits head)
        "fusion_alpha_head_dropout": 0.1,
        # Cross-asset attention v2 upgrades
        "fusion_asset_identity_enabled": True,               # Learnable per-asset embeddings
        "fusion_context_cross_attention_enabled": False,     # PERF-FIX #8: disabled — undertrained with 150K steps
        "fusion_context_cross_attention_heads": 4,
        "fusion_context_cross_attention_dropout": 0.1,
        "fusion_per_asset_alpha_head": True,                 # Per-asset alpha output (no AvgPool bottleneck)
        # Optional recurrent memory.
        "recurrent_memory_enabled": False,          # PERF-FIX #8: disabled — TCN already captures temporal
        "recurrent_memory_units": 64,
        "recurrent_memory_dropout": 0.1,
        # Optional regime-aware conditioning.
        "regime_conditioning_enabled": False,        # PERF-FIX #8: disabled — regime info already in features
        "regime_conditioning_hidden_dim": 32,
        "regime_conditioning_dropout": 0.0,
        # Optional state augmentation for regime summary features.
        "state_augmentation_enabled": True,
        # Optional distributional critic head.
        "distributional_critic_enabled": False,      # PERF-FIX #8: disabled — simpler critic learns faster
        "distributional_num_quantiles": 17,
        # Dual-head policy (Dirichlet + softmax/projection).
        "dual_head_enabled": False,
        "dual_head_blend_schedule": [
            {"threshold": 0, "rho": 0.35},
            {"threshold": 30_000, "rho": 0.55},
            {"threshold": 60_000, "rho": 0.70},
        ],
        "dual_head_eval_deterministic_rho": 0.90,
        "dual_head_eval_stochastic_rho": 0.60,
        "dual_head_projection_use_constraints": False,
        "dual_head_projection_max_single_position": 0.95,
        "dual_head_projection_min_cash_position": 0.05,

        # Dirichlet alpha activation (controls action concentration)
        "dirichlet_alpha_activation": "exp_tanh",   # PERF-FIX #4c: exp(tanh(x)*scale) — better diversity than softplus
        "dirichlet_exp_clip": (-5.0, 3.0),
        "dirichlet_logit_temperature": 0.5,           # PERF-FIX #4a: sharper allocation (was 1.0)
        # Optional adaptive temperature controller:
        # temperature = clip(base + slope * |logit|, t_min, t_max)
        # Larger |logit| -> larger temperature -> flatter alpha map.
        "dirichlet_adaptive_temperature_enabled": False,
        "dirichlet_adaptive_temperature_base": 1.0,
        "dirichlet_adaptive_temperature_slope": 0.0,
        "dirichlet_adaptive_temperature_min": 0.8,
        "dirichlet_adaptive_temperature_max": 2.5,
        "dirichlet_alpha_cap": 50.0,                 # PERF-FIX #4a: tighter cap (was 100.0)

        # Dirichlet exploration (epsilon annealing)
        "dirichlet_epsilon": {
            "max": 0.5,  # Early training: encourage exploration
            "min": 0.1,  # Late training / evaluation: sharper allocations
        },

        # Deterministic evaluation mode
        # Options: 'mean', 'mode', 'mean_plus_noise'
        "evaluation_mode": "mode",  # [OK] RECOMMENDED: Shows true learned policy
        
        # PPO Algorithm parameters
        # Stabilized PPO regime for better out-of-sample Sharpe retention.
        "ppo_params": {
            # PERF-FIX #1: PPO stability overhaul
            "gamma": 0.99, "gae_lambda": 0.92, "policy_clip": 0.15,
            "entropy_coef": 0.005, "vf_coef": 0.5, "num_ppo_epochs": 3,
            "batch_size_ppo": 252, "actor_lr": 0.00003, "critic_lr": 0.00015,
            "max_grad_norm": 0.5, "value_clip": 0.3, "target_kl": 0.0,  # disabled: exp_tanh has naturally larger KL
            "kl_stop_multiplier": 2.0, "minibatches_before_kl_stop": 2,
            # PERF-FIX #4b: Alpha diversity HHI auxiliary loss coefficient
            "alpha_diversity_coef": 0.01,
            # Optional risk-aware actor auxiliaries.
            "use_risk_aux_loss": True,
            # Per-asset feature index used as one-step return proxy in structured state tensor.
            "risk_aux_return_feature_index": 0,
            "risk_aux_cash_return": 0.0,
            "risk_aux_sharpe_coef": 0.0,
            "risk_aux_mvo_coef": 0.0,
            "risk_aux_cvar_coef": 0.01,
            "risk_aux_cvar_alpha": 0.05,
            "risk_aux_cvar_adaptive_enabled": True,
            "risk_aux_cvar_target": 0.015,
            "risk_aux_cvar_adapt_lr": 0.05,
            "risk_aux_cvar_min_coef": 0.0,
            "risk_aux_cvar_max_coef": 0.08,
            "risk_aux_mvo_cov_ridge": 1e-3,
            "risk_aux_mvo_long_only": True,
            "risk_aux_mvo_risky_budget": 0.95,
            "distributional_huber_kappa": 1.0,
            "distributional_mean_loss_coef": 0.1,
            "dual_head_consistency_coef": 0.0,
            "popart_enabled": True,
            "popart_min_std": 1e-3,
            "multi_horizon_reward_enabled": True,
            "multi_horizon_reward_coef": 0.20,
            "multi_horizon_reward_horizons": [21, 63, 126, 252],
            "multi_horizon_reward_weights": [0.15, 0.25, 0.30, 0.30],
        },
    },
    #================================================
    "training_params": {
        "max_total_timesteps": 500_000,  # PERF-FIX #5: extended from 150K for complex architecture
        "num_parallel_envs": 1,  # >1 enables vectorized rollout collection
        "timesteps_per_ppo_update": 504,  # Frequent updates (matched to episode length) — archive used ~252
        "log_interval_episodes": 10,
        "update_log_interval": 20,
        "alpha_diversity_log_interval": 10,
        "alpha_diversity_warning_after_updates": 500,
        "alpha_diversity_warning_std_threshold": 0.30,
        "save_freq_episodes": 50,
        "max_episode_length": None,  # Episode length controlled by curriculum
        
        # STATE-OF-THE-ART FIX #2: Stronger Entropy Incentive
        "entropy_coefficient": 0.10,  # Diversification bonus weight (10x stronger for meaningful impact)
        
        # STATE-OF-THE-ART FIX #3: Position Size Constraints
        "max_single_position": 95.00,  # Effectively uncapped — soft constraints handle concentration
        
        # Alternative: Curriculum schedule for max single position
        # Start strict, relax as agent learns 
        #"max_single_position_curriculum": {
        #    0: 20.0,        # First 30k steps: Learn diversification
        #    30_000: 30.0,   # 30k-60k: Allow more concentration
        #    60_000: 35.0,   # 60k-100k: Further relaxation
        #    100_000: 40.0,  # Final: Full flexibility
        #},
        "min_cash_position": 0.05,    # Minimum cash buffer (5%)
        
        # STATE-OF-THE-ART FIX #4: Curriculum Learning
        "use_curriculum_learning": True,
        "curriculum_phases": [
            {"name": "all", "timesteps_fraction": 0.30},    # Regime-balanced from start
            {"name": "all", "timesteps_fraction": 0.40},    # Regime-balanced throughout
            {"name": "all", "timesteps_fraction": 0.30}     # Regime-balanced to end
        ],

        # PERF-FIX #2 + #5: Smooth schedule transitions with wider spacing for 500K budget.
        "use_episode_length_curriculum": True,
        "episode_length_curriculum_schedule": [
            {"threshold": 0,        "limit": 756},
            {"threshold": 100_000,  "limit": 1008},
            {"threshold": 250_000,  "limit": 1500},
            {"threshold": 400_000,  "limit": None},
        ],
        "episode_length_curriculum_smooth_enabled": True,
        "episode_length_curriculum_overlap_steps": 20_000,
        "ppo_gamma_schedule": [
            {"threshold": 0,        "gamma": 0.990},
            {"threshold": 150_000,  "gamma": 0.995},
            {"threshold": 350_000,  "gamma": 0.998},
        ],
        "ppo_gae_lambda_schedule": [
            {"threshold": 0,        "gae_lambda": 0.92},
            {"threshold": 150_000,  "gae_lambda": 0.95},
            {"threshold": 350_000,  "gae_lambda": 0.97},
        ],
        # PERF-FIX #2: Actor LR schedule (gentle decay)
        "actor_lr_schedule": [
            {"threshold": 0,        "lr": 0.00003},
            {"threshold": 150_000,  "lr": 0.00002},
            {"threshold": 300_000,  "lr": 0.00001},
        ],
        # PERF-FIX #6: Execution inertia — start high beta, reduce slowly
        "action_execution_beta_schedule": [
            {"threshold": 0,        "beta": 0.50},
            {"threshold": 100_000,  "beta": 0.40},
            {"threshold": 200_000,  "beta": 0.30},
            {"threshold": 350_000,  "beta": 0.25},
        ],
        # PERF-FIX #2: Turnover penalty curriculum (scaled for 500K)
        "turnover_penalty_curriculum": {
            0:        0.75,
            100_000:  1.25,
            200_000:  1.50,
            300_000:  1.75,
            400_000:  2.00,
        },
        
        # PHASE 1: Progressive Threshold Curriculum
        "use_progressive_threshold": True,
        # Progressive threshold schedule for Phase 1 (20K episodes, gentler curve)
        "progressive_threshold_schedule": {
            0: 0.90,       # Episodes 1-1000: Very forgiving start
            1000: 0.85,    # Episodes 1001-2000: Gradual decrease
            2000: 0.80,    # Episodes 2001-3000
            3000: 0.75,    # Episodes 3001-4000
            4000: 0.70,    # Episodes 4001-5000
            5000: 0.65,    # Episodes 5001-6000
            6000: 0.60,    # Episodes 6001-7000
            7000: 0.55,    # Episodes 7001-8000
            8000: 0.50     # Episodes 8001-20000: Target threshold
        },

        # Checkpointing default: periodic deterministic validation is the primary selector.
        "deterministic_validation_checkpointing_enabled": True,
        "deterministic_validation_eval_every_episodes": 5,
        "deterministic_validation_mode": "mean",
        "deterministic_validation_episode_length_limit": None,  # None = full validation horizon
        "deterministic_validation_sharpe_min": 0.5,
        "deterministic_validation_sharpe_min_delta": 0.0,
        "deterministic_validation_seed_offset": 10_000,
        "deterministic_validation_multi_horizon_enabled": True,
        "deterministic_validation_multi_horizon_limits": [252, 504, 756, 1008],
        "deterministic_validation_multi_horizon_weights": [0.35, 0.30, 0.20, 0.15],
        "deterministic_validation_multi_horizon_dd_penalty_coef": 0.25,
        "deterministic_validation_stochastic_sanity_enabled": True,
        "deterministic_validation_stochastic_sanity_runs": 3,
        "deterministic_validation_stochastic_sanity_episode_length_limit": 252,
        "deterministic_validation_stochastic_sanity_min_mean_sharpe": 0.0,
        "deterministic_validation_stochastic_sanity_max_sharpe_std": 1.5,
        # If True, legacy checkpoint routes remain disabled even if toggled elsewhere.
        "deterministic_validation_checkpointing_only": True,

        # Legacy checkpoint routes (disabled by default).
        "rare_checkpoint_params": {
            "enable": False,
            "min_sharpe": 1.5,
            "min_sortino": 2.0,
            "max_mdd": 0.15,          # 15% drawdown
            "max_turnover": 0.80,     # 80% daily turnover
            "top_n": 5
        },
        "tape_checkpoint_threshold": 999.0,
        "periodic_checkpoint_every_steps": 0,
        "high_watermark_checkpoint_enabled": False,
        "high_watermark_sharpe_threshold": 0.5,
        "step_sharpe_checkpoint_enabled": False,
        "step_sharpe_checkpoint_threshold": 0.5,

        # Actor LR schedule (canonical across project).
        # Starts conservative, then decays further for stability.
        "actor_lr_schedule": [
            {"threshold": 0, "lr": 0.00002},
            {"threshold": 40_000, "lr": 0.000015},
            {"threshold": 70_000, "lr": 0.00001},
        ],

        # Regime-Adaptive KL controller (disabled by default).
        # If enabled, target_kl is adjusted online from observed approx_kl.
        "ra_kl_enabled": False,
        "ra_kl_target_ratio": 1.0,
        "ra_kl_ema_alpha": 0.25,
        "ra_kl_gain": 0.06,
        "ra_kl_deadband": 0.10,
        "ra_kl_max_change_fraction": 0.10,
        # Bounds are absolute values for target_kl when RA-KL is enabled.
        "ra_kl_min_target_kl": 0.008,
        "ra_kl_max_target_kl": 0.040,

        # Turnover curriculum matching 2.0 => 1.75 => 1.50 => 1.25 request
        "turnover_penalty_curriculum": {
            0: 0.75,
            30_000: 1.25,
            60_000: 1.50,
            90_000: 1.75,
            120_000: 2.00,
        },
    },
}

# Phase 2: Advanced Single-Horizon Model (3-Day Prototype)
PHASE2_CONFIG = {
    "phase_name": "Phase2_Advanced_Prototype",
    #================================================
    "ASSET_TICKERS": ASSET_TICKERS,
    "NUM_ASSETS": NUM_ASSETS,
    "BASE_DATA_PATH": BASE_DATA_PATH,
    "PATH_DAILY_OHLCV": PATH_DAILY_OHLCV,
    "DATA_FETCH_START_DATE": DATA_FETCH_START_DATE,
    "DATA_FETCH_END_DATE": DATA_FETCH_END_DATE,
    "ANALYSIS_START_DATE": ANALYSIS_START_DATE,
    "ANALYSIS_END_DATE": ANALYSIS_END_DATE,
    "feature_params": {
        "technical_indicators": TECHNICAL_INDICATORS_CONFIG,
        "candlestick_features": copy.deepcopy(CANDLESTICK_FEATURES_CONFIG),
        "include_log_returns": True,
        "log_return_col_name": "Daily_LogReturn",
        "temporal_forecast": None,  # Disabled for testing - TCN rolling forecast is too slow (4000+ models to train)
        "dynamic_covariance": DYNAMIC_COVARIANCE_PARAMS,
        "macro_data": copy.deepcopy(MACRO_DATA_CONFIG),
        "fundamental_features": copy.deepcopy(FUNDAMENTAL_FEATURES_CONFIG),
        "regime_features": {
            "enabled": True,
            "vol_windows": {"short": 21, "long": 126},
            "trend_windows": {"short": 50, "long": 200},
            "momentum_windows": {"short": 63, "long": 252},
            "correlation_window": 60,
            "breadth_window": 21,
        },
        "feature_selection": copy.deepcopy(FEATURE_SELECTION_CONFIG),
        "alpha_features": copy.deepcopy(ALPHA_FEATURES_CONFIG),
        "cross_sectional_features": copy.deepcopy(CROSS_SECTIONAL_FEATURES_CONFIG),
    },
    #================================================
    "environment_params": {
        "initial_balance": 100000.0, "transaction_cost_pct": 0.001,
        "structured_observation": True,
        "global_feature_columns": copy.deepcopy(PHASE12_GLOBAL_FEATURE_COLUMNS),
        "global_feature_prefixes": copy.deepcopy(PHASE12_GLOBAL_FEATURE_PREFIXES),
        "reward_type": "advanced_tape", # Use TAPE reward system
        "truncated_gaussian_lambda": 0.2,
        "max_steps_per_episode": 252,
        "done_on_balance_threshold_pct": 0.5,
        "initial_allocation_mode": "equal_assets_with_min_cash",
        "initial_cash_position": 0.05,
        "target_turnover": 0.60,  # Relax early ceiling; tighten via curriculum as policy stabilizes
        "tape_terminal_bonus_mode": "signed",
        "tape_terminal_baseline": 0.20,
        "tape_terminal_neutral_band_enabled": True,
        "tape_terminal_neutral_band_halfwidth": 0.02,
        "tape_terminal_gate_a_enabled": True,
        "tape_terminal_gate_a_sharpe_threshold": 0.0,
        "tape_terminal_gate_a_max_drawdown": 0.25,
        "turnover_penalty_scalar": 2.0,
        "turnover_target_band": 0.20,
        "dsr_scalar": 2.0,  # Further reduce PBRS noise while policy is unstable
        "concentration_penalty_scalar": 2.0,
        "concentration_target_hhi": 0.14,
        "top_weight_penalty_scalar": 1.5,
        "target_top_weight": 0.22,
        "action_realization_penalty_scalar": 0.5,
        "penalty_budget_ratio": 1.25,
        "intra_step_tape_delta_enabled": True,
        "intra_step_tape_delta_window": 60,
        "intra_step_tape_delta_min_history": 20,
        "intra_step_tape_delta_beta": 0.01,
        "intra_step_tape_delta_clip": 0.20,
        "dd_regime_scaling": {
            "enabled": True,
            "vol_window": 21,
            "low_vol_threshold": 0.12,
            "high_vol_threshold": 0.25,
            "low_mult": 0.90,
            "mid_mult": 1.00,
            "high_mult": 1.35,
        },
        "drawdown_constraint": {
            "enabled": True,
            "target": 0.18,
            "penalty_coef": 1.5,
            "dual_learning_rate": 0.10,
            "lambda_init": 0.50,
            "lambda_floor": 0.0,
            "lambda_max": 5.0,
            "tolerance": -0.015,
            "penalty_reference": "trigger_boundary",
            "cooling_rate": 0.35,
            "lambda_carry_decay": 0.7,
        },
        "drawdown_constraint_overrides": {
            "sequential": {
                "penalty_coef": 1.5,
                "dual_learning_rate": 0.10,
                "lambda_floor": 0.0,
                "lambda_max": 5.0,
                "tolerance": -0.015,
                "penalty_reference": "trigger_boundary",
                "cooling_rate": 0.35,
                "lambda_carry_decay": 0.7,
            }
        }
    },
    #================================================
    "agent_params": {
        # Architecture Selection: 'TCN', 'TCN_ATTENTION', 'TCN_FUSION'
        "actor_critic_type": "TCN_FUSION",
        "use_attention": False,
        "use_fusion": True,
        
        # Network dimensions for TCN architectures
        "actor_hidden_dims": [256, 128], # Larger TCN for more features
        "critic_hidden_dims": [256, 128],
        
        # Sequence parameters for sequential models (TCN, TCN, etc.)
        "sequence_length": 60,  # Requested architecture update
        
        # STATE-OF-THE-ART FIX #3: Right-sized TCN dimensions (2x faster, minimal quality loss)
        # TCN-specific parameters for faster training
        
        # TCN-specific parameters
        #"tcn_filters": [64, 128, 256],  # Modest pyramid for deeper receptive field
        #"tcn_kernel_size": 3,
        #"tcn_dilations": [1, 2, 4, 8, 16],  # Extended dilations to cover ~60–90 days
        #"tcn_dropout": 0.2,

        # IMPROVED TCN ARCHITECTURE (deeper with better receptive field)
        "tcn_filters": [64, 128, 128],  # Upgraded TCN capacity for richer temporal representation
        "tcn_kernel_size": 5,                # Requested architecture update
        "tcn_dilations": [2, 4, 8],       # Requested architecture update
        "tcn_dropout": 0.2,
        
        # Attention-specific parameters
        "attention_heads": 4,
        "attention_dim": 64,
        "attention_dropout": 0.1,

        # Fusion-specific parameters (for TCN_FUSION or TCN with use_fusion=True)
        "fusion_embed_dim": 128,
        "fusion_attention_heads": 4,
        "fusion_dropout": 0.1,
        "fusion_cross_asset_mixer_enabled": False,   # A4 toggle (kept off by default for checkpoint compatibility)
        "fusion_cross_asset_mixer_layers": 1,
        "fusion_cross_asset_mixer_expansion": 2.0,
        "fusion_cross_asset_mixer_dropout": 0.1,
        "fusion_alpha_head_hidden_dims": [],         # A3 toggle (empty = legacy direct logits head)
        "fusion_alpha_head_dropout": 0.1,
        # Optional recurrent memory.
        "recurrent_memory_enabled": True,
        "recurrent_memory_units": 64,
        "recurrent_memory_dropout": 0.1,
        # Optional regime-aware conditioning.
        "regime_conditioning_enabled": True,
        "regime_conditioning_hidden_dim": 32,
        "regime_conditioning_dropout": 0.0,
        # Optional state augmentation for regime summary features.
        "state_augmentation_enabled": True,
        # Optional distributional critic head.
        "distributional_critic_enabled": True,
        "distributional_num_quantiles": 17,
        # Dual-head policy (Dirichlet + softmax/projection).
        "dual_head_enabled": False,
        "dual_head_blend_schedule": [
            {"threshold": 0, "rho": 0.35},
            {"threshold": 30_000, "rho": 0.55},
            {"threshold": 60_000, "rho": 0.70},
        ],
        "dual_head_eval_deterministic_rho": 0.90,
        "dual_head_eval_stochastic_rho": 0.60,
        "dual_head_projection_use_constraints": False,
        "dual_head_projection_max_single_position": 0.95,
        "dual_head_projection_min_cash_position": 0.05,

        # Dirichlet alpha activation (controls action concentration)
        "dirichlet_alpha_activation": "softplus",  # Stable strictly-positive alpha map
        "dirichlet_exp_clip": (-5.0, 3.0),
        "dirichlet_logit_temperature": 1.0,
        # Optional adaptive temperature controller:
        # temperature = clip(base + slope * |logit|, t_min, t_max)
        # Larger |logit| -> larger temperature -> flatter alpha map.
        "dirichlet_adaptive_temperature_enabled": False,
        "dirichlet_adaptive_temperature_base": 1.0,
        "dirichlet_adaptive_temperature_slope": 0.0,
        "dirichlet_adaptive_temperature_min": 0.8,
        "dirichlet_adaptive_temperature_max": 2.5,
        "dirichlet_alpha_cap": 100.0,

        # Dirichlet exploration (epsilon annealing)
        "dirichlet_epsilon": {
            "max": 0.5,
            "min": 0.1,
        },
        
        # Deterministic evaluation mode
        # Options: 'mean', 'mode', 'mean_plus_noise'
        "evaluation_mode": "mode",  # [OK] RECOMMENDED: Shows true learned policy
        
        # PPO Algorithm parameters
        "ppo_params": {
            "gamma": 0.99, "gae_lambda": 0.9, "policy_clip": 0.10,
            "entropy_coef": 0.01, "vf_coef": 0.5, "num_ppo_epochs": 4,
            "batch_size_ppo": 256, "actor_lr": 0.00002, "critic_lr": 0.0003,
            "max_grad_norm": 0.5, "value_clip": 0.2, "target_kl": 0.015,
            "kl_stop_multiplier": 1.2, "minibatches_before_kl_stop": 1,
            # Optional risk-aware actor auxiliaries.
            "use_risk_aux_loss": True,
            "risk_aux_return_feature_index": 0,
            "risk_aux_cash_return": 0.0,
            "risk_aux_sharpe_coef": 0.0,
            "risk_aux_mvo_coef": 0.0,
            "risk_aux_cvar_coef": 0.01,
            "risk_aux_cvar_alpha": 0.05,
            "risk_aux_cvar_adaptive_enabled": True,
            "risk_aux_cvar_target": 0.015,
            "risk_aux_cvar_adapt_lr": 0.05,
            "risk_aux_cvar_min_coef": 0.0,
            "risk_aux_cvar_max_coef": 0.08,
            "risk_aux_mvo_cov_ridge": 1e-3,
            "risk_aux_mvo_long_only": True,
            "risk_aux_mvo_risky_budget": 0.95,
            "distributional_huber_kappa": 1.0,
            "distributional_mean_loss_coef": 0.1,
            "dual_head_consistency_coef": 0.0,
            "popart_enabled": True,
            "popart_min_std": 1e-3,
            "multi_horizon_reward_enabled": True,
            "multi_horizon_reward_coef": 0.20,
            "multi_horizon_reward_horizons": [21, 63, 126, 252],
            "multi_horizon_reward_weights": [0.15, 0.25, 0.30, 0.30],
        },
    },
    #================================================
    "training_params": {
        "max_total_timesteps": 100000,
        "num_parallel_envs": 1,  # >1 enables vectorized rollout collection
        "timesteps_per_ppo_update": 250,
        "log_interval_episodes": 10,
        "save_freq_episodes": 50,
        "max_episode_length": None,  # Use full dataset horizon

        # STATE-OF-THE-ART FIX #2: Stronger Entropy Incentive
        "entropy_coefficient": 0.10,  # Diversification bonus weight (10x stronger for meaningful impact)
        
        # STATE-OF-THE-ART FIX #3: Position Size Constraints
        "max_single_position": 95.00,  # Effectively uncapped — soft constraints handle concentration
        "min_cash_position": 0.05,    # Minimum cash buffer (5%)

        # STATE-OF-THE-ART FIX #4: Curriculum Learning
        "use_curriculum_learning": True,
        "curriculum_phases": [
            {"name": "all", "timesteps_fraction": 0.30},    # Regime-balanced from start
            {"name": "all", "timesteps_fraction": 0.40},    # Regime-balanced throughout
            {"name": "all", "timesteps_fraction": 0.30}     # Regime-balanced to end
        ],

        # Enable episode-length curriculum with smooth overlap ramps.
        "use_episode_length_curriculum": True,
        "episode_length_curriculum_schedule": [
            {"threshold": 0, "limit": 504},
            {"threshold": 15_000, "limit": 756},
            {"threshold": 30_000, "limit": 1_200},
            {"threshold": 45_000, "limit": 1_500},
            {"threshold": 60_000, "limit": 2_500},
            {"threshold": 75_000, "limit": None},
        ],
        "episode_length_curriculum_smooth_enabled": True,
        "episode_length_curriculum_overlap_steps": 7_500,
        "ppo_gamma_schedule": [
            {"threshold": 0, "gamma": 0.985},
            {"threshold": 40_000, "gamma": 0.992},
            {"threshold": 80_000, "gamma": 0.997},
        ],
        "ppo_gae_lambda_schedule": [
            {"threshold": 0, "gae_lambda": 0.90},
            {"threshold": 40_000, "gae_lambda": 0.94},
            {"threshold": 80_000, "gae_lambda": 0.97},
        ],

        # Turnover penalty schedule to match Phase 1 discipline
        "turnover_penalty_curriculum": {
            0: 0.75,
            30_000: 1.25,
            60_000: 1.50,
            90_000: 1.75,
            120_000: 2.00,
        },

        # Actor LR decay schedule (critic stays constant)
        "actor_lr_schedule": [
            {"threshold": 0, "lr": 0.00002},
            {"threshold": 40_000, "lr": 0.000015},
            {"threshold": 70_000, "lr": 0.00001},
        ],

        # Regime-Adaptive KL controller (disabled by default).
        "ra_kl_enabled": False,
        "ra_kl_target_ratio": 1.0,
        "ra_kl_ema_alpha": 0.25,
        "ra_kl_gain": 0.06,
        "ra_kl_deadband": 0.10,
        "ra_kl_max_change_fraction": 0.10,
        "ra_kl_min_target_kl": 0.008,
        "ra_kl_max_target_kl": 0.040,

        # Progressive reward thresholding identical to Phase 1
        "use_progressive_threshold": True,
        "progressive_threshold_schedule": {
            0: 0.90,
            1000: 0.85,
            2000: 0.80,
            3000: 0.75,
            4000: 0.70,
            5000: 0.65,
            6000: 0.60,
            7000: 0.55,
            8000: 0.50,
        },

        # Console logging cadence
        "episode_log_interval": 10,

        # Checkpointing default: periodic deterministic validation is the primary selector.
        "deterministic_validation_checkpointing_enabled": True,
        "deterministic_validation_eval_every_episodes": 5,
        "deterministic_validation_mode": "mean",
        "deterministic_validation_episode_length_limit": None,
        "deterministic_validation_sharpe_min": 0.5,
        "deterministic_validation_sharpe_min_delta": 0.0,
        "deterministic_validation_seed_offset": 10_000,
        "deterministic_validation_multi_horizon_enabled": False,
        "deterministic_validation_multi_horizon_limits": [252, 504, 756, 1008],
        "deterministic_validation_multi_horizon_weights": [0.35, 0.30, 0.20, 0.15],
        "deterministic_validation_multi_horizon_dd_penalty_coef": 0.25,
        "deterministic_validation_stochastic_sanity_enabled": False,
        "deterministic_validation_stochastic_sanity_runs": 3,
        "deterministic_validation_stochastic_sanity_episode_length_limit": 252,
        "deterministic_validation_stochastic_sanity_min_mean_sharpe": 0.0,
        "deterministic_validation_stochastic_sanity_max_sharpe_std": 1.5,
        "deterministic_validation_checkpointing_only": True,

        # Legacy checkpoint routes (disabled by default).
        "rare_checkpoint_params": {
            "enable": False,
            "min_sharpe": 1.5,
            "min_sortino": 2.0,
            "max_mdd": 0.15,          # 15% drawdown
            "max_turnover": 0.80,     # 80% daily turnover
            "top_n": 5
        },
        "tape_checkpoint_threshold": 999.0,
        "periodic_checkpoint_every_steps": 0,
        "high_watermark_checkpoint_enabled": False,
        "high_watermark_sharpe_threshold": 0.5,
        "step_sharpe_checkpoint_enabled": False,
        "step_sharpe_checkpoint_threshold": 0.5,
        
        "results_path": os.path.join(BASE_PROJECT_PATH, 'results', "phase2_advanced_prototype")
    }
}

# =============================================================================
# RUN 5 OVERRIDES — toggleable fixes from Run 4 analysis
# =============================================================================
# Apply via: apply_run5_overrides(config)
# Revert to Run 4: simply don't call the function.
#
# Changes vs Run 4:
#   1. Train/test split -> COVID stress (train <= 2019, test from 2020)
#   2. Regime conditioning enabled with FiLM modulation
#   3. MVO auxiliary loss enabled (was 0.0)
#   4. Lighter turnover penalty (0.25->1.00 vs 0.75->2.00)
#   5. Lower drawdown trigger (target 0.12 vs 0.18)
RUN5_OVERRIDES = {
    # FIX 1: Train/test split -> COVID stress test
    "train_test_split": TRAIN_TEST_SPLIT_DATE_COVID_STRESS,

    # FIX 2: Enable regime conditioning with FiLM modulation
    "regime_conditioning_enabled": True,
    "regime_conditioning_hidden_dim": 32,
    "regime_conditioning_dropout": 0.05,
    "regime_conditioning_mode": "film",  # 'concat' for legacy, 'film' for FiLM

    # FIX 3: Enable MVO auxiliary loss
    "risk_aux_mvo_coef": 0.02,

    # FIX 4: Lighter turnover penalty curriculum
    "turnover_penalty_curriculum": {
        0:        0.25,
        100_000:  0.50,
        200_000:  0.75,
        300_000:  0.90,
        400_000:  1.00,
    },

    # FIX 5: Lower drawdown trigger
    "drawdown_constraint_target": 0.20,
    "drawdown_constraint_tolerance": -0.01,
}


def get_active_config(phase_name: str = None):
    """Selects the active configuration based on phase_name or environment variable."""
    if phase_name is None:
        phase_name = os.getenv("RL_PORTFOLIO_PHASE", "phase1")

    if phase_name.lower() == "phase1": return PHASE1_CONFIG
    if phase_name.lower() == "phase2": return PHASE2_CONFIG
    
    print(f"Warning: Invalid phase_name '{phase_name}'. Defaulting to Phase 1 Config.")
    return PHASE1_CONFIG


def apply_run5_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply Run 5 fixes to a config dict. Modifies config in-place and returns it.

    Usage in training notebook:
        config = get_active_config("phase1")
        apply_run5_overrides(config)  # <= adds all Run 5 fixes

    To revert to Run 4: simply don't call this function.

    Args:
        config: Phase config dict (e.g. PHASE1_CONFIG).
        overrides: Override dict (defaults to RUN5_OVERRIDES).

    Returns:
        The modified config dict (same object, modified in place).
    """
    global TRAIN_TEST_SPLIT_DATE
    if overrides is None:
        overrides = RUN5_OVERRIDES

    # --- FIX 1: Train/test split ---
    split_date = overrides.get("train_test_split")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        # Also set in the config dict so prepare_phase1_dataset picks it up
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
        print(f"[Run5] Train/test split => {split_date}")

    # --- FIX 2: Regime conditioning ---
    agent = config.get("agent_params", {})
    if "regime_conditioning_enabled" in overrides:
        agent["regime_conditioning_enabled"] = overrides["regime_conditioning_enabled"]
    if "regime_conditioning_hidden_dim" in overrides:
        agent["regime_conditioning_hidden_dim"] = overrides["regime_conditioning_hidden_dim"]
    if "regime_conditioning_dropout" in overrides:
        agent["regime_conditioning_dropout"] = overrides["regime_conditioning_dropout"]
    if "regime_conditioning_mode" in overrides:
        agent["regime_conditioning_mode"] = overrides["regime_conditioning_mode"]

    # --- FIX 3: MVO auxiliary loss ---
    ppo = agent.get("ppo_params", {})
    if "risk_aux_mvo_coef" in overrides:
        ppo["risk_aux_mvo_coef"] = overrides["risk_aux_mvo_coef"]
        print(f"[Run5] MVO aux coef => {overrides['risk_aux_mvo_coef']}")

    # --- FIX 4: Turnover penalty curriculum ---
    training = config.get("training_params", {})
    if "turnover_penalty_curriculum" in overrides:
        training["turnover_penalty_curriculum"] = copy.deepcopy(overrides["turnover_penalty_curriculum"])
        print(f"[Run5] Turnover penalty => {overrides['turnover_penalty_curriculum']}")

    # --- FIX 5: Drawdown constraint ---
    env = config.get("environment_params", {})
    dd = env.get("drawdown_constraint", {})
    if "drawdown_constraint_target" in overrides:
        dd["target"] = overrides["drawdown_constraint_target"]
        print(f"[Run5] DD target => {overrides['drawdown_constraint_target']}")
    if "drawdown_constraint_tolerance" in overrides:
        dd["tolerance"] = overrides["drawdown_constraint_tolerance"]

    regime_mode = overrides.get("regime_conditioning_mode", "concat")
    regime_on = overrides.get("regime_conditioning_enabled", False)
    print(
        f"[Run5] Regime conditioning: enabled={regime_on}, mode={regime_mode}, "
        f"hidden_dim={overrides.get('regime_conditioning_hidden_dim', 32)}"
    )
    print("[Run5] All overrides applied successfully.")
    return config


def validate_profile_manager_config(config: dict) -> bool:
    """Profile manager deprecated; keep for backwards compatibility."""
    return True

def get_available_profiles():
    """Returns a list of available profile names."""
    return [profile["name"] for profile in ALL_PROFILES_LIST]

def get_profile_by_name(profile_name: str):
    """Returns the profile configuration by name."""
    for profile in ALL_PROFILES_LIST:
        if profile["name"] == profile_name:
            return profile
    raise ValueError(f"Profile '{profile_name}' not found. Available profiles: {get_available_profiles()}")

# --- ARCHITECTURE UTILITIES ---

def get_available_architectures():
    """Returns list of supported neural network architectures."""
    return ['TCN', 'TCN_ATTENTION', 'TCN_FUSION']

def is_sequential_architecture(architecture: str) -> bool:
    """Check if architecture requires sequential (3D) input."""
    architecture_upper = architecture.upper()
    sequential_archs = ['TCN', 'TCN_ATTENTION', 'TCN_FUSION', 'GRU', 'RNN']
    return any(arch in architecture_upper for arch in sequential_archs)

def validate_agent_params(agent_params: dict) -> bool:
    """Validates agent parameters for completeness and consistency."""
    
    # Check architecture type
    if "actor_critic_type" not in agent_params:
        print("Error: 'actor_critic_type' not specified in agent_params")
        return False
    
    arch_type = agent_params["actor_critic_type"]
    available = get_available_architectures()
    
    if arch_type not in available:
        print(f"Error: Invalid architecture '{arch_type}'. Available: {available}")
        return False
    
    # Check sequence length for sequential models
    if is_sequential_architecture(arch_type):
        if "sequence_length" not in agent_params or agent_params["sequence_length"] < 2:
            print(f"Error: Sequential architecture '{arch_type}' requires sequence_length >= 2")
            return False
        
        # Check architecture-specific params
        
        if 'TCN' in arch_type and "tcn_filters" not in agent_params:
            print(f"Warning: 'tcn_filters' not specified for {arch_type}, using defaults")
        
        if 'ATTENTION' in arch_type and "attention_heads" not in agent_params:
            print(f"Warning: 'attention_heads' not specified for {arch_type}, using defaults")
    
    # Check PPO params
    if "ppo_params" not in agent_params:
        print("Error: 'ppo_params' not found in agent_params")
        return False
    
    print(f"Agent parameters validation passed for architecture: {arch_type}")
    return True


# Backward-compatible alias for phase-1 config consumers
BASE_CONFIG_TCN_PHASE1 = PHASE1_CONFIG
