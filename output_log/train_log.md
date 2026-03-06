🚀 Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
✅ Actuarial feature check passed: {'Actuarial_Prob_60d': 54767, 'Actuarial_Prob_30d': 54767, 'Actuarial_Reserve_Severity': 54767, 'Actuarial_Expected_Recovery': 54767}
✅ Fundamental feature check passed: none present

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
   Gate A: enabled (Sharpe ≤ 0.00 or MDD ≥ 25.0% -> force non-positive terminal bonus)
   Neutral Band: enabled (±0.020 around baseline)
   🔄 Profile Manager: disabled (static profile only)
🎲 Experiment Seed: 6042 (Base: 42, Offset: 6000)
✅ Features: Enhanced (includes 2 covariance eigenvalues)
   Eigenvalues: ['Covariance_Eigenvalue_0', 'Covariance_Eigenvalue_1']
   Train shape: (43757, 66)
   Test shape: (11010, 66)
   🧮 Actuarial columns: 4 detected (enabled=True) | total non-null=219068
      {'Actuarial_Expected_Recovery': 54767, 'Actuarial_Prob_30d': 54767, 'Actuarial_Prob_60d': 54767, 'Actuarial_Reserve_Severity': 54767}

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.35, band=±0.20, scalar=0.75 -> 1.25 → 1.50 → 1.75 → 2.00)
      ↳ Schedule: 0.75@0 → 1.25@30,000 → 1.50@60,000 → 1.75@90,000 → 2.00@120,000
   ⚙️  Component 4: Execution Inertia (beta=0.50 -> 0.40 → 0.30 → 0.25, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.50@0 → 0.40@100,000 → 0.30@200,000 → 0.25@350,000
   ⚡ Parallel rollout envs: 4
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe ≤ 0.00, MDD ≥ 25.0%)
   🧠 Credit Assignment: step reward is computed at each environment step
   🧾 Episode-End Handling: terminal TAPE bonus is added at episode completion only
   ✅ Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🔒 Drawdown dual controller (requested): target=18.00%, tolerance=-1.50% (trigger boundary ≈ 16.50%), lr=0.100, λ_init=0.50, λ_floor=0.00, λ_max=5.00, penalty_coef=1.50
   ✅ Drawdown controller armed in env: target=18.00%, trigger=16.50%, λ_init=0.500, λ_floor=0.000, λ_max=5.00, penalty_coef=1.50
✅ THREE-COMPONENT TAPE v3 Environments created:
   Training: 4400 days
   Parallel train env instances: 4
   Testing: 1101 days

🤖 Creating TCN_FUSION agent with Dirichlet distribution for Exp 6...
✅ Agent created: PPOAgentTF
   🎲 Dirichlet Distribution: ENABLED
   🔧 Actor LR schedule: 0.000030@0 → 0.000020@150,000 → 0.000010@350,000
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
   🧠 Recurrent memory: enabled=False | units=64 | dropout=0.1
   🌐 Regime conditioning: enabled=False | hidden_dim=32 | dropout=0.0
   🧬 State augmentation: enabled=False
   📉 Distributional critic: enabled=False | num_quantiles=17
   🎛️ Dirichlet controls: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Dual-head consistency coef: 0.0
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0050
   📉 PPO gamma schedule: 0.9900@0 → 0.9950@150,000 → 0.9980@350,000
   📉 PPO GAE-λ schedule: 0.9200@0 → 0.9500@150,000 → 0.9700@350,000
   📐 PPO rollout schedule: 1008@0 → 1512@150,000 → 2016@300,000
   🧺 PPO batch-size schedule: 252@0 → 336@150,000 → 504@300,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260302_143707_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260302_143707_step_diagnostics.csv

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
   PPO gamma schedule: 0.9900@0 → 0.9950@150,000 → 0.9980@350,000
   PPO GAE-λ schedule: 0.9200@0 → 0.9500@150,000 → 0.9700@350,000
   📚 Episode Length Curriculum:
      0+ steps: limit=756
      100,000+ steps: limit=1008
      250,000+ steps: limit=1500
      400,000+ steps: limit=full
      ↳ smooth ramp: enabled (overlap=10,000 steps)
   📚 Turnover Scalar Curriculum:
      0+ steps: scalar=0.75
      30,000+ steps: scalar=1.25
      60,000+ steps: scalar=1.50
      90,000+ steps: scalar=1.75
      120,000+ steps: scalar=2.00
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.50
      100,000+ steps: beta=0.40
      200,000+ steps: beta=0.30
      350,000+ steps: beta=0.25
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   ⚠️ Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe ≥ 0.70, MDD ≤ 25.0%, skip_on_det_validation=True)
🧾 Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260302_143707_active_feature_manifest.json
🧾 Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260302_143707_metadata.json
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p013_actor.weights.h5 (Sharpe=1.013, MDD=16.97%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp1p101_actor.weights.h5 (Sharpe=1.101, MDD=11.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p454_actor.weights.h5 (Sharpe=1.454, MDD=11.52%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p744_actor.weights.h5 (Sharpe=0.744, MDD=13.65%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00012_shp0p867_actor.weights.h5 (Sharpe=0.867, MDD=11.33%)
🔄 Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 502.7s
   📊 Metrics: Return=+38.97% | Sharpe=0.867 | DD=11.33% | Turnover=30.31%
   🎚️ Intra-Step TAPE: potential=0.7259 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1774 | critic_loss=0.4577 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2288 | risk_aux_total=0.0995 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.6580 | cvar_loss=0.0995 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.14 | std=0.44 | range=[0.43, 3.94]
🔄 Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 986.1s
   📊 Metrics: Return=-31.19% | Sharpe=-0.462 | DD=45.23% | Turnover=29.07%
   🎚️ Intra-Step TAPE: potential=0.7423 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1573 | critic_loss=0.2016 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1008 | risk_aux_total=0.0857 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.4288 | cvar_loss=0.0857 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.05 | std=0.31 | range=[0.48, 2.86]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00029_shp1p374_actor.weights.h5 (Sharpe=1.374, MDD=10.09%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00036_shp0p774_actor.weights.h5 (Sharpe=0.774, MDD=10.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00037_shp0p762_actor.weights.h5 (Sharpe=0.762, MDD=16.11%)

📚 TURNOVER CURRICULUM UPDATE at 30,240 steps:
   Turnover penalty scalar: 1.25
🔄 Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 1445.1s
   📊 Metrics: Return=-13.61% | Sharpe=-0.141 | DD=49.09% | Turnover=27.14%
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2108 | critic_loss=0.4864 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2432 | risk_aux_total=0.1422 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.3702 | cvar_loss=0.1422 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.37 | std=0.54 | range=[0.49, 4.15]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=3.601 (peak 3.601) | TAPE=0.2079
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00051_shp1p009_actor.weights.h5 (Sharpe=1.009, MDD=7.26%)
🔄 Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 1898.7s
   📊 Metrics: Return=+30.94% | Sharpe=0.676 | DD=15.40% | Turnover=32.07%
   🎚️ Intra-Step TAPE: potential=0.2395 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2172 | critic_loss=0.2764 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1382 | risk_aux_total=0.1407 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.3454 | cvar_loss=0.1407 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.31 | std=0.46 | range=[0.51, 3.30]
🔄 Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 2349.8s
   📊 Metrics: Return=+11.41% | Sharpe=0.196 | DD=16.04% | Turnover=30.30%
   🎚️ Intra-Step TAPE: potential=0.7342 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2044 | critic_loss=0.1071 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0535 | risk_aux_total=0.1382 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.3027 | cvar_loss=0.1382 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.20 | std=0.31 | range=[0.49, 2.39]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00072_shp1p297_actor.weights.h5 (Sharpe=1.297, MDD=10.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00075_shp0p851_actor.weights.h5 (Sharpe=0.851, MDD=13.93%)

📚 TURNOVER CURRICULUM UPDATE at 60,480 steps:
   Turnover penalty scalar: 1.5
🔄 Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 2808.0s
   📊 Metrics: Return=+13.48% | Sharpe=0.242 | DD=16.76% | Turnover=30.01%
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1882 | critic_loss=0.4639 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2320 | risk_aux_total=0.1178 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.9638 | cvar_loss=0.1178 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.46 | std=0.30 | range=[0.80, 2.89]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2521
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00082_shp0p757_actor.weights.h5 (Sharpe=0.757, MDD=11.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp0p941_actor.weights.h5 (Sharpe=0.941, MDD=11.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp0p977_actor.weights.h5 (Sharpe=0.977, MDD=13.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00092_shp0p820_actor.weights.h5 (Sharpe=0.820, MDD=13.54%)
🔄 Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 3288.3s
   📊 Metrics: Return=+37.93% | Sharpe=0.820 | DD=13.54% | Turnover=26.80%
   🎚️ Intra-Step TAPE: potential=0.2467 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1665 | critic_loss=0.1261 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0630 | risk_aux_total=0.0890 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.4841 | cvar_loss=0.0890 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.62 | std=0.58 | range=[0.48, 4.38]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00094_shp0p950_actor.weights.h5 (Sharpe=0.950, MDD=10.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00097_shp0p832_actor.weights.h5 (Sharpe=0.832, MDD=11.14%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00098_shp1p098_actor.weights.h5 (Sharpe=1.098, MDD=8.74%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00099_shp0p849_actor.weights.h5 (Sharpe=0.849, MDD=11.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00100_shp1p076_actor.weights.h5 (Sharpe=1.076, MDD=8.11%)
🔄 Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 3767.5s
   📊 Metrics: Return=+18.60% | Sharpe=0.365 | DD=18.81% | Turnover=30.47%
   🎚️ Intra-Step TAPE: potential=0.6510 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1271 | critic_loss=0.0825 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0412 | risk_aux_total=0.0563 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.9380 | cvar_loss=0.0563 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.17 | std=0.24 | range=[0.45, 1.97]
   ⚠️  WARNING: Alpha std < 0.25 after 80 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00107_shp0p830_actor.weights.h5 (Sharpe=0.830, MDD=9.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00108_shp0p886_actor.weights.h5 (Sharpe=0.886, MDD=8.92%)

📚 TURNOVER CURRICULUM UPDATE at 90,720 steps:
   Turnover penalty scalar: 1.75

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
🔄 Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 4233.1s
   📊 Metrics: Return=-7.44% | Sharpe=-0.047 | DD=48.55% | Turnover=31.03%
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1791 | critic_loss=0.0648 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0324 | risk_aux_total=0.1058 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.7639 | cvar_loss=0.1058 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.13 | std=0.42 | range=[0.32, 2.19]
   🔒 Drawdown λ snapshot=0.626 (peak 0.626, dd 0.00% / trig 16.50%) | terminal=4.075 (peak 4.075) | TAPE=0.2057

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00122_shp0p704_actor.weights.h5 (Sharpe=0.704, MDD=13.03%)

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00125_shp0p784_actor.weights.h5 (Sharpe=0.784, MDD=9.56%)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps

🎛️ EXECUTION BETA UPDATE at 100,800 steps:
   action_execution_beta: 0.400 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
🔄 Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 4690.0s
   📊 Metrics: Return=+31.07% | Sharpe=0.492 | DD=14.72% | Turnover=28.66%
   🎚️ Intra-Step TAPE: potential=0.2011 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2079 | critic_loss=0.0363 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0182 | risk_aux_total=0.1421 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.3679 | cvar_loss=0.1421 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.00 | std=0.32 | range=[0.40, 1.91]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00133_shp0p833_actor.weights.h5 (Sharpe=0.833, MDD=13.57%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00136_shp0p701_actor.weights.h5 (Sharpe=0.701, MDD=15.51%)
🔄 Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 5147.4s
   📊 Metrics: Return=-5.28% | Sharpe=-0.024 | DD=48.83% | Turnover=24.04%
   🎚️ Intra-Step TAPE: potential=0.7203 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1459 | critic_loss=0.2212 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1106 | risk_aux_total=0.0797 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.3283 | cvar_loss=0.0797 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.07 | std=0.21 | range=[0.63, 2.25]
   ⚠️  WARNING: Alpha std < 0.25 after 110 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.35% / trig 16.50%) | terminal=5.000 (peak 5.000) | TAPE=0.2122
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00143_shp0p710_actor.weights.h5 (Sharpe=0.710, MDD=13.73%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00144_shp1p107_actor.weights.h5 (Sharpe=1.107, MDD=12.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00147_shp0p723_actor.weights.h5 (Sharpe=0.723, MDD=13.66%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00148_shp0p785_actor.weights.h5 (Sharpe=0.785, MDD=14.82%)

📚 TURNOVER CURRICULUM UPDATE at 120,960 steps:
   Turnover penalty scalar: 2.0
🔄 Update 120/348 | Step 120,960/500,000 | Episode 148 | Time: 5613.5s
   📊 Metrics: Return=+68.22% | Sharpe=0.785 | DD=14.82% | Turnover=22.33%
   🎚️ Intra-Step TAPE: potential=0.2347 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1444 | critic_loss=0.0819 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0410 | risk_aux_total=0.0726 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.2094 | cvar_loss=0.0726 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.09 | std=0.29 | range=[0.61, 2.85]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00149_shp1p026_actor.weights.h5 (Sharpe=1.026, MDD=14.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00152_shp1p076_actor.weights.h5 (Sharpe=1.076, MDD=9.72%)
🔄 Update 130/348 | Step 131,040/500,000 | Episode 160 | Time: 6073.1s
   📊 Metrics: Return=+3.00% | Sharpe=0.055 | DD=46.98% | Turnover=18.50%
   🎚️ Intra-Step TAPE: potential=0.5552 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1526 | critic_loss=0.1518 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0759 | risk_aux_total=0.0814 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.3575 | cvar_loss=0.0814 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.39 | std=0.58 | range=[0.43, 3.45]
   🔒 Drawdown λ snapshot=2.065 (peak 3.226, dd 0.23% / trig 16.50%) | terminal=4.298 (peak 4.298) | TAPE=0.2162
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00161_shp0p820_actor.weights.h5 (Sharpe=0.820, MDD=15.74%)
🔄 Update 140/348 | Step 141,120/500,000 | Episode 168 | Time: 6530.2s
   📊 Metrics: Return=+45.36% | Sharpe=0.491 | DD=30.23% | Turnover=23.59%
   🎚️ Intra-Step TAPE: potential=0.7448 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1652 | critic_loss=0.0774 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0387 | risk_aux_total=0.0977 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.6280 | cvar_loss=0.0977 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.11 | std=0.36 | range=[0.65, 3.29]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00176_shp0p775_actor.weights.h5 (Sharpe=0.775, MDD=14.16%)
   🔧 Actor learning rate adjusted to 0.000020 at step 150,000

📚 PPO ROLLOUT UPDATE at 150,192 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 150,192 steps:
   Batch size: 336

📉 PPO GAMMA UPDATE at 150,192 steps:
   gamma: 0.9950

📉 PPO GAE-λ UPDATE at 150,192 steps:
   gae_lambda: 0.9500
🔄 Update 150/348 | Step 151,704/500,000 | Episode 180 | Time: 7021.8s
   📊 Metrics: Return=-16.51% | Sharpe=-0.147 | DD=49.06% | Turnover=17.00%
   🎚️ Intra-Step TAPE: potential=0.6166 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2296 | critic_loss=0.2070 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1035 | risk_aux_total=0.1507 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.5122 | cvar_loss=0.1507 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.02 | std=1.26 | range=[0.53, 6.29]
   🔒 Drawdown λ snapshot=1.291 (peak 1.484, dd 5.94% / trig 16.50%) | terminal=5.000 (peak 5.000) | TAPE=0.2082
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00187_shp0p759_actor.weights.h5 (Sharpe=0.759, MDD=16.49%)
🔄 Update 160/348 | Step 166,824/500,000 | Episode 196 | Time: 7688.5s
   📊 Metrics: Return=-1.03% | Sharpe=0.014 | DD=49.64% | Turnover=22.46%
   🎚️ Intra-Step TAPE: potential=0.7568 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2155 | critic_loss=0.0709 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0354 | risk_aux_total=0.1370 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.2840 | cvar_loss=0.1370 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.30 | std=0.47 | range=[0.52, 3.50]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.07% / trig 16.50%) | terminal=4.894 (peak 4.894) | TAPE=0.2141
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00198_shp0p805_actor.weights.h5 (Sharpe=0.805, MDD=11.72%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00204_shp1p277_actor.weights.h5 (Sharpe=1.277, MDD=6.93%)
🔄 Update 170/348 | Step 181,944/500,000 | Episode 208 | Time: 8365.0s
   📊 Metrics: Return=+45.13% | Sharpe=0.669 | DD=13.21% | Turnover=23.15%
   🎚️ Intra-Step TAPE: potential=0.2232 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1400 | critic_loss=0.0249 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0778 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.2961 | cvar_loss=0.0778 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.59 | std=0.45 | range=[0.57, 3.12]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00217_shp0p857_actor.weights.h5 (Sharpe=0.857, MDD=16.48%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00220_shp0p906_actor.weights.h5 (Sharpe=0.906, MDD=12.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00222_shp0p786_actor.weights.h5 (Sharpe=0.786, MDD=16.95%)
🔄 Update 180/348 | Step 197,064/500,000 | Episode 224 | Time: 9043.5s
   📊 Metrics: Return=+59.68% | Sharpe=0.611 | DD=30.26% | Turnover=22.98%
   🎚️ Intra-Step TAPE: potential=0.7476 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1647 | critic_loss=0.0303 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0152 | risk_aux_total=0.0918 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.5297 | cvar_loss=0.0918 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.10 | std=0.35 | range=[0.53, 2.70]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00226_shp0p802_actor.weights.h5 (Sharpe=0.802, MDD=13.65%)

🎛️ EXECUTION BETA UPDATE at 200,088 steps:
   action_execution_beta: 0.300 (w_exec=(1-β)w_prev + βw_raw)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00229_shp0p789_actor.weights.h5 (Sharpe=0.789, MDD=12.48%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00232_shp0p876_actor.weights.h5 (Sharpe=0.876, MDD=13.35%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00235_shp0p718_actor.weights.h5 (Sharpe=0.718, MDD=13.49%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00238_shp0p839_actor.weights.h5 (Sharpe=0.839, MDD=13.37%)
🔄 Update 190/348 | Step 212,184/500,000 | Episode 240 | Time: 9729.4s
   📊 Metrics: Return=-10.77% | Sharpe=-0.089 | DD=46.91% | Turnover=14.99%
   🎚️ Intra-Step TAPE: potential=0.3351 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1812 | critic_loss=0.0465 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0232 | risk_aux_total=0.1089 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.8144 | cvar_loss=0.1089 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.15 | std=0.43 | range=[0.44, 3.60]
   🔒 Drawdown λ snapshot=1.422 (peak 2.843, dd 10.76% / trig 16.50%) | terminal=4.673 (peak 5.000) | TAPE=0.2107
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00243_shp0p753_actor.weights.h5 (Sharpe=0.753, MDD=14.52%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00245_shp0p768_actor.weights.h5 (Sharpe=0.768, MDD=12.94%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00247_shp0p819_actor.weights.h5 (Sharpe=0.819, MDD=12.30%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00248_shp0p771_actor.weights.h5 (Sharpe=0.771, MDD=13.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00251_shp0p722_actor.weights.h5 (Sharpe=0.722, MDD=13.16%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00256_shp0p943_actor.weights.h5 (Sharpe=0.943, MDD=12.78%)
🔄 Update 200/348 | Step 227,304/500,000 | Episode 256 | Time: 10411.3s
   📊 Metrics: Return=+63.02% | Sharpe=0.943 | DD=12.78% | Turnover=16.44%
   🎚️ Intra-Step TAPE: potential=0.7284 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1884 | critic_loss=0.0904 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0452 | risk_aux_total=0.1212 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.0207 | cvar_loss=0.1212 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.35 | std=0.58 | range=[0.51, 4.43]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.96% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4852
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00259_shp0p753_actor.weights.h5 (Sharpe=0.753, MDD=10.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00266_shp0p829_actor.weights.h5 (Sharpe=0.829, MDD=17.52%)

📚 EPISODE HORIZON UPDATE at 240,912 steps:
   Episode horizon: 1053 steps

📚 EPISODE HORIZON UPDATE at 242,424 steps:
   Episode horizon: 1127 steps
🔄 Update 210/348 | Step 242,424/500,000 | Episode 268 | Time: 11080.3s
   📊 Metrics: Return=+46.15% | Sharpe=0.696 | DD=12.13% | Turnover=16.89%
   🎚️ Intra-Step TAPE: potential=0.3656 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1879 | critic_loss=0.0148 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0074 | risk_aux_total=0.1197 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.9953 | cvar_loss=0.1197 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.97 | std=0.97 | range=[0.67, 6.25]

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
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00277_shp0p953_actor.weights.h5 (Sharpe=0.953, MDD=13.53%)
🔄 Update 220/348 | Step 257,544/500,000 | Episode 280 | Time: 11746.2s
   📊 Metrics: Return=+23.50% | Sharpe=0.179 | DD=43.88% | Turnover=14.89%
   🎚️ Intra-Step TAPE: potential=0.7509 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1648 | critic_loss=0.0159 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0080 | risk_aux_total=0.0842 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.4027 | cvar_loss=0.0842 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.47 | std=1.09 | range=[0.64, 7.71]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00282_shp0p889_actor.weights.h5 (Sharpe=0.889, MDD=14.79%)
🔄 Update 230/348 | Step 272,664/500,000 | Episode 288 | Time: 12408.1s
   📊 Metrics: Return=+72.49% | Sharpe=0.606 | DD=13.63% | Turnover=17.14%
   🎚️ Intra-Step TAPE: potential=0.7483 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1915 | critic_loss=0.0135 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0068 | risk_aux_total=0.1137 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.8956 | cvar_loss=0.1137 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.29 | std=1.13 | range=[0.54, 8.28]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00291_shp0p753_actor.weights.h5 (Sharpe=0.753, MDD=14.94%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00293_shp0p715_actor.weights.h5 (Sharpe=0.715, MDD=14.15%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00294_shp0p718_actor.weights.h5 (Sharpe=0.718, MDD=12.92%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00297_shp0p863_actor.weights.h5 (Sharpe=0.863, MDD=12.71%)
🔄 Update 240/348 | Step 287,784/500,000 | Episode 300 | Time: 13077.6s
   📊 Metrics: Return=+34.11% | Sharpe=0.248 | DD=38.20% | Turnover=14.80%
   🎚️ Intra-Step TAPE: potential=0.2474 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1545 | critic_loss=0.0146 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0073 | risk_aux_total=0.0800 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.3331 | cvar_loss=0.0800 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.79 | std=0.95 | range=[0.71, 7.67]

📚 PPO ROLLOUT UPDATE at 301,392 steps:
   Timesteps per update: 2016

📚 PPO BATCH SIZE UPDATE at 301,392 steps:
   Batch size: 504
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00309_shp0p927_actor.weights.h5 (Sharpe=0.927, MDD=11.93%)
🔄 Update 250/348 | Step 303,408/500,000 | Episode 312 | Time: 13768.8s
   📊 Metrics: Return=+34.78% | Sharpe=0.251 | DD=43.93% | Turnover=15.43%
   🎚️ Intra-Step TAPE: potential=0.3687 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1997 | critic_loss=0.0211 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0105 | risk_aux_total=0.1266 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.1106 | cvar_loss=0.1266 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.48 | std=1.08 | range=[0.52, 8.64]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.66% / trig 16.50%) | terminal=2.111 (peak 3.381) | TAPE=0.2306
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00314_shp0p834_actor.weights.h5 (Sharpe=0.834, MDD=13.85%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00316_shp0p854_actor.weights.h5 (Sharpe=0.854, MDD=13.50%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00319_shp0p769_actor.weights.h5 (Sharpe=0.769, MDD=13.88%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00322_shp0p840_actor.weights.h5 (Sharpe=0.840, MDD=12.46%)
🔄 Update 260/348 | Step 323,568/500,000 | Episode 324 | Time: 14565.9s
   📊 Metrics: Return=+86.63% | Sharpe=0.667 | DD=24.27% | Turnover=15.71%
   🎚️ Intra-Step TAPE: potential=0.2456 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2007 | critic_loss=0.0127 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0064 | risk_aux_total=0.1152 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.9205 | cvar_loss=0.1152 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.28 | std=1.25 | range=[0.36, 9.01]
🔄 Update 270/348 | Step 343,728/500,000 | Episode 336 | Time: 15382.3s
   📊 Metrics: Return=+32.16% | Sharpe=0.235 | DD=40.08% | Turnover=15.19%
   🎚️ Intra-Step TAPE: potential=0.7368 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2276 | critic_loss=0.0152 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0076 | risk_aux_total=0.1441 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.4021 | cvar_loss=0.1441 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.31 | std=2.09 | range=[0.54, 10.82]
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00338_shp0p732_actor.weights.h5 (Sharpe=0.732, MDD=15.71%)
   🔧 Actor learning rate adjusted to 0.000010 at step 350,000
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00344_shp0p741_actor.weights.h5 (Sharpe=0.741, MDD=13.19%)

🎛️ EXECUTION BETA UPDATE at 351,792 steps:
   action_execution_beta: 0.250 (w_exec=(1-β)w_prev + βw_raw)

📉 PPO GAMMA UPDATE at 351,792 steps:
   gamma: 0.9980

📉 PPO GAE-λ UPDATE at 351,792 steps:
   gae_lambda: 0.9700
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00346_shp0p713_actor.weights.h5 (Sharpe=0.713, MDD=13.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00347_shp0p740_actor.weights.h5 (Sharpe=0.740, MDD=12.94%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00348_shp0p834_actor.weights.h5 (Sharpe=0.834, MDD=12.96%)
🔄 Update 280/348 | Step 363,888/500,000 | Episode 352 | Time: 16206.7s
   📊 Metrics: Return=+37.93% | Sharpe=0.273 | DD=41.56% | Turnover=13.37%
   🎚️ Intra-Step TAPE: potential=0.2298 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1527 | critic_loss=0.0979 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0490 | risk_aux_total=0.0835 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.3917 | cvar_loss=0.0835 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.08 | std=0.39 | range=[0.51, 4.69]
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.56% / trig 16.50%) | terminal=1.576 (peak 2.317) | TAPE=0.2354
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00355_shp0p869_actor.weights.h5 (Sharpe=0.869, MDD=12.63%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00361_shp0p743_actor.weights.h5 (Sharpe=0.743, MDD=13.23%)
🔄 Update 290/348 | Step 384,048/500,000 | Episode 364 | Time: 17035.2s
   📊 Metrics: Return=+48.83% | Sharpe=0.341 | DD=45.28% | Turnover=13.92%
   🎚️ Intra-Step TAPE: potential=0.7218 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.2032 | critic_loss=0.0220 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0110 | risk_aux_total=0.1334 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=2.2235 | cvar_loss=0.1334 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.31 | std=1.03 | range=[0.50, 8.89]

📚 EPISODE HORIZON UPDATE at 390,096 steps:
   Episode horizon: 1528 steps

📚 EPISODE HORIZON UPDATE at 392,112 steps:
   Episode horizon: 2112 steps

📚 EPISODE HORIZON UPDATE at 394,128 steps:
   Episode horizon: 2697 steps

📚 EPISODE HORIZON UPDATE at 396,144 steps:
   Episode horizon: 3282 steps

📚 EPISODE HORIZON UPDATE at 398,160 steps:
   Episode horizon: 3866 steps

📚 EPISODE HORIZON UPDATE at 400,176 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 402,192 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 404,208 steps:
   Episode horizon set to full dataset
🔄 Update 300/348 | Step 404,208/500,000 | Episode 372 | Time: 17854.1s
   📊 Metrics: Return=+247.18% | Sharpe=0.479 | DD=43.90% | Turnover=13.85%
   🎚️ Intra-Step TAPE: potential=0.7203 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1823 | critic_loss=0.0167 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.1079 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.7991 | cvar_loss=0.1079 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.42 | std=1.06 | range=[0.50, 9.93]

📚 EPISODE HORIZON UPDATE at 406,224 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 408,240 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 410,256 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 412,272 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 414,288 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 416,304 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 418,320 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 420,336 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 422,352 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 424,368 steps:
   Episode horizon set to full dataset
🔄 Update 310/348 | Step 424,368/500,000 | Episode 379 | Time: 18671.1s
   📊 Metrics: Return=+150.41% | Sharpe=0.713 | DD=30.82% | Turnover=13.66%
   🎚️ Intra-Step TAPE: potential=0.2360 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1800 | critic_loss=0.0114 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0057 | risk_aux_total=0.1081 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.8020 | cvar_loss=0.1081 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.35 | std=0.60 | range=[0.51, 7.68]

📚 EPISODE HORIZON UPDATE at 426,384 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 428,400 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 430,416 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 432,432 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 434,448 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 436,464 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 438,480 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 440,496 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 442,512 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 444,528 steps:
   Episode horizon set to full dataset
🔄 Update 320/348 | Step 444,528/500,000 | Episode 386 | Time: 19487.6s
   📊 Metrics: Return=+46.54% | Sharpe=0.684 | DD=30.50% | Turnover=13.23%
   🎚️ Intra-Step TAPE: potential=0.2554 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1476 | critic_loss=0.0563 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0281 | risk_aux_total=0.0791 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.3175 | cvar_loss=0.0791 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.38 | std=0.24 | range=[0.79, 2.96]
   ⚠️  WARNING: Alpha std < 0.25 after 320 updates. TCN may not be learning asset discrimination.

📚 EPISODE HORIZON UPDATE at 446,544 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 448,560 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 450,576 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 452,592 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 454,608 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 456,624 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 458,640 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 460,656 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 462,672 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 464,688 steps:
   Episode horizon set to full dataset
🔄 Update 330/348 | Step 464,688/500,000 | Episode 395 | Time: 20305.8s
   📊 Metrics: Return=+367.89% | Sharpe=0.571 | DD=43.06% | Turnover=13.42%
   🎚️ Intra-Step TAPE: potential=0.2464 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1861 | critic_loss=0.0142 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0071 | risk_aux_total=0.1171 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.9524 | cvar_loss=0.1171 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.45 | std=0.43 | range=[0.48, 6.24]

📚 EPISODE HORIZON UPDATE at 466,704 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 468,720 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 470,736 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 472,752 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 474,768 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 476,784 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 478,800 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 480,816 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 482,832 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 484,848 steps:
   Episode horizon set to full dataset
🔄 Update 340/348 | Step 484,848/500,000 | Episode 407 | Time: 21117.8s
   📊 Metrics: Return=+84.39% | Sharpe=0.816 | DD=30.88% | Turnover=13.61%
   🎚️ Intra-Step TAPE: potential=0.2311 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1722 | critic_loss=0.0359 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0180 | risk_aux_total=0.1022 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.7031 | cvar_loss=0.1022 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.35 | std=0.31 | range=[0.53, 3.30]

📚 EPISODE HORIZON UPDATE at 486,864 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 488,880 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 490,896 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 492,912 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 494,928 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 496,944 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 498,960 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 500,000 steps:
   Episode horizon set to full dataset
🔄 Update 348/348 | Step 500,000/500,000 | Episode 416 | Time: 21734.1s
   📊 Metrics: Return=+158.23% | Sharpe=0.755 | DD=30.66% | Turnover=13.01%
   🎚️ Intra-Step TAPE: potential=0.2090 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   🧠 Training: actor_loss=0.1570 | critic_loss=0.0628 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0314 | risk_aux_total=0.1071 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=1.7854 | cvar_loss=0.1071 | cvar_coef=0.0600
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.62 | std=0.41 | range=[0.71, 3.94]
   🔒 Drawdown λ snapshot=0.034 (peak 0.034, dd 23.77% / trig 16.50%) | terminal=0.000 (peak 0.097) | TAPE=0.3360

✅ THREE-COMPONENT TAPE v3 training completed!
   Total episodes: 416
   Total timesteps: 500,000
   Training time: 21734.05s (362.23min)
📊 Training summary saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260302_143707_summary.csv
💾 Final models saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00416_shp0p755_actor.weights.h5, /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00416_shp0p755_critic.weights.h5
🎯 Default selected checkpoint: final high-watermark-style checkpoint
✅ Training complete
checkpoint_prefix: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00416_shp0p755