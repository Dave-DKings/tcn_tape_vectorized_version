[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
[OK] Actuarial feature check passed: {'Actuarial_Prob_30d': 54767, 'Actuarial_Expected_Recovery': 54767, 'Actuarial_Prob_60d': 54767, 'Actuarial_Reserve_Severity': 54767}
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
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_022909_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_022909_step_diagnostics.csv

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
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_022909_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260309_022909_metadata.json
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp0p750_actor.weights.h5 (Sharpe=0.750, MDD=11.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00003_shp1p116_actor.weights.h5 (Sharpe=1.116, MDD=10.27%)
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 1066.3s
   📊 Metrics: Return=+22.69% | Sharpe=0.437 | DD=14.37% | Turnover=34.31%
   🎚️ Intra-Step TAPE: potential=0.7337 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0848 | critic_loss=0.6258 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3129 | risk_aux_total=0.0733 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.8184 | cvar_loss=0.0727 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.24 | std=2.27 | range=[0.39, 17.01]
   🏷️ Alpha Per-Asset  TOP: GOOGL=3.64 | JNJ=3.36 | PG=3.09  BOT: JPM=1.54 | UNH=1.41 | CAT=1.24
   🧭 Regime Start Dist (train resets): high_vol=6 (37.5%), low_vol=6 (37.5%), medium_vol=4 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00014_shp0p817_actor.weights.h5 (Sharpe=0.817, MDD=11.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00017_shp0p870_actor.weights.h5 (Sharpe=0.870, MDD=10.79%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00018_shp0p869_actor.weights.h5 (Sharpe=0.869, MDD=9.69%)
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 2114.2s
   📊 Metrics: Return=+9.60% | Sharpe=0.151 | DD=11.95% | Turnover=48.11%
   🎚️ Intra-Step TAPE: potential=0.5921 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0759 | critic_loss=0.1297 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0649 | risk_aux_total=0.0667 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.6524 | cvar_loss=0.0661 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.91 | std=1.54 | range=[0.35, 9.38]
   🏷️ Alpha Per-Asset  TOP: NEE=3.85 | JNJ=3.65 | PG=3.35  BOT: UNH=1.00 | JPM=0.67 | CAT=0.58
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=11 (39.3%), medium_vol=7 (25.0%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 3161.6s
   📊 Metrics: Return=-14.16% | Sharpe=-0.250 | DD=37.30% | Turnover=30.25%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1119 | critic_loss=0.2132 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1066 | risk_aux_total=0.1080 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=2.6824 | cvar_loss=0.1073 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.67 | std=1.85 | range=[0.28, 9.14]
   🏷️ Alpha Per-Asset  TOP: JNJ=4.66 | PG=4.11 | NEE=2.49  BOT: UNH=0.61 | CAT=0.55 | JPM=0.44
   🧭 Regime Start Dist (train resets): high_vol=19 (43.2%), low_vol=14 (31.8%), medium_vol=11 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.532 (peak 0.532) | TAPE=0.2226
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00042_shp0p766_actor.weights.h5 (Sharpe=0.766, MDD=13.03%)
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 4210.7s
   📊 Metrics: Return=-27.44% | Sharpe=-0.449 | DD=46.29% | Turnover=32.26%
   🎚️ Intra-Step TAPE: potential=0.2343 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0917 | critic_loss=0.0598 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0299 | risk_aux_total=0.0853 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=2.1168 | cvar_loss=0.0847 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.30 | std=2.63 | range=[0.44, 16.05]
   🏷️ Alpha Per-Asset  TOP: PG=5.85 | JNJ=4.68 | NEE=2.86  BOT: UNH=0.90 | MSFT=0.89 | JPM=0.84
   🧭 Regime Start Dist (train resets): high_vol=24 (42.9%), low_vol=18 (32.1%), medium_vol=14 (25.0%)
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 5269.3s
   📊 Metrics: Return=-11.39% | Sharpe=-0.165 | DD=37.30% | Turnover=28.38%
   🎚️ Intra-Step TAPE: potential=0.2195 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1021 | critic_loss=0.0967 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0484 | risk_aux_total=0.0934 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=2.3179 | cvar_loss=0.0927 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.23 | std=2.56 | range=[0.44, 16.43]
   🏷️ Alpha Per-Asset  TOP: JNJ=5.74 | PG=5.64 | NEE=3.24  BOT: GOOGL=0.94 | JPM=0.78 | CAT=0.65
   🧭 Regime Start Dist (train resets): high_vol=27 (39.7%), low_vol=24 (35.3%), medium_vol=17 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00065_shp0p743_actor.weights.h5 (Sharpe=0.743, MDD=11.91%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 6324.9s
   📊 Metrics: Return=+28.91% | Sharpe=0.692 | DD=11.40% | Turnover=30.68%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0808 | critic_loss=0.0556 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0278 | risk_aux_total=0.0707 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.7525 | cvar_loss=0.0701 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.46 | std=1.70 | range=[0.43, 13.38]
   🏷️ Alpha Per-Asset  TOP: JNJ=3.22 | NEE=2.96 | PG=2.75  BOT: UNH=0.66 | CAT=0.61 | MSFT=0.58
   🧭 Regime Start Dist (train resets): high_vol=34 (40.5%), low_vol=29 (34.5%), medium_vol=21 (25.0%)
   🔒 Drawdown λ snapshot=1.827 (peak 1.827, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3441
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp0p797_actor.weights.h5 (Sharpe=0.797, MDD=11.45%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp0p755_actor.weights.h5 (Sharpe=0.755, MDD=11.59%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00091_shp0p764_actor.weights.h5 (Sharpe=0.764, MDD=11.87%)
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 7380.9s
   📊 Metrics: Return=+26.63% | Sharpe=0.607 | DD=11.61% | Turnover=26.88%
   🎚️ Intra-Step TAPE: potential=0.2495 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0668 | critic_loss=0.1309 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0654 | risk_aux_total=0.0540 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.3365 | cvar_loss=0.0535 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=4.19 | std=5.03 | range=[0.44, 22.88]
   🏷️ Alpha Per-Asset  TOP: JNJ=10.50 | PG=8.96 | NEE=8.80  BOT: MSFT=1.52 | CAT=0.95 | JPM=0.66
   🧭 Regime Start Dist (train resets): high_vol=38 (39.6%), low_vol=35 (36.5%), medium_vol=23 (24.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00094_shp0p815_actor.weights.h5 (Sharpe=0.815, MDD=10.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00096_shp0p804_actor.weights.h5 (Sharpe=0.804, MDD=12.48%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00101_shp0p838_actor.weights.h5 (Sharpe=0.838, MDD=10.23%)
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 8440.2s
   📊 Metrics: Return=+1.69% | Sharpe=-0.056 | DD=18.47% | Turnover=40.03%
   🎚️ Intra-Step TAPE: potential=0.2327 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0675 | critic_loss=0.1560 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0780 | risk_aux_total=0.0585 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=1.4459 | cvar_loss=0.0578 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.40 | std=4.28 | range=[0.35, 22.65]
   🏷️ Alpha Per-Asset  TOP: JNJ=9.94 | NEE=5.84 | PG=3.91  BOT: MSFT=0.46 | CAT=0.42 | JPM=0.41
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=40 (37.0%), medium_vol=26 (24.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00105_shp0p845_actor.weights.h5 (Sharpe=0.845, MDD=6.49%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 9497.2s
   📊 Metrics: Return=+5.53% | Sharpe=0.040 | DD=20.10% | Turnover=38.28%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0626 | critic_loss=0.1106 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0553 | risk_aux_total=0.0502 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=1.2402 | cvar_loss=0.0496 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.89 | std=2.29 | range=[0.58, 18.79]
   🏷️ Alpha Per-Asset  TOP: JNJ=4.91 | PG=4.76 | NEE=2.77  BOT: MSFT=0.88 | LIN=0.87 | CAT=0.79
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=46 (37.1%), medium_vol=30 (24.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2326

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
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 10557.0s
   📊 Metrics: Return=+38.91% | Sharpe=0.568 | DD=15.86% | Turnover=33.57%
   🎚️ Intra-Step TAPE: potential=0.5916 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0912 | critic_loss=0.1071 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0535 | risk_aux_total=0.0852 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=2.1121 | cvar_loss=0.0845 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=4.44 | std=6.58 | range=[0.62, 29.08]
   🏷️ Alpha Per-Asset  TOP: NEE=11.79 | PG=11.73 | JNJ=9.28  BOT: JPM=0.98 | GOOGL=0.89 | MSFT=0.80
   🧭 Regime Start Dist (train resets): high_vol=52 (39.4%), low_vol=47 (35.6%), medium_vol=33 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00130_shp1p109_actor.weights.h5 (Sharpe=1.109, MDD=11.34%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00131_shp1p016_actor.weights.h5 (Sharpe=1.016, MDD=11.05%)
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 11617.8s
   📊 Metrics: Return=+3.71% | Sharpe=0.045 | DD=36.61% | Turnover=20.09%
   🎚️ Intra-Step TAPE: potential=0.2268 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0976 | critic_loss=0.2135 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1068 | risk_aux_total=0.0850 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=2.1034 | cvar_loss=0.0841 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=4.69 | std=8.01 | range=[0.44, 30.76]
   🏷️ Alpha Per-Asset  TOP: PG=17.97 | JNJ=14.12 | NEE=9.18  BOT: JPM=0.62 | CAT=0.62 | UNH=0.62
   🧭 Regime Start Dist (train resets): high_vol=57 (39.6%), low_vol=51 (35.4%), medium_vol=36 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 12.40% / trig 21.00%) | terminal=0.000 (peak 0.422) | TAPE=0.2290
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00141_shp0p865_actor.weights.h5 (Sharpe=0.865, MDD=12.40%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00148_shp0p714_actor.weights.h5 (Sharpe=0.714, MDD=12.22%)
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 148 | Time: 12679.1s
   📊 Metrics: Return=+45.64% | Sharpe=0.714 | DD=12.22% | Turnover=20.85%
   🎚️ Intra-Step TAPE: potential=0.3640 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0947 | critic_loss=0.1060 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0530 | risk_aux_total=0.0843 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=2.0886 | cvar_loss=0.0835 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=5.90 | std=8.63 | range=[0.44, 31.65]
   🏷️ Alpha Per-Asset  TOP: JNJ=19.81 | PG=14.99 | NEE=10.89  BOT: JPM=0.75 | MSFT=0.72 | UNH=0.69
   🧭 Regime Start Dist (train resets): high_vol=58 (38.2%), low_vol=53 (34.9%), medium_vol=41 (27.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00151_shp0p901_actor.weights.h5 (Sharpe=0.901, MDD=13.23%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00156_shp0p991_actor.weights.h5 (Sharpe=0.991, MDD=13.12%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00160_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=12.89%)
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 160 | Time: 13746.6s
   📊 Metrics: Return=+52.01% | Sharpe=0.806 | DD=12.89% | Turnover=22.29%
   🎚️ Intra-Step TAPE: potential=0.7459 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1018 | critic_loss=0.1409 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0705 | risk_aux_total=0.0905 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=2.2429 | cvar_loss=0.0897 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.30 | std=6.21 | range=[0.36, 31.10]
   🏷️ Alpha Per-Asset  TOP: JNJ=12.16 | PG=7.66 | NEE=6.55  BOT: JPM=0.57 | CAT=0.57 | MSFT=0.56
   🧭 Regime Start Dist (train resets): high_vol=64 (39.0%), low_vol=58 (35.4%), medium_vol=42 (25.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.68% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4327
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00161_shp1p321_actor.weights.h5 (Sharpe=1.321, MDD=11.44%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00166_shp1p039_actor.weights.h5 (Sharpe=1.039, MDD=12.85%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00167_shp0p927_actor.weights.h5 (Sharpe=0.927, MDD=9.82%)
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 168 | Time: 14803.8s
   📊 Metrics: Return=+36.89% | Sharpe=0.555 | DD=17.75% | Turnover=29.83%
   🎚️ Intra-Step TAPE: potential=0.2607 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0595 | critic_loss=0.0789 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0395 | risk_aux_total=0.0514 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.2646 | cvar_loss=0.0506 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=5.12 | std=8.44 | range=[0.44, 31.73]
   🏷️ Alpha Per-Asset  TOP: PG=19.69 | JNJ=15.69 | NEE=8.65  BOT: GOOGL=0.64 | UNH=0.62 | JPM=0.59
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
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00179_shp0p953_actor.weights.h5 (Sharpe=0.953, MDD=9.08%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00180_shp0p760_actor.weights.h5 (Sharpe=0.760, MDD=9.03%)
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 180 | Time: 15937.8s
   📊 Metrics: Return=+75.46% | Sharpe=0.760 | DD=9.03% | Turnover=21.18%
   🎚️ Intra-Step TAPE: potential=0.2296 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0637 | critic_loss=0.1623 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0811 | risk_aux_total=0.0542 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.3358 | cvar_loss=0.0534 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.43 | std=7.36 | range=[0.47, 30.75]
   🏷️ Alpha Per-Asset  TOP: JNJ=14.12 | PG=9.94 | NEE=7.08  BOT: UNH=0.98 | LIN=0.91 | CAT=0.79
   🧭 Regime Start Dist (train resets): high_vol=69 (37.5%), low_vol=68 (37.0%), medium_vol=47 (25.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.99% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5084
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00182_shp0p968_actor.weights.h5 (Sharpe=0.968, MDD=12.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00189_shp0p846_actor.weights.h5 (Sharpe=0.846, MDD=12.31%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00193_shp0p967_actor.weights.h5 (Sharpe=0.967, MDD=12.34%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00194_shp0p822_actor.weights.h5 (Sharpe=0.822, MDD=13.18%)
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 196 | Time: 17470.7s
   📊 Metrics: Return=+36.45% | Sharpe=0.581 | DD=21.96% | Turnover=25.09%
   🎚️ Intra-Step TAPE: potential=0.6071 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0547 | critic_loss=0.1220 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0610 | risk_aux_total=0.0486 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=1.1941 | cvar_loss=0.0478 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.60 | std=6.69 | range=[0.47, 29.99]
   🏷️ Alpha Per-Asset  TOP: JNJ=10.19 | PG=9.86 | NEE=6.37  BOT: LIN=1.13 | CAT=0.78 | UNH=0.75
   🧭 Regime Start Dist (train resets): high_vol=71 (35.5%), low_vol=76 (38.0%), medium_vol=53 (26.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.85% / trig 21.00%) | terminal=0.000 (peak 0.003) | TAPE=0.3242
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00200_shp0p764_actor.weights.h5 (Sharpe=0.764, MDD=11.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00202_shp1p074_actor.weights.h5 (Sharpe=1.074, MDD=11.08%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00203_shp1p156_actor.weights.h5 (Sharpe=1.156, MDD=11.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00206_shp0p803_actor.weights.h5 (Sharpe=0.803, MDD=12.81%)
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 208 | Time: 18998.3s
   📊 Metrics: Return=+24.79% | Sharpe=0.364 | DD=21.80% | Turnover=34.06%
   🎚️ Intra-Step TAPE: potential=0.2318 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0968 | critic_loss=0.0738 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0369 | risk_aux_total=0.0914 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=2.2654 | cvar_loss=0.0906 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.63 | std=5.62 | range=[0.42, 29.12]
   🏷️ Alpha Per-Asset  TOP: JNJ=13.26 | PG=7.27 | NEE=1.10  BOT: GOOGL=0.65 | LIN=0.62 | MSFT=0.58
   🧭 Regime Start Dist (train resets): high_vol=75 (35.4%), low_vol=79 (37.3%), medium_vol=58 (27.4%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00216_shp0p737_actor.weights.h5 (Sharpe=0.737, MDD=13.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00217_shp0p743_actor.weights.h5 (Sharpe=0.743, MDD=10.90%)
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 224 | Time: 20523.6s
   📊 Metrics: Return=+32.49% | Sharpe=0.498 | DD=24.83% | Turnover=29.57%
   🎚️ Intra-Step TAPE: potential=0.2290 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0826 | critic_loss=0.1006 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0503 | risk_aux_total=0.0715 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=1.7624 | cvar_loss=0.0705 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.94 | std=6.94 | range=[0.32, 31.63]
   🏷️ Alpha Per-Asset  TOP: PG=14.84 | JNJ=7.75 | NEE=2.48  BOT: MSFT=0.43 | CAT=0.42 | JPM=0.41
   🧭 Regime Start Dist (train resets): high_vol=79 (34.6%), low_vol=86 (37.7%), medium_vol=63 (27.6%)

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.75
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 240 | Time: 22067.2s
   📊 Metrics: Return=-4.77% | Sharpe=-0.083 | DD=38.53% | Turnover=18.36%
   🎚️ Intra-Step TAPE: potential=0.5848 | delta_reward=+0.0028
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0793 | critic_loss=0.0770 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0385 | risk_aux_total=0.0732 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=1.8025 | cvar_loss=0.0721 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.07 | std=7.85 | range=[0.41, 31.27]
   🏷️ Alpha Per-Asset  TOP: JNJ=18.20 | PG=11.46 | MSFT=2.81  BOT: CAT=0.71 | XOM=0.67 | LIN=0.62
   🧭 Regime Start Dist (train resets): high_vol=85 (34.8%), low_vol=89 (36.5%), medium_vol=70 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.39% / trig 21.00%) | terminal=0.000 (peak 0.743) | TAPE=0.2266
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00241_shp0p719_actor.weights.h5 (Sharpe=0.719, MDD=13.46%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00243_shp0p816_actor.weights.h5 (Sharpe=0.816, MDD=11.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00247_shp0p873_actor.weights.h5 (Sharpe=0.873, MDD=9.72%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00248_shp0p943_actor.weights.h5 (Sharpe=0.943, MDD=10.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00250_shp0p889_actor.weights.h5 (Sharpe=0.889, MDD=11.03%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00253_shp0p843_actor.weights.h5 (Sharpe=0.843, MDD=10.87%)
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 256 | Time: 23598.7s
   📊 Metrics: Return=+28.51% | Sharpe=0.431 | DD=22.98% | Turnover=30.16%
   🎚️ Intra-Step TAPE: potential=0.7587 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0698 | critic_loss=0.1174 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0587 | risk_aux_total=0.0682 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=1.6840 | cvar_loss=0.0674 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.15 | std=7.80 | range=[0.41, 31.84]
   🏷️ Alpha Per-Asset  TOP: JNJ=18.53 | PG=11.42 | NEE=6.03  BOT: CAT=0.60 | JPM=0.56 | LIN=0.56
   🧭 Regime Start Dist (train resets): high_vol=89 (34.2%), low_vol=96 (36.9%), medium_vol=75 (28.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.44% / trig 21.00%) | terminal=0.000 (peak 0.015) | TAPE=0.2798
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00257_shp0p871_actor.weights.h5 (Sharpe=0.871, MDD=11.34%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00261_shp0p720_actor.weights.h5 (Sharpe=0.720, MDD=22.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00265_shp1p124_actor.weights.h5 (Sharpe=1.124, MDD=12.81%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00268_shp0p846_actor.weights.h5 (Sharpe=0.846, MDD=11.49%)

📚 EPISODE HORIZON UPDATE at 240,912 steps:
   Episode horizon: 1053 steps

📚 EPISODE HORIZON UPDATE at 242,424 steps:
   Episode horizon: 1127 steps
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 268 | Time: 25126.7s
   📊 Metrics: Return=+67.37% | Sharpe=0.846 | DD=11.49% | Turnover=15.04%
   🎚️ Intra-Step TAPE: potential=0.2187 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0592 | critic_loss=0.0335 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0168 | risk_aux_total=0.0519 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0012 | cvar_proxy=1.2663 | cvar_loss=0.0507 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=5.35 | std=10.30 | range=[0.36, 32.72]
   🏷️ Alpha Per-Asset  TOP: PG=21.94 | JNJ=21.83 | NEE=5.30  BOT: CAT=0.49 | GOOGL=0.47 | MSFT=0.44
   🧭 Regime Start Dist (train resets): high_vol=93 (34.2%), low_vol=101 (37.1%), medium_vol=78 (28.7%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00269_shp0p702_actor.weights.h5 (Sharpe=0.702, MDD=23.83%)

📚 EPISODE HORIZON UPDATE at 243,936 steps:
   Episode horizon: 1202 steps

📚 EPISODE HORIZON UPDATE at 245,448 steps:
   Episode horizon: 1276 steps

📚 EPISODE HORIZON UPDATE at 246,960 steps:
   Episode horizon: 1350 steps

📚 EPISODE HORIZON UPDATE at 248,472 steps:
   Episode horizon: 1425 steps
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00273_shp0p921_actor.weights.h5 (Sharpe=0.921, MDD=16.82%)

📚 EPISODE HORIZON UPDATE at 249,984 steps:
   Episode horizon: 1499 steps

📚 EPISODE HORIZON UPDATE at 251,496 steps:
   Episode horizon: 1500 steps
[CYCLE] Update 220/348 | Step 257,544/500,000 | Episode 280 | Time: 26649.4s
   📊 Metrics: Return=+24.84% | Sharpe=0.187 | DD=33.48% | Turnover=18.51%
   🎚️ Intra-Step TAPE: potential=0.2474 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1046 | critic_loss=0.0739 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0369 | risk_aux_total=0.0931 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=2.3017 | cvar_loss=0.0921 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.75 | std=9.52 | range=[0.40, 32.64]
   🏷️ Alpha Per-Asset  TOP: JNJ=24.27 | PG=12.68 | NEE=3.98  BOT: XOM=0.58 | GOOGL=0.58 | LIN=0.56
   🧭 Regime Start Dist (train resets): high_vol=96 (33.8%), low_vol=104 (36.6%), medium_vol=84 (29.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00286_shp0p720_actor.weights.h5 (Sharpe=0.720, MDD=20.08%)
[CYCLE] Update 230/348 | Step 272,664/500,000 | Episode 289 | Time: 28188.1s
   📊 Metrics: Return=+59.46% | Sharpe=0.555 | DD=21.79% | Turnover=25.88%
   🎚️ Intra-Step TAPE: potential=0.2372 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0916 | critic_loss=0.0787 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0393 | risk_aux_total=0.0764 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=1.8822 | cvar_loss=0.0753 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.83 | std=8.31 | range=[0.41, 32.62]
   🏷️ Alpha Per-Asset  TOP: PG=14.32 | JNJ=8.67 | NEE=7.85  BOT: MSFT=0.62 | GOOGL=0.62 | JPM=0.59
   🧭 Regime Start Dist (train resets): high_vol=98 (33.4%), low_vol=108 (36.9%), medium_vol=87 (29.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.96% / trig 21.00%) | terminal=0.000 (peak 0.001) | TAPE=0.3188
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00295_shp0p840_actor.weights.h5 (Sharpe=0.840, MDD=21.07%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00298_shp0p988_actor.weights.h5 (Sharpe=0.988, MDD=20.66%)
[CYCLE] Update 240/348 | Step 287,784/500,000 | Episode 300 | Time: 29711.7s
   📊 Metrics: Return=+19.24% | Sharpe=0.142 | DD=35.18% | Turnover=15.95%
   🎚️ Intra-Step TAPE: potential=0.5651 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1017 | critic_loss=0.0419 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0210 | risk_aux_total=0.0951 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0011 | cvar_proxy=2.3516 | cvar_loss=0.0941 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.18 | std=8.77 | range=[0.47, 32.21]
   🏷️ Alpha Per-Asset  TOP: JNJ=21.98 | PG=12.72 | NEE=1.83  BOT: JPM=0.74 | MSFT=0.71 | XOM=0.68
   🧭 Regime Start Dist (train resets): high_vol=105 (34.5%), low_vol=109 (35.9%), medium_vol=90 (29.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00306_shp0p706_actor.weights.h5 (Sharpe=0.706, MDD=19.58%)

📚 TURNOVER CURRICULUM UPDATE at 301,392 steps:
   Turnover penalty scalar: 0.9

📚 PPO ROLLOUT UPDATE at 301,392 steps:
   Timesteps per update: 2016

📚 PPO BATCH SIZE UPDATE at 301,392 steps:
   Batch size: 504
[CYCLE] Update 250/348 | Step 303,408/500,000 | Episode 312 | Time: 31281.5s
   📊 Metrics: Return=+44.15% | Sharpe=0.331 | DD=35.03% | Turnover=24.52%
   🎚️ Intra-Step TAPE: potential=0.3239 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0576 | critic_loss=0.0883 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0441 | risk_aux_total=0.0509 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0010 | cvar_proxy=1.2477 | cvar_loss=0.0499 | cvar_coef=0.0400
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=4.21 | std=8.96 | range=[0.48, 32.64]
   🏷️ Alpha Per-Asset  TOP: PG=14.72 | JNJ=8.28 | NEE=7.43  BOT: UNH=0.84 | CAT=0.84 | LIN=0.74
   🧭 Regime Start Dist (train resets): high_vol=108 (34.2%), low_vol=112 (35.4%), medium_vol=96 (30.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 5.63% / trig 21.00%) | terminal=0.000 (peak 0.251) | TAPE=0.2553
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00315_shp0p707_actor.weights.h5 (Sharpe=0.707, MDD=21.07%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00319_shp0p723_actor.weights.h5 (Sharpe=0.723, MDD=20.31%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00321_shp1p017_actor.weights.h5 (Sharpe=1.017, MDD=22.64%)