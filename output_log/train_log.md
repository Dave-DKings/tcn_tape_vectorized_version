[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
[OK] Actuarial feature check passed: {'Actuarial_Reserve_Severity': 54767, 'Actuarial_Prob_30d': 54767, 'Actuarial_Prob_60d': 54767, 'Actuarial_Expected_Recovery': 54767}
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
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260308_052615_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260308_052615_step_diagnostics.csv

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
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260308_052615_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260308_052615_metadata.json
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp0p719_actor.weights.h5 (Sharpe=0.719, MDD=11.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00003_shp1p254_actor.weights.h5 (Sharpe=1.254, MDD=8.95%)
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 1018.2s
   📊 Metrics: Return=-0.62% | Sharpe=-0.078 | DD=17.91% | Turnover=61.79%
   🎚️ Intra-Step TAPE: potential=0.7399 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0834 | critic_loss=0.5000 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2500 | risk_aux_total=0.0764 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.8969 | cvar_loss=0.0759 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.78 | std=1.05 | range=[0.43, 6.27]
   🧭 Regime Start Dist (train resets): high_vol=6 (37.5%), low_vol=6 (37.5%), medium_vol=4 (25.0%)
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 2009.3s
   📊 Metrics: Return=+1.28% | Sharpe=-0.074 | DD=13.01% | Turnover=53.76%
   🎚️ Intra-Step TAPE: potential=0.4056 | delta_reward=+0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0767 | critic_loss=0.1877 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0938 | risk_aux_total=0.0648 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.6070 | cvar_loss=0.0643 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.43 | std=1.43 | range=[0.29, 7.69]
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=11 (39.3%), medium_vol=7 (25.0%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 3006.7s
   📊 Metrics: Return=-5.16% | Sharpe=-0.094 | DD=30.64% | Turnover=32.34%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1151 | critic_loss=0.2946 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1473 | risk_aux_total=0.1075 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=2.6686 | cvar_loss=0.1067 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.24 | std=1.57 | range=[0.28, 9.20]
   🧭 Regime Start Dist (train resets): high_vol=19 (43.2%), low_vol=14 (31.8%), medium_vol=11 (25.0%)
   🔒 Drawdown λ snapshot=0.025 (peak 0.025, dd 0.00% / trig 21.00%) | terminal=0.172 (peak 0.172) | TAPE=0.2264
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 4006.4s
   📊 Metrics: Return=-12.57% | Sharpe=-0.200 | DD=39.43% | Turnover=34.45%
   🎚️ Intra-Step TAPE: potential=0.6735 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0879 | critic_loss=0.1231 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0616 | risk_aux_total=0.0819 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=2.0256 | cvar_loss=0.0810 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.41 | std=4.54 | range=[0.24, 24.38]
   🧭 Regime Start Dist (train resets): high_vol=24 (42.9%), low_vol=18 (32.1%), medium_vol=14 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00057_shp0p834_actor.weights.h5 (Sharpe=0.834, MDD=12.88%)
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 5005.4s
   📊 Metrics: Return=-7.43% | Sharpe=-0.123 | DD=36.19% | Turnover=27.95%
   🎚️ Intra-Step TAPE: potential=0.2200 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0969 | critic_loss=0.1137 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0569 | risk_aux_total=0.0884 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=2.1882 | cvar_loss=0.0875 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.97 | std=4.71 | range=[0.29, 23.26]
   🧭 Regime Start Dist (train resets): high_vol=27 (39.7%), low_vol=24 (35.3%), medium_vol=17 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00068_shp0p897_actor.weights.h5 (Sharpe=0.897, MDD=12.97%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00069_shp1p005_actor.weights.h5 (Sharpe=1.005, MDD=12.36%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00078_shp0p962_actor.weights.h5 (Sharpe=0.962, MDD=7.99%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 5998.3s
   📊 Metrics: Return=+19.73% | Sharpe=0.421 | DD=12.70% | Turnover=35.00%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0829 | critic_loss=0.1243 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0621 | risk_aux_total=0.0713 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.7668 | cvar_loss=0.0707 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.19 | std=4.24 | range=[0.33, 22.73]
   🧭 Regime Start Dist (train resets): high_vol=34 (40.5%), low_vol=29 (34.5%), medium_vol=21 (25.0%)
   🔒 Drawdown λ snapshot=0.580 (peak 0.580, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2741
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00081_shp0p887_actor.weights.h5 (Sharpe=0.887, MDD=11.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00083_shp0p753_actor.weights.h5 (Sharpe=0.753, MDD=11.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp1p008_actor.weights.h5 (Sharpe=1.008, MDD=6.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00090_shp0p725_actor.weights.h5 (Sharpe=0.725, MDD=12.76%)
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 6998.0s
   📊 Metrics: Return=+9.20% | Sharpe=0.142 | DD=12.67% | Turnover=36.41%
   🎚️ Intra-Step TAPE: potential=0.2493 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0653 | critic_loss=0.0986 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0493 | risk_aux_total=0.0549 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.3604 | cvar_loss=0.0544 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.88 | std=3.97 | range=[0.34, 21.61]
   🧭 Regime Start Dist (train resets): high_vol=38 (39.6%), low_vol=35 (36.5%), medium_vol=23 (24.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00096_shp0p906_actor.weights.h5 (Sharpe=0.906, MDD=12.13%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00101_shp0p987_actor.weights.h5 (Sharpe=0.987, MDD=7.67%)
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 7998.6s
   📊 Metrics: Return=+4.24% | Sharpe=0.003 | DD=22.14% | Turnover=24.22%
   🎚️ Intra-Step TAPE: potential=0.3341 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0658 | critic_loss=0.0863 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0431 | risk_aux_total=0.0578 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.4314 | cvar_loss=0.0573 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.48 | std=4.10 | range=[0.49, 22.41]
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=40 (37.0%), medium_vol=26 (24.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00105_shp1p051_actor.weights.h5 (Sharpe=1.051, MDD=7.57%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00107_shp0p765_actor.weights.h5 (Sharpe=0.765, MDD=12.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00117_shp0p774_actor.weights.h5 (Sharpe=0.774, MDD=7.14%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 8997.7s
   📊 Metrics: Return=-3.01% | Sharpe=-0.223 | DD=21.52% | Turnover=28.42%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0606 | critic_loss=0.1742 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0871 | risk_aux_total=0.0481 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.1873 | cvar_loss=0.0475 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.44 | std=5.05 | range=[0.34, 24.93]
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=46 (37.1%), medium_vol=30 (24.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2287

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

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 9991.7s
   📊 Metrics: Return=+17.00% | Sharpe=0.242 | DD=15.24% | Turnover=27.71%
   🎚️ Intra-Step TAPE: potential=0.4837 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0977 | critic_loss=0.1498 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0749 | risk_aux_total=0.0856 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=2.1170 | cvar_loss=0.0847 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.99 | std=6.26 | range=[0.29, 29.20]
   🧭 Regime Start Dist (train resets): high_vol=52 (39.4%), low_vol=47 (35.6%), medium_vol=33 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00134_shp0p907_actor.weights.h5 (Sharpe=0.907, MDD=12.14%)
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 10995.9s
   📊 Metrics: Return=-8.81% | Sharpe=-0.129 | DD=36.36% | Turnover=19.05%
   🎚️ Intra-Step TAPE: potential=0.2253 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1009 | critic_loss=0.1402 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0701 | risk_aux_total=0.0871 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=2.1572 | cvar_loss=0.0863 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=5.21 | std=7.14 | range=[0.38, 29.98]
   🧭 Regime Start Dist (train resets): high_vol=57 (39.6%), low_vol=51 (35.4%), medium_vol=36 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 11.04% / trig 21.00%) | terminal=0.000 (peak 0.516) | TAPE=0.2252
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00141_shp0p888_actor.weights.h5 (Sharpe=0.888, MDD=11.04%)