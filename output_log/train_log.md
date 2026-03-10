[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
[OK] Actuarial feature check passed: {'Actuarial_Prob_30d': 54767, 'Actuarial_Reserve_Severity': 54767, 'Actuarial_Expected_Recovery': 54767, 'Actuarial_Prob_60d': 54767}
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
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_172715_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_172715_step_diagnostics.csv

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
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_172715_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_172715_metadata.json
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00003_shp0p783_actor.weights.h5 (Sharpe=0.783, MDD=10.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=14.54%)
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 997.6s
   📊 Metrics: Return=+26.40% | Sharpe=0.525 | DD=15.18% | Turnover=33.76%
   🎚️ Intra-Step TAPE: potential=0.7369 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0808 | critic_loss=0.6926 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3463 | risk_aux_total=0.0696 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.7241 | cvar_loss=0.0690 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.62 | std=3.31 | range=[0.36, 15.37]
   🏷️ Alpha Per-Asset  TOP: PG=6.14 | JNJ=6.06 | NEE=4.48  BOT: JPM=2.28 | UNH=1.90 | CAT=1.69
   🧭 Regime Start Dist (train resets): high_vol=6 (37.5%), low_vol=6 (37.5%), medium_vol=4 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00014_shp1p079_actor.weights.h5 (Sharpe=1.079, MDD=6.95%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00017_shp1p241_actor.weights.h5 (Sharpe=1.241, MDD=8.46%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00018_shp0p937_actor.weights.h5 (Sharpe=0.937, MDD=8.35%)
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1974.4s
   📊 Metrics: Return=+11.58% | Sharpe=0.205 | DD=11.43% | Turnover=43.11%
   🎚️ Intra-Step TAPE: potential=0.6258 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0772 | critic_loss=0.1634 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0817 | risk_aux_total=0.0636 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=1.5775 | cvar_loss=0.0631 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.99 | std=2.12 | range=[0.27, 13.59]
   🏷️ Alpha Per-Asset  TOP: JNJ=4.45 | PG=4.34 | NEE=4.32  BOT: UNH=0.75 | JPM=0.45 | CAT=0.39
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=11 (39.3%), medium_vol=7 (25.0%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 2950.7s
   📊 Metrics: Return=-9.40% | Sharpe=-0.191 | DD=27.65% | Turnover=31.63%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1137 | critic_loss=0.1955 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0977 | risk_aux_total=0.1045 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=2.5917 | cvar_loss=0.1037 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.38 | std=4.20 | range=[0.24, 22.73]
   🏷️ Alpha Per-Asset  TOP: JNJ=9.15 | PG=6.73 | NEE=3.89  BOT: MSFT=0.42 | CAT=0.34 | JPM=0.30
   🧭 Regime Start Dist (train resets): high_vol=19 (43.2%), low_vol=14 (31.8%), medium_vol=11 (25.0%)
   🔒 Drawdown λ snapshot=0.440 (peak 0.440, dd 0.00% / trig 21.00%) | terminal=0.999 (peak 2.044) | TAPE=0.2273
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00042_shp0p923_actor.weights.h5 (Sharpe=0.923, MDD=11.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00043_shp0p810_actor.weights.h5 (Sharpe=0.810, MDD=11.30%)
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 3928.9s
   📊 Metrics: Return=-20.89% | Sharpe=-0.348 | DD=42.39% | Turnover=34.18%
   🎚️ Intra-Step TAPE: potential=0.2268 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0918 | critic_loss=0.0978 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0489 | risk_aux_total=0.0838 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=2.0767 | cvar_loss=0.0831 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.08 | std=3.89 | range=[0.26, 24.95]
   🏷️ Alpha Per-Asset  TOP: JNJ=6.28 | PG=5.22 | NEE=3.23  BOT: UNH=0.55 | JPM=0.49 | MSFT=0.47
   🧭 Regime Start Dist (train resets): high_vol=24 (42.9%), low_vol=18 (32.1%), medium_vol=14 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00062_shp0p730_actor.weights.h5 (Sharpe=0.730, MDD=11.37%)
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 4905.3s
   📊 Metrics: Return=-16.62% | Sharpe=-0.302 | DD=36.84% | Turnover=26.74%
   🎚️ Intra-Step TAPE: potential=0.2129 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0993 | critic_loss=0.1413 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0706 | risk_aux_total=0.0889 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=2.2023 | cvar_loss=0.0881 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.26 | std=2.21 | range=[0.25, 17.16]
   🏷️ Alpha Per-Asset  TOP: JNJ=4.65 | PG=2.87 | NEE=2.14  BOT: GOOGL=0.38 | LIN=0.37 | CAT=0.30
   🧭 Regime Start Dist (train resets): high_vol=27 (39.7%), low_vol=24 (35.3%), medium_vol=17 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00069_shp0p938_actor.weights.h5 (Sharpe=0.938, MDD=12.62%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00078_shp0p748_actor.weights.h5 (Sharpe=0.748, MDD=8.62%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00080_shp0p709_actor.weights.h5 (Sharpe=0.709, MDD=11.13%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 5883.5s
   📊 Metrics: Return=+30.72% | Sharpe=0.709 | DD=11.13% | Turnover=31.29%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0806 | critic_loss=0.0419 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0210 | risk_aux_total=0.0698 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.7317 | cvar_loss=0.0693 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.67 | std=2.69 | range=[0.26, 16.45]
   🏷️ Alpha Per-Asset  TOP: NEE=4.74 | PG=4.07 | JNJ=3.21  BOT: MSFT=0.55 | UNH=0.52 | CAT=0.40
   🧭 Regime Start Dist (train resets): high_vol=34 (40.5%), low_vol=29 (34.5%), medium_vol=21 (25.0%)
   🔒 Drawdown λ snapshot=3.533 (peak 3.533, dd 0.00% / trig 21.00%) | terminal=0.432 (peak 1.807) | TAPE=0.3537
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00081_shp0p814_actor.weights.h5 (Sharpe=0.814, MDD=13.03%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp1p005_actor.weights.h5 (Sharpe=1.005, MDD=9.02%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00090_shp0p815_actor.weights.h5 (Sharpe=0.815, MDD=12.30%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00091_shp0p724_actor.weights.h5 (Sharpe=0.724, MDD=11.02%)
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 6863.8s
   📊 Metrics: Return=+15.09% | Sharpe=0.303 | DD=13.27% | Turnover=28.55%
   🎚️ Intra-Step TAPE: potential=0.2289 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0707 | critic_loss=0.2066 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1033 | risk_aux_total=0.0546 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.3493 | cvar_loss=0.0540 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.09 | std=2.32 | range=[0.23, 19.99]
   🏷️ Alpha Per-Asset  TOP: JNJ=3.37 | NEE=2.58 | PG=1.96  BOT: UNH=0.31 | CAT=0.26 | JPM=0.25
   🧭 Regime Start Dist (train resets): high_vol=38 (39.6%), low_vol=35 (36.5%), medium_vol=23 (24.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00101_shp0p954_actor.weights.h5 (Sharpe=0.954, MDD=9.88%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00103_shp0p727_actor.weights.h5 (Sharpe=0.727, MDD=10.63%)
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 7843.2s
   📊 Metrics: Return=-2.17% | Sharpe=-0.167 | DD=24.09% | Turnover=29.91%
   🎚️ Intra-Step TAPE: potential=0.2182 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0679 | critic_loss=0.1025 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0512 | risk_aux_total=0.0581 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.4336 | cvar_loss=0.0573 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.36 | std=5.67 | range=[0.23, 27.92]
   🏷️ Alpha Per-Asset  TOP: JNJ=11.69 | NEE=9.83 | PG=6.52  BOT: CAT=0.41 | MSFT=0.36 | JPM=0.29
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=40 (37.0%), medium_vol=26 (24.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00105_shp0p923_actor.weights.h5 (Sharpe=0.923, MDD=7.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00107_shp0p969_actor.weights.h5 (Sharpe=0.969, MDD=13.20%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00109_shp0p884_actor.weights.h5 (Sharpe=0.884, MDD=7.51%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00111_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=11.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00117_shp0p741_actor.weights.h5 (Sharpe=0.741, MDD=8.19%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 8823.4s
   📊 Metrics: Return=+8.83% | Sharpe=0.131 | DD=26.28% | Turnover=28.06%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0632 | critic_loss=0.1395 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0697 | risk_aux_total=0.0498 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.2272 | cvar_loss=0.0491 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.66 | std=4.46 | range=[0.24, 24.28]
   🏷️ Alpha Per-Asset  TOP: JNJ=9.05 | PG=7.11 | NEE=5.32  BOT: GOOGL=0.50 | MSFT=0.47 | CAT=0.32
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=46 (37.1%), medium_vol=30 (24.2%)
   🔒 Drawdown λ snapshot=1.838 (peak 1.838, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.176) | TAPE=0.2310

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
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00125_shp0p754_actor.weights.h5 (Sharpe=0.754, MDD=12.59%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00126_shp0p939_actor.weights.h5 (Sharpe=0.939, MDD=12.25%)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.5

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 9804.1s
   📊 Metrics: Return=+37.99% | Sharpe=0.628 | DD=12.30% | Turnover=19.57%
   🎚️ Intra-Step TAPE: potential=0.6094 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0936 | critic_loss=0.1822 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0911 | risk_aux_total=0.0855 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=2.1148 | cvar_loss=0.0846 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.79 | std=4.83 | range=[0.29, 28.02]
   🏷️ Alpha Per-Asset  TOP: PG=6.91 | NEE=6.77 | JNJ=6.54  BOT: JPM=0.55 | UNH=0.53 | MSFT=0.47
   🧭 Regime Start Dist (train resets): high_vol=52 (39.4%), low_vol=47 (35.6%), medium_vol=33 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00130_shp0p833_actor.weights.h5 (Sharpe=0.833, MDD=11.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00131_shp0p927_actor.weights.h5 (Sharpe=0.927, MDD=11.66%)
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 10785.2s
   📊 Metrics: Return=-6.96% | Sharpe=-0.101 | DD=35.57% | Turnover=22.86%
   🎚️ Intra-Step TAPE: potential=0.2222 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1028 | critic_loss=0.1242 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0621 | risk_aux_total=0.0894 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=2.2185 | cvar_loss=0.0887 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=4.14 | std=5.11 | range=[0.53, 26.69]
   🏷️ Alpha Per-Asset  TOP: PG=11.50 | JNJ=10.74 | NEE=8.25  BOT: JPM=1.13 | CAT=1.06 | UNH=1.05
   🧭 Regime Start Dist (train resets): high_vol=57 (39.6%), low_vol=51 (35.4%), medium_vol=36 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 12.18% / trig 21.00%) | terminal=0.564 (peak 1.137) | TAPE=0.2229
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 148 | Time: 11767.0s
   📊 Metrics: Return=+40.49% | Sharpe=0.611 | DD=12.87% | Turnover=25.42%
   🎚️ Intra-Step TAPE: potential=0.3166 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0980 | critic_loss=0.0788 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0394 | risk_aux_total=0.0845 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=2.0941 | cvar_loss=0.0838 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.48 | std=5.23 | range=[0.28, 29.13]
   🏷️ Alpha Per-Asset  TOP: JNJ=11.51 | PG=5.71 | NEE=2.97  BOT: MSFT=0.38 | JPM=0.38 | UNH=0.37
   🧭 Regime Start Dist (train resets): high_vol=58 (38.2%), low_vol=53 (34.9%), medium_vol=41 (27.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00156_shp0p940_actor.weights.h5 (Sharpe=0.940, MDD=10.72%)
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 160 | Time: 12748.0s
   📊 Metrics: Return=+41.16% | Sharpe=0.639 | DD=12.66% | Turnover=25.74%
   🎚️ Intra-Step TAPE: potential=0.7484 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1056 | critic_loss=0.1839 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0919 | risk_aux_total=0.0895 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=2.2142 | cvar_loss=0.0886 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.06 | std=6.25 | range=[0.26, 29.87]
   🏷️ Alpha Per-Asset  TOP: JNJ=11.76 | PG=9.55 | NEE=5.25  BOT: UNH=0.32 | JPM=0.31 | CAT=0.30
   🧭 Regime Start Dist (train resets): high_vol=64 (39.0%), low_vol=58 (35.4%), medium_vol=42 (25.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.60% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3568
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00161_shp1p019_actor.weights.h5 (Sharpe=1.019, MDD=12.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00166_shp1p022_actor.weights.h5 (Sharpe=1.022, MDD=11.79%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00167_shp1p117_actor.weights.h5 (Sharpe=1.117, MDD=7.52%)
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 168 | Time: 13729.9s
   📊 Metrics: Return=+25.56% | Sharpe=0.392 | DD=20.05% | Turnover=17.47%
   🎚️ Intra-Step TAPE: potential=0.2824 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0626 | critic_loss=0.0370 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0185 | risk_aux_total=0.0522 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.2840 | cvar_loss=0.0514 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=4.53 | std=6.90 | range=[0.42, 28.18]
   🏷️ Alpha Per-Asset  TOP: PG=15.21 | JNJ=14.61 | NEE=7.73  BOT: UNH=0.61 | JPM=0.55 | CAT=0.53
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
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00179_shp0p870_actor.weights.h5 (Sharpe=0.870, MDD=11.30%)
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 180 | Time: 14775.7s
   📊 Metrics: Return=+40.23% | Sharpe=0.588 | DD=12.23% | Turnover=25.60%
   🎚️ Intra-Step TAPE: potential=0.2289 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0570 | critic_loss=0.1823 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0912 | risk_aux_total=0.0519 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=1.2705 | cvar_loss=0.0508 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=5.72 | std=9.69 | range=[0.31, 30.84]
   🏷️ Alpha Per-Asset  TOP: JNJ=19.05 | PG=15.37 | NEE=10.37  BOT: LIN=0.90 | XOM=0.75 | CAT=0.38
   🧭 Regime Start Dist (train resets): high_vol=69 (37.5%), low_vol=68 (37.0%), medium_vol=47 (25.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.161, dd 3.86% / trig 21.00%) | terminal=0.000 (peak 0.593) | TAPE=0.3924
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00182_shp0p893_actor.weights.h5 (Sharpe=0.893, MDD=11.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00187_shp0p713_actor.weights.h5 (Sharpe=0.713, MDD=21.26%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00189_shp0p958_actor.weights.h5 (Sharpe=0.958, MDD=11.64%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00193_shp0p894_actor.weights.h5 (Sharpe=0.894, MDD=11.83%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00194_shp0p913_actor.weights.h5 (Sharpe=0.913, MDD=11.84%)
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 196 | Time: 16196.1s
   📊 Metrics: Return=+41.48% | Sharpe=0.657 | DD=22.96% | Turnover=22.04%
   🎚️ Intra-Step TAPE: potential=0.6382 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0524 | critic_loss=0.1334 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0667 | risk_aux_total=0.0485 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.1907 | cvar_loss=0.0476 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.33 | std=6.67 | range=[0.37, 29.10]
   🏷️ Alpha Per-Asset  TOP: PG=10.66 | JNJ=9.89 | NEE=4.11  BOT: LIN=0.85 | CAT=0.60 | UNH=0.47
   🧭 Regime Start Dist (train resets): high_vol=71 (35.5%), low_vol=76 (38.0%), medium_vol=53 (26.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.65% / trig 21.00%) | terminal=0.000 (peak 0.014) | TAPE=0.3547
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00200_shp0p849_actor.weights.h5 (Sharpe=0.849, MDD=11.21%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00202_shp0p937_actor.weights.h5 (Sharpe=0.937, MDD=15.97%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00203_shp0p984_actor.weights.h5 (Sharpe=0.984, MDD=16.85%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00206_shp0p934_actor.weights.h5 (Sharpe=0.934, MDD=11.82%)
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 208 | Time: 17613.9s
   📊 Metrics: Return=+36.31% | Sharpe=0.551 | DD=24.46% | Turnover=22.17%
   🎚️ Intra-Step TAPE: potential=0.2360 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1021 | critic_loss=0.0862 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0431 | risk_aux_total=0.0875 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=2.1637 | cvar_loss=0.0865 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.74 | std=9.19 | range=[0.35, 31.88]
   🏷️ Alpha Per-Asset  TOP: JNJ=20.64 | PG=18.37 | NEE=3.27  BOT: CAT=0.47 | JPM=0.47 | MSFT=0.46
   🧭 Regime Start Dist (train resets): high_vol=75 (35.4%), low_vol=79 (37.3%), medium_vol=58 (27.4%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00209_shp0p758_actor.weights.h5 (Sharpe=0.758, MDD=23.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00216_shp1p074_actor.weights.h5 (Sharpe=1.074, MDD=11.66%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00217_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=11.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00218_shp0p827_actor.weights.h5 (Sharpe=0.827, MDD=11.97%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00219_shp0p866_actor.weights.h5 (Sharpe=0.866, MDD=11.45%)
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 224 | Time: 19032.4s
   📊 Metrics: Return=+24.50% | Sharpe=0.363 | DD=26.02% | Turnover=25.93%
   🎚️ Intra-Step TAPE: potential=0.2171 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0841 | critic_loss=0.0877 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0439 | risk_aux_total=0.0752 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0012 | cvar_proxy=1.8503 | cvar_loss=0.0740 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.03 | std=7.48 | range=[0.30, 31.69]
   🏷️ Alpha Per-Asset  TOP: PG=16.22 | JNJ=7.31 | NEE=2.81  BOT: MSFT=0.38 | CAT=0.37 | JPM=0.37
   🧭 Regime Start Dist (train resets): high_vol=79 (34.6%), low_vol=86 (37.7%), medium_vol=63 (27.6%)

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.75
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 240 | Time: 20448.6s
   📊 Metrics: Return=+1.55% | Sharpe=0.011 | DD=36.78% | Turnover=19.20%
   🎚️ Intra-Step TAPE: potential=0.6304 | delta_reward=+0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0791 | critic_loss=0.1048 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0524 | risk_aux_total=0.0714 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=1.7617 | cvar_loss=0.0705 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=5.09 | std=9.23 | range=[0.44, 32.22]
   🏷️ Alpha Per-Asset  TOP: JNJ=21.10 | PG=14.36 | NEE=6.12  BOT: UNH=0.83 | LIN=0.72 | CAT=0.70
   🧭 Regime Start Dist (train resets): high_vol=85 (34.8%), low_vol=89 (36.5%), medium_vol=70 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.18% / trig 21.00%) | terminal=0.145 (peak 0.550) | TAPE=0.2298
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00241_shp0p923_actor.weights.h5 (Sharpe=0.923, MDD=11.59%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00243_shp0p974_actor.weights.h5 (Sharpe=0.974, MDD=11.61%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00247_shp1p061_actor.weights.h5 (Sharpe=1.061, MDD=7.92%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00248_shp1p207_actor.weights.h5 (Sharpe=1.207, MDD=7.84%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00249_shp0p958_actor.weights.h5 (Sharpe=0.958, MDD=11.02%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00250_shp1p085_actor.weights.h5 (Sharpe=1.085, MDD=9.61%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00253_shp1p003_actor.weights.h5 (Sharpe=1.003, MDD=10.66%)
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 256 | Time: 21866.5s
   📊 Metrics: Return=+31.89% | Sharpe=0.474 | DD=22.03% | Turnover=24.44%
   🎚️ Intra-Step TAPE: potential=0.7597 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0781 | critic_loss=0.1701 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0851 | risk_aux_total=0.0726 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=1.7866 | cvar_loss=0.0715 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.50 | std=8.91 | range=[0.35, 32.32]
   🏷️ Alpha Per-Asset  TOP: JNJ=20.85 | PG=11.37 | NEE=8.01  BOT: CAT=0.57 | LIN=0.55 | JPM=0.54
   🧭 Regime Start Dist (train resets): high_vol=89 (34.2%), low_vol=96 (36.9%), medium_vol=75 (28.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.35% / trig 21.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2922
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00257_shp1p026_actor.weights.h5 (Sharpe=1.026, MDD=10.69%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00259_shp0p755_actor.weights.h5 (Sharpe=0.755, MDD=10.74%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00265_shp0p988_actor.weights.h5 (Sharpe=0.988, MDD=11.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00268_shp1p040_actor.weights.h5 (Sharpe=1.040, MDD=10.99%)

📚 EPISODE HORIZON UPDATE at 240,912 steps:
   Episode horizon: 1053 steps

📚 EPISODE HORIZON UPDATE at 242,424 steps:
   Episode horizon: 1127 steps
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 268 | Time: 23284.3s
   📊 Metrics: Return=+80.17% | Sharpe=1.040 | DD=10.99% | Turnover=15.01%
   🎚️ Intra-Step TAPE: potential=0.2144 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0621 | critic_loss=0.0309 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0154 | risk_aux_total=0.0527 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0013 | cvar_proxy=1.2853 | cvar_loss=0.0514 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.11 | std=8.72 | range=[0.38, 32.35]
   🏷️ Alpha Per-Asset  TOP: JNJ=18.05 | PG=15.16 | NEE=3.42  BOT: MSFT=0.61 | XOM=0.60 | CAT=0.58
   🧭 Regime Start Dist (train resets): high_vol=93 (34.2%), low_vol=101 (37.1%), medium_vol=78 (28.7%)

📚 EPISODE HORIZON UPDATE at 243,936 steps:
   Episode horizon: 1202 steps

📚 EPISODE HORIZON UPDATE at 245,448 steps:
   Episode horizon: 1276 steps

📚 EPISODE HORIZON UPDATE at 246,960 steps:
   Episode horizon: 1350 steps

📚 EPISODE HORIZON UPDATE at 248,472 steps:
   Episode horizon: 1425 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00273_shp0p750_actor.weights.h5 (Sharpe=0.750, MDD=17.77%)

📚 EPISODE HORIZON UPDATE at 249,984 steps:
   Episode horizon: 1499 steps

📚 EPISODE HORIZON UPDATE at 251,496 steps:
   Episode horizon: 1500 steps
[CYCLE] Update 220/348 | Step 257,544/500,000 | Episode 280 | Time: 24702.4s
   📊 Metrics: Return=+30.31% | Sharpe=0.230 | DD=35.97% | Turnover=18.93%
   🎚️ Intra-Step TAPE: potential=0.2455 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0987 | critic_loss=0.0566 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0283 | risk_aux_total=0.0918 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=2.2667 | cvar_loss=0.0907 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.37 | std=7.71 | range=[0.27, 32.38]
   🏷️ Alpha Per-Asset  TOP: JNJ=19.70 | PG=7.85 | NEE=2.74  BOT: LIN=0.36 | CAT=0.35 | UNH=0.33
   🧭 Regime Start Dist (train resets): high_vol=96 (33.8%), low_vol=104 (36.6%), medium_vol=84 (29.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00286_shp0p794_actor.weights.h5 (Sharpe=0.794, MDD=19.49%)
[CYCLE] Update 230/348 | Step 272,664/500,000 | Episode 289 | Time: 26119.7s
   📊 Metrics: Return=+56.64% | Sharpe=0.525 | DD=24.79% | Turnover=23.22%
   🎚️ Intra-Step TAPE: potential=0.2374 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0800 | critic_loss=0.0619 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0310 | risk_aux_total=0.0777 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=1.9153 | cvar_loss=0.0766 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.52 | std=8.32 | range=[0.31, 32.59]
   🏷️ Alpha Per-Asset  TOP: PG=11.96 | NEE=10.96 | JNJ=7.28  BOT: MSFT=0.43 | UNH=0.43 | JPM=0.42
   🧭 Regime Start Dist (train resets): high_vol=98 (33.4%), low_vol=108 (36.9%), medium_vol=87 (29.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.63% / trig 21.00%) | terminal=0.000 (peak 0.056) | TAPE=0.3024
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00295_shp0p831_actor.weights.h5 (Sharpe=0.831, MDD=24.93%)
[CYCLE] Update 240/348 | Step 287,784/500,000 | Episode 300 | Time: 27537.0s
   📊 Metrics: Return=+25.95% | Sharpe=0.196 | DD=35.55% | Turnover=14.10%
   🎚️ Intra-Step TAPE: potential=0.3212 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0954 | critic_loss=0.0436 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0218 | risk_aux_total=0.0913 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0013 | cvar_proxy=2.2502 | cvar_loss=0.0900 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.86 | std=8.78 | range=[0.26, 32.80]
   🏷️ Alpha Per-Asset  TOP: JNJ=22.16 | PG=11.46 | NEE=2.27  BOT: GOOGL=0.37 | MSFT=0.36 | LIN=0.36
   🧭 Regime Start Dist (train resets): high_vol=105 (34.5%), low_vol=109 (35.9%), medium_vol=90 (29.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00305_shp0p842_actor.weights.h5 (Sharpe=0.842, MDD=13.29%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00306_shp0p986_actor.weights.h5 (Sharpe=0.986, MDD=21.37%)

📚 TURNOVER CURRICULUM UPDATE at 301,392 steps:
   Turnover penalty scalar: 0.9

📚 PPO ROLLOUT UPDATE at 301,392 steps:
   Timesteps per update: 2016

📚 PPO BATCH SIZE UPDATE at 301,392 steps:
   Batch size: 504
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00310_shp0p704_actor.weights.h5 (Sharpe=0.704, MDD=21.56%)
[CYCLE] Update 250/348 | Step 303,408/500,000 | Episode 312 | Time: 29002.5s
   📊 Metrics: Return=+46.80% | Sharpe=0.353 | DD=35.74% | Turnover=21.59%
   🎚️ Intra-Step TAPE: potential=0.6103 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0540 | critic_loss=0.0946 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0473 | risk_aux_total=0.0501 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.2324 | cvar_loss=0.0493 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.11 | std=7.68 | range=[0.80, 32.54]
   🏷️ Alpha Per-Asset  TOP: PG=12.23 | NEE=9.52 | JNJ=5.96  BOT: CAT=1.37 | JPM=1.30 | UNH=1.28
   🧭 Regime Start Dist (train resets): high_vol=108 (34.2%), low_vol=112 (35.4%), medium_vol=96 (30.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.42% / trig 21.00%) | terminal=0.000 (peak 0.455) | TAPE=0.2609
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00319_shp0p762_actor.weights.h5 (Sharpe=0.762, MDD=22.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00321_shp0p948_actor.weights.h5 (Sharpe=0.948, MDD=22.67%)
[CYCLE] Update 260/348 | Step 323,568/500,000 | Episode 324 | Time: 30732.3s
   📊 Metrics: Return=+71.03% | Sharpe=0.639 | DD=23.48% | Turnover=21.65%
   🎚️ Intra-Step TAPE: potential=0.6448 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0725 | critic_loss=0.0267 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0133 | risk_aux_total=0.0688 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0012 | cvar_proxy=1.6894 | cvar_loss=0.0676 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.78 | std=9.59 | range=[0.38, 32.85]
   🏷️ Alpha Per-Asset  TOP: PG=16.22 | JNJ=16.01 | NEE=7.25  BOT: LIN=0.74 | UNH=0.73 | CAT=0.69
   🧭 Regime Start Dist (train resets): high_vol=112 (34.1%), low_vol=117 (35.7%), medium_vol=99 (30.2%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00327_shp0p728_actor.weights.h5 (Sharpe=0.728, MDD=23.07%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00331_shp0p712_actor.weights.h5 (Sharpe=0.712, MDD=24.50%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00335_shp0p859_actor.weights.h5 (Sharpe=0.859, MDD=22.65%)
[CYCLE] Update 270/348 | Step 343,728/500,000 | Episode 336 | Time: 32461.5s
   📊 Metrics: Return=+54.20% | Sharpe=0.393 | DD=36.88% | Turnover=19.78%
   🎚️ Intra-Step TAPE: potential=0.2244 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0825 | critic_loss=0.0332 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0166 | risk_aux_total=0.0832 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0012 | cvar_proxy=2.0482 | cvar_loss=0.0819 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.63 | std=9.46 | range=[0.37, 32.88]
   🏷️ Alpha Per-Asset  TOP: JNJ=18.14 | PG=12.35 | NEE=7.36  BOT: CAT=0.81 | JPM=0.79 | UNH=0.74
   🧭 Regime Start Dist (train resets): high_vol=117 (34.4%), low_vol=121 (35.6%), medium_vol=102 (30.0%)
   [TOOL] Actor learning rate adjusted to 0.000010 at step 350,000
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00341_shp0p876_actor.weights.h5 (Sharpe=0.876, MDD=24.23%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00342_shp0p726_actor.weights.h5 (Sharpe=0.726, MDD=23.14%)

[DOWN] PPO GAMMA UPDATE at 351,792 steps:
   gamma: 0.9980

[DOWN] PPO GAE-λ UPDATE at 351,792 steps:
   gae_lambda: 0.9700
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00351_shp0p815_actor.weights.h5 (Sharpe=0.815, MDD=22.52%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00352_shp0p874_actor.weights.h5 (Sharpe=0.874, MDD=12.97%)
[CYCLE] Update 280/348 | Step 363,888/500,000 | Episode 352 | Time: 34192.0s
   📊 Metrics: Return=+98.62% | Sharpe=0.874 | DD=12.97% | Turnover=17.70%
   🎚️ Intra-Step TAPE: potential=0.4105 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0535 | critic_loss=0.0879 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0440 | risk_aux_total=0.0503 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=1.2331 | cvar_loss=0.0493 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=4.77 | std=9.42 | range=[0.42, 32.88]
   🏷️ Alpha Per-Asset  TOP: NEE=15.34 | PG=11.74 | JNJ=8.21  BOT: JPM=1.14 | CAT=1.12 | UNH=1.08
   🧭 Regime Start Dist (train resets): high_vol=124 (34.8%), low_vol=125 (35.1%), medium_vol=107 (30.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.58% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4690
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00354_shp0p753_actor.weights.h5 (Sharpe=0.753, MDD=12.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00364_shp0p760_actor.weights.h5 (Sharpe=0.760, MDD=12.97%)
[CYCLE] Update 290/348 | Step 384,048/500,000 | Episode 364 | Time: 35919.5s
   📊 Metrics: Return=+83.20% | Sharpe=0.760 | DD=12.97% | Turnover=20.53%
   🎚️ Intra-Step TAPE: potential=0.2278 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0849 | critic_loss=0.0701 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0350 | risk_aux_total=0.0802 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0012 | cvar_proxy=1.9760 | cvar_loss=0.0790 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=5.05 | std=10.07 | range=[0.39, 32.85]
   🏷️ Alpha Per-Asset  TOP: JNJ=29.79 | PG=10.16 | NEE=3.55  BOT: UNH=0.85 | CAT=0.85 | LIN=0.85
   🧭 Regime Start Dist (train resets): high_vol=127 (34.5%), low_vol=128 (34.8%), medium_vol=113 (30.7%)

📚 EPISODE HORIZON UPDATE at 390,096 steps:
   Episode horizon: 1525 steps

📚 EPISODE HORIZON UPDATE at 392,112 steps:
   Episode horizon: 2044 steps

📚 EPISODE HORIZON UPDATE at 394,128 steps:
   Episode horizon: 2564 steps

📚 EPISODE HORIZON UPDATE at 396,144 steps:
   Episode horizon: 3084 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00369_shp0p850_actor.weights.h5 (Sharpe=0.850, MDD=23.34%)

📚 EPISODE HORIZON UPDATE at 398,160 steps:
   Episode horizon: 3604 steps

📚 TURNOVER CURRICULUM UPDATE at 400,176 steps:
   Turnover penalty scalar: 1.0

📚 EPISODE HORIZON UPDATE at 400,176 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 402,192 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00373_shp1p488_actor.weights.h5 (Sharpe=1.488, MDD=9.08%)

📚 EPISODE HORIZON UPDATE at 404,208 steps:
   Episode horizon set to full dataset
[CYCLE] Update 300/348 | Step 404,208/500,000 | Episode 373 | Time: 37649.7s
   📊 Metrics: Return=+31.21% | Sharpe=1.488 | DD=9.08% | Turnover=15.29%
   🎚️ Intra-Step TAPE: potential=0.6615 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0797 | critic_loss=0.0472 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0236 | risk_aux_total=0.0772 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0012 | cvar_proxy=1.9007 | cvar_loss=0.0760 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=4.47 | std=9.65 | range=[0.34, 32.91]
   🏷️ Alpha Per-Asset  TOP: JNJ=14.52 | NEE=14.25 | PG=6.71  BOT: MSFT=0.86 | CAT=0.83 | JPM=0.78
   🧭 Regime Start Dist (train resets): high_vol=129 (34.2%), low_vol=130 (34.5%), medium_vol=118 (31.3%)
   🔒 Drawdown λ snapshot=0.619 (peak 0.629, dd 18.03% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5903

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
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00377_shp0p914_actor.weights.h5 (Sharpe=0.914, MDD=24.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00378_shp1p863_actor.weights.h5 (Sharpe=1.863, MDD=8.64%)

📚 EPISODE HORIZON UPDATE at 418,320 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 420,336 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00380_shp0p732_actor.weights.h5 (Sharpe=0.732, MDD=24.40%)

📚 EPISODE HORIZON UPDATE at 422,352 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00381_shp1p160_actor.weights.h5 (Sharpe=1.160, MDD=11.96%)

📚 EPISODE HORIZON UPDATE at 424,368 steps:
   Episode horizon set to full dataset
[CYCLE] Update 310/348 | Step 424,368/500,000 | Episode 381 | Time: 39382.7s
   📊 Metrics: Return=+57.72% | Sharpe=1.160 | DD=11.96% | Turnover=14.58%
   🎚️ Intra-Step TAPE: potential=0.2279 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0484 | critic_loss=0.0370 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0185 | risk_aux_total=0.0461 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=1.1283 | cvar_loss=0.0451 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=5.32 | std=10.45 | range=[0.43, 32.92]
   🏷️ Alpha Per-Asset  TOP: NEE=17.28 | JNJ=16.34 | PG=11.48  BOT: CAT=0.91 | UNH=0.85 | GOOGL=0.85
   🧭 Regime Start Dist (train resets): high_vol=132 (34.3%), low_vol=130 (33.8%), medium_vol=123 (31.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.820, dd 10.19% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5303

📚 EPISODE HORIZON UPDATE at 426,384 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 428,400 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00383_shp0p951_actor.weights.h5 (Sharpe=0.951, MDD=24.44%)

📚 EPISODE HORIZON UPDATE at 430,416 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 432,432 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00385_shp0p967_actor.weights.h5 (Sharpe=0.967, MDD=21.07%)

📚 EPISODE HORIZON UPDATE at 434,448 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00386_shp0p888_actor.weights.h5 (Sharpe=0.888, MDD=19.04%)

📚 EPISODE HORIZON UPDATE at 436,464 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 438,480 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 440,496 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00388_shp0p796_actor.weights.h5 (Sharpe=0.796, MDD=22.20%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00389_shp1p899_actor.weights.h5 (Sharpe=1.899, MDD=9.38%)

📚 EPISODE HORIZON UPDATE at 442,512 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 444,528 steps:
   Episode horizon set to full dataset
[CYCLE] Update 320/348 | Step 444,528/500,000 | Episode 389 | Time: 41116.9s
   📊 Metrics: Return=+33.90% | Sharpe=1.899 | DD=9.38% | Turnover=14.49%
   🎚️ Intra-Step TAPE: potential=0.6952 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0512 | critic_loss=0.0175 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0087 | risk_aux_total=0.0473 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=1.1552 | cvar_loss=0.0462 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=5.03 | std=10.04 | range=[0.46, 32.89]
   🏷️ Alpha Per-Asset  TOP: NEE=16.68 | PG=16.18 | JNJ=7.42  BOT: JPM=0.88 | GOOGL=0.84 | UNH=0.81
   🧭 Regime Start Dist (train resets): high_vol=139 (35.4%), low_vol=130 (33.1%), medium_vol=124 (31.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00390_shp1p225_actor.weights.h5 (Sharpe=1.225, MDD=13.38%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00392_shp0p850_actor.weights.h5 (Sharpe=0.850, MDD=23.08%)

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
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00394_shp0p890_actor.weights.h5 (Sharpe=0.890, MDD=21.01%)

📚 EPISODE HORIZON UPDATE at 458,640 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 460,656 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 462,672 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 464,688 steps:
   Episode horizon set to full dataset
[CYCLE] Update 330/348 | Step 464,688/500,000 | Episode 397 | Time: 42856.3s
   📊 Metrics: Return=+304.10% | Sharpe=0.565 | DD=35.53% | Turnover=19.05%
   🎚️ Intra-Step TAPE: potential=0.2362 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0561 | critic_loss=0.0211 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0105 | risk_aux_total=0.0503 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=1.2306 | cvar_loss=0.0492 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=4.74 | std=9.71 | range=[0.45, 32.91]
   🏷️ Alpha Per-Asset  TOP: NEE=16.00 | PG=14.33 | JNJ=7.66  BOT: JPM=0.80 | GOOGL=0.76 | UNH=0.72
   🧭 Regime Start Dist (train resets): high_vol=140 (34.9%), low_vol=133 (33.2%), medium_vol=128 (31.9%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp0p937_actor.weights.h5 (Sharpe=0.937, MDD=23.57%)

📚 EPISODE HORIZON UPDATE at 466,704 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00400_shp0p827_actor.weights.h5 (Sharpe=0.827, MDD=24.37%)

📚 EPISODE HORIZON UPDATE at 468,720 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00401_shp0p758_actor.weights.h5 (Sharpe=0.758, MDD=24.58%)

📚 EPISODE HORIZON UPDATE at 470,736 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00402_shp0p842_actor.weights.h5 (Sharpe=0.842, MDD=23.41%)

📚 EPISODE HORIZON UPDATE at 472,752 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 474,768 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00404_shp1p162_actor.weights.h5 (Sharpe=1.162, MDD=15.76%)

📚 EPISODE HORIZON UPDATE at 476,784 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 478,800 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00406_shp0p874_actor.weights.h5 (Sharpe=0.874, MDD=22.69%)

📚 EPISODE HORIZON UPDATE at 480,816 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00407_shp0p751_actor.weights.h5 (Sharpe=0.751, MDD=23.65%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p348_actor.weights.h5 (Sharpe=1.348, MDD=14.69%)

📚 EPISODE HORIZON UPDATE at 482,832 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p172_actor.weights.h5 (Sharpe=1.172, MDD=13.90%)

📚 EPISODE HORIZON UPDATE at 484,848 steps:
   Episode horizon set to full dataset
[CYCLE] Update 340/348 | Step 484,848/500,000 | Episode 409 | Time: 44591.2s
   📊 Metrics: Return=+47.71% | Sharpe=1.172 | DD=13.90% | Turnover=13.58%
   🎚️ Intra-Step TAPE: potential=0.2805 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0612 | critic_loss=0.0391 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0195 | risk_aux_total=0.0561 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=1.3792 | cvar_loss=0.0552 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=5.58 | std=10.73 | range=[0.35, 32.94]
   🏷️ Alpha Per-Asset  TOP: NEE=24.35 | PG=16.97 | JNJ=5.46  BOT: JPM=0.81 | UNH=0.81 | LIN=0.79
   🧭 Regime Start Dist (train resets): high_vol=144 (34.9%), low_vol=138 (33.4%), medium_vol=131 (31.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.58% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5298
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00410_shp0p799_actor.weights.h5 (Sharpe=0.799, MDD=18.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00411_shp1p961_actor.weights.h5 (Sharpe=1.961, MDD=8.35%)

📚 EPISODE HORIZON UPDATE at 486,864 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 488,880 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 490,896 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00413_shp0p913_actor.weights.h5 (Sharpe=0.913, MDD=21.80%)

📚 EPISODE HORIZON UPDATE at 492,912 steps:
   Episode horizon set to full dataset
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00414_shp0p833_actor.weights.h5 (Sharpe=0.833, MDD=24.13%)

📚 EPISODE HORIZON UPDATE at 494,928 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 496,944 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 498,960 steps:
   Episode horizon set to full dataset

📚 EPISODE HORIZON UPDATE at 500,000 steps:
   Episode horizon set to full dataset
[CYCLE] Update 348/348 | Step 500,000/500,000 | Episode 416 | Time: 45900.1s
   📊 Metrics: Return=+205.70% | Sharpe=0.505 | DD=35.32% | Turnover=19.04%
   🎚️ Intra-Step TAPE: potential=0.7511 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0509 | critic_loss=0.0270 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0135 | risk_aux_total=0.0479 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=1.1704 | cvar_loss=0.0468 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=4.55 | std=9.42 | range=[0.47, 32.92]
   🏷️ Alpha Per-Asset  TOP: PG=17.62 | NEE=15.39 | JNJ=4.17  BOT: JPM=0.82 | LIN=0.81 | UNH=0.80
   🧭 Regime Start Dist (train resets): high_vol=149 (35.5%), low_vol=139 (33.1%), medium_vol=132 (31.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.329, dd 2.39% / trig 21.00%) | terminal=0.000 (peak 0.405) | TAPE=0.2897

[OK] THREE-COMPONENT TAPE v3 training completed!
   Total episodes: 416
   Total timesteps: 500,000
   Training time: 45900.10s (765.00min)
📊 Training summary saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_172715_summary.csv
💾 Final models saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00416_shp0p505_actor.weights.h5, /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00416_shp0p505_critic.weights.h5
🎯 Default selected checkpoint: final high-watermark-style checkpoint
[OK] Training complete
checkpoint_prefix: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00416_shp0p505