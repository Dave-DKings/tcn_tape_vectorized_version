[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4

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
   Train shape: (15110, 67)
   Test shape: (9180, 67)
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
   ⚡ Parallel rollout envs: 4
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 25.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🌊 DSR Regime Scaling: ENABLED | low_mult=0.3 (vol<0.12) | mid_mult=1.0 | high_mult=1.5 (vol>0.25)
   📈 Outperformance Bonus (SPY): ENABLED | scalar=3.0
   🔐 Lagrangian CVaR: ENABLED | threshold=-0.025 | lr=0.004 | lambda_max=5.0 | penalty_scale=3.0
   Tail-Aware Advantage: ENABLED | weight=0.1 | bottom_k=4
   Alpha Regularization: hhi_coef=0.01 | dispersion_coef=0.05 | target_std=0.07
   🧪 Aux Per-Asset Return Head: ENABLED | coef=0.35
   🔒 Dirichlet Alpha Cap: 16.0
   🔒 Drawdown dual controller (requested): target=18.00%, tolerance=-1.50% (trigger boundary ≈ 16.50%), lr=0.100, λ_init=0.50, λ_floor=0.00, λ_max=5.00, penalty_coef=1.50
   📐 Position constraints: max_single_asset=25%, min_cash=5%
   [DEBUG] Regime-balanced sampling: use_curriculum_learning=True, volatility_regime pre-existing=False
   🎲 Volatility regimes ready for sampling (computed):
      high_vol: 494 dates (32.7%)
      low_vol: 494 dates (32.7%)
      medium_vol: 523 dates (34.6%)
   🧭 Regime start buckets (train env):
      high_vol: 494 dates (32.7%)
      low_vol: 494 dates (32.7%)
      medium_vol: 523 dates (34.6%)
   [OK] Drawdown controller armed in env: target=18.00%, trigger=16.50%, λ_init=0.500, λ_floor=0.000, λ_max=5.00, penalty_coef=1.50
[OK] THREE-COMPONENT TAPE v3 Environments created:
   Training: 1511 days
   Parallel train env instances: 4
   Testing: 918 days

🤖 Creating TCN_FUSION agent with Dirichlet distribution for Exp 6...
[OK] Agent created: PPOAgentTF
   [RAND] Dirichlet Distribution: ENABLED
   [TOOL] Actor LR schedule: 0.000030@0 => 0.000020@150,000 => 0.000010@350,000
   [TOOL] Critic LR schedule: 0.000150@0 => 0.000120@150,000 => 0.000100@350,000
   State dim: 447
   Action dim: 10
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
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260313_055213_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260313_055213_step_diagnostics.csv

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
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260313_055213_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260313_055213_metadata.json
[CYCLE] Update 1/348 | Step 1,008/500,000 | Episode 0 | Time: 66.0s
   📊 Metrics: Return=+3.68% | Sharpe=0.182 | DD=18.59% | Turnover=7.14%
   🎚️ Intra-Step TAPE: potential=0.5423 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2113 | critic_loss=0.3379 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1690 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1822 | ema=0.1822 | best_ema=0.1822 | no_improve=0
[CYCLE] Update 2/348 | Step 2,016/500,000 | Episode 0 | Time: 117.6s
   📊 Metrics: Return=+34.55% | Sharpe=0.667 | DD=26.81% | Turnover=7.69%
   🎚️ Intra-Step TAPE: potential=0.7293 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1642 | critic_loss=0.2714 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1357 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6233 | ema=0.2263 | best_ema=0.2263 | no_improve=0
   🔬 Alpha Diversity: mean=8.76 | std=3.10 | range=[0.33, 16.00] | cap_hit=1.4%
   🏷️ Alpha Per-Asset  TOP: NVDA=12.16 | CAT=9.95 | AMZN=9.69  BOT: JNJ=9.04 | JPM=9.04 | XOM=7.94
   🧭 Regime Start Dist (train resets): high_vol=1 (25.0%), low_vol=2 (50.0%), medium_vol=1 (25.0%)
   🔐 Lagrangian CVaR: λ=0.0019 | penalty=-0.0000 | rolling_cvar=-0.02272
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp1p153_actor.weights.h5 (Sharpe=1.153, MDD=18.77%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00004_shp1p259_actor.weights.h5 (Sharpe=1.259, MDD=18.12%)
[CYCLE] Update 3/348 | Step 3,024/500,000 | Episode 4 | Time: 169.7s
   📊 Metrics: Return=+69.17% | Sharpe=1.259 | DD=18.12% | Turnover=8.39%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1313 | critic_loss=0.1413 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0707 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2589 | ema=0.3295 | best_ema=0.3295 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.500) | TAPE=0.5360
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00013) | SPY bonus=0.000 (SPY ret=-0.00025)
   🔐 Lagrangian CVaR: λ=0.0121 | penalty=-0.0001 | rolling_cvar=-0.02152
[CYCLE] Update 4/348 | Step 4,032/500,000 | Episode 4 | Time: 222.4s
   📊 Metrics: Return=-0.88% | Sharpe=-0.088 | DD=20.22% | Turnover=12.27%
   🎚️ Intra-Step TAPE: potential=0.7543 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1133 | critic_loss=0.2121 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1060 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0008
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0877 | ema=0.2878 | best_ema=0.2878 | no_improve=0
   🔬 Alpha Diversity: mean=3.48 | std=1.21 | range=[1.05, 8.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.27 | GLD=4.24 | NEE=3.92  BOT: JPM=3.22 | XOM=3.17 | MSFT=3.03
   🧭 Regime Start Dist (train resets): high_vol=3 (37.5%), low_vol=4 (50.0%), medium_vol=1 (12.5%)
[CYCLE] Update 5/348 | Step 5,040/500,000 | Episode 4 | Time: 276.2s
   📊 Metrics: Return=-11.06% | Sharpe=-0.311 | DD=25.52% | Turnover=15.00%
   🎚️ Intra-Step TAPE: potential=0.2122 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0974 | critic_loss=0.2574 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1287 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0013 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3231 | ema=0.2267 | best_ema=0.2267 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p769_actor.weights.h5 (Sharpe=0.769, MDD=23.66%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p444_actor.weights.h5 (Sharpe=1.444, MDD=14.67%)
[CYCLE] Update 6/348 | Step 6,048/500,000 | Episode 8 | Time: 330.7s
   📊 Metrics: Return=+74.86% | Sharpe=1.444 | DD=14.67% | Turnover=17.54%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0938 | critic_loss=0.2238 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1119 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0014 | dispersion_loss=0.0006
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4440 | ema=0.3485 | best_ema=0.3485 | no_improve=0
   🔬 Alpha Diversity: mean=0.91 | std=0.54 | range=[0.46, 3.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.03 | NEE=0.88 | JNJ=0.79  BOT: AMZN=0.70 | MSFT=0.68 | JPM=0.65
   🧭 Regime Start Dist (train resets): high_vol=5 (41.7%), low_vol=4 (33.3%), medium_vol=3 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5823
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00054) | SPY bonus=0.006 (SPY ret=-0.00200)
   🔐 Lagrangian CVaR: λ=0.0027 | penalty=-0.0000 | rolling_cvar=-0.01851
[CYCLE] Update 7/348 | Step 7,056/500,000 | Episode 8 | Time: 384.6s
   📊 Metrics: Return=+5.24% | Sharpe=0.368 | DD=10.15% | Turnover=23.87%
   🎚️ Intra-Step TAPE: potential=0.7169 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0898 | critic_loss=0.1003 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0502 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0014 | dispersion_loss=0.0005
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3678 | ema=0.3504 | best_ema=0.3504 | no_improve=0
[CYCLE] Update 8/348 | Step 8,064/500,000 | Episode 8 | Time: 438.1s
   📊 Metrics: Return=+24.82% | Sharpe=0.586 | DD=21.38% | Turnover=24.26%
   🎚️ Intra-Step TAPE: potential=0.2308 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0851 | critic_loss=0.2047 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1023 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0013 | dispersion_loss=0.0007
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5864 | ema=0.3740 | best_ema=0.3740 | no_improve=0
   🔬 Alpha Diversity: mean=1.09 | std=0.54 | range=[0.53, 3.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.21 | NEE=1.04 | XOM=1.00  BOT: NVDA=0.82 | MSFT=0.80 | AMZN=0.77
   🧭 Regime Start Dist (train resets): high_vol=5 (41.7%), low_vol=4 (33.3%), medium_vol=3 (25.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01310
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00009_shp0p740_actor.weights.h5 (Sharpe=0.740, MDD=21.38%)
[CYCLE] Update 9/348 | Step 9,072/500,000 | Episode 12 | Time: 490.6s
   📊 Metrics: Return=+19.34% | Sharpe=0.432 | DD=16.50% | Turnover=24.31%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0843 | critic_loss=0.1424 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0712 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0013 | dispersion_loss=0.0008
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4322 | ema=0.3798 | best_ema=0.3798 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2741
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.02418) | SPY bonus=0.042 (SPY ret=-0.03007)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01751
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 544.7s
   📊 Metrics: Return=+1.00% | Sharpe=-0.008 | DD=12.75% | Turnover=24.73%
   🎚️ Intra-Step TAPE: potential=0.2330 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0788 | critic_loss=0.0927 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0464 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0083 | ema=0.3410 | best_ema=0.3410 | no_improve=0
   🔬 Alpha Diversity: mean=0.99 | std=0.25 | range=[0.59, 2.14] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.10 | NEE=0.99 | XOM=0.97  BOT: JPM=0.85 | MSFT=0.84 | AMZN=0.80
   🧭 Regime Start Dist (train resets): high_vol=5 (31.2%), low_vol=5 (31.2%), medium_vol=6 (37.5%)
[CYCLE] Update 11/348 | Step 11,088/500,000 | Episode 12 | Time: 598.1s
   📊 Metrics: Return=+25.15% | Sharpe=0.538 | DD=25.85% | Turnover=24.78%
   🎚️ Intra-Step TAPE: potential=0.6393 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0756 | critic_loss=0.1424 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0712 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5177 | ema=0.3587 | best_ema=0.3587 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02180
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00015_shp0p747_actor.weights.h5 (Sharpe=0.747, MDD=20.20%)
[CYCLE] Update 12/348 | Step 12,096/500,000 | Episode 16 | Time: 651.3s
   📊 Metrics: Return=+28.55% | Sharpe=0.437 | DD=24.60% | Turnover=25.61%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0791 | critic_loss=0.0962 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0481 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4368 | ema=0.3665 | best_ema=0.3665 | no_improve=0
   🔬 Alpha Diversity: mean=0.77 | std=0.16 | range=[0.39, 1.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.78 | GLD=0.78 | XOM=0.75  BOT: MSFT=0.70 | AMZN=0.69 | JPM=0.69
   🧭 Regime Start Dist (train resets): high_vol=7 (35.0%), low_vol=5 (25.0%), medium_vol=8 (40.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 12 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.042) | TAPE=0.2683
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02959
[CYCLE] Update 13/348 | Step 13,104/500,000 | Episode 16 | Time: 705.2s
   📊 Metrics: Return=-6.68% | Sharpe=-0.506 | DD=19.39% | Turnover=26.56%
   🎚️ Intra-Step TAPE: potential=0.2282 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0797 | critic_loss=0.0470 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0235 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5059 | ema=0.2793 | best_ema=0.2793 | no_improve=0
[CYCLE] Update 14/348 | Step 14,112/500,000 | Episode 16 | Time: 759.0s
   📊 Metrics: Return=+5.35% | Sharpe=0.114 | DD=19.39% | Turnover=26.29%
   🎚️ Intra-Step TAPE: potential=0.2399 | delta_reward=-0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0734 | critic_loss=0.0723 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0362 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1137 | ema=0.2627 | best_ema=0.2627 | no_improve=0
   🔬 Alpha Diversity: mean=1.05 | std=0.16 | range=[0.75, 1.85] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.18 | XOM=1.08 | JNJ=1.08  BOT: MSFT=0.97 | JPM=0.97 | AMZN=0.94
   🧭 Regime Start Dist (train resets): high_vol=7 (35.0%), low_vol=5 (25.0%), medium_vol=8 (40.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 14 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02244
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00019_shp0p720_actor.weights.h5 (Sharpe=0.720, MDD=19.02%)
[CYCLE] Update 15/348 | Step 15,120/500,000 | Episode 20 | Time: 813.0s
   📊 Metrics: Return=+27.23% | Sharpe=0.414 | DD=26.59% | Turnover=25.10%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0733 | critic_loss=0.0657 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0328 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3756 | ema=0.2740 | best_ema=0.2740 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.049) | TAPE=0.2636
   🔐 Lagrangian CVaR: λ=0.0081 | penalty=-0.0000 | rolling_cvar=-0.03037
[CYCLE] Update 16/348 | Step 16,128/500,000 | Episode 20 | Time: 867.1s
   📊 Metrics: Return=+24.44% | Sharpe=2.286 | DD=2.40% | Turnover=17.55%
   🎚️ Intra-Step TAPE: potential=0.5949 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0758 | critic_loss=0.0276 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.2859 | ema=0.4752 | best_ema=0.4752 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=0.50 | range=[1.25, 4.23] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=3.20 | JNJ=2.76 | NEE=2.76  BOT: JPM=2.37 | MSFT=2.33 | AMZN=2.29
   🧭 Regime Start Dist (train resets): high_vol=8 (33.3%), low_vol=5 (20.8%), medium_vol=11 (45.8%)
[CYCLE] Update 17/348 | Step 17,136/500,000 | Episode 20 | Time: 920.4s
   📊 Metrics: Return=+46.44% | Sharpe=1.719 | DD=8.61% | Turnover=17.26%
   🎚️ Intra-Step TAPE: potential=0.2515 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0750 | critic_loss=0.0434 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0217 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7193 | ema=0.5996 | best_ema=0.5996 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03419
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00021_shp1p042_actor.weights.h5 (Sharpe=1.042, MDD=19.21%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00023_shp1p119_actor.weights.h5 (Sharpe=1.119, MDD=18.98%)
[CYCLE] Update 18/348 | Step 18,144/500,000 | Episode 24 | Time: 973.9s
   📊 Metrics: Return=+56.21% | Sharpe=0.758 | DD=27.13% | Turnover=18.02%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0726 | critic_loss=0.0523 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0261 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7069 | ema=0.6103 | best_ema=0.6103 | no_improve=0
   🔬 Alpha Diversity: mean=1.66 | std=0.30 | range=[0.74, 3.34] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.80 | XOM=1.74 | JNJ=1.69  BOT: JPM=1.57 | MSFT=1.55 | AMZN=1.50
   🧭 Regime Start Dist (train resets): high_vol=9 (32.1%), low_vol=7 (25.0%), medium_vol=12 (42.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.066) | TAPE=0.3489
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00310) | SPY bonus=0.007 (SPY ret=-0.00082)
   🔐 Lagrangian CVaR: λ=0.0016 | penalty=-0.0000 | rolling_cvar=-0.03063
[CYCLE] Update 19/348 | Step 19,152/500,000 | Episode 24 | Time: 1027.8s
   📊 Metrics: Return=-0.35% | Sharpe=-0.102 | DD=16.93% | Turnover=22.42%
   🎚️ Intra-Step TAPE: potential=0.3142 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0668 | critic_loss=0.0303 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0151 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1020 | ema=0.5391 | best_ema=0.5391 | no_improve=0
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1081.5s
   📊 Metrics: Return=+0.92% | Sharpe=0.021 | DD=25.89% | Turnover=22.78%
   🎚️ Intra-Step TAPE: potential=0.2279 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0701 | critic_loss=0.0608 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0304 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0005 | ema=0.4851 | best_ema=0.4851 | no_improve=0
   🔬 Alpha Diversity: mean=1.12 | std=0.36 | range=[0.62, 3.34] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.11 | XOM=1.10 | JNJ=1.09  BOT: CAT=0.97 | AMZN=0.94 | NVDA=0.91
   🧭 Regime Start Dist (train resets): high_vol=9 (32.1%), low_vol=7 (25.0%), medium_vol=12 (42.9%)
   🔐 Lagrangian CVaR: λ=0.0004 | penalty=-0.0000 | rolling_cvar=-0.03301
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00026_shp0p728_actor.weights.h5 (Sharpe=0.728, MDD=16.41%)
[CYCLE] Update 21/348 | Step 21,168/500,000 | Episode 28 | Time: 1134.4s
   📊 Metrics: Return=+50.83% | Sharpe=0.732 | DD=26.24% | Turnover=23.84%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0705 | critic_loss=0.0452 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0226 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7027 | ema=0.5069 | best_ema=0.5069 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.057) | TAPE=0.3364
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00314) | SPY bonus=0.021 (SPY ret=-0.01111)
   🔐 Lagrangian CVaR: λ=0.0030 | penalty=-0.0000 | rolling_cvar=-0.02829
[CYCLE] Update 22/348 | Step 22,176/500,000 | Episode 28 | Time: 1187.2s
   📊 Metrics: Return=+16.49% | Sharpe=1.321 | DD=8.76% | Turnover=24.44%
   🎚️ Intra-Step TAPE: potential=0.2263 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0661 | critic_loss=0.0500 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0250 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3210 | ema=0.5883 | best_ema=0.5883 | no_improve=0
   🔬 Alpha Diversity: mean=1.04 | std=0.29 | range=[0.55, 3.04] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.05 | PG=1.05 | JNJ=1.04  BOT: CAT=0.90 | AMZN=0.86 | NVDA=0.82
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=9 (28.1%), medium_vol=13 (40.6%)
[CYCLE] Update 23/348 | Step 23,184/500,000 | Episode 28 | Time: 1240.6s
   📊 Metrics: Return=+16.84% | Sharpe=0.542 | DD=16.63% | Turnover=24.74%
   🎚️ Intra-Step TAPE: potential=0.6740 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0668 | critic_loss=0.0655 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0327 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5424 | ema=0.5837 | best_ema=0.5837 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01960
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00030_shp0p949_actor.weights.h5 (Sharpe=0.949, MDD=24.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00031_shp0p801_actor.weights.h5 (Sharpe=0.801, MDD=16.42%)
[CYCLE] Update 24/348 | Step 24,192/500,000 | Episode 32 | Time: 1293.2s
   📊 Metrics: Return=+30.56% | Sharpe=0.474 | DD=25.31% | Turnover=24.53%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0656 | critic_loss=0.0519 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0259 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4665 | ema=0.5720 | best_ema=0.5720 | no_improve=0
   🔬 Alpha Diversity: mean=1.05 | std=0.28 | range=[0.64, 2.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.11 | JNJ=1.05 | PG=1.05  BOT: AMZN=0.92 | CAT=0.92 | NVDA=0.87
   🧭 Regime Start Dist (train resets): high_vol=10 (27.8%), low_vol=13 (36.1%), medium_vol=13 (36.1%)
   🔒 Drawdown λ snapshot=0.044 (peak 0.044, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.044) | TAPE=0.2761
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.02332) | SPY bonus=0.020 (SPY ret=-0.02732)
   🔐 Lagrangian CVaR: λ=0.0002 | penalty=-0.0000 | rolling_cvar=-0.02849
[CYCLE] Update 25/348 | Step 25,200/500,000 | Episode 32 | Time: 1345.9s
   📊 Metrics: Return=+13.61% | Sharpe=1.071 | DD=7.37% | Turnover=25.06%
   🎚️ Intra-Step TAPE: potential=0.6800 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0679 | critic_loss=0.0461 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0230 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0712 | ema=0.6219 | best_ema=0.6219 | no_improve=0
[CYCLE] Update 26/348 | Step 26,208/500,000 | Episode 32 | Time: 1399.0s
   📊 Metrics: Return=+13.24% | Sharpe=0.413 | DD=15.29% | Turnover=25.52%
   🎚️ Intra-Step TAPE: potential=0.2310 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0660 | critic_loss=0.0414 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0207 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4131 | ema=0.6010 | best_ema=0.6010 | no_improve=0
   🔬 Alpha Diversity: mean=1.15 | std=0.47 | range=[0.67, 3.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.11 | JNJ=1.07 | XOM=1.06  BOT: CAT=0.92 | AMZN=0.92 | NVDA=0.89
   🧭 Regime Start Dist (train resets): high_vol=10 (27.8%), low_vol=13 (36.1%), medium_vol=13 (36.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00036_shp0p830_actor.weights.h5 (Sharpe=0.830, MDD=16.21%)
[CYCLE] Update 27/348 | Step 27,216/500,000 | Episode 36 | Time: 1453.4s
   📊 Metrics: Return=+36.86% | Sharpe=0.830 | DD=16.21% | Turnover=24.24%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0672 | critic_loss=0.0513 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0256 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8302 | ema=0.6239 | best_ema=0.6239 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4029
   🔐 Lagrangian CVaR: λ=0.0005 | penalty=-0.0000 | rolling_cvar=-0.01794
[CYCLE] Update 28/348 | Step 28,224/500,000 | Episode 36 | Time: 1506.7s
   📊 Metrics: Return=+2.56% | Sharpe=0.108 | DD=10.57% | Turnover=24.31%
   🎚️ Intra-Step TAPE: potential=0.2322 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0649 | critic_loss=0.0267 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0134 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1082 | ema=0.5724 | best_ema=0.5724 | no_improve=0
   🔬 Alpha Diversity: mean=1.05 | std=0.32 | range=[0.68, 2.44] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.04 | JNJ=0.99 | PG=0.99  BOT: NVDA=0.91 | CAT=0.90 | AMZN=0.89
   🧭 Regime Start Dist (train resets): high_vol=10 (25.0%), low_vol=16 (40.0%), medium_vol=14 (35.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02285
[CYCLE] Update 29/348 | Step 29,232/500,000 | Episode 36 | Time: 1560.0s
   📊 Metrics: Return=+14.90% | Sharpe=0.467 | DD=18.53% | Turnover=24.28%
   🎚️ Intra-Step TAPE: potential=0.7178 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0660 | critic_loss=0.0286 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0143 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4665 | ema=0.5618 | best_ema=0.5618 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00038_shp0p741_actor.weights.h5 (Sharpe=0.741, MDD=17.47%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 1613.4s
   📊 Metrics: Return=+23.42% | Sharpe=0.365 | DD=26.21% | Turnover=24.42%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0614 | critic_loss=0.0553 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0277 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3355 | ema=0.5392 | best_ema=0.5392 | no_improve=0
   🔬 Alpha Diversity: mean=1.08 | std=0.24 | range=[0.65, 2.22] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.18 | PG=1.11 | JNJ=1.08  BOT: JPM=0.97 | CAT=0.94 | NVDA=0.93
   🧭 Regime Start Dist (train resets): high_vol=11 (25.0%), low_vol=19 (43.2%), medium_vol=14 (31.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 30 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.052) | TAPE=0.2516
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.01438) | SPY bonus=0.006 (SPY ret=0.00860)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02928
[CYCLE] Update 31/348 | Step 31,248/500,000 | Episode 40 | Time: 1667.1s
   📊 Metrics: Return=+3.95% | Sharpe=0.210 | DD=16.70% | Turnover=23.86%
   🎚️ Intra-Step TAPE: potential=0.7381 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0667 | critic_loss=0.0276 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2099 | ema=0.5062 | best_ema=0.5062 | no_improve=0
[CYCLE] Update 32/348 | Step 32,256/500,000 | Episode 40 | Time: 1720.1s
   📊 Metrics: Return=+10.38% | Sharpe=0.249 | DD=26.06% | Turnover=23.98%
   🎚️ Intra-Step TAPE: potential=0.2184 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0635 | critic_loss=0.0262 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0131 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2231 | ema=0.4779 | best_ema=0.4779 | no_improve=0
   🔬 Alpha Diversity: mean=0.89 | std=0.28 | range=[0.50, 2.45] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=0.89 | GLD=0.88 | PG=0.87  BOT: AMZN=0.75 | CAT=0.73 | NVDA=0.72
   🧭 Regime Start Dist (train resets): high_vol=11 (25.0%), low_vol=19 (43.2%), medium_vol=14 (31.8%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01882
[CYCLE] Update 33/348 | Step 33,264/500,000 | Episode 44 | Time: 1772.9s
   📊 Metrics: Return=+27.41% | Sharpe=0.450 | DD=26.20% | Turnover=24.95%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0636 | critic_loss=0.0358 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0179 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4211 | ema=0.4722 | best_ema=0.4722 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.071) | TAPE=0.2571
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02670
[CYCLE] Update 34/348 | Step 34,272/500,000 | Episode 44 | Time: 1826.8s
   📊 Metrics: Return=+0.96% | Sharpe=-0.025 | DD=9.75% | Turnover=25.67%
   🎚️ Intra-Step TAPE: potential=0.2223 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0669 | critic_loss=0.0396 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0198 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0246 | ema=0.4226 | best_ema=0.4226 | no_improve=0
   🔬 Alpha Diversity: mean=1.05 | std=0.15 | range=[0.69, 1.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.18 | NEE=1.12 | JNJ=1.07  BOT: AMZN=0.95 | CAT=0.94 | NVDA=0.91
   🧭 Regime Start Dist (train resets): high_vol=11 (22.9%), low_vol=21 (43.8%), medium_vol=16 (33.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 34 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02214
[CYCLE] Update 35/348 | Step 35,280/500,000 | Episode 44 | Time: 1880.2s
   📊 Metrics: Return=+15.53% | Sharpe=0.484 | DD=16.38% | Turnover=25.05%
   🎚️ Intra-Step TAPE: potential=0.6742 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0627 | critic_loss=0.0269 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0134 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4837 | ema=0.4287 | best_ema=0.4287 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00046_shp0p779_actor.weights.h5 (Sharpe=0.779, MDD=20.06%)
[CYCLE] Update 36/348 | Step 36,288/500,000 | Episode 48 | Time: 1932.7s
   📊 Metrics: Return=+25.76% | Sharpe=0.396 | DD=26.22% | Turnover=23.63%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0648 | critic_loss=0.0393 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0197 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3662 | ema=0.4224 | best_ema=0.4224 | no_improve=0
   🔬 Alpha Diversity: mean=1.63 | std=0.27 | range=[0.93, 2.23] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.96 | PG=1.84 | JNJ=1.78  BOT: JPM=1.50 | CAT=1.46 | NVDA=1.45
   🧭 Regime Start Dist (train resets): high_vol=14 (26.9%), low_vol=22 (42.3%), medium_vol=16 (30.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.054) | TAPE=0.2577
   🔐 Lagrangian CVaR: λ=0.0069 | penalty=-0.0000 | rolling_cvar=-0.03001
[CYCLE] Update 37/348 | Step 37,296/500,000 | Episode 48 | Time: 1985.7s
   📊 Metrics: Return=+27.49% | Sharpe=2.474 | DD=3.18% | Turnover=20.15%
   🎚️ Intra-Step TAPE: potential=0.6399 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0647 | critic_loss=0.0147 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0073 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4739 | ema=0.6276 | best_ema=0.6276 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01963
[CYCLE] Update 38/348 | Step 38,304/500,000 | Episode 48 | Time: 2039.1s
   📊 Metrics: Return=+62.97% | Sharpe=2.341 | DD=8.47% | Turnover=19.59%
   🎚️ Intra-Step TAPE: potential=0.4929 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0643 | critic_loss=0.0254 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0127 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3409 | ema=0.7989 | best_ema=0.7989 | no_improve=0
   🔬 Alpha Diversity: mean=1.68 | std=0.20 | range=[1.06, 2.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.82 | PG=1.76 | NEE=1.74  BOT: CAT=1.58 | NVDA=1.57 | JPM=1.57
   🧭 Regime Start Dist (train resets): high_vol=14 (26.9%), low_vol=22 (42.3%), medium_vol=16 (30.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 38 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.03378
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00049_shp1p319_actor.weights.h5 (Sharpe=1.319, MDD=16.86%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00050_shp1p236_actor.weights.h5 (Sharpe=1.236, MDD=15.62%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00051_shp0p750_actor.weights.h5 (Sharpe=0.750, MDD=24.73%)
[CYCLE] Update 39/348 | Step 39,312/500,000 | Episode 52 | Time: 2091.9s
   📊 Metrics: Return=+63.55% | Sharpe=0.861 | DD=26.24% | Turnover=20.29%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0634 | critic_loss=0.0280 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0140 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8316 | ema=0.8022 | best_ema=0.8022 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.049) | TAPE=0.3990
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02904
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 2144.5s
   📊 Metrics: Return=+28.15% | Sharpe=2.467 | DD=3.30% | Turnover=23.19%
   🎚️ Intra-Step TAPE: potential=0.7561 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0633 | critic_loss=0.0420 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0210 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4673 | ema=0.9687 | best_ema=0.9687 | no_improve=0
   🔬 Alpha Diversity: mean=1.36 | std=0.27 | range=[0.73, 2.30] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.39 | NEE=1.39 | JNJ=1.35  BOT: JPM=1.23 | CAT=1.21 | NVDA=1.10
   🧭 Regime Start Dist (train resets): high_vol=16 (28.6%), low_vol=23 (41.1%), medium_vol=17 (30.4%)
[CYCLE] Update 41/348 | Step 41,328/500,000 | Episode 52 | Time: 2198.3s
   📊 Metrics: Return=+62.59% | Sharpe=2.736 | DD=3.30% | Turnover=22.77%
   🎚️ Intra-Step TAPE: potential=0.7413 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0580 | critic_loss=0.0330 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0165 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.7361 | ema=1.1454 | best_ema=1.1454 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00053_shp1p092_actor.weights.h5 (Sharpe=1.092, MDD=16.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00054_shp0p865_actor.weights.h5 (Sharpe=0.865, MDD=15.29%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00055_shp0p979_actor.weights.h5 (Sharpe=0.979, MDD=18.21%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00056_shp0p847_actor.weights.h5 (Sharpe=0.847, MDD=19.11%)
[CYCLE] Update 42/348 | Step 42,336/500,000 | Episode 56 | Time: 2251.9s
   📊 Metrics: Return=+38.05% | Sharpe=0.847 | DD=19.11% | Turnover=22.47%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0643 | critic_loss=0.0426 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0213 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8469 | ema=1.1156 | best_ema=1.1156 | no_improve=0
   🔬 Alpha Diversity: mean=1.55 | std=0.51 | range=[0.74, 3.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.64 | PG=1.56 | GLD=1.53  BOT: AMZN=1.29 | CAT=1.19 | NVDA=1.13
   🧭 Regime Start Dist (train resets): high_vol=16 (26.7%), low_vol=23 (38.3%), medium_vol=21 (35.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.003) | TAPE=0.4031
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00085) | SPY bonus=0.006 (SPY ret=-0.00107)
[CYCLE] Update 43/348 | Step 43,344/500,000 | Episode 56 | Time: 2305.5s
   📊 Metrics: Return=+23.24% | Sharpe=2.627 | DD=2.41% | Turnover=21.38%
   🎚️ Intra-Step TAPE: potential=0.7575 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0592 | critic_loss=0.0266 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0133 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.6274 | ema=1.2668 | best_ema=1.2668 | no_improve=0
[CYCLE] Update 44/348 | Step 44,352/500,000 | Episode 56 | Time: 2358.7s
   📊 Metrics: Return=+26.86% | Sharpe=1.043 | DD=9.90% | Turnover=21.28%
   🎚️ Intra-Step TAPE: potential=0.2286 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0600 | critic_loss=0.0613 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0306 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0427 | ema=1.2444 | best_ema=1.2444 | no_improve=0
   🔬 Alpha Diversity: mean=1.40 | std=0.31 | range=[0.99, 2.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.43 | GLD=1.39 | JNJ=1.33  BOT: AMZN=1.24 | NVDA=1.23 | CAT=1.20
   🧭 Regime Start Dist (train resets): high_vol=16 (26.7%), low_vol=23 (38.3%), medium_vol=21 (35.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00057_shp0p925_actor.weights.h5 (Sharpe=0.925, MDD=16.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00058_shp0p890_actor.weights.h5 (Sharpe=0.890, MDD=14.86%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00059_shp1p107_actor.weights.h5 (Sharpe=1.107, MDD=14.89%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00060_shp0p794_actor.weights.h5 (Sharpe=0.794, MDD=18.13%)
[CYCLE] Update 45/348 | Step 45,360/500,000 | Episode 60 | Time: 2411.9s
   📊 Metrics: Return=+35.06% | Sharpe=0.794 | DD=18.13% | Turnover=22.10%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0608 | critic_loss=0.0442 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0221 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7936 | ema=1.1993 | best_ema=1.1993 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.002) | TAPE=0.3778
[CYCLE] Update 46/348 | Step 46,368/500,000 | Episode 60 | Time: 2464.2s
   📊 Metrics: Return=+4.06% | Sharpe=0.214 | DD=14.65% | Turnover=23.62%
   🎚️ Intra-Step TAPE: potential=0.2395 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0600 | critic_loss=0.0359 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0180 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2143 | ema=1.1008 | best_ema=1.1008 | no_improve=0
   🔬 Alpha Diversity: mean=1.15 | std=0.22 | range=[0.67, 2.04] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.29 | PG=1.22 | JNJ=1.14  BOT: AMZN=1.03 | CAT=0.95 | NVDA=0.90
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=23 (35.9%), medium_vol=23 (35.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 46 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01530
[CYCLE] Update 47/348 | Step 47,376/500,000 | Episode 60 | Time: 2517.3s
   📊 Metrics: Return=+33.57% | Sharpe=0.696 | DD=23.30% | Turnover=23.73%
   🎚️ Intra-Step TAPE: potential=0.6003 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0642 | critic_loss=0.0441 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0221 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6957 | ema=1.0603 | best_ema=1.0603 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0141 | penalty=-0.0001 | rolling_cvar=-0.03245
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00061_shp0p749_actor.weights.h5 (Sharpe=0.749, MDD=23.30%)
[CYCLE] Update 48/348 | Step 48,384/500,000 | Episode 64 | Time: 2570.6s
   📊 Metrics: Return=+82.68% | Sharpe=1.090 | DD=25.36% | Turnover=23.82%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0585 | critic_loss=0.0291 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0145 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0811 | ema=1.0624 | best_ema=1.0624 | no_improve=0
   🔬 Alpha Diversity: mean=1.06 | std=0.16 | range=[0.72, 1.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.13 | PG=1.11 | GLD=1.09  BOT: AMZN=0.98 | JPM=0.97 | XOM=0.95
   🧭 Regime Start Dist (train resets): high_vol=19 (27.9%), low_vol=24 (35.3%), medium_vol=25 (36.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 48 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.047) | TAPE=0.4920
   🔐 Lagrangian CVaR: λ=0.0318 | penalty=-0.0003 | rolling_cvar=-0.02751
[CYCLE] Update 49/348 | Step 49,392/500,000 | Episode 64 | Time: 2623.3s
   📊 Metrics: Return=+26.02% | Sharpe=1.900 | DD=5.46% | Turnover=24.86%
   🎚️ Intra-Step TAPE: potential=0.6419 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0608 | critic_loss=0.0285 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0142 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.9005 | ema=1.1462 | best_ema=1.1462 | no_improve=0
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 2676.4s
   📊 Metrics: Return=+60.74% | Sharpe=2.338 | DD=5.46% | Turnover=24.48%
   🎚️ Intra-Step TAPE: potential=0.7544 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0581 | critic_loss=0.0254 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0127 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3383 | ema=1.2654 | best_ema=1.2654 | no_improve=0
   🔬 Alpha Diversity: mean=1.10 | std=0.08 | range=[0.77, 1.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.13 | MSFT=1.11 | XOM=1.10  BOT: JPM=1.07 | GLD=1.07 | CAT=1.06
   🧭 Regime Start Dist (train resets): high_vol=19 (27.9%), low_vol=24 (35.3%), medium_vol=25 (36.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 50 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00065_shp1p087_actor.weights.h5 (Sharpe=1.087, MDD=16.72%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00066_shp1p231_actor.weights.h5 (Sharpe=1.231, MDD=17.21%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00067_shp0p854_actor.weights.h5 (Sharpe=0.854, MDD=14.79%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00068_shp1p029_actor.weights.h5 (Sharpe=1.029, MDD=17.83%)
[CYCLE] Update 51/348 | Step 51,408/500,000 | Episode 68 | Time: 2730.1s
   📊 Metrics: Return=+49.57% | Sharpe=1.029 | DD=17.83% | Turnover=24.61%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0613 | critic_loss=0.0385 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0193 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0291 | ema=1.2417 | best_ema=1.2417 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.5028
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00079) | SPY bonus=0.000 (SPY ret=-0.00043)
[CYCLE] Update 52/348 | Step 52,416/500,000 | Episode 68 | Time: 2783.1s
   📊 Metrics: Return=+20.72% | Sharpe=1.465 | DD=7.97% | Turnover=21.66%
   🎚️ Intra-Step TAPE: potential=0.2485 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0629 | critic_loss=0.0199 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0100 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4647 | ema=1.2640 | best_ema=1.2640 | no_improve=0
   🔬 Alpha Diversity: mean=1.48 | std=0.21 | range=[0.77, 2.19] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.60 | XOM=1.57 | MSFT=1.57  BOT: JNJ=1.49 | GLD=1.49 | CAT=1.47
   🧭 Regime Start Dist (train resets): high_vol=21 (29.2%), low_vol=25 (34.7%), medium_vol=26 (36.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 52 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 53/348 | Step 53,424/500,000 | Episode 68 | Time: 2836.4s
   📊 Metrics: Return=+23.37% | Sharpe=0.705 | DD=19.21% | Turnover=20.89%
   🎚️ Intra-Step TAPE: potential=0.6325 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0644 | critic_loss=0.0303 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0151 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7050 | ema=1.2081 | best_ema=1.2081 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0010 | penalty=-0.0000 | rolling_cvar=-0.03434
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00070_shp1p004_actor.weights.h5 (Sharpe=1.004, MDD=17.41%)
[CYCLE] Update 54/348 | Step 54,432/500,000 | Episode 72 | Time: 2888.7s
   📊 Metrics: Return=+52.70% | Sharpe=0.708 | DD=28.66% | Turnover=20.14%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0656 | critic_loss=0.0307 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0154 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6202 | ema=1.1493 | best_ema=1.1493 | no_improve=0
   🔬 Alpha Diversity: mean=2.20 | std=0.46 | range=[0.52, 2.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=2.51 | JNJ=2.46 | NEE=2.45  BOT: JPM=2.25 | CAT=2.20 | NVDA=2.16
   🧭 Regime Start Dist (train resets): high_vol=23 (30.3%), low_vol=26 (34.2%), medium_vol=27 (35.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.090) | TAPE=0.3225
   🔐 Lagrangian CVaR: λ=0.0104 | penalty=-0.0001 | rolling_cvar=-0.03171
[CYCLE] Update 55/348 | Step 55,440/500,000 | Episode 72 | Time: 2941.3s
   📊 Metrics: Return=+29.30% | Sharpe=2.204 | DD=3.65% | Turnover=17.03%
   🎚️ Intra-Step TAPE: potential=0.7434 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0602 | critic_loss=0.0225 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0113 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.2040 | ema=1.2548 | best_ema=1.2548 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02065
[CYCLE] Update 56/348 | Step 56,448/500,000 | Episode 72 | Time: 2994.7s
   📊 Metrics: Return=+67.45% | Sharpe=2.582 | DD=3.65% | Turnover=16.95%
   🎚️ Intra-Step TAPE: potential=0.7592 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0635 | critic_loss=0.0259 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0129 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.5816 | ema=1.3875 | best_ema=1.3875 | no_improve=0
   🔬 Alpha Diversity: mean=2.26 | std=0.47 | range=[0.57, 3.13] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.50 | PG=2.49 | XOM=2.49  BOT: JPM=2.31 | CAT=2.30 | NVDA=2.05
   🧭 Regime Start Dist (train resets): high_vol=23 (30.3%), low_vol=26 (34.2%), medium_vol=27 (35.5%)
   🔐 Lagrangian CVaR: λ=0.0056 | penalty=-0.0000 | rolling_cvar=-0.03496
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp1p207_actor.weights.h5 (Sharpe=1.207, MDD=17.13%)
[CYCLE] Update 57/348 | Step 57,456/500,000 | Episode 76 | Time: 3047.7s
   📊 Metrics: Return=+70.76% | Sharpe=0.919 | DD=27.35% | Turnover=17.53%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0570 | critic_loss=0.0298 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0149 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8628 | ema=1.3350 | best_ema=1.3350 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.066) | TAPE=0.4216
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00633) | SPY bonus=0.011 (SPY ret=-0.00870)
   🔐 Lagrangian CVaR: λ=0.0200 | penalty=-0.0002 | rolling_cvar=-0.03002
[CYCLE] Update 58/348 | Step 58,464/500,000 | Episode 76 | Time: 3099.8s
   📊 Metrics: Return=+26.41% | Sharpe=2.231 | DD=8.57% | Turnover=18.32%
   🎚️ Intra-Step TAPE: potential=0.4885 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0581 | critic_loss=0.0277 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.2309 | ema=1.4246 | best_ema=1.4246 | no_improve=0
   🔬 Alpha Diversity: mean=2.02 | std=0.37 | range=[0.96, 2.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.32 | NEE=2.31 | XOM=2.24  BOT: CAT=1.92 | AMZN=1.87 | NVDA=1.77
   🧭 Regime Start Dist (train resets): high_vol=26 (32.5%), low_vol=27 (33.8%), medium_vol=27 (33.8%)
[CYCLE] Update 59/348 | Step 59,472/500,000 | Episode 76 | Time: 3152.0s
   📊 Metrics: Return=+32.13% | Sharpe=1.015 | DD=15.89% | Turnover=18.34%
   🎚️ Intra-Step TAPE: potential=0.5660 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0616 | critic_loss=0.0354 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0177 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0153 | ema=1.3837 | best_ema=1.3837 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0007 | penalty=-0.0000 | rolling_cvar=-0.03474
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 3205.2s
   📊 Metrics: Return=+44.74% | Sharpe=0.621 | DD=27.53% | Turnover=18.77%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0589 | critic_loss=0.0362 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0181 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5598 | ema=1.3013 | best_ema=1.3013 | no_improve=0
   🔬 Alpha Diversity: mean=1.80 | std=0.32 | range=[0.86, 2.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.02 | JNJ=1.96 | PG=1.91  BOT: CAT=1.71 | JPM=1.68 | NVDA=1.55
   🧭 Regime Start Dist (train resets): high_vol=27 (32.1%), low_vol=28 (33.3%), medium_vol=29 (34.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.075) | TAPE=0.2999
   🔐 Lagrangian CVaR: λ=0.0162 | penalty=-0.0001 | rolling_cvar=-0.03123
[CYCLE] Update 61/348 | Step 61,488/500,000 | Episode 80 | Time: 3259.3s
   📊 Metrics: Return=+12.79% | Sharpe=0.952 | DD=8.84% | Turnover=19.08%
   🎚️ Intra-Step TAPE: potential=0.5865 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0559 | critic_loss=0.0208 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0104 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9525 | ema=1.2664 | best_ema=1.2664 | no_improve=0
[CYCLE] Update 62/348 | Step 62,496/500,000 | Episode 80 | Time: 3313.3s
   📊 Metrics: Return=+14.46% | Sharpe=0.445 | DD=15.78% | Turnover=19.23%
   🎚️ Intra-Step TAPE: potential=0.2363 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0604 | critic_loss=0.0423 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0211 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4446 | ema=1.1842 | best_ema=1.1842 | no_improve=0
   🔬 Alpha Diversity: mean=1.96 | std=0.32 | range=[0.67, 2.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.14 | JNJ=2.10 | NEE=2.08  BOT: AMZN=1.84 | CAT=1.82 | NVDA=1.66
   🧭 Regime Start Dist (train resets): high_vol=27 (32.1%), low_vol=28 (33.3%), medium_vol=29 (34.5%)
   🔐 Lagrangian CVaR: λ=0.0008 | penalty=-0.0000 | rolling_cvar=-0.03346
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00082_shp0p890_actor.weights.h5 (Sharpe=0.890, MDD=16.66%)
[CYCLE] Update 63/348 | Step 63,504/500,000 | Episode 84 | Time: 3367.6s
   📊 Metrics: Return=+78.86% | Sharpe=1.040 | DD=28.10% | Turnover=19.91%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0588 | critic_loss=0.0293 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0146 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9654 | ema=1.1623 | best_ema=1.1623 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.075) | TAPE=0.4668
   🔐 Lagrangian CVaR: λ=0.0055 | penalty=-0.0000 | rolling_cvar=-0.02843
[CYCLE] Update 64/348 | Step 64,512/500,000 | Episode 84 | Time: 3421.8s
   📊 Metrics: Return=+22.41% | Sharpe=1.780 | DD=8.05% | Turnover=21.70%
   🎚️ Intra-Step TAPE: potential=0.7316 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0574 | critic_loss=0.0223 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0111 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7798 | ema=1.2241 | best_ema=1.2241 | no_improve=0
   🔬 Alpha Diversity: mean=1.45 | std=0.23 | range=[0.48, 1.87] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.60 | NEE=1.60 | JNJ=1.58  BOT: JPM=1.38 | AMZN=1.35 | NVDA=1.08
   🧭 Regime Start Dist (train resets): high_vol=30 (34.1%), low_vol=29 (33.0%), medium_vol=29 (33.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 64 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 65/348 | Step 65,520/500,000 | Episode 84 | Time: 3475.4s
   📊 Metrics: Return=+48.48% | Sharpe=0.934 | DD=26.83% | Turnover=21.75%
   🎚️ Intra-Step TAPE: potential=0.7251 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0604 | critic_loss=0.0361 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0181 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8903 | ema=1.1907 | best_ema=1.1907 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01217
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00086_shp1p070_actor.weights.h5 (Sharpe=1.070, MDD=19.27%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00087_shp1p050_actor.weights.h5 (Sharpe=1.050, MDD=18.09%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp1p091_actor.weights.h5 (Sharpe=1.091, MDD=16.44%)
[CYCLE] Update 66/348 | Step 66,528/500,000 | Episode 88 | Time: 3528.8s
   📊 Metrics: Return=+51.52% | Sharpe=1.091 | DD=16.44% | Turnover=20.48%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0571 | critic_loss=0.0429 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0214 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0906 | ema=1.1807 | best_ema=1.1807 | no_improve=0
   🔬 Alpha Diversity: mean=1.76 | std=0.29 | range=[0.67, 2.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.96 | JNJ=1.94 | PG=1.93  BOT: AMZN=1.67 | CAT=1.66 | NVDA=1.55
   🧭 Regime Start Dist (train resets): high_vol=30 (32.6%), low_vol=32 (34.8%), medium_vol=30 (32.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5146
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01859
[CYCLE] Update 67/348 | Step 67,536/500,000 | Episode 88 | Time: 3581.1s
   📊 Metrics: Return=+22.49% | Sharpe=2.611 | DD=2.35% | Turnover=19.17%
   🎚️ Intra-Step TAPE: potential=0.7583 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0585 | critic_loss=0.0216 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.6111 | ema=1.3237 | best_ema=1.3237 | no_improve=0
[CYCLE] Update 68/348 | Step 68,544/500,000 | Episode 88 | Time: 3633.5s
   📊 Metrics: Return=+23.83% | Sharpe=0.811 | DD=13.40% | Turnover=19.10%
   🎚️ Intra-Step TAPE: potential=0.2379 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0617 | critic_loss=0.0297 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0148 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8115 | ema=1.2725 | best_ema=1.2725 | no_improve=0
   🔬 Alpha Diversity: mean=1.87 | std=0.32 | range=[0.76, 2.37] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=2.12 | XOM=2.04 | JNJ=2.04  BOT: AMZN=1.74 | CAT=1.72 | NVDA=1.61
   🧭 Regime Start Dist (train resets): high_vol=30 (32.6%), low_vol=32 (34.8%), medium_vol=30 (32.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp0p815_actor.weights.h5 (Sharpe=0.815, MDD=18.86%)
[CYCLE] Update 69/348 | Step 69,552/500,000 | Episode 92 | Time: 3686.5s
   📊 Metrics: Return=+40.43% | Sharpe=0.596 | DD=24.88% | Turnover=19.68%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0606 | critic_loss=0.0363 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0182 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5957 | ema=1.2048 | best_ema=1.2048 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.049) | TAPE=0.2983
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00405) | SPY bonus=0.004 (SPY ret=-0.00634)
   🔐 Lagrangian CVaR: λ=0.0040 | penalty=-0.0000 | rolling_cvar=-0.02960
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 3739.7s
   📊 Metrics: Return=+28.69% | Sharpe=2.572 | DD=3.00% | Turnover=19.94%
   🎚️ Intra-Step TAPE: potential=0.7188 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0570 | critic_loss=0.0158 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0079 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.5724 | ema=1.3416 | best_ema=1.3416 | no_improve=0
   🔬 Alpha Diversity: mean=1.78 | std=0.25 | range=[0.76, 2.28] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.92 | XOM=1.91 | NEE=1.91  BOT: AMZN=1.71 | CAT=1.68 | NVDA=1.63
   🧭 Regime Start Dist (train resets): high_vol=34 (35.4%), low_vol=32 (33.3%), medium_vol=30 (31.2%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01204
[CYCLE] Update 71/348 | Step 71,568/500,000 | Episode 92 | Time: 3793.5s
   📊 Metrics: Return=+58.55% | Sharpe=2.239 | DD=8.23% | Turnover=19.66%
   🎚️ Intra-Step TAPE: potential=0.5287 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0616 | critic_loss=0.0209 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0105 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.2389 | ema=1.4313 | best_ema=1.4313 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01420
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00093_shp1p129_actor.weights.h5 (Sharpe=1.129, MDD=18.50%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00096_shp0p992_actor.weights.h5 (Sharpe=0.992, MDD=18.17%)
[CYCLE] Update 72/348 | Step 72,576/500,000 | Episode 96 | Time: 3846.9s
   📊 Metrics: Return=+47.18% | Sharpe=0.992 | DD=18.17% | Turnover=20.54%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0601 | critic_loss=0.0218 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0109 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9923 | ema=1.3874 | best_ema=1.3874 | no_improve=0
   🔬 Alpha Diversity: mean=1.51 | std=0.19 | range=[0.65, 1.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.62 | NEE=1.60 | PG=1.60  BOT: NVDA=1.48 | AMZN=1.48 | CAT=1.43
   🧭 Regime Start Dist (train resets): high_vol=36 (36.0%), low_vol=32 (32.0%), medium_vol=32 (32.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 72 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.002) | TAPE=0.4827
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00091) | SPY bonus=0.002 (SPY ret=-0.00301)
   🔐 Lagrangian CVaR: λ=0.0002 | penalty=-0.0000 | rolling_cvar=-0.01908
[CYCLE] Update 73/348 | Step 73,584/500,000 | Episode 96 | Time: 3898.3s
   📊 Metrics: Return=+9.25% | Sharpe=0.567 | DD=16.39% | Turnover=21.69%
   🎚️ Intra-Step TAPE: potential=0.7463 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0589 | critic_loss=0.0146 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0073 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5671 | ema=1.3054 | best_ema=1.3054 | no_improve=0
[CYCLE] Update 74/348 | Step 74,592/500,000 | Episode 96 | Time: 3949.7s
   📊 Metrics: Return=+18.37% | Sharpe=0.414 | DD=24.04% | Turnover=21.69%
   🎚️ Intra-Step TAPE: potential=0.2285 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0573 | critic_loss=0.0179 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0090 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4141 | ema=1.2163 | best_ema=1.2163 | no_improve=0
   🔬 Alpha Diversity: mean=1.33 | std=0.16 | range=[0.77, 2.15] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.36 | PG=1.35 | JNJ=1.33  BOT: JPM=1.30 | GLD=1.26 | CAT=1.25
   🧭 Regime Start Dist (train resets): high_vol=36 (36.0%), low_vol=32 (32.0%), medium_vol=32 (32.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 74 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0040 | penalty=-0.0000 | rolling_cvar=-0.01797
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00097_shp0p884_actor.weights.h5 (Sharpe=0.884, MDD=24.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00098_shp0p935_actor.weights.h5 (Sharpe=0.935, MDD=23.98%)
[CYCLE] Update 75/348 | Step 75,600/500,000 | Episode 100 | Time: 4001.9s
   📊 Metrics: Return=+33.23% | Sharpe=0.694 | DD=19.87% | Turnover=21.96%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0558 | critic_loss=0.0231 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0115 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6938 | ema=1.1640 | best_ema=1.1640 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.005) | TAPE=0.3360
   🔐 Lagrangian CVaR: λ=0.0178 | penalty=-0.0002 | rolling_cvar=-0.01977
[CYCLE] Update 76/348 | Step 76,608/500,000 | Episode 100 | Time: 4056.4s
   📊 Metrics: Return=+7.51% | Sharpe=0.460 | DD=10.46% | Turnover=23.70%
   🎚️ Intra-Step TAPE: potential=0.2228 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0580 | critic_loss=0.0137 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0068 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4600 | ema=1.0936 | best_ema=1.0936 | no_improve=0
   🔬 Alpha Diversity: mean=1.06 | std=0.16 | range=[0.52, 1.78] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.09 | NEE=1.08 | PG=1.07  BOT: NVDA=1.02 | CAT=0.97 | GLD=0.97
   🧭 Regime Start Dist (train resets): high_vol=38 (36.5%), low_vol=33 (31.7%), medium_vol=33 (31.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 76 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0067 | penalty=-0.0000 | rolling_cvar=-0.01963
[CYCLE] Update 77/348 | Step 77,616/500,000 | Episode 100 | Time: 4110.3s
   📊 Metrics: Return=+21.75% | Sharpe=0.637 | DD=17.48% | Turnover=23.96%
   🎚️ Intra-Step TAPE: potential=0.6627 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0560 | critic_loss=0.0212 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0106 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6368 | ema=1.0479 | best_ema=1.0479 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0131 | penalty=-0.0001 | rolling_cvar=-0.03450
[CYCLE] Update 78/348 | Step 78,624/500,000 | Episode 104 | Time: 4163.1s
   📊 Metrics: Return=+72.42% | Sharpe=0.948 | DD=26.84% | Turnover=24.20%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0577 | critic_loss=0.0227 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0114 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9037 | ema=1.0335 | best_ema=1.0335 | no_improve=0
   🔬 Alpha Diversity: mean=1.03 | std=0.09 | range=[0.63, 1.31] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.10 | JNJ=1.07 | PG=1.06  BOT: AMZN=1.01 | JPM=1.00 | XOM=1.00
   🧭 Regime Start Dist (train resets): high_vol=39 (36.1%), low_vol=35 (32.4%), medium_vol=34 (31.5%)
   [WARN]  WARNING: Alpha std < 0.25 after 78 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.054) | TAPE=0.4325
   🔐 Lagrangian CVaR: λ=0.0370 | penalty=-0.0005 | rolling_cvar=-0.02944
[CYCLE] Update 79/348 | Step 79,632/500,000 | Episode 104 | Time: 4216.0s
   📊 Metrics: Return=+13.86% | Sharpe=0.947 | DD=9.71% | Turnover=24.08%
   🎚️ Intra-Step TAPE: potential=0.7058 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0599 | critic_loss=0.0193 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0096 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9470 | ema=1.0249 | best_ema=1.0249 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0065 | penalty=-0.0000 | rolling_cvar=-0.02037
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 4270.0s
   📊 Metrics: Return=+17.42% | Sharpe=0.509 | DD=17.23% | Turnover=24.32%
   🎚️ Intra-Step TAPE: potential=0.2974 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0599 | critic_loss=0.0225 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0113 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5087 | ema=0.9732 | best_ema=0.9732 | no_improve=0
   🔬 Alpha Diversity: mean=1.04 | std=0.12 | range=[0.56, 1.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.18 | MSFT=1.09 | AMZN=1.06  BOT: XOM=1.04 | CAT=1.04 | GLD=0.97
   🧭 Regime Start Dist (train resets): high_vol=39 (36.1%), low_vol=35 (32.4%), medium_vol=34 (31.5%)
   [WARN]  WARNING: Alpha std < 0.25 after 80 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03642
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00106_shp0p883_actor.weights.h5 (Sharpe=0.883, MDD=18.78%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00107_shp1p127_actor.weights.h5 (Sharpe=1.127, MDD=21.09%)
[CYCLE] Update 81/348 | Step 81,648/500,000 | Episode 108 | Time: 4324.2s
   📊 Metrics: Return=+46.89% | Sharpe=0.658 | DD=30.04% | Turnover=24.02%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0599 | critic_loss=0.0271 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0136 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5373 | ema=0.9296 | best_ema=0.9296 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.105) | TAPE=0.3027
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01923) | SPY bonus=0.009 (SPY ret=-0.01946)
   🔐 Lagrangian CVaR: λ=0.0017 | penalty=-0.0000 | rolling_cvar=-0.03088
[CYCLE] Update 82/348 | Step 82,656/500,000 | Episode 108 | Time: 4378.7s
   📊 Metrics: Return=+25.67% | Sharpe=2.319 | DD=4.03% | Turnover=25.23%
   🎚️ Intra-Step TAPE: potential=0.7423 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0602 | critic_loss=0.0183 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0092 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3186 | ema=1.0685 | best_ema=1.0685 | no_improve=0
   🔬 Alpha Diversity: mean=0.89 | std=0.10 | range=[0.65, 1.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.06 | AMZN=0.93 | CAT=0.91  BOT: NEE=0.86 | PG=0.85 | GLD=0.78
   🧭 Regime Start Dist (train resets): high_vol=39 (34.8%), low_vol=36 (32.1%), medium_vol=37 (33.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 82 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02023
[CYCLE] Update 83/348 | Step 83,664/500,000 | Episode 108 | Time: 4433.0s
   📊 Metrics: Return=+47.45% | Sharpe=1.665 | DD=8.27% | Turnover=25.42%
   🎚️ Intra-Step TAPE: potential=0.2942 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0580 | critic_loss=0.0189 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0094 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6648 | ema=1.1282 | best_ema=1.1282 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00109_shp0p930_actor.weights.h5 (Sharpe=0.930, MDD=16.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00110_shp1p171_actor.weights.h5 (Sharpe=1.171, MDD=20.41%)
[CYCLE] Update 84/348 | Step 84,672/500,000 | Episode 112 | Time: 4487.1s
   📊 Metrics: Return=+28.31% | Sharpe=0.427 | DD=25.89% | Turnover=25.40%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0587 | critic_loss=0.0202 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0101 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4054 | ema=1.0559 | best_ema=1.0559 | no_improve=0
   🔬 Alpha Diversity: mean=1.00 | std=0.10 | range=[0.64, 1.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.08 | MSFT=1.06 | XOM=1.04  BOT: NEE=1.01 | CAT=1.00 | GLD=0.94
   🧭 Regime Start Dist (train resets): high_vol=39 (33.6%), low_vol=38 (32.8%), medium_vol=39 (33.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 84 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.052) | TAPE=0.2612
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00140) | SPY bonus=0.012 (SPY ret=-0.00185)
   🔐 Lagrangian CVaR: λ=0.0002 | penalty=-0.0000 | rolling_cvar=-0.03033
[CYCLE] Update 85/348 | Step 85,680/500,000 | Episode 112 | Time: 4542.0s
   📊 Metrics: Return=+23.02% | Sharpe=2.195 | DD=3.09% | Turnover=24.22%
   🎚️ Intra-Step TAPE: potential=0.6898 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0599 | critic_loss=0.0138 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0069 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1954 | ema=1.1698 | best_ema=1.1698 | no_improve=0
[CYCLE] Update 86/348 | Step 86,688/500,000 | Episode 112 | Time: 4596.5s
   📊 Metrics: Return=+49.37% | Sharpe=1.816 | DD=7.40% | Turnover=24.26%
   🎚️ Intra-Step TAPE: potential=0.7422 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0584 | critic_loss=0.0129 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0065 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8156 | ema=1.2344 | best_ema=1.2344 | no_improve=0
   🔬 Alpha Diversity: mean=1.09 | std=0.13 | range=[0.69, 1.72] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.24 | MSFT=1.14 | NEE=1.13  BOT: JNJ=1.08 | XOM=1.06 | GLD=0.99
   🧭 Regime Start Dist (train resets): high_vol=39 (33.6%), low_vol=38 (32.8%), medium_vol=39 (33.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 86 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00113_shp1p019_actor.weights.h5 (Sharpe=1.019, MDD=17.61%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00114_shp1p075_actor.weights.h5 (Sharpe=1.075, MDD=19.13%)
[CYCLE] Update 87/348 | Step 87,696/500,000 | Episode 116 | Time: 4650.4s
   📊 Metrics: Return=+40.02% | Sharpe=0.562 | DD=27.49% | Turnover=23.99%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0568 | critic_loss=0.0171 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0086 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5024 | ema=1.1612 | best_ema=1.1612 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.065) | TAPE=0.2882
   🔐 Lagrangian CVaR: λ=0.0004 | penalty=-0.0000 | rolling_cvar=-0.03150
[CYCLE] Update 88/348 | Step 88,704/500,000 | Episode 116 | Time: 4705.0s
   📊 Metrics: Return=-7.70% | Sharpe=-0.538 | DD=17.30% | Turnover=25.10%
   🎚️ Intra-Step TAPE: potential=0.2409 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0578 | critic_loss=0.0134 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0067 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5380 | ema=0.9913 | best_ema=0.9913 | no_improve=0
   🔬 Alpha Diversity: mean=0.87 | std=0.14 | range=[0.52, 1.45] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.03 | MSFT=0.92 | NEE=0.91  BOT: PG=0.84 | XOM=0.81 | GLD=0.80
   🧭 Regime Start Dist (train resets): high_vol=40 (33.3%), low_vol=39 (32.5%), medium_vol=41 (34.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 88 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01323
[CYCLE] Update 89/348 | Step 89,712/500,000 | Episode 116 | Time: 4759.5s
   📊 Metrics: Return=+10.54% | Sharpe=0.294 | DD=17.30% | Turnover=26.39%
   🎚️ Intra-Step TAPE: potential=0.7473 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0602 | critic_loss=0.0122 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0061 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2942 | ema=0.9216 | best_ema=0.9216 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00118_shp0p879_actor.weights.h5 (Sharpe=0.879, MDD=24.97%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00119_shp0p756_actor.weights.h5 (Sharpe=0.756, MDD=15.92%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00120_shp1p069_actor.weights.h5 (Sharpe=1.069, MDD=19.72%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 4813.7s
   📊 Metrics: Return=+54.82% | Sharpe=1.069 | DD=19.72% | Turnover=26.24%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0599 | critic_loss=0.0195 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0097 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0689 | ema=0.9363 | best_ema=0.9363 | no_improve=0
   🔬 Alpha Diversity: mean=0.69 | std=0.08 | range=[0.53, 1.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.76 | NEE=0.73 | MSFT=0.72  BOT: JPM=0.65 | CAT=0.64 | XOM=0.63
   🧭 Regime Start Dist (train resets): high_vol=43 (34.7%), low_vol=40 (32.3%), medium_vol=41 (33.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 90 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.006) | TAPE=0.5051
   🔐 Lagrangian CVaR: λ=0.0006 | penalty=-0.0000 | rolling_cvar=-0.02060

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps
[CYCLE] Update 91/348 | Step 91,728/500,000 | Episode 120 | Time: 4867.4s
   📊 Metrics: Return=+21.64% | Sharpe=1.529 | DD=7.23% | Turnover=27.69%
   🎚️ Intra-Step TAPE: potential=0.7273 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0595 | critic_loss=0.0108 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5289 | ema=0.9956 | best_ema=0.9956 | no_improve=0

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps
[CYCLE] Update 92/348 | Step 92,736/500,000 | Episode 120 | Time: 4921.2s
   📊 Metrics: Return=+59.61% | Sharpe=1.095 | DD=22.99% | Turnover=26.92%
   🎚️ Intra-Step TAPE: potential=0.7057 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0594 | critic_loss=0.0189 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0094 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0955 | ema=1.0056 | best_ema=1.0056 | no_improve=0
   🔬 Alpha Diversity: mean=0.75 | std=0.09 | range=[0.56, 1.37] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.88 | MSFT=0.79 | PG=0.78  BOT: CAT=0.73 | GLD=0.71 | XOM=0.68
   🧭 Regime Start Dist (train resets): high_vol=43 (34.7%), low_vol=40 (32.3%), medium_vol=41 (33.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 92 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0013 | penalty=-0.0000 | rolling_cvar=-0.01776

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps
[CYCLE] Update 93/348 | Step 93,744/500,000 | Episode 120 | Time: 4975.8s
   📊 Metrics: Return=+83.31% | Sharpe=1.057 | DD=22.99% | Turnover=26.90%
   🎚️ Intra-Step TAPE: potential=0.5411 | delta_reward=-0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0571 | critic_loss=0.0183 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0092 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0570 | ema=1.0107 | best_ema=1.0107 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0170 | penalty=-0.0001 | rolling_cvar=-0.01982
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00121_shp1p080_actor.weights.h5 (Sharpe=1.080, MDD=22.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00124_shp0p977_actor.weights.h5 (Sharpe=0.977, MDD=17.55%)

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps
[CYCLE] Update 94/348 | Step 94,752/500,000 | Episode 124 | Time: 5029.9s
   📊 Metrics: Return=+56.06% | Sharpe=0.977 | DD=17.55% | Turnover=26.92%
   🎚️ Intra-Step TAPE: potential=0.2372 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0558 | critic_loss=0.0185 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0092 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9769 | ema=1.0073 | best_ema=1.0073 | no_improve=0
   🔬 Alpha Diversity: mean=0.66 | std=0.19 | range=[0.48, 1.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.67 | MSFT=0.62 | AMZN=0.62  BOT: XOM=0.60 | JNJ=0.59 | GLD=0.55
   🧭 Regime Start Dist (train resets): high_vol=44 (34.4%), low_vol=42 (32.8%), medium_vol=42 (32.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 94 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.014, dd 5.76% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.4765
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00152) | SPY bonus=0.001 (SPY ret=-0.00111)
   🔐 Lagrangian CVaR: λ=0.0064 | penalty=-0.0001 | rolling_cvar=-0.01136

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps
[CYCLE] Update 95/348 | Step 95,760/500,000 | Episode 124 | Time: 5082.7s
   📊 Metrics: Return=+6.98% | Sharpe=0.175 | DD=25.49% | Turnover=28.84%
   🎚️ Intra-Step TAPE: potential=0.6662 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0594 | critic_loss=0.0163 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0081 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1629 | ema=0.9229 | best_ema=0.9229 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01615

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps
[CYCLE] Update 96/348 | Step 96,768/500,000 | Episode 124 | Time: 5134.9s
   📊 Metrics: Return=+33.91% | Sharpe=0.520 | DD=25.49% | Turnover=28.26%
   🎚️ Intra-Step TAPE: potential=0.6793 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0584 | critic_loss=0.0205 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0103 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5088 | ema=0.8815 | best_ema=0.8815 | no_improve=0
   🔬 Alpha Diversity: mean=0.80 | std=0.30 | range=[0.54, 2.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.78 | NEE=0.72 | JNJ=0.72  BOT: CAT=0.70 | JPM=0.69 | XOM=0.68
   🧭 Regime Start Dist (train resets): high_vol=44 (34.4%), low_vol=42 (32.8%), medium_vol=42 (32.8%)
   🔐 Lagrangian CVaR: λ=0.0082 | penalty=-0.0000 | rolling_cvar=-0.01810

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps
[CYCLE] Update 97/348 | Step 97,776/500,000 | Episode 126 | Time: 5187.7s
   📊 Metrics: Return=+48.06% | Sharpe=0.640 | DD=23.22% | Turnover=27.77%
   🎚️ Intra-Step TAPE: potential=0.7478 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0559 | critic_loss=0.0377 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0188 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6396 | ema=0.8573 | best_ema=0.8573 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.60% / trig 16.50%) | terminal=0.000 (peak 0.032) | TAPE=0.3128
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00063) | SPY bonus=0.006 (SPY ret=-0.00252)
   🔐 Lagrangian CVaR: λ=0.0035 | penalty=-0.0000 | rolling_cvar=-0.02551
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00128_shp0p742_actor.weights.h5 (Sharpe=0.742, MDD=24.47%)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps
[CYCLE] Update 98/348 | Step 98,784/500,000 | Episode 128 | Time: 5240.8s
   📊 Metrics: Return=+61.67% | Sharpe=0.742 | DD=24.47% | Turnover=27.24%
   🎚️ Intra-Step TAPE: potential=0.2391 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0623 | critic_loss=0.0250 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7421 | ema=0.8458 | best_ema=0.8458 | no_improve=0
   🔬 Alpha Diversity: mean=1.19 | std=0.15 | range=[0.81, 1.92] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.41 | AMZN=1.22 | MSFT=1.18  BOT: PG=1.13 | XOM=1.13 | GLD=1.07
   🧭 Regime Start Dist (train resets): high_vol=46 (34.8%), low_vol=43 (32.6%), medium_vol=43 (32.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 98 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 9.72% / trig 16.50%) | terminal=0.000 (peak 0.027) | TAPE=0.3549
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01621

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps
[CYCLE] Update 99/348 | Step 99,792/500,000 | Episode 128 | Time: 5294.1s
   📊 Metrics: Return=+33.98% | Sharpe=0.808 | DD=18.44% | Turnover=24.20%
   🎚️ Intra-Step TAPE: potential=0.7257 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0555 | critic_loss=0.0179 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0090 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8076 | ema=0.8419 | best_ema=0.8419 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02271

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.55

🎛️ EXECUTION BETA UPDATE at 100,800 steps:
   action_execution_beta: 0.450 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 5347.1s
   📊 Metrics: Return=+59.51% | Sharpe=0.684 | DD=27.82% | Turnover=23.49%
   🎚️ Intra-Step TAPE: potential=0.5540 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0569 | critic_loss=0.0191 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6167 | ema=0.8194 | best_ema=0.8194 | no_improve=0
   🔬 Alpha Diversity: mean=1.31 | std=0.16 | range=[0.78, 2.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.62 | MSFT=1.35 | AMZN=1.34  BOT: JNJ=1.26 | XOM=1.25 | GLD=1.18
   🧭 Regime Start Dist (train resets): high_vol=46 (34.8%), low_vol=43 (32.6%), medium_vol=43 (32.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 100 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0002 | penalty=-0.0000 | rolling_cvar=-0.02068
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00130_shp0p732_actor.weights.h5 (Sharpe=0.732, MDD=24.38%)
[CYCLE] Update 101/348 | Step 101,808/500,000 | Episode 130 | Time: 5400.6s
   📊 Metrics: Return=+69.40% | Sharpe=0.732 | DD=24.38% | Turnover=24.66%
   🎚️ Intra-Step TAPE: potential=0.6337 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0567 | critic_loss=0.0189 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0094 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7323 | ema=0.8107 | best_ema=0.8194 | no_improve=1
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.06% / trig 16.50%) | terminal=0.000 (peak 0.036) | TAPE=0.3528
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00063) | SPY bonus=0.010 (SPY ret=-0.00252)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02960
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00131_shp1p122_actor.weights.h5 (Sharpe=1.122, MDD=17.47%)
[CYCLE] Update 102/348 | Step 102,816/500,000 | Episode 132 | Time: 5454.0s
   📊 Metrics: Return=+73.30% | Sharpe=0.738 | DD=27.23% | Turnover=24.92%
   🎚️ Intra-Step TAPE: potential=0.6816 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0595 | critic_loss=0.0285 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0142 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6842 | ema=0.7981 | best_ema=0.8194 | no_improve=2
   🔬 Alpha Diversity: mean=1.28 | std=0.20 | range=[0.93, 1.92] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.66 | CAT=1.27 | AMZN=1.26  BOT: NEE=1.18 | XOM=1.16 | GLD=1.07
   🧭 Regime Start Dist (train resets): high_vol=48 (35.3%), low_vol=43 (31.6%), medium_vol=45 (33.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 102 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.82% / trig 16.50%) | terminal=0.000 (peak 0.080) | TAPE=0.3286
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00633) | SPY bonus=0.010 (SPY ret=0.00116)
[CYCLE] Update 103/348 | Step 103,824/500,000 | Episode 132 | Time: 5507.9s
   📊 Metrics: Return=+57.45% | Sharpe=1.534 | DD=8.83% | Turnover=30.17%
   🎚️ Intra-Step TAPE: potential=0.7197 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0600 | critic_loss=0.0242 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0121 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5345 | ema=0.8717 | best_ema=0.8717 | no_improve=0
[CYCLE] Update 104/348 | Step 104,832/500,000 | Episode 132 | Time: 5561.8s
   📊 Metrics: Return=+50.76% | Sharpe=0.839 | DD=18.78% | Turnover=30.66%
   🎚️ Intra-Step TAPE: potential=0.2369 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0552 | critic_loss=0.0360 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0180 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8391 | ema=0.8684 | best_ema=0.8717 | no_improve=1
   🔬 Alpha Diversity: mean=1.12 | std=0.14 | range=[0.89, 1.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.21 | MSFT=1.16 | AMZN=1.15  BOT: CAT=1.06 | XOM=1.05 | GLD=0.96
   🧭 Regime Start Dist (train resets): high_vol=48 (35.3%), low_vol=43 (31.6%), medium_vol=45 (33.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 104 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00133_shp0p702_actor.weights.h5 (Sharpe=0.702, MDD=18.78%)
[CYCLE] Update 105/348 | Step 105,840/500,000 | Episode 134 | Time: 5616.4s
   📊 Metrics: Return=+43.38% | Sharpe=0.510 | DD=27.26% | Turnover=30.92%
   🎚️ Intra-Step TAPE: potential=0.7105 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0575 | critic_loss=0.0249 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4555 | ema=0.8271 | best_ema=0.8717 | no_improve=2
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.04% / trig 16.50%) | terminal=0.059 (peak 0.059) | TAPE=0.2678
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02925
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00135_shp0p734_actor.weights.h5 (Sharpe=0.734, MDD=21.02%)
[CYCLE] Update 106/348 | Step 106,848/500,000 | Episode 136 | Time: 5671.6s
   📊 Metrics: Return=+63.18% | Sharpe=0.656 | DD=27.42% | Turnover=30.82%
   🎚️ Intra-Step TAPE: potential=0.3536 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0533 | critic_loss=0.0151 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5982 | ema=0.8042 | best_ema=0.8717 | no_improve=3
   🔬 Alpha Diversity: mean=0.91 | std=0.22 | range=[0.65, 2.04] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.10 | AMZN=0.89 | CAT=0.87  BOT: XOM=0.81 | PG=0.80 | GLD=0.74
   🧭 Regime Start Dist (train resets): high_vol=48 (34.3%), low_vol=46 (32.9%), medium_vol=46 (32.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 106 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.002, dd 4.42% / trig 16.50%) | terminal=0.000 (peak 0.092) | TAPE=0.3026
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00292) | SPY bonus=0.012 (SPY ret=-0.00023)
[CYCLE] Update 107/348 | Step 107,856/500,000 | Episode 136 | Time: 5726.0s
   📊 Metrics: Return=+18.56% | Sharpe=0.331 | DD=22.59% | Turnover=33.93%
   🎚️ Intra-Step TAPE: potential=0.6358 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0566 | critic_loss=0.0188 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0094 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3314 | ema=0.7570 | best_ema=0.8717 | no_improve=4
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02288
[CYCLE] Update 108/348 | Step 108,864/500,000 | Episode 136 | Time: 5779.5s
   📊 Metrics: Return=+47.23% | Sharpe=0.575 | DD=22.59% | Turnover=33.87%
   🎚️ Intra-Step TAPE: potential=0.6021 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0547 | critic_loss=0.0181 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0091 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5754 | ema=0.7388 | best_ema=0.8717 | no_improve=5
   🔬 Alpha Diversity: mean=0.97 | std=0.17 | range=[0.73, 2.00] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.08 | MSFT=0.94 | JPM=0.93  BOT: NEE=0.89 | PG=0.89 | GLD=0.85
   🧭 Regime Start Dist (train resets): high_vol=48 (34.3%), low_vol=46 (32.9%), medium_vol=46 (32.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 108 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0010 | penalty=-0.0000 | rolling_cvar=-0.02941
[CYCLE] Update 109/348 | Step 109,872/500,000 | Episode 138 | Time: 5833.5s
   📊 Metrics: Return=+67.75% | Sharpe=0.702 | DD=25.58% | Turnover=33.85%
   🎚️ Intra-Step TAPE: potential=0.5327 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0577 | critic_loss=0.0202 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0101 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6879 | ema=0.7337 | best_ema=0.8717 | no_improve=6
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.07% / trig 16.50%) | terminal=0.000 (peak 0.044) | TAPE=0.3289
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02784
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 5887.3s
   📊 Metrics: Return=+54.64% | Sharpe=0.612 | DD=23.99% | Turnover=33.66%
   🎚️ Intra-Step TAPE: potential=0.6981 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0532 | critic_loss=0.0181 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0091 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6117 | ema=0.7215 | best_ema=0.8717 | no_improve=7
   🔬 Alpha Diversity: mean=1.10 | std=0.29 | range=[0.82, 2.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.55 | CAT=1.07 | AMZN=1.02  BOT: PG=0.94 | XOM=0.93 | GLD=0.92
   🧭 Regime Start Dist (train resets): high_vol=49 (34.0%), low_vol=47 (32.6%), medium_vol=48 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.039) | TAPE=0.2992
[CYCLE] Update 111/348 | Step 111,888/500,000 | Episode 140 | Time: 5941.4s
   📊 Metrics: Return=+52.00% | Sharpe=1.462 | DD=7.98% | Turnover=32.09%
   🎚️ Intra-Step TAPE: potential=0.6927 | delta_reward=+0.0018
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0561 | critic_loss=0.0231 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0115 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4618 | ema=0.7956 | best_ema=0.8717 | no_improve=8
[CYCLE] Update 112/348 | Step 112,896/500,000 | Episode 140 | Time: 5995.1s
   📊 Metrics: Return=+47.77% | Sharpe=0.836 | DD=18.05% | Turnover=32.08%
   🎚️ Intra-Step TAPE: potential=0.2259 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0566 | critic_loss=0.0292 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0146 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8364 | ema=0.7996 | best_ema=0.8717 | no_improve=9
   🔬 Alpha Diversity: mean=1.11 | std=0.40 | range=[0.84, 3.07] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.12 | MSFT=1.00 | AMZN=0.99  BOT: PG=0.96 | XOM=0.96 | GLD=0.92
   🧭 Regime Start Dist (train resets): high_vol=49 (34.0%), low_vol=47 (32.6%), medium_vol=48 (33.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00141_shp0p872_actor.weights.h5 (Sharpe=0.872, MDD=18.05%)
[CYCLE] Update 113/348 | Step 113,904/500,000 | Episode 142 | Time: 6049.2s
   📊 Metrics: Return=+48.09% | Sharpe=0.569 | DD=26.50% | Turnover=31.90%
   🎚️ Intra-Step TAPE: potential=0.7534 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0533 | critic_loss=0.0350 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0175 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5334 | ema=0.7730 | best_ema=0.8717 | no_improve=10
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.87% / trig 16.50%) | terminal=0.055 (peak 0.066) | TAPE=0.2769
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.02393) | SPY bonus=0.004 (SPY ret=0.02219)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02647
[CYCLE] Update 114/348 | Step 114,912/500,000 | Episode 144 | Time: 6102.0s
   📊 Metrics: Return=+49.62% | Sharpe=0.567 | DD=23.56% | Turnover=32.23%
   🎚️ Intra-Step TAPE: potential=0.6264 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0588 | critic_loss=0.0169 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0084 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5666 | ema=0.7524 | best_ema=0.8717 | no_improve=11
   🔬 Alpha Diversity: mean=1.13 | std=0.29 | range=[0.87, 2.34] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.21 | CAT=1.06 | AMZN=1.06  BOT: NEE=1.00 | GLD=0.99 | PG=0.99
   🧭 Regime Start Dist (train resets): high_vol=49 (33.1%), low_vol=49 (33.1%), medium_vol=50 (33.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.58% / trig 16.50%) | terminal=0.000 (peak 0.032) | TAPE=0.2839
[CYCLE] Update 115/348 | Step 115,920/500,000 | Episode 144 | Time: 6154.7s
   📊 Metrics: Return=+27.80% | Sharpe=0.691 | DD=16.11% | Turnover=31.90%
   🎚️ Intra-Step TAPE: potential=0.2488 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0583 | critic_loss=0.0226 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0113 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6914 | ema=0.7463 | best_ema=0.8717 | no_improve=12
[CYCLE] Update 116/348 | Step 116,928/500,000 | Episode 144 | Time: 6207.8s
   📊 Metrics: Return=+52.76% | Sharpe=0.657 | DD=26.34% | Turnover=31.57%
   🎚️ Intra-Step TAPE: potential=0.7211 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0593 | critic_loss=0.0243 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0122 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6251 | ema=0.7342 | best_ema=0.8717 | no_improve=13
   🔬 Alpha Diversity: mean=1.41 | std=0.12 | range=[0.80, 2.13] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.50 | JNJ=1.40 | MSFT=1.40  BOT: CAT=1.37 | GLD=1.37 | NEE=1.36
   🧭 Regime Start Dist (train resets): high_vol=49 (33.1%), low_vol=49 (33.1%), medium_vol=50 (33.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 116 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01702
[CYCLE] Update 117/348 | Step 117,936/500,000 | Episode 146 | Time: 6261.1s
   📊 Metrics: Return=+50.02% | Sharpe=0.565 | DD=26.74% | Turnover=30.53%
   🎚️ Intra-Step TAPE: potential=0.7170 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0599 | critic_loss=0.0220 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0110 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5230 | ema=0.7130 | best_ema=0.8717 | no_improve=14
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.55% / trig 16.50%) | terminal=0.000 (peak 0.057) | TAPE=0.2896
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01894
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00148_shp1p084_actor.weights.h5 (Sharpe=1.084, MDD=19.47%)
[CYCLE] Update 118/348 | Step 118,944/500,000 | Episode 148 | Time: 6314.5s
   📊 Metrics: Return=+74.81% | Sharpe=1.084 | DD=19.47% | Turnover=30.43%
   🎚️ Intra-Step TAPE: potential=0.6402 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0581 | critic_loss=0.0272 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0136 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0844 | ema=0.7502 | best_ema=0.8717 | no_improve=15
   🔬 Alpha Diversity: mean=1.86 | std=0.20 | range=[1.32, 2.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.12 | CAT=1.99 | AMZN=1.97  BOT: NEE=1.82 | PG=1.80 | GLD=1.78
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=50 (32.9%), medium_vol=52 (34.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 118 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.33% / trig 16.50%) | terminal=0.000 (peak 0.004) | TAPE=0.5084
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00602) | SPY bonus=0.007 (SPY ret=-0.00889)
[CYCLE] Update 119/348 | Step 119,952/500,000 | Episode 148 | Time: 6367.7s
   📊 Metrics: Return=+68.65% | Sharpe=1.863 | DD=8.01% | Turnover=26.51%
   🎚️ Intra-Step TAPE: potential=0.7300 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0556 | critic_loss=0.0283 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0142 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8631 | ema=0.8615 | best_ema=0.8717 | no_improve=16
   🛑 Early-stop triggered: low_advantage_stagnation (|mean_adv|<=1.0e-04 for 20 updates) (step=119,952, update=119)

[OK] THREE-COMPONENT TAPE v3 training completed!
   🛑 Stop reason: low_advantage_stagnation (|mean_adv|<=1.0e-04 for 20 updates)
   Total episodes: 148
   Total timesteps: 119,952
   Training time: 6367.74s (106.13min)
📊 Training summary saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260313_055213_summary.csv
💾 Final models saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00148_shp1p084_actor.weights.h5, /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00148_shp1p084_critic.weights.h5
🎯 Default selected checkpoint: final high-watermark-style checkpoint
[OK] Training complete
checkpoint_prefix: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00148_shp1p084