[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
[OK] Actuarial feature check passed: {'Actuarial_Reserve_Severity': 54703, 'Actuarial_Prob_60d': 54703, 'Actuarial_Prob_30d': 54703, 'Actuarial_Expected_Recovery': 54703}
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
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260310_204958_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260310_204958_step_diagnostics.csv

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
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260310_204958_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260310_204958_metadata.json
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp1p258_actor.weights.h5 (Sharpe=1.258, MDD=12.14%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00003_shp0p949_actor.weights.h5 (Sharpe=0.949, MDD=22.34%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p792_actor.weights.h5 (Sharpe=0.792, MDD=19.24%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p196_actor.weights.h5 (Sharpe=1.196, MDD=14.49%)
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 542.1s
   📊 Metrics: Return=-5.60% | Sharpe=-0.158 | DD=22.20% | Turnover=49.97%
   🎚️ Intra-Step TAPE: potential=0.2471 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0096 | critic_loss=0.8357 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4179 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.38 | std=0.94 | range=[0.62, 7.02]
   🏷️ Alpha Per-Asset  TOP: GLD=3.18 | NEE=2.80 | XOM=2.73  BOT: CAT=2.29 | NVDA=1.75 | AMZN=1.60
   🧭 Regime Start Dist (train resets): high_vol=6 (37.5%), low_vol=4 (25.0%), medium_vol=6 (37.5%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00019_shp1p249_actor.weights.h5 (Sharpe=1.249, MDD=9.45%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00023_shp0p950_actor.weights.h5 (Sharpe=0.950, MDD=12.40%)
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1073.4s
   📊 Metrics: Return=+27.30% | Sharpe=0.610 | DD=19.99% | Turnover=37.71%
   🎚️ Intra-Step TAPE: potential=0.7166 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0068 | critic_loss=0.6975 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3487 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.04 | std=0.24 | range=[0.37, 1.78]
   🏷️ Alpha Per-Asset  TOP: NEE=1.26 | PG=1.16 | JNJ=1.13  BOT: GLD=0.98 | NVDA=0.89 | AMZN=0.86
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=9 (32.1%), medium_vol=9 (32.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 20 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00029_shp1p123_actor.weights.h5 (Sharpe=1.123, MDD=9.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00033_shp0p858_actor.weights.h5 (Sharpe=0.858, MDD=18.05%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 1605.2s
   📊 Metrics: Return=+23.76% | Sharpe=0.508 | DD=9.30% | Turnover=44.20%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0116 | critic_loss=0.1164 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0582 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.41 | std=0.41 | range=[0.32, 2.79]
   🏷️ Alpha Per-Asset  TOP: NEE=1.59 | GLD=1.53 | JNJ=1.51  BOT: JPM=1.37 | AMZN=1.24 | NVDA=1.16
   🧭 Regime Start Dist (train resets): high_vol=14 (31.8%), low_vol=18 (40.9%), medium_vol=12 (27.3%)
   🔒 Drawdown λ snapshot=2.481 (peak 2.481, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3198
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 2133.3s
   📊 Metrics: Return=-9.93% | Sharpe=-0.227 | DD=32.72% | Turnover=71.61%
   🎚️ Intra-Step TAPE: potential=0.6535 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0066 | critic_loss=0.1143 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0572 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.50 | std=0.21 | range=[0.30, 1.59]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.56 | AMZN=0.54 | GLD=0.52  BOT: PG=0.48 | JPM=0.48 | MSFT=0.46
   🧭 Regime Start Dist (train resets): high_vol=19 (33.9%), low_vol=21 (37.5%), medium_vol=16 (28.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 40 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 2683.1s
   📊 Metrics: Return=-7.61% | Sharpe=0.009 | DD=54.17% | Turnover=44.95%
   🎚️ Intra-Step TAPE: potential=0.2075 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0135 | critic_loss=0.2167 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1083 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.40 | std=0.29 | range=[0.25, 2.42]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.91 | AMZN=0.65 | CAT=0.33  BOT: NEE=0.29 | JNJ=0.28 | PG=0.27
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=24 (35.3%), medium_vol=21 (30.9%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00066_shp1p412_actor.weights.h5 (Sharpe=1.412, MDD=13.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00068_shp0p879_actor.weights.h5 (Sharpe=0.879, MDD=17.12%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00070_shp0p887_actor.weights.h5 (Sharpe=0.887, MDD=21.31%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00071_shp0p948_actor.weights.h5 (Sharpe=0.948, MDD=20.12%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00075_shp1p678_actor.weights.h5 (Sharpe=1.678, MDD=17.71%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 3244.1s
   📊 Metrics: Return=-7.90% | Sharpe=-0.059 | DD=39.05% | Turnover=49.26%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0076 | critic_loss=0.1718 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0859 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.89 | std=1.44 | range=[0.24, 14.74]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.49 | AMZN=1.85 | CAT=1.19  BOT: NEE=0.36 | JNJ=0.34 | PG=0.33
   🧭 Regime Start Dist (train resets): high_vol=31 (36.9%), low_vol=30 (35.7%), medium_vol=23 (27.4%)
   🔒 Drawdown λ snapshot=4.500 (peak 4.500, dd 0.00% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2104
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00087_shp1p505_actor.weights.h5 (Sharpe=1.505, MDD=21.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00091_shp1p832_actor.weights.h5 (Sharpe=1.832, MDD=22.70%)
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 3789.6s
   📊 Metrics: Return=-21.73% | Sharpe=-0.087 | DD=65.18% | Turnover=31.77%
   🎚️ Intra-Step TAPE: potential=0.7366 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0057 | critic_loss=0.1985 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0992 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.58 | std=2.89 | range=[0.24, 17.36]
   🏷️ Alpha Per-Asset  TOP: AMZN=5.94 | NVDA=4.91 | JPM=1.22  BOT: GLD=0.46 | PG=0.42 | JNJ=0.42
   🧭 Regime Start Dist (train resets): high_vol=38 (39.6%), low_vol=33 (34.4%), medium_vol=25 (26.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00095_shp1p829_actor.weights.h5 (Sharpe=1.829, MDD=21.61%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00101_shp0p938_actor.weights.h5 (Sharpe=0.938, MDD=11.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00104_shp0p925_actor.weights.h5 (Sharpe=0.925, MDD=23.10%)
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 4332.4s
   📊 Metrics: Return=+94.17% | Sharpe=0.925 | DD=23.10% | Turnover=17.98%
   🎚️ Intra-Step TAPE: potential=0.2215 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0112 | critic_loss=0.0983 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0492 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.93 | std=4.51 | range=[0.39, 24.52]
   🏷️ Alpha Per-Asset  TOP: NVDA=8.99 | AMZN=6.33 | CAT=6.15  BOT: NEE=0.82 | JNJ=0.66 | PG=0.56
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=36 (33.3%), medium_vol=30 (27.8%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00114_shp1p840_actor.weights.h5 (Sharpe=1.840, MDD=21.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00116_shp1p031_actor.weights.h5 (Sharpe=1.031, MDD=22.77%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 4874.1s
   📊 Metrics: Return=-34.02% | Sharpe=-0.639 | DD=43.99% | Turnover=60.28%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0089 | critic_loss=0.0775 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0388 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.79 | std=1.81 | range=[0.28, 17.14]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.94 | AMZN=0.95 | CAT=0.76  BOT: JNJ=0.43 | XOM=0.41 | PG=0.40
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=42 (33.9%), medium_vol=34 (27.4%)
   🔒 Drawdown λ snapshot=4.500 (peak 4.500, dd 0.00% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.1956

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00128_shp1p335_actor.weights.h5 (Sharpe=1.335, MDD=23.40%)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.5

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 5416.3s
   📊 Metrics: Return=+295.81% | Sharpe=1.335 | DD=23.40% | Turnover=45.59%
   🎚️ Intra-Step TAPE: potential=0.5251 | delta_reward=+0.0021
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0102 | critic_loss=0.0546 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0273 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.56 | std=0.40 | range=[0.26, 2.82]
   🏷️ Alpha Per-Asset  TOP: GLD=0.67 | JNJ=0.65 | PG=0.63  BOT: JPM=0.46 | CAT=0.46 | NVDA=0.45
   🧭 Regime Start Dist (train resets): high_vol=51 (38.6%), low_vol=45 (34.1%), medium_vol=36 (27.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00133_shp1p252_actor.weights.h5 (Sharpe=1.252, MDD=21.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00136_shp1p441_actor.weights.h5 (Sharpe=1.441, MDD=19.01%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00138_shp0p882_actor.weights.h5 (Sharpe=0.882, MDD=22.01%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00140_shp0p942_actor.weights.h5 (Sharpe=0.942, MDD=22.37%)
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 5963.4s
   📊 Metrics: Return=+128.52% | Sharpe=0.942 | DD=22.37% | Turnover=44.72%
   🎚️ Intra-Step TAPE: potential=0.2193 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0078 | critic_loss=0.1159 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0580 | risk_aux_total=0.0009 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.21 | std=3.75 | range=[0.25, 26.20]
   🏷️ Alpha Per-Asset  TOP: NVDA=7.58 | CAT=1.04 | AMZN=0.68  BOT: JPM=0.40 | XOM=0.39 | MSFT=0.38
   🧭 Regime Start Dist (train resets): high_vol=55 (38.2%), low_vol=51 (35.4%), medium_vol=38 (26.4%)
   🔒 Drawdown λ snapshot=4.890 (peak 4.890, dd 30.98% / trig 21.00%) | terminal=1.017 (peak 2.518) | TAPE=0.5020
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 148 | Time: 6501.9s
   📊 Metrics: Return=-26.29% | Sharpe=-0.411 | DD=33.21% | Turnover=50.54%
   🎚️ Intra-Step TAPE: potential=0.3705 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0120 | critic_loss=0.0598 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0299 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.25 | std=5.38 | range=[0.38, 27.50]
   🏷️ Alpha Per-Asset  TOP: AMZN=8.39 | CAT=6.71 | NVDA=5.40  BOT: JNJ=1.10 | XOM=1.03 | PG=0.99
   🧭 Regime Start Dist (train resets): high_vol=59 (38.8%), low_vol=51 (33.6%), medium_vol=42 (27.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00153_shp0p722_actor.weights.h5 (Sharpe=0.722, MDD=24.26%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00156_shp0p953_actor.weights.h5 (Sharpe=0.953, MDD=23.21%)
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 160 | Time: 7042.2s
   📊 Metrics: Return=+24.74% | Sharpe=0.269 | DD=38.09% | Turnover=33.87%
   🎚️ Intra-Step TAPE: potential=0.2233 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0155 | critic_loss=0.2081 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1040 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.28 | std=4.80 | range=[0.30, 25.75]
   🏷️ Alpha Per-Asset  TOP: AMZN=8.53 | NVDA=5.46 | CAT=4.54  BOT: JNJ=0.56 | JPM=0.55 | PG=0.54
   🧭 Regime Start Dist (train resets): high_vol=64 (39.0%), low_vol=52 (31.7%), medium_vol=48 (29.3%)
   🔒 Drawdown λ snapshot=4.278 (peak 4.500, dd 26.52% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2332
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 168 | Time: 7581.3s
   📊 Metrics: Return=-3.86% | Sharpe=-0.051 | DD=33.75% | Turnover=44.04%
   🎚️ Intra-Step TAPE: potential=0.3131 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0030 | critic_loss=0.1104 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0552 | risk_aux_total=0.0011 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.29 | std=5.35 | range=[0.32, 25.59]
   🏷️ Alpha Per-Asset  TOP: NVDA=14.38 | AMZN=4.71 | CAT=0.71  BOT: JNJ=0.43 | XOM=0.41 | PG=0.40
   🧭 Regime Start Dist (train resets): high_vol=67 (39.0%), low_vol=55 (32.0%), medium_vol=50 (29.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00171_shp1p448_actor.weights.h5 (Sharpe=1.448, MDD=22.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00173_shp1p567_actor.weights.h5 (Sharpe=1.567, MDD=23.49%)
   [TOOL] Actor learning rate adjusted to 0.000020 at step 150,000

📚 PPO ROLLOUT UPDATE at 150,192 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 150,192 steps:
   Batch size: 336

[DOWN] PPO GAMMA UPDATE at 150,192 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 150,192 steps:
   gae_lambda: 0.9500
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 180 | Time: 8146.1s
   📊 Metrics: Return=-22.76% | Sharpe=0.014 | DD=67.20% | Turnover=22.24%
   🎚️ Intra-Step TAPE: potential=0.2191 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0017 | critic_loss=0.0842 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0421 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.43 | std=4.26 | range=[0.50, 23.95]
   🏷️ Alpha Per-Asset  TOP: NVDA=10.67 | AMZN=5.19 | CAT=1.33  BOT: JNJ=1.02 | XOM=0.90 | PG=0.88
   🧭 Regime Start Dist (train resets): high_vol=72 (39.1%), low_vol=57 (31.0%), medium_vol=55 (29.9%)
   🔒 Drawdown λ snapshot=3.915 (peak 4.500, dd 10.99% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2251
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00181_shp1p055_actor.weights.h5 (Sharpe=1.055, MDD=23.95%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00190_shp1p468_actor.weights.h5 (Sharpe=1.468, MDD=21.40%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00193_shp1p264_actor.weights.h5 (Sharpe=1.264, MDD=19.20%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00195_shp1p492_actor.weights.h5 (Sharpe=1.492, MDD=19.73%)
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 196 | Time: 8911.7s
   📊 Metrics: Return=+10.63% | Sharpe=0.138 | DD=36.24% | Turnover=34.66%
   🎚️ Intra-Step TAPE: potential=0.6614 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0053 | critic_loss=0.0454 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0227 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.45 | std=3.81 | range=[0.71, 23.85]
   🏷️ Alpha Per-Asset  TOP: NVDA=9.35 | AMZN=3.07 | JPM=2.98  BOT: GLD=1.14 | XOM=1.12 | PG=1.10
   🧭 Regime Start Dist (train resets): high_vol=79 (39.5%), low_vol=61 (30.5%), medium_vol=60 (30.0%)
   🔒 Drawdown λ snapshot=2.670 (peak 2.745, dd 2.88% / trig 21.00%) | terminal=4.678 (peak 4.770) | TAPE=0.2214
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00202_shp1p265_actor.weights.h5 (Sharpe=1.265, MDD=20.12%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00205_shp0p877_actor.weights.h5 (Sharpe=0.877, MDD=24.76%)
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 208 | Time: 9646.2s
   📊 Metrics: Return=+338.92% | Sharpe=1.336 | DD=35.98% | Turnover=29.82%
   🎚️ Intra-Step TAPE: potential=0.7467 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0138 | critic_loss=0.0238 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0119 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.38 | std=5.78 | range=[0.51, 27.14]
   🏷️ Alpha Per-Asset  TOP: NVDA=12.83 | AMZN=6.81 | JPM=5.31  BOT: NEE=0.77 | JNJ=0.76 | PG=0.69
   🧭 Regime Start Dist (train resets): high_vol=80 (37.7%), low_vol=67 (31.6%), medium_vol=65 (30.7%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00211_shp1p586_actor.weights.h5 (Sharpe=1.586, MDD=21.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00212_shp1p048_actor.weights.h5 (Sharpe=1.048, MDD=22.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00214_shp1p260_actor.weights.h5 (Sharpe=1.260, MDD=22.65%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00218_shp1p655_actor.weights.h5 (Sharpe=1.655, MDD=23.93%)
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 224 | Time: 10386.7s
   📊 Metrics: Return=-1.96% | Sharpe=-0.018 | DD=29.15% | Turnover=38.57%
   🎚️ Intra-Step TAPE: potential=0.2295 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0085 | critic_loss=0.0461 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0231 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.48 | std=3.49 | range=[0.22, 25.94]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.84 | JPM=3.82 | AMZN=2.74  BOT: PG=0.32 | NEE=0.31 | MSFT=0.30
   🧭 Regime Start Dist (train resets): high_vol=89 (39.0%), low_vol=68 (29.8%), medium_vol=71 (31.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00227_shp1p556_actor.weights.h5 (Sharpe=1.556, MDD=22.44%)

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.75
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00237_shp1p679_actor.weights.h5 (Sharpe=1.679, MDD=23.87%)
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 240 | Time: 11119.0s
   📊 Metrics: Return=+188.37% | Sharpe=0.929 | DD=39.83% | Turnover=21.59%
   🎚️ Intra-Step TAPE: potential=0.2342 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0070 | critic_loss=0.1083 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0542 | risk_aux_total=0.0010 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.16 | std=6.70 | range=[0.21, 30.36]
   🏷️ Alpha Per-Asset  TOP: NVDA=9.98 | JPM=9.72 | AMZN=6.37  BOT: JNJ=0.43 | NEE=0.42 | PG=0.41
   🧭 Regime Start Dist (train resets): high_vol=98 (40.2%), low_vol=74 (30.3%), medium_vol=72 (29.5%)
   🔒 Drawdown λ snapshot=2.008 (peak 2.615, dd 16.54% / trig 21.00%) | terminal=4.175 (peak 5.000) | TAPE=0.4911
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00241_shp1p735_actor.weights.h5 (Sharpe=1.735, MDD=24.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00251_shp1p445_actor.weights.h5 (Sharpe=1.445, MDD=23.46%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00253_shp1p718_actor.weights.h5 (Sharpe=1.718, MDD=22.20%)
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 256 | Time: 11867.7s
   📊 Metrics: Return=-47.20% | Sharpe=-0.084 | DD=73.40% | Turnover=17.71%
   🎚️ Intra-Step TAPE: potential=0.2495 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0059 | critic_loss=0.0642 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0321 | risk_aux_total=0.0010 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.38 | std=5.74 | range=[0.18, 30.04]
   🏷️ Alpha Per-Asset  TOP: NVDA=12.77 | AMZN=4.51 | CAT=2.52  BOT: PG=0.39 | JNJ=0.37 | XOM=0.34
   🧭 Regime Start Dist (train resets): high_vol=102 (39.2%), low_vol=79 (30.4%), medium_vol=79 (30.4%)
   🔒 Drawdown λ snapshot=0.800 (peak 0.956, dd 4.78% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2271
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00257_shp1p798_actor.weights.h5 (Sharpe=1.798, MDD=24.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00264_shp0p875_actor.weights.h5 (Sharpe=0.875, MDD=24.09%)

📚 EPISODE HORIZON UPDATE at 240,912 steps:
   Episode horizon: 1053 steps

📚 EPISODE HORIZON UPDATE at 242,424 steps:
   Episode horizon: 1127 steps
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 268 | Time: 12649.8s
   📊 Metrics: Return=-16.15% | Sharpe=0.127 | DD=75.71% | Turnover=17.57%
   🎚️ Intra-Step TAPE: potential=0.6868 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0059 | critic_loss=0.0431 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0216 | risk_aux_total=0.0011 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.06 | std=8.02 | range=[0.26, 30.46]
   🏷️ Alpha Per-Asset  TOP: NVDA=17.80 | JPM=7.60 | AMZN=7.02  BOT: JNJ=0.45 | NEE=0.44 | PG=0.44
   🧭 Regime Start Dist (train resets): high_vol=109 (40.1%), low_vol=81 (29.8%), medium_vol=82 (30.1%)

📚 EPISODE HORIZON UPDATE at 243,936 steps:
   Episode horizon: 1202 steps

📚 EPISODE HORIZON UPDATE at 245,448 steps:
   Episode horizon: 1276 steps

📚 EPISODE HORIZON UPDATE at 246,960 steps:
   Episode horizon: 1350 steps

📚 EPISODE HORIZON UPDATE at 248,472 steps:
   Episode horizon: 1425 steps

📚 EPISODE HORIZON UPDATE at 249,984 steps:
   Episode horizon: 1499 steps

📚 EPISODE HORIZON UPDATE at 251,496 steps:
   Episode horizon: 1500 steps