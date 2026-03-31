# Run17: Expanded Universe (20 Assets, 10yr Train / 5yr Test)

## Configuration Summary

**Base**: Run10 champion config (TCN_FUSION + full TAPE reward stack)
**Changes**: Asset universe expanded 10 -> 20, data split shifted

### Asset Universe (20 + cash)

| # | Ticker | Sector | Regime Role |
|---|--------|--------|-------------|
| 1 | MSFT | Tech / Software | Growth, quality |
| 2 | AAPL | Tech / Hardware | Quality, mega-cap anchor |
| 3 | NVDA | Tech / Semis | High-beta growth, AI cycle |
| 4 | GOOGL | Tech / Advertising | Growth, different revenue model |
| 5 | AMZN | E-commerce / Cloud | Consumer + enterprise |
| 6 | JPM | Banking | Rate-cycle proxy |
| 7 | BRK-B | Conglomerate | Value investing proxy |
| 8 | V | Payments | Consumer spending proxy |
| 9 | UNH | Healthcare / MCO | Defensive growth |
| 10 | JNJ | Healthcare / Pharma | Ultra-defensive |
| 11 | PG | Consumer Staples | Low-vol defensive |
| 12 | KO | Beverages | Global defensive, dividend |
| 13 | HD | Home Improvement | Housing cycle exposure |
| 14 | CAT | Construction | Infrastructure / cyclical |
| 15 | HON | Diversified Industrial | Industrial + tech crossover |
| 16 | XOM | Oil & Gas (Major) | Energy / inflation hedge |
| 17 | COP | Oil & Gas (E&P) | Higher-beta energy |
| 18 | NEE | Utilities | Clean energy, low-beta |
| 19 | GLD | Gold ETF | Crisis / inflation hedge |
| 20 | AMT | REIT / Towers | Real estate, rate-sensitive |

Sectors: Tech(5), Financials(2), Healthcare(2), Staples(2), Industrials(2), Energy(2), Utilities(1), Gold(1), REIT(1), Payments(1)

### Data Split

| Period | Range |
|--------|-------|
| Analysis start | 2009-01-01 |
| Training | ~mid-2009 to 2019-12-31 (10 years after lookback NaN drop) |
| Testing | 2020-01-01 to present (~5 years) |

### Architecture (unchanged from Run10)

- TCN_FUSION: filters=[64,96,128,128,128], dilations=[1,2,4,8,16], kernel=5
- FiLM regime conditioning
- Distributional critic (17 quantiles)
- Per-asset alpha heads with exp_tanh activation
- Dirichlet policy (21-dim: 20 assets + cash)

### Reward Stack (unchanged from Run10)

- Base return (scaled x100)
- DSR + PBRS (dsr_scalar=2.0)
- Turnover ceiling (target=0.35, penalty=0.50)
- Terminal bonus (TAPE score, signed mode, scalar=10.0)
- Lagrangian CVaR (penalty_scale=3.0)
- Drawdown controller (target=0.15, penalty_coef=1.5)

### Key Differences from Run10

| Dimension | Run10 | Run17 |
|-----------|-------|-------|
| Assets | 10 | 20 |
| Action dims | 11 (10+cash) | 21 (20+cash) |
| Obs dims | ~554 | ~1104 |
| Train period | 2016-01 to 2021-12 | 2009-mid to 2019-12 |
| Test period | 2022-01 to 2025-08 | 2020-01 to present |
| Train years | ~6 | ~10 |
| Test includes | 2022 bear market | COVID + QE + inflation + rate hikes + AI rally |

## Training Log

[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 8

================================================================================
EXPERIMENT 6: TCN_FUSION Enhanced + TAPE Three-Component
================================================================================
Architecture: TCN + Fusion
Results root: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results
Working dir: /content/tcn_tape_vectorized_version_clean
Covariance Features: Yes
🎯 REWARD SYSTEM: TAPE (Three-Component v3)
   Profile: BalancedGrowth
   Daily: Base + DSR/PBRS + Turnover_Proximity
   Terminal: mode=signed | baseline=0.20 | scalar=10.0 (clipped ±10.0)
   Gate A: enabled (Sharpe <= 0.00 or MDD >= 25.0% -> force non-positive terminal bonus)
   Neutral Band: enabled (±0.020 around baseline)
   [CYCLE] Profile Manager: disabled (static profile only)
[RAND] Experiment Seed: 6042 (Base: 42, Offset: 6000)
[OK] Features: Enhanced (includes 2 covariance eigenvalues)
   Eigenvalues: ['Covariance_Eigenvalue_0', 'Covariance_Eigenvalue_1']
   Train shape: (55360, 67)
   Test shape: (28460, 67)
   ℹ️ Actuarial features disabled by config.

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.35, band=±0.20, scalar=0.25 -> 0.55 => 0.75 => 0.90 => 1.00)
      ↳ Schedule: 0.25@0 => 0.55@100,000 => 0.75@200,000 => 0.90@300,000 => 1.00@400,000
   ⚙️  Component 4: Execution Inertia (beta=0.35 -> 0.45 => 0.55 => 0.60, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.35@0 => 0.45@100,000 => 0.55@200,000 => 0.60@350,000
   ⚡ Parallel rollout envs: 8
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 25.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🌊 DSR Regime Scaling: ENABLED | low_mult=0.3 (vol<0.12) | mid_mult=1.0 | high_mult=1.5 (vol>0.25)
   📈 Outperformance Bonus (SPY): ENABLED | scalar=3.0 | mode=positive_only
   🔐 Lagrangian CVaR: ENABLED | threshold=-0.025 | lr=0.004 | lambda_max=5.0 | penalty_scale=3.0
   Tail-Aware Advantage: ENABLED | weight=0.1 | bottom_k=4
   Alpha Regularization: hhi_coef=0.01 | dispersion_coef=0.05 | target_std=0.07
   Risk Aux: sharpe_coef=0.0 | mvo_coef=0.002 | cvar_coef=0.0
   🧪 Aux Per-Asset Return Head: ENABLED | coef=0.35
   🔒 Dirichlet Alpha Cap: 16.0
   🔒 Drawdown dual controller (requested): target=18.00%, tolerance=-1.50% (trigger boundary ≈ 16.50%), lr=0.100, λ_init=0.50, λ_floor=0.00, λ_max=5.00, penalty_coef=1.50
   📐 Position constraints: max_single_asset=25%, min_cash=5%
   [DEBUG] Regime-balanced sampling: use_curriculum_learning=True, volatility_regime pre-existing=False
   🎲 Volatility regimes ready for sampling (computed):
      high_vol: 909 dates (32.8%)
      low_vol: 909 dates (32.8%)
      medium_vol: 950 dates (34.3%)
   🧭 Regime start buckets (train env):
      high_vol: 909 dates (32.8%)
      low_vol: 909 dates (32.8%)
      medium_vol: 950 dates (34.3%)
   [OK] Drawdown controller armed in env: target=18.00%, trigger=16.50%, λ_init=0.500, λ_floor=0.000, λ_max=5.00, penalty_coef=1.50
[OK] THREE-COMPONENT TAPE v3 Environments created:
   Training: 2768 days
   Parallel train env instances: 8
   Testing: 1423 days

🤖 Creating TCN_FUSION agent with Dirichlet distribution for Exp 6...
[OK] Agent created: PPOAgentTF
   [RAND] Dirichlet Distribution: ENABLED
   [TOOL] Actor LR schedule: 0.000030@0 => 0.000020@150,000 => 0.000010@350,000
   [TOOL] Critic LR schedule: 0.000150@0 => 0.000120@150,000 => 0.000100@350,000
   State dim: 877
   Action dim: 20
   Actor LR (configured): 3e-05
   Actor LR (active): 0.000030
   Critic LR (active): 0.000150
   🧱 TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Cross-Asset Mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DNA] State augmentation: enabled=False
   [DOWN] Distributional critic: enabled=True | num_quantiles=17
   🎛️ Dirichlet controls: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Dual-head consistency coef: 0.0
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0030
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@150,000 => 0.9980@350,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@150,000 => 0.9700@350,000
   🎯 Entropy coef schedule: 0.0030@0 => 0.0030@100,000 => 0.0025@250,000 => 0.0015@400,000
   🧪 Aux-return coef schedule: 0.3500@0 => 0.3000@150,000 => 0.2500@300,000
   🌡️ Temperature schedule: 1.0000@0 => 0.9000@150,000 => 0.8000@300,000
   📐 PPO rollout schedule: 1008@0 => 1512@150,000 => 2016@300,000
   🧺 PPO batch-size schedule: 252@0 => 336@150,000 => 504@300,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_053418_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_053418_step_diagnostics.csv

🎯 Starting THREE-COMPONENT TAPE v3 training (with curriculum)...
   Total timesteps: 500,000
   Timesteps per update: scheduled
      0+ steps: timesteps_per_update=1008
      150,000+ steps: timesteps_per_update=1512
      300,000+ steps: timesteps_per_update=2016
   Number of updates: 348
   PPO batch_size: scheduled
      0+ steps: batch_size=252
      150,000+ steps: batch_size=336
      300,000+ steps: batch_size=504
   PPO gamma schedule: 0.9900@0 => 0.9950@150,000 => 0.9980@350,000
   PPO GAE-λ schedule: 0.9200@0 => 0.9500@150,000 => 0.9700@350,000
   📚 Episode Length Curriculum:
      0+ steps: limit=756
      100,000+ steps: limit=1008
      250,000+ steps: limit=1500
      400,000+ steps: limit=full
      ↳ smooth ramp: enabled (overlap=10,000 steps)
   📚 Turnover Scalar Curriculum:
      0+ steps: scalar=0.25
      100,000+ steps: scalar=0.55
      200,000+ steps: scalar=0.75
      300,000+ steps: scalar=0.90
      400,000+ steps: scalar=1.00
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.35
      100,000+ steps: beta=0.45
      200,000+ steps: beta=0.55
      350,000+ steps: beta=0.60
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.70, MDD <= 25.0%, skip_on_det_validation=True)
   ⏹️ Training early-stop: enabled (warmup=100,000 steps, patience=25 updates, min_delta=0.010, hard_dd=45.0% x 8)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_053418_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_053418_metadata.json
[CYCLE] Update 1/348 | Step 1,008/500,000 | Episode 0 | Time: 130.3s
   📊 Metrics: Return=+5.47% | Sharpe=0.737 | DD=5.81% | Turnover=8.00%
   🎚️ Intra-Step TAPE: potential=0.3396 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.4859 | critic_loss=0.3064 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1532 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7374 | ema=0.7374 | best_ema=0.7374 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01431
[CYCLE] Update 2/348 | Step 2,016/500,000 | Episode 0 | Time: 222.5s
   📊 Metrics: Return=+3.35% | Sharpe=0.163 | DD=10.04% | Turnover=7.72%
   🎚️ Intra-Step TAPE: potential=0.2478 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2553 | critic_loss=0.2312 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1156 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1634 | ema=0.6800 | best_ema=0.6800 | no_improve=0
   🔬 Alpha Diversity: mean=13.11 | std=2.76 | range=[1.15, 16.00] | cap_hit=9.0%
   🏷️ Alpha Per-Asset  TOP: AMT=14.34 | UNH=14.27 | GLD=14.12  BOT: NVDA=12.88 | AAPL=12.83 | CAT=12.66
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0003, db=0.0002, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=1 (12.5%), low_vol=6 (75.0%), medium_vol=1 (12.5%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01491
[CYCLE] Update 3/348 | Step 3,024/500,000 | Episode 0 | Time: 315.9s
   📊 Metrics: Return=+14.00% | Sharpe=0.533 | DD=10.26% | Turnover=7.78%
   🎚️ Intra-Step TAPE: potential=0.5244 | delta_reward=+0.0022
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2309 | critic_loss=0.2065 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5328 | ema=0.6653 | best_ema=0.6653 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01415
[CYCLE] Update 4/348 | Step 4,032/500,000 | Episode 0 | Time: 407.0s
   📊 Metrics: Return=+24.93% | Sharpe=0.736 | DD=10.26% | Turnover=7.67%
   🎚️ Intra-Step TAPE: potential=0.5569 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2218 | critic_loss=0.2438 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1219 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7360 | ema=0.6723 | best_ema=0.6723 | no_improve=0
   🔬 Alpha Diversity: mean=13.71 | std=2.89 | range=[1.00, 16.00] | cap_hit=20.6%
   🏷️ Alpha Per-Asset  TOP: AMT=14.77 | MSFT=14.77 | XOM=14.63  BOT: NEE=13.79 | BRK-B=13.74 | NVDA=13.70
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0005, db=0.0003, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=1 (12.5%), low_vol=6 (75.0%), medium_vol=1 (12.5%)
[CYCLE] Update 5/348 | Step 5,040/500,000 | Episode 0 | Time: 497.3s
   📊 Metrics: Return=+40.99% | Sharpe=0.986 | DD=10.26% | Turnover=7.63%
   🎚️ Intra-Step TAPE: potential=0.7547 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2068 | critic_loss=0.2349 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1175 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9863 | ema=0.7037 | best_ema=0.7037 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p142_actor.weights.h5 (Sharpe=1.142, MDD=10.26%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp0p713_actor.weights.h5 (Sharpe=0.713, MDD=13.53%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00003_shp0p985_actor.weights.h5 (Sharpe=0.985, MDD=13.66%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00004_shp0p817_actor.weights.h5 (Sharpe=0.817, MDD=12.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00005_shp1p091_actor.weights.h5 (Sharpe=1.091, MDD=8.02%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p951_actor.weights.h5 (Sharpe=0.951, MDD=10.11%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p861_actor.weights.h5 (Sharpe=0.861, MDD=12.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp0p723_actor.weights.h5 (Sharpe=0.723, MDD=9.84%)
[CYCLE] Update 6/348 | Step 6,048/500,000 | Episode 8 | Time: 592.7s
   📊 Metrics: Return=+33.10% | Sharpe=0.723 | DD=9.84% | Turnover=8.29%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1796 | critic_loss=0.2019 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1009 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7227 | ema=0.7056 | best_ema=0.7056 | no_improve=0
   🔬 Alpha Diversity: mean=2.58 | std=0.94 | range=[1.27, 7.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.85 | MSFT=2.68 | JNJ=2.67  BOT: COP=2.22 | NEE=2.21 | NVDA=2.13
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0011, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.500) | TAPE=0.3923
   📈 Benchmark Relative: 1/N bonus=0.000 (EW ret=-0.00208) | SPY bonus=0.007 (SPY ret=-0.00362)
[CYCLE] Update 7/348 | Step 7,056/500,000 | Episode 8 | Time: 684.6s
   📊 Metrics: Return=+17.62% | Sharpe=3.138 | DD=2.86% | Turnover=23.36%
   🎚️ Intra-Step TAPE: potential=0.7141 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1710 | critic_loss=0.2524 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1262 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.1379 | ema=0.9489 | best_ema=0.9489 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.04418
[CYCLE] Update 8/348 | Step 8,064/500,000 | Episode 8 | Time: 776.5s
   📊 Metrics: Return=+11.92% | Sharpe=0.689 | DD=14.07% | Turnover=24.18%
   🎚️ Intra-Step TAPE: potential=0.2393 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1612 | critic_loss=0.2267 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1134 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6885 | ema=0.9228 | best_ema=0.9228 | no_improve=0
   🔬 Alpha Diversity: mean=1.12 | std=0.33 | range=[0.42, 3.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.18 | KO=1.17 | HD=1.12  BOT: COP=0.98 | UNH=0.97 | CAT=0.93
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0021, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03574
[CYCLE] Update 9/348 | Step 9,072/500,000 | Episode 8 | Time: 866.9s
   📊 Metrics: Return=+22.56% | Sharpe=0.794 | DD=14.07% | Turnover=24.48%
   🎚️ Intra-Step TAPE: potential=0.6786 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1586 | critic_loss=0.1965 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0983 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7936 | ema=0.9099 | best_ema=0.9099 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03265
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 8 | Time: 960.3s
   📊 Metrics: Return=+24.03% | Sharpe=0.660 | DD=14.07% | Turnover=25.15%
   🎚️ Intra-Step TAPE: potential=0.6028 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1560 | critic_loss=0.1316 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0658 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6596 | ema=0.8849 | best_ema=0.8849 | no_improve=0
   🔬 Alpha Diversity: mean=1.01 | std=0.64 | range=[0.61, 5.13] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.05 | GLD=0.93 | HD=0.92  BOT: XOM=0.82 | AMT=0.81 | NEE=0.79
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0027, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02992
[CYCLE] Update 11/348 | Step 11,088/500,000 | Episode 8 | Time: 1051.3s
   📊 Metrics: Return=+28.60% | Sharpe=0.640 | DD=14.07% | Turnover=25.56%
   🎚️ Intra-Step TAPE: potential=0.6036 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1533 | critic_loss=0.1514 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0757 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0024
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6396 | ema=0.8603 | best_ema=0.8603 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02804
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p013_actor.weights.h5 (Sharpe=1.013, MDD=15.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp0p841_actor.weights.h5 (Sharpe=0.841, MDD=9.85%)
[CYCLE] Update 12/348 | Step 12,096/500,000 | Episode 16 | Time: 1144.4s
   📊 Metrics: Return=+39.53% | Sharpe=0.564 | DD=24.15% | Turnover=25.26%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1480 | critic_loss=0.1313 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0656 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0025
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5636 | ema=0.8307 | best_ema=0.8307 | no_improve=0
   🔬 Alpha Diversity: mean=1.25 | std=0.20 | range=[0.57, 2.44] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.35 | MSFT=1.32 | KO=1.31  BOT: GLD=1.18 | NEE=1.16 | CAT=1.11
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0032, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=12 (50.0%), medium_vol=5 (20.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 12 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.035) | TAPE=0.3117
   📈 Benchmark Relative: 1/N bonus=0.000 (EW ret=0.00251) | SPY bonus=0.002 (SPY ret=0.00157)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02982
[CYCLE] Update 13/348 | Step 13,104/500,000 | Episode 16 | Time: 1237.1s
   📊 Metrics: Return=+5.77% | Sharpe=0.490 | DD=10.37% | Turnover=23.47%
   🎚️ Intra-Step TAPE: potential=0.6463 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1509 | critic_loss=0.1102 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0551 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0024
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4897 | ema=0.7966 | best_ema=0.7966 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03437
[CYCLE] Update 14/348 | Step 14,112/500,000 | Episode 16 | Time: 1329.9s
   📊 Metrics: Return=+10.30% | Sharpe=0.493 | DD=10.37% | Turnover=25.99%
   🎚️ Intra-Step TAPE: potential=0.2651 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1492 | critic_loss=0.0549 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0275 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0024
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4932 | ema=0.7662 | best_ema=0.7662 | no_improve=0
   🔬 Alpha Diversity: mean=0.83 | std=0.28 | range=[0.58, 2.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.95 | GLD=0.83 | AAPL=0.81  BOT: COP=0.74 | AMT=0.73 | NEE=0.71
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0036, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=12 (50.0%), medium_vol=5 (20.8%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02974
[CYCLE] Update 15/348 | Step 15,120/500,000 | Episode 16 | Time: 1421.6s
   📊 Metrics: Return=+14.93% | Sharpe=0.508 | DD=10.37% | Turnover=26.65%
   🎚️ Intra-Step TAPE: potential=0.5512 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1511 | critic_loss=0.1087 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0544 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5084 | ema=0.7404 | best_ema=0.7404 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02622
[CYCLE] Update 16/348 | Step 16,128/500,000 | Episode 16 | Time: 1514.5s
   📊 Metrics: Return=+24.36% | Sharpe=0.639 | DD=10.37% | Turnover=25.73%
   🎚️ Intra-Step TAPE: potential=0.4054 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1517 | critic_loss=0.0765 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0383 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6394 | ema=0.7303 | best_ema=0.7303 | no_improve=0
   🔬 Alpha Diversity: mean=1.35 | std=0.30 | range=[0.61, 3.85] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.68 | NVDA=1.62 | AAPL=1.57  BOT: JNJ=1.24 | KO=1.21 | NEE=1.10
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0038, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=12 (50.0%), medium_vol=5 (20.8%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02387
[CYCLE] Update 17/348 | Step 17,136/500,000 | Episode 16 | Time: 1606.8s
   📊 Metrics: Return=+31.63% | Sharpe=0.683 | DD=10.37% | Turnover=25.29%
   🎚️ Intra-Step TAPE: potential=0.4619 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1493 | critic_loss=0.0705 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0353 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0025
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6828 | ema=0.7256 | best_ema=0.7256 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00017_shp0p707_actor.weights.h5 (Sharpe=0.707, MDD=10.37%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00018_shp0p957_actor.weights.h5 (Sharpe=0.957, MDD=20.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00023_shp0p959_actor.weights.h5 (Sharpe=0.959, MDD=19.04%)
[CYCLE] Update 18/348 | Step 18,144/500,000 | Episode 24 | Time: 1700.4s
   📊 Metrics: Return=+20.31% | Sharpe=0.363 | DD=13.51% | Turnover=25.58%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1470 | critic_loss=0.0625 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0312 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3633 | ema=0.6894 | best_ema=0.6894 | no_improve=0
   🔬 Alpha Diversity: mean=0.94 | std=0.23 | range=[0.68, 2.35] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.09 | AAPL=1.06 | AMZN=1.04  BOT: JNJ=0.84 | PG=0.83 | NEE=0.74
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0043, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=9 (28.1%), low_vol=13 (40.6%), medium_vol=10 (31.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 18 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2775
[CYCLE] Update 19/348 | Step 19,152/500,000 | Episode 24 | Time: 1791.4s
   📊 Metrics: Return=+19.23% | Sharpe=1.240 | DD=18.56% | Turnover=26.16%
   🎚️ Intra-Step TAPE: potential=0.6350 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1455 | critic_loss=0.0757 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0379 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2403 | ema=0.7445 | best_ema=0.7445 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0008 | penalty=-0.0000 | rolling_cvar=-0.00958
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1884.7s
   📊 Metrics: Return=+44.71% | Sharpe=1.600 | DD=18.56% | Turnover=25.55%
   🎚️ Intra-Step TAPE: potential=0.6518 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1453 | critic_loss=0.0497 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0249 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6005 | ema=0.8301 | best_ema=0.8301 | no_improve=0
   🔬 Alpha Diversity: mean=1.06 | std=0.13 | range=[0.49, 1.84] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.13 | KO=1.12 | HD=1.11  BOT: BRK-B=1.01 | CAT=1.01 | NEE=0.98
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0050, db=0.0033, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=9 (28.1%), low_vol=13 (40.6%), medium_vol=10 (31.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 20 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01269
[CYCLE] Update 21/348 | Step 21,168/500,000 | Episode 24 | Time: 1978.3s
   📊 Metrics: Return=+35.60% | Sharpe=0.944 | DD=18.56% | Turnover=25.69%
   🎚️ Intra-Step TAPE: potential=0.2430 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1523 | critic_loss=0.0685 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0343 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9442 | ema=0.8415 | best_ema=0.8415 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01489
[CYCLE] Update 22/348 | Step 22,176/500,000 | Episode 24 | Time: 2071.0s
   📊 Metrics: Return=+58.77% | Sharpe=1.166 | DD=18.56% | Turnover=26.54%
   🎚️ Intra-Step TAPE: potential=0.7479 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1435 | critic_loss=0.0402 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0201 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0025
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1658 | ema=0.8739 | best_ema=0.8739 | no_improve=0
   🔬 Alpha Diversity: mean=0.85 | std=0.34 | range=[0.58, 3.18] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.86 | GLD=0.86 | KO=0.83  BOT: JPM=0.73 | COP=0.73 | CAT=0.72
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0047, db=0.0031, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=9 (28.1%), low_vol=13 (40.6%), medium_vol=10 (31.2%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01467
[CYCLE] Update 23/348 | Step 23,184/500,000 | Episode 24 | Time: 2162.9s
   📊 Metrics: Return=+52.03% | Sharpe=0.894 | DD=18.56% | Turnover=26.55%
   🎚️ Intra-Step TAPE: potential=0.2396 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1430 | critic_loss=0.0418 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0209 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0024
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8940 | ema=0.8759 | best_ema=0.8759 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01636
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp0p720_actor.weights.h5 (Sharpe=0.720, MDD=18.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00026_shp0p965_actor.weights.h5 (Sharpe=0.965, MDD=13.62%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00028_shp1p084_actor.weights.h5 (Sharpe=1.084, MDD=10.52%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00031_shp0p868_actor.weights.h5 (Sharpe=0.868, MDD=17.77%)
[CYCLE] Update 24/348 | Step 24,192/500,000 | Episode 32 | Time: 2253.5s
   📊 Metrics: Return=+18.35% | Sharpe=0.368 | DD=11.63% | Turnover=27.53%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1449 | critic_loss=0.0440 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0220 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3677 | ema=0.8251 | best_ema=0.8251 | no_improve=0
   🔬 Alpha Diversity: mean=0.93 | std=0.28 | range=[0.70, 3.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.95 | AMZN=0.93 | AAPL=0.93  BOT: BRK-B=0.84 | AMT=0.84 | NEE=0.82
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0048, db=0.0032, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (25.0%), low_vol=16 (40.0%), medium_vol=14 (35.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2792
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01716
[CYCLE] Update 25/348 | Step 25,200/500,000 | Episode 32 | Time: 2347.4s
   📊 Metrics: Return=+10.40% | Sharpe=2.560 | DD=2.09% | Turnover=26.20%
   🎚️ Intra-Step TAPE: potential=0.7325 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1425 | critic_loss=0.0459 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0230 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.5602 | ema=0.9986 | best_ema=0.9986 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01594
[CYCLE] Update 26/348 | Step 26,208/500,000 | Episode 32 | Time: 2440.7s
   📊 Metrics: Return=+21.47% | Sharpe=2.493 | DD=2.79% | Turnover=26.05%
   🎚️ Intra-Step TAPE: potential=0.7519 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1452 | critic_loss=0.0382 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0191 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0025
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4932 | ema=1.1481 | best_ema=1.1481 | no_improve=0
   🔬 Alpha Diversity: mean=0.94 | std=0.41 | range=[0.69, 3.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.01 | MSFT=0.92 | AMZN=0.89  BOT: AMT=0.82 | BRK-B=0.82 | NEE=0.80
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0047, db=0.0032, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (25.0%), low_vol=16 (40.0%), medium_vol=14 (35.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01303
[CYCLE] Update 27/348 | Step 27,216/500,000 | Episode 32 | Time: 2533.0s
   📊 Metrics: Return=+27.49% | Sharpe=1.436 | DD=9.34% | Turnover=26.48%
   🎚️ Intra-Step TAPE: potential=0.2699 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1476 | critic_loss=0.0291 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0145 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0025
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4361 | ema=1.1769 | best_ema=1.1769 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01281
[CYCLE] Update 28/348 | Step 28,224/500,000 | Episode 32 | Time: 2624.9s
   📊 Metrics: Return=+23.87% | Sharpe=0.844 | DD=9.36% | Turnover=27.19%
   🎚️ Intra-Step TAPE: potential=0.2355 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1435 | critic_loss=0.0367 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0184 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8438 | ema=1.1436 | best_ema=1.1436 | no_improve=0
   🔬 Alpha Diversity: mean=0.82 | std=0.24 | range=[0.63, 2.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.83 | AAPL=0.81 | MSFT=0.81  BOT: NEE=0.74 | GLD=0.73 | AMT=0.73
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0046, db=0.0031, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (25.0%), low_vol=16 (40.0%), medium_vol=14 (35.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 28 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 29/348 | Step 29,232/500,000 | Episode 32 | Time: 2715.9s
   📊 Metrics: Return=+33.24% | Sharpe=0.858 | DD=16.83% | Turnover=27.48%
   🎚️ Intra-Step TAPE: potential=0.2516 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1464 | critic_loss=0.0272 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0136 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8582 | ema=1.1150 | best_ema=1.1150 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00033_shp0p960_actor.weights.h5 (Sharpe=0.960, MDD=16.83%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00037_shp0p871_actor.weights.h5 (Sharpe=0.871, MDD=21.48%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 2808.6s
   📊 Metrics: Return=+29.46% | Sharpe=0.655 | DD=12.20% | Turnover=28.17%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1413 | critic_loss=0.0437 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0219 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6551 | ema=1.0690 | best_ema=1.0690 | no_improve=0
   🔬 Alpha Diversity: mean=0.98 | std=0.25 | range=[0.70, 3.13] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.08 | MSFT=1.00 | COP=0.98  BOT: PG=0.88 | AMT=0.88 | NEE=0.86
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0049, db=0.0033, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=13 (27.1%), low_vol=18 (37.5%), medium_vol=17 (35.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 30 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3572
   📈 Benchmark Relative: 1/N bonus=0.000 (EW ret=-0.00171) | SPY bonus=0.003 (SPY ret=-0.00229)
[CYCLE] Update 31/348 | Step 31,248/500,000 | Episode 40 | Time: 2899.9s
   📊 Metrics: Return=-1.22% | Sharpe=-0.160 | DD=15.14% | Turnover=23.11%
   🎚️ Intra-Step TAPE: potential=0.2434 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1430 | critic_loss=0.0306 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0153 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1603 | ema=0.9461 | best_ema=0.9461 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.04136
[CYCLE] Update 32/348 | Step 32,256/500,000 | Episode 40 | Time: 2993.5s
   📊 Metrics: Return=+15.65% | Sharpe=0.901 | DD=15.14% | Turnover=24.99%
   🎚️ Intra-Step TAPE: potential=0.7095 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1428 | critic_loss=0.0214 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0107 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9008 | ema=0.9416 | best_ema=0.9416 | no_improve=0
   🔬 Alpha Diversity: mean=0.98 | std=0.18 | range=[0.63, 2.11] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.21 | AAPL=1.01 | JPM=1.00  BOT: KO=0.91 | BRK-B=0.90 | NEE=0.88
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0059, db=0.0041, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=13 (27.1%), low_vol=18 (37.5%), medium_vol=17 (35.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 32 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03497
[CYCLE] Update 33/348 | Step 33,264/500,000 | Episode 40 | Time: 3087.7s
   📊 Metrics: Return=+18.52% | Sharpe=0.718 | DD=15.14% | Turnover=25.25%
   🎚️ Intra-Step TAPE: potential=0.2410 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1424 | critic_loss=0.0220 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0110 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7175 | ema=0.9192 | best_ema=0.9192 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03258
[CYCLE] Update 34/348 | Step 34,272/500,000 | Episode 40 | Time: 3181.7s
   📊 Metrics: Return=+22.06% | Sharpe=0.536 | DD=15.14% | Turnover=25.42%
   🎚️ Intra-Step TAPE: potential=0.5743 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1383 | critic_loss=0.0214 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0107 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5359 | ema=0.8808 | best_ema=0.8808 | no_improve=0
   🔬 Alpha Diversity: mean=1.00 | std=0.14 | range=[0.50, 1.84] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.24 | MSFT=1.05 | AMZN=1.03  BOT: NEE=0.95 | AMT=0.95 | GLD=0.86
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0059, db=0.0041, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=13 (27.1%), low_vol=18 (37.5%), medium_vol=17 (35.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 34 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03023
[CYCLE] Update 35/348 | Step 35,280/500,000 | Episode 40 | Time: 3275.6s
   📊 Metrics: Return=+26.24% | Sharpe=0.519 | DD=15.14% | Turnover=25.39%
   🎚️ Intra-Step TAPE: potential=0.2475 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1401 | critic_loss=0.0165 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5189 | ema=0.8446 | best_ema=0.8446 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02830
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00042_shp0p861_actor.weights.h5 (Sharpe=0.861, MDD=18.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00046_shp1p104_actor.weights.h5 (Sharpe=1.104, MDD=10.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00047_shp0p738_actor.weights.h5 (Sharpe=0.738, MDD=15.23%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00048_shp0p771_actor.weights.h5 (Sharpe=0.771, MDD=18.08%)
[CYCLE] Update 36/348 | Step 36,288/500,000 | Episode 48 | Time: 3367.5s
   📊 Metrics: Return=+58.78% | Sharpe=0.771 | DD=18.08% | Turnover=25.00%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1471 | critic_loss=0.0171 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0086 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7708 | ema=0.8373 | best_ema=0.8373 | no_improve=0
   🔬 Alpha Diversity: mean=1.15 | std=0.18 | range=[0.43, 1.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.29 | AAPL=1.22 | HON=1.22  BOT: AMT=1.13 | CAT=1.13 | GLD=1.02
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0060, db=0.0041, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=15 (26.8%), low_vol=22 (39.3%), medium_vol=19 (33.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 36 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.003) | TAPE=0.4068
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03018
[CYCLE] Update 37/348 | Step 37,296/500,000 | Episode 48 | Time: 3459.9s
   📊 Metrics: Return=+12.54% | Sharpe=1.874 | DD=8.01% | Turnover=26.85%
   🎚️ Intra-Step TAPE: potential=0.2594 | delta_reward=-0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1400 | critic_loss=0.0169 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0085 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8739 | ema=0.9409 | best_ema=0.9409 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0008 | penalty=-0.0000 | rolling_cvar=-0.02812
[CYCLE] Update 38/348 | Step 38,304/500,000 | Episode 48 | Time: 3552.1s
   📊 Metrics: Return=+5.24% | Sharpe=0.261 | DD=17.23% | Turnover=26.44%
   🎚️ Intra-Step TAPE: potential=0.2433 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1356 | critic_loss=0.0132 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2608 | ema=0.8729 | best_ema=0.8729 | no_improve=0
   🔬 Alpha Diversity: mean=0.94 | std=0.11 | range=[0.42, 1.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=0.99 | XOM=0.99 | JNJ=0.99  BOT: NEE=0.92 | AMT=0.91 | GLD=0.88
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0056, db=0.0038, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=15 (26.8%), low_vol=22 (39.3%), medium_vol=19 (33.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 38 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02436
[CYCLE] Update 39/348 | Step 39,312/500,000 | Episode 48 | Time: 3646.8s
   📊 Metrics: Return=+15.85% | Sharpe=0.533 | DD=17.23% | Turnover=26.45%
   🎚️ Intra-Step TAPE: potential=0.6427 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1425 | critic_loss=0.0125 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0063 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5329 | ema=0.8389 | best_ema=0.8389 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03005
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 48 | Time: 3739.5s
   📊 Metrics: Return=+15.12% | Sharpe=0.390 | DD=17.23% | Turnover=26.64%
   🎚️ Intra-Step TAPE: potential=0.3930 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1424 | critic_loss=0.0109 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3903 | ema=0.7940 | best_ema=0.7940 | no_improve=0
   🔬 Alpha Diversity: mean=0.93 | std=0.11 | range=[0.50, 1.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AAPL=0.99 | MSFT=0.98 | HD=0.98  BOT: AMZN=0.91 | AMT=0.90 | CAT=0.88
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0060, db=0.0042, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=15 (26.8%), low_vol=22 (39.3%), medium_vol=19 (33.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 40 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02744
[CYCLE] Update 41/348 | Step 41,328/500,000 | Episode 48 | Time: 3832.6s
   📊 Metrics: Return=+22.37% | Sharpe=0.472 | DD=17.23% | Turnover=26.71%
   🎚️ Intra-Step TAPE: potential=0.5811 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1414 | critic_loss=0.0100 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4719 | ema=0.7618 | best_ema=0.7618 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02550
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00050_shp0p935_actor.weights.h5 (Sharpe=0.935, MDD=11.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00054_shp0p769_actor.weights.h5 (Sharpe=0.769, MDD=9.07%)
[CYCLE] Update 42/348 | Step 42,336/500,000 | Episode 56 | Time: 3923.0s
   📊 Metrics: Return=+21.02% | Sharpe=0.352 | DD=16.13% | Turnover=26.98%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1389 | critic_loss=0.0308 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0154 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3519 | ema=0.7208 | best_ema=0.7208 | no_improve=0
   🔬 Alpha Diversity: mean=0.87 | std=0.14 | range=[0.67, 1.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.96 | NVDA=0.95 | AMZN=0.95  BOT: PG=0.81 | AMT=0.80 | NEE=0.77
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0060, db=0.0042, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (25.0%), low_vol=26 (40.6%), medium_vol=22 (34.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 42 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2715
[CYCLE] Update 43/348 | Step 43,344/500,000 | Episode 56 | Time: 4013.5s
   📊 Metrics: Return=+3.99% | Sharpe=0.677 | DD=4.54% | Turnover=27.85%
   🎚️ Intra-Step TAPE: potential=0.5201 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1402 | critic_loss=0.0164 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0082 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6766 | ema=0.7164 | best_ema=0.7164 | no_improve=0
[CYCLE] Update 44/348 | Step 44,352/500,000 | Episode 56 | Time: 4107.2s
   📊 Metrics: Return=+9.45% | Sharpe=0.761 | DD=6.59% | Turnover=28.49%
   🎚️ Intra-Step TAPE: potential=0.6713 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1385 | critic_loss=0.0191 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7610 | ema=0.7209 | best_ema=0.7209 | no_improve=0
   🔬 Alpha Diversity: mean=0.83 | std=0.10 | range=[0.68, 1.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AAPL=0.87 | JNJ=0.85 | HON=0.84  BOT: NVDA=0.80 | AMT=0.78 | CAT=0.77
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0067, db=0.0047, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (25.0%), low_vol=26 (40.6%), medium_vol=22 (34.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 44 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01381
[CYCLE] Update 45/348 | Step 45,360/500,000 | Episode 56 | Time: 4200.7s
   📊 Metrics: Return=+7.74% | Sharpe=0.333 | DD=6.59% | Turnover=28.37%
   🎚️ Intra-Step TAPE: potential=0.2555 | delta_reward=-0.0020
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1409 | critic_loss=0.0128 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0064 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3334 | ema=0.6821 | best_ema=0.6821 | no_improve=0
[CYCLE] Update 46/348 | Step 46,368/500,000 | Episode 56 | Time: 4294.3s
   📊 Metrics: Return=+12.44% | Sharpe=0.373 | DD=10.46% | Turnover=28.13%
   🎚️ Intra-Step TAPE: potential=0.7268 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1357 | critic_loss=0.0138 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0069 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3734 | ema=0.6512 | best_ema=0.6512 | no_improve=0
   🔬 Alpha Diversity: mean=0.88 | std=0.06 | range=[0.52, 1.15] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HON=0.90 | COP=0.90 | MSFT=0.90  BOT: GLD=0.85 | AMT=0.85 | CAT=0.84
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0071, db=0.0050, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (25.0%), low_vol=26 (40.6%), medium_vol=22 (34.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 46 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 47/348 | Step 47,376/500,000 | Episode 56 | Time: 4387.9s
   📊 Metrics: Return=+15.52% | Sharpe=0.358 | DD=11.81% | Turnover=27.80%
   🎚️ Intra-Step TAPE: potential=0.2526 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1418 | critic_loss=0.0166 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3580 | ema=0.6219 | best_ema=0.6219 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00058_shp0p834_actor.weights.h5 (Sharpe=0.834, MDD=11.31%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00063_shp0p717_actor.weights.h5 (Sharpe=0.717, MDD=10.21%)
[CYCLE] Update 48/348 | Step 48,384/500,000 | Episode 64 | Time: 4481.7s
   📊 Metrics: Return=+16.42% | Sharpe=0.313 | DD=12.51% | Turnover=27.66%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1384 | critic_loss=0.0182 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0091 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3126 | ema=0.5910 | best_ema=0.5910 | no_improve=0
   🔬 Alpha Diversity: mean=1.11 | std=0.11 | range=[0.70, 1.93] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.18 | MSFT=1.17 | HON=1.11  BOT: CAT=1.07 | AMT=1.06 | NEE=1.03
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0071, db=0.0050, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (26.4%), low_vol=31 (43.1%), medium_vol=22 (30.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 48 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2699
[CYCLE] Update 49/348 | Step 49,392/500,000 | Episode 64 | Time: 4575.3s
   📊 Metrics: Return=+7.57% | Sharpe=1.381 | DD=7.18% | Turnover=24.54%
   🎚️ Intra-Step TAPE: potential=0.4672 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1394 | critic_loss=0.0250 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3812 | ema=0.6700 | best_ema=0.6700 | no_improve=0
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 4668.5s
   📊 Metrics: Return=+6.21% | Sharpe=0.427 | DD=7.18% | Turnover=24.39%
   🎚️ Intra-Step TAPE: potential=0.2532 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1424 | critic_loss=0.0165 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4267 | ema=0.6457 | best_ema=0.6457 | no_improve=0
   🔬 Alpha Diversity: mean=1.10 | std=0.20 | range=[0.88, 2.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.31 | MSFT=1.11 | COP=1.09  BOT: AMT=1.03 | BRK-B=1.03 | NEE=1.01
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0068, db=0.0048, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (26.4%), low_vol=31 (43.1%), medium_vol=22 (30.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 50 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 51/348 | Step 51,408/500,000 | Episode 64 | Time: 4761.0s
   📊 Metrics: Return=+8.44% | Sharpe=0.337 | DD=11.20% | Turnover=25.07%
   🎚️ Intra-Step TAPE: potential=0.7246 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1417 | critic_loss=0.0109 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0055 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3365 | ema=0.6148 | best_ema=0.6148 | no_improve=0
[CYCLE] Update 52/348 | Step 52,416/500,000 | Episode 64 | Time: 4854.9s
   📊 Metrics: Return=+11.47% | Sharpe=0.330 | DD=12.05% | Turnover=25.89%
   🎚️ Intra-Step TAPE: potential=0.6951 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1368 | critic_loss=0.0161 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0081 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3295 | ema=0.5862 | best_ema=0.5862 | no_improve=0
   🔬 Alpha Diversity: mean=0.98 | std=0.18 | range=[0.73, 2.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.19 | COP=1.01 | MSFT=0.99  BOT: AMT=0.91 | JNJ=0.91 | NEE=0.87
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0066, db=0.0047, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (26.4%), low_vol=31 (43.1%), medium_vol=22 (30.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 52 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 53/348 | Step 53,424/500,000 | Episode 64 | Time: 4947.3s
   📊 Metrics: Return=+20.18% | Sharpe=0.488 | DD=12.05% | Turnover=25.97%
   🎚️ Intra-Step TAPE: potential=0.5649 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1373 | critic_loss=0.0129 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0065 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4875 | ema=0.5764 | best_ema=0.5764 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00065_shp0p752_actor.weights.h5 (Sharpe=0.752, MDD=12.05%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00066_shp0p857_actor.weights.h5 (Sharpe=0.857, MDD=19.62%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00067_shp0p797_actor.weights.h5 (Sharpe=0.797, MDD=18.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00068_shp0p775_actor.weights.h5 (Sharpe=0.775, MDD=18.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00072_shp1p057_actor.weights.h5 (Sharpe=1.057, MDD=10.91%)
[CYCLE] Update 54/348 | Step 54,432/500,000 | Episode 72 | Time: 5040.8s
   📊 Metrics: Return=+50.67% | Sharpe=1.057 | DD=10.91% | Turnover=26.09%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1420 | critic_loss=0.0201 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0101 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0572 | ema=0.6244 | best_ema=0.6244 | no_improve=0
   🔬 Alpha Diversity: mean=1.02 | std=0.12 | range=[0.46, 1.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.28 | AAPL=1.10 | MSFT=1.07  BOT: PG=0.98 | GLD=0.98 | NEE=0.97
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0075, db=0.0053, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=33 (41.2%), medium_vol=23 (28.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 54 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5319
[CYCLE] Update 55/348 | Step 55,440/500,000 | Episode 72 | Time: 5132.4s
   📊 Metrics: Return=+16.93% | Sharpe=2.643 | DD=5.41% | Turnover=26.85%
   🎚️ Intra-Step TAPE: potential=0.5269 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1429 | critic_loss=0.0150 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.6432 | ema=0.8263 | best_ema=0.8263 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01835
[CYCLE] Update 56/348 | Step 56,448/500,000 | Episode 72 | Time: 5224.4s
   📊 Metrics: Return=+24.85% | Sharpe=2.042 | DD=5.41% | Turnover=26.83%
   🎚️ Intra-Step TAPE: potential=0.7459 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1383 | critic_loss=0.0122 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0061 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.0423 | ema=0.9479 | best_ema=0.9479 | no_improve=0
   🔬 Alpha Diversity: mean=0.86 | std=0.11 | range=[0.69, 1.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.00 | GLD=0.93 | AMZN=0.92  BOT: PG=0.80 | JNJ=0.80 | NEE=0.77
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0072, db=0.0052, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=33 (41.2%), medium_vol=23 (28.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 56 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 57/348 | Step 57,456/500,000 | Episode 72 | Time: 5317.7s
   📊 Metrics: Return=+36.93% | Sharpe=2.092 | DD=5.41% | Turnover=27.30%
   🎚️ Intra-Step TAPE: potential=0.5803 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1430 | critic_loss=0.0082 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0041 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.0920 | ema=1.0623 | best_ema=1.0623 | no_improve=0
[CYCLE] Update 58/348 | Step 58,464/500,000 | Episode 72 | Time: 5409.3s
   📊 Metrics: Return=+48.14% | Sharpe=1.839 | DD=9.44% | Turnover=27.74%
   🎚️ Intra-Step TAPE: potential=0.2328 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1371 | critic_loss=0.0098 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0049 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8386 | ema=1.1399 | best_ema=1.1399 | no_improve=0
   🔬 Alpha Diversity: mean=0.82 | std=0.11 | range=[0.68, 1.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.94 | GLD=0.85 | MSFT=0.83  BOT: BRK-B=0.76 | JNJ=0.76 | NEE=0.73
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0083, db=0.0060, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=33 (41.2%), medium_vol=23 (28.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 58 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01277
[CYCLE] Update 59/348 | Step 59,472/500,000 | Episode 72 | Time: 5502.7s
   📊 Metrics: Return=+56.19% | Sharpe=1.567 | DD=9.44% | Turnover=27.97%
   🎚️ Intra-Step TAPE: potential=0.5225 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1421 | critic_loss=0.0090 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5673 | ema=1.1827 | best_ema=1.1827 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp0p971_actor.weights.h5 (Sharpe=0.971, MDD=17.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00077_shp1p068_actor.weights.h5 (Sharpe=1.068, MDD=16.28%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00078_shp0p853_actor.weights.h5 (Sharpe=0.853, MDD=17.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00080_shp0p842_actor.weights.h5 (Sharpe=0.842, MDD=18.13%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 5597.4s
   📊 Metrics: Return=+41.69% | Sharpe=0.842 | DD=18.13% | Turnover=27.93%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1397 | critic_loss=0.0289 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0144 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8419 | ema=1.1486 | best_ema=1.1486 | no_improve=0
   🔬 Alpha Diversity: mean=0.88 | std=0.08 | range=[0.67, 1.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.95 | MSFT=0.91 | GLD=0.90  BOT: GOOGL=0.85 | XOM=0.85 | NEE=0.83
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0071, db=0.0052, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=37 (42.0%), medium_vol=25 (28.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 60 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.002) | TAPE=0.4284
[CYCLE] Update 61/348 | Step 61,488/500,000 | Episode 80 | Time: 5687.7s
   📊 Metrics: Return=+7.43% | Sharpe=0.797 | DD=11.02% | Turnover=26.83%
   🎚️ Intra-Step TAPE: potential=0.7475 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1392 | critic_loss=0.0131 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0065 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7971 | ema=1.1135 | best_ema=1.1135 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01394
[CYCLE] Update 62/348 | Step 62,496/500,000 | Episode 80 | Time: 5781.4s
   📊 Metrics: Return=+13.25% | Sharpe=0.788 | DD=11.02% | Turnover=27.05%
   🎚️ Intra-Step TAPE: potential=0.2306 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1400 | critic_loss=0.0158 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0079 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7880 | ema=1.0809 | best_ema=1.0809 | no_improve=0
   🔬 Alpha Diversity: mean=0.93 | std=0.13 | range=[0.72, 1.95] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=0.96 | MSFT=0.95 | NVDA=0.94  BOT: AMT=0.89 | BRK-B=0.88 | NEE=0.87
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0085, db=0.0062, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=37 (42.0%), medium_vol=25 (28.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 62 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01540
[CYCLE] Update 63/348 | Step 63,504/500,000 | Episode 80 | Time: 5875.5s
   📊 Metrics: Return=+10.13% | Sharpe=0.336 | DD=16.34% | Turnover=26.94%
   🎚️ Intra-Step TAPE: potential=0.5435 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1406 | critic_loss=0.0106 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0053 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3358 | ema=1.0064 | best_ema=1.0064 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01553
[CYCLE] Update 64/348 | Step 64,512/500,000 | Episode 80 | Time: 5966.4s
   📊 Metrics: Return=+14.07% | Sharpe=0.353 | DD=16.34% | Turnover=27.86%
   🎚️ Intra-Step TAPE: potential=0.2442 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1408 | critic_loss=0.0065 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3532 | ema=0.9411 | best_ema=0.9411 | no_improve=0
   🔬 Alpha Diversity: mean=0.70 | std=0.10 | range=[0.58, 1.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AAPL=0.72 | GLD=0.72 | COP=0.72  BOT: BRK-B=0.67 | AMT=0.66 | NEE=0.65
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0076, db=0.0055, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=37 (42.0%), medium_vol=25 (28.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 64 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 65/348 | Step 65,520/500,000 | Episode 80 | Time: 6061.1s
   📊 Metrics: Return=+15.98% | Sharpe=0.323 | DD=16.34% | Turnover=28.24%
   🎚️ Intra-Step TAPE: potential=0.2413 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1377 | critic_loss=0.0089 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3234 | ema=0.8793 | best_ema=0.8793 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00087_shp0p720_actor.weights.h5 (Sharpe=0.720, MDD=13.24%)
[CYCLE] Update 66/348 | Step 66,528/500,000 | Episode 88 | Time: 6152.4s
   📊 Metrics: Return=+22.36% | Sharpe=0.455 | DD=10.47% | Turnover=29.00%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1384 | critic_loss=0.0241 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0121 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4548 | ema=0.8369 | best_ema=0.8369 | no_improve=0
   🔬 Alpha Diversity: mean=0.79 | std=0.13 | range=[0.65, 1.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.81 | NVDA=0.81 | AAPL=0.80  BOT: BRK-B=0.74 | CAT=0.74 | XOM=0.74
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0088, db=0.0064, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=29 (30.2%), low_vol=41 (42.7%), medium_vol=26 (27.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 66 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2949
   📈 Benchmark Relative: 1/N bonus=0.000 (EW ret=-0.00170) | SPY bonus=0.002 (SPY ret=-0.00278)
[CYCLE] Update 67/348 | Step 67,536/500,000 | Episode 88 | Time: 6243.9s
   📊 Metrics: Return=+5.10% | Sharpe=0.746 | DD=8.66% | Turnover=28.97%
   🎚️ Intra-Step TAPE: potential=0.2458 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1372 | critic_loss=0.0201 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0101 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7459 | ema=0.8278 | best_ema=0.8278 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01301
[CYCLE] Update 68/348 | Step 68,544/500,000 | Episode 88 | Time: 6336.5s
   📊 Metrics: Return=+11.97% | Sharpe=0.873 | DD=8.66% | Turnover=27.60%
   🎚️ Intra-Step TAPE: potential=0.2340 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1392 | critic_loss=0.0101 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0051 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8729 | ema=0.8323 | best_ema=0.8323 | no_improve=0
   🔬 Alpha Diversity: mean=1.05 | std=0.12 | range=[0.63, 1.91] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.08 | GLD=1.08 | JNJ=1.07  BOT: NVDA=1.01 | BRK-B=1.01 | CAT=1.01
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0088, db=0.0065, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=29 (30.2%), low_vol=41 (42.7%), medium_vol=26 (27.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 68 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 69/348 | Step 69,552/500,000 | Episode 88 | Time: 6429.1s
   📊 Metrics: Return=+24.61% | Sharpe=1.190 | DD=8.66% | Turnover=27.14%
   🎚️ Intra-Step TAPE: potential=0.6561 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1345 | critic_loss=0.0111 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0055 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1899 | ema=0.8680 | best_ema=0.8680 | no_improve=0
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 88 | Time: 6520.9s
   📊 Metrics: Return=+30.44% | Sharpe=1.102 | DD=8.66% | Turnover=27.05%
   🎚️ Intra-Step TAPE: potential=0.5404 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1384 | critic_loss=0.0049 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1018 | ema=0.8914 | best_ema=0.8914 | no_improve=0
   🔬 Alpha Diversity: mean=0.92 | std=0.18 | range=[0.72, 2.28] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.93 | HD=0.93 | MSFT=0.91  BOT: COP=0.85 | NVDA=0.85 | AMZN=0.85
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0089, db=0.0065, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=29 (30.2%), low_vol=41 (42.7%), medium_vol=26 (27.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 70 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 71/348 | Step 71,568/500,000 | Episode 88 | Time: 6612.5s
   📊 Metrics: Return=+41.60% | Sharpe=1.197 | DD=8.66% | Turnover=27.36%
   🎚️ Intra-Step TAPE: potential=0.5802 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1365 | critic_loss=0.0055 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0028 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1967 | ema=0.9219 | best_ema=0.9219 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp1p052_actor.weights.h5 (Sharpe=1.052, MDD=8.66%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00091_shp0p942_actor.weights.h5 (Sharpe=0.942, MDD=10.24%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00092_shp0p787_actor.weights.h5 (Sharpe=0.787, MDD=9.30%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00094_shp0p705_actor.weights.h5 (Sharpe=0.705, MDD=13.48%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00095_shp1p008_actor.weights.h5 (Sharpe=1.008, MDD=11.13%)
[CYCLE] Update 72/348 | Step 72,576/500,000 | Episode 96 | Time: 6704.9s
   📊 Metrics: Return=+26.81% | Sharpe=0.562 | DD=10.75% | Turnover=27.50%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1362 | critic_loss=0.0164 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0082 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5618 | ema=0.8859 | best_ema=0.8859 | no_improve=0
   🔬 Alpha Diversity: mean=0.77 | std=0.17 | range=[0.62, 2.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.78 | HD=0.77 | KO=0.76  BOT: CAT=0.71 | AMZN=0.69 | NVDA=0.68
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0092, db=0.0067, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (28.8%), low_vol=47 (45.2%), medium_vol=27 (26.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 72 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3261
[CYCLE] Update 73/348 | Step 73,584/500,000 | Episode 96 | Time: 6796.5s
   📊 Metrics: Return=+12.49% | Sharpe=3.490 | DD=1.39% | Turnover=28.45%
   🎚️ Intra-Step TAPE: potential=0.7358 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1368 | critic_loss=0.0132 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.4895 | ema=1.1463 | best_ema=1.1463 | no_improve=0
[CYCLE] Update 74/348 | Step 74,592/500,000 | Episode 96 | Time: 6886.8s
   📊 Metrics: Return=+22.37% | Sharpe=2.834 | DD=2.40% | Turnover=27.98%
   🎚️ Intra-Step TAPE: potential=0.7481 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1389 | critic_loss=0.0064 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0032 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.8343 | ema=1.3151 | best_ema=1.3151 | no_improve=0
   🔬 Alpha Diversity: mean=0.95 | std=0.09 | range=[0.66, 1.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.02 | GLD=1.00 | MSFT=0.99  BOT: COP=0.89 | CAT=0.89 | NVDA=0.89
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0096, db=0.0071, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (28.8%), low_vol=47 (45.2%), medium_vol=27 (26.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 74 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 75/348 | Step 75,600/500,000 | Episode 96 | Time: 6980.5s
   📊 Metrics: Return=+29.44% | Sharpe=1.526 | DD=10.01% | Turnover=27.56%
   🎚️ Intra-Step TAPE: potential=0.3447 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1382 | critic_loss=0.0080 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5261 | ema=1.3362 | best_ema=1.3362 | no_improve=0
[CYCLE] Update 76/348 | Step 76,608/500,000 | Episode 96 | Time: 7071.8s
   📊 Metrics: Return=+27.38% | Sharpe=0.947 | DD=10.45% | Turnover=27.43%
   🎚️ Intra-Step TAPE: potential=0.2344 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1372 | critic_loss=0.0067 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9467 | ema=1.2972 | best_ema=1.2972 | no_improve=0
   🔬 Alpha Diversity: mean=0.92 | std=0.08 | range=[0.63, 1.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.99 | HD=0.95 | MSFT=0.95  BOT: NEE=0.90 | JPM=0.90 | BRK-B=0.89
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0099, db=0.0072, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (28.8%), low_vol=47 (45.2%), medium_vol=27 (26.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 76 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 77/348 | Step 77,616/500,000 | Episode 96 | Time: 7166.1s
   📊 Metrics: Return=+29.73% | Sharpe=0.746 | DD=18.27% | Turnover=27.40%
   🎚️ Intra-Step TAPE: potential=0.3033 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1395 | critic_loss=0.0059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7464 | ema=1.2421 | best_ema=1.2421 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00097_shp0p779_actor.weights.h5 (Sharpe=0.779, MDD=18.27%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00098_shp0p990_actor.weights.h5 (Sharpe=0.990, MDD=11.37%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00101_shp0p734_actor.weights.h5 (Sharpe=0.734, MDD=17.65%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00102_shp0p747_actor.weights.h5 (Sharpe=0.747, MDD=19.05%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00103_shp0p757_actor.weights.h5 (Sharpe=0.757, MDD=11.08%)
[CYCLE] Update 78/348 | Step 78,624/500,000 | Episode 104 | Time: 7260.7s
   📊 Metrics: Return=+14.66% | Sharpe=0.288 | DD=11.28% | Turnover=27.41%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1357 | critic_loss=0.0108 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2881 | ema=1.1467 | best_ema=1.1467 | no_improve=0
   🔬 Alpha Diversity: mean=0.92 | std=0.10 | range=[0.58, 1.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.10 | GLD=0.98 | AAPL=0.97  BOT: JPM=0.88 | XOM=0.88 | NEE=0.86
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0097, db=0.0070, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=33 (29.5%), low_vol=48 (42.9%), medium_vol=31 (27.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 78 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2661
[CYCLE] Update 79/348 | Step 79,632/500,000 | Episode 104 | Time: 7354.2s
   📊 Metrics: Return=+6.39% | Sharpe=0.694 | DD=11.90% | Turnover=27.29%
   🎚️ Intra-Step TAPE: potential=0.7472 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1408 | critic_loss=0.0072 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0036 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6938 | ema=1.1015 | best_ema=1.1015 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02682
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 7448.0s
   📊 Metrics: Return=+15.46% | Sharpe=0.935 | DD=11.90% | Turnover=27.39%
   🎚️ Intra-Step TAPE: potential=0.2275 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1403 | critic_loss=0.0085 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0043 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9345 | ema=1.0848 | best_ema=1.0848 | no_improve=0
   🔬 Alpha Diversity: mean=0.96 | std=0.18 | range=[0.75, 2.29] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.07 | GLD=1.00 | COP=0.99  BOT: XOM=0.90 | BRK-B=0.89 | NEE=0.88
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0091, db=0.0066, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=33 (29.5%), low_vol=48 (42.9%), medium_vol=31 (27.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 80 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 81/348 | Step 81,648/500,000 | Episode 104 | Time: 7539.1s
   📊 Metrics: Return=+13.43% | Sharpe=0.440 | DD=13.74% | Turnover=26.70%
   🎚️ Intra-Step TAPE: potential=0.5257 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1357 | critic_loss=0.0078 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0039 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4404 | ema=1.0203 | best_ema=1.0203 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02056
[CYCLE] Update 82/348 | Step 82,656/500,000 | Episode 104 | Time: 7630.3s
   📊 Metrics: Return=+23.85% | Sharpe=0.587 | DD=13.74% | Turnover=26.92%
   🎚️ Intra-Step TAPE: potential=0.4808 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1407 | critic_loss=0.0042 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0021 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5871 | ema=0.9770 | best_ema=0.9770 | no_improve=0
   🔬 Alpha Diversity: mean=0.96 | std=0.15 | range=[0.74, 1.75] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.23 | GLD=1.04 | AMZN=1.02  BOT: HON=0.89 | KO=0.89 | NEE=0.88
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0096, db=0.0070, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=33 (29.5%), low_vol=48 (42.9%), medium_vol=31 (27.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 82 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01841
[CYCLE] Update 83/348 | Step 83,664/500,000 | Episode 104 | Time: 7722.8s
   📊 Metrics: Return=+25.61% | Sharpe=0.514 | DD=13.74% | Turnover=26.67%
   🎚️ Intra-Step TAPE: potential=0.2461 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1360 | critic_loss=0.0065 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5138 | ema=0.9307 | best_ema=0.9307 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00106_shp1p012_actor.weights.h5 (Sharpe=1.012, MDD=8.29%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00108_shp1p134_actor.weights.h5 (Sharpe=1.134, MDD=11.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00109_shp1p152_actor.weights.h5 (Sharpe=1.152, MDD=18.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00111_shp1p256_actor.weights.h5 (Sharpe=1.256, MDD=11.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00112_shp1p181_actor.weights.h5 (Sharpe=1.181, MDD=11.91%)
[CYCLE] Update 84/348 | Step 84,672/500,000 | Episode 112 | Time: 7817.1s
   📊 Metrics: Return=+60.36% | Sharpe=1.181 | DD=11.91% | Turnover=26.28%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1353 | critic_loss=0.0261 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0131 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1813 | ema=0.9557 | best_ema=0.9557 | no_improve=0
   🔬 Alpha Diversity: mean=1.11 | std=0.13 | range=[0.63, 1.86] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.22 | AAPL=1.19 | AMZN=1.18  BOT: AMT=1.08 | KO=1.08 | NEE=1.05
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0089, db=0.0065, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (29.2%), low_vol=53 (44.2%), medium_vol=32 (26.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 84 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5396
   📈 Benchmark Relative: 1/N bonus=0.000 (EW ret=0.00173) | SPY bonus=0.012 (SPY ret=-0.00236)
[CYCLE] Update 85/348 | Step 85,680/500,000 | Episode 112 | Time: 7909.3s
   📊 Metrics: Return=+5.34% | Sharpe=0.766 | DD=7.32% | Turnover=24.67%
   🎚️ Intra-Step TAPE: potential=0.6540 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1394 | critic_loss=0.0109 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0055 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7662 | ema=0.9368 | best_ema=0.9368 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01382
[CYCLE] Update 86/348 | Step 86,688/500,000 | Episode 112 | Time: 8001.0s
   📊 Metrics: Return=+10.89% | Sharpe=0.805 | DD=7.84% | Turnover=24.23%
   🎚️ Intra-Step TAPE: potential=0.7561 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1386 | critic_loss=0.0067 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8047 | ema=0.9236 | best_ema=0.9236 | no_improve=0
   🔬 Alpha Diversity: mean=1.20 | std=0.13 | range=[0.79, 2.17] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.24 | MSFT=1.22 | KO=1.21  BOT: PG=1.17 | BRK-B=1.15 | NEE=1.14
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0090, db=0.0065, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (29.2%), low_vol=53 (44.2%), medium_vol=32 (26.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 86 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01581
[CYCLE] Update 87/348 | Step 87,696/500,000 | Episode 112 | Time: 8091.7s
   📊 Metrics: Return=+14.56% | Sharpe=0.707 | DD=7.84% | Turnover=24.59%
   🎚️ Intra-Step TAPE: potential=0.2311 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1374 | critic_loss=0.0048 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7070 | ema=0.9019 | best_ema=0.9019 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01581
[CYCLE] Update 88/348 | Step 88,704/500,000 | Episode 112 | Time: 8185.5s
   📊 Metrics: Return=+23.76% | Sharpe=0.882 | DD=7.84% | Turnover=24.93%
   🎚️ Intra-Step TAPE: potential=0.2708 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1342 | critic_loss=0.0035 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8816 | ema=0.8999 | best_ema=0.8999 | no_improve=0
   🔬 Alpha Diversity: mean=0.94 | std=0.28 | range=[0.75, 3.04] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.96 | MSFT=0.94 | NVDA=0.92  BOT: AMZN=0.86 | BRK-B=0.85 | NEE=0.85
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0093, db=0.0068, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (29.2%), low_vol=53 (44.2%), medium_vol=32 (26.7%)
[CYCLE] Update 89/348 | Step 89,712/500,000 | Episode 112 | Time: 8279.4s
   📊 Metrics: Return=+28.48% | Sharpe=0.850 | DD=7.84% | Turnover=25.64%
   🎚️ Intra-Step TAPE: potential=0.5929 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1381 | critic_loss=0.0040 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0024
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8499 | ema=0.8949 | best_ema=0.8949 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00114_shp0p827_actor.weights.h5 (Sharpe=0.827, MDD=13.16%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00115_shp1p084_actor.weights.h5 (Sharpe=1.084, MDD=10.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00116_shp0p787_actor.weights.h5 (Sharpe=0.787, MDD=8.23%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00118_shp0p977_actor.weights.h5 (Sharpe=0.977, MDD=12.09%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00119_shp0p702_actor.weights.h5 (Sharpe=0.702, MDD=10.46%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 8374.8s
   📊 Metrics: Return=+22.19% | Sharpe=0.457 | DD=12.40% | Turnover=26.28%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1454 | critic_loss=0.0211 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0105 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4567 | ema=0.8511 | best_ema=0.8511 | no_improve=0
   🔬 Alpha Diversity: mean=0.73 | std=0.54 | range=[0.52, 4.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.69 | AAPL=0.66 | AMZN=0.65  BOT: AMT=0.59 | XOM=0.59 | NEE=0.57
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0092, db=0.0067, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=38 (29.7%), low_vol=55 (43.0%), medium_vol=35 (27.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2953
   📈 Benchmark Relative: 1/N bonus=0.000 (EW ret=-0.00322) | SPY bonus=0.002 (SPY ret=-0.00251)

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps
[CYCLE] Update 91/348 | Step 91,728/500,000 | Episode 120 | Time: 8467.8s
   📊 Metrics: Return=+2.52% | Sharpe=0.274 | DD=9.70% | Turnover=30.46%
   🎚️ Intra-Step TAPE: potential=0.6660 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1394 | critic_loss=0.0120 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2741 | ema=0.7934 | best_ema=0.7934 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01385

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps
[CYCLE] Update 92/348 | Step 92,736/500,000 | Episode 120 | Time: 8560.2s
   📊 Metrics: Return=+4.94% | Sharpe=0.268 | DD=11.49% | Turnover=30.36%
   🎚️ Intra-Step TAPE: potential=0.7116 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1449 | critic_loss=0.0078 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0039 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2677 | ema=0.7408 | best_ema=0.7408 | no_improve=0
   🔬 Alpha Diversity: mean=0.74 | std=0.29 | range=[0.55, 2.78] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.77 | AAPL=0.74 | GLD=0.73  BOT: PG=0.65 | HON=0.65 | NEE=0.62
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0096, db=0.0070, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=38 (29.7%), low_vol=55 (43.0%), medium_vol=35 (27.3%)

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps
[CYCLE] Update 93/348 | Step 93,744/500,000 | Episode 120 | Time: 8653.4s
   📊 Metrics: Return=+12.35% | Sharpe=0.504 | DD=11.49% | Turnover=30.27%
   🎚️ Intra-Step TAPE: potential=0.4415 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1364 | critic_loss=0.0063 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0032 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5043 | ema=0.7172 | best_ema=0.7172 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02510

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps
[CYCLE] Update 94/348 | Step 94,752/500,000 | Episode 120 | Time: 8744.7s
   📊 Metrics: Return=+26.39% | Sharpe=0.871 | DD=11.49% | Turnover=29.39%
   🎚️ Intra-Step TAPE: potential=0.7382 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1369 | critic_loss=0.0051 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8715 | ema=0.7326 | best_ema=0.7326 | no_improve=0
   🔬 Alpha Diversity: mean=0.96 | std=0.13 | range=[0.72, 1.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.05 | NVDA=1.04 | MSFT=1.03  BOT: KO=0.88 | PG=0.87 | NEE=0.85
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0098, db=0.0072, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=38 (29.7%), low_vol=55 (43.0%), medium_vol=35 (27.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 94 updates. Policy may not be learning asset discrimination.

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps
[CYCLE] Update 95/348 | Step 95,760/500,000 | Episode 120 | Time: 8838.6s
   📊 Metrics: Return=+43.80% | Sharpe=1.175 | DD=11.49% | Turnover=28.98%
   🎚️ Intra-Step TAPE: potential=0.7556 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1368 | critic_loss=0.0035 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1749 | ema=0.7768 | best_ema=0.7768 | no_improve=0

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps
[CYCLE] Update 96/348 | Step 96,768/500,000 | Episode 120 | Time: 8932.1s
   📊 Metrics: Return=+45.41% | Sharpe=0.930 | DD=11.49% | Turnover=28.52%
   🎚️ Intra-Step TAPE: potential=0.2393 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1334 | critic_loss=0.0052 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9296 | ema=0.7921 | best_ema=0.7921 | no_improve=0
   🔬 Alpha Diversity: mean=0.85 | std=0.10 | range=[0.64, 1.38] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AAPL=0.90 | NVDA=0.89 | AMZN=0.89  BOT: XOM=0.80 | KO=0.80 | NEE=0.78
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0095, db=0.0070, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=38 (29.7%), low_vol=55 (43.0%), medium_vol=35 (27.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 96 updates. Policy may not be learning asset discrimination.

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps
[CYCLE] Update 97/348 | Step 97,776/500,000 | Episode 120 | Time: 9023.9s
   📊 Metrics: Return=+43.75% | Sharpe=0.749 | DD=11.49% | Turnover=28.52%
   🎚️ Intra-Step TAPE: potential=0.2389 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1411 | critic_loss=0.0040 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7491 | ema=0.7878 | best_ema=0.7878 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00126_shp0p708_actor.weights.h5 (Sharpe=0.708, MDD=13.58%)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps
[CYCLE] Update 98/348 | Step 98,784/500,000 | Episode 128 | Time: 9114.9s
   📊 Metrics: Return=+45.35% | Sharpe=0.670 | DD=12.97% | Turnover=28.27%
   🎚️ Intra-Step TAPE: potential=0.6929 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1354 | critic_loss=0.0206 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0103 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6701 | ema=0.7760 | best_ema=0.7760 | no_improve=0
   🔬 Alpha Diversity: mean=0.74 | std=0.11 | range=[0.54, 1.95] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.81 | AMZN=0.77 | MSFT=0.76  BOT: PG=0.70 | KO=0.70 | NEE=0.69
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0111, db=0.0082, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=57 (41.9%), medium_vol=35 (25.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 98 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.72% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3622
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01878

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps
[CYCLE] Update 99/348 | Step 99,792/500,000 | Episode 128 | Time: 9209.4s
   📊 Metrics: Return=+15.81% | Sharpe=1.358 | DD=11.29% | Turnover=29.94%
   🎚️ Intra-Step TAPE: potential=0.7429 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1370 | critic_loss=0.0101 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3580 | ema=0.8342 | best_ema=0.8342 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03093

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.55

🎛️ EXECUTION BETA UPDATE at 100,800 steps:
   action_execution_beta: 0.450 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 9303.0s
   📊 Metrics: Return=+20.48% | Sharpe=1.096 | DD=11.29% | Turnover=30.69%
   🎚️ Intra-Step TAPE: potential=0.4198 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1395 | critic_loss=0.0044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0960 | ema=0.8604 | best_ema=0.8604 | no_improve=0
   🔬 Alpha Diversity: mean=0.69 | std=0.06 | range=[0.48, 1.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.74 | AAPL=0.71 | HD=0.71  BOT: GOOGL=0.67 | XOM=0.67 | JPM=0.66
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0107, db=0.0079, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=57 (41.9%), medium_vol=35 (25.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 100 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02794
[CYCLE] Update 101/348 | Step 101,808/500,000 | Episode 128 | Time: 9395.4s
   📊 Metrics: Return=+38.85% | Sharpe=1.536 | DD=11.29% | Turnover=33.15%
   🎚️ Intra-Step TAPE: potential=0.7409 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1357 | critic_loss=0.0044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5358 | ema=0.9280 | best_ema=0.9280 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02510
[CYCLE] Update 102/348 | Step 102,816/500,000 | Episode 128 | Time: 9488.7s
   📊 Metrics: Return=+55.73% | Sharpe=1.717 | DD=11.29% | Turnover=33.64%
   🎚️ Intra-Step TAPE: potential=0.7450 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1386 | critic_loss=0.0046 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7166 | ema=1.0068 | best_ema=1.0068 | no_improve=0
   🔬 Alpha Diversity: mean=0.91 | std=0.14 | range=[0.35, 1.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.00 | V=0.98 | MSFT=0.97  BOT: COP=0.90 | XOM=0.90 | CAT=0.89
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0105, db=0.0078, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=57 (41.9%), medium_vol=35 (25.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 102 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 103/348 | Step 103,824/500,000 | Episode 128 | Time: 9580.8s
   📊 Metrics: Return=+69.95% | Sharpe=1.554 | DD=11.29% | Turnover=33.79%
   🎚️ Intra-Step TAPE: potential=0.3990 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1362 | critic_loss=0.0043 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5539 | ema=1.0615 | best_ema=1.0615 | no_improve=0
[CYCLE] Update 104/348 | Step 104,832/500,000 | Episode 128 | Time: 9674.7s
   📊 Metrics: Return=+62.99% | Sharpe=1.156 | DD=11.29% | Turnover=34.25%
   🎚️ Intra-Step TAPE: potential=0.2303 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1334 | critic_loss=0.0051 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1555 | ema=1.0709 | best_ema=1.0615 | no_improve=1
   🔬 Alpha Diversity: mean=0.85 | std=0.09 | range=[0.41, 1.22] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=0.90 | MSFT=0.90 | JNJ=0.90  BOT: JPM=0.85 | AMZN=0.83 | CAT=0.82
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0104, db=0.0078, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=57 (41.9%), medium_vol=35 (25.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 104 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 105/348 | Step 105,840/500,000 | Episode 128 | Time: 9769.3s
   📊 Metrics: Return=+71.20% | Sharpe=1.064 | DD=17.60% | Turnover=34.44%
   🎚️ Intra-Step TAPE: potential=0.2964 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1337 | critic_loss=0.0047 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0637 | ema=1.0702 | best_ema=1.0615 | no_improve=2
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00129_shp0p997_actor.weights.h5 (Sharpe=0.997, MDD=18.05%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00130_shp1p032_actor.weights.h5 (Sharpe=1.032, MDD=17.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00131_shp0p883_actor.weights.h5 (Sharpe=0.883, MDD=11.38%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00133_shp0p716_actor.weights.h5 (Sharpe=0.716, MDD=15.94%)
[CYCLE] Update 106/348 | Step 106,848/500,000 | Episode 136 | Time: 9864.5s
   📊 Metrics: Return=+26.65% | Sharpe=0.360 | DD=13.28% | Turnover=34.93%
   🎚️ Intra-Step TAPE: potential=0.2421 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1402 | critic_loss=0.0299 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0149 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3604 | ema=0.9992 | best_ema=1.0615 | no_improve=3
   🔬 Alpha Diversity: mean=0.89 | std=0.11 | range=[0.23, 1.31] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.97 | JNJ=0.95 | HD=0.94  BOT: NVDA=0.84 | CAT=0.83 | AMZN=0.83
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0099, db=0.0074, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=46 (31.9%), low_vol=59 (41.0%), medium_vol=39 (27.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 106 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.75% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2704
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02513
[CYCLE] Update 107/348 | Step 107,856/500,000 | Episode 136 | Time: 9958.2s
   📊 Metrics: Return=-6.51% | Sharpe=-0.606 | DD=11.45% | Turnover=37.58%
   🎚️ Intra-Step TAPE: potential=0.2361 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1352 | critic_loss=0.0099 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.6280 | ema=0.8365 | best_ema=1.0615 | no_improve=4
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02349
[CYCLE] Update 108/348 | Step 108,864/500,000 | Episode 136 | Time: 10051.4s
   📊 Metrics: Return=+3.83% | Sharpe=0.148 | DD=12.58% | Turnover=37.25%
   🎚️ Intra-Step TAPE: potential=0.6173 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1383 | critic_loss=0.0086 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0043 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1286 | ema=0.7657 | best_ema=1.0615 | no_improve=5
   🔬 Alpha Diversity: mean=1.00 | std=0.10 | range=[0.70, 1.45] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.07 | HD=1.07 | V=1.04  BOT: XOM=0.95 | CAT=0.94 | COP=0.93
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0097, db=0.0072, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=46 (31.9%), low_vol=59 (41.0%), medium_vol=39 (27.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 108 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02551
[CYCLE] Update 109/348 | Step 109,872/500,000 | Episode 136 | Time: 10144.3s
   📊 Metrics: Return=+11.99% | Sharpe=0.411 | DD=12.58% | Turnover=36.04%
   🎚️ Intra-Step TAPE: potential=0.7536 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1335 | critic_loss=0.0068 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4019 | ema=0.7293 | best_ema=1.0615 | no_improve=6
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02360
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 136 | Time: 10237.2s
   📊 Metrics: Return=+23.29% | Sharpe=0.672 | DD=12.58% | Turnover=34.65%
   🎚️ Intra-Step TAPE: potential=0.7269 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1408 | critic_loss=0.0047 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6721 | ema=0.7236 | best_ema=1.0615 | no_improve=7
   🔬 Alpha Diversity: mean=1.34 | std=0.14 | range=[0.85, 2.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.48 | UNH=1.41 | HD=1.41  BOT: GOOGL=1.30 | AMZN=1.29 | COP=1.27
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0112, db=0.0084, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=46 (31.9%), low_vol=59 (41.0%), medium_vol=39 (27.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 110 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02433
[CYCLE] Update 111/348 | Step 111,888/500,000 | Episode 136 | Time: 10328.3s
   📊 Metrics: Return=+39.66% | Sharpe=0.952 | DD=12.58% | Turnover=33.63%
   🎚️ Intra-Step TAPE: potential=0.6684 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1422 | critic_loss=0.0041 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0021 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9518 | ema=0.7464 | best_ema=1.0615 | no_improve=8
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02574
[CYCLE] Update 112/348 | Step 112,896/500,000 | Episode 136 | Time: 10419.6s
   📊 Metrics: Return=+43.39% | Sharpe=0.823 | DD=12.58% | Turnover=33.45%
   🎚️ Intra-Step TAPE: potential=0.5888 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1356 | critic_loss=0.0044 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8229 | ema=0.7541 | best_ema=1.0615 | no_improve=9
   🔬 Alpha Diversity: mean=1.36 | std=0.13 | range=[0.95, 2.01] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.46 | GLD=1.45 | MSFT=1.43  BOT: COP=1.29 | XOM=1.29 | CAT=1.28
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0109, db=0.0082, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=46 (31.9%), low_vol=59 (41.0%), medium_vol=39 (27.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 112 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02461
[CYCLE] Update 113/348 | Step 113,904/500,000 | Episode 136 | Time: 10510.4s
   📊 Metrics: Return=+37.05% | Sharpe=0.565 | DD=17.23% | Turnover=32.91%
   🎚️ Intra-Step TAPE: potential=0.2435 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1406 | critic_loss=0.0036 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0018 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5647 | ema=0.7351 | best_ema=1.0615 | no_improve=10
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00139_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=20.77%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00140_shp0p709_actor.weights.h5 (Sharpe=0.709, MDD=11.98%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00141_shp0p790_actor.weights.h5 (Sharpe=0.790, MDD=16.29%)
[CYCLE] Update 114/348 | Step 114,912/500,000 | Episode 144 | Time: 10605.0s
   📊 Metrics: Return=+54.68% | Sharpe=0.659 | DD=15.71% | Turnover=32.86%
   🎚️ Intra-Step TAPE: potential=0.7540 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1409 | critic_loss=0.0207 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0103 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6594 | ema=0.7276 | best_ema=1.0615 | no_improve=11
   🔬 Alpha Diversity: mean=1.58 | std=0.19 | range=[0.75, 2.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.77 | GLD=1.76 | KO=1.69  BOT: NVDA=1.46 | COP=1.46 | CAT=1.42
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0093, db=0.0070, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=61 (40.1%), medium_vol=41 (27.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 114 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3536
   📈 Benchmark Relative: 1/N bonus=0.000 (EW ret=0.00190) | SPY bonus=0.000 (SPY ret=0.00144)
[CYCLE] Update 115/348 | Step 115,920/500,000 | Episode 144 | Time: 10696.9s
   📊 Metrics: Return=+11.16% | Sharpe=1.252 | DD=7.04% | Turnover=29.27%
   🎚️ Intra-Step TAPE: potential=0.4140 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1431 | critic_loss=0.0097 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2522 | ema=0.7800 | best_ema=1.0615 | no_improve=12
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02127
[CYCLE] Update 116/348 | Step 116,928/500,000 | Episode 144 | Time: 10790.1s
   📊 Metrics: Return=+18.43% | Sharpe=1.185 | DD=7.04% | Turnover=30.12%
   🎚️ Intra-Step TAPE: potential=0.6689 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1400 | critic_loss=0.0052 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1851 | ema=0.8205 | best_ema=1.0615 | no_improve=13
   🔬 Alpha Diversity: mean=1.23 | std=0.24 | range=[0.92, 3.04] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.30 | HD=1.28 | KO=1.24  BOT: COP=1.11 | CAT=1.09 | NVDA=1.09
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0102, db=0.0077, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=61 (40.1%), medium_vol=41 (27.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 116 updates. Policy may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02087
[CYCLE] Update 117/348 | Step 117,936/500,000 | Episode 144 | Time: 10881.2s
   📊 Metrics: Return=+25.81% | Sharpe=1.175 | DD=7.04% | Turnover=30.56%
   🎚️ Intra-Step TAPE: potential=0.4554 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1390 | critic_loss=0.0044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1754 | ema=0.8560 | best_ema=1.0615 | no_improve=14
[CYCLE] Update 118/348 | Step 118,944/500,000 | Episode 144 | Time: 10973.7s
   📊 Metrics: Return=+30.28% | Sharpe=1.074 | DD=7.04% | Turnover=30.85%
   🎚️ Intra-Step TAPE: potential=0.2320 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1395 | critic_loss=0.0047 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0737 | ema=0.8778 | best_ema=1.0615 | no_improve=15
   🔬 Alpha Diversity: mean=1.31 | std=0.29 | range=[0.93, 3.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.34 | HD=1.33 | JNJ=1.30  BOT: CAT=1.17 | AMZN=1.15 | NVDA=1.15
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0102, db=0.0077, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=61 (40.1%), medium_vol=41 (27.0%)
[CYCLE] Update 119/348 | Step 119,952/500,000 | Episode 144 | Time: 11065.0s
   📊 Metrics: Return=+29.77% | Sharpe=0.798 | DD=7.19% | Turnover=31.21%
   🎚️ Intra-Step TAPE: potential=0.2422 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1388 | critic_loss=0.0038 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0019 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7985 | ema=0.8699 | best_ema=1.0615 | no_improve=16
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 144 | Time: 11158.8s
   📊 Metrics: Return=+26.42% | Sharpe=0.541 | DD=10.09% | Turnover=31.32%
   🎚️ Intra-Step TAPE: potential=0.2398 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1402 | critic_loss=0.0049 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0028
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5409 | ema=0.8370 | best_ema=1.0615 | no_improve=17
   🔬 Alpha Diversity: mean=1.29 | std=0.24 | range=[0.95, 2.92] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.35 | HD=1.35 | KO=1.31  BOT: CAT=1.16 | NVDA=1.15 | AMZN=1.13
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0097, db=0.0073, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=61 (40.1%), medium_vol=41 (27.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 120 updates. Policy may not be learning asset discrimination.
[CYCLE] Update 121/348 | Step 121,968/500,000 | Episode 144 | Time: 11251.0s
   📊 Metrics: Return=+33.54% | Sharpe=0.558 | DD=10.35% | Turnover=31.46%
   🎚️ Intra-Step TAPE: potential=0.2667 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1369 | critic_loss=0.0037 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0019 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5582 | ema=0.8091 | best_ema=1.0615 | no_improve=18
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00145_shp0p832_actor.weights.h5 (Sharpe=0.832, MDD=17.80%)
[CYCLE] Update 122/348 | Step 122,976/500,000 | Episode 152 | Time: 11344.6s
   📊 Metrics: Return=+35.46% | Sharpe=0.527 | DD=11.98% | Turnover=31.30%
   🎚️ Intra-Step TAPE: potential=0.2395 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1393 | critic_loss=0.0235 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0118 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5271 | ema=0.7809 | best_ema=1.0615 | no_improve=19
   🔬 Alpha Diversity: mean=1.21 | std=0.17 | range=[0.80, 2.43] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.29 | HD=1.26 | KO=1.25  BOT: AMZN=1.14 | CAT=1.12 | NVDA=1.10
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0095, db=0.0071, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=64 (40.0%), medium_vol=43 (26.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 122 updates. Policy may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 7.73% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3043
   📈 Benchmark Relative: 1/N bonus=0.000 (EW ret=0.00497) | SPY bonus=0.013 (SPY ret=-0.00034)
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.01565
[CYCLE] Update 123/348 | Step 123,984/500,000 | Episode 152 | Time: 11438.7s
   📊 Metrics: Return=-4.97% | Sharpe=-0.718 | DD=10.24% | Turnover=32.84%
   🎚️ Intra-Step TAPE: potential=0.2360 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1403 | critic_loss=0.0071 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0036 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.7180 | ema=0.6310 | best_ema=1.0615 | no_improve=20
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01401
[CYCLE] Update 124/348 | Step 124,992/500,000 | Episode 152 | Time: 11532.7s
   📊 Metrics: Return=+2.54% | Sharpe=0.063 | DD=10.24% | Turnover=33.86%
   🎚️ Intra-Step TAPE: potential=0.2989 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1372 | critic_loss=0.0046 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0631 | ema=0.5742 | best_ema=1.0615 | no_improve=21
   🔬 Alpha Diversity: mean=1.04 | std=0.44 | range=[0.79, 4.13] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.02 | GLD=0.99 | V=0.98  BOT: CAT=0.89 | AMZN=0.89 | NVDA=0.87
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0099, db=0.0073, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=64 (40.0%), medium_vol=43 (26.9%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01367
[CYCLE] Update 125/348 | Step 126,000/500,000 | Episode 152 | Time: 11626.1s
   📊 Metrics: Return=+9.78% | Sharpe=0.384 | DD=10.24% | Turnover=33.58%
   🎚️ Intra-Step TAPE: potential=0.7385 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1379 | critic_loss=0.0059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3845 | ema=0.5552 | best_ema=1.0615 | no_improve=22
[CYCLE] Update 126/348 | Step 127,008/500,000 | Episode 152 | Time: 11717.1s
   📊 Metrics: Return=+11.43% | Sharpe=0.342 | DD=10.24% | Turnover=33.37%
   🎚️ Intra-Step TAPE: potential=0.3219 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1368 | critic_loss=0.0078 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0039 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3424 | ema=0.5340 | best_ema=1.0615 | no_improve=23
   🔬 Alpha Diversity: mean=1.35 | std=0.50 | range=[1.04, 4.26] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.32 | V=1.30 | HON=1.27  BOT: AMZN=1.20 | NVDA=1.20 | CAT=1.19
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0097, db=0.0072, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=64 (40.0%), medium_vol=43 (26.9%)
[CYCLE] Update 127/348 | Step 128,016/500,000 | Episode 152 | Time: 11808.3s
   📊 Metrics: Return=+14.81% | Sharpe=0.359 | DD=10.24% | Turnover=33.07%
   🎚️ Intra-Step TAPE: potential=0.6151 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1395 | critic_loss=0.0064 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0032 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3594 | ema=0.5165 | best_ema=1.0615 | no_improve=24
[CYCLE] Update 128/348 | Step 129,024/500,000 | Episode 152 | Time: 11902.0s
   📊 Metrics: Return=+12.11% | Sharpe=0.204 | DD=10.24% | Turnover=32.52%
   🎚️ Intra-Step TAPE: potential=0.2447 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1380 | critic_loss=0.0056 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0028 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0029
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2040 | ema=0.4852 | best_ema=1.0615 | no_improve=25
   🔬 Alpha Diversity: mean=1.42 | std=0.24 | range=[1.09, 3.13] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: HD=1.45 | UNH=1.43 | MSFT=1.41  BOT: CAT=1.34 | COP=1.32 | AMZN=1.28
   🎛️ Mixture Usage: C0=0.0% | C1=0.0% | C2=0.0%
   🧬 FiLM: seq(dg=0.0000, db=0.0000, sat=0.0%) | latent(dg=0.0000, db=0.0000, sat=0.0%) | regime(dg=0.0095, db=0.0070, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=64 (40.0%), medium_vol=43 (26.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 128 updates. Policy may not be learning asset discrimination.
   🛑 Early-stop triggered: ema_patience_exhausted (no improvement for 25 updates) (step=129,024, update=128)

[OK] THREE-COMPONENT TAPE v3 training completed!
   🛑 Stop reason: ema_patience_exhausted (no improvement for 25 updates)
   Total episodes: 152
   Total timesteps: 129,024
   Training time: 11902.04s (198.37min)
📊 Training summary saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_053418_summary.csv
💾 Final models saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00152_shp0p527_actor.weights.h5, /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00152_shp0p527_critic.weights.h5
🎯 Default selected checkpoint: final high-watermark-style checkpoint
[OK] Training complete
checkpoint_prefix: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00152_shp0p527