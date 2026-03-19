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
   Gate A: enabled (Sharpe <= 0.00 or MDD >= 30.0% -> force non-positive terminal bonus)
   Neutral Band: enabled (±0.020 around baseline)
   [CYCLE] Profile Manager: disabled (static profile only)
[RAND] Experiment Seed: 6042 (Base: 42, Offset: 6000)
[OK] Features: Enhanced (includes 2 covariance eigenvalues)
   Eigenvalues: ['Covariance_Eigenvalue_0', 'Covariance_Eigenvalue_1']
   Train shape: (25170, 67)
   Test shape: (9180, 67)
   ℹ️ Actuarial features disabled by config.

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.60, band=±0.20, scalar=0.10 -> 0.15 => 0.20 => 0.25 => 0.30)
      ↳ Schedule: 0.10@0 => 0.15@100,000 => 0.20@200,000 => 0.25@300,000 => 0.30@400,000
   ⚙️  Component 4: Execution Inertia (beta=0.50 -> 0.65 => 0.80 => 1.00, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.50@0 => 0.65@100,000 => 0.80@200,000 => 1.00@350,000
   ⚡ Parallel rollout envs: 4
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 30.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🌊 DSR Regime Scaling: ENABLED | low_mult=0.3 (vol<0.12) | mid_mult=1.0 | high_mult=1.5 (vol>0.25)
   📈 Outperformance Bonus (SPY): ENABLED | scalar=3.0
   🔐 Lagrangian CVaR: ENABLED | threshold=-0.035 | lr=0.002 | lambda_max=2.0 | penalty_scale=0.75
   Alpha Regularization: hhi_coef=0.005 | dispersion_coef=0.02 | target_std=0.1
   🧪 Aux Per-Asset Return Head: ENABLED | coef=0.35
   🔒 Dirichlet Alpha Cap: 16.0
   🔒 Drawdown dual controller (requested): target=27.00%, tolerance=-2.00% (trigger boundary ≈ 25.00%), lr=0.100, λ_init=0.05, λ_floor=0.00, λ_max=5.00, penalty_coef=0.50
   📐 Position constraints: max_single_asset=25%, min_cash=5%
   [DEBUG] Regime-balanced sampling: use_curriculum_learning=True, volatility_regime pre-existing=False
   🎲 Volatility regimes ready for sampling (computed):
      high_vol: 826 dates (32.8%)
      low_vol: 826 dates (32.8%)
      medium_vol: 865 dates (34.4%)
   🧭 Regime start buckets (train env):
      high_vol: 826 dates (32.8%)
      low_vol: 826 dates (32.8%)
      medium_vol: 865 dates (34.4%)
   [OK] Drawdown controller armed in env: target=27.00%, trigger=25.00%, λ_init=0.050, λ_floor=0.000, λ_max=5.00, penalty_coef=0.50
[OK] THREE-COMPONENT TAPE v3 Environments created:
   Training: 2517 days
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
   🔀 Cross-Asset Mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Recurrent memory: enabled=True | units=64 | dropout=0.1
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
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_070726_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_070726_step_diagnostics.csv

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
      0+ steps: scalar=0.10
      100,000+ steps: scalar=0.15
      200,000+ steps: scalar=0.20
      300,000+ steps: scalar=0.25
      400,000+ steps: scalar=0.30
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.50
      100,000+ steps: beta=0.65
      200,000+ steps: beta=0.80
      350,000+ steps: beta=1.00
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.60, MDD <= 30.0%, skip_on_det_validation=True)
   ⏹️ Training early-stop: enabled (warmup=100,000 steps, patience=25 updates, min_delta=0.010, hard_dd=60.0% x 12)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_070726_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_070726_metadata.json
[CYCLE] Update 1/348 | Step 1,008/500,000 | Episode 0 | Time: 90.5s
   📊 Metrics: Return=+29.88% | Sharpe=2.190 | DD=3.73% | Turnover=26.94%
   🎚️ Intra-Step TAPE: potential=0.7443 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2573 | critic_loss=0.4559 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2279 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0008 | dispersion_loss=0.0004
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1901 | ema=2.1901 | best_ema=2.1901 | no_improve=0
[CYCLE] Update 2/348 | Step 2,016/500,000 | Episode 0 | Time: 165.4s
   📊 Metrics: Return=+52.33% | Sharpe=1.563 | DD=8.10% | Turnover=27.30%
   🎚️ Intra-Step TAPE: potential=0.3152 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1860 | critic_loss=0.3063 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1532 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0006
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5629 | ema=2.1274 | best_ema=2.1274 | no_improve=0
   🔬 Alpha Diversity: mean=2.09 | std=1.07 | range=[0.80, 7.19] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.77 | JPM=2.71 | NVDA=2.20  BOT: NEE=1.61 | PG=1.46 | GLD=1.21
   🧭 Regime Start Dist (train resets): high_vol=2 (50.0%), low_vol=1 (25.0%), medium_vol=1 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p000_actor.weights.h5 (Sharpe=1.000, MDD=18.84%)
[CYCLE] Update 3/348 | Step 3,024/500,000 | Episode 4 | Time: 239.9s
   📊 Metrics: Return=+19.47% | Sharpe=0.453 | DD=8.84% | Turnover=28.12%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1428 | critic_loss=0.2677 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1338 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0007
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4529 | ema=1.9600 | best_ema=1.9600 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.050) | TAPE=0.2965
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01358) | SPY bonus=0.005 (SPY ret=-0.01396)
[CYCLE] Update 4/348 | Step 4,032/500,000 | Episode 4 | Time: 314.1s
   📊 Metrics: Return=+15.15% | Sharpe=1.896 | DD=2.77% | Turnover=35.13%
   🎚️ Intra-Step TAPE: potential=0.7368 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1164 | critic_loss=0.2328 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1164 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0007
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8958 | ema=1.9536 | best_ema=1.9536 | no_improve=0
   🔬 Alpha Diversity: mean=1.03 | std=0.45 | range=[0.46, 3.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=1.09 | AMZN=0.98 | XOM=0.97  BOT: MSFT=0.85 | PG=0.77 | NEE=0.75
   🧭 Regime Start Dist (train resets): high_vol=4 (50.0%), low_vol=3 (37.5%), medium_vol=1 (12.5%)
[CYCLE] Update 5/348 | Step 5,040/500,000 | Episode 4 | Time: 388.0s
   📊 Metrics: Return=+5.27% | Sharpe=0.109 | DD=18.51% | Turnover=35.87%
   🎚️ Intra-Step TAPE: potential=0.2332 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1028 | critic_loss=0.2792 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1396 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0008
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1088 | ema=1.7691 | best_ema=1.7691 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp1p241_actor.weights.h5 (Sharpe=1.241, MDD=11.26%)
[CYCLE] Update 6/348 | Step 6,048/500,000 | Episode 8 | Time: 462.1s
   📊 Metrics: Return=+20.40% | Sharpe=0.460 | DD=11.61% | Turnover=37.05%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0935 | critic_loss=0.1988 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0994 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0008
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4602 | ema=1.6382 | best_ema=1.6382 | no_improve=0
   🔬 Alpha Diversity: mean=0.78 | std=0.20 | range=[0.50, 1.80] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=0.82 | GLD=0.78 | XOM=0.77  BOT: NVDA=0.69 | PG=0.66 | NEE=0.62
   🧭 Regime Start Dist (train resets): high_vol=5 (41.7%), low_vol=6 (50.0%), medium_vol=1 (8.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3050
[CYCLE] Update 7/348 | Step 7,056/500,000 | Episode 8 | Time: 535.9s
   📊 Metrics: Return=+11.88% | Sharpe=0.903 | DD=8.48% | Turnover=39.33%
   🎚️ Intra-Step TAPE: potential=0.2246 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0876 | critic_loss=0.2306 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1153 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9029 | ema=1.5647 | best_ema=1.5647 | no_improve=0
[CYCLE] Update 8/348 | Step 8,064/500,000 | Episode 8 | Time: 610.4s
   📊 Metrics: Return=+21.46% | Sharpe=0.659 | DD=15.73% | Turnover=39.47%
   🎚️ Intra-Step TAPE: potential=0.7328 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0857 | critic_loss=0.2815 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1408 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6593 | ema=1.4741 | best_ema=1.4741 | no_improve=0
   🔬 Alpha Diversity: mean=0.72 | std=0.24 | range=[0.50, 1.84] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=0.69 | GLD=0.69 | AMZN=0.69  BOT: MSFT=0.63 | PG=0.61 | NEE=0.59
   🧭 Regime Start Dist (train resets): high_vol=5 (41.7%), low_vol=6 (50.0%), medium_vol=1 (8.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp0p852_actor.weights.h5 (Sharpe=0.852, MDD=25.34%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00012_shp0p763_actor.weights.h5 (Sharpe=0.763, MDD=12.81%)
[CYCLE] Update 9/348 | Step 9,072/500,000 | Episode 12 | Time: 686.2s
   📊 Metrics: Return=+33.32% | Sharpe=0.763 | DD=12.81% | Turnover=40.84%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0811 | critic_loss=0.1752 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0876 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7632 | ema=1.4030 | best_ema=1.4030 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4061
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 761.2s
   📊 Metrics: Return=+3.22% | Sharpe=0.167 | DD=10.06% | Turnover=39.52%
   🎚️ Intra-Step TAPE: potential=0.2373 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0813 | critic_loss=0.1392 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0696 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1666 | ema=1.2794 | best_ema=1.2794 | no_improve=0
   🔬 Alpha Diversity: mean=0.78 | std=0.20 | range=[0.49, 1.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=0.79 | XOM=0.77 | AMZN=0.77  BOT: PG=0.69 | NEE=0.69 | NVDA=0.66
   🧭 Regime Start Dist (train resets): high_vol=5 (31.2%), low_vol=7 (43.8%), medium_vol=4 (25.0%)
[CYCLE] Update 11/348 | Step 11,088/500,000 | Episode 12 | Time: 836.7s
   📊 Metrics: Return=+10.48% | Sharpe=0.344 | DD=10.06% | Turnover=39.78%
   🎚️ Intra-Step TAPE: potential=0.5511 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0754 | critic_loss=0.1945 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0972 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3437 | ema=1.1858 | best_ema=1.1858 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00016_shp0p987_actor.weights.h5 (Sharpe=0.987, MDD=10.20%)
[CYCLE] Update 12/348 | Step 12,096/500,000 | Episode 16 | Time: 911.6s
   📊 Metrics: Return=+44.63% | Sharpe=0.987 | DD=10.20% | Turnover=39.28%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0729 | critic_loss=0.2162 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1081 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9873 | ema=1.1660 | best_ema=1.1660 | no_improve=0
   🔬 Alpha Diversity: mean=0.96 | std=0.13 | range=[0.69, 1.43] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=1.03 | XOM=1.02 | GLD=0.97  BOT: PG=0.88 | NEE=0.88 | NVDA=0.87
   🧭 Regime Start Dist (train resets): high_vol=6 (30.0%), low_vol=7 (35.0%), medium_vol=7 (35.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 12 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5095
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00233) | SPY bonus=0.008 (SPY ret=-0.00109)
[CYCLE] Update 13/348 | Step 13,104/500,000 | Episode 16 | Time: 987.3s
   📊 Metrics: Return=+7.66% | Sharpe=0.567 | DD=6.66% | Turnover=36.38%
   🎚️ Intra-Step TAPE: potential=0.2552 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0707 | critic_loss=0.1722 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0861 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5670 | ema=1.1061 | best_ema=1.1061 | no_improve=0
[CYCLE] Update 14/348 | Step 14,112/500,000 | Episode 16 | Time: 1062.0s
   📊 Metrics: Return=+15.35% | Sharpe=0.547 | DD=6.66% | Turnover=34.04%
   🎚️ Intra-Step TAPE: potential=0.2781 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0672 | critic_loss=0.1838 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0919 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5475 | ema=1.0502 | best_ema=1.0502 | no_improve=0
   🔬 Alpha Diversity: mean=1.54 | std=0.21 | range=[0.80, 2.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=1.70 | JPM=1.67 | XOM=1.65  BOT: NEE=1.50 | GLD=1.49 | PG=1.44
   🧭 Regime Start Dist (train resets): high_vol=6 (30.0%), low_vol=7 (35.0%), medium_vol=7 (35.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 14 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00019_shp1p448_actor.weights.h5 (Sharpe=1.448, MDD=8.99%)
[CYCLE] Update 15/348 | Step 15,120/500,000 | Episode 20 | Time: 1136.5s
   📊 Metrics: Return=+12.59% | Sharpe=0.232 | DD=13.92% | Turnover=33.56%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0738 | critic_loss=0.2425 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1213 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2324 | ema=0.9684 | best_ema=0.9684 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2590
[CYCLE] Update 16/348 | Step 16,128/500,000 | Episode 20 | Time: 1211.4s
   📊 Metrics: Return=-0.01% | Sharpe=-0.071 | DD=10.81% | Turnover=30.41%
   🎚️ Intra-Step TAPE: potential=0.2517 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0704 | critic_loss=0.1863 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0931 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0709 | ema=0.8645 | best_ema=0.8645 | no_improve=0
   🔬 Alpha Diversity: mean=1.56 | std=0.29 | range=[0.66, 2.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.71 | JPM=1.70 | XOM=1.66  BOT: GLD=1.58 | NEE=1.53 | PG=1.48
   🧭 Regime Start Dist (train resets): high_vol=8 (33.3%), low_vol=8 (33.3%), medium_vol=8 (33.3%)
[CYCLE] Update 17/348 | Step 17,136/500,000 | Episode 20 | Time: 1291.8s
   📊 Metrics: Return=+31.19% | Sharpe=0.950 | DD=10.81% | Turnover=30.42%
   🎚️ Intra-Step TAPE: potential=0.7389 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0682 | critic_loss=0.2238 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1119 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9501 | ema=0.8731 | best_ema=0.8731 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00021_shp1p176_actor.weights.h5 (Sharpe=1.176, MDD=10.81%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00022_shp0p684_actor.weights.h5 (Sharpe=0.684, MDD=26.84%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00023_shp0p758_actor.weights.h5 (Sharpe=0.758, MDD=10.09%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00024_shp1p461_actor.weights.h5 (Sharpe=1.461, MDD=9.31%)
[CYCLE] Update 18/348 | Step 18,144/500,000 | Episode 24 | Time: 1366.5s
   📊 Metrics: Return=+73.18% | Sharpe=1.461 | DD=9.31% | Turnover=31.65%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0656 | critic_loss=0.1331 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0666 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4613 | ema=0.9319 | best_ema=0.9319 | no_improve=0
   🔬 Alpha Diversity: mean=1.06 | std=0.14 | range=[0.69, 1.43] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=1.13 | AMZN=1.13 | MSFT=1.12  BOT: NEE=1.05 | GLD=1.04 | PG=0.97
   🧭 Regime Start Dist (train resets): high_vol=11 (39.3%), low_vol=9 (32.1%), medium_vol=8 (28.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 18 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5909
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00375) | SPY bonus=0.011 (SPY ret=-0.00058)
[CYCLE] Update 19/348 | Step 19,152/500,000 | Episode 24 | Time: 1440.5s
   📊 Metrics: Return=+11.43% | Sharpe=0.800 | DD=9.55% | Turnover=37.44%
   🎚️ Intra-Step TAPE: potential=0.2324 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0631 | critic_loss=0.1196 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0598 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8004 | ema=0.9187 | best_ema=0.9187 | no_improve=0
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1514.5s
   📊 Metrics: Return=+41.60% | Sharpe=1.561 | DD=9.55% | Turnover=38.74%
   🎚️ Intra-Step TAPE: potential=0.7508 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0659 | critic_loss=0.1367 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0683 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5612 | ema=0.9830 | best_ema=0.9830 | no_improve=0
   🔬 Alpha Diversity: mean=0.76 | std=0.10 | range=[0.47, 1.02] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=0.86 | CAT=0.82 | AMZN=0.80  BOT: NVDA=0.75 | JNJ=0.74 | PG=0.72
   🧭 Regime Start Dist (train resets): high_vol=11 (39.3%), low_vol=9 (32.1%), medium_vol=8 (28.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 20 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp0p790_actor.weights.h5 (Sharpe=0.790, MDD=13.62%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00027_shp0p967_actor.weights.h5 (Sharpe=0.967, MDD=10.92%)
[CYCLE] Update 21/348 | Step 21,168/500,000 | Episode 28 | Time: 1589.7s
   📊 Metrics: Return=+1.61% | Sharpe=-0.091 | DD=9.89% | Turnover=38.92%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0692 | critic_loss=0.2105 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1053 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0912 | ema=0.8756 | best_ema=0.8756 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2421
[CYCLE] Update 22/348 | Step 22,176/500,000 | Episode 28 | Time: 1664.5s
   📊 Metrics: Return=+9.46% | Sharpe=0.667 | DD=6.30% | Turnover=39.80%
   🎚️ Intra-Step TAPE: potential=0.2497 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0664 | critic_loss=0.0711 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0355 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6669 | ema=0.8547 | best_ema=0.8547 | no_improve=0
   🔬 Alpha Diversity: mean=0.67 | std=0.10 | range=[0.37, 0.89] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.71 | JPM=0.71 | JNJ=0.70  BOT: GLD=0.68 | PG=0.68 | NEE=0.67
   🧭 Regime Start Dist (train resets): high_vol=14 (43.8%), low_vol=10 (31.2%), medium_vol=8 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 22 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 23/348 | Step 23,184/500,000 | Episode 28 | Time: 1738.0s
   📊 Metrics: Return=+36.12% | Sharpe=1.412 | DD=6.30% | Turnover=39.81%
   🎚️ Intra-Step TAPE: potential=0.7457 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0679 | critic_loss=0.1286 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0643 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4115 | ema=0.9104 | best_ema=0.9104 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00030_shp0p684_actor.weights.h5 (Sharpe=0.684, MDD=15.88%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p748_actor.weights.h5 (Sharpe=0.748, MDD=25.33%)
[CYCLE] Update 24/348 | Step 24,192/500,000 | Episode 32 | Time: 1810.5s
   📊 Metrics: Return=+54.74% | Sharpe=0.748 | DD=25.33% | Turnover=40.97%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0617 | critic_loss=0.1061 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0530 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7478 | ema=0.8941 | best_ema=0.8941 | no_improve=0
   🔬 Alpha Diversity: mean=0.75 | std=0.09 | range=[0.51, 1.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.78 | MSFT=0.76 | JPM=0.76  BOT: CAT=0.71 | PG=0.69 | NEE=0.68
   🧭 Regime Start Dist (train resets): high_vol=16 (44.4%), low_vol=12 (33.3%), medium_vol=8 (22.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 24 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3399
[CYCLE] Update 25/348 | Step 25,200/500,000 | Episode 32 | Time: 1883.1s
   📊 Metrics: Return=+18.02% | Sharpe=1.659 | DD=7.62% | Turnover=38.10%
   🎚️ Intra-Step TAPE: potential=0.5321 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0605 | critic_loss=0.0893 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0447 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6594 | ema=0.9706 | best_ema=0.9706 | no_improve=0
[CYCLE] Update 26/348 | Step 26,208/500,000 | Episode 32 | Time: 1955.5s
   📊 Metrics: Return=+13.60% | Sharpe=0.406 | DD=17.43% | Turnover=36.59%
   🎚️ Intra-Step TAPE: potential=0.3158 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0639 | critic_loss=0.1076 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0538 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4060 | ema=0.9142 | best_ema=0.9142 | no_improve=0
   🔬 Alpha Diversity: mean=1.01 | std=0.17 | range=[0.48, 1.35] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.11 | XOM=1.08 | AMZN=1.08  BOT: GLD=1.03 | NEE=1.01 | PG=0.97
   🧭 Regime Start Dist (train resets): high_vol=16 (44.4%), low_vol=12 (33.3%), medium_vol=8 (22.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 26 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00033_shp0p600_actor.weights.h5 (Sharpe=0.600, MDD=17.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00036_shp0p987_actor.weights.h5 (Sharpe=0.987, MDD=10.33%)
[CYCLE] Update 27/348 | Step 27,216/500,000 | Episode 36 | Time: 2027.7s
   📊 Metrics: Return=+46.29% | Sharpe=0.987 | DD=10.33% | Turnover=36.87%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0647 | critic_loss=0.0805 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0402 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9870 | ema=0.9215 | best_ema=0.9215 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5185
[CYCLE] Update 28/348 | Step 28,224/500,000 | Episode 36 | Time: 2100.0s
   📊 Metrics: Return=+15.90% | Sharpe=1.070 | DD=9.16% | Turnover=39.45%
   🎚️ Intra-Step TAPE: potential=0.3269 | delta_reward=-0.0021
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0635 | critic_loss=0.0642 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0321 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0703 | ema=0.9363 | best_ema=0.9363 | no_improve=0
   🔬 Alpha Diversity: mean=0.75 | std=0.08 | range=[0.55, 1.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.82 | JNJ=0.82 | JPM=0.75  BOT: PG=0.74 | NEE=0.73 | NVDA=0.73
   🧭 Regime Start Dist (train resets): high_vol=18 (45.0%), low_vol=12 (30.0%), medium_vol=10 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 28 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 29/348 | Step 29,232/500,000 | Episode 36 | Time: 2172.6s
   📊 Metrics: Return=+43.69% | Sharpe=1.591 | DD=9.16% | Turnover=40.01%
   🎚️ Intra-Step TAPE: potential=0.7442 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0606 | critic_loss=0.0990 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0495 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5909 | ema=1.0018 | best_ema=1.0018 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00037_shp0p767_actor.weights.h5 (Sharpe=0.767, MDD=14.61%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00039_shp1p398_actor.weights.h5 (Sharpe=1.398, MDD=10.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00040_shp0p766_actor.weights.h5 (Sharpe=0.766, MDD=10.65%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 2245.7s
   📊 Metrics: Return=+37.98% | Sharpe=0.766 | DD=10.65% | Turnover=40.44%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0628 | critic_loss=0.1002 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0501 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7661 | ema=0.9782 | best_ema=0.9782 | no_improve=0
   🔬 Alpha Diversity: mean=0.66 | std=0.06 | range=[0.46, 0.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.73 | GLD=0.70 | JNJ=0.67  BOT: MSFT=0.65 | PG=0.64 | NEE=0.64
   🧭 Regime Start Dist (train resets): high_vol=20 (45.5%), low_vol=14 (31.8%), medium_vol=10 (22.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 30 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3974
[CYCLE] Update 31/348 | Step 31,248/500,000 | Episode 40 | Time: 2318.1s
   📊 Metrics: Return=+12.86% | Sharpe=0.906 | DD=8.67% | Turnover=40.45%
   🎚️ Intra-Step TAPE: potential=0.3330 | delta_reward=-0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0569 | critic_loss=0.0952 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0476 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9062 | ema=0.9710 | best_ema=0.9710 | no_improve=0
[CYCLE] Update 32/348 | Step 32,256/500,000 | Episode 40 | Time: 2392.1s
   📊 Metrics: Return=+13.34% | Sharpe=0.389 | DD=15.27% | Turnover=41.24%
   🎚️ Intra-Step TAPE: potential=0.5172 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0608 | critic_loss=0.1086 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0543 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3894 | ema=0.9129 | best_ema=0.9129 | no_improve=0
   🔬 Alpha Diversity: mean=0.61 | std=0.04 | range=[0.50, 0.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.67 | GLD=0.64 | JPM=0.62  BOT: NEE=0.60 | AMZN=0.60 | NVDA=0.59
   🧭 Regime Start Dist (train resets): high_vol=20 (45.5%), low_vol=14 (31.8%), medium_vol=10 (22.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 32 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00041_shp0p614_actor.weights.h5 (Sharpe=0.614, MDD=28.05%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00043_shp0p652_actor.weights.h5 (Sharpe=0.652, MDD=18.17%)
[CYCLE] Update 33/348 | Step 33,264/500,000 | Episode 44 | Time: 2465.7s
   📊 Metrics: Return=-2.22% | Sharpe=-0.058 | DD=32.78% | Turnover=42.10%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0624 | critic_loss=0.1037 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0518 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0581 | ema=0.8158 | best_ema=0.8158 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.038 (peak 0.043) | TAPE=0.2017
[CYCLE] Update 34/348 | Step 34,272/500,000 | Episode 44 | Time: 2539.1s
   📊 Metrics: Return=+4.11% | Sharpe=0.277 | DD=7.45% | Turnover=41.32%
   🎚️ Intra-Step TAPE: potential=0.2498 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0616 | critic_loss=0.0427 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0213 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2769 | ema=0.7619 | best_ema=0.7619 | no_improve=0
   🔬 Alpha Diversity: mean=0.71 | std=0.18 | range=[0.55, 1.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.70 | JNJ=0.68 | NEE=0.67  BOT: PG=0.64 | AMZN=0.64 | NVDA=0.64
   🧭 Regime Start Dist (train resets): high_vol=22 (45.8%), low_vol=15 (31.2%), medium_vol=11 (22.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 34 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 35/348 | Step 35,280/500,000 | Episode 44 | Time: 2612.1s
   📊 Metrics: Return=+0.02% | Sharpe=-0.134 | DD=15.56% | Turnover=41.33%
   🎚️ Intra-Step TAPE: potential=0.2793 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0627 | critic_loss=0.0591 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0296 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1338 | ema=0.6723 | best_ema=0.6723 | no_improve=0
[CYCLE] Update 36/348 | Step 36,288/500,000 | Episode 48 | Time: 2684.7s
   📊 Metrics: Return=+12.07% | Sharpe=0.224 | DD=14.58% | Turnover=41.83%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0649 | critic_loss=0.0939 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0469 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2239 | ema=0.6275 | best_ema=0.6275 | no_improve=0
   🔬 Alpha Diversity: mean=0.70 | std=0.17 | range=[0.54, 1.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.69 | NEE=0.67 | JNJ=0.67  BOT: NVDA=0.64 | MSFT=0.64 | CAT=0.63
   🧭 Regime Start Dist (train resets): high_vol=23 (44.2%), low_vol=17 (32.7%), medium_vol=12 (23.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 36 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.008) | TAPE=0.2614
[CYCLE] Update 37/348 | Step 37,296/500,000 | Episode 48 | Time: 2757.1s
   📊 Metrics: Return=+1.58% | Sharpe=-0.002 | DD=6.22% | Turnover=40.88%
   🎚️ Intra-Step TAPE: potential=0.7019 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0639 | critic_loss=0.0494 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0247 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0018 | ema=0.5645 | best_ema=0.5645 | no_improve=0
[CYCLE] Update 38/348 | Step 38,304/500,000 | Episode 48 | Time: 2830.6s
   📊 Metrics: Return=-1.58% | Sharpe=-0.286 | DD=7.26% | Turnover=39.36%
   🎚️ Intra-Step TAPE: potential=0.2282 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0639 | critic_loss=0.0544 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0272 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0007 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2865 | ema=0.4794 | best_ema=0.4794 | no_improve=0
   🔬 Alpha Diversity: mean=0.91 | std=0.56 | range=[0.61, 3.35] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=0.78 | XOM=0.75 | GLD=0.74  BOT: AMZN=0.72 | CAT=0.72 | NVDA=0.70
   🧭 Regime Start Dist (train resets): high_vol=23 (44.2%), low_vol=17 (32.7%), medium_vol=12 (23.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00052_shp0p682_actor.weights.h5 (Sharpe=0.682, MDD=10.90%)
[CYCLE] Update 39/348 | Step 39,312/500,000 | Episode 52 | Time: 2903.2s
   📊 Metrics: Return=+29.37% | Sharpe=0.682 | DD=10.90% | Turnover=39.07%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0646 | critic_loss=0.0744 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0372 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6821 | ema=0.4997 | best_ema=0.4997 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3575
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 2977.0s
   📊 Metrics: Return=-5.06% | Sharpe=-0.455 | DD=15.92% | Turnover=38.16%
   🎚️ Intra-Step TAPE: potential=0.2254 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0585 | critic_loss=0.0677 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0339 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4554 | ema=0.4042 | best_ema=0.4042 | no_improve=0
   🔬 Alpha Diversity: mean=0.96 | std=0.11 | range=[0.71, 1.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=0.99 | XOM=0.98 | JNJ=0.98  BOT: AMZN=0.92 | CAT=0.91 | NVDA=0.87
   🧭 Regime Start Dist (train resets): high_vol=24 (42.9%), low_vol=18 (32.1%), medium_vol=14 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 40 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 41/348 | Step 41,328/500,000 | Episode 52 | Time: 3050.6s
   📊 Metrics: Return=+5.67% | Sharpe=0.142 | DD=27.78% | Turnover=37.44%
   🎚️ Intra-Step TAPE: potential=0.2470 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0576 | critic_loss=0.0750 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0375 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1418 | ema=0.3780 | best_ema=0.3780 | no_improve=0
[CYCLE] Update 42/348 | Step 42,336/500,000 | Episode 56 | Time: 3123.3s
   📊 Metrics: Return=+3.36% | Sharpe=-0.038 | DD=8.24% | Turnover=37.20%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0583 | critic_loss=0.0945 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0473 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0379 | ema=0.3364 | best_ema=0.3364 | no_improve=0
   🔬 Alpha Diversity: mean=0.96 | std=0.13 | range=[0.48, 1.19] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.06 | JNJ=1.02 | XOM=1.02  BOT: NVDA=0.97 | NEE=0.97 | MSFT=0.95
   🧭 Regime Start Dist (train resets): high_vol=25 (41.7%), low_vol=19 (31.7%), medium_vol=16 (26.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 42 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2415
[CYCLE] Update 43/348 | Step 43,344/500,000 | Episode 56 | Time: 3196.9s
   📊 Metrics: Return=-0.78% | Sharpe=-0.111 | DD=19.84% | Turnover=35.87%
   🎚️ Intra-Step TAPE: potential=0.2368 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0632 | critic_loss=0.0452 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0226 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1115 | ema=0.2916 | best_ema=0.2916 | no_improve=0
[CYCLE] Update 44/348 | Step 44,352/500,000 | Episode 56 | Time: 3271.2s
   📊 Metrics: Return=+21.67% | Sharpe=0.458 | DD=25.32% | Turnover=35.30%
   🎚️ Intra-Step TAPE: potential=0.7085 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0588 | critic_loss=0.0531 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0266 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4584 | ema=0.3083 | best_ema=0.3083 | no_improve=0
   🔬 Alpha Diversity: mean=1.17 | std=0.13 | range=[0.68, 1.53] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.32 | AMZN=1.23 | JPM=1.22  BOT: JNJ=1.18 | MSFT=1.17 | NVDA=1.15
   🧭 Regime Start Dist (train resets): high_vol=25 (41.7%), low_vol=19 (31.7%), medium_vol=16 (26.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 44 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00057_shp0p610_actor.weights.h5 (Sharpe=0.610, MDD=25.32%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00060_shp0p765_actor.weights.h5 (Sharpe=0.765, MDD=19.76%)
[CYCLE] Update 45/348 | Step 45,360/500,000 | Episode 60 | Time: 3346.3s
   📊 Metrics: Return=+38.30% | Sharpe=0.765 | DD=19.76% | Turnover=34.65%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0557 | critic_loss=0.0399 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0200 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7650 | ema=0.3539 | best_ema=0.3539 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3651
[CYCLE] Update 46/348 | Step 46,368/500,000 | Episode 60 | Time: 3421.9s
   📊 Metrics: Return=+4.40% | Sharpe=0.257 | DD=7.05% | Turnover=35.46%
   🎚️ Intra-Step TAPE: potential=0.2361 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0580 | critic_loss=0.0342 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0171 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2572 | ema=0.3443 | best_ema=0.3443 | no_improve=0
   🔬 Alpha Diversity: mean=1.06 | std=0.31 | range=[0.78, 2.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.03 | AMZN=1.02 | XOM=0.99  BOT: NVDA=0.94 | PG=0.94 | JNJ=0.93
   🧭 Regime Start Dist (train resets): high_vol=26 (40.6%), low_vol=21 (32.8%), medium_vol=17 (26.6%)
[CYCLE] Update 47/348 | Step 47,376/500,000 | Episode 60 | Time: 3497.1s
   📊 Metrics: Return=+11.29% | Sharpe=0.340 | DD=13.50% | Turnover=36.29%
   🎚️ Intra-Step TAPE: potential=0.5917 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0636 | critic_loss=0.0443 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0222 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3399 | ema=0.3438 | best_ema=0.3438 | no_improve=0
[CYCLE] Update 48/348 | Step 48,384/500,000 | Episode 64 | Time: 3570.3s
   📊 Metrics: Return=+23.12% | Sharpe=0.364 | DD=21.72% | Turnover=36.10%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0608 | critic_loss=0.0614 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0307 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3636 | ema=0.3458 | best_ema=0.3458 | no_improve=0
   🔬 Alpha Diversity: mean=1.14 | std=0.46 | range=[0.78, 3.53] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.08 | AMZN=1.02 | NEE=1.01  BOT: JNJ=0.98 | XOM=0.97 | NVDA=0.96
   🧭 Regime Start Dist (train resets): high_vol=28 (41.2%), low_vol=22 (32.4%), medium_vol=18 (26.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2627
[CYCLE] Update 49/348 | Step 49,392/500,000 | Episode 64 | Time: 3645.4s
   📊 Metrics: Return=-5.60% | Sharpe=-0.647 | DD=15.02% | Turnover=34.60%
   🎚️ Intra-Step TAPE: potential=0.2292 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0567 | critic_loss=0.0418 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0209 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.6468 | ema=0.2465 | best_ema=0.2465 | no_improve=0
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 3720.4s
   📊 Metrics: Return=+6.19% | Sharpe=0.149 | DD=15.02% | Turnover=35.28%
   🎚️ Intra-Step TAPE: potential=0.2643 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0601 | critic_loss=0.0324 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0162 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1494 | ema=0.2368 | best_ema=0.2368 | no_improve=0
   🔬 Alpha Diversity: mean=0.90 | std=0.41 | range=[0.62, 2.76] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.80 | NEE=0.79 | AMZN=0.79  BOT: JPM=0.77 | CAT=0.76 | NVDA=0.73
   🧭 Regime Start Dist (train resets): high_vol=28 (41.2%), low_vol=22 (32.4%), medium_vol=18 (26.5%)
[CYCLE] Update 51/348 | Step 51,408/500,000 | Episode 68 | Time: 3793.4s
   📊 Metrics: Return=+31.03% | Sharpe=0.497 | DD=20.98% | Turnover=37.64%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0568 | critic_loss=0.0470 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0235 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4969 | ema=0.2628 | best_ema=0.2628 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2841
[CYCLE] Update 52/348 | Step 52,416/500,000 | Episode 68 | Time: 3865.9s
   📊 Metrics: Return=+20.54% | Sharpe=1.413 | DD=8.59% | Turnover=38.31%
   🎚️ Intra-Step TAPE: potential=0.6860 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0572 | critic_loss=0.0322 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0161 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4132 | ema=0.3779 | best_ema=0.3779 | no_improve=0
   🔬 Alpha Diversity: mean=0.83 | std=0.08 | range=[0.67, 1.28] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=0.83 | NEE=0.82 | GLD=0.82  BOT: JPM=0.80 | PG=0.78 | NVDA=0.78
   🧭 Regime Start Dist (train resets): high_vol=31 (43.1%), low_vol=23 (31.9%), medium_vol=18 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 52 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 53/348 | Step 53,424/500,000 | Episode 68 | Time: 3940.1s
   📊 Metrics: Return=+34.36% | Sharpe=1.257 | DD=8.59% | Turnover=38.67%
   🎚️ Intra-Step TAPE: potential=0.6012 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0587 | critic_loss=0.0351 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0176 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2570 | ema=0.4658 | best_ema=0.4658 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00069_shp1p217_actor.weights.h5 (Sharpe=1.217, MDD=8.59%)
[CYCLE] Update 54/348 | Step 54,432/500,000 | Episode 72 | Time: 4014.0s
   📊 Metrics: Return=+14.29% | Sharpe=0.224 | DD=26.45% | Turnover=37.99%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0576 | critic_loss=0.0906 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0453 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2243 | ema=0.4416 | best_ema=0.4416 | no_improve=0
   🔬 Alpha Diversity: mean=1.02 | std=0.12 | range=[0.53, 1.20] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.08 | NEE=1.07 | MSFT=1.07  BOT: XOM=1.03 | NVDA=1.02 | PG=1.01
   🧭 Regime Start Dist (train resets): high_vol=32 (42.1%), low_vol=26 (34.2%), medium_vol=18 (23.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 54 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2336
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00949) | SPY bonus=0.015 (SPY ret=-0.00949)
[CYCLE] Update 55/348 | Step 55,440/500,000 | Episode 72 | Time: 4087.8s
   📊 Metrics: Return=+9.01% | Sharpe=0.620 | DD=8.43% | Turnover=36.35%
   🎚️ Intra-Step TAPE: potential=0.5898 | delta_reward=+0.0025
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0572 | critic_loss=0.0318 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0159 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6204 | ema=0.4595 | best_ema=0.4595 | no_improve=0
[CYCLE] Update 56/348 | Step 56,448/500,000 | Episode 72 | Time: 4160.7s
   📊 Metrics: Return=-0.27% | Sharpe=-0.078 | DD=21.01% | Turnover=35.18%
   🎚️ Intra-Step TAPE: potential=0.2384 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0596 | critic_loss=0.0293 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0147 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0777 | ema=0.4058 | best_ema=0.4058 | no_improve=0
   🔬 Alpha Diversity: mean=1.30 | std=0.22 | range=[0.62, 1.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.41 | JNJ=1.40 | XOM=1.40  BOT: JPM=1.34 | PG=1.31 | NVDA=1.23
   🧭 Regime Start Dist (train resets): high_vol=32 (42.1%), low_vol=26 (34.2%), medium_vol=18 (23.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 56 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00076_shp1p220_actor.weights.h5 (Sharpe=1.220, MDD=10.21%)
[CYCLE] Update 57/348 | Step 57,456/500,000 | Episode 76 | Time: 4233.4s
   📊 Metrics: Return=+63.29% | Sharpe=1.220 | DD=10.21% | Turnover=33.75%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0598 | critic_loss=0.0468 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0234 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2200 | ema=0.4872 | best_ema=0.4872 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5533
[CYCLE] Update 58/348 | Step 58,464/500,000 | Episode 76 | Time: 4305.8s
   📊 Metrics: Return=+26.42% | Sharpe=2.569 | DD=2.48% | Turnover=28.80%
   🎚️ Intra-Step TAPE: potential=0.7235 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0558 | critic_loss=0.0198 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0099 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.5692 | ema=0.6954 | best_ema=0.6954 | no_improve=0
   🔬 Alpha Diversity: mean=1.63 | std=0.30 | range=[0.64, 2.07] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.78 | MSFT=1.77 | NEE=1.76  BOT: GLD=1.70 | PG=1.65 | NVDA=1.63
   🧭 Regime Start Dist (train resets): high_vol=32 (40.0%), low_vol=29 (36.2%), medium_vol=19 (23.8%)
[CYCLE] Update 59/348 | Step 59,472/500,000 | Episode 76 | Time: 4379.7s
   📊 Metrics: Return=+29.30% | Sharpe=1.008 | DD=9.83% | Turnover=29.20%
   🎚️ Intra-Step TAPE: potential=0.2214 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0565 | critic_loss=0.0261 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0131 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0077 | ema=0.7266 | best_ema=0.7266 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00077_shp0p874_actor.weights.h5 (Sharpe=0.874, MDD=17.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00078_shp0p670_actor.weights.h5 (Sharpe=0.670, MDD=25.74%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 4453.3s
   📊 Metrics: Return=+33.34% | Sharpe=0.492 | DD=27.16% | Turnover=30.07%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0557 | critic_loss=0.0291 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0145 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4924 | ema=0.7032 | best_ema=0.7032 | no_improve=0
   🔬 Alpha Diversity: mean=1.36 | std=0.15 | range=[0.70, 1.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.44 | JNJ=1.43 | GLD=1.42  BOT: MSFT=1.38 | AMZN=1.38 | NVDA=1.34
   🧭 Regime Start Dist (train resets): high_vol=34 (40.5%), low_vol=30 (35.7%), medium_vol=20 (23.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 60 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.003) | TAPE=0.2671
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00038) | SPY bonus=0.018 (SPY ret=-0.00644)
[CYCLE] Update 61/348 | Step 61,488/500,000 | Episode 80 | Time: 4528.0s
   📊 Metrics: Return=+11.71% | Sharpe=0.806 | DD=9.41% | Turnover=34.04%
   🎚️ Intra-Step TAPE: potential=0.2344 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0546 | critic_loss=0.0238 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0119 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8059 | ema=0.7135 | best_ema=0.7135 | no_improve=0
[CYCLE] Update 62/348 | Step 62,496/500,000 | Episode 80 | Time: 4602.1s
   📊 Metrics: Return=+39.63% | Sharpe=1.503 | DD=9.41% | Turnover=35.21%
   🎚️ Intra-Step TAPE: potential=0.7491 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0558 | critic_loss=0.0324 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0162 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5028 | ema=0.7924 | best_ema=0.7924 | no_improve=0
   🔬 Alpha Diversity: mean=0.98 | std=0.08 | range=[0.81, 1.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.00 | CAT=0.97 | GLD=0.97  BOT: JNJ=0.95 | JPM=0.95 | XOM=0.92
   🧭 Regime Start Dist (train resets): high_vol=34 (40.5%), low_vol=30 (35.7%), medium_vol=20 (23.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 62 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00081_shp0p923_actor.weights.h5 (Sharpe=0.923, MDD=11.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00083_shp0p798_actor.weights.h5 (Sharpe=0.798, MDD=26.29%)
[CYCLE] Update 63/348 | Step 63,504/500,000 | Episode 84 | Time: 4676.0s
   📊 Metrics: Return=+39.86% | Sharpe=0.574 | DD=24.45% | Turnover=36.08%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0561 | critic_loss=0.0432 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0216 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5736 | ema=0.7705 | best_ema=0.7705 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2897
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00397) | SPY bonus=0.005 (SPY ret=-0.00540)
[CYCLE] Update 64/348 | Step 64,512/500,000 | Episode 84 | Time: 4749.5s
   📊 Metrics: Return=-1.69% | Sharpe=-0.171 | DD=17.45% | Turnover=34.42%
   🎚️ Intra-Step TAPE: potential=0.2352 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0538 | critic_loss=0.0271 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0135 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1708 | ema=0.6764 | best_ema=0.6764 | no_improve=0
   🔬 Alpha Diversity: mean=1.25 | std=0.08 | range=[0.97, 1.49] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.31 | AMZN=1.30 | JPM=1.27  BOT: PG=1.25 | XOM=1.22 | JNJ=1.21
   🧭 Regime Start Dist (train resets): high_vol=34 (38.6%), low_vol=33 (37.5%), medium_vol=21 (23.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 64 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 65/348 | Step 65,520/500,000 | Episode 84 | Time: 4822.0s
   📊 Metrics: Return=+18.21% | Sharpe=0.397 | DD=25.78% | Turnover=33.79%
   🎚️ Intra-Step TAPE: potential=0.7162 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0607 | critic_loss=0.0300 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0150 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3972 | ema=0.6485 | best_ema=0.6485 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00087_shp0p700_actor.weights.h5 (Sharpe=0.700, MDD=18.50%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp1p151_actor.weights.h5 (Sharpe=1.151, MDD=9.84%)
[CYCLE] Update 66/348 | Step 66,528/500,000 | Episode 88 | Time: 4894.8s
   📊 Metrics: Return=+58.22% | Sharpe=1.151 | DD=9.84% | Turnover=33.35%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0520 | critic_loss=0.0324 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0162 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1506 | ema=0.6987 | best_ema=0.6987 | no_improve=0
   🔬 Alpha Diversity: mean=1.17 | std=0.12 | range=[0.73, 1.37] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.25 | CAT=1.22 | GLD=1.22  BOT: JNJ=1.19 | XOM=1.17 | NVDA=1.16
   🧭 Regime Start Dist (train resets): high_vol=36 (39.1%), low_vol=35 (38.0%), medium_vol=21 (22.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 66 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5362
[CYCLE] Update 67/348 | Step 67,536/500,000 | Episode 88 | Time: 4967.9s
   📊 Metrics: Return=+16.41% | Sharpe=1.132 | DD=9.58% | Turnover=35.53%
   🎚️ Intra-Step TAPE: potential=0.6364 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0564 | critic_loss=0.0234 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0117 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1322 | ema=0.7420 | best_ema=0.7420 | no_improve=0
[CYCLE] Update 68/348 | Step 68,544/500,000 | Episode 88 | Time: 5042.1s
   📊 Metrics: Return=+37.54% | Sharpe=1.385 | DD=9.58% | Turnover=34.18%
   🎚️ Intra-Step TAPE: potential=0.7535 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0537 | critic_loss=0.0340 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0170 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3850 | ema=0.8063 | best_ema=0.8063 | no_improve=0
   🔬 Alpha Diversity: mean=1.51 | std=0.25 | range=[0.62, 1.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.65 | JNJ=1.63 | CAT=1.62  BOT: PG=1.56 | XOM=1.55 | NVDA=1.50
   🧭 Regime Start Dist (train resets): high_vol=36 (39.1%), low_vol=35 (38.0%), medium_vol=21 (22.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 68 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp0p832_actor.weights.h5 (Sharpe=0.832, MDD=11.80%)
[CYCLE] Update 69/348 | Step 69,552/500,000 | Episode 92 | Time: 5116.4s
   📊 Metrics: Return=+24.79% | Sharpe=0.516 | DD=16.15% | Turnover=32.04%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0556 | critic_loss=0.0338 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0169 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5163 | ema=0.7773 | best_ema=0.7773 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3081
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00611) | SPY bonus=0.010 (SPY ret=0.00231)
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 5190.9s
   📊 Metrics: Return=+9.80% | Sharpe=0.585 | DD=9.89% | Turnover=29.57%
   🎚️ Intra-Step TAPE: potential=0.7137 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0577 | critic_loss=0.0286 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0143 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5847 | ema=0.7581 | best_ema=0.7581 | no_improve=0
   🔬 Alpha Diversity: mean=1.68 | std=0.21 | range=[0.90, 2.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.80 | JNJ=1.80 | JPM=1.77  BOT: XOM=1.73 | MSFT=1.72 | NVDA=1.67
   🧭 Regime Start Dist (train resets): high_vol=37 (38.5%), low_vol=36 (37.5%), medium_vol=23 (24.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 70 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 71/348 | Step 71,568/500,000 | Episode 92 | Time: 5265.1s
   📊 Metrics: Return=+23.56% | Sharpe=0.773 | DD=9.89% | Turnover=30.10%
   🎚️ Intra-Step TAPE: potential=0.5588 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0537 | critic_loss=0.0527 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0264 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7729 | ema=0.7596 | best_ema=0.7596 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00093_shp0p748_actor.weights.h5 (Sharpe=0.748, MDD=9.89%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00094_shp0p957_actor.weights.h5 (Sharpe=0.957, MDD=10.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00095_shp1p094_actor.weights.h5 (Sharpe=1.094, MDD=10.64%)
[CYCLE] Update 72/348 | Step 72,576/500,000 | Episode 96 | Time: 5339.5s
   📊 Metrics: Return=+27.26% | Sharpe=0.567 | DD=12.44% | Turnover=31.02%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0570 | critic_loss=0.0446 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0223 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5666 | ema=0.7403 | best_ema=0.7403 | no_improve=0
   🔬 Alpha Diversity: mean=1.22 | std=0.06 | range=[1.06, 1.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.24 | XOM=1.24 | AMZN=1.23  BOT: GLD=1.20 | JPM=1.19 | NVDA=1.19
   🧭 Regime Start Dist (train resets): high_vol=39 (39.0%), low_vol=37 (37.0%), medium_vol=24 (24.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 72 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3264
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00996) | SPY bonus=0.023 (SPY ret=0.00425)
[CYCLE] Update 73/348 | Step 73,584/500,000 | Episode 96 | Time: 5413.9s
   📊 Metrics: Return=+18.91% | Sharpe=1.706 | DD=4.24% | Turnover=35.19%
   🎚️ Intra-Step TAPE: potential=0.6403 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0573 | critic_loss=0.0276 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7061 | ema=0.8368 | best_ema=0.8368 | no_improve=0
[CYCLE] Update 74/348 | Step 74,592/500,000 | Episode 96 | Time: 5488.0s
   📊 Metrics: Return=+40.81% | Sharpe=1.643 | DD=8.84% | Turnover=35.48%
   🎚️ Intra-Step TAPE: potential=0.2553 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0561 | critic_loss=0.0243 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0121 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6426 | ema=0.9174 | best_ema=0.9174 | no_improve=0
   🔬 Alpha Diversity: mean=1.15 | std=0.08 | range=[0.97, 1.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.17 | XOM=1.16 | MSFT=1.15  BOT: JPM=1.11 | GLD=1.10 | NVDA=1.08
   🧭 Regime Start Dist (train resets): high_vol=39 (39.0%), low_vol=37 (37.0%), medium_vol=24 (24.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 74 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00097_shp0p934_actor.weights.h5 (Sharpe=0.934, MDD=19.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00098_shp1p000_actor.weights.h5 (Sharpe=1.000, MDD=10.05%)
[CYCLE] Update 75/348 | Step 75,600/500,000 | Episode 100 | Time: 5563.1s
   📊 Metrics: Return=+26.12% | Sharpe=0.399 | DD=23.81% | Turnover=34.41%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0546 | critic_loss=0.0293 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0146 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3993 | ema=0.8656 | best_ema=0.8656 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2559
[CYCLE] Update 76/348 | Step 76,608/500,000 | Episode 100 | Time: 5638.0s
   📊 Metrics: Return=+25.47% | Sharpe=2.069 | DD=5.46% | Turnover=33.10%
   🎚️ Intra-Step TAPE: potential=0.7496 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0501 | critic_loss=0.0178 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0089 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.0694 | ema=0.9860 | best_ema=0.9860 | no_improve=0
   🔬 Alpha Diversity: mean=1.32 | std=0.08 | range=[0.98, 1.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.38 | PG=1.35 | XOM=1.35  BOT: JPM=1.32 | GLD=1.31 | NVDA=1.30
   🧭 Regime Start Dist (train resets): high_vol=42 (40.4%), low_vol=38 (36.5%), medium_vol=24 (23.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 76 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 77/348 | Step 77,616/500,000 | Episode 100 | Time: 5712.6s
   📊 Metrics: Return=+59.31% | Sharpe=2.426 | DD=5.46% | Turnover=33.10%
   🎚️ Intra-Step TAPE: potential=0.7227 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0572 | critic_loss=0.0190 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4256 | ema=1.1299 | best_ema=1.1299 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00101_shp0p895_actor.weights.h5 (Sharpe=0.895, MDD=18.26%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00103_shp1p056_actor.weights.h5 (Sharpe=1.056, MDD=18.75%)
[CYCLE] Update 78/348 | Step 78,624/500,000 | Episode 104 | Time: 5787.2s
   📊 Metrics: Return=+27.59% | Sharpe=0.567 | DD=19.12% | Turnover=33.74%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0553 | critic_loss=0.0279 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0140 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5673 | ema=1.0737 | best_ema=1.0737 | no_improve=0
   🔬 Alpha Diversity: mean=1.16 | std=0.07 | range=[0.88, 1.38] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.19 | CAT=1.17 | XOM=1.16  BOT: GLD=1.14 | NVDA=1.13 | JPM=1.13
   🧭 Regime Start Dist (train resets): high_vol=44 (40.7%), low_vol=39 (36.1%), medium_vol=25 (23.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 78 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3070
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00276) | SPY bonus=0.001 (SPY ret=0.00264)
[CYCLE] Update 79/348 | Step 79,632/500,000 | Episode 104 | Time: 5862.6s
   📊 Metrics: Return=-4.05% | Sharpe=-0.546 | DD=8.77% | Turnover=36.10%
   🎚️ Intra-Step TAPE: potential=0.2745 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0508 | critic_loss=0.0165 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5459 | ema=0.9117 | best_ema=0.9117 | no_improve=0
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 5937.7s
   📊 Metrics: Return=+13.22% | Sharpe=0.411 | DD=14.03% | Turnover=35.40%
   🎚️ Intra-Step TAPE: potential=0.7442 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0576 | critic_loss=0.0310 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0155 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4112 | ema=0.8617 | best_ema=0.8617 | no_improve=0
   🔬 Alpha Diversity: mean=1.34 | std=0.21 | range=[1.10, 2.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.32 | XOM=1.31 | PG=1.31  BOT: JNJ=1.27 | GLD=1.25 | NVDA=1.22
   🧭 Regime Start Dist (train resets): high_vol=44 (40.7%), low_vol=39 (36.1%), medium_vol=25 (23.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 80 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00105_shp0p676_actor.weights.h5 (Sharpe=0.676, MDD=14.03%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00106_shp0p937_actor.weights.h5 (Sharpe=0.937, MDD=9.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00107_shp0p988_actor.weights.h5 (Sharpe=0.988, MDD=10.45%)
[CYCLE] Update 81/348 | Step 81,648/500,000 | Episode 108 | Time: 6012.5s
   📊 Metrics: Return=+12.59% | Sharpe=0.247 | DD=9.05% | Turnover=34.80%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0538 | critic_loss=0.0515 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0257 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2467 | ema=0.8002 | best_ema=0.8002 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2654
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00120) | SPY bonus=0.006 (SPY ret=-0.00395)
[CYCLE] Update 82/348 | Step 82,656/500,000 | Episode 108 | Time: 6087.3s
   📊 Metrics: Return=-0.41% | Sharpe=-0.104 | DD=16.10% | Turnover=34.17%
   🎚️ Intra-Step TAPE: potential=0.2608 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0558 | critic_loss=0.0301 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0150 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1043 | ema=0.7097 | best_ema=0.7097 | no_improve=0
   🔬 Alpha Diversity: mean=1.21 | std=0.21 | range=[0.97, 2.24] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.19 | XOM=1.18 | MSFT=1.17  BOT: JPM=1.13 | GLD=1.12 | NVDA=1.09
   🧭 Regime Start Dist (train resets): high_vol=45 (40.2%), low_vol=39 (34.8%), medium_vol=28 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 82 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 83/348 | Step 83,664/500,000 | Episode 108 | Time: 6161.8s
   📊 Metrics: Return=-0.27% | Sharpe=0.006 | DD=27.93% | Turnover=34.63%
   🎚️ Intra-Step TAPE: potential=0.2070 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0534 | critic_loss=0.0299 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0150 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0062 | ema=0.6394 | best_ema=0.6394 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00110_shp0p762_actor.weights.h5 (Sharpe=0.762, MDD=17.34%)
[CYCLE] Update 84/348 | Step 84,672/500,000 | Episode 112 | Time: 6236.7s
   📊 Metrics: Return=+35.89% | Sharpe=0.540 | DD=23.98% | Turnover=34.12%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0586 | critic_loss=0.0275 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5397 | ema=0.6294 | best_ema=0.6294 | no_improve=0
   🔬 Alpha Diversity: mean=1.26 | std=0.07 | range=[0.77, 1.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.28 | GLD=1.27 | NEE=1.27  BOT: JPM=1.25 | MSFT=1.25 | NVDA=1.21
   🧭 Regime Start Dist (train resets): high_vol=48 (41.4%), low_vol=40 (34.5%), medium_vol=28 (24.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 84 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2823
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00106) | SPY bonus=0.007 (SPY ret=-0.00210)
[CYCLE] Update 85/348 | Step 85,680/500,000 | Episode 112 | Time: 6311.6s
   📊 Metrics: Return=+28.73% | Sharpe=1.760 | DD=8.78% | Turnover=33.03%
   🎚️ Intra-Step TAPE: potential=0.5646 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0516 | critic_loss=0.0336 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0168 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7604 | ema=0.7425 | best_ema=0.7425 | no_improve=0
[CYCLE] Update 86/348 | Step 86,688/500,000 | Episode 112 | Time: 6386.2s
   📊 Metrics: Return=+53.34% | Sharpe=1.718 | DD=8.78% | Turnover=33.22%
   🎚️ Intra-Step TAPE: potential=0.5849 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0531 | critic_loss=0.0196 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0098 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7179 | ema=0.8400 | best_ema=0.8400 | no_improve=0
   🔬 Alpha Diversity: mean=1.18 | std=0.09 | range=[0.73, 1.36] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.23 | XOM=1.23 | GLD=1.22  BOT: MSFT=1.19 | NVDA=1.17 | NEE=1.17
   🧭 Regime Start Dist (train resets): high_vol=48 (41.4%), low_vol=40 (34.5%), medium_vol=28 (24.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 86 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00113_shp1p298_actor.weights.h5 (Sharpe=1.298, MDD=10.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00114_shp0p776_actor.weights.h5 (Sharpe=0.776, MDD=18.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00116_shp0p986_actor.weights.h5 (Sharpe=0.986, MDD=12.63%)
[CYCLE] Update 87/348 | Step 87,696/500,000 | Episode 116 | Time: 6460.5s
   📊 Metrics: Return=+45.81% | Sharpe=0.986 | DD=12.63% | Turnover=33.40%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0508 | critic_loss=0.0486 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0243 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9856 | ema=0.8546 | best_ema=0.8546 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5181
[CYCLE] Update 88/348 | Step 88,704/500,000 | Episode 116 | Time: 6535.7s
   📊 Metrics: Return=+6.34% | Sharpe=0.462 | DD=5.93% | Turnover=34.85%
   🎚️ Intra-Step TAPE: potential=0.2354 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0549 | critic_loss=0.0181 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0091 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4623 | ema=0.8154 | best_ema=0.8154 | no_improve=0
   🔬 Alpha Diversity: mean=1.18 | std=0.12 | range=[1.01, 1.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.18 | GLD=1.18 | PG=1.17  BOT: CAT=1.12 | JNJ=1.12 | NVDA=1.10
   🧭 Regime Start Dist (train resets): high_vol=48 (40.0%), low_vol=41 (34.2%), medium_vol=31 (25.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 88 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 89/348 | Step 89,712/500,000 | Episode 116 | Time: 6610.0s
   📊 Metrics: Return=+6.03% | Sharpe=0.144 | DD=9.47% | Turnover=34.99%
   🎚️ Intra-Step TAPE: potential=0.2418 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0551 | critic_loss=0.0442 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0221 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1439 | ema=0.7482 | best_ema=0.7482 | no_improve=0

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 6683.6s
   📊 Metrics: Return=+9.25% | Sharpe=0.144 | DD=15.04% | Turnover=35.21%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0484 | critic_loss=0.0485 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0243 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1436 | ema=0.6878 | best_ema=0.6878 | no_improve=0
   🔬 Alpha Diversity: mean=1.06 | std=0.04 | range=[0.81, 1.18] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.08 | PG=1.07 | XOM=1.07  BOT: NEE=1.04 | MSFT=1.03 | NVDA=1.01
   🧭 Regime Start Dist (train resets): high_vol=50 (40.3%), low_vol=43 (34.7%), medium_vol=31 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 90 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2513
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00630) | SPY bonus=0.008 (SPY ret=0.00455)

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps
[CYCLE] Update 91/348 | Step 91,728/500,000 | Episode 120 | Time: 6756.6s
   📊 Metrics: Return=-2.50% | Sharpe=-0.350 | DD=8.28% | Turnover=36.03%
   🎚️ Intra-Step TAPE: potential=0.2485 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0512 | critic_loss=0.0250 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3500 | ema=0.5840 | best_ema=0.5840 | no_improve=0

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps
[CYCLE] Update 92/348 | Step 92,736/500,000 | Episode 120 | Time: 6828.5s
   📊 Metrics: Return=+12.00% | Sharpe=0.358 | DD=11.42% | Turnover=35.81%
   🎚️ Intra-Step TAPE: potential=0.7341 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0558 | critic_loss=0.0236 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0118 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3577 | ema=0.5614 | best_ema=0.5614 | no_improve=0
   🔬 Alpha Diversity: mean=1.09 | std=0.14 | range=[0.96, 1.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.07 | NEE=1.06 | XOM=1.05  BOT: NVDA=1.04 | JPM=1.03 | JNJ=1.02
   🧭 Regime Start Dist (train resets): high_vol=50 (40.3%), low_vol=43 (34.7%), medium_vol=31 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 92 updates. TCN may not be learning asset discrimination.

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps
[CYCLE] Update 93/348 | Step 93,744/500,000 | Episode 120 | Time: 6901.8s
   📊 Metrics: Return=+33.20% | Sharpe=0.715 | DD=11.42% | Turnover=36.01%
   🎚️ Intra-Step TAPE: potential=0.7306 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0511 | critic_loss=0.0246 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0123 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7149 | ema=0.5767 | best_ema=0.5767 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00121_shp0p798_actor.weights.h5 (Sharpe=0.798, MDD=11.42%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00124_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=18.60%)

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps
[CYCLE] Update 94/348 | Step 94,752/500,000 | Episode 124 | Time: 6974.0s
   📊 Metrics: Return=+43.47% | Sharpe=0.806 | DD=18.60% | Turnover=36.12%
   🎚️ Intra-Step TAPE: potential=0.7201 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0548 | critic_loss=0.0250 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8058 | ema=0.5996 | best_ema=0.5996 | no_improve=0
   🔬 Alpha Diversity: mean=0.96 | std=0.05 | range=[0.75, 1.17] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=0.97 | CAT=0.96 | AMZN=0.96  BOT: MSFT=0.95 | JPM=0.94 | NVDA=0.92
   🧭 Regime Start Dist (train resets): high_vol=51 (39.8%), low_vol=45 (35.2%), medium_vol=32 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 94 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.20% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3938
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.01192) | SPY bonus=0.006 (SPY ret=0.01047)

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps
[CYCLE] Update 95/348 | Step 95,760/500,000 | Episode 124 | Time: 7045.0s
   📊 Metrics: Return=+44.46% | Sharpe=2.292 | DD=3.88% | Turnover=37.12%
   🎚️ Intra-Step TAPE: potential=0.5577 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0493 | critic_loss=0.0196 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0098 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.2917 | ema=0.7688 | best_ema=0.7688 | no_improve=0

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps
[CYCLE] Update 96/348 | Step 96,768/500,000 | Episode 124 | Time: 7115.9s
   📊 Metrics: Return=+63.72% | Sharpe=1.686 | DD=7.75% | Turnover=36.67%
   🎚️ Intra-Step TAPE: potential=0.6432 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0552 | critic_loss=0.0258 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0129 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6864 | ema=0.8606 | best_ema=0.8606 | no_improve=0
   🔬 Alpha Diversity: mean=1.12 | std=0.09 | range=[0.57, 1.28] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.18 | JNJ=1.15 | AMZN=1.15  BOT: JPM=1.14 | GLD=1.14 | NVDA=1.11
   🧭 Regime Start Dist (train resets): high_vol=51 (39.8%), low_vol=45 (35.2%), medium_vol=32 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 96 updates. TCN may not be learning asset discrimination.

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps
[CYCLE] Update 97/348 | Step 97,776/500,000 | Episode 124 | Time: 7186.8s
   📊 Metrics: Return=+60.84% | Sharpe=0.990 | DD=18.90% | Turnover=36.10%
   🎚️ Intra-Step TAPE: potential=0.2254 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0540 | critic_loss=0.0171 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0085 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9904 | ema=0.8736 | best_ema=0.8736 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00125_shp0p992_actor.weights.h5 (Sharpe=0.992, MDD=18.90%)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps
[CYCLE] Update 98/348 | Step 98,784/500,000 | Episode 128 | Time: 7256.6s
   📊 Metrics: Return=+29.52% | Sharpe=0.481 | DD=11.44% | Turnover=35.44%
   🎚️ Intra-Step TAPE: potential=0.6847 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0510 | critic_loss=0.0249 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0124 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4812 | ema=0.8343 | best_ema=0.8343 | no_improve=0
   🔬 Alpha Diversity: mean=1.01 | std=0.06 | range=[0.89, 1.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.04 | AMZN=1.01 | JNJ=1.00  BOT: PG=0.99 | GLD=0.98 | NVDA=0.95
   🧭 Regime Start Dist (train resets): high_vol=52 (39.4%), low_vol=47 (35.6%), medium_vol=33 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 98 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.16% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3067
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00078) | SPY bonus=0.001 (SPY ret=0.00093)

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps
[CYCLE] Update 99/348 | Step 99,792/500,000 | Episode 128 | Time: 7326.4s
   📊 Metrics: Return=+32.73% | Sharpe=1.331 | DD=9.28% | Turnover=35.89%
   🎚️ Intra-Step TAPE: potential=0.2492 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0509 | critic_loss=0.0230 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0115 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3308 | ema=0.8840 | best_ema=0.8840 | no_improve=0

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.15

🎛️ EXECUTION BETA UPDATE at 100,800 steps:
   action_execution_beta: 0.650 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 7396.0s
   📊 Metrics: Return=+18.20% | Sharpe=0.381 | DD=22.52% | Turnover=36.71%
   🎚️ Intra-Step TAPE: potential=0.2188 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0551 | critic_loss=0.0249 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0124 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3807 | ema=0.8336 | best_ema=0.8336 | no_improve=0
   🔬 Alpha Diversity: mean=0.88 | std=0.05 | range=[0.73, 1.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=0.90 | AMZN=0.89 | JNJ=0.88  BOT: CAT=0.87 | PG=0.87 | NVDA=0.83
   🧭 Regime Start Dist (train resets): high_vol=52 (39.4%), low_vol=47 (35.6%), medium_vol=33 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 100 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 101/348 | Step 101,808/500,000 | Episode 128 | Time: 7466.8s
   📊 Metrics: Return=+30.52% | Sharpe=0.372 | DD=31.35% | Turnover=40.78%
   🎚️ Intra-Step TAPE: potential=0.7417 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0515 | critic_loss=0.0205 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0102 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3724 | ema=0.7875 | best_ema=0.8336 | no_improve=1
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00132_shp0p987_actor.weights.h5 (Sharpe=0.987, MDD=17.04%)
[CYCLE] Update 102/348 | Step 102,816/500,000 | Episode 132 | Time: 7540.1s
   📊 Metrics: Return=+66.26% | Sharpe=0.987 | DD=17.04% | Turnover=41.54%
   🎚️ Intra-Step TAPE: potential=0.2255 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0568 | critic_loss=0.0338 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0169 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9872 | ema=0.8075 | best_ema=0.8336 | no_improve=2
   🔬 Alpha Diversity: mean=0.95 | std=0.05 | range=[0.60, 1.11] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=0.97 | NEE=0.97 | AMZN=0.97  BOT: PG=0.94 | MSFT=0.93 | NVDA=0.91
   🧭 Regime Start Dist (train resets): high_vol=53 (39.0%), low_vol=49 (36.0%), medium_vol=34 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 102 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.87% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4940
[CYCLE] Update 103/348 | Step 103,824/500,000 | Episode 132 | Time: 7612.9s
   📊 Metrics: Return=-7.67% | Sharpe=-0.559 | DD=14.06% | Turnover=50.51%
   🎚️ Intra-Step TAPE: potential=0.2338 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0565 | critic_loss=0.0474 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0237 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5593 | ema=0.6708 | best_ema=0.8336 | no_improve=3
[CYCLE] Update 104/348 | Step 104,832/500,000 | Episode 132 | Time: 7684.0s
   📊 Metrics: Return=-1.64% | Sharpe=-0.160 | DD=18.34% | Turnover=50.83%
   🎚️ Intra-Step TAPE: potential=0.4786 | delta_reward=+0.0023
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0550 | critic_loss=0.0504 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0252 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1603 | ema=0.5877 | best_ema=0.8336 | no_improve=4
   🔬 Alpha Diversity: mean=0.99 | std=0.23 | range=[0.79, 1.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=0.94 | JPM=0.94 | NEE=0.93  BOT: CAT=0.89 | MSFT=0.89 | NVDA=0.87
   🧭 Regime Start Dist (train resets): high_vol=53 (39.0%), low_vol=49 (36.0%), medium_vol=34 (25.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 104 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 105/348 | Step 105,840/500,000 | Episode 132 | Time: 7753.5s
   📊 Metrics: Return=+10.50% | Sharpe=0.111 | DD=18.34% | Turnover=50.60%
   🎚️ Intra-Step TAPE: potential=0.6666 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0523 | critic_loss=0.0250 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1108 | ema=0.5400 | best_ema=0.8336 | no_improve=5
[CYCLE] Update 106/348 | Step 106,848/500,000 | Episode 136 | Time: 7825.1s
   📊 Metrics: Return=+15.76% | Sharpe=0.207 | DD=14.04% | Turnover=50.70%
   🎚️ Intra-Step TAPE: potential=0.2373 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0526 | critic_loss=0.0221 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0110 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2073 | ema=0.5067 | best_ema=0.8336 | no_improve=6
   🔬 Alpha Diversity: mean=1.14 | std=0.40 | range=[0.89, 2.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.05 | NEE=1.04 | JNJ=1.04  BOT: CAT=0.99 | MSFT=0.98 | NVDA=0.97
   🧭 Regime Start Dist (train resets): high_vol=55 (39.3%), low_vol=49 (35.0%), medium_vol=36 (25.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.55% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2519
[CYCLE] Update 107/348 | Step 107,856/500,000 | Episode 136 | Time: 7898.7s
   📊 Metrics: Return=+22.57% | Sharpe=0.835 | DD=11.62% | Turnover=49.12%
   🎚️ Intra-Step TAPE: potential=0.7058 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0515 | critic_loss=0.0311 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0156 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8347 | ema=0.5395 | best_ema=0.8336 | no_improve=7
[CYCLE] Update 108/348 | Step 108,864/500,000 | Episode 136 | Time: 7971.2s
   📊 Metrics: Return=+39.56% | Sharpe=0.933 | DD=11.62% | Turnover=48.75%
   🎚️ Intra-Step TAPE: potential=0.2217 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0541 | critic_loss=0.0237 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0118 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9334 | ema=0.5789 | best_ema=0.8336 | no_improve=8
   🔬 Alpha Diversity: mean=1.10 | std=0.04 | range=[0.97, 1.23] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.13 | AMZN=1.12 | JPM=1.12  BOT: MSFT=1.07 | CAT=1.07 | NVDA=1.07
   🧭 Regime Start Dist (train resets): high_vol=55 (39.3%), low_vol=49 (35.0%), medium_vol=36 (25.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 108 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 109/348 | Step 109,872/500,000 | Episode 136 | Time: 8043.3s
   📊 Metrics: Return=+21.78% | Sharpe=0.314 | DD=25.25% | Turnover=49.05%
   🎚️ Intra-Step TAPE: potential=0.2258 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0512 | critic_loss=0.0216 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3140 | ema=0.5524 | best_ema=0.8336 | no_improve=9
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 8116.2s
   📊 Metrics: Return=-11.06% | Sharpe=-0.370 | DD=21.31% | Turnover=48.75%
   🎚️ Intra-Step TAPE: potential=0.2140 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0520 | critic_loss=0.0310 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0155 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3698 | ema=0.4602 | best_ema=0.8336 | no_improve=10
   🔬 Alpha Diversity: mean=1.00 | std=0.05 | range=[0.82, 1.29] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.02 | AMZN=1.01 | XOM=1.00  BOT: CAT=0.97 | MSFT=0.97 | NVDA=0.97
   🧭 Regime Start Dist (train resets): high_vol=55 (38.2%), low_vol=51 (35.4%), medium_vol=38 (26.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 110 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 8.12% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2200
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.01480) | SPY bonus=0.000 (SPY ret=0.01243)