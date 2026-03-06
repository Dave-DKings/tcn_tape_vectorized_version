[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
[OK] Actuarial feature check passed: {'Actuarial_Expected_Recovery': 54767, 'Actuarial_Prob_60d': 54767, 'Actuarial_Reserve_Severity': 54767, 'Actuarial_Prob_30d': 54767}
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
   Train shape: (40537, 66)
   Test shape: (14230, 66)
   🧮 Actuarial columns: 4 detected (enabled=True) | total non-null=219068
      {'Actuarial_Expected_Recovery': 54767, 'Actuarial_Prob_30d': 54767, 'Actuarial_Prob_60d': 54767, 'Actuarial_Reserve_Severity': 54767}

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.35, band=±0.20, scalar=0.25 -> 0.50 => 0.75 => 0.90 => 1.00)
      ↳ Schedule: 0.25@0 => 0.50@100,000 => 0.75@200,000 => 0.90@300,000 => 1.00@400,000
   ⚙️  Component 4: Execution Inertia (beta=0.50 -> 0.40 => 0.30 => 0.25, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.50@0 => 0.40@100,000 => 0.30@200,000 => 0.25@350,000
   ⚡ Parallel rollout envs: 4
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 25.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🔒 Drawdown dual controller (requested): target=20.00%, tolerance=-1.00% (trigger boundary ≈ 19.00%), lr=0.100, λ_init=0.50, λ_floor=0.00, λ_max=5.00, penalty_coef=1.50
   [OK] Drawdown controller armed in env: target=20.00%, trigger=19.00%, λ_init=0.500, λ_floor=0.000, λ_max=5.00, penalty_coef=1.50
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
   🎛️ Dirichlet controls: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Dual-head consistency coef: 0.0
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0050
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@150,000 => 0.9980@350,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@150,000 => 0.9700@350,000
   📐 PPO rollout schedule: 1008@0 => 1512@150,000 => 2016@300,000
   🧺 PPO batch-size schedule: 252@0 => 336@150,000 => 504@300,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260303_112113_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260303_112113_step_diagnostics.csv

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
      0+ steps: beta=0.50
      100,000+ steps: beta=0.40
      200,000+ steps: beta=0.30
      350,000+ steps: beta=0.25
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.70, MDD <= 25.0%, skip_on_det_validation=True)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260303_112113_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260303_112113_metadata.json
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp0p755_actor.weights.h5 (Sharpe=0.755, MDD=13.55%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp0p761_actor.weights.h5 (Sharpe=0.761, MDD=11.67%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p002_actor.weights.h5 (Sharpe=1.002, MDD=9.93%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp0p750_actor.weights.h5 (Sharpe=0.750, MDD=15.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p860_actor.weights.h5 (Sharpe=0.860, MDD=14.64%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00012_shp1p193_actor.weights.h5 (Sharpe=1.193, MDD=9.66%)
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 560.0s
   📊 Metrics: Return=+59.63% | Sharpe=1.193 | DD=9.66% | Turnover=26.40%
   🎚️ Intra-Step TAPE: potential=0.7100 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1764 | critic_loss=0.5815 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2908 | risk_aux_total=0.0977 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.6207 | cvar_loss=0.0972 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.14 | std=0.48 | range=[0.43, 3.21]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00021_shp0p885_actor.weights.h5 (Sharpe=0.885, MDD=10.77%)
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1115.1s
   📊 Metrics: Return=-28.60% | Sharpe=-0.445 | DD=44.24% | Turnover=24.87%
   🎚️ Intra-Step TAPE: potential=0.2926 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1591 | critic_loss=0.2044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1022 | risk_aux_total=0.0870 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.4435 | cvar_loss=0.0866 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.37 | std=0.47 | range=[0.44, 3.06]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p107_actor.weights.h5 (Sharpe=1.107, MDD=9.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00033_shp0p706_actor.weights.h5 (Sharpe=0.706, MDD=16.49%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00036_shp1p059_actor.weights.h5 (Sharpe=1.059, MDD=6.86%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 1668.3s
   📊 Metrics: Return=-11.14% | Sharpe=-0.110 | DD=46.81% | Turnover=28.36%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2129 | critic_loss=0.4234 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2117 | risk_aux_total=0.1383 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.2958 | cvar_loss=0.1377 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.06 | std=0.30 | range=[0.45, 2.55]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 19.00%) | terminal=3.048 (peak 3.048) | TAPE=0.2081
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00051_shp0p783_actor.weights.h5 (Sharpe=0.783, MDD=9.21%)
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 2220.8s
   📊 Metrics: Return=-8.63% | Sharpe=-0.066 | DD=43.44% | Turnover=30.56%
   🎚️ Intra-Step TAPE: potential=0.6869 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1514 | critic_loss=0.2337 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1169 | risk_aux_total=0.0818 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.3564 | cvar_loss=0.0814 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.14 | std=0.30 | range=[0.50, 2.69]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00064_shp1p200_actor.weights.h5 (Sharpe=1.200, MDD=8.80%)
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 2774.0s
   📊 Metrics: Return=+55.19% | Sharpe=1.200 | DD=8.80% | Turnover=26.65%
   🎚️ Intra-Step TAPE: potential=0.2219 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1671 | critic_loss=0.1292 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0646 | risk_aux_total=0.0891 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.4769 | cvar_loss=0.0886 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.94 | std=0.67 | range=[0.52, 4.85]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00067_shp0p790_actor.weights.h5 (Sharpe=0.790, MDD=8.57%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00075_shp1p022_actor.weights.h5 (Sharpe=1.022, MDD=13.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00077_shp0p719_actor.weights.h5 (Sharpe=0.719, MDD=13.72%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00080_shp1p259_actor.weights.h5 (Sharpe=1.259, MDD=11.23%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 3314.3s
   📊 Metrics: Return=+58.31% | Sharpe=1.259 | DD=11.23% | Turnover=27.39%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1487 | critic_loss=0.2662 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1331 | risk_aux_total=0.0753 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.2467 | cvar_loss=0.0748 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.58 | std=0.23 | range=[0.97, 2.28]
   [WARN]  WARNING: Alpha std < 0.25 after 60 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 19.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5519
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00084_shp0p824_actor.weights.h5 (Sharpe=0.824, MDD=13.52%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00085_shp0p847_actor.weights.h5 (Sharpe=0.847, MDD=13.63%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00092_shp1p001_actor.weights.h5 (Sharpe=1.001, MDD=8.62%)
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 3856.8s
   📊 Metrics: Return=+49.00% | Sharpe=1.001 | DD=8.62% | Turnover=26.68%
   🎚️ Intra-Step TAPE: potential=0.2914 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1454 | critic_loss=0.1955 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0977 | risk_aux_total=0.0742 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.2303 | cvar_loss=0.0738 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.67 | std=0.38 | range=[0.49, 2.82]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00093_shp0p892_actor.weights.h5 (Sharpe=0.892, MDD=11.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00094_shp0p871_actor.weights.h5 (Sharpe=0.871, MDD=8.31%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00095_shp0p798_actor.weights.h5 (Sharpe=0.798, MDD=11.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00100_shp0p940_actor.weights.h5 (Sharpe=0.940, MDD=8.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00103_shp0p873_actor.weights.h5 (Sharpe=0.873, MDD=11.48%)
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 4403.5s
   📊 Metrics: Return=+20.72% | Sharpe=0.422 | DD=18.43% | Turnover=30.81%
   🎚️ Intra-Step TAPE: potential=0.2211 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1987 | critic_loss=0.0718 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0359 | risk_aux_total=0.1296 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.1531 | cvar_loss=0.1292 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.50 | std=0.34 | range=[0.44, 2.81]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00117_shp1p088_actor.weights.h5 (Sharpe=1.088, MDD=11.63%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 4952.8s
   📊 Metrics: Return=+18.35% | Sharpe=0.369 | DD=17.41% | Turnover=28.13%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1568 | critic_loss=0.0258 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0129 | risk_aux_total=0.0869 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.4389 | cvar_loss=0.0863 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.15 | std=0.28 | range=[0.38, 2.06]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 19.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2699

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00121_shp0p770_actor.weights.h5 (Sharpe=0.770, MDD=17.06%)

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00126_shp0p768_actor.weights.h5 (Sharpe=0.768, MDD=15.60%)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.5

🎛️ EXECUTION BETA UPDATE at 100,800 steps:
   action_execution_beta: 0.400 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 5502.4s
   📊 Metrics: Return=+48.27% | Sharpe=0.680 | DD=13.66% | Turnover=27.98%
   🎚️ Intra-Step TAPE: potential=0.7042 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2054 | critic_loss=0.0250 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.1336 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.2189 | cvar_loss=0.1331 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.25 | std=0.33 | range=[0.46, 2.57]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00129_shp0p771_actor.weights.h5 (Sharpe=0.771, MDD=14.84%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00136_shp0p986_actor.weights.h5 (Sharpe=0.986, MDD=14.31%)
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 6051.7s
   📊 Metrics: Return=+51.18% | Sharpe=0.627 | DD=14.66% | Turnover=23.63%
   🎚️ Intra-Step TAPE: potential=0.2331 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1428 | critic_loss=0.2005 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1003 | risk_aux_total=0.0718 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.1889 | cvar_loss=0.0713 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.45 | std=0.91 | range=[0.49, 7.73]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.48% / trig 19.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3474
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00142_shp0p978_actor.weights.h5 (Sharpe=0.978, MDD=13.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00144_shp1p031_actor.weights.h5 (Sharpe=1.031, MDD=8.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00148_shp0p729_actor.weights.h5 (Sharpe=0.729, MDD=14.15%)
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 148 | Time: 6601.6s
   📊 Metrics: Return=+48.59% | Sharpe=0.729 | DD=14.15% | Turnover=20.47%
   🎚️ Intra-Step TAPE: potential=0.2447 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1644 | critic_loss=0.0728 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0364 | risk_aux_total=0.0925 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.5314 | cvar_loss=0.0919 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.56 | std=0.52 | range=[0.59, 3.80]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00154_shp0p767_actor.weights.h5 (Sharpe=0.767, MDD=17.48%)
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 160 | Time: 7151.4s
   📊 Metrics: Return=+44.14% | Sharpe=0.646 | DD=13.28% | Turnover=23.13%
   🎚️ Intra-Step TAPE: potential=0.7290 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1509 | critic_loss=0.1343 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0671 | risk_aux_total=0.0749 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.2405 | cvar_loss=0.0744 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.49 | std=0.46 | range=[0.42, 3.22]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.72% / trig 19.00%) | terminal=0.000 (peak 3.454) | TAPE=0.3448
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 168 | Time: 7700.2s
   📊 Metrics: Return=-17.21% | Sharpe=-0.147 | DD=47.19% | Turnover=23.86%
   🎚️ Intra-Step TAPE: potential=0.6782 | delta_reward=+0.0021
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2094 | critic_loss=0.0241 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0121 | risk_aux_total=0.1381 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.2932 | cvar_loss=0.1376 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.49 | std=0.50 | range=[0.54, 3.93]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00169_shp0p735_actor.weights.h5 (Sharpe=0.735, MDD=14.29%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00175_shp0p781_actor.weights.h5 (Sharpe=0.781, MDD=18.36%)
   [TOOL] Actor learning rate adjusted to 0.000020 at step 150,000

📚 PPO ROLLOUT UPDATE at 150,192 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 150,192 steps:
   Batch size: 336

[DOWN] PPO GAMMA UPDATE at 150,192 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 150,192 steps:
   gae_lambda: 0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00178_shp0p715_actor.weights.h5 (Sharpe=0.715, MDD=13.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00179_shp0p737_actor.weights.h5 (Sharpe=0.737, MDD=14.16%)
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 180 | Time: 8290.1s
   📊 Metrics: Return=+10.66% | Sharpe=0.142 | DD=42.18% | Turnover=19.82%
   🎚️ Intra-Step TAPE: potential=0.4624 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1805 | critic_loss=0.0464 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0232 | risk_aux_total=0.1094 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.8150 | cvar_loss=0.1089 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.69 | std=0.72 | range=[0.52, 5.21]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 19.00%) | terminal=0.000 (peak 1.771) | TAPE=0.2188
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00192_shp1p236_actor.weights.h5 (Sharpe=1.236, MDD=10.38%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00195_shp0p701_actor.weights.h5 (Sharpe=0.701, MDD=13.29%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00196_shp0p797_actor.weights.h5 (Sharpe=0.797, MDD=14.24%)
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 196 | Time: 9085.4s
   📊 Metrics: Return=+55.35% | Sharpe=0.797 | DD=14.24% | Turnover=21.13%
   🎚️ Intra-Step TAPE: potential=0.5956 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1614 | critic_loss=0.0489 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0245 | risk_aux_total=0.0871 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.4457 | cvar_loss=0.0867 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.63 | std=0.62 | range=[0.81, 7.54]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.52% / trig 19.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4065
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00198_shp0p853_actor.weights.h5 (Sharpe=0.853, MDD=15.93%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00201_shp0p911_actor.weights.h5 (Sharpe=0.911, MDD=16.28%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00205_shp0p886_actor.weights.h5 (Sharpe=0.886, MDD=13.28%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00208_shp1p016_actor.weights.h5 (Sharpe=1.016, MDD=13.06%)
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 208 | Time: 9880.9s
   📊 Metrics: Return=+76.63% | Sharpe=1.016 | DD=13.06% | Turnover=21.32%
   🎚️ Intra-Step TAPE: potential=0.4343 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1412 | critic_loss=0.1315 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0658 | risk_aux_total=0.0771 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.2774 | cvar_loss=0.0766 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.01 | std=0.19 | range=[0.62, 1.83]
   [WARN]  WARNING: Alpha std < 0.25 after 170 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00222_shp0p704_actor.weights.h5 (Sharpe=0.704, MDD=13.19%)
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 224 | Time: 10677.8s
   📊 Metrics: Return=-16.66% | Sharpe=-0.160 | DD=46.63% | Turnover=22.02%
   🎚️ Intra-Step TAPE: potential=0.4981 | delta_reward=+0.0022
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1524 | critic_loss=0.0083 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0041 | risk_aux_total=0.0768 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.2731 | cvar_loss=0.0764 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.33 | std=0.34 | range=[0.66, 3.22]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00227_shp0p727_actor.weights.h5 (Sharpe=0.727, MDD=12.89%)

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.75

🎛️ EXECUTION BETA UPDATE at 200,088 steps:
   action_execution_beta: 0.300 (w_exec=(1-β)w_prev + βw_raw)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00229_shp0p892_actor.weights.h5 (Sharpe=0.892, MDD=15.78%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00231_shp0p756_actor.weights.h5 (Sharpe=0.756, MDD=13.69%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00232_shp0p718_actor.weights.h5 (Sharpe=0.718, MDD=13.97%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00237_shp0p782_actor.weights.h5 (Sharpe=0.782, MDD=17.55%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00240_shp0p966_actor.weights.h5 (Sharpe=0.966, MDD=13.36%)
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 240 | Time: 11479.7s
   📊 Metrics: Return=+65.92% | Sharpe=0.966 | DD=13.36% | Turnover=17.80%
   🎚️ Intra-Step TAPE: potential=0.3049 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1856 | critic_loss=0.1373 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0687 | risk_aux_total=0.1068 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.7728 | cvar_loss=0.1064 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=0.90 | std=0.37 | range=[0.35, 3.88]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 8.17% / trig 19.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4944
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00243_shp0p736_actor.weights.h5 (Sharpe=0.736, MDD=9.90%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00254_shp0p952_actor.weights.h5 (Sharpe=0.952, MDD=13.77%)
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 256 | Time: 12278.5s
   📊 Metrics: Return=+4.33% | Sharpe=0.054 | DD=38.67% | Turnover=16.51%
   🎚️ Intra-Step TAPE: potential=0.2115 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2259 | critic_loss=0.0469 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0235 | risk_aux_total=0.1563 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.5966 | cvar_loss=0.1558 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.40 | std=1.04 | range=[0.64, 7.70]
   🔒 Drawdown λ snapshot=0.139 (peak 0.139, dd 22.74% / trig 19.00%) | terminal=0.629 (peak 0.629) | TAPE=0.2193
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00257_shp0p743_actor.weights.h5 (Sharpe=0.743, MDD=13.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00260_shp0p721_actor.weights.h5 (Sharpe=0.721, MDD=14.48%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00261_shp1p125_actor.weights.h5 (Sharpe=1.125, MDD=13.18%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00268_shp0p963_actor.weights.h5 (Sharpe=0.963, MDD=12.84%)

📚 EPISODE HORIZON UPDATE at 240,912 steps:
   Episode horizon: 1053 steps

📚 EPISODE HORIZON UPDATE at 242,424 steps:
   Episode horizon: 1127 steps
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 268 | Time: 13079.1s
   📊 Metrics: Return=+63.75% | Sharpe=0.963 | DD=12.84% | Turnover=15.98%
   🎚️ Intra-Step TAPE: potential=0.6325 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1902 | critic_loss=0.0150 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.1184 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.9657 | cvar_loss=0.1179 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.39 | std=0.86 | range=[0.66, 8.01]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00270_shp0p838_actor.weights.h5 (Sharpe=0.838, MDD=13.84%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00271_shp0p820_actor.weights.h5 (Sharpe=0.820, MDD=13.81%)

📚 EPISODE HORIZON UPDATE at 243,936 steps:
   Episode horizon: 1202 steps

📚 EPISODE HORIZON UPDATE at 245,448 steps:
   Episode horizon: 1276 steps

📚 EPISODE HORIZON UPDATE at 246,960 steps:
   Episode horizon: 1350 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00273_shp0p765_actor.weights.h5 (Sharpe=0.765, MDD=13.03%)

📚 EPISODE HORIZON UPDATE at 248,472 steps:
   Episode horizon: 1425 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00275_shp0p836_actor.weights.h5 (Sharpe=0.836, MDD=13.69%)

📚 EPISODE HORIZON UPDATE at 249,984 steps:
   Episode horizon: 1499 steps

📚 EPISODE HORIZON UPDATE at 251,496 steps:
   Episode horizon: 1500 steps
[CYCLE] Update 220/348 | Step 257,544/500,000 | Episode 280 | Time: 13880.1s
   📊 Metrics: Return=+62.39% | Sharpe=0.404 | DD=46.39% | Turnover=16.55%
   🎚️ Intra-Step TAPE: potential=0.2345 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2092 | critic_loss=0.0126 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0063 | risk_aux_total=0.1285 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=2.1319 | cvar_loss=0.1279 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.67 | std=1.49 | range=[0.70, 10.02]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00286_shp0p800_actor.weights.h5 (Sharpe=0.800, MDD=12.89%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00287_shp0p871_actor.weights.h5 (Sharpe=0.871, MDD=12.23%)
[CYCLE] Update 230/348 | Step 272,664/500,000 | Episode 289 | Time: 14675.3s
   📊 Metrics: Return=+56.32% | Sharpe=0.380 | DD=43.18% | Turnover=14.83%
   🎚️ Intra-Step TAPE: potential=0.5863 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2246 | critic_loss=0.0150 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.1524 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=2.5309 | cvar_loss=0.1519 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.38 | std=1.36 | range=[0.56, 9.22]
   🔒 Drawdown λ snapshot=2.163 (peak 2.163, dd 26.99% / trig 19.00%) | terminal=2.353 (peak 2.450) | TAPE=0.2516
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00297_shp0p859_actor.weights.h5 (Sharpe=0.859, MDD=11.49%)
[CYCLE] Update 240/348 | Step 287,784/500,000 | Episode 300 | Time: 15471.4s
   📊 Metrics: Return=+24.44% | Sharpe=0.184 | DD=45.36% | Turnover=14.77%
   🎚️ Intra-Step TAPE: potential=0.7546 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1648 | critic_loss=0.0117 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0914 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.5170 | cvar_loss=0.0910 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.14 | std=0.47 | range=[0.46, 5.58]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00302_shp0p710_actor.weights.h5 (Sharpe=0.710, MDD=14.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00304_shp0p775_actor.weights.h5 (Sharpe=0.775, MDD=15.11%)

📚 TURNOVER CURRICULUM UPDATE at 301,392 steps:
   Turnover penalty scalar: 0.9

📚 PPO ROLLOUT UPDATE at 301,392 steps:
   Timesteps per update: 2016

📚 PPO BATCH SIZE UPDATE at 301,392 steps:
   Batch size: 504
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00310_shp0p765_actor.weights.h5 (Sharpe=0.765, MDD=13.65%)
[CYCLE] Update 250/348 | Step 303,408/500,000 | Episode 312 | Time: 16292.9s
   📊 Metrics: Return=+88.44% | Sharpe=0.658 | DD=24.62% | Turnover=16.71%
   🎚️ Intra-Step TAPE: potential=0.2366 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1469 | critic_loss=0.1065 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0532 | risk_aux_total=0.0771 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.2786 | cvar_loss=0.0767 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.30 | std=0.50 | range=[0.50, 9.13]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 9.66% / trig 19.00%) | terminal=0.000 (peak 1.359) | TAPE=0.3203
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00321_shp0p734_actor.weights.h5 (Sharpe=0.734, MDD=14.28%)
[CYCLE] Update 260/348 | Step 323,568/500,000 | Episode 324 | Time: 17271.5s
   📊 Metrics: Return=+34.51% | Sharpe=0.251 | DD=43.48% | Turnover=13.31%
   🎚️ Intra-Step TAPE: potential=0.6546 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1771 | critic_loss=0.0099 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.1033 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.7143 | cvar_loss=0.1029 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.21 | std=1.12 | range=[0.51, 10.89]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00328_shp0p802_actor.weights.h5 (Sharpe=0.802, MDD=13.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00329_shp0p752_actor.weights.h5 (Sharpe=0.752, MDD=13.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00332_shp0p896_actor.weights.h5 (Sharpe=0.896, MDD=12.35%)
[CYCLE] Update 270/348 | Step 343,728/500,000 | Episode 336 | Time: 18254.3s
   📊 Metrics: Return=+38.30% | Sharpe=0.275 | DD=40.13% | Turnover=16.21%
   🎚️ Intra-Step TAPE: potential=0.7506 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1517 | critic_loss=0.0097 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0831 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.3769 | cvar_loss=0.0826 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.14 | std=0.61 | range=[0.56, 8.12]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00339_shp0p835_actor.weights.h5 (Sharpe=0.835, MDD=13.16%)
   [TOOL] Actor learning rate adjusted to 0.000010 at step 350,000
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00342_shp0p744_actor.weights.h5 (Sharpe=0.744, MDD=14.12%)

🎛️ EXECUTION BETA UPDATE at 351,792 steps:
   action_execution_beta: 0.250 (w_exec=(1-β)w_prev + βw_raw)

[DOWN] PPO GAMMA UPDATE at 351,792 steps:
   gamma: 0.9980

[DOWN] PPO GAE-λ UPDATE at 351,792 steps:
   gae_lambda: 0.9700
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00345_shp0p919_actor.weights.h5 (Sharpe=0.919, MDD=14.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00346_shp0p718_actor.weights.h5 (Sharpe=0.718, MDD=13.81%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00351_shp1p000_actor.weights.h5 (Sharpe=1.000, MDD=13.55%)
[CYCLE] Update 280/348 | Step 363,888/500,000 | Episode 352 | Time: 19236.8s
   📊 Metrics: Return=+33.62% | Sharpe=0.244 | DD=41.13% | Turnover=12.30%
   🎚️ Intra-Step TAPE: potential=0.7428 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1661 | critic_loss=0.0986 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0493 | risk_aux_total=0.0914 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.5170 | cvar_loss=0.0910 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.42 | std=0.93 | range=[0.56, 9.50]
   🔒 Drawdown λ snapshot=0.000 (peak 0.014, dd 0.18% / trig 19.00%) | terminal=0.000 (peak 2.266) | TAPE=0.2300
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00355_shp0p837_actor.weights.h5 (Sharpe=0.837, MDD=23.21%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00363_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=14.13%)
[CYCLE] Update 290/348 | Step 384,048/500,000 | Episode 364 | Time: 20205.9s
   📊 Metrics: Return=+82.66% | Sharpe=0.698 | DD=13.77% | Turnover=13.71%
   🎚️ Intra-Step TAPE: potential=0.5557 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1461 | critic_loss=0.0977 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0488 | risk_aux_total=0.0746 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.2361 | cvar_loss=0.0742 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.06 | std=0.25 | range=[0.54, 3.45]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00365_shp0p730_actor.weights.h5 (Sharpe=0.730, MDD=13.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00367_shp0p820_actor.weights.h5 (Sharpe=0.820, MDD=13.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00368_shp0p870_actor.weights.h5 (Sharpe=0.870, MDD=13.06%)

📚 EPISODE HORIZON UPDATE at 390,096 steps:
   Episode horizon: 1525 steps

📚 EPISODE HORIZON UPDATE at 392,112 steps:
   Episode horizon: 2044 steps

📚 EPISODE HORIZON UPDATE at 394,128 steps:
   Episode horizon: 2564 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00369_shp0p789_actor.weights.h5 (Sharpe=0.789, MDD=13.94%)

📚 EPISODE HORIZON UPDATE at 396,144 steps:
   Episode horizon: 3084 steps

📚 EPISODE HORIZON UPDATE at 398,160 steps:
   Episode horizon: 3604 steps

📚 TURNOVER CURRICULUM UPDATE at 400,176 steps:
   Turnover penalty scalar: 1.0

📚 EPISODE HORIZON UPDATE at 400,176 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00372_shp0p966_actor.weights.h5 (Sharpe=0.966, MDD=13.06%)

📚 EPISODE HORIZON UPDATE at 402,192 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 404,208 steps:
   Episode horizon set to full dataset
[CYCLE] Update 300/348 | Step 404,208/500,000 | Episode 373 | Time: 21171.7s
   📊 Metrics: Return=+460.83% | Sharpe=0.648 | DD=44.29% | Turnover=13.82%
   🎚️ Intra-Step TAPE: potential=0.7533 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1616 | critic_loss=0.1149 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0575 | risk_aux_total=0.0918 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.5222 | cvar_loss=0.0913 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.27 | std=0.94 | range=[0.58, 9.23]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.67% / trig 19.00%) | terminal=0.000 (peak 2.802) | TAPE=0.3124
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5 (Sharpe=1.215, MDD=12.92%)

📚 EPISODE HORIZON UPDATE at 406,224 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00375_shp1p012_actor.weights.h5 (Sharpe=1.012, MDD=13.23%)

📚 EPISODE HORIZON UPDATE at 408,240 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 410,256 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00377_shp0p767_actor.weights.h5 (Sharpe=0.767, MDD=13.77%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00378_shp0p824_actor.weights.h5 (Sharpe=0.824, MDD=13.50%)

📚 EPISODE HORIZON UPDATE at 412,272 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00379_shp0p881_actor.weights.h5 (Sharpe=0.881, MDD=13.81%)

📚 EPISODE HORIZON UPDATE at 414,288 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00380_shp1p015_actor.weights.h5 (Sharpe=1.015, MDD=13.93%)

📚 EPISODE HORIZON UPDATE at 416,304 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00381_shp1p088_actor.weights.h5 (Sharpe=1.088, MDD=13.32%)

📚 EPISODE HORIZON UPDATE at 418,320 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00382_shp0p977_actor.weights.h5 (Sharpe=0.977, MDD=13.42%)

📚 EPISODE HORIZON UPDATE at 420,336 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00383_shp0p908_actor.weights.h5 (Sharpe=0.908, MDD=13.71%)

📚 EPISODE HORIZON UPDATE at 422,352 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 424,368 steps:
   Episode horizon set to full dataset
[CYCLE] Update 310/348 | Step 424,368/500,000 | Episode 384 | Time: 22143.1s
   📊 Metrics: Return=+365.16% | Sharpe=0.596 | DD=45.72% | Turnover=13.63%
   🎚️ Intra-Step TAPE: potential=0.4366 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2093 | critic_loss=0.0113 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0056 | risk_aux_total=0.1336 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.2177 | cvar_loss=0.1331 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.67 | std=1.64 | range=[0.56, 11.45]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00385_shp1p060_actor.weights.h5 (Sharpe=1.060, MDD=13.14%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00386_shp0p856_actor.weights.h5 (Sharpe=0.856, MDD=12.91%)

📚 EPISODE HORIZON UPDATE at 426,384 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 428,400 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 430,416 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00387_shp0p886_actor.weights.h5 (Sharpe=0.886, MDD=13.11%)

📚 EPISODE HORIZON UPDATE at 432,432 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00388_shp0p911_actor.weights.h5 (Sharpe=0.911, MDD=14.05%)

📚 EPISODE HORIZON UPDATE at 434,448 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 436,464 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 438,480 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00391_shp0p846_actor.weights.h5 (Sharpe=0.846, MDD=13.27%)

📚 EPISODE HORIZON UPDATE at 440,496 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 442,512 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 444,528 steps:
   Episode horizon set to full dataset
[CYCLE] Update 320/348 | Step 444,528/500,000 | Episode 392 | Time: 23118.3s
   📊 Metrics: Return=+198.12% | Sharpe=0.481 | DD=45.52% | Turnover=13.39%
   🎚️ Intra-Step TAPE: potential=0.4527 | delta_reward=+0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1585 | critic_loss=0.0906 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0453 | risk_aux_total=0.0882 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.4631 | cvar_loss=0.0878 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.28 | std=0.49 | range=[0.53, 9.41]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 19.00%) | terminal=0.000 (peak 3.189) | TAPE=0.2628
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00393_shp0p864_actor.weights.h5 (Sharpe=0.864, MDD=13.70%)

📚 EPISODE HORIZON UPDATE at 446,544 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00395_shp0p775_actor.weights.h5 (Sharpe=0.775, MDD=13.46%)

📚 EPISODE HORIZON UPDATE at 448,560 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5 (Sharpe=1.102, MDD=12.82%)

📚 EPISODE HORIZON UPDATE at 450,576 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 452,592 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00397_shp0p908_actor.weights.h5 (Sharpe=0.908, MDD=13.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5 (Sharpe=1.259, MDD=12.59%)

📚 EPISODE HORIZON UPDATE at 454,608 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00399_shp0p742_actor.weights.h5 (Sharpe=0.742, MDD=22.23%)

📚 EPISODE HORIZON UPDATE at 456,624 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 458,640 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00401_shp0p974_actor.weights.h5 (Sharpe=0.974, MDD=12.13%)

📚 EPISODE HORIZON UPDATE at 460,656 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00402_shp0p906_actor.weights.h5 (Sharpe=0.906, MDD=13.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00403_shp0p808_actor.weights.h5 (Sharpe=0.808, MDD=14.01%)

📚 EPISODE HORIZON UPDATE at 462,672 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 464,688 steps:
   Episode horizon set to full dataset
[CYCLE] Update 330/348 | Step 464,688/500,000 | Episode 403 | Time: 24115.9s
   📊 Metrics: Return=+168.95% | Sharpe=0.808 | DD=14.01% | Turnover=13.49%
   🎚️ Intra-Step TAPE: potential=0.2365 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1595 | critic_loss=0.0107 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0881 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.4616 | cvar_loss=0.0877 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.33 | std=0.61 | range=[0.62, 7.78]

📚 EPISODE HORIZON UPDATE at 466,704 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00404_shp0p978_actor.weights.h5 (Sharpe=0.978, MDD=12.37%)

📚 EPISODE HORIZON UPDATE at 468,720 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00405_shp1p040_actor.weights.h5 (Sharpe=1.040, MDD=13.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00406_shp0p925_actor.weights.h5 (Sharpe=0.925, MDD=13.40%)

📚 EPISODE HORIZON UPDATE at 470,736 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5 (Sharpe=1.103, MDD=12.78%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5 (Sharpe=1.133, MDD=13.15%)

📚 EPISODE HORIZON UPDATE at 472,752 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 474,768 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 476,784 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00411_shp0p951_actor.weights.h5 (Sharpe=0.951, MDD=12.75%)

📚 EPISODE HORIZON UPDATE at 478,800 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00412_shp0p958_actor.weights.h5 (Sharpe=0.958, MDD=12.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00413_shp0p851_actor.weights.h5 (Sharpe=0.851, MDD=13.63%)

📚 EPISODE HORIZON UPDATE at 480,816 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00414_shp0p813_actor.weights.h5 (Sharpe=0.813, MDD=12.96%)

📚 EPISODE HORIZON UPDATE at 482,832 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 484,848 steps:
   Episode horizon set to full dataset
[CYCLE] Update 340/348 | Step 484,848/500,000 | Episode 415 | Time: 25102.9s
   📊 Metrics: Return=+157.42% | Sharpe=0.436 | DD=44.10% | Turnover=13.10%
   🎚️ Intra-Step TAPE: potential=0.3471 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1424 | critic_loss=0.0471 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0235 | risk_aux_total=0.0736 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.2207 | cvar_loss=0.0732 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.30 | std=0.37 | range=[0.73, 5.10]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 19.00%) | terminal=0.000 (peak 3.096) | TAPE=0.2531

📚 EPISODE HORIZON UPDATE at 486,864 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00416_shp0p867_actor.weights.h5 (Sharpe=0.867, MDD=14.70%)

📚 EPISODE HORIZON UPDATE at 488,880 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 490,896 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00417_shp0p763_actor.weights.h5 (Sharpe=0.763, MDD=14.79%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00419_shp0p922_actor.weights.h5 (Sharpe=0.922, MDD=12.87%)

📚 EPISODE HORIZON UPDATE at 492,912 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 494,928 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 496,944 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00421_shp0p779_actor.weights.h5 (Sharpe=0.779, MDD=13.84%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00422_shp0p897_actor.weights.h5 (Sharpe=0.897, MDD=12.41%)

📚 EPISODE HORIZON UPDATE at 498,960 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 500,000 steps:
   Episode horizon set to full dataset
[CYCLE] Update 348/348 | Step 500,000/500,000 | Episode 422 | Time: 25865.7s
   📊 Metrics: Return=+86.80% | Sharpe=0.897 | DD=12.41% | Turnover=13.27%
   🎚️ Intra-Step TAPE: potential=0.6047 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1009 | critic_loss=0.0442 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0221 | risk_aux_total=0.0636 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.0534 | cvar_loss=0.0632 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.65 | std=0.40 | range=[0.98, 5.16]

[OK] THREE-COMPONENT TAPE v3 training completed!
   Total episodes: 422
   Total timesteps: 500,000
   Training time: 25865.67s (431.09min)
📊 Training summary saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260303_112113_summary.csv
💾 Final models saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00422_shp0p897_actor.weights.h5, /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00422_shp0p897_critic.weights.h5
🎯 Default selected checkpoint: final high-watermark-style checkpoint
[OK] Training complete
checkpoint_prefix: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00422_shp0p897