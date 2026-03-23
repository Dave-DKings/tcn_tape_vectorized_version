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
TRAIN_TEST_SPLIT_DATE_RECENT = "2021-12-31"        # Train: <= 2021-12-31
TRAIN_TEST_SPLIT_DATE_COVID_STRESS = "2019-12-31"  # Train: <= 2019-12-31
TRAIN_TEST_SPLIT_DATE = TRAIN_TEST_SPLIT_DATE_BENCHMARK

# --- ASSET CONFIGURATION ---
ASSET_TICKERS = ["MSFT", "NVDA", "AMZN", "JPM", "CAT", "XOM", "JNJ", "PG", "GLD", "NEE"]
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
    "num_eigenvalues": min(2, NUM_ASSETS),
    "num_loading_components": min(2, NUM_ASSETS),
    "include_explained_variance_ratios": True,
    "include_trace": True,
    "include_effective_rank": True,
    "include_pairwise_correlation_stats": True,
    "include_pc_loadings": True,
}

ACTUARIAL_PARAMS = {
    "enabled": False,
    "severity_buckets": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
    "development_horizons": [10, 20, 30, 60, 90, 120],
    "min_events_for_credibility": 2,       # Reduced from 5 — censored events increase sample size
    "min_drawdown_depth": 0.03,            # 3% materiality gate — filters microstructure noise
    "recovery_retracement": 0.50,          # 50% Fibonacci retracement closes an event (partial recovery)
}

FUNDAMENTAL_FEATURES_CONFIG = {
    "enabled": False,
    # CSV expected to contain columns: Date, Ticker, FCFE, Revenue, NCFO
    "data_path": os.path.join(BASE_DATA_PATH, "quarterly_fundamentals.csv"),
    "lag_quarters": 8,
    "staleness_days_normalizer": 90.0,
    # Information-availability guard: shift feature availability forward by N days.
    # If your CSV "Date" is already the publication/release date, keep at 1.
    # If "Date" is period-end, increase (e.g., 45-60) to avoid look-ahead bias.
    "report_lag_days": 1,
}

# Canonical Exp6 feature-audit active set.
# This is enforced via allowlist to keep training/evaluation deterministic.
# Default runtime uses the non-actuarial subset (actuarial is optional/off).
# Non-actuarial count: 60 (includes 3 regime-buy + 5 alpha-return features)
# Full count with actuarial extension: 64 (60 + 4 actuarial)
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
    "AlphaRet_1d",
    "AlphaRet_5d",
    "AlphaRet_20d",
    "AlphaRet_5d_Z",
    "AlphaRet_20d_Z",
    "Residual_Momentum_21",
    "Volume_Percentile_63",
    "ShortTerm_Reversal_5",
    "VolOfVol_63",
    "Beta_to_Market",
    "OBV_Delta_Norm_21",
    # Covariance
    "Covariance_Eigenvalue_0",
    "Covariance_Eigenvalue_1",
    "Covariance_ExplainedVarRatio_0",
    "Covariance_ExplainedVarRatio_1",
    "Covariance_Trace",
    "Covariance_EffectiveRank",
    "Covariance_MeanPairwiseCorr",
    "Covariance_CorrDispersion",
    "Covariance_PC1_Loading",
    "Covariance_PC2_Loading",
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
    "active_features_allowlist": copy.deepcopy(PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL),
    "feature_audit_plan_name": "exp6_feature_audit_20260221_v2",
    "feature_audit_expected_non_actuarial_count": len(PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL),
    "feature_audit_expected_total_count": len(PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL),
}

ALPHA_FEATURES_CONFIG = {
    "enabled": True,
    "cross_sectional_column": "LogReturn_1d",
    "residual_momentum_window": 21,
    "volume_percentile_window": 63,
    "reversal_window": 5,
    "vol_of_vol_window": 63,
    "beta_window": 63,
    "alpha_return_windows": [1, 5, 20],
    "alpha_return_zscore_windows": [5, 20],
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
    "Covariance_ExplainedVarRatio_",
    "Covariance_Trace",
    "Covariance_EffectiveRank",
    "Covariance_MeanPairwiseCorr",
    "Covariance_CorrDispersion",
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
    # Information-availability guard: each macro value becomes usable after N days.
    # Default 1 day prevents same-day publication leakage.
    "release_lag_days": 1,
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
        # Episode-level regime-CVaR: DISABLED — Lagrangian CVaR provides dense per-step tail pressure
        "episode_cvar_enabled": False,
        "episode_cvar_alpha": 0.05,            # CVaR tail fraction (5% worst returns)
        "episode_cvar_scalar": 100.0,  # Reduced from 500          # Multiplier for CVaR penalty/bonus
        "episode_cvar_min_history": 40,        # Skip noisy CVaR estimates on very short episodes
        "episode_cvar_low_vol_boundary": 0.12, # Annualized vol boundary for low-vol episodes
        "episode_cvar_high_vol_boundary": 0.25,# Annualized vol boundary for high-vol episodes
        "episode_cvar_low_vol_threshold": -0.012,  # Calm markets should still keep daily tail losses tight
        "episode_cvar_mid_vol_threshold": -0.017,  # Moderate tail budget in mixed regimes
        "episode_cvar_high_vol_threshold": -0.024, # Allow wider tails when realized vol is structurally high
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
        "dsr_regime_scaling": {
            "enabled": True,
            "vol_window": 21,
            "low_vol_threshold": 0.12,
            "high_vol_threshold": 0.25,
            "low_pos_mult": 1.0,   # Low vol: keep full reward for good picks
            "low_neg_mult": 0.3,   # Low vol: reduce penalty → encourage rotation
            "mid_pos_mult": 1.0,
            "mid_neg_mult": 1.0,
            "high_pos_mult": 1.5,  # High vol: amplify reward for safety
            "high_neg_mult": 1.5,  # High vol: amplify penalty for risk
        },
        "outperformance_bonus_enabled": True,
        "outperformance_bonus_scalar": 5.0,
        "spy_outperformance_bonus_enabled": True,
        "spy_outperformance_bonus_scalar": 3.0,
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
            "cooling_rate": 0.25,             # Faster cooldown (was 0.10)
            "lambda_carry_decay": 0.75,         # Stronger decay (was 0.9)
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
        "distributional_critic_enabled": True,       # SOTA-FIX: quantile regression critic learns full return distribution (CVaR baked in)
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
        "dual_head_projection_max_single_position": 0.25,
        "dual_head_projection_min_cash_position": 0.05,
        # Mixture-of-Dirichlets policy head.
        "mixture_dirichlet_enabled": False,
        "mixture_dirichlet_num_components": 3,
        "mixture_dirichlet_gating_hidden_dims": [64],
        "mixture_dirichlet_component_hidden_dims": [64],
        "mixture_dirichlet_eval_mode": "top_component_mean",

        # Dirichlet alpha activation (controls action concentration)
        "dirichlet_alpha_activation": "exp_tanh",   # PERF-FIX #4c: exp(tanh(x)*scale) — better diversity than softplus
        "dirichlet_exp_clip": (-5.0, 3.0),
        "dirichlet_logit_temperature": 0.5,           # PERF-FIX #4a: sharper allocation (was 1.0)
        "dirichlet_exp_tanh_scale": 2.5,
        "dirichlet_softplus_alpha_floor": 0.0,
        "dirichlet_softplus_alpha_scale": 1.0,
        "dirichlet_cross_sectional_standardize": False,
        # Optional adaptive temperature controller:
        # temperature = clip(base + slope * |logit|, t_min, t_max)
        # Larger |logit| -> larger temperature -> flatter alpha map.
        "dirichlet_adaptive_temperature_enabled": False,
        "dirichlet_adaptive_temperature_base": 1.0,
        "dirichlet_adaptive_temperature_slope": 0.0,
        "dirichlet_adaptive_temperature_min": 0.8,
        "dirichlet_adaptive_temperature_max": 2.5,
        "dirichlet_alpha_cap": 12.0,                 # SOTA-FIX: structural bound on concentration (was 50.0). Still allows 12:1 conviction vs equal-weight.

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
            "alpha_diversity_coef": 0.01,             # SOTA-FIX: HHI anti-concentration penalty (sign corrected)
            "alpha_dispersion_coef": 0.0,            # Run9: penalize near-uniform allocations (disabled by default)
            "alpha_dispersion_target_std": 0.05,
            "mixture_dirichlet_balance_coef": 0.0,
            "mixture_dirichlet_separation_coef": 0.0,
            "mixture_dirichlet_entropy_coef": 0.0,
            "mixture_component_dispersion_coef": 0.0,
            "mixture_component_target_std": 0.30,
            "mixture_component_min_distance": 0.10,
            "mixture_dirichlet_balance_schedule": [],
            "mixture_dirichlet_entropy_schedule": [],
            # Optional risk-aware actor auxiliaries.
            "use_risk_aux_loss": True,
            # Per-asset feature index used as one-step return proxy in structured state tensor.
            "risk_aux_return_feature_index": 0,
            "risk_aux_cash_return": 0.0,
            "risk_aux_sharpe_coef": 0.0,
            "risk_aux_mvo_coef": 0.0,
            "risk_aux_cvar_coef": 0.0,       # DISABLED: distributional critic (17q) provides tail awareness
            "risk_aux_cvar_alpha": 0.05,
            "risk_aux_cvar_adaptive_enabled": False,  # DISABLED: not needed with distributional critic
            "risk_aux_cvar_target": 0.02,
            "risk_aux_cvar_adapt_lr": 0.05,
            "risk_aux_cvar_min_coef": 0.0,
            "risk_aux_cvar_max_coef": 0.08,
            "risk_aux_mvo_cov_ridge": 1e-3,
            "risk_aux_mvo_long_only": True,
            "risk_aux_mvo_risky_budget": 0.95,
            "distributional_huber_kappa": 1.0,
            "distributional_mean_loss_coef": 0.1,
            "dual_head_consistency_coef": 0.0,
            # SOTA-FIX Phase 3: Auxiliary per-asset return prediction (UNREAL-style)
            "aux_return_pred_enabled": True,           # Forces backbone asset-discriminative learning
            "aux_return_pred_coef": 0.10,              # MSE loss weight for aux return prediction
            # SOTA-FIX Phase 3: Lagrangian CVaR constraint (RCPO)
            "lagrangian_cvar_enabled": True,            # Dense step-level tail-risk constraint
            "lagrangian_cvar_threshold": -0.017,        # CVaR floor (mid-regime calibrated)
            "lagrangian_cvar_lr": 0.01,                 # Multiplier adaptation speed
            "lagrangian_cvar_lambda_max": 2.0,          # Maximum Lagrangian multiplier
            "lagrangian_cvar_penalty_scale": 1.0,       # Run9: scale dense CVaR penalty before reward normalization
            "cvar_advantage_weight": 0.0,               # Run9: blend lower-tail critic estimate into GAE baseline
            "cvar_advantage_k": 4,
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
        "log_interval_episodes": 1,  # Log every episode
        "update_log_interval": 20,
        "alpha_diversity_log_interval": 10,
        "alpha_diversity_warning_after_updates": 500,
        "alpha_diversity_warning_std_threshold": 0.30,
        "save_freq_episodes": 50,
        "max_episode_length": None,  # Episode length controlled by curriculum
        
        # STATE-OF-THE-ART FIX #2: Stronger Entropy Incentive
        "entropy_coefficient": 0.10,  # Diversification bonus weight (10x stronger for meaningful impact)
        
        # STATE-OF-THE-ART FIX #3: Position Size Constraints
        "max_single_position": 25.00,  # Cap at 25% per asset — soft constraints handle concentration
        
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
        # SOTA-FIX: Entropy coefficient annealing (SAC-inspired exploration)
        # High early entropy forces Dirichlet to spread probability across assets,
        # preventing alpha collapse. Anneals to let the agent exploit learned diversity.
        "ppo_entropy_coef_schedule": [
            {"threshold": 0,        "entropy_coef": 0.010},
            {"threshold": 100_000,  "entropy_coef": 0.005},
            {"threshold": 250_000,  "entropy_coef": 0.002},
            {"threshold": 400_000,  "entropy_coef": 0.001},
        ],
        # SOTA-FIX: Dirichlet temperature annealing
        # Temperature > 1 flattens the Dirichlet distribution, forcing diverse
        # portfolio sampling early. Combined with entropy schedule, powerful anti-collapse.
        "dirichlet_temperature_schedule": [
            {"threshold": 0,        "temperature": 1.5},
            {"threshold": 150_000,  "temperature": 1.2},
            {"threshold": 300_000,  "temperature": 1.0},
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
        # Episode-level regime-CVaR: DISABLED — Lagrangian CVaR provides dense per-step tail pressure
        "episode_cvar_enabled": False,
        "episode_cvar_alpha": 0.05,
        "episode_cvar_scalar": 100.0,  # Reduced from 500
        "episode_cvar_min_history": 40,
        "episode_cvar_low_vol_boundary": 0.12,
        "episode_cvar_high_vol_boundary": 0.25,
        "episode_cvar_low_vol_threshold": -0.012,
        "episode_cvar_mid_vol_threshold": -0.017,
        "episode_cvar_high_vol_threshold": -0.024,
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
        "dsr_regime_scaling": {
            "enabled": True,
            "vol_window": 21,
            "low_vol_threshold": 0.12,
            "high_vol_threshold": 0.25,
            "low_pos_mult": 1.0,   # Low vol: keep full reward for good picks
            "low_neg_mult": 0.3,   # Low vol: reduce penalty → encourage rotation
            "mid_pos_mult": 1.0,
            "mid_neg_mult": 1.0,
            "high_pos_mult": 1.5,  # High vol: amplify reward for safety
            "high_neg_mult": 1.5,  # High vol: amplify penalty for risk
        },
        "outperformance_bonus_enabled": True,
        "outperformance_bonus_scalar": 5.0,
        "spy_outperformance_bonus_enabled": True,
        "spy_outperformance_bonus_scalar": 3.0,
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
            "cooling_rate": 0.25,             # Faster cooldown (was 0.10)
            "lambda_carry_decay": 0.75,         # Stronger decay (was 0.9)
        },
        "drawdown_constraint_overrides": {
            "sequential": {
                "penalty_coef": 1.5,
                "dual_learning_rate": 0.10,
                "lambda_floor": 0.0,
                "lambda_max": 5.0,
                "tolerance": -0.015,
                "penalty_reference": "trigger_boundary",
                "cooling_rate": 0.25,             # Faster cooldown (was 0.10)
                "lambda_carry_decay": 0.75,         # Stronger decay (was 0.9)
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
        "dual_head_projection_max_single_position": 0.25,
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
            "alpha_dispersion_coef": 0.0,
            "alpha_dispersion_target_std": 0.05,
            "risk_aux_return_feature_index": 0,
            "risk_aux_cash_return": 0.0,
            "risk_aux_sharpe_coef": 0.0,
            "risk_aux_mvo_coef": 0.0,
            "risk_aux_cvar_coef": 0.0,       # DISABLED: step-level CVaR suppresses conviction
            "risk_aux_cvar_alpha": 0.05,
            "risk_aux_cvar_adaptive_enabled": False,  # DISABLED: distributional critic + Lagrangian CVaR replace step-level aux
            "risk_aux_cvar_target": 0.015,
            "risk_aux_cvar_adapt_lr": 0.05,
            "risk_aux_cvar_min_coef": 0.0,
            "risk_aux_cvar_max_coef": 0.08,
            "risk_aux_mvo_cov_ridge": 1e-3,
            "risk_aux_mvo_long_only": True,
            "risk_aux_mvo_risky_budget": 0.95,
            "distributional_huber_kappa": 1.0,
            "distributional_mean_loss_coef": 0.1,
            "lagrangian_cvar_penalty_scale": 1.0,
            "cvar_advantage_weight": 0.0,
            "cvar_advantage_k": 4,
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
        "log_interval_episodes": 1,  # Log every episode
        "save_freq_episodes": 50,
        "max_episode_length": None,  # Use full dataset horizon

        # STATE-OF-THE-ART FIX #2: Stronger Entropy Incentive
        "entropy_coefficient": 0.10,  # Diversification bonus weight (10x stronger for meaningful impact)
        
        # STATE-OF-THE-ART FIX #3: Position Size Constraints
        "max_single_position": 25.00,  # Cap at 25% per asset — soft constraints handle concentration
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


_DEEP_UPDATE_REPLACE_KEYS = {
    # Curricula are canonical schedules; merging old thresholds into new ones causes drift.
    "turnover_penalty_curriculum",
    "action_execution_beta_curriculum",
}


def _deep_update_config(target: dict, updates: dict) -> dict:
    """Recursively merge config updates into target."""
    for key, value in updates.items():
        if key in _DEEP_UPDATE_REPLACE_KEYS:
            target[key] = copy.deepcopy(value)
        elif isinstance(value, dict) and isinstance(target.get(key), dict):
            _deep_update_config(target[key], value)
        else:
            target[key] = copy.deepcopy(value)
    return target


def enforce_feature_audit_plan(config: dict) -> dict:
    """Ensure the active feature allowlist remains the canonical notebook view."""
    feature_params = config.setdefault("feature_params", {})
    feature_selection = feature_params.setdefault("feature_selection", {})
    feature_selection["enforce_allowlist"] = True
    feature_selection["allowlist_apply_to_phase2"] = False
    allowlist = list(dict.fromkeys(feature_selection.get("active_features_allowlist", []) or []))
    feature_selection["active_features_allowlist"] = allowlist
    return config


RUN9_ALPHA_OVERRIDES = {
    "TRAIN_TEST_SPLIT_DATE": TRAIN_TEST_SPLIT_DATE_COVID_STRESS,
    "feature_params": {
        "fundamental_features": {"enabled": False},
        "actuarial_params": {"enabled": False},
    },
    "agent_params": {
        "actor_critic_type": "TCN_FUSION",
        "use_attention": False,
        "use_fusion": True,
        "tcn_filters": [64, 96, 128, 128, 128],
        "tcn_kernel_size": 5,
        "tcn_dilations": [1, 2, 4, 8, 16],
        "tcn_dropout": 0.15,
        # Keep the base self-attention block, but disable the extra mixer stack.
        "fusion_cross_asset_mixer_enabled": False,
        "fusion_cross_asset_mixer_layers": 1,
        "fusion_cross_asset_mixer_expansion": 2.0,
        "fusion_cross_asset_mixer_dropout": 0.10,
        "fusion_asset_identity_enabled": True,
        "fusion_context_cross_attention_enabled": False,
        "fusion_per_asset_alpha_head": True,
        "fusion_alpha_head_hidden_dims": [128, 64],
        "fusion_alpha_head_dropout": 0.05,
        "recurrent_memory_enabled": False,
        "regime_conditioning_enabled": False,
        "state_augmentation_enabled": False,
        "distributional_critic_enabled": True,
        "distributional_num_quantiles": 17,
        "dirichlet_alpha_activation": "exp_tanh",
        # Match the initial schedule value so the startup banner reflects the live setting.
        "dirichlet_logit_temperature": 1.2,
        "dirichlet_alpha_cap": 16.0,
        "dirichlet_exp_tanh_scale": 3.5,
        "dirichlet_softplus_alpha_floor": 0.0,
        "dirichlet_softplus_alpha_scale": 1.0,
        "dirichlet_cross_sectional_standardize": False,
        "dirichlet_epsilon": {"max": 0.2, "min": 0.02},
        "ppo_params": {
            "num_ppo_epochs": 3,
            "policy_clip": 0.15,
            "target_kl": 0.0,
            "kl_stop_multiplier": 2.0,
            "minibatches_before_kl_stop": 2,
            "max_grad_norm": 0.50,
            "value_clip": 0.3,
            "actor_lr": 3e-5,
            "critic_lr": 1.5e-4,
            "entropy_coef": 0.003,
            "alpha_diversity_coef": 0.01,
            "alpha_dispersion_coef": 0.05,
            "alpha_dispersion_target_std": 0.07,
            "use_risk_aux_loss": True,
            "risk_aux_return_feature_index": 0,
            "risk_aux_cash_return": 0.0,
            "risk_aux_sharpe_coef": 0.0,
            "risk_aux_mvo_coef": 0.0,
            "risk_aux_cvar_coef": 0.0,
            "risk_aux_cvar_alpha": 0.05,
            "risk_aux_cvar_adaptive_enabled": False,
            "risk_aux_mvo_cov_ridge": 1e-3,
            "risk_aux_mvo_long_only": True,
            "risk_aux_mvo_risky_budget": 0.95,
            "aux_return_pred_enabled": True,
            "aux_return_pred_coef": 0.35,
            "lagrangian_cvar_enabled": True,
            "lagrangian_cvar_threshold": -0.025,
            "lagrangian_cvar_lr": 0.004,
            "lagrangian_cvar_lambda_max": 5.0,
            "lagrangian_cvar_penalty_scale": 5.0,
            "cvar_advantage_weight": 0.10,
            "cvar_advantage_k": 4,
            "popart_enabled": True,
            "popart_min_std": 1e-3,
            "multi_horizon_reward_enabled": False,
            "multi_horizon_reward_coef": 0.0,
        },
    },
    "environment_params": {
        "target_turnover": 0.35,
        "turnover_penalty_scalar": 0.50,
        "transaction_cost_pct": 0.001,
        "concentration_penalty_scalar": 0.0,
        "top_weight_penalty_scalar": 0.0,
        "action_realization_penalty_scalar": 0.5,
        "target_top_weight": 0.30,
        "penalty_budget_ratio": 1.0,
        "outperformance_bonus_enabled": False,
        "spy_outperformance_bonus_enabled": True,
        "spy_outperformance_bonus_scalar": 3.0,
        "regime_sampling_mode": "uniform_regime",
        "episode_cvar_enabled": False,
        "drawdown_constraint": {
            "target": 0.15,
            "tolerance": -0.01,
            "penalty_coef": 1.5,
            "lambda_init": 0.10,
            "lambda_carry_decay": 0.4,
        },
    },
    "training_params": {
        "max_total_timesteps": 500_000,
        "timesteps_per_ppo_update": 1008,
        "num_parallel_envs": 4,
        "timesteps_per_ppo_update_schedule": [
            {"threshold": 0, "timesteps_per_update": 1008},
            {"threshold": 150_000, "timesteps_per_update": 1512},
            {"threshold": 300_000, "timesteps_per_update": 2016},
        ],
        "batch_size_ppo_schedule": [
            {"threshold": 0, "batch_size": 252},
            {"threshold": 150_000, "batch_size": 336},
            {"threshold": 300_000, "batch_size": 504},
        ],
        "actor_lr_schedule": [
            {"threshold": 0, "lr": 3e-5},
            {"threshold": 150_000, "lr": 2e-5},
            {"threshold": 350_000, "lr": 1e-5},
        ],
        "ppo_gamma_schedule": [
            {"threshold": 0, "gamma": 0.990},
            {"threshold": 150_000, "gamma": 0.995},
            {"threshold": 350_000, "gamma": 0.998},
        ],
        "ppo_gae_lambda_schedule": [
            {"threshold": 0, "gae_lambda": 0.92},
            {"threshold": 150_000, "gae_lambda": 0.95},
            {"threshold": 350_000, "gae_lambda": 0.97},
        ],
        "ppo_entropy_coef_schedule": [
            {"threshold": 0, "entropy_coef": 0.003},
            {"threshold": 100_000, "entropy_coef": 0.002},
            {"threshold": 250_000, "entropy_coef": 0.0015},
            {"threshold": 400_000, "entropy_coef": 0.001},
        ],
        "dirichlet_temperature_schedule": [
            {"threshold": 0, "temperature": 1.0},
            {"threshold": 150_000, "temperature": 0.9},
            {"threshold": 300_000, "temperature": 0.8},
        ],
        "ra_kl_enabled": False,
        "use_episode_length_curriculum": True,
        "episode_length_curriculum_schedule": [
            {"threshold": 0, "limit": 756},
            {"threshold": 100_000, "limit": 1008},
            {"threshold": 250_000, "limit": 1500},
            {"threshold": 400_000, "limit": None},
        ],
        "episode_length_curriculum_smooth_enabled": True,
        "episode_length_curriculum_overlap_steps": 10_000,
        "action_execution_beta_schedule": [
            {"threshold": 0, "beta": 0.35},
            {"threshold": 100_000, "beta": 0.45},
            {"threshold": 200_000, "beta": 0.55},
            {"threshold": 350_000, "beta": 0.55},
        ],
        "action_execution_beta_curriculum": {
            0: 0.35,
            100_000: 0.45,
            200_000: 0.55,
            350_000: 0.55,
        },
        "evaluation_action_execution_beta": 0.60,
        "turnover_penalty_curriculum": {
            0: 0.50,
            100_000: 0.75,
            200_000: 0.90,
            300_000: 1.00,
            400_000: 1.00,
        },
        "evaluation_turnover_penalty_scalar": 1.00,
        "log_step_diagnostics": True,
        "update_log_interval": 1,
        "alpha_diversity_log_interval": 2,
        "alpha_diversity_warning_after_updates": 10,
        "alpha_diversity_warning_std_threshold": 0.25,
        "deterministic_validation_checkpointing_enabled": True,
        "deterministic_validation_eval_every_episodes": 5,
        "deterministic_validation_mode": "mean",
        "deterministic_validation_episode_length_limit": None,
        "deterministic_validation_episode_length_limit_curriculum": [
            {"threshold": 0, "limit": 756},
            {"threshold": 100_000, "limit": 1008},
            {"threshold": 250_000, "limit": 1500},
            {"threshold": 400_000, "limit": None},
        ],
        "deterministic_validation_sharpe_min": 0.50,
        "deterministic_validation_sharpe_min_delta": 0.0,
        "deterministic_validation_seed_offset": 10_000,
        "deterministic_validation_log_alpha_stats": True,
        "deterministic_validation_checkpointing_only": True,
        "deterministic_validation_multi_horizon_enabled": True,
        "deterministic_validation_multi_horizon_limits": [252, 504, 756, 1008],
        "deterministic_validation_multi_horizon_weights": [0.35, 0.30, 0.20, 0.15],
        "deterministic_validation_multi_horizon_dd_penalty_coef": 0.25,
        "deterministic_validation_stochastic_sanity_enabled": True,
        "deterministic_validation_stochastic_sanity_runs": 5,
        "deterministic_validation_stochastic_sanity_episode_length_limit": 252,
        "deterministic_validation_stochastic_sanity_min_mean_sharpe": 0.2,
        "deterministic_validation_stochastic_sanity_max_sharpe_std": 1.0,
        "deterministic_validation_require_spy_outperformance": True,
        "deterministic_validation_min_spy_outperformance": 0.0,
        "high_watermark_checkpoint_enabled": False,
        "step_sharpe_checkpoint_enabled": False,
        "periodic_checkpoint_every_steps": 0,
        "rare_checkpoint_params": {"enable": False},
        "tape_checkpoint_threshold": 999.0,
    },
}


RUN10_ALPHA_OVERRIDES = copy.deepcopy(RUN9_ALPHA_OVERRIDES)
RUN10_ALPHA_OVERRIDES.update(
    {
        "TRAIN_TEST_SPLIT_DATE": TRAIN_TEST_SPLIT_DATE_RECENT,
        "ANALYSIS_START_DATE": "2016-01-01",
    }
)
RUN10_ALPHA_OVERRIDES["agent_params"].update(
    {
        "regime_conditioning_enabled": True,
        "regime_conditioning_mode": "film",
        "regime_conditioning_dropout": 0.05,
    }
)
RUN10_ALPHA_OVERRIDES["agent_params"]["ppo_params"].update(
    {
        "risk_aux_mvo_coef": 0.002,
        "lagrangian_cvar_penalty_scale": 3.0,
    }
)
RUN10_ALPHA_OVERRIDES["environment_params"].update(
    {
        "drawdown_constraint": {
            "penalty_coef": 1.5,
        },
    }
)
RUN10_ALPHA_OVERRIDES["feature_params"].update(
    {
        "actuarial_params": {"enabled": False},
        "feature_selection": {
            "active_features_allowlist": copy.deepcopy(PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL),
            "feature_audit_expected_non_actuarial_count": len(PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL),
            "feature_audit_expected_total_count": len(PHASE12_AUDIT_ACTIVE_FEATURES_NON_ACTUARIAL),
        },
        "alpha_features": {
            "enabled": True,
            "alpha_return_windows": [1, 5, 20],
            "alpha_return_zscore_windows": [5, 20],
        }
    }
)
RUN10_ALPHA_OVERRIDES["training_params"].update(
    {
        "action_execution_beta_schedule": [
            {"threshold": 0, "beta": 0.35},
            {"threshold": 100_000, "beta": 0.45},
            {"threshold": 200_000, "beta": 0.55},
            {"threshold": 350_000, "beta": 0.60},
        ],
        "critic_lr_schedule": [
            {"threshold": 0, "lr": 1.5e-4},
            {"threshold": 150_000, "lr": 1.2e-4},
            {"threshold": 350_000, "lr": 1.0e-4},
        ],
        "action_execution_beta_curriculum": {
            0: 0.35,
            100_000: 0.45,
            200_000: 0.55,
            350_000: 0.60,
        },
        "evaluation_action_execution_beta": 0.60,
        "turnover_penalty_curriculum": {
            0: 0.25,
            100_000: 0.55,
            200_000: 0.75,
            300_000: 0.90,
            400_000: 1.00,
        },
        "ppo_entropy_coef_schedule": [
            {"threshold": 0, "entropy_coef": 0.003},
            {"threshold": 100_000, "entropy_coef": 0.003},
            {"threshold": 250_000, "entropy_coef": 0.0025},
            {"threshold": 400_000, "entropy_coef": 0.0015},
        ],
        "aux_return_pred_coef_schedule": [
            {"threshold": 0, "aux_return_pred_coef": 0.35},
            {"threshold": 150_000, "aux_return_pred_coef": 0.30},
            {"threshold": 300_000, "aux_return_pred_coef": 0.25},
        ],
        "dirichlet_temperature_schedule": [
            {"threshold": 0, "temperature": 1.0},
            {"threshold": 150_000, "temperature": 0.9},
            {"threshold": 300_000, "temperature": 0.8},
        ],
        "deterministic_validation_checkpointing_enabled": False,
        "deterministic_validation_checkpointing_only": False,
        "periodic_checkpoint_every_steps": 50_000,
        "high_watermark_checkpoint_enabled": True,
        "high_watermark_sharpe_threshold": 0.70,
        "high_watermark_max_drawdown_abs_threshold": 0.25,
        "training_early_stop_enabled": True,
        "training_early_stop_warmup_steps": 100_000,
        "training_early_stop_ema_alpha": 0.10,
        "training_early_stop_min_delta": 0.01,
        "training_early_stop_patience_updates": 25,
        "training_early_stop_dd_soft_limit_pct": 25.0,
        "training_early_stop_turnover_soft_limit_pct": 35.0,
        "training_early_stop_dd_penalty_weight": 0.60,
        "training_early_stop_turnover_penalty_weight": 0.30,
        "training_early_stop_hard_dd_limit_pct": 45.0,
        "training_early_stop_hard_dd_patience_updates": 8,
        "training_early_stop_mean_adv_abs_threshold": 1e-4,
        "training_early_stop_mean_adv_patience_updates": 20,
    }
)


# ── Run 17: Expanded 20-asset universe with 10yr train / 5yr test ──
RUN17_EXPANDED_OVERRIDES = copy.deepcopy(RUN10_ALPHA_OVERRIDES)
RUN17_EXPANDED_OVERRIDES.update(
    {
        "TRAIN_TEST_SPLIT_DATE": TRAIN_TEST_SPLIT_DATE_COVID_STRESS,  # "2019-12-31"
        "ANALYSIS_START_DATE": "2009-01-01",
        "ASSET_TICKERS": [
            "MSFT", "AAPL", "NVDA", "GOOGL", "AMZN",
            "JPM", "BRK-B", "V", "UNH", "JNJ",
            "PG", "KO", "HD", "CAT", "HON",
            "XOM", "COP", "NEE", "GLD", "AMT",
        ],
        "NUM_ASSETS": 20,
    }
)
RUN17_EXPANDED_OVERRIDES["agent_params"].update(
    {
        # Wider Dirichlet range is needed once the action simplex expands to 20 assets + cash.
        "dirichlet_alpha_cap": 50.0,
        "dirichlet_exp_tanh_scale": 5.0,
    }
)
RUN17_EXPANDED_OVERRIDES["agent_params"]["ppo_params"].update(
    {
        # Reduce forces toward near-uniform allocations and push harder for cross-sectional spread.
        "entropy_coef": 0.0015,
        "risk_aux_mvo_coef": 0.0,
        "alpha_diversity_coef": 0.002,
        "alpha_dispersion_coef": 0.10,
        "alpha_dispersion_target_std": 0.15,
        "lagrangian_cvar_penalty_scale": 0.0,
    }
)
RUN17_EXPANDED_OVERRIDES["training_params"].update(
    {
        "num_parallel_envs": 8,  # doubled from 4 for 21-dim Dirichlet exploration
        "ppo_entropy_coef_schedule": [
            {"threshold": 0, "entropy_coef": 0.0015},
            {"threshold": 100_000, "entropy_coef": 0.0015},
            {"threshold": 250_000, "entropy_coef": 0.0010},
            {"threshold": 400_000, "entropy_coef": 0.0005},
        ],
        "action_execution_beta_schedule": [
            {"threshold": 0, "beta": 0.55},
            {"threshold": 100_000, "beta": 0.70},
            {"threshold": 200_000, "beta": 0.85},
            {"threshold": 300_000, "beta": 1.00},
        ],
        "action_execution_beta_curriculum": {
            0: 0.55,
            100_000: 0.70,
            200_000: 0.85,
            300_000: 1.00,
        },
        "evaluation_action_execution_beta": 1.00,
        "turnover_penalty_curriculum": {
            0: 0.05,
            100_000: 0.10,
            200_000: 0.20,
            300_000: 0.30,
            400_000: 0.40,
        },
        "evaluation_turnover_penalty_scalar": 0.40,
        "reward_component_schedule": [
            {
                "threshold": 0,
                "phase": "A_return_only",
                "enable_base_reward": True,
                "enable_dsr_reward": False,
                "enable_turnover_penalty": False,
                "enable_benchmark_shaping": False,
                "enable_terminal_tape_bonus": False,
            },
            {
                "threshold": 150_000,
                "phase": "B_add_risk",
                "enable_base_reward": True,
                "enable_dsr_reward": True,
                "enable_turnover_penalty": False,
                "enable_benchmark_shaping": True,
                "enable_terminal_tape_bonus": False,
            },
            {
                "threshold": 300_000,
                "phase": "C_full_tape",
                "enable_base_reward": True,
                "enable_dsr_reward": True,
                "enable_turnover_penalty": True,
                "enable_benchmark_shaping": True,
                "enable_terminal_tape_bonus": True,
            },
        ],
        "training_early_stop_warmup_steps": 200_000,
        "training_early_stop_min_delta": 0.005,
        "training_early_stop_patience_updates": 40,
        # Keep step-triggered artifacts off so training does not spam low-information checkpoints.
        "step_sharpe_checkpoint_enabled": False,
    }
)
RUN17_EXPANDED_OVERRIDES["environment_params"].update(
    {
        "target_turnover": 0.35,
        "turnover_penalty_scalar": 0.05,
        "action_execution_beta": 0.55,
        "action_realization_penalty_scalar": 0.0,
        "dsr_regime_scaling": {
            "enabled": True,
            "vol_window": 21,
            "low_vol_threshold": 0.12,
            "high_vol_threshold": 0.25,
            "low_pos_mult": 0.8,
            "low_neg_mult": 0.9,
            "mid_pos_mult": 1.0,
            "mid_neg_mult": 1.0,
            "high_pos_mult": 1.25,
            "high_neg_mult": 1.25,
        },
        "outperformance_bonus_enabled": True,
        "outperformance_bonus_scalar": 6.0,
        "outperformance_bonus_mode": "signed_clipped",
        "outperformance_bonus_clip": 0.02,
        "spy_outperformance_bonus_enabled": True,
        "spy_outperformance_bonus_scalar": 1.5,
        "spy_outperformance_bonus_mode": "signed_clipped",
        "spy_outperformance_bonus_clip": 0.01,
    }
)


def _scale_threshold_value(threshold: int, scale: float, *, quantum: int = 1_000) -> int:
    scaled = int(round(float(threshold) * float(scale)))
    if threshold > 0 and scaled <= 0:
        scaled = max(1, quantum)
    if quantum > 1:
        scaled = int(round(scaled / float(quantum))) * int(quantum)
    return max(0, scaled)


def _scale_threshold_schedule(entries: list, scale: float, *, quantum: int = 1_000) -> list:
    if not isinstance(entries, list):
        return []
    scaled_entries = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        new_entry = copy.deepcopy(entry)
        new_entry["threshold"] = _scale_threshold_value(int(entry.get("threshold", 0)), scale, quantum=quantum)
        scaled_entries.append(new_entry)

    # Later entries should override earlier ones if thresholds collide after scaling.
    deduped = {}
    for entry in scaled_entries:
        deduped[int(entry["threshold"])] = entry
    return [deduped[key] for key in sorted(deduped.keys())]


def _scale_threshold_mapping(mapping: dict, scale: float, *, quantum: int = 1_000) -> dict:
    if not isinstance(mapping, dict):
        return {}
    scaled = {}
    for threshold, value in mapping.items():
        scaled_threshold = _scale_threshold_value(int(threshold), scale, quantum=quantum)
        scaled[scaled_threshold] = copy.deepcopy(value)
    return {key: scaled[key] for key in sorted(scaled.keys())}


RUN17_TEST_OVERRIDES = copy.deepcopy(RUN17_EXPANDED_OVERRIDES)
_RUN17_TEST_TIMESTEPS = 100_000
_RUN17_TEST_SCALE = float(_RUN17_TEST_TIMESTEPS) / float(
    RUN17_EXPANDED_OVERRIDES["training_params"]["max_total_timesteps"]
)
RUN17_TEST_OVERRIDES["training_params"].update(
    {
        "max_total_timesteps": _RUN17_TEST_TIMESTEPS,
        "timesteps_per_ppo_update_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["timesteps_per_ppo_update_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "batch_size_ppo_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["batch_size_ppo_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "actor_lr_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["actor_lr_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "critic_lr_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["critic_lr_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "ppo_gamma_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["ppo_gamma_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "ppo_gae_lambda_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["ppo_gae_lambda_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "ppo_entropy_coef_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["ppo_entropy_coef_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "aux_return_pred_coef_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["aux_return_pred_coef_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "dirichlet_temperature_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["dirichlet_temperature_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "episode_length_curriculum_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["episode_length_curriculum_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "action_execution_beta_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["action_execution_beta_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "action_execution_beta_curriculum": _scale_threshold_mapping(
            RUN17_EXPANDED_OVERRIDES["training_params"]["action_execution_beta_curriculum"],
            _RUN17_TEST_SCALE,
        ),
        "turnover_penalty_curriculum": _scale_threshold_mapping(
            RUN17_EXPANDED_OVERRIDES["training_params"]["turnover_penalty_curriculum"],
            _RUN17_TEST_SCALE,
        ),
        "reward_component_schedule": _scale_threshold_schedule(
            RUN17_EXPANDED_OVERRIDES["training_params"]["reward_component_schedule"],
            _RUN17_TEST_SCALE,
        ),
        "periodic_checkpoint_every_steps": _scale_threshold_value(
            RUN17_EXPANDED_OVERRIDES["training_params"]["periodic_checkpoint_every_steps"],
            _RUN17_TEST_SCALE,
            quantum=1_000,
        ),
        "episode_length_curriculum_overlap_steps": _scale_threshold_value(
            RUN17_EXPANDED_OVERRIDES["training_params"].get("episode_length_curriculum_overlap_steps", 10_000),
            _RUN17_TEST_SCALE,
            quantum=1_000,
        ),
        # Keep the test run on a fixed 100k horizon for fair alpha-generator A/B comparisons.
        "training_early_stop_warmup_steps": _RUN17_TEST_TIMESTEPS,
    }
)


# ── Run 18: Canonical 10-asset scaled TAPE recipe with softened transitions ──
RUN18_OVERRIDES = copy.deepcopy(RUN17_EXPANDED_OVERRIDES)
RUN18_ACTIVE_FEATURE_ALLOWLIST = [
    "LogReturn_1d",
    "LogReturn_5d",
    "LogReturn_21d",
    "RollingVolatility_21d",
    "DownsideSemiVar_21d",
    "MACDh_12_26_9",
    "RSI_14",
    "ADX_14",
    "NATR_14",
    "Candle_BodyToRange",
    "Candle_CloseLocation",
    "Regime_Breadth_Positive",
    "CrossSectional_ZScore_LogReturn_1d",
    "AlphaRet_1d",
    "AlphaRet_5d",
    "AlphaRet_20d",
    "AlphaRet_5d_Z",
    "AlphaRet_20d_Z",
    "Residual_Momentum_21",
    "ShortTerm_Reversal_5",
    "VolOfVol_63",
    "Beta_to_Market",
    "BuyProb_Regime",
    "BuyEdge_Regime",
    "Covariance_Eigenvalue_0",
    "Covariance_Eigenvalue_1",
    "Covariance_ExplainedVarRatio_0",
    "Covariance_ExplainedVarRatio_1",
    "Covariance_Trace",
    "Covariance_EffectiveRank",
    "Covariance_MeanPairwiseCorr",
    "Covariance_CorrDispersion",
    "Covariance_PC1_Loading",
    "Covariance_PC2_Loading",
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
]
RUN18_OVERRIDES.update(
    {
        "TRAIN_TEST_SPLIT_DATE": TRAIN_TEST_SPLIT_DATE_COVID_STRESS,
        "ANALYSIS_START_DATE": "2009-01-01",
        "ASSET_TICKERS": ["NVDA", "MSFT", "AMZN", "JPM", "BRK-B", "CAT", "XOM", "NEE", "GLD", "KO"],
        "NUM_ASSETS": 10,
        "EQUAL_WEIGHT_CASH_ALLOCATION": 1.0 / 11.0,
    }
)
RUN18_OVERRIDES["feature_params"].update(
    {
        "dynamic_covariance": {
            **copy.deepcopy(DYNAMIC_COVARIANCE_PARAMS),
            "num_eigenvalues": 2,
            "num_loading_components": 2,
        },
        "feature_selection": {
            **copy.deepcopy(FEATURE_SELECTION_CONFIG),
            "enforce_allowlist": True,
            "allowlist_apply_to_phase2": False,
            "active_features_allowlist": copy.deepcopy(RUN18_ACTIVE_FEATURE_ALLOWLIST),
            "feature_audit_expected_non_actuarial_count": len(RUN18_ACTIVE_FEATURE_ALLOWLIST),
            "feature_audit_expected_total_count": len(RUN18_ACTIVE_FEATURE_ALLOWLIST),
        },
    }
)
RUN18_OVERRIDES["agent_params"].update(
    {
        "num_assets": 10,
        "tcn_filters": [64, 96, 128],
        "tcn_dilations": [1, 2, 4],
        "tcn_kernel_size": 5,
        "dirichlet_alpha_activation": "cross_softplus",
        "dirichlet_softplus_alpha_floor": 0.75,
        "dirichlet_softplus_alpha_scale": 2.5,
        "dirichlet_cross_sectional_standardize": True,
    }
)
RUN18_OVERRIDES["agent_params"]["ppo_params"].update(
    {
        "entropy_coef": 0.0007,
        "risk_aux_mvo_coef": 0.0,
        "alpha_diversity_coef": 0.0,
        "alpha_dispersion_coef": 0.20,
        "alpha_dispersion_target_std": 0.20,
        "lagrangian_cvar_enabled": False,
        "lagrangian_cvar_penalty_scale": 0.0,
    }
)
RUN18_OVERRIDES["training_params"].update(
    {
        "max_total_timesteps": 500_000,
        "ppo_entropy_coef_schedule": [
            {"threshold": 0, "entropy_coef": 0.0007},
            {"threshold": 150_000, "entropy_coef": 0.0005},
            {"threshold": 300_000, "entropy_coef": 0.0003},
            {"threshold": 425_000, "entropy_coef": 0.0001},
        ],
        "action_execution_beta_schedule": [
            {"threshold": 0, "beta": 0.55},
            {"threshold": 150_000, "beta": 0.65},
            {"threshold": 300_000, "beta": 0.80},
            {"threshold": 425_000, "beta": 0.95},
            {"threshold": 475_000, "beta": 1.00},
        ],
        "action_execution_beta_curriculum": {
            0: 0.55,
            150_000: 0.65,
            300_000: 0.80,
            425_000: 0.95,
            475_000: 1.00,
        },
        "evaluation_action_execution_beta": 1.00,
        "turnover_penalty_curriculum": {
            0: 0.00,
            200_000: 0.05,
            325_000: 0.10,
            400_000: 0.20,
            475_000: 0.30,
        },
        "evaluation_turnover_penalty_scalar": 0.30,
        "reward_component_schedule": [
            {
                "threshold": 0,
                "phase": "A_return_only",
                "enable_base_reward": True,
                "enable_dsr_reward": False,
                "enable_turnover_penalty": False,
                "enable_benchmark_shaping": False,
                "enable_terminal_tape_bonus": False,
                "base_reward_weight": 1.0,
                "dsr_reward_weight": 0.0,
                "turnover_penalty_weight": 0.0,
                "benchmark_shaping_weight": 0.0,
                "terminal_tape_bonus_weight": 0.0,
            },
            {
                "threshold": 200_000,
                "phase": "B_ramp_1",
                "enable_base_reward": True,
                "enable_dsr_reward": True,
                "enable_turnover_penalty": False,
                "enable_benchmark_shaping": True,
                "enable_terminal_tape_bonus": False,
                "base_reward_weight": 1.0,
                "dsr_reward_weight": 0.25,
                "turnover_penalty_weight": 0.0,
                "benchmark_shaping_weight": 0.20,
                "terminal_tape_bonus_weight": 0.0,
            },
            {
                "threshold": 240_000,
                "phase": "B_ramp_2",
                "enable_base_reward": True,
                "enable_dsr_reward": True,
                "enable_turnover_penalty": False,
                "enable_benchmark_shaping": True,
                "enable_terminal_tape_bonus": False,
                "base_reward_weight": 1.0,
                "dsr_reward_weight": 0.55,
                "turnover_penalty_weight": 0.0,
                "benchmark_shaping_weight": 0.45,
                "terminal_tape_bonus_weight": 0.0,
            },
            {
                "threshold": 280_000,
                "phase": "B_full",
                "enable_base_reward": True,
                "enable_dsr_reward": True,
                "enable_turnover_penalty": False,
                "enable_benchmark_shaping": True,
                "enable_terminal_tape_bonus": False,
                "base_reward_weight": 1.0,
                "dsr_reward_weight": 1.0,
                "turnover_penalty_weight": 0.0,
                "benchmark_shaping_weight": 0.75,
                "terminal_tape_bonus_weight": 0.0,
            },
            {
                "threshold": 375_000,
                "phase": "C_ramp_1",
                "enable_base_reward": True,
                "enable_dsr_reward": True,
                "enable_turnover_penalty": True,
                "enable_benchmark_shaping": True,
                "enable_terminal_tape_bonus": True,
                "base_reward_weight": 1.0,
                "dsr_reward_weight": 1.0,
                "turnover_penalty_weight": 0.20,
                "benchmark_shaping_weight": 0.90,
                "terminal_tape_bonus_weight": 0.20,
            },
            {
                "threshold": 410_000,
                "phase": "C_ramp_2",
                "enable_base_reward": True,
                "enable_dsr_reward": True,
                "enable_turnover_penalty": True,
                "enable_benchmark_shaping": True,
                "enable_terminal_tape_bonus": True,
                "base_reward_weight": 1.0,
                "dsr_reward_weight": 1.0,
                "turnover_penalty_weight": 0.50,
                "benchmark_shaping_weight": 1.0,
                "terminal_tape_bonus_weight": 0.50,
            },
            {
                "threshold": 445_000,
                "phase": "C_full_tape",
                "enable_base_reward": True,
                "enable_dsr_reward": True,
                "enable_turnover_penalty": True,
                "enable_benchmark_shaping": True,
                "enable_terminal_tape_bonus": True,
                "base_reward_weight": 1.0,
                "dsr_reward_weight": 1.0,
                "turnover_penalty_weight": 1.0,
                "benchmark_shaping_weight": 1.0,
                "terminal_tape_bonus_weight": 1.0,
            },
        ],
        "episode_length_curriculum_schedule": [
            {"threshold": 0, "limit": 756},
            {"threshold": 200_000, "limit": 1008},
            {"threshold": 350_000, "limit": 1500},
            {"threshold": 475_000, "limit": None},
        ],
        "episode_length_curriculum_overlap_steps": 10_000,
        "training_early_stop_warmup_steps": 250_000,
        "training_early_stop_patience_updates": 50,
    }
)
RUN18_OVERRIDES["environment_params"].update(
    {
        "stock_dim": 10,
        "num_assets": 10,
        "target_turnover": 0.35,
        "turnover_penalty_scalar": 0.00,
        "action_execution_beta": 0.55,
        "action_realization_penalty_scalar": 0.0,
    }
)


# ── Run 19: Multi-objective TAPE experts on top of the Run18 backbone ──
RUN19_OVERRIDES = copy.deepcopy(RUN18_OVERRIDES)
RUN19_OVERRIDES["agent_params"].update(
    {
        "distributional_critic_enabled": False,
        "objective_experts_enabled": True,
        "objective_expert_names": ["return", "risk", "discipline"],
        "objective_expert_adapter_dim": 128,
        "objective_expert_dropout": 0.10,
        "objective_router_hidden_dims": [64, 32],
        "objective_router_dropout": 0.05,
    }
)
RUN19_OVERRIDES["agent_params"]["ppo_params"].update(
    {
        "objective_head_aux_coef": 0.50,
        "objective_head_diversity_coef": 0.02,
        "objective_router_entropy_coef": 0.005,
    }
)
RUN19_OVERRIDES["training_params"]["reward_component_schedule"] = [
    {
        "threshold": 0,
        "phase": "A_return_only",
        "enable_base_reward": True,
        "enable_dsr_reward": False,
        "enable_turnover_penalty": False,
        "enable_benchmark_shaping": False,
        "enable_terminal_tape_bonus": False,
        "base_reward_weight": 1.0,
        "dsr_reward_weight": 0.0,
        "turnover_penalty_weight": 0.0,
        "benchmark_shaping_weight": 0.0,
        "terminal_tape_bonus_weight": 0.0,
    },
    {
        "threshold": 200_000,
        "phase": "B_ramp_1",
        "enable_base_reward": True,
        "enable_dsr_reward": True,
        "enable_turnover_penalty": False,
        "enable_benchmark_shaping": True,
        "enable_terminal_tape_bonus": False,
        "base_reward_weight": 1.0,
        "dsr_reward_weight": 0.25,
        "turnover_penalty_weight": 0.0,
        "benchmark_shaping_weight": 0.20,
        "terminal_tape_bonus_weight": 0.0,
    },
    {
        "threshold": 260_000,
        "phase": "B_ramp_2",
        "enable_base_reward": True,
        "enable_dsr_reward": True,
        "enable_turnover_penalty": False,
        "enable_benchmark_shaping": True,
        "enable_terminal_tape_bonus": False,
        "base_reward_weight": 1.0,
        "dsr_reward_weight": 0.60,
        "turnover_penalty_weight": 0.0,
        "benchmark_shaping_weight": 0.50,
        "terminal_tape_bonus_weight": 0.0,
    },
    {
        "threshold": 320_000,
        "phase": "C_ramp_1",
        "enable_base_reward": True,
        "enable_dsr_reward": True,
        "enable_turnover_penalty": True,
        "enable_benchmark_shaping": True,
        "enable_terminal_tape_bonus": True,
        "base_reward_weight": 1.0,
        "dsr_reward_weight": 1.0,
        "turnover_penalty_weight": 0.15,
        "benchmark_shaping_weight": 0.75,
        "terminal_tape_bonus_weight": 0.15,
    },
    {
        "threshold": 380_000,
        "phase": "C_ramp_2",
        "enable_base_reward": True,
        "enable_dsr_reward": True,
        "enable_turnover_penalty": True,
        "enable_benchmark_shaping": True,
        "enable_terminal_tape_bonus": True,
        "base_reward_weight": 1.0,
        "dsr_reward_weight": 1.0,
        "turnover_penalty_weight": 0.45,
        "benchmark_shaping_weight": 1.0,
        "terminal_tape_bonus_weight": 0.45,
    },
    {
        "threshold": 440_000,
        "phase": "C_full_tape",
        "enable_base_reward": True,
        "enable_dsr_reward": True,
        "enable_turnover_penalty": True,
        "enable_benchmark_shaping": True,
        "enable_terminal_tape_bonus": True,
        "base_reward_weight": 1.0,
        "dsr_reward_weight": 1.0,
        "turnover_penalty_weight": 1.0,
        "benchmark_shaping_weight": 1.0,
        "terminal_tape_bonus_weight": 1.0,
    },
]


RUN11_RELAXED_OVERRIDES = copy.deepcopy(RUN10_ALPHA_OVERRIDES)
RUN11_RELAXED_OVERRIDES.update(
    {
        "ANALYSIS_START_DATE": "2012-01-01",
    }
)
RUN11_RELAXED_OVERRIDES["agent_params"].update(
    {
        "fusion_cross_asset_mixer_enabled": True,
        "fusion_cross_asset_mixer_layers": 1,
        "fusion_cross_asset_mixer_expansion": 2.0,
        "fusion_cross_asset_mixer_dropout": 0.10,
        "recurrent_memory_enabled": True,
        "recurrent_memory_units": 64,
        "recurrent_memory_dropout": 0.1,
    }
)
RUN11_RELAXED_OVERRIDES["agent_params"]["ppo_params"].update(
    {
        "lagrangian_cvar_threshold": -0.035,
        "lagrangian_cvar_lr": 0.002,
        "lagrangian_cvar_lambda_max": 2.0,
        "lagrangian_cvar_penalty_scale": 0.75,
        "cvar_advantage_weight": 0.0,
        "alpha_diversity_coef": 0.005,
        "alpha_dispersion_coef": 0.02,
        "alpha_dispersion_target_std": 0.10,
    }
)
RUN11_RELAXED_OVERRIDES["environment_params"].update(
    {
        "target_turnover": 0.60,
        "turnover_penalty_scalar": 0.15,
        "action_realization_penalty_scalar": 0.10,
        "tape_terminal_gate_a_enabled": True,
        "tape_terminal_gate_a_sharpe_threshold": 0.0,
        "tape_terminal_gate_a_max_drawdown": 0.30,
        "drawdown_constraint": {
            "target": 0.27,
            "tolerance": -0.02,
            "penalty_coef": 0.50,
            "lambda_init": 0.05,
            "lambda_carry_decay": 0.20,
        },
    }
)
RUN11_RELAXED_OVERRIDES["training_params"].update(
    {
        "action_execution_beta_schedule": [
            {"threshold": 0, "beta": 0.50},
            {"threshold": 100_000, "beta": 0.65},
            {"threshold": 200_000, "beta": 0.80},
            {"threshold": 350_000, "beta": 1.00},
        ],
        "action_execution_beta_curriculum": {
            0: 0.50,
            100_000: 0.65,
            200_000: 0.80,
            350_000: 1.00,
        },
        "evaluation_action_execution_beta": 1.00,
        "turnover_penalty_curriculum": {
            0: 0.10,
            100_000: 0.15,
            200_000: 0.20,
            300_000: 0.25,
            400_000: 0.30,
        },
        "periodic_checkpoint_every_steps": 50_000,
        "high_watermark_checkpoint_enabled": True,
        "high_watermark_sharpe_threshold": 0.60,
        "high_watermark_max_drawdown_abs_threshold": 0.30,
        "step_sharpe_checkpoint_enabled": True,
        "step_sharpe_checkpoint_threshold": 1.15,
        "training_early_stop_dd_soft_limit_pct": 35.0,
        "training_early_stop_turnover_soft_limit_pct": 60.0,
        "training_early_stop_dd_penalty_weight": 0.25,
        "training_early_stop_turnover_penalty_weight": 0.10,
        "training_early_stop_hard_dd_limit_pct": 60.0,
        "training_early_stop_hard_dd_patience_updates": 12,
    }
)

RUN12_MIXTURE_OVERRIDES = copy.deepcopy(RUN11_RELAXED_OVERRIDES)
RUN12_MIXTURE_OVERRIDES["agent_params"].update(
    {
        "mixture_dirichlet_enabled": True,
        "mixture_dirichlet_num_components": 3,
        "mixture_dirichlet_gating_hidden_dims": [64],
        "mixture_dirichlet_component_hidden_dims": [64],
        "mixture_dirichlet_eval_mode": "top_component_mean",
    }
)
RUN12_MIXTURE_OVERRIDES["agent_params"]["ppo_params"].update(
    {
        "mixture_dirichlet_balance_coef": 0.015,
        "mixture_dirichlet_separation_coef": 0.06,
        "mixture_dirichlet_entropy_coef": 0.003,
        "mixture_component_dispersion_coef": 0.04,
        "mixture_component_target_std": 0.30,
        "mixture_component_min_distance": 0.18,
        "mixture_dirichlet_balance_schedule": [
            {"threshold": 0, "coef": 0.015},
            {"threshold": 80_000, "coef": 0.008},
            {"threshold": 160_000, "coef": 0.003},
            {"threshold": 220_000, "coef": 0.001},
        ],
        "mixture_dirichlet_entropy_schedule": [
            {"threshold": 0, "coef": 0.003},
            {"threshold": 80_000, "coef": 0.0015},
            {"threshold": 160_000, "coef": 0.0007},
            {"threshold": 220_000, "coef": 0.0002},
        ],
    }
)
RUN12_MIXTURE_OVERRIDES["environment_params"].update(
    {
        "regime_sampling_mode": "balanced_quota",
    }
)
RUN12_MIXTURE_OVERRIDES["training_params"].update(
    {
        "max_total_timesteps": 300_000,
        "timesteps_per_ppo_update_schedule": [
            {"threshold": 0, "timesteps_per_update": 1008},
            {"threshold": 100_000, "timesteps_per_update": 1512},
            {"threshold": 220_000, "timesteps_per_update": 2016},
        ],
        "batch_size_ppo_schedule": [
            {"threshold": 0, "batch_size": 252},
            {"threshold": 100_000, "batch_size": 336},
            {"threshold": 220_000, "batch_size": 504},
        ],
        "actor_lr_schedule": [
            {"threshold": 0, "lr": 3e-5},
            {"threshold": 100_000, "lr": 2e-5},
            {"threshold": 220_000, "lr": 1e-5},
        ],
        "critic_lr_schedule": [
            {"threshold": 0, "lr": 1.5e-4},
            {"threshold": 100_000, "lr": 1.2e-4},
            {"threshold": 220_000, "lr": 1.0e-4},
        ],
        "ppo_gamma_schedule": [
            {"threshold": 0, "gamma": 0.990},
            {"threshold": 100_000, "gamma": 0.995},
            {"threshold": 220_000, "gamma": 0.998},
        ],
        "ppo_gae_lambda_schedule": [
            {"threshold": 0, "gae_lambda": 0.92},
            {"threshold": 100_000, "gae_lambda": 0.95},
            {"threshold": 220_000, "gae_lambda": 0.97},
        ],
        "ppo_entropy_coef_schedule": [
            {"threshold": 0, "entropy_coef": 0.003},
            {"threshold": 100_000, "entropy_coef": 0.003},
            {"threshold": 200_000, "entropy_coef": 0.0025},
            {"threshold": 280_000, "entropy_coef": 0.0015},
        ],
        "aux_return_pred_coef_schedule": [
            {"threshold": 0, "aux_return_pred_coef": 0.35},
            {"threshold": 100_000, "aux_return_pred_coef": 0.30},
            {"threshold": 220_000, "aux_return_pred_coef": 0.25},
        ],
        "dirichlet_temperature_schedule": [
            {"threshold": 0, "temperature": 1.0},
            {"threshold": 100_000, "temperature": 0.9},
            {"threshold": 220_000, "temperature": 0.8},
        ],
        "episode_length_curriculum_schedule": [
            {"threshold": 0, "limit": 756},
            {"threshold": 60_000, "limit": 1008},
            {"threshold": 180_000, "limit": 1500},
            {"threshold": 260_000, "limit": None},
        ],
        "action_execution_beta_schedule": [
            {"threshold": 0, "beta": 0.50},
            {"threshold": 60_000, "beta": 0.65},
            {"threshold": 140_000, "beta": 0.80},
            {"threshold": 220_000, "beta": 1.00},
        ],
        "action_execution_beta_curriculum": {
            0: 0.50,
            60_000: 0.65,
            140_000: 0.80,
            220_000: 1.00,
        },
        "turnover_penalty_curriculum": {
            0: 0.10,
            60_000: 0.15,
            140_000: 0.20,
            220_000: 0.25,
            280_000: 0.30,
        },
    }
)

RUN13_MLP_OVERRIDES = copy.deepcopy(RUN12_MIXTURE_OVERRIDES)
RUN13_MLP_OVERRIDES["agent_params"].update(
    {
        "actor_critic_type": "MLP",
        "use_fusion": False,
        "use_attention": False,
        "recurrent_memory_enabled": False,
        "fusion_cross_asset_mixer_enabled": False,
        "fusion_asset_identity_enabled": False,
        "fusion_context_cross_attention_enabled": False,
        "fusion_per_asset_alpha_head": False,
        "actor_hidden_dims": [1024, 512, 256],
        "critic_hidden_dims": [1024, 512, 256],
        "mlp_dropout": 0.10,
        "dirichlet_logit_temperature": 0.80,
        "dual_head_projection_max_single_position": 0.35,
        "dual_head_projection_min_cash_position": 0.02,
    }
)
RUN13_MLP_OVERRIDES["agent_params"]["ppo_params"].update(
    {
        "risk_aux_mvo_coef": 0.0,
        "mixture_dirichlet_balance_coef": 0.005,
        "mixture_dirichlet_entropy_coef": 0.001,
        "mixture_dirichlet_balance_schedule": [
            {"threshold": 0, "coef": 0.005},
            {"threshold": 80_000, "coef": 0.003},
            {"threshold": 160_000, "coef": 0.0015},
            {"threshold": 220_000, "coef": 0.0005},
        ],
        "mixture_dirichlet_entropy_schedule": [
            {"threshold": 0, "coef": 0.001},
            {"threshold": 80_000, "coef": 0.0005},
            {"threshold": 160_000, "coef": 0.0002},
            {"threshold": 220_000, "coef": 0.0001},
        ],
    }
)
RUN13_MLP_OVERRIDES["environment_params"].update(
    {
        "outperformance_bonus_enabled": True,
        "outperformance_bonus_scalar": 8.0,
        "outperformance_bonus_mode": "signed_clipped",
        "outperformance_bonus_clip": 0.02,
        "spy_outperformance_bonus_enabled": True,
        "spy_outperformance_bonus_scalar": 5.0,
        "spy_outperformance_bonus_mode": "signed_clipped",
        "spy_outperformance_bonus_clip": 0.02,
    }
)
RUN13_MLP_OVERRIDES["training_params"].update(
    {
        "deterministic_validation_checkpointing_enabled": True,
        "deterministic_validation_checkpointing_only": True,
        "deterministic_validation_eval_every_episodes": 5,
        "deterministic_validation_mode": "mode",
        "deterministic_validation_multi_horizon_enabled": True,
        "deterministic_validation_multi_horizon_limits": [252, 504, 756, 1008],
        "deterministic_validation_multi_horizon_weights": [0.35, 0.30, 0.20, 0.15],
        "deterministic_validation_multi_horizon_dd_penalty_coef": 0.25,
        "deterministic_validation_stochastic_sanity_enabled": True,
        "deterministic_validation_stochastic_sanity_runs": 3,
        "deterministic_validation_stochastic_sanity_episode_length_limit": 252,
        "deterministic_validation_stochastic_sanity_min_mean_sharpe": 0.0,
        "deterministic_validation_stochastic_sanity_max_sharpe_std": 1.5,
        "deterministic_validation_require_spy_outperformance": True,
        "deterministic_validation_min_spy_outperformance": 0.0,
        "deterministic_validation_require_equal_weight_outperformance": True,
        "deterministic_validation_min_equal_weight_outperformance": 0.0,
        "high_watermark_checkpoint_enabled": False,
        "step_sharpe_checkpoint_enabled": False,
        "periodic_checkpoint_every_steps": 0,
        "training_early_stop_low_advantage_enabled": False,
        "dirichlet_temperature_schedule": [
            {"threshold": 0, "temperature": 0.8},
            {"threshold": 100_000, "temperature": 0.7},
            {"threshold": 220_000, "temperature": 0.6},
        ],
        "max_single_position": 35.00,
        "min_cash_position": 0.02,
    }
)


def apply_run9_alpha_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical Run9 alpha-generation training recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN9_ALPHA_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run9_alpha_config(config: dict) -> None:
    """Raise if a config expected to match the Run9 alpha recipe drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    env = config.get("environment_params", {})
    training = config.get("training_params", {})
    feature_params = config.get("feature_params", {})
    assert not bool(agent.get("regime_conditioning_enabled", False)), "regime_conditioning_enabled drifted on"
    assert bool(agent.get("distributional_critic_enabled", False)), "distributional_critic_enabled must stay on"
    assert float(ppo.get("risk_aux_mvo_coef", 0.0)) == 0.0, "risk_aux_mvo_coef must stay off"
    assert float(ppo.get("risk_aux_cvar_coef", 0.0)) == 0.0, "step-level CVaR aux must stay off"
    assert not bool(env.get("episode_cvar_enabled", False)), "episode_cvar_enabled must stay off"
    assert bool(ppo.get("lagrangian_cvar_enabled", False)), "lagrangian_cvar_enabled must stay on"
    assert not bool(agent.get("fusion_cross_asset_mixer_enabled", True)), (
        "fusion_cross_asset_mixer_enabled must stay off for the canonical alpha run"
    )
    assert bool(training.get("deterministic_validation_checkpointing_enabled", False)), (
        "deterministic validation must stay enabled for Run9"
    )
    assert not bool(training.get("high_watermark_checkpoint_enabled", True)), (
        "legacy high-watermark checkpoints must stay off"
    )
    assert bool(training.get("deterministic_validation_checkpointing_only", False)), (
        "deterministic_validation_checkpointing_only must stay enabled for Run9"
    )
    assert bool(training.get("deterministic_validation_require_spy_outperformance", False)), (
        "deterministic validation must require SPY outperformance"
    )
    assert not bool(feature_params.get("actuarial_params", {}).get("enabled", False)), (
        "Actuarial features are globally disabled and must stay off"
    )
    assert float(ppo.get("entropy_coef", 1.0)) <= 0.003, "base entropy must stay in the low-entropy regime"
    assert float(ppo.get("alpha_dispersion_coef", 0.0)) >= 0.05, "alpha_dispersion_coef drifted below the calibrated floor"
    assert float(ppo.get("aux_return_pred_coef", 0.0)) >= 0.35, "aux_return_pred_coef drifted below the calibrated floor"
    expected_turnover = copy.deepcopy(RUN9_ALPHA_OVERRIDES["training_params"]["turnover_penalty_curriculum"])
    actual_turnover = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("turnover_penalty_curriculum", {})).items()
    }
    assert actual_turnover == expected_turnover, "turnover_penalty_curriculum drifted from the canonical Run9 schedule"


def build_run9_alpha_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with feature-audit + Run9 alpha overrides applied."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run9_alpha_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run9_alpha_config(config)
    return config


def apply_run10_alpha_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical Run10 alpha-generation training recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN10_ALPHA_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run10_alpha_config(config: dict) -> None:
    """Raise if a config expected to match the Run10 alpha recipe drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    env = config.get("environment_params", {})
    training = config.get("training_params", {})
    feature_params = config.get("feature_params", {})
    assert str(config.get("TRAIN_TEST_SPLIT_DATE", "")) == str(TRAIN_TEST_SPLIT_DATE_RECENT), (
        "Run10 split date drifted from the recent-window target"
    )
    assert str(config.get("ANALYSIS_START_DATE", "")) == "2016-01-01", (
        "Run10 analysis start date drifted from the recent-window target"
    )
    assert bool(agent.get("regime_conditioning_enabled", False)), "regime_conditioning_enabled must stay on"
    assert str(agent.get("regime_conditioning_mode", "concat")).lower() == "film", "regime_conditioning_mode must be film"
    assert bool(agent.get("distributional_critic_enabled", False)), "distributional_critic_enabled must stay on"
    assert float(agent.get("dirichlet_alpha_cap", 0.0)) >= 40.0, "dirichlet_alpha_cap drifted below the large-universe floor"
    assert float(agent.get("dirichlet_exp_tanh_scale", 0.0)) >= 5.0, "dirichlet_exp_tanh_scale drifted below the large-universe floor"
    assert float(ppo.get("risk_aux_mvo_coef", 1.0)) == 0.0, "risk_aux_mvo_coef must stay off for Run17"
    assert float(ppo.get("risk_aux_cvar_coef", 0.0)) == 0.0, "step-level CVaR aux must stay off"
    assert not bool(env.get("episode_cvar_enabled", False)), "episode_cvar_enabled must stay off"
    assert bool(ppo.get("lagrangian_cvar_enabled", False)), "lagrangian_cvar_enabled must stay on"
    assert float(ppo.get("lagrangian_cvar_penalty_scale", 1.0)) == 0.0, (
        "lagrangian_cvar_penalty_scale must stay off for Run17"
    )
    assert not bool(agent.get("fusion_cross_asset_mixer_enabled", True)), (
        "fusion_cross_asset_mixer_enabled must stay off for the canonical alpha run"
    )
    assert not bool(training.get("deterministic_validation_checkpointing_enabled", True)), (
        "deterministic validation must stay disabled for Run10 compute-efficient mode"
    )
    assert bool(training.get("high_watermark_checkpoint_enabled", False)), (
        "high_watermark_checkpoint_enabled must stay on for Run10 checkpoint selection"
    )
    assert not bool(training.get("deterministic_validation_checkpointing_only", True)), (
        "deterministic_validation_checkpointing_only must stay disabled when det-validation is off"
    )
    assert int(training.get("periodic_checkpoint_every_steps", 0)) > 0, (
        "periodic checkpoints must stay enabled in Run10 compute-efficient mode"
    )
    assert bool(training.get("training_early_stop_enabled", False)), (
        "training_early_stop_enabled must stay on for Run10 compute-efficient mode"
    )
    assert float(ppo.get("entropy_coef", 1.0)) <= 0.003, "base entropy must stay in the low-entropy regime"
    assert float(ppo.get("alpha_dispersion_coef", 0.0)) >= 0.05, "alpha_dispersion_coef drifted below the calibrated floor"
    assert float(ppo.get("aux_return_pred_coef", 0.0)) >= 0.25, "aux_return_pred_coef drifted below the calibrated floor"
    assert not bool(feature_params.get("actuarial_params", {}).get("enabled", False)), (
        "Run10 actuarial features must stay disabled"
    )

    expected_turnover = copy.deepcopy(RUN10_ALPHA_OVERRIDES["training_params"]["turnover_penalty_curriculum"])
    actual_turnover = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("turnover_penalty_curriculum", {})).items()
    }
    assert actual_turnover == expected_turnover, "turnover_penalty_curriculum drifted from the canonical Run10 schedule"

    expected_beta = copy.deepcopy(RUN10_ALPHA_OVERRIDES["training_params"]["action_execution_beta_curriculum"])
    actual_beta = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("action_execution_beta_curriculum", {})).items()
    }
    assert actual_beta == expected_beta, "action_execution_beta_curriculum drifted from the canonical Run10 schedule"

    expected_entropy = copy.deepcopy(RUN10_ALPHA_OVERRIDES["training_params"]["ppo_entropy_coef_schedule"])
    actual_entropy = copy.deepcopy(training.get("ppo_entropy_coef_schedule", []))
    assert actual_entropy == expected_entropy, "ppo_entropy_coef_schedule drifted from the canonical Run10 schedule"
    expected_aux_return_coef_schedule = copy.deepcopy(
        RUN10_ALPHA_OVERRIDES["training_params"]["aux_return_pred_coef_schedule"]
    )
    actual_aux_return_coef_schedule = copy.deepcopy(training.get("aux_return_pred_coef_schedule", []))
    assert actual_aux_return_coef_schedule == expected_aux_return_coef_schedule, (
        "aux_return_pred_coef_schedule drifted from the canonical Run10 schedule"
    )
    expected_critic_schedule = copy.deepcopy(RUN10_ALPHA_OVERRIDES["training_params"]["critic_lr_schedule"])
    actual_critic_schedule = copy.deepcopy(training.get("critic_lr_schedule", []))
    assert actual_critic_schedule == expected_critic_schedule, "critic_lr_schedule drifted from the canonical Run10 schedule"


def build_run10_alpha_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with feature-audit + Run10 alpha overrides applied."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run10_alpha_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run10_alpha_config(config)
    return config


def apply_run11_relaxed_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical Run11 relaxed-risk exploration recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN11_RELAXED_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run11_relaxed_config(config: dict) -> None:
    """Raise if a config expected to match the Run11 relaxed recipe drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    env = config.get("environment_params", {})
    training = config.get("training_params", {})
    feature_params = config.get("feature_params", {})

    assert str(config.get("TRAIN_TEST_SPLIT_DATE", "")) == str(TRAIN_TEST_SPLIT_DATE_RECENT), (
        "Run11 split date drifted from the recent-window target"
    )
    assert str(config.get("ANALYSIS_START_DATE", "")) == "2012-01-01", (
        "Run11 analysis start date drifted from the 10-year training target"
    )
    assert bool(agent.get("regime_conditioning_enabled", False)), "regime_conditioning_enabled must stay on"
    assert str(agent.get("regime_conditioning_mode", "concat")).lower() == "film", "regime_conditioning_mode must be film"
    assert bool(agent.get("fusion_cross_asset_mixer_enabled", False)), (
        "fusion_cross_asset_mixer_enabled must stay on for Run11 architecture upgrade"
    )
    assert bool(agent.get("recurrent_memory_enabled", False)), (
        "recurrent_memory_enabled must stay on for the Run11 architecture upgrade"
    )
    assert bool(agent.get("distributional_critic_enabled", False)), "distributional_critic_enabled must stay on"
    assert float(ppo.get("lagrangian_cvar_penalty_scale", 999.0)) <= 0.75, (
        "lagrangian_cvar_penalty_scale drifted above the relaxed Run11 cap"
    )
    assert float(ppo.get("cvar_advantage_weight", 999.0)) == 0.0, "cvar_advantage_weight must stay off for Run11"
    assert float(env.get("target_turnover", 0.0)) >= 0.60, "target_turnover drifted below the relaxed Run11 floor"
    assert float(env.get("turnover_penalty_scalar", 999.0)) <= 0.15, (
        "turnover_penalty_scalar drifted above the relaxed Run11 cap"
    )
    assert float(env.get("action_realization_penalty_scalar", 999.0)) <= 0.10, (
        "action_realization_penalty_scalar drifted above the relaxed Run11 cap"
    )
    dd = env.get("drawdown_constraint", {}) or {}
    assert float(dd.get("target", 0.0)) >= 0.27, "drawdown target drifted below the relaxed Run11 floor"
    assert float(dd.get("penalty_coef", 999.0)) <= 0.50, "drawdown penalty coef drifted above the relaxed Run11 cap"
    assert bool(env.get("tape_terminal_gate_a_enabled", False)), "Run11 Gate A must stay enabled"
    assert float(env.get("tape_terminal_gate_a_max_drawdown", 0.0)) == 0.30, (
        "Run11 terminal Gate A max drawdown must stay aligned at 30%"
    )
    assert not bool(training.get("deterministic_validation_checkpointing_enabled", True)), (
        "deterministic validation must stay disabled for Run11 compute-efficient mode"
    )
    assert bool(training.get("high_watermark_checkpoint_enabled", False)), (
        "high_watermark_checkpoint_enabled must stay on for Run11 checkpoint selection"
    )
    assert bool(training.get("step_sharpe_checkpoint_enabled", False)), (
        "step_sharpe_checkpoint_enabled must stay on for Run11 checkpoint capture"
    )
    assert int(training.get("periodic_checkpoint_every_steps", 0)) > 0, (
        "periodic checkpoints must stay enabled for Run11"
    )
    assert not bool(feature_params.get("actuarial_params", {}).get("enabled", False)), (
        "Run11 actuarial features must stay disabled"
    )

    expected_turnover = copy.deepcopy(RUN11_RELAXED_OVERRIDES["training_params"]["turnover_penalty_curriculum"])
    actual_turnover = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("turnover_penalty_curriculum", {})).items()
    }
    assert actual_turnover == expected_turnover, "turnover_penalty_curriculum drifted from the canonical Run11 schedule"

    expected_beta = copy.deepcopy(RUN11_RELAXED_OVERRIDES["training_params"]["action_execution_beta_curriculum"])
    actual_beta = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("action_execution_beta_curriculum", {})).items()
    }
    assert actual_beta == expected_beta, "action_execution_beta_curriculum drifted from the canonical Run11 schedule"


def build_run11_relaxed_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with feature-audit + Run11 relaxed overrides applied."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run11_relaxed_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run11_relaxed_config(config)
    return config


def apply_run12_mixture_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical Run12 mixture-head exploration recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN12_MIXTURE_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run12_mixture_config(config: dict) -> None:
    """Raise if a config expected to match the Run12 mixture-head recipe drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    env = config.get("environment_params", {})
    training = config.get("training_params", {})
    feature_params = config.get("feature_params", {})
    dd = env.get("drawdown_constraint", {}) or {}

    assert str(config.get("TRAIN_TEST_SPLIT_DATE", "")) == str(TRAIN_TEST_SPLIT_DATE_RECENT), (
        "Run12 split date drifted from the recent-window target"
    )
    assert str(config.get("ANALYSIS_START_DATE", "")) == "2012-01-01", (
        "Run12 analysis start date drifted from the 10-year training target"
    )
    assert bool(agent.get("regime_conditioning_enabled", False)), "regime_conditioning_enabled must stay on"
    assert str(agent.get("regime_conditioning_mode", "concat")).lower() == "film", (
        "regime_conditioning_mode must be film"
    )
    assert bool(agent.get("fusion_cross_asset_mixer_enabled", False)), (
        "fusion_cross_asset_mixer_enabled must stay on for Run12"
    )
    assert bool(agent.get("recurrent_memory_enabled", False)), (
        "recurrent_memory_enabled must stay on for Run12"
    )
    assert bool(agent.get("distributional_critic_enabled", False)), "distributional_critic_enabled must stay on"
    assert float(ppo.get("lagrangian_cvar_penalty_scale", 999.0)) <= 0.75, (
        "lagrangian_cvar_penalty_scale drifted above the relaxed Run12 cap"
    )
    assert float(ppo.get("cvar_advantage_weight", 999.0)) == 0.0, (
        "cvar_advantage_weight must stay off for Run12"
    )
    assert float(env.get("target_turnover", 0.0)) >= 0.60, (
        "target_turnover drifted below the relaxed Run12 floor"
    )
    assert float(env.get("turnover_penalty_scalar", 999.0)) <= 0.15, (
        "turnover_penalty_scalar drifted above the relaxed Run12 cap"
    )
    assert float(env.get("action_realization_penalty_scalar", 999.0)) <= 0.10, (
        "action_realization_penalty_scalar drifted above the relaxed Run12 cap"
    )
    assert float(dd.get("target", 0.0)) >= 0.27, "drawdown target drifted below the relaxed Run12 floor"
    assert float(dd.get("penalty_coef", 999.0)) <= 0.50, (
        "drawdown penalty coef drifted above the relaxed Run12 cap"
    )
    assert bool(env.get("tape_terminal_gate_a_enabled", False)), "Run12 Gate A must stay enabled"
    assert float(env.get("tape_terminal_gate_a_max_drawdown", 0.0)) == 0.30, (
        "Run12 terminal Gate A max drawdown must stay aligned at 30%"
    )
    assert not bool(training.get("deterministic_validation_checkpointing_enabled", True)), (
        "deterministic validation must stay disabled for Run12 compute-efficient mode"
    )
    assert bool(training.get("high_watermark_checkpoint_enabled", False)), (
        "high_watermark_checkpoint_enabled must stay on for Run12 checkpoint selection"
    )
    assert bool(training.get("step_sharpe_checkpoint_enabled", False)), (
        "step_sharpe_checkpoint_enabled must stay on for Run12 checkpoint capture"
    )
    assert int(training.get("periodic_checkpoint_every_steps", 0)) > 0, (
        "periodic checkpoints must stay enabled for Run12"
    )
    assert not bool(feature_params.get("actuarial_params", {}).get("enabled", False)), (
        "Run12 actuarial features must stay disabled"
    )

    assert int(training.get("max_total_timesteps", 0)) == 300_000, (
        "Run12 max_total_timesteps must stay at 300,000"
    )
    assert bool(agent.get("mixture_dirichlet_enabled", False)), (
        "mixture_dirichlet_enabled must stay on for Run12"
    )
    assert int(agent.get("mixture_dirichlet_num_components", 0)) == 3, (
        "Run12 mixture head must keep 3 components"
    )
    assert str(agent.get("mixture_dirichlet_eval_mode", "")).lower() == "top_component_mean", (
        "Run12 mixture eval mode must stay top_component_mean"
    )
    assert float(ppo.get("mixture_dirichlet_balance_coef", 0.0)) > 0.0, (
        "Run12 mixture_dirichlet_balance_coef must stay on"
    )
    assert float(ppo.get("mixture_dirichlet_separation_coef", 0.0)) > 0.0, (
        "Run12 mixture_dirichlet_separation_coef must stay on"
    )
    assert float(ppo.get("mixture_dirichlet_entropy_coef", 0.0)) > 0.0, (
        "Run12 mixture_dirichlet_entropy_coef must stay on"
    )
    assert float(ppo.get("mixture_component_dispersion_coef", 0.0)) > 0.0, (
        "Run12 mixture_component_dispersion_coef must stay on"
    )
    assert float(ppo.get("mixture_component_target_std", 0.0)) >= 0.30, (
        "Run12 mixture_component_target_std must stay at least 0.30"
    )
    assert float(ppo.get("mixture_component_min_distance", 0.0)) >= 0.18, (
        "Run12 mixture_component_min_distance must stay at least 0.18"
    )
    assert str(env.get("regime_sampling_mode", "")).lower() == "balanced_quota", (
        "Run12 regime_sampling_mode must stay balanced_quota"
    )

    expected_turnover = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["turnover_penalty_curriculum"])
    actual_turnover = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("turnover_penalty_curriculum", {})).items()
    }
    assert actual_turnover == expected_turnover, (
        "Run12 turnover_penalty_curriculum drifted from the canonical schedule"
    )

    expected_beta = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["action_execution_beta_curriculum"])
    actual_beta = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("action_execution_beta_curriculum", {})).items()
    }
    assert actual_beta == expected_beta, (
        "Run12 action_execution_beta_curriculum drifted from the canonical schedule"
    )

    expected_rollout = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["timesteps_per_ppo_update_schedule"])
    actual_rollout = copy.deepcopy(training.get("timesteps_per_ppo_update_schedule", []))
    assert actual_rollout == expected_rollout, (
        "Run12 timesteps_per_ppo_update_schedule drifted from the canonical schedule"
    )

    expected_batch = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["batch_size_ppo_schedule"])
    actual_batch = copy.deepcopy(training.get("batch_size_ppo_schedule", []))
    assert actual_batch == expected_batch, (
        "Run12 batch_size_ppo_schedule drifted from the canonical schedule"
    )

    expected_gamma = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["ppo_gamma_schedule"])
    actual_gamma = copy.deepcopy(training.get("ppo_gamma_schedule", []))
    assert actual_gamma == expected_gamma, (
        "Run12 ppo_gamma_schedule drifted from the canonical schedule"
    )

    expected_gae = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["ppo_gae_lambda_schedule"])
    actual_gae = copy.deepcopy(training.get("ppo_gae_lambda_schedule", []))
    assert actual_gae == expected_gae, (
        "Run12 ppo_gae_lambda_schedule drifted from the canonical schedule"
    )

    expected_entropy = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["ppo_entropy_coef_schedule"])
    actual_entropy = copy.deepcopy(training.get("ppo_entropy_coef_schedule", []))
    assert actual_entropy == expected_entropy, (
        "Run12 ppo_entropy_coef_schedule drifted from the canonical schedule"
    )

    expected_aux = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["aux_return_pred_coef_schedule"])
    actual_aux = copy.deepcopy(training.get("aux_return_pred_coef_schedule", []))
    assert actual_aux == expected_aux, (
        "Run12 aux_return_pred_coef_schedule drifted from the canonical schedule"
    )

    expected_temp = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["dirichlet_temperature_schedule"])
    actual_temp = copy.deepcopy(training.get("dirichlet_temperature_schedule", []))
    assert actual_temp == expected_temp, (
        "Run12 dirichlet_temperature_schedule drifted from the canonical schedule"
    )

    expected_episode = copy.deepcopy(RUN12_MIXTURE_OVERRIDES["training_params"]["episode_length_curriculum_schedule"])
    actual_episode = copy.deepcopy(training.get("episode_length_curriculum_schedule", []))
    assert actual_episode == expected_episode, (
        "Run12 episode_length_curriculum_schedule drifted from the canonical schedule"
    )


def build_run12_mixture_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with feature-audit + Run12 mixture-head overrides applied."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run12_mixture_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run12_mixture_config(config)
    return config


def apply_run13_mlp_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical Run13 MLP ablation recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN13_MLP_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run13_mlp_config(config: dict) -> None:
    """Raise if a config expected to match the Run13 MLP ablation drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    env = config.get("environment_params", {})
    training = config.get("training_params", {})
    feature_params = config.get("feature_params", {})
    dd = env.get("drawdown_constraint", {}) or {}

    assert str(config.get("TRAIN_TEST_SPLIT_DATE", "")) == str(TRAIN_TEST_SPLIT_DATE_RECENT), (
        "Run13 split date drifted from the recent-window target"
    )
    assert str(config.get("ANALYSIS_START_DATE", "")) == "2012-01-01", (
        "Run13 analysis start date drifted from the 10-year training target"
    )
    assert str(agent.get("actor_critic_type", "")).upper() == "MLP", "Run13 must use the MLP actor-critic"
    assert not bool(agent.get("use_fusion", False)), "Run13 must keep fusion disabled"
    assert not bool(agent.get("use_attention", False)), "Run13 must keep attention disabled"
    assert not bool(agent.get("fusion_cross_asset_mixer_enabled", False)), (
        "Run13 must keep fusion_cross_asset_mixer_enabled off"
    )
    assert not bool(agent.get("recurrent_memory_enabled", False)), (
        "Run13 must keep recurrent_memory_enabled off"
    )
    assert bool(agent.get("regime_conditioning_enabled", False)), "regime_conditioning_enabled must stay on"
    assert str(agent.get("regime_conditioning_mode", "concat")).lower() == "film", (
        "regime_conditioning_mode must stay film"
    )
    assert bool(agent.get("distributional_critic_enabled", False)), "distributional_critic_enabled must stay on"
    assert bool(agent.get("mixture_dirichlet_enabled", False)), "mixture_dirichlet_enabled must stay on"
    assert int(agent.get("mixture_dirichlet_num_components", 0)) == 3, (
        "Run13 mixture head must keep 3 components"
    )
    assert str(agent.get("mixture_dirichlet_eval_mode", "")).lower() == "top_component_mean", (
        "Run13 mixture eval mode must stay top_component_mean"
    )
    assert float(agent.get("dirichlet_logit_temperature", 999.0)) <= 0.80, (
        "Run13 base dirichlet_logit_temperature drifted above the sharper conviction regime"
    )
    assert float(agent.get("mlp_dropout", 0.0)) > 0.0, "Run13 mlp_dropout must stay configured"
    assert bool(agent.get("actor_hidden_dims", [])), "Run13 actor_hidden_dims must stay configured"
    assert bool(agent.get("critic_hidden_dims", [])), "Run13 critic_hidden_dims must stay configured"
    assert float(ppo.get("lagrangian_cvar_penalty_scale", 999.0)) <= 0.75, (
        "lagrangian_cvar_penalty_scale drifted above the relaxed Run13 cap"
    )
    assert float(ppo.get("cvar_advantage_weight", 999.0)) == 0.0, (
        "cvar_advantage_weight must stay off for Run13"
    )
    assert float(ppo.get("risk_aux_mvo_coef", 999.0)) == 0.0, (
        "Run13 risk_aux_mvo_coef must stay off"
    )
    assert float(ppo.get("mixture_dirichlet_balance_coef", 0.0)) > 0.0, (
        "Run13 mixture_dirichlet_balance_coef must stay on"
    )
    assert float(ppo.get("mixture_dirichlet_balance_coef", 999.0)) <= 0.005, (
        "Run13 mixture_dirichlet_balance_coef drifted above the sharper specialization cap"
    )
    assert float(ppo.get("mixture_dirichlet_separation_coef", 0.0)) > 0.0, (
        "Run13 mixture_dirichlet_separation_coef must stay on"
    )
    assert float(ppo.get("mixture_dirichlet_entropy_coef", 999.0)) <= 0.001, (
        "Run13 mixture_dirichlet_entropy_coef drifted above the sharper specialization cap"
    )
    assert float(ppo.get("mixture_component_dispersion_coef", 0.0)) > 0.0, (
        "Run13 mixture_component_dispersion_coef must stay on"
    )
    assert float(env.get("target_turnover", 0.0)) >= 0.60, (
        "target_turnover drifted below the relaxed Run13 floor"
    )
    assert float(env.get("turnover_penalty_scalar", 999.0)) <= 0.15, (
        "turnover_penalty_scalar drifted above the relaxed Run13 cap"
    )
    assert float(env.get("action_realization_penalty_scalar", 999.0)) <= 0.10, (
        "action_realization_penalty_scalar drifted above the relaxed Run13 cap"
    )
    assert bool(env.get("outperformance_bonus_enabled", False)), (
        "Run13 must keep equal-weight benchmark shaping enabled"
    )
    assert float(env.get("outperformance_bonus_scalar", 0.0)) >= 8.0, (
        "Run13 equal-weight benchmark shaping scalar drifted below the conviction floor"
    )
    assert str(env.get("outperformance_bonus_mode", "")).lower() == "signed_clipped", (
        "Run13 equal-weight benchmark shaping must stay signed_clipped"
    )
    assert bool(env.get("spy_outperformance_bonus_enabled", False)), (
        "Run13 must keep SPY benchmark shaping enabled"
    )
    assert float(env.get("spy_outperformance_bonus_scalar", 0.0)) >= 5.0, (
        "Run13 SPY benchmark shaping scalar drifted below the conviction floor"
    )
    assert str(env.get("spy_outperformance_bonus_mode", "")).lower() == "signed_clipped", (
        "Run13 SPY benchmark shaping must stay signed_clipped"
    )
    assert float(dd.get("target", 0.0)) >= 0.27, "drawdown target drifted below the relaxed Run13 floor"
    assert float(dd.get("penalty_coef", 999.0)) <= 0.50, (
        "drawdown penalty coef drifted above the relaxed Run13 cap"
    )
    assert bool(env.get("tape_terminal_gate_a_enabled", False)), "Run13 Gate A must stay enabled"
    assert float(env.get("tape_terminal_gate_a_max_drawdown", 0.0)) == 0.30, (
        "Run13 terminal Gate A max drawdown must stay aligned at 30%"
    )
    assert str(env.get("regime_sampling_mode", "")).lower() == "balanced_quota", (
        "Run13 regime_sampling_mode must stay balanced_quota"
    )
    assert int(training.get("max_total_timesteps", 0)) == 300_000, (
        "Run13 max_total_timesteps must stay at 300,000"
    )
    assert bool(training.get("deterministic_validation_checkpointing_enabled", False)), (
        "deterministic validation must stay enabled for Run13 checkpoint selection"
    )
    assert bool(training.get("deterministic_validation_checkpointing_only", False)), (
        "Run13 must use deterministic validation as the primary checkpoint selector"
    )
    assert str(training.get("deterministic_validation_mode", "")).lower() == "mode", (
        "Run13 deterministic validation must stay in mode evaluation"
    )
    assert bool(training.get("deterministic_validation_require_spy_outperformance", False)), (
        "Run13 deterministic validation must require SPY outperformance"
    )
    assert bool(training.get("deterministic_validation_require_equal_weight_outperformance", False)), (
        "Run13 deterministic validation must require equal-weight outperformance"
    )
    assert not bool(training.get("high_watermark_checkpoint_enabled", True)), (
        "high_watermark_checkpoint_enabled must stay off for Run13 deterministic selection"
    )
    assert not bool(training.get("step_sharpe_checkpoint_enabled", True)), (
        "step_sharpe_checkpoint_enabled must stay off for Run13 deterministic selection"
    )
    assert int(training.get("periodic_checkpoint_every_steps", 1)) == 0, (
        "periodic checkpoints must stay disabled for Run13 deterministic selection"
    )
    assert not bool(training.get("training_early_stop_low_advantage_enabled", True)), (
        "Run13 must keep low-advantage early-stop disabled"
    )
    assert not bool(feature_params.get("actuarial_params", {}).get("enabled", False)), (
        "Run13 actuarial features must stay disabled"
    )
    assert float(training.get("max_single_position", 0.0)) >= 35.0, (
        "Run13 max_single_position drifted below the frontier-exploration floor"
    )
    assert float(training.get("min_cash_position", 999.0)) <= 0.02, (
        "Run13 min_cash_position drifted above the frontier-exploration cap"
    )

    expected_turnover = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["turnover_penalty_curriculum"])
    actual_turnover = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("turnover_penalty_curriculum", {})).items()
    }
    assert actual_turnover == expected_turnover, (
        "Run13 turnover_penalty_curriculum drifted from the canonical schedule"
    )

    expected_beta = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["action_execution_beta_curriculum"])
    actual_beta = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("action_execution_beta_curriculum", {})).items()
    }
    assert actual_beta == expected_beta, (
        "Run13 action_execution_beta_curriculum drifted from the canonical schedule"
    )

    expected_rollout = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["timesteps_per_ppo_update_schedule"])
    actual_rollout = copy.deepcopy(training.get("timesteps_per_ppo_update_schedule", []))
    assert actual_rollout == expected_rollout, (
        "Run13 timesteps_per_ppo_update_schedule drifted from the canonical schedule"
    )

    expected_batch = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["batch_size_ppo_schedule"])
    actual_batch = copy.deepcopy(training.get("batch_size_ppo_schedule", []))
    assert actual_batch == expected_batch, (
        "Run13 batch_size_ppo_schedule drifted from the canonical schedule"
    )

    expected_gamma = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["ppo_gamma_schedule"])
    actual_gamma = copy.deepcopy(training.get("ppo_gamma_schedule", []))
    assert actual_gamma == expected_gamma, (
        "Run13 ppo_gamma_schedule drifted from the canonical schedule"
    )

    expected_gae = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["ppo_gae_lambda_schedule"])
    actual_gae = copy.deepcopy(training.get("ppo_gae_lambda_schedule", []))
    assert actual_gae == expected_gae, (
        "Run13 ppo_gae_lambda_schedule drifted from the canonical schedule"
    )

    expected_entropy = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["ppo_entropy_coef_schedule"])
    actual_entropy = copy.deepcopy(training.get("ppo_entropy_coef_schedule", []))
    assert actual_entropy == expected_entropy, (
        "Run13 ppo_entropy_coef_schedule drifted from the canonical schedule"
    )

    expected_aux = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["aux_return_pred_coef_schedule"])
    actual_aux = copy.deepcopy(training.get("aux_return_pred_coef_schedule", []))
    assert actual_aux == expected_aux, (
        "Run13 aux_return_pred_coef_schedule drifted from the canonical schedule"
    )

    expected_temp = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["dirichlet_temperature_schedule"])
    actual_temp = copy.deepcopy(training.get("dirichlet_temperature_schedule", []))
    assert actual_temp == expected_temp, (
        "Run13 dirichlet_temperature_schedule drifted from the canonical schedule"
    )

    expected_episode = copy.deepcopy(RUN13_MLP_OVERRIDES["training_params"]["episode_length_curriculum_schedule"])
    actual_episode = copy.deepcopy(training.get("episode_length_curriculum_schedule", []))
    assert actual_episode == expected_episode, (
        "Run13 episode_length_curriculum_schedule drifted from the canonical schedule"
    )


def build_run13_mlp_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with feature-audit + Run13 MLP overrides applied."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run13_mlp_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run13_mlp_config(config)
    return config


# ── Run 17 helpers ────────────────────────────────────────────────────


def apply_run17_expanded_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical Run17 expanded-universe recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN17_EXPANDED_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run17_expanded_config(config: dict) -> None:
    """Raise if a config expected to match the Run17 expanded-universe recipe drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    env = config.get("environment_params", {})
    training = config.get("training_params", {})
    feature_params = config.get("feature_params", {})

    # ── Run17-specific assertions (universe + dates) ──
    assert str(config.get("TRAIN_TEST_SPLIT_DATE", "")) == str(TRAIN_TEST_SPLIT_DATE_COVID_STRESS), (
        "Run17 split date must be 2019-12-31 (COVID stress window)"
    )
    assert str(config.get("ANALYSIS_START_DATE", "")) == "2009-01-01", (
        "Run17 analysis start date must be 2009-01-01 for 10-year training"
    )
    assert int(config.get("NUM_ASSETS", 0)) == 20, (
        f"Run17 must have 20 assets, got {config.get('NUM_ASSETS')}"
    )
    assert len(config.get("ASSET_TICKERS", [])) == 20, (
        f"Run17 must have 20 tickers, got {len(config.get('ASSET_TICKERS', []))}"
    )

    # ── Architecture assertions (inherited from Run10) ──
    assert bool(agent.get("regime_conditioning_enabled", False)), "regime_conditioning_enabled must stay on"
    assert str(agent.get("regime_conditioning_mode", "concat")).lower() == "film", "regime_conditioning_mode must be film"
    assert bool(agent.get("distributional_critic_enabled", False)), "distributional_critic_enabled must stay on"
    assert float(ppo.get("risk_aux_mvo_coef", 1.0)) == 0.0, (
        "risk_aux_mvo_coef must stay off for Run17"
    )
    assert float(ppo.get("risk_aux_cvar_coef", 0.0)) == 0.0, "step-level CVaR aux must stay off"
    assert not bool(env.get("episode_cvar_enabled", False)), "episode_cvar_enabled must stay off"
    assert bool(ppo.get("lagrangian_cvar_enabled", False)), "lagrangian_cvar_enabled must stay on"
    assert not bool(agent.get("fusion_cross_asset_mixer_enabled", True)), (
        "fusion_cross_asset_mixer_enabled must stay off for the canonical alpha run"
    )
    assert not bool(training.get("deterministic_validation_checkpointing_enabled", True)), (
        "deterministic validation must stay disabled for compute-efficient mode"
    )
    assert bool(training.get("high_watermark_checkpoint_enabled", False)), (
        "high_watermark_checkpoint_enabled must stay on"
    )
    assert not bool(training.get("deterministic_validation_checkpointing_only", True)), (
        "deterministic_validation_checkpointing_only must stay disabled when det-validation is off"
    )
    assert int(training.get("periodic_checkpoint_every_steps", 0)) > 0, (
        "periodic checkpoints must stay enabled"
    )
    assert not bool(training.get("step_sharpe_checkpoint_enabled", True)), (
        "step_sharpe_checkpoint_enabled must stay off for Run17"
    )
    assert bool(training.get("training_early_stop_enabled", False)), (
        "training_early_stop_enabled must stay on"
    )
    assert float(ppo.get("entropy_coef", 1.0)) <= 0.0015, "base entropy must stay in the sharpened low-entropy regime"
    assert float(ppo.get("alpha_diversity_coef", 1.0)) <= 0.002, "alpha_diversity_coef drifted above the anti-collapse ceiling"
    assert float(ppo.get("alpha_dispersion_coef", 0.0)) >= 0.10, "alpha_dispersion_coef drifted below the large-universe floor"
    assert float(ppo.get("alpha_dispersion_target_std", 0.0)) >= 0.15, (
        "alpha_dispersion_target_std drifted below the large-universe floor"
    )
    assert float(ppo.get("aux_return_pred_coef", 0.0)) >= 0.25, "aux_return_pred_coef drifted below the calibrated floor"
    assert not bool(feature_params.get("actuarial_params", {}).get("enabled", False)), (
        "Run17 actuarial features must stay disabled"
    )

    # ── Curriculum schedule assertions (canonical Run17) ──
    assert float(env.get("target_turnover", 0.0)) == 0.35, "target_turnover must stay at the aligned Run17 ceiling"
    assert float(env.get("turnover_penalty_scalar", 1.0)) == 0.05, (
        "environment turnover_penalty_scalar must stay at the aligned Run17 bootstrap level"
    )
    assert float(env.get("action_execution_beta", 0.0)) == 0.55, (
        "environment action_execution_beta must stay at the aligned Run17 bootstrap value"
    )
    assert float(env.get("action_realization_penalty_scalar", 1.0)) == 0.0, (
        "action_realization_penalty_scalar must stay off for Run17"
    )
    dsr_regime = env.get("dsr_regime_scaling", {}) if isinstance(env.get("dsr_regime_scaling", {}), dict) else {}
    assert bool(dsr_regime.get("enabled", False)), "Run17 DSR regime scaling must stay enabled"
    assert float(dsr_regime.get("low_pos_mult", 0.0)) == 0.8, (
        "Run17 low-vol positive DSR multiplier must stay at 0.8"
    )
    assert float(dsr_regime.get("low_neg_mult", 0.0)) == 0.9, (
        "Run17 low-vol negative DSR multiplier must stay at 0.9"
    )
    assert float(dsr_regime.get("mid_pos_mult", 0.0)) == 1.0, (
        "Run17 mid-vol positive DSR multiplier must stay at 1.0"
    )
    assert float(dsr_regime.get("mid_neg_mult", 0.0)) == 1.0, (
        "Run17 mid-vol negative DSR multiplier must stay at 1.0"
    )
    assert float(dsr_regime.get("high_pos_mult", 0.0)) == 1.25, (
        "Run17 high-vol positive DSR multiplier must stay at 1.25"
    )
    assert float(dsr_regime.get("high_neg_mult", 0.0)) == 1.25, (
        "Run17 high-vol negative DSR multiplier must stay at 1.25"
    )
    assert bool(env.get("outperformance_bonus_enabled", False)), (
        "Run17 must keep equal-weight benchmark shaping enabled"
    )
    assert float(env.get("outperformance_bonus_scalar", 0.0)) == 6.0, (
        "Run17 equal-weight benchmark shaping scalar must stay at 6.0"
    )
    assert str(env.get("outperformance_bonus_mode", "")).lower() == "signed_clipped", (
        "Run17 equal-weight benchmark shaping must stay signed_clipped"
    )
    assert float(env.get("outperformance_bonus_clip", 0.0)) == 0.02, (
        "Run17 equal-weight benchmark shaping clip must stay at 0.02"
    )
    assert bool(env.get("spy_outperformance_bonus_enabled", False)), (
        "Run17 must keep SPY benchmark shaping enabled"
    )
    assert float(env.get("spy_outperformance_bonus_scalar", 0.0)) == 1.5, (
        "Run17 SPY benchmark shaping scalar must stay at 1.5"
    )
    assert str(env.get("spy_outperformance_bonus_mode", "")).lower() == "signed_clipped", (
        "Run17 SPY benchmark shaping must stay signed_clipped"
    )
    assert float(env.get("spy_outperformance_bonus_clip", 0.0)) == 0.01, (
        "Run17 SPY benchmark shaping clip must stay at 0.01"
    )

    expected_turnover = copy.deepcopy(RUN17_EXPANDED_OVERRIDES["training_params"]["turnover_penalty_curriculum"])
    actual_turnover = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("turnover_penalty_curriculum", {})).items()
    }
    assert actual_turnover == expected_turnover, "turnover_penalty_curriculum drifted from the canonical Run17 schedule"

    expected_beta = copy.deepcopy(RUN17_EXPANDED_OVERRIDES["training_params"]["action_execution_beta_curriculum"])
    actual_beta = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("action_execution_beta_curriculum", {})).items()
    }
    assert actual_beta == expected_beta, "action_execution_beta_curriculum drifted from the canonical Run17 schedule"
    assert float(training.get("evaluation_action_execution_beta", 0.0)) == 1.0, (
        "evaluation_action_execution_beta must stay at 1.0 for unsmoothed evaluation"
    )
    assert float(training.get("evaluation_turnover_penalty_scalar", 0.0)) == 0.40, (
        "evaluation_turnover_penalty_scalar must stay aligned with the late Run17 curriculum"
    )

    expected_entropy = copy.deepcopy(RUN17_EXPANDED_OVERRIDES["training_params"]["ppo_entropy_coef_schedule"])
    actual_entropy = copy.deepcopy(training.get("ppo_entropy_coef_schedule", []))
    assert actual_entropy == expected_entropy, "ppo_entropy_coef_schedule drifted from the canonical Run17 schedule"
    expected_reward_schedule = copy.deepcopy(RUN17_EXPANDED_OVERRIDES["training_params"]["reward_component_schedule"])
    actual_reward_schedule = copy.deepcopy(training.get("reward_component_schedule", []))
    assert actual_reward_schedule == expected_reward_schedule, (
        "reward_component_schedule drifted from the canonical Run17 schedule"
    )

    expected_aux_return_coef_schedule = copy.deepcopy(
        RUN10_ALPHA_OVERRIDES["training_params"]["aux_return_pred_coef_schedule"]
    )
    actual_aux_return_coef_schedule = copy.deepcopy(training.get("aux_return_pred_coef_schedule", []))
    assert actual_aux_return_coef_schedule == expected_aux_return_coef_schedule, (
        "aux_return_pred_coef_schedule drifted from the canonical Run10 schedule"
    )

    expected_critic_schedule = copy.deepcopy(RUN10_ALPHA_OVERRIDES["training_params"]["critic_lr_schedule"])
    actual_critic_schedule = copy.deepcopy(training.get("critic_lr_schedule", []))
    assert actual_critic_schedule == expected_critic_schedule, "critic_lr_schedule drifted from the canonical Run10 schedule"


def build_run17_expanded_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with feature-audit + Run17 expanded-universe overrides."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run17_expanded_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run17_expanded_config(config)
    return config


def apply_run17_test_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical 100k-timestep Run17 test recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN17_TEST_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run17_test_config(config: dict) -> None:
    """Raise if a config expected to match the Run17 100k test recipe drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    env = config.get("environment_params", {})
    training = config.get("training_params", {})
    feature_params = config.get("feature_params", {})

    assert str(config.get("TRAIN_TEST_SPLIT_DATE", "")) == str(TRAIN_TEST_SPLIT_DATE_COVID_STRESS), (
        "Run17_test split date must be 2019-12-31 (COVID stress window)"
    )
    assert str(config.get("ANALYSIS_START_DATE", "")) == "2009-01-01", (
        "Run17_test analysis start date must be 2009-01-01"
    )
    assert int(config.get("NUM_ASSETS", 0)) == 20, (
        f"Run17_test must start from the canonical 20-asset config, got {config.get('NUM_ASSETS')}"
    )
    assert len(config.get("ASSET_TICKERS", [])) == 20, (
        f"Run17_test must start from 20 tickers, got {len(config.get('ASSET_TICKERS', []))}"
    )
    assert int(training.get("max_total_timesteps", 0)) == _RUN17_TEST_TIMESTEPS, (
        f"Run17_test max_total_timesteps must stay at {_RUN17_TEST_TIMESTEPS}"
    )

    assert bool(agent.get("regime_conditioning_enabled", False)), "regime_conditioning_enabled must stay on"
    assert str(agent.get("regime_conditioning_mode", "concat")).lower() == "film", "regime_conditioning_mode must be film"
    assert bool(agent.get("distributional_critic_enabled", False)), "distributional_critic_enabled must stay on"
    assert float(ppo.get("risk_aux_mvo_coef", 1.0)) == 0.0, "risk_aux_mvo_coef must stay off for Run17_test"
    assert float(ppo.get("risk_aux_cvar_coef", 0.0)) == 0.0, "step-level CVaR aux must stay off"
    assert not bool(env.get("episode_cvar_enabled", False)), "episode_cvar_enabled must stay off"
    assert bool(ppo.get("lagrangian_cvar_enabled", False)), "lagrangian_cvar_enabled must stay on"
    assert not bool(agent.get("fusion_cross_asset_mixer_enabled", True)), (
        "fusion_cross_asset_mixer_enabled must stay off for the canonical alpha test"
    )
    assert not bool(training.get("deterministic_validation_checkpointing_enabled", True)), (
        "deterministic validation must stay disabled for compute-efficient test mode"
    )
    assert bool(training.get("high_watermark_checkpoint_enabled", False)), "high_watermark_checkpoint_enabled must stay on"
    assert not bool(training.get("deterministic_validation_checkpointing_only", True)), (
        "deterministic_validation_checkpointing_only must stay disabled when det-validation is off"
    )
    assert int(training.get("periodic_checkpoint_every_steps", 0)) > 0, "periodic checkpoints must stay enabled"
    assert not bool(training.get("step_sharpe_checkpoint_enabled", True)), (
        "step_sharpe_checkpoint_enabled must stay off for Run17_test"
    )
    assert bool(training.get("training_early_stop_enabled", False)), "training_early_stop_enabled must stay on"
    assert float(training.get("training_early_stop_warmup_steps", 0)) == float(_RUN17_TEST_TIMESTEPS), (
        "training_early_stop_warmup_steps must pin the 100k fixed-horizon test"
    )
    assert float(ppo.get("entropy_coef", 1.0)) <= 0.0015, "base entropy must stay in the sharpened low-entropy regime"
    assert float(ppo.get("alpha_diversity_coef", 1.0)) <= 0.002, "alpha_diversity_coef drifted above the anti-collapse ceiling"
    assert float(ppo.get("alpha_dispersion_coef", 0.0)) >= 0.10, "alpha_dispersion_coef drifted below the large-universe floor"
    assert float(ppo.get("alpha_dispersion_target_std", 0.0)) >= 0.15, (
        "alpha_dispersion_target_std drifted below the large-universe floor"
    )
    assert float(ppo.get("aux_return_pred_coef", 0.0)) >= 0.25, "aux_return_pred_coef drifted below the calibrated floor"
    assert not bool(feature_params.get("actuarial_params", {}).get("enabled", False)), (
        "Run17_test actuarial features must stay disabled"
    )

    assert float(env.get("target_turnover", 0.0)) == 0.35, "target_turnover must stay at the aligned Run17_test ceiling"
    assert float(env.get("turnover_penalty_scalar", 1.0)) == 0.05, (
        "environment turnover_penalty_scalar must stay at the aligned Run17_test bootstrap level"
    )
    assert float(env.get("action_execution_beta", 0.0)) == 0.55, (
        "environment action_execution_beta must stay at the aligned Run17_test bootstrap value"
    )
    assert float(env.get("action_realization_penalty_scalar", 1.0)) == 0.0, (
        "action_realization_penalty_scalar must stay off for Run17_test"
    )

    dsr_regime = env.get("dsr_regime_scaling", {}) if isinstance(env.get("dsr_regime_scaling", {}), dict) else {}
    assert bool(dsr_regime.get("enabled", False)), "Run17_test DSR regime scaling must stay enabled"
    assert float(dsr_regime.get("low_pos_mult", 0.0)) == 0.8
    assert float(dsr_regime.get("low_neg_mult", 0.0)) == 0.9
    assert float(dsr_regime.get("mid_pos_mult", 0.0)) == 1.0
    assert float(dsr_regime.get("mid_neg_mult", 0.0)) == 1.0
    assert float(dsr_regime.get("high_pos_mult", 0.0)) == 1.25
    assert float(dsr_regime.get("high_neg_mult", 0.0)) == 1.25
    assert bool(env.get("outperformance_bonus_enabled", False))
    assert float(env.get("outperformance_bonus_scalar", 0.0)) == 6.0
    assert str(env.get("outperformance_bonus_mode", "")).lower() == "signed_clipped"
    assert float(env.get("outperformance_bonus_clip", 0.0)) == 0.02
    assert bool(env.get("spy_outperformance_bonus_enabled", False))
    assert float(env.get("spy_outperformance_bonus_scalar", 0.0)) == 1.5
    assert str(env.get("spy_outperformance_bonus_mode", "")).lower() == "signed_clipped"
    assert float(env.get("spy_outperformance_bonus_clip", 0.0)) == 0.01

    expected_turnover = copy.deepcopy(RUN17_TEST_OVERRIDES["training_params"]["turnover_penalty_curriculum"])
    actual_turnover = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("turnover_penalty_curriculum", {})).items()
    }
    assert actual_turnover == expected_turnover, "turnover_penalty_curriculum drifted from the canonical Run17_test schedule"

    expected_beta = copy.deepcopy(RUN17_TEST_OVERRIDES["training_params"]["action_execution_beta_curriculum"])
    actual_beta = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("action_execution_beta_curriculum", {})).items()
    }
    assert actual_beta == expected_beta, "action_execution_beta_curriculum drifted from the canonical Run17_test schedule"
    assert float(training.get("evaluation_action_execution_beta", 0.0)) == 1.0
    assert float(training.get("evaluation_turnover_penalty_scalar", 0.0)) == 0.40

    for key in [
        "timesteps_per_ppo_update_schedule",
        "batch_size_ppo_schedule",
        "actor_lr_schedule",
        "critic_lr_schedule",
        "ppo_gamma_schedule",
        "ppo_gae_lambda_schedule",
        "ppo_entropy_coef_schedule",
        "aux_return_pred_coef_schedule",
        "dirichlet_temperature_schedule",
        "episode_length_curriculum_schedule",
        "reward_component_schedule",
    ]:
        expected = copy.deepcopy(RUN17_TEST_OVERRIDES["training_params"][key])
        actual = copy.deepcopy(training.get(key, []))
        assert actual == expected, f"{key} drifted from the canonical Run17_test schedule"

    assert int(training.get("episode_length_curriculum_overlap_steps", 0)) == int(
        RUN17_TEST_OVERRIDES["training_params"]["episode_length_curriculum_overlap_steps"]
    ), "episode_length_curriculum_overlap_steps drifted from the canonical Run17_test schedule"


def build_run17_test_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with the canonical 100k-timestep Run17 test overrides."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run17_test_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run17_test_config(config)
    return config


def apply_run18_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical Run18 10-asset scaled-TAPE recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN18_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run18_config(config: dict) -> None:
    """Raise if a config expected to match the canonical Run18 recipe drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    env = config.get("environment_params", {})
    training = config.get("training_params", {})
    feature_params = config.get("feature_params", {})
    feature_selection = (
        feature_params.get("feature_selection", {})
        if isinstance(feature_params.get("feature_selection", {}), dict)
        else {}
    )
    dyn_cov = (
        feature_params.get("dynamic_covariance", {})
        if isinstance(feature_params.get("dynamic_covariance", {}), dict)
        else {}
    )

    assert str(config.get("TRAIN_TEST_SPLIT_DATE", "")) == str(TRAIN_TEST_SPLIT_DATE_COVID_STRESS), (
        "Run18 split date must be 2019-12-31 (COVID stress window)"
    )
    assert str(config.get("ANALYSIS_START_DATE", "")) == "2009-01-01", (
        "Run18 analysis start date must be 2009-01-01"
    )
    assert int(config.get("NUM_ASSETS", 0)) == 10, f"Run18 must have 10 assets, got {config.get('NUM_ASSETS')}"
    assert len(config.get("ASSET_TICKERS", [])) == 10, (
        f"Run18 must have 10 tickers, got {len(config.get('ASSET_TICKERS', []))}"
    )
    assert abs(float(config.get("EQUAL_WEIGHT_CASH_ALLOCATION", 0.0)) - (1.0 / 11.0)) < 1e-12, (
        "Run18 equal-weight cash allocation must match the 10-asset universe"
    )

    assert bool(agent.get("regime_conditioning_enabled", False)), "Run18 regime_conditioning_enabled must stay on"
    assert str(agent.get("regime_conditioning_mode", "concat")).lower() == "film", (
        "Run18 regime_conditioning_mode must stay film"
    )
    assert bool(agent.get("distributional_critic_enabled", False)), "Run18 distributional critic must stay on"
    assert not bool(agent.get("fusion_cross_asset_mixer_enabled", True)), (
        "Run18 fusion_cross_asset_mixer_enabled must stay off"
    )
    assert list(agent.get("tcn_filters", [])) == [64, 96, 128], "Run18 TCN filters drifted"
    assert list(agent.get("tcn_dilations", [])) == [1, 2, 4], "Run18 TCN dilations drifted"
    assert int(agent.get("tcn_kernel_size", 0)) == 5, "Run18 TCN kernel size drifted"
    assert str(agent.get("dirichlet_alpha_activation", "")).lower() == "cross_softplus", (
        "Run18 alpha activation must stay cross_softplus"
    )
    assert float(agent.get("dirichlet_softplus_alpha_floor", 0.0)) == 0.75, (
        "Run18 softplus alpha floor drifted"
    )
    assert float(agent.get("dirichlet_softplus_alpha_scale", 0.0)) == 2.5, (
        "Run18 softplus alpha scale drifted"
    )
    assert bool(agent.get("dirichlet_cross_sectional_standardize", False)), (
        "Run18 cross-sectional alpha standardization must stay on"
    )

    assert float(ppo.get("entropy_coef", 1.0)) == 0.0007, "Run18 base entropy drifted"
    assert float(ppo.get("risk_aux_mvo_coef", 1.0)) == 0.0, "Run18 risk_aux_mvo_coef must stay off"
    assert float(ppo.get("alpha_diversity_coef", 1.0)) == 0.0, "Run18 alpha_diversity_coef must stay off"
    assert float(ppo.get("alpha_dispersion_coef", 0.0)) == 0.20, "Run18 alpha_dispersion_coef drifted"
    assert float(ppo.get("alpha_dispersion_target_std", 0.0)) == 0.20, (
        "Run18 alpha_dispersion_target_std drifted"
    )
    assert not bool(ppo.get("lagrangian_cvar_enabled", True)), "Run18 lagrangian_cvar_enabled must stay off"
    assert float(ppo.get("lagrangian_cvar_penalty_scale", 1.0)) == 0.0, (
        "Run18 lagrangian_cvar_penalty_scale must stay at 0.0"
    )

    assert int(training.get("max_total_timesteps", 0)) == 500_000, "Run18 max_total_timesteps must stay at 500k"
    assert bool(training.get("training_early_stop_enabled", False)), "Run18 early stop must stay enabled"
    assert int(training.get("training_early_stop_warmup_steps", 0)) == 250_000, (
        "Run18 early-stop warmup drifted"
    )
    assert int(training.get("training_early_stop_patience_updates", 0)) == 50, (
        "Run18 early-stop patience drifted"
    )
    assert float(training.get("evaluation_action_execution_beta", 0.0)) == 1.0, (
        "Run18 evaluation_action_execution_beta must stay at 1.0"
    )
    assert float(training.get("evaluation_turnover_penalty_scalar", 0.0)) == 0.30, (
        "Run18 evaluation_turnover_penalty_scalar drifted"
    )
    assert int(training.get("episode_length_curriculum_overlap_steps", 0)) == 10_000, (
        "Run18 episode-length overlap drifted"
    )

    assert float(env.get("target_turnover", 0.0)) == 0.35, "Run18 target_turnover drifted"
    assert float(env.get("turnover_penalty_scalar", 1.0)) == 0.0, (
        "Run18 bootstrap environment turnover scalar must stay at 0.0"
    )
    assert float(env.get("action_execution_beta", 0.0)) == 0.55, (
        "Run18 bootstrap environment beta must stay at 0.55"
    )
    assert float(env.get("action_realization_penalty_scalar", 1.0)) == 0.0, (
        "Run18 action_realization_penalty_scalar must stay off"
    )
    assert int(env.get("stock_dim", 0)) == 10, "Run18 environment stock_dim drifted"
    assert int(env.get("num_assets", 0)) == 10, "Run18 environment num_assets drifted"

    assert bool(feature_selection.get("enforce_allowlist", False)), "Run18 feature allowlist must stay enforced"
    assert not bool(feature_params.get("actuarial_params", {}).get("enabled", False)), (
        "Run18 actuarial features must stay disabled"
    )
    assert copy.deepcopy(feature_selection.get("active_features_allowlist", [])) == copy.deepcopy(
        RUN18_ACTIVE_FEATURE_ALLOWLIST
    ), "Run18 feature allowlist drifted"
    assert int(feature_selection.get("feature_audit_expected_non_actuarial_count", 0)) == len(
        RUN18_ACTIVE_FEATURE_ALLOWLIST
    ), "Run18 non-actuarial feature audit count drifted"
    assert int(feature_selection.get("feature_audit_expected_total_count", 0)) == len(
        RUN18_ACTIVE_FEATURE_ALLOWLIST
    ), "Run18 total feature audit count drifted"
    assert int(dyn_cov.get("num_eigenvalues", 0)) == 2, "Run18 dynamic covariance num_eigenvalues drifted"
    assert int(dyn_cov.get("num_loading_components", 0)) == 2, (
        "Run18 dynamic covariance num_loading_components drifted"
    )

    for key in [
        "ppo_entropy_coef_schedule",
        "action_execution_beta_schedule",
        "reward_component_schedule",
        "episode_length_curriculum_schedule",
    ]:
        expected = copy.deepcopy(RUN18_OVERRIDES["training_params"][key])
        actual = copy.deepcopy(training.get(key, []))
        assert actual == expected, f"Run18 {key} drifted from the canonical schedule"

    expected_turnover = copy.deepcopy(RUN18_OVERRIDES["training_params"]["turnover_penalty_curriculum"])
    actual_turnover = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("turnover_penalty_curriculum", {})).items()
    }
    assert actual_turnover == expected_turnover, "Run18 turnover_penalty_curriculum drifted"

    expected_beta = copy.deepcopy(RUN18_OVERRIDES["training_params"]["action_execution_beta_curriculum"])
    actual_beta = {
        int(threshold): float(value)
        for threshold, value in dict(training.get("action_execution_beta_curriculum", {})).items()
    }
    assert actual_beta == expected_beta, "Run18 action_execution_beta_curriculum drifted"


def build_run18_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with the canonical Run18 overrides applied."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run18_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run18_config(config)
    return config


def apply_run19_overrides(config: dict, overrides: dict = None) -> dict:
    """Apply the canonical Run19 multi-objective expert recipe in-place."""
    global TRAIN_TEST_SPLIT_DATE
    resolved = copy.deepcopy(RUN19_OVERRIDES if overrides is None else overrides)
    split_date = resolved.get("TRAIN_TEST_SPLIT_DATE")
    if split_date:
        TRAIN_TEST_SPLIT_DATE = split_date
        config["TRAIN_TEST_SPLIT_DATE"] = split_date
    _deep_update_config(config, resolved)
    return config


def assert_run19_config(config: dict) -> None:
    """Raise if a config expected to match the canonical Run19 recipe drifted."""
    agent = config.get("agent_params", {})
    ppo = agent.get("ppo_params", {})
    training = config.get("training_params", {})
    env = config.get("environment_params", {})
    assert int(config.get("NUM_ASSETS", 0)) == 10, "Run19 must stay on the 10-asset universe"
    assert list(agent.get("tcn_filters", [])) == [64, 96, 128], "Run19 TCN filters drifted"
    assert list(agent.get("tcn_dilations", [])) == [1, 2, 4], "Run19 TCN dilations drifted"
    assert int(agent.get("tcn_kernel_size", 0)) == 5, "Run19 TCN kernel size drifted"
    assert str(agent.get("dirichlet_alpha_activation", "")).lower() == "cross_softplus", (
        "Run19 alpha activation must stay cross_softplus"
    )
    assert float(agent.get("dirichlet_softplus_alpha_floor", 0.0)) == 0.75, (
        "Run19 softplus alpha floor drifted"
    )
    assert float(agent.get("dirichlet_softplus_alpha_scale", 0.0)) == 2.5, (
        "Run19 softplus alpha scale drifted"
    )
    assert float(env.get("target_turnover", 0.0)) == 0.35, "Run19 target_turnover drifted"
    assert bool(agent.get("objective_experts_enabled", False)), "Run19 objective experts must stay enabled"
    assert list(agent.get("objective_expert_names", [])) == ["return", "risk", "discipline"], (
        "Run19 objective_expert_names drifted"
    )
    assert int(agent.get("objective_expert_adapter_dim", 0)) == 128, (
        "Run19 objective_expert_adapter_dim drifted"
    )
    assert float(agent.get("objective_expert_dropout", 0.0)) == 0.10, (
        "Run19 objective_expert_dropout drifted"
    )
    assert list(agent.get("objective_router_hidden_dims", [])) == [64, 32], (
        "Run19 objective_router_hidden_dims drifted"
    )
    assert float(agent.get("objective_router_dropout", 0.0)) == 0.05, (
        "Run19 objective_router_dropout drifted"
    )
    assert not bool(agent.get("distributional_critic_enabled", True)), (
        "Run19 distributional critic must stay off for the first expert implementation"
    )
    assert not bool(agent.get("dual_head_enabled", False)), "Run19 dual_head must stay off"
    assert not bool(agent.get("mixture_dirichlet_enabled", False)), "Run19 mixture_dirichlet must stay off"
    assert float(ppo.get("objective_head_aux_coef", 0.0)) == 0.50, (
        "Run19 objective_head_aux_coef drifted"
    )
    assert float(ppo.get("objective_head_diversity_coef", 0.0)) == 0.02, (
        "Run19 objective_head_diversity_coef drifted"
    )
    assert float(ppo.get("objective_router_entropy_coef", 0.0)) == 0.005, (
        "Run19 objective_router_entropy_coef drifted"
    )
    expected_reward_schedule = copy.deepcopy(RUN19_OVERRIDES["training_params"]["reward_component_schedule"])
    actual_reward_schedule = copy.deepcopy(training.get("reward_component_schedule", []))
    assert actual_reward_schedule == expected_reward_schedule, "Run19 reward_component_schedule drifted"


def build_run19_config(
    phase_name: str = "phase1",
    *,
    analysis_end_date: str | None = None,
    overrides: dict | None = None,
) -> dict:
    """Return a deep-copied phase config with the canonical Run19 overrides applied."""
    config = copy.deepcopy(get_active_config(phase_name))
    enforce_feature_audit_plan(config)
    apply_run19_overrides(config, overrides=overrides)
    if analysis_end_date is not None:
        config["ANALYSIS_END_DATE"] = analysis_end_date
    assert_run19_config(config)
    return config


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
    return ['MLP', 'TCN', 'TCN_ATTENTION', 'TCN_FUSION']

def is_sequential_architecture(architecture: str) -> bool:
    """Check if architecture requires sequential (3D) input."""
    architecture_upper = architecture.upper()
    sequential_archs = ['MLP', 'TCN', 'TCN_ATTENTION', 'TCN_FUSION', 'GRU', 'RNN']
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
