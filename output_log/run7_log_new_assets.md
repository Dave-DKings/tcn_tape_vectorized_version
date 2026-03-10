[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
[OK] Actuarial feature check passed: {'Actuarial_Prob_60d': 54703, 'Actuarial_Prob_30d': 54703, 'Actuarial_Expected_Recovery': 54703, 'Actuarial_Reserve_Severity': 54703}
[OK] Fundamental feature check passed: none present

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
   Train shape: (40473, 66)
   Test shape: (14230, 66)
   🧮 Actuarial columns: 4 detected (enabled=True) | total non-null=218812
      {'Actuarial_Expected_Recovery': 54703, 'Actuarial_Prob_30d': 54703, 'Actuarial_Prob_60d': 54703, 'Actuarial_Reserve_Severity': 54703}

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.35, band=±0.20, scalar=0.25 -> 0.50 => 0.75 => 0.90 => 1.00)
      ↳ Schedule: 0.25@0 => 0.50@100,000 => 0.75@200,000 => 0.90@300,000 => 1.00@400,000
   ⚙️  Component 4: Execution Inertia (beta=0.65 -> 0.65 => 0.65 => 0.65, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.65@0 => 0.65@100,000 => 0.65@200,000 => 0.65@350,000
   ⚡ Parallel rollout envs: 4
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 25.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🔒 Drawdown dual controller (requested): target=22.00%, tolerance=-1.00% (trigger boundary ≈ 21.00%), lr=0.100, λ_init=0.25, λ_floor=0.00, λ_max=5.00, penalty_coef=1.50
   📐 Position constraints: max_single_asset=95%, min_cash=5%
   [DEBUG] Regime-balanced sampling: use_curriculum_learning=True, volatility_regime pre-existing=False
   🎲 Volatility regimes ready for sampling (computed):
      high_vol: 1341 dates (32.9%)
      low_vol: 1341 dates (32.9%)
      medium_vol: 1396 dates (34.2%)
   🧭 Regime start buckets (train env):
      high_vol: 1341 dates (32.9%)
      low_vol: 1341 dates (32.9%)
      medium_vol: 1396 dates (34.2%)
   [OK] Drawdown controller armed in env: target=22.00%, trigger=21.00%, λ_init=0.250, λ_floor=0.000, λ_max=5.00, penalty_coef=1.50
[OK] THREE-COMPONENT TAPE v3 Environments created:
   Training: 4078 days
   Parallel train env instances: 4
   Testing: 1423 days

🤖 Creating TCN_FUSION agent with Dirichlet distribution for Exp 6...
[OK] Agent created: PPOAgentTF
   [RAND] Dirichlet Distribution: ENABLED
   [TOOL] Actor LR schedule: 0.000030@0 => 0.000020@150,000 => 0.000010@350,000
   State dim: 437
   Action dim: 10
   Actor LR (configured): 3e-05
   Actor LR (active): 0.000030
   Critic LR (active): 0.000150
   🧱 TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Cross-Asset Mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DNA] State augmentation: enabled=False
   [DOWN] Distributional critic: enabled=False | num_quantiles=17
   🎛️ Dirichlet controls: activation=exp_tanh | temperature=1.0 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Dual-head consistency coef: 0.0
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0010
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@150,000 => 0.9980@350,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@150,000 => 0.9700@350,000
   📐 PPO rollout schedule: 1008@0 => 1512@150,000 => 2016@300,000
   🧺 PPO batch-size schedule: 252@0 => 336@150,000 => 504@300,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_215955_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_215955_step_diagnostics.csv

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
      100,000+ steps: scalar=0.50
      200,000+ steps: scalar=0.75
      300,000+ steps: scalar=0.90
      400,000+ steps: scalar=1.00
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.65
      100,000+ steps: beta=0.65
      200,000+ steps: beta=0.65
      350,000+ steps: beta=0.65
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.70, MDD <= 25.0%, skip_on_det_validation=True)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_215955_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_215955_metadata.json
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00003_shp0p933_actor.weights.h5 (Sharpe=0.933, MDD=16.04%)
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 1026.5s
   📊 Metrics: Return=+10.10% | Sharpe=0.163 | DD=11.84% | Turnover=36.15%
   🎚️ Intra-Step TAPE: potential=0.2459 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0601 | critic_loss=0.5820 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2910 | risk_aux_total=0.0449 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.1075 | cvar_loss=0.0443 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.38 | std=1.70 | range=[0.28, 12.53]
   🏷️ Alpha Per-Asset  TOP: GLD=4.00 | PG=2.10 | NEE=1.92  BOT: CAT=0.58 | NVDA=0.43 | AMZN=0.38
   🧭 Regime Start Dist (train resets): high_vol=6 (37.5%), low_vol=4 (25.0%), medium_vol=6 (37.5%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00014_shp0p874_actor.weights.h5 (Sharpe=0.874, MDD=7.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p799_actor.weights.h5 (Sharpe=0.799, MDD=7.20%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00021_shp0p986_actor.weights.h5 (Sharpe=0.986, MDD=8.20%)
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 2033.5s
   📊 Metrics: Return=+4.42% | Sharpe=-0.030 | DD=19.11% | Turnover=29.19%
   🎚️ Intra-Step TAPE: potential=0.6941 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0621 | critic_loss=0.5829 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2914 | risk_aux_total=0.0533 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=1.3150 | cvar_loss=0.0526 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.63 | std=2.47 | range=[0.26, 11.87]
   🏷️ Alpha Per-Asset  TOP: GLD=7.33 | JNJ=2.71 | PG=2.50  BOT: JPM=0.38 | AMZN=0.33 | NVDA=0.31
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=9 (32.1%), medium_vol=9 (32.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p975_actor.weights.h5 (Sharpe=0.975, MDD=7.38%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00038_shp0p875_actor.weights.h5 (Sharpe=0.875, MDD=10.71%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 3048.1s
   📊 Metrics: Return=-1.13% | Sharpe=-0.174 | DD=14.21% | Turnover=34.43%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0508 | critic_loss=0.2760 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1380 | risk_aux_total=0.0420 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=1.0334 | cvar_loss=0.0413 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.88 | std=2.94 | range=[0.28, 17.73]
   🏷️ Alpha Per-Asset  TOP: GLD=7.41 | JNJ=3.42 | PG=3.02  BOT: CAT=0.44 | NVDA=0.36 | AMZN=0.36
   🧭 Regime Start Dist (train resets): high_vol=14 (31.8%), low_vol=18 (40.9%), medium_vol=12 (27.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2213
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00046_shp0p767_actor.weights.h5 (Sharpe=0.767, MDD=9.12%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00052_shp1p082_actor.weights.h5 (Sharpe=1.082, MDD=10.50%)
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 4058.1s
   📊 Metrics: Return=+45.68% | Sharpe=1.082 | DD=10.50% | Turnover=22.39%
   🎚️ Intra-Step TAPE: potential=0.6583 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0607 | critic_loss=0.1735 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0868 | risk_aux_total=0.0505 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.2440 | cvar_loss=0.0498 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.90 | std=3.86 | range=[0.26, 20.48]
   🏷️ Alpha Per-Asset  TOP: GLD=8.39 | JNJ=3.43 | NEE=2.46  BOT: CAT=0.35 | NVDA=0.32 | AMZN=0.30
   🧭 Regime Start Dist (train resets): high_vol=19 (33.9%), low_vol=21 (37.5%), medium_vol=16 (28.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00053_shp1p088_actor.weights.h5 (Sharpe=1.088, MDD=7.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00055_shp0p891_actor.weights.h5 (Sharpe=0.891, MDD=10.73%)
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 5065.2s
   📊 Metrics: Return=+24.10% | Sharpe=0.412 | DD=20.86% | Turnover=16.93%
   🎚️ Intra-Step TAPE: potential=0.4817 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0428 | critic_loss=0.2883 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1442 | risk_aux_total=0.0345 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.8477 | cvar_loss=0.0339 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.66 | std=5.31 | range=[0.30, 21.94]
   🏷️ Alpha Per-Asset  TOP: GLD=12.27 | JNJ=6.63 | NEE=5.56  BOT: CAT=0.65 | NVDA=0.60 | AMZN=0.56
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=24 (35.3%), medium_vol=21 (30.9%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00067_shp0p832_actor.weights.h5 (Sharpe=0.832, MDD=8.11%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp0p720_actor.weights.h5 (Sharpe=0.720, MDD=12.12%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 6075.5s
   📊 Metrics: Return=+24.68% | Sharpe=0.530 | DD=8.43% | Turnover=37.81%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0694 | critic_loss=0.3365 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1682 | risk_aux_total=0.0643 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=1.5914 | cvar_loss=0.0637 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.70 | std=2.40 | range=[0.35, 16.12]
   🏷️ Alpha Per-Asset  TOP: GLD=6.08 | JNJ=3.04 | PG=2.68  BOT: CAT=0.53 | MSFT=0.52 | NVDA=0.47
   🧭 Regime Start Dist (train resets): high_vol=31 (36.9%), low_vol=30 (35.7%), medium_vol=23 (27.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2974
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00090_shp1p034_actor.weights.h5 (Sharpe=1.034, MDD=8.79%)
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 7091.1s
   📊 Metrics: Return=+12.08% | Sharpe=0.194 | DD=29.78% | Turnover=31.65%
   🎚️ Intra-Step TAPE: potential=0.2489 | delta_reward=-0.0033
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0697 | critic_loss=0.1323 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0661 | risk_aux_total=0.0610 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=1.5017 | cvar_loss=0.0601 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.11 | std=2.29 | range=[0.26, 17.31]
   🏷️ Alpha Per-Asset  TOP: GLD=6.60 | JNJ=1.50 | PG=0.72  BOT: MSFT=0.30 | JPM=0.30 | CAT=0.28
   🧭 Regime Start Dist (train resets): high_vol=38 (39.6%), low_vol=33 (34.4%), medium_vol=25 (26.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00104_shp0p923_actor.weights.h5 (Sharpe=0.923, MDD=9.61%)
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 8097.8s
   📊 Metrics: Return=+36.55% | Sharpe=0.923 | DD=9.61% | Turnover=25.86%
   🎚️ Intra-Step TAPE: potential=0.2182 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0593 | critic_loss=0.1335 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0667 | risk_aux_total=0.0491 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.2087 | cvar_loss=0.0483 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.63 | std=2.78 | range=[0.28, 16.94]
   🏷️ Alpha Per-Asset  TOP: GLD=6.77 | PG=3.34 | JNJ=1.87  BOT: AMZN=0.33 | CAT=0.31 | NVDA=0.31
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=36 (33.3%), medium_vol=30 (27.8%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00105_shp1p067_actor.weights.h5 (Sharpe=1.067, MDD=6.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00115_shp1p212_actor.weights.h5 (Sharpe=1.212, MDD=7.03%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00119_shp1p057_actor.weights.h5 (Sharpe=1.057, MDD=7.64%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 9116.2s
   📊 Metrics: Return=+27.24% | Sharpe=0.617 | DD=8.82% | Turnover=28.07%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0520 | critic_loss=0.2289 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1145 | risk_aux_total=0.0425 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.0472 | cvar_loss=0.0419 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.78 | std=3.65 | range=[0.34, 19.26]
   🏷️ Alpha Per-Asset  TOP: PG=6.27 | JNJ=5.62 | GLD=5.56  BOT: CAT=0.55 | AMZN=0.52 | NVDA=0.48
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=42 (33.9%), medium_vol=34 (27.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3438

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00123_shp0p999_actor.weights.h5 (Sharpe=0.999, MDD=6.79%)

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.5

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 10136.6s
   📊 Metrics: Return=+5.26% | Sharpe=-0.030 | DD=15.61% | Turnover=20.78%
   🎚️ Intra-Step TAPE: potential=0.3038 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0627 | critic_loss=0.1604 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0802 | risk_aux_total=0.0566 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=1.3963 | cvar_loss=0.0559 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.07 | std=5.01 | range=[0.34, 25.35]
   🏷️ Alpha Per-Asset  TOP: GLD=11.71 | PG=6.20 | JNJ=4.77  BOT: CAT=0.52 | JPM=0.49 | NVDA=0.49
   🧭 Regime Start Dist (train resets): high_vol=51 (38.6%), low_vol=45 (34.1%), medium_vol=36 (27.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00133_shp0p852_actor.weights.h5 (Sharpe=0.852, MDD=11.29%)
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 11153.2s
   📊 Metrics: Return=-2.50% | Sharpe=-0.221 | DD=15.89% | Turnover=25.21%
   🎚️ Intra-Step TAPE: potential=0.5919 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0607 | critic_loss=0.1397 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0698 | risk_aux_total=0.0498 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=1.2295 | cvar_loss=0.0492 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.46 | std=5.09 | range=[0.29, 23.77]
   🏷️ Alpha Per-Asset  TOP: JNJ=9.99 | GLD=7.86 | PG=6.62  BOT: NVDA=0.41 | CAT=0.39 | AMZN=0.39
   🧭 Regime Start Dist (train resets): high_vol=55 (38.2%), low_vol=51 (35.4%), medium_vol=38 (26.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.69% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2256