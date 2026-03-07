[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
[OK] Actuarial feature check passed: {'Actuarial_Prob_60d': 54767, 'Actuarial_Expected_Recovery': 54767, 'Actuarial_Reserve_Severity': 54767, 'Actuarial_Prob_30d': 54767}
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
   ⚙️  Component 4: Execution Inertia (beta=0.60 -> 0.55 => 0.50 => 0.40, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.60@0 => 0.55@100,000 => 0.50@200,000 => 0.40@350,000
   ⚡ Parallel rollout envs: 4
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 25.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🔒 Drawdown dual controller (requested): target=22.00%, tolerance=-1.00% (trigger boundary ≈ 21.00%), lr=0.100, λ_init=0.25, λ_floor=0.00, λ_max=5.00, penalty_coef=1.50
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
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0050
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@150,000 => 0.9980@350,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@150,000 => 0.9700@350,000
   📐 PPO rollout schedule: 1008@0 => 1512@150,000 => 2016@300,000
   🧺 PPO batch-size schedule: 252@0 => 336@150,000 => 504@300,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260307_074452_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260307_074452_step_diagnostics.csv

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
      0+ steps: beta=0.60
      100,000+ steps: beta=0.55
      200,000+ steps: beta=0.50
      350,000+ steps: beta=0.40
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.70, MDD <= 25.0%, skip_on_det_validation=True)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260307_074452_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260307_074452_metadata.json
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00003_shp0p809_actor.weights.h5 (Sharpe=0.809, MDD=7.77%)
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 532.1s
   📊 Metrics: Return=+21.23% | Sharpe=0.382 | DD=14.54% | Turnover=39.93%
   🎚️ Intra-Step TAPE: potential=0.7024 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1467 | critic_loss=0.5688 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2844 | risk_aux_total=0.0766 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.9017 | cvar_loss=0.0761 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.02 | std=0.21 | range=[0.56, 2.02]
   🧭 Regime Start Dist (train resets): high_vol=6 (37.5%), low_vol=6 (37.5%), medium_vol=4 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00014_shp0p794_actor.weights.h5 (Sharpe=0.794, MDD=12.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00017_shp0p949_actor.weights.h5 (Sharpe=0.949, MDD=11.50%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00018_shp0p791_actor.weights.h5 (Sharpe=0.791, MDD=11.52%)
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1028.8s
   📊 Metrics: Return=+28.04% | Sharpe=0.575 | DD=11.47% | Turnover=37.13%
   🎚️ Intra-Step TAPE: potential=0.5959 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1382 | critic_loss=0.1798 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0899 | risk_aux_total=0.0721 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.7920 | cvar_loss=0.0717 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.13 | std=0.28 | range=[0.52, 1.84]
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=11 (39.3%), medium_vol=7 (25.0%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 1526.2s
   📊 Metrics: Return=-22.62% | Sharpe=-0.340 | DD=44.85% | Turnover=35.82%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1844 | critic_loss=0.1426 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0713 | risk_aux_total=0.1140 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=2.8348 | cvar_loss=0.1134 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.59 | std=0.53 | range=[0.66, 3.24]
   🧭 Regime Start Dist (train resets): high_vol=19 (43.2%), low_vol=14 (31.8%), medium_vol=11 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.872 (peak 0.872) | TAPE=0.2205
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00042_shp0p832_actor.weights.h5 (Sharpe=0.832, MDD=15.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00047_shp0p723_actor.weights.h5 (Sharpe=0.723, MDD=8.49%)
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 2034.4s
   📊 Metrics: Return=-19.55% | Sharpe=-0.220 | DD=47.17% | Turnover=35.41%
   🎚️ Intra-Step TAPE: potential=0.2215 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1603 | critic_loss=0.0369 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0184 | risk_aux_total=0.0925 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.2995 | cvar_loss=0.0920 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.21 | std=0.24 | range=[0.61, 2.08]
   🧭 Regime Start Dist (train resets): high_vol=24 (42.9%), low_vol=18 (32.1%), medium_vol=14 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 40 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 2544.2s
   📊 Metrics: Return=-20.81% | Sharpe=-0.246 | DD=45.48% | Turnover=34.75%
   🎚️ Intra-Step TAPE: potential=0.2182 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1722 | critic_loss=0.0580 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0290 | risk_aux_total=0.0996 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.4772 | cvar_loss=0.0991 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.43 | std=0.60 | range=[0.51, 3.84]
   🧭 Regime Start Dist (train resets): high_vol=27 (39.7%), low_vol=24 (35.3%), medium_vol=17 (25.0%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 3053.0s
   📊 Metrics: Return=+20.78% | Sharpe=0.432 | DD=17.20% | Turnover=41.96%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1443 | critic_loss=0.0481 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0240 | risk_aux_total=0.0755 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.8775 | cvar_loss=0.0751 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.88 | std=0.22 | range=[0.39, 1.70]
   🧭 Regime Start Dist (train resets): high_vol=34 (40.5%), low_vol=29 (34.5%), medium_vol=21 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 60 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=3.345 (peak 3.345, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2678
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp1p088_actor.weights.h5 (Sharpe=1.088, MDD=11.73%)
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 3563.4s
   📊 Metrics: Return=+23.41% | Sharpe=0.485 | DD=12.89% | Turnover=34.99%
   🎚️ Intra-Step TAPE: potential=0.2758 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1368 | critic_loss=0.1047 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0523 | risk_aux_total=0.0623 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.5472 | cvar_loss=0.0619 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.45 | std=0.60 | range=[0.49, 3.83]
   🧭 Regime Start Dist (train resets): high_vol=38 (39.6%), low_vol=35 (36.5%), medium_vol=23 (24.0%)
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 4090.1s
   📊 Metrics: Return=+5.14% | Sharpe=0.037 | DD=16.43% | Turnover=38.68%
   🎚️ Intra-Step TAPE: potential=0.2348 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1341 | critic_loss=0.0712 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0356 | risk_aux_total=0.0645 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.6011 | cvar_loss=0.0640 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.44 | std=0.28 | range=[0.66, 2.44]
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=40 (37.0%), medium_vol=26 (24.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00117_shp0p771_actor.weights.h5 (Sharpe=0.771, MDD=8.83%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 4615.0s
   📊 Metrics: Return=+21.98% | Sharpe=0.444 | DD=14.20% | Turnover=40.06%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1295 | critic_loss=0.0959 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0479 | risk_aux_total=0.0578 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.4329 | cvar_loss=0.0573 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.85 | std=0.08 | range=[0.68, 1.12]
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=46 (37.1%), medium_vol=30 (24.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 90 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2910

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

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.5

🎛️ EXECUTION BETA UPDATE at 100,800 steps:
   action_execution_beta: 0.550 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 5132.4s
   📊 Metrics: Return=+21.50% | Sharpe=0.285 | DD=15.94% | Turnover=35.79%
   🎚️ Intra-Step TAPE: potential=0.6468 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1607 | critic_loss=0.1553 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0776 | risk_aux_total=0.0964 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=2.4016 | cvar_loss=0.0961 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.53 | std=0.32 | range=[0.74, 2.82]
   🧭 Regime Start Dist (train resets): high_vol=52 (39.4%), low_vol=47 (35.6%), medium_vol=33 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00130_shp0p717_actor.weights.h5 (Sharpe=0.717, MDD=15.58%)
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 5660.8s
   📊 Metrics: Return=-10.38% | Sharpe=-0.067 | DD=46.73% | Turnover=28.98%
   🎚️ Intra-Step TAPE: potential=0.2191 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1680 | critic_loss=0.0730 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0365 | risk_aux_total=0.0996 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.4797 | cvar_loss=0.0992 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.48 | std=0.41 | range=[0.57, 2.50]
   🧭 Regime Start Dist (train resets): high_vol=57 (39.6%), low_vol=51 (35.4%), medium_vol=36 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 14.17% / trig 21.00%) | terminal=4.701 (peak 5.000) | TAPE=0.2221
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 148 | Time: 6196.1s
   📊 Metrics: Return=+24.19% | Sharpe=0.316 | DD=14.94% | Turnover=33.93%
   🎚️ Intra-Step TAPE: potential=0.2529 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1625 | critic_loss=0.0509 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0254 | risk_aux_total=0.0961 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.3907 | cvar_loss=0.0956 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.05 | std=0.25 | range=[0.60, 2.09]
   🧭 Regime Start Dist (train resets): high_vol=58 (38.2%), low_vol=53 (34.9%), medium_vol=41 (27.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 120 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 160 | Time: 6730.0s
   📊 Metrics: Return=+21.70% | Sharpe=0.276 | DD=16.03% | Turnover=34.43%
   🎚️ Intra-Step TAPE: potential=0.6491 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1708 | critic_loss=0.0748 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0374 | risk_aux_total=0.1019 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=2.5361 | cvar_loss=0.1014 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.34 | std=0.36 | range=[0.64, 2.71]
   🧭 Regime Start Dist (train resets): high_vol=64 (39.0%), low_vol=58 (35.4%), medium_vol=42 (25.6%)
   🔒 Drawdown λ snapshot=0.086 (peak 1.516, dd 0.45% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2569
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00161_shp0p810_actor.weights.h5 (Sharpe=0.810, MDD=13.27%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00166_shp0p769_actor.weights.h5 (Sharpe=0.769, MDD=14.87%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00167_shp0p782_actor.weights.h5 (Sharpe=0.782, MDD=6.89%)
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 168 | Time: 7259.8s
   📊 Metrics: Return=+17.41% | Sharpe=0.227 | DD=17.71% | Turnover=33.67%
   🎚️ Intra-Step TAPE: potential=0.5954 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1333 | critic_loss=0.0615 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0307 | risk_aux_total=0.0650 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.6133 | cvar_loss=0.0645 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.71 | std=0.36 | range=[1.00, 2.88]
   🧭 Regime Start Dist (train resets): high_vol=68 (39.5%), low_vol=61 (35.5%), medium_vol=43 (25.0%)
   [TOOL] Actor learning rate adjusted to 0.000020 at step 150,000

📚 PPO ROLLOUT UPDATE at 150,192 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 150,192 steps:
   Batch size: 336

[DOWN] PPO GAMMA UPDATE at 150,192 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 150,192 steps:
   gae_lambda: 0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00179_shp0p979_actor.weights.h5 (Sharpe=0.979, MDD=11.02%)
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 180 | Time: 7827.3s
   📊 Metrics: Return=+41.44% | Sharpe=0.642 | DD=11.59% | Turnover=30.20%
   🎚️ Intra-Step TAPE: potential=0.2309 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1282 | critic_loss=0.1995 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0998 | risk_aux_total=0.0606 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.5015 | cvar_loss=0.0601 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.65 | std=0.35 | range=[0.81, 3.18]
   🧭 Regime Start Dist (train resets): high_vol=69 (37.5%), low_vol=68 (37.0%), medium_vol=47 (25.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.35% / trig 21.00%) | terminal=0.000 (peak 3.050) | TAPE=0.3603
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00182_shp0p736_actor.weights.h5 (Sharpe=0.736, MDD=17.38%)
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 196 | Time: 8587.9s
   📊 Metrics: Return=+20.83% | Sharpe=0.294 | DD=18.56% | Turnover=29.90%
   🎚️ Intra-Step TAPE: potential=0.6411 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1331 | critic_loss=0.0287 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0143 | risk_aux_total=0.0554 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.3756 | cvar_loss=0.0550 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.83 | std=0.31 | range=[0.90, 3.10]
   🧭 Regime Start Dist (train resets): high_vol=71 (35.5%), low_vol=76 (38.0%), medium_vol=53 (26.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.82% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2583
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 208 | Time: 9336.2s
   📊 Metrics: Return=+36.70% | Sharpe=0.545 | DD=15.05% | Turnover=31.07%
   🎚️ Intra-Step TAPE: potential=0.2613 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1668 | critic_loss=0.0566 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0283 | risk_aux_total=0.1011 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.5151 | cvar_loss=0.1006 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.32 | std=0.43 | range=[0.46, 2.49]
   🧭 Regime Start Dist (train resets): high_vol=75 (35.4%), low_vol=79 (37.3%), medium_vol=58 (27.4%)
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 224 | Time: 10092.7s
   📊 Metrics: Return=+8.90% | Sharpe=0.075 | DD=16.99% | Turnover=34.13%
   🎚️ Intra-Step TAPE: potential=0.2141 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1466 | critic_loss=0.0505 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0252 | risk_aux_total=0.0830 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.0622 | cvar_loss=0.0825 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.03 | std=0.20 | range=[0.53, 2.01]
   🧭 Regime Start Dist (train resets): high_vol=79 (34.6%), low_vol=86 (37.7%), medium_vol=63 (27.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 180 updates. TCN may not be learning asset discrimination.

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.75

🎛️ EXECUTION BETA UPDATE at 200,088 steps:
   action_execution_beta: 0.500 (w_exec=(1-β)w_prev + βw_raw)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00235_shp0p702_actor.weights.h5 (Sharpe=0.702, MDD=13.49%)
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 240 | Time: 10831.3s
   📊 Metrics: Return=-11.25% | Sharpe=-0.087 | DD=47.47% | Turnover=27.85%
   🎚️ Intra-Step TAPE: potential=0.2380 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1568 | critic_loss=0.0590 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0295 | risk_aux_total=0.0861 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=2.1413 | cvar_loss=0.0857 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.68 | std=0.29 | range=[0.95, 2.59]
   🧭 Regime Start Dist (train resets): high_vol=85 (34.8%), low_vol=89 (36.5%), medium_vol=70 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.47% / trig 21.00%) | terminal=4.747 (peak 5.000) | TAPE=0.2242
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00247_shp1p059_actor.weights.h5 (Sharpe=1.059, MDD=9.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00248_shp1p110_actor.weights.h5 (Sharpe=1.110, MDD=7.98%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00250_shp1p068_actor.weights.h5 (Sharpe=1.068, MDD=12.46%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00253_shp0p776_actor.weights.h5 (Sharpe=0.776, MDD=17.06%)
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 256 | Time: 11571.7s
   📊 Metrics: Return=+20.31% | Sharpe=0.282 | DD=17.35% | Turnover=31.26%
   🎚️ Intra-Step TAPE: potential=0.7329 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1599 | critic_loss=0.1055 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0528 | risk_aux_total=0.0831 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=2.0676 | cvar_loss=0.0827 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.15 | std=0.29 | range=[0.58, 2.78]
   🧭 Regime Start Dist (train resets): high_vol=89 (34.2%), low_vol=96 (36.9%), medium_vol=75 (28.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.33% / trig 21.00%) | terminal=0.000 (peak 0.539) | TAPE=0.2597
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00265_shp0p705_actor.weights.h5 (Sharpe=0.705, MDD=15.37%)

📚 EPISODE HORIZON UPDATE at 240,912 steps:
   Episode horizon: 1053 steps

📚 EPISODE HORIZON UPDATE at 242,424 steps:
   Episode horizon: 1127 steps
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 268 | Time: 12307.9s
   📊 Metrics: Return=+43.12% | Sharpe=0.607 | DD=21.44% | Turnover=29.47%
   🎚️ Intra-Step TAPE: potential=0.2195 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1461 | critic_loss=0.0250 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0659 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=1.6376 | cvar_loss=0.0655 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.02 | std=0.28 | range=[0.55, 2.05]
   🧭 Regime Start Dist (train resets): high_vol=93 (34.2%), low_vol=101 (37.1%), medium_vol=78 (28.7%)

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
[CYCLE] Update 220/348 | Step 257,544/500,000 | Episode 280 | Time: 13042.8s
   📊 Metrics: Return=-18.13% | Sharpe=-0.143 | DD=54.05% | Turnover=30.09%
   🎚️ Intra-Step TAPE: potential=0.2412 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1740 | critic_loss=0.0345 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0173 | risk_aux_total=0.1034 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=2.5687 | cvar_loss=0.1027 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.20 | std=0.39 | range=[0.56, 2.65]
   🧭 Regime Start Dist (train resets): high_vol=96 (33.8%), low_vol=104 (36.6%), medium_vol=84 (29.6%)