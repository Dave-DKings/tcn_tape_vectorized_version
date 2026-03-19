[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 300000
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
      ↳ Schedule: 0.10@0 => 0.15@60,000 => 0.20@140,000 => 0.25@220,000 => 0.30@280,000
   ⚙️  Component 4: Execution Inertia (beta=0.50 -> 0.65 => 0.80 => 1.00, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.50@0 => 0.65@60,000 => 0.80@140,000 => 1.00@220,000
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
   [TOOL] Actor LR schedule: 0.000030@0 => 0.000020@100,000 => 0.000010@220,000
   [TOOL] Critic LR schedule: 0.000150@0 => 0.000120@100,000 => 0.000100@220,000
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
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@100,000 => 0.9980@220,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@100,000 => 0.9700@220,000
   🎯 Entropy coef schedule: 0.0030@0 => 0.0030@100,000 => 0.0025@200,000 => 0.0015@280,000
   🧪 Aux-return coef schedule: 0.3500@0 => 0.3000@100,000 => 0.2500@220,000
   🌡️ Temperature schedule: 1.0000@0 => 0.9000@100,000 => 0.8000@220,000
   📐 PPO rollout schedule: 1008@0 => 1512@100,000 => 2016@220,000
   🧺 PPO batch-size schedule: 252@0 => 336@100,000 => 504@220,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_150216_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_150216_step_diagnostics.csv

🎯 Starting THREE-COMPONENT TAPE v3 training (with curriculum)...
   Total timesteps: 300,000
   Timesteps per update: scheduled
      0+ steps: timesteps_per_update=1008
      100,000+ steps: timesteps_per_update=1512
      220,000+ steps: timesteps_per_update=2016
   Number of updates: 219
   PPO batch_size: scheduled
      0+ steps: batch_size=252
      100,000+ steps: batch_size=336
      220,000+ steps: batch_size=504
   PPO gamma schedule: 0.9900@0 => 0.9950@100,000 => 0.9980@220,000
   PPO GAE-λ schedule: 0.9200@0 => 0.9500@100,000 => 0.9700@220,000
   📚 Episode Length Curriculum:
      0+ steps: limit=756
      60,000+ steps: limit=1008
      180,000+ steps: limit=1500
      260,000+ steps: limit=full
      ↳ smooth ramp: enabled (overlap=10,000 steps)
   📚 Turnover Scalar Curriculum:
      0+ steps: scalar=0.10
      60,000+ steps: scalar=0.15
      140,000+ steps: scalar=0.20
      220,000+ steps: scalar=0.25
      280,000+ steps: scalar=0.30
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.50
      60,000+ steps: beta=0.65
      140,000+ steps: beta=0.80
      220,000+ steps: beta=1.00
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.60, MDD <= 30.0%, skip_on_det_validation=True)
   ⏹️ Training early-stop: enabled (warmup=100,000 steps, patience=25 updates, min_delta=0.010, hard_dd=60.0% x 12)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_150216_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_150216_metadata.json
[CYCLE] Update 1/219 | Step 1,008/300,000 | Episode 0 | Time: 98.4s
   📊 Metrics: Return=+23.31% | Sharpe=2.180 | DD=2.72% | Turnover=25.17%
   🎚️ Intra-Step TAPE: potential=0.7329 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.3062 | critic_loss=0.4407 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2204 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0784 | balance_loss=0.0002 | separation_loss=0.0062 | component_dispersion_loss=0.0096
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1795 | ema=2.1795 | best_ema=2.1795 | no_improve=0
[CYCLE] Update 2/219 | Step 2,016/300,000 | Episode 0 | Time: 185.8s
   📊 Metrics: Return=+44.58% | Sharpe=1.640 | DD=7.66% | Turnover=25.20%
   🎚️ Intra-Step TAPE: potential=0.3023 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2073 | critic_loss=0.2850 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1425 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0895 | balance_loss=0.0001 | separation_loss=0.0062 | component_dispersion_loss=0.0096
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6401 | ema=2.1256 | best_ema=2.1256 | no_improve=0
   🔬 Alpha Diversity: mean=6.81 | std=0.59 | range=[5.48, 8.87] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=7.45 | NVDA=7.17 | AMZN=6.88  BOT: XOM=6.53 | JPM=6.43 | GLD=6.21
   🎛️ Mixture Usage: C0=39.2% | C1=27.1% | C2=33.7%
   🧭 Regime Start Dist (train resets): high_vol=2 (50.0%), low_vol=1 (25.0%), medium_vol=1 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p000_actor.weights.h5 (Sharpe=1.000, MDD=17.02%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00003_shp0p719_actor.weights.h5 (Sharpe=0.719, MDD=12.27%)
[CYCLE] Update 3/219 | Step 3,024/300,000 | Episode 4 | Time: 273.8s
   📊 Metrics: Return=+22.67% | Sharpe=0.510 | DD=10.88% | Turnover=24.36%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1652 | critic_loss=0.2747 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1373 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0882 | balance_loss=0.0001 | separation_loss=0.0064 | component_dispersion_loss=0.0097
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5098 | ema=1.9640 | best_ema=1.9640 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.050) | TAPE=0.3180
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01358) | SPY bonus=0.007 (SPY ret=-0.01396)
[CYCLE] Update 4/219 | Step 4,032/300,000 | Episode 4 | Time: 358.8s
   📊 Metrics: Return=+29.34% | Sharpe=2.877 | DD=2.78% | Turnover=24.46%
   🎚️ Intra-Step TAPE: potential=0.7566 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1371 | critic_loss=0.2052 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0751 | balance_loss=0.0003 | separation_loss=0.0066 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.8768 | ema=2.0553 | best_ema=2.0553 | no_improve=0
   🔬 Alpha Diversity: mean=6.11 | std=0.78 | range=[4.43, 9.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.19 | CAT=6.31 | AMZN=6.22  BOT: GLD=5.60 | NEE=5.51 | JPM=5.37
   🎛️ Mixture Usage: C0=33.7% | C1=41.0% | C2=25.3%
   🧭 Regime Start Dist (train resets): high_vol=2 (25.0%), low_vol=4 (50.0%), medium_vol=2 (25.0%)
[CYCLE] Update 5/219 | Step 5,040/300,000 | Episode 4 | Time: 446.0s
   📊 Metrics: Return=+21.24% | Sharpe=0.665 | DD=18.71% | Turnover=26.16%
   🎚️ Intra-Step TAPE: potential=0.2352 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1192 | critic_loss=0.3103 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1552 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0734 | balance_loss=0.0003 | separation_loss=0.0064 | component_dispersion_loss=0.0097
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6655 | ema=1.9163 | best_ema=1.9163 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00005_shp0p917_actor.weights.h5 (Sharpe=0.917, MDD=18.71%)
[CYCLE] Update 6/219 | Step 6,048/300,000 | Episode 8 | Time: 534.1s
   📊 Metrics: Return=+22.94% | Sharpe=0.496 | DD=11.43% | Turnover=25.67%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1125 | critic_loss=0.2629 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1315 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0743 | balance_loss=0.0003 | separation_loss=0.0065 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4957 | ema=1.7743 | best_ema=1.7743 | no_improve=0
   🔬 Alpha Diversity: mean=5.36 | std=0.51 | range=[3.77, 7.16] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.90 | CAT=5.60 | AMZN=5.51  BOT: NEE=4.94 | GLD=4.89 | JPM=4.86
   🎛️ Mixture Usage: C0=36.2% | C1=40.8% | C2=23.0%
   🧭 Regime Start Dist (train resets): high_vol=4 (33.3%), low_vol=4 (33.3%), medium_vol=4 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3092
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00445) | SPY bonus=0.003 (SPY ret=-0.00511)
[CYCLE] Update 7/219 | Step 7,056/300,000 | Episode 8 | Time: 622.3s
   📊 Metrics: Return=+4.83% | Sharpe=0.280 | DD=11.24% | Turnover=27.32%
   🎚️ Intra-Step TAPE: potential=0.2709 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1084 | critic_loss=0.1651 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0826 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0688 | balance_loss=0.0004 | separation_loss=0.0066 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2800 | ema=1.6248 | best_ema=1.6248 | no_improve=0
[CYCLE] Update 8/219 | Step 8,064/300,000 | Episode 8 | Time: 710.4s
   📊 Metrics: Return=+33.89% | Sharpe=1.080 | DD=11.24% | Turnover=27.03%
   🎚️ Intra-Step TAPE: potential=0.4471 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1059 | critic_loss=0.2694 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1347 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0760 | balance_loss=0.0003 | separation_loss=0.0068 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0799 | ema=1.5703 | best_ema=1.5703 | no_improve=0
   🔬 Alpha Diversity: mean=5.56 | std=0.35 | range=[4.61, 6.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=5.90 | NVDA=5.83 | CAT=5.78  BOT: GLD=5.40 | NEE=5.32 | JPM=5.11
   🎛️ Mixture Usage: C0=39.1% | C1=37.5% | C2=23.4%
   🧭 Regime Start Dist (train resets): high_vol=4 (33.3%), low_vol=4 (33.3%), medium_vol=4 (33.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00009_shp1p327_actor.weights.h5 (Sharpe=1.327, MDD=11.24%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00012_shp0p761_actor.weights.h5 (Sharpe=0.761, MDD=19.76%)
[CYCLE] Update 9/219 | Step 9,072/300,000 | Episode 12 | Time: 798.8s
   📊 Metrics: Return=+37.55% | Sharpe=0.761 | DD=19.76% | Turnover=26.54%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1004 | critic_loss=0.2553 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1277 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0740 | balance_loss=0.0003 | separation_loss=0.0069 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7608 | ema=1.4894 | best_ema=1.4894 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3594
[CYCLE] Update 10/219 | Step 10,080/300,000 | Episode 12 | Time: 886.7s
   📊 Metrics: Return=+2.93% | Sharpe=0.135 | DD=11.47% | Turnover=26.47%
   🎚️ Intra-Step TAPE: potential=0.2423 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0975 | critic_loss=0.1745 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0872 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0690 | balance_loss=0.0004 | separation_loss=0.0069 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1348 | ema=1.3539 | best_ema=1.3539 | no_improve=0
   🔬 Alpha Diversity: mean=4.97 | std=0.61 | range=[2.75, 6.34] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=5.38 | JNJ=5.35 | NVDA=5.34  BOT: XOM=4.98 | NEE=4.95 | JPM=4.95
   🎛️ Mixture Usage: C0=41.7% | C1=40.9% | C2=17.5%
   🧭 Regime Start Dist (train resets): high_vol=5 (31.2%), low_vol=4 (25.0%), medium_vol=7 (43.8%)
[CYCLE] Update 11/219 | Step 11,088/300,000 | Episode 12 | Time: 974.4s
   📊 Metrics: Return=+13.68% | Sharpe=0.458 | DD=11.47% | Turnover=27.10%
   🎚️ Intra-Step TAPE: potential=0.6060 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0930 | critic_loss=0.2171 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1085 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0729 | balance_loss=0.0003 | separation_loss=0.0068 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4575 | ema=1.2643 | best_ema=1.2643 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00016_shp1p180_actor.weights.h5 (Sharpe=1.180, MDD=9.56%)
[CYCLE] Update 12/219 | Step 12,096/300,000 | Episode 16 | Time: 1062.0s
   📊 Metrics: Return=+54.16% | Sharpe=1.180 | DD=9.56% | Turnover=27.54%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0932 | critic_loss=0.2824 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1412 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0699 | balance_loss=0.0004 | separation_loss=0.0067 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1801 | ema=1.2559 | best_ema=1.2559 | no_improve=0
   🔬 Alpha Diversity: mean=4.47 | std=0.76 | range=[1.82, 5.24] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.93 | CAT=4.83 | PG=4.80  BOT: NEE=4.64 | MSFT=4.53 | JPM=4.49
   🎛️ Mixture Usage: C0=41.2% | C1=37.4% | C2=21.4%
   🧭 Regime Start Dist (train resets): high_vol=7 (35.0%), low_vol=5 (25.0%), medium_vol=8 (40.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5385
[CYCLE] Update 13/219 | Step 13,104/300,000 | Episode 16 | Time: 1157.3s
   📊 Metrics: Return=+11.71% | Sharpe=0.830 | DD=9.33% | Turnover=29.53%
   🎚️ Intra-Step TAPE: potential=0.2334 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0945 | critic_loss=0.2675 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1337 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0664 | balance_loss=0.0004 | separation_loss=0.0067 | component_dispersion_loss=0.0097
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8298 | ema=1.2133 | best_ema=1.2133 | no_improve=0
[CYCLE] Update 14/219 | Step 14,112/300,000 | Episode 16 | Time: 1251.2s
   📊 Metrics: Return=+44.85% | Sharpe=1.634 | DD=9.33% | Turnover=30.69%
   🎚️ Intra-Step TAPE: potential=0.7542 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0969 | critic_loss=0.2153 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1076 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0697 | balance_loss=0.0004 | separation_loss=0.0067 | component_dispersion_loss=0.0097
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6341 | ema=1.2553 | best_ema=1.2553 | no_improve=0
   🔬 Alpha Diversity: mean=4.32 | std=0.73 | range=[1.28, 5.11] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.73 | CAT=4.64 | NVDA=4.62  BOT: NEE=4.50 | MSFT=4.43 | JPM=4.41
   🎛️ Mixture Usage: C0=39.7% | C1=38.3% | C2=22.0%
   🧭 Regime Start Dist (train resets): high_vol=7 (35.0%), low_vol=5 (25.0%), medium_vol=8 (40.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00017_shp1p057_actor.weights.h5 (Sharpe=1.057, MDD=9.38%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp1p300_actor.weights.h5 (Sharpe=1.300, MDD=9.72%)
[CYCLE] Update 15/219 | Step 15,120/300,000 | Episode 20 | Time: 1332.8s
   📊 Metrics: Return=+60.29% | Sharpe=1.300 | DD=9.72% | Turnover=30.82%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0946 | critic_loss=0.1808 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0904 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0656 | balance_loss=0.0004 | separation_loss=0.0067 | component_dispersion_loss=0.0097
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2999 | ema=1.2598 | best_ema=1.2598 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5644
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00233) | SPY bonus=0.006 (SPY ret=-0.00109)
[CYCLE] Update 16/219 | Step 16,128/300,000 | Episode 20 | Time: 1415.0s
   📊 Metrics: Return=+9.61% | Sharpe=0.801 | DD=6.23% | Turnover=32.59%
   🎚️ Intra-Step TAPE: potential=0.2404 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0899 | critic_loss=0.1563 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0782 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0635 | balance_loss=0.0005 | separation_loss=0.0068 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8011 | ema=1.2139 | best_ema=1.2139 | no_improve=0
   🔬 Alpha Diversity: mean=4.17 | std=0.64 | range=[1.83, 4.95] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=4.50 | JNJ=4.50 | AMZN=4.43  BOT: NEE=4.29 | MSFT=4.28 | JPM=4.24
   🎛️ Mixture Usage: C0=42.5% | C1=37.8% | C2=19.7%
   🧭 Regime Start Dist (train resets): high_vol=8 (33.3%), low_vol=8 (33.3%), medium_vol=8 (33.3%)
[CYCLE] Update 17/219 | Step 17,136/300,000 | Episode 20 | Time: 1497.1s
   📊 Metrics: Return=+9.10% | Sharpe=0.284 | DD=8.00% | Turnover=31.52%
   🎚️ Intra-Step TAPE: potential=0.2415 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0928 | critic_loss=0.2171 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1086 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0687 | balance_loss=0.0004 | separation_loss=0.0069 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2843 | ema=1.1210 | best_ema=1.1210 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00023_shp1p197_actor.weights.h5 (Sharpe=1.197, MDD=14.31%)
[CYCLE] Update 18/219 | Step 18,144/300,000 | Episode 24 | Time: 1580.0s
   📊 Metrics: Return=+24.99% | Sharpe=0.544 | DD=14.10% | Turnover=30.39%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0951 | critic_loss=0.1378 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0689 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0614 | balance_loss=0.0005 | separation_loss=0.0068 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5442 | ema=1.0633 | best_ema=1.0633 | no_improve=0
   🔬 Alpha Diversity: mean=4.32 | std=0.69 | range=[1.62, 5.17] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.67 | CAT=4.64 | PG=4.62  BOT: GLD=4.46 | NEE=4.42 | JPM=4.39
   🎛️ Mixture Usage: C0=41.9% | C1=36.6% | C2=21.5%
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=10 (35.7%), medium_vol=8 (28.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3161
[CYCLE] Update 19/219 | Step 19,152/300,000 | Episode 24 | Time: 1663.4s
   📊 Metrics: Return=+0.39% | Sharpe=-0.054 | DD=10.21% | Turnover=29.09%
   🎚️ Intra-Step TAPE: potential=0.2472 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0903 | critic_loss=0.1280 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0640 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0444 | balance_loss=0.0008 | separation_loss=0.0069 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0544 | ema=0.9515 | best_ema=0.9515 | no_improve=0
[CYCLE] Update 20/219 | Step 20,160/300,000 | Episode 24 | Time: 1745.4s
   📊 Metrics: Return=+34.45% | Sharpe=1.097 | DD=10.21% | Turnover=28.09%
   🎚️ Intra-Step TAPE: potential=0.7489 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0921 | critic_loss=0.1053 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0526 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0502 | balance_loss=0.0007 | separation_loss=0.0071 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0973 | ema=0.9661 | best_ema=0.9661 | no_improve=0
   🔬 Alpha Diversity: mean=4.34 | std=0.88 | range=[1.37, 5.22] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.82 | CAT=4.78 | JNJ=4.72  BOT: GLD=4.52 | NEE=4.44 | JPM=4.42
   🎛️ Mixture Usage: C0=40.1% | C1=40.8% | C2=19.1%
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=10 (35.7%), medium_vol=8 (28.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p535_actor.weights.h5 (Sharpe=1.535, MDD=10.21%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00027_shp1p474_actor.weights.h5 (Sharpe=1.474, MDD=8.44%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00028_shp0p624_actor.weights.h5 (Sharpe=0.624, MDD=14.06%)
[CYCLE] Update 21/219 | Step 21,168/300,000 | Episode 28 | Time: 1827.2s
   📊 Metrics: Return=+29.12% | Sharpe=0.624 | DD=14.06% | Turnover=28.00%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0887 | critic_loss=0.1166 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0583 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0450 | balance_loss=0.0008 | separation_loss=0.0072 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6236 | ema=0.9318 | best_ema=0.9318 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3437
[CYCLE] Update 22/219 | Step 22,176/300,000 | Episode 28 | Time: 1908.8s
   📊 Metrics: Return=+4.76% | Sharpe=0.283 | DD=11.53% | Turnover=27.39%
   🎚️ Intra-Step TAPE: potential=0.6428 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0872 | critic_loss=0.0808 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0404 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0230 | balance_loss=0.0011 | separation_loss=0.0072 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2832 | ema=0.8670 | best_ema=0.8670 | no_improve=0
   🔬 Alpha Diversity: mean=3.71 | std=0.75 | range=[1.06, 4.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.07 | CAT=4.05 | PG=4.02  BOT: NEE=3.85 | MSFT=3.84 | JPM=3.78
   🎛️ Mixture Usage: C0=45.2% | C1=39.0% | C2=15.8%
   🧭 Regime Start Dist (train resets): high_vol=11 (34.4%), low_vol=12 (37.5%), medium_vol=9 (28.1%)
[CYCLE] Update 23/219 | Step 23,184/300,000 | Episode 28 | Time: 1989.5s
   📊 Metrics: Return=+9.02% | Sharpe=0.266 | DD=11.53% | Turnover=28.50%
   🎚️ Intra-Step TAPE: potential=0.2890 | delta_reward=-0.0025
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0892 | critic_loss=0.1024 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0512 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=0.9904 | balance_loss=0.0016 | separation_loss=0.0072 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2656 | ema=0.8068 | best_ema=0.8068 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p730_actor.weights.h5 (Sharpe=0.730, MDD=10.22%)
[CYCLE] Update 24/219 | Step 24,192/300,000 | Episode 32 | Time: 2069.9s
   📊 Metrics: Return=+34.55% | Sharpe=0.730 | DD=10.22% | Turnover=29.64%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0927 | critic_loss=0.0647 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0323 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=0.9544 | balance_loss=0.0021 | separation_loss=0.0072 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7296 | ema=0.7991 | best_ema=0.7991 | no_improve=0
   🔬 Alpha Diversity: mean=2.72 | std=0.45 | range=[0.96, 3.28] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=2.93 | JNJ=2.92 | AMZN=2.90  BOT: NEE=2.81 | MSFT=2.81 | JPM=2.76
   🎛️ Mixture Usage: C0=52.8% | C1=35.1% | C2=12.1%
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=12 (33.3%), medium_vol=12 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3956
[CYCLE] Update 25/219 | Step 25,200/300,000 | Episode 32 | Time: 2151.1s
   📊 Metrics: Return=+9.70% | Sharpe=0.791 | DD=4.38% | Turnover=35.98%
   🎚️ Intra-Step TAPE: potential=0.5454 | delta_reward=-0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0893 | critic_loss=0.0643 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0322 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9379 | balance_loss=0.0023 | separation_loss=0.0069 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7907 | ema=0.7983 | best_ema=0.7983 | no_improve=0
[CYCLE] Update 26/219 | Step 26,208/300,000 | Episode 32 | Time: 2231.7s
   📊 Metrics: Return=+4.16% | Sharpe=0.053 | DD=8.76% | Turnover=38.77%
   🎚️ Intra-Step TAPE: potential=0.2355 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0886 | critic_loss=0.1018 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0509 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9251 | balance_loss=0.0025 | separation_loss=0.0064 | component_dispersion_loss=0.0095
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0533 | ema=0.7238 | best_ema=0.7238 | no_improve=0
   🔬 Alpha Diversity: mean=2.36 | std=0.37 | range=[2.00, 4.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.31 | AMZN=2.30 | CAT=2.29  BOT: NEE=2.22 | MSFT=2.20 | JPM=2.17
   🎛️ Mixture Usage: C0=58.8% | C1=31.8% | C2=9.3%
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=12 (33.3%), medium_vol=12 (33.3%)
[CYCLE] Update 27/219 | Step 27,216/300,000 | Episode 36 | Time: 2310.9s
   📊 Metrics: Return=+8.17% | Sharpe=0.115 | DD=8.10% | Turnover=38.25%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0894 | critic_loss=0.1062 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0531 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9280 | balance_loss=0.0025 | separation_loss=0.0067 | component_dispersion_loss=0.0097
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1148 | ema=0.6629 | best_ema=0.6629 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2499
[CYCLE] Update 28/219 | Step 28,224/300,000 | Episode 36 | Time: 2392.9s
   📊 Metrics: Return=+12.94% | Sharpe=1.240 | DD=7.12% | Turnover=36.46%
   🎚️ Intra-Step TAPE: potential=0.4908 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0861 | critic_loss=0.0898 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0449 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9477 | balance_loss=0.0022 | separation_loss=0.0070 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2398 | ema=0.7206 | best_ema=0.7206 | no_improve=0
   🔬 Alpha Diversity: mean=2.67 | std=0.21 | range=[1.58, 3.01] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.81 | NVDA=2.79 | CAT=2.77  BOT: NEE=2.69 | MSFT=2.63 | JPM=2.62
   🎛️ Mixture Usage: C0=59.6% | C1=30.0% | C2=10.4%
   🧭 Regime Start Dist (train resets): high_vol=15 (37.5%), low_vol=13 (32.5%), medium_vol=12 (30.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 28 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 29/219 | Step 29,232/300,000 | Episode 36 | Time: 2473.1s
   📊 Metrics: Return=+11.09% | Sharpe=0.333 | DD=16.74% | Turnover=35.62%
   🎚️ Intra-Step TAPE: potential=0.5013 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0900 | critic_loss=0.0869 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0434 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9552 | balance_loss=0.0021 | separation_loss=0.0070 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3333 | ema=0.6819 | best_ema=0.6819 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00039_shp0p601_actor.weights.h5 (Sharpe=0.601, MDD=25.18%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00040_shp0p750_actor.weights.h5 (Sharpe=0.750, MDD=21.39%)
[CYCLE] Update 30/219 | Step 30,240/300,000 | Episode 40 | Time: 2553.3s
   📊 Metrics: Return=+50.39% | Sharpe=0.750 | DD=21.39% | Turnover=35.91%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0900 | critic_loss=0.0481 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0241 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9647 | balance_loss=0.0020 | separation_loss=0.0069 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7498 | ema=0.6887 | best_ema=0.6887 | no_improve=0
   🔬 Alpha Diversity: mean=2.72 | std=0.17 | range=[2.18, 3.93] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.79 | CAT=2.76 | GLD=2.74  BOT: XOM=2.71 | MSFT=2.66 | JPM=2.65
   🎛️ Mixture Usage: C0=54.8% | C1=34.0% | C2=11.2%
   🧭 Regime Start Dist (train resets): high_vol=15 (34.1%), low_vol=14 (31.8%), medium_vol=15 (34.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 30 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3557
[CYCLE] Update 31/219 | Step 31,248/300,000 | Episode 40 | Time: 2629.6s
   📊 Metrics: Return=+2.86% | Sharpe=0.143 | DD=7.54% | Turnover=33.88%
   🎚️ Intra-Step TAPE: potential=0.2434 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0875 | critic_loss=0.0640 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0320 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9729 | balance_loss=0.0018 | separation_loss=0.0069 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1427 | ema=0.6341 | best_ema=0.6341 | no_improve=0
[CYCLE] Update 32/219 | Step 32,256/300,000 | Episode 40 | Time: 2704.8s
   📊 Metrics: Return=-0.87% | Sharpe=-0.180 | DD=16.13% | Turnover=33.78%
   🎚️ Intra-Step TAPE: potential=0.2702 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0844 | critic_loss=0.1712 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0856 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9726 | balance_loss=0.0018 | separation_loss=0.0070 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1800 | ema=0.5526 | best_ema=0.5526 | no_improve=0
   🔬 Alpha Diversity: mean=2.95 | std=0.27 | range=[1.56, 3.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.12 | PG=3.07 | GLD=3.06  BOT: NVDA=2.99 | MSFT=2.93 | JPM=2.90
   🎛️ Mixture Usage: C0=50.4% | C1=39.8% | C2=9.8%
   🧭 Regime Start Dist (train resets): high_vol=15 (34.1%), low_vol=14 (31.8%), medium_vol=15 (34.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00044_shp1p009_actor.weights.h5 (Sharpe=1.009, MDD=12.77%)
[CYCLE] Update 33/219 | Step 33,264/300,000 | Episode 44 | Time: 2779.9s
   📊 Metrics: Return=+41.16% | Sharpe=1.009 | DD=12.77% | Turnover=32.28%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0872 | critic_loss=0.1118 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0559 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9992 | balance_loss=0.0014 | separation_loss=0.0071 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0087 | ema=0.5983 | best_ema=0.5983 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5173
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00359) | SPY bonus=0.001 (SPY ret=0.00301)
[CYCLE] Update 34/219 | Step 34,272/300,000 | Episode 44 | Time: 2854.8s
   📊 Metrics: Return=-3.58% | Sharpe=-0.327 | DD=18.75% | Turnover=32.42%
   🎚️ Intra-Step TAPE: potential=0.3054 | delta_reward=-0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0867 | critic_loss=0.0776 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0388 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9770 | balance_loss=0.0018 | separation_loss=0.0071 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3273 | ema=0.5057 | best_ema=0.5057 | no_improve=0
   🔬 Alpha Diversity: mean=3.02 | std=0.41 | range=[1.37, 3.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.25 | GLD=3.22 | PG=3.17  BOT: XOM=3.10 | MSFT=3.04 | JPM=3.00
   🎛️ Mixture Usage: C0=49.6% | C1=37.6% | C2=12.8%
   🧭 Regime Start Dist (train resets): high_vol=16 (33.3%), low_vol=16 (33.3%), medium_vol=16 (33.3%)
[CYCLE] Update 35/219 | Step 35,280/300,000 | Episode 44 | Time: 2929.7s
   📊 Metrics: Return=+0.40% | Sharpe=-0.071 | DD=18.75% | Turnover=32.03%
   🎚️ Intra-Step TAPE: potential=0.2195 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0853 | critic_loss=0.0644 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0322 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9805 | balance_loss=0.0017 | separation_loss=0.0072 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0705 | ema=0.4481 | best_ema=0.4481 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00046_shp1p260_actor.weights.h5 (Sharpe=1.260, MDD=9.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00047_shp0p606_actor.weights.h5 (Sharpe=0.606, MDD=18.98%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00048_shp0p864_actor.weights.h5 (Sharpe=0.864, MDD=11.04%)
[CYCLE] Update 36/219 | Step 36,288/300,000 | Episode 48 | Time: 3005.2s
   📊 Metrics: Return=+40.82% | Sharpe=0.864 | DD=11.04% | Turnover=31.43%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0865 | critic_loss=0.0632 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0316 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9908 | balance_loss=0.0015 | separation_loss=0.0071 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8641 | ema=0.4897 | best_ema=0.4897 | no_improve=0
   🔬 Alpha Diversity: mean=2.92 | std=0.47 | range=[1.10, 3.36] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.14 | NVDA=3.13 | GLD=3.11  BOT: NEE=3.04 | MSFT=2.99 | JPM=2.96
   🎛️ Mixture Usage: C0=47.1% | C1=39.2% | C2=13.7%
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=18 (34.6%), medium_vol=17 (32.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4402
[CYCLE] Update 37/219 | Step 37,296/300,000 | Episode 48 | Time: 3080.3s
   📊 Metrics: Return=+1.23% | Sharpe=-0.029 | DD=9.79% | Turnover=34.36%
   🎚️ Intra-Step TAPE: potential=0.2372 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0818 | critic_loss=0.0369 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0184 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0077 | balance_loss=0.0013 | separation_loss=0.0072 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0294 | ema=0.4378 | best_ema=0.4378 | no_improve=0
[CYCLE] Update 38/219 | Step 38,304/300,000 | Episode 48 | Time: 3155.6s
   📊 Metrics: Return=+4.09% | Sharpe=0.058 | DD=14.02% | Turnover=33.26%
   🎚️ Intra-Step TAPE: potential=0.4704 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0838 | critic_loss=0.0618 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0309 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0045 | balance_loss=0.0013 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0583 | ema=0.3998 | best_ema=0.3998 | no_improve=0
   🔬 Alpha Diversity: mean=3.04 | std=0.54 | range=[1.20, 3.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.29 | NVDA=3.25 | GLD=3.25  BOT: NEE=3.17 | MSFT=3.15 | JPM=3.11
   🎛️ Mixture Usage: C0=41.0% | C1=43.8% | C2=15.3%
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=18 (34.6%), medium_vol=17 (32.7%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00050_shp0p803_actor.weights.h5 (Sharpe=0.803, MDD=18.61%)
[CYCLE] Update 39/219 | Step 39,312/300,000 | Episode 52 | Time: 3232.5s
   📊 Metrics: Return=+13.19% | Sharpe=0.210 | DD=26.97% | Turnover=33.59%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0821 | critic_loss=0.0424 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0212 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0037 | balance_loss=0.0014 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2097 | ema=0.3808 | best_ema=0.3808 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.003) | TAPE=0.2278
[CYCLE] Update 40/219 | Step 40,320/300,000 | Episode 52 | Time: 3308.6s
   📊 Metrics: Return=+4.55% | Sharpe=0.314 | DD=5.32% | Turnover=32.19%
   🎚️ Intra-Step TAPE: potential=0.2246 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0807 | critic_loss=0.0249 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9965 | balance_loss=0.0015 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3144 | ema=0.3742 | best_ema=0.3742 | no_improve=0
   🔬 Alpha Diversity: mean=2.99 | std=0.57 | range=[1.04, 3.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.25 | GLD=3.21 | NVDA=3.19  BOT: NEE=3.13 | MSFT=3.13 | JPM=3.08
   🎛️ Mixture Usage: C0=42.4% | C1=44.0% | C2=13.6%
   🧭 Regime Start Dist (train resets): high_vol=18 (32.1%), low_vol=20 (35.7%), medium_vol=18 (32.1%)
[CYCLE] Update 41/219 | Step 41,328/300,000 | Episode 52 | Time: 3384.3s
   📊 Metrics: Return=+1.88% | Sharpe=-0.054 | DD=10.27% | Turnover=32.36%
   🎚️ Intra-Step TAPE: potential=0.2472 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0811 | critic_loss=0.0497 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0248 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9971 | balance_loss=0.0015 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0540 | ema=0.3313 | best_ema=0.3313 | no_improve=0
[CYCLE] Update 42/219 | Step 42,336/300,000 | Episode 56 | Time: 3460.6s
   📊 Metrics: Return=-3.03% | Sharpe=-0.232 | DD=14.87% | Turnover=34.02%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0872 | critic_loss=0.1358 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0679 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=0.9899 | balance_loss=0.0016 | separation_loss=0.0070 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2320 | ema=0.2750 | best_ema=0.2750 | no_improve=0
   🔬 Alpha Diversity: mean=2.88 | std=0.14 | range=[2.22, 3.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.94 | GLD=2.92 | PG=2.90  BOT: NEE=2.85 | MSFT=2.82 | JPM=2.79
   🎛️ Mixture Usage: C0=45.3% | C1=43.9% | C2=10.7%
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=20 (33.3%), medium_vol=20 (33.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 42 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2347
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00146) | SPY bonus=0.002 (SPY ret=-0.00225)
[CYCLE] Update 43/219 | Step 43,344/300,000 | Episode 56 | Time: 3537.5s
   📊 Metrics: Return=-3.73% | Sharpe=-0.383 | DD=16.36% | Turnover=37.58%
   🎚️ Intra-Step TAPE: potential=0.7411 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0854 | critic_loss=0.0693 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0347 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9923 | balance_loss=0.0015 | separation_loss=0.0071 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3831 | ema=0.2092 | best_ema=0.2092 | no_improve=0
[CYCLE] Update 44/219 | Step 44,352/300,000 | Episode 56 | Time: 3614.0s
   📊 Metrics: Return=-8.73% | Sharpe=-0.266 | DD=22.83% | Turnover=36.04%
   🎚️ Intra-Step TAPE: potential=0.2212 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0846 | critic_loss=0.0415 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0208 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0137 | balance_loss=0.0012 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2661 | ema=0.1617 | best_ema=0.1617 | no_improve=0
   🔬 Alpha Diversity: mean=3.13 | std=0.30 | range=[1.88, 3.45] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.30 | GLD=3.26 | PG=3.24  BOT: NEE=3.19 | MSFT=3.15 | JPM=3.14
   🎛️ Mixture Usage: C0=43.0% | C1=44.0% | C2=13.0%
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=20 (33.3%), medium_vol=20 (33.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00059_shp0p713_actor.weights.h5 (Sharpe=0.713, MDD=16.46%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00060_shp1p030_actor.weights.h5 (Sharpe=1.030, MDD=9.48%)
[CYCLE] Update 45/219 | Step 45,360/300,000 | Episode 60 | Time: 3690.4s
   📊 Metrics: Return=+42.00% | Sharpe=1.030 | DD=9.48% | Turnover=35.49%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0835 | critic_loss=0.0500 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0250 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0249 | balance_loss=0.0010 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0296 | ema=0.2485 | best_ema=0.2485 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5068
[CYCLE] Update 46/219 | Step 46,368/300,000 | Episode 60 | Time: 3765.7s
   📊 Metrics: Return=-5.83% | Sharpe=-0.438 | DD=17.85% | Turnover=32.69%
   🎚️ Intra-Step TAPE: potential=0.5117 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0834 | critic_loss=0.0443 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0222 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0317 | balance_loss=0.0009 | separation_loss=0.0078 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4378 | ema=0.1798 | best_ema=0.1798 | no_improve=0
   🔬 Alpha Diversity: mean=3.29 | std=0.72 | range=[0.85, 3.89] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.59 | PG=3.55 | CAT=3.53  BOT: NEE=3.49 | MSFT=3.48 | JPM=3.46
   🎛️ Mixture Usage: C0=41.8% | C1=39.2% | C2=19.0%
   🧭 Regime Start Dist (train resets): high_vol=22 (34.4%), low_vol=21 (32.8%), medium_vol=21 (32.8%)
[CYCLE] Update 47/219 | Step 47,376/300,000 | Episode 60 | Time: 3841.4s
   📊 Metrics: Return=+19.01% | Sharpe=0.412 | DD=25.54% | Turnover=32.72%
   🎚️ Intra-Step TAPE: potential=0.6872 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0786 | critic_loss=0.0512 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0256 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0381 | balance_loss=0.0008 | separation_loss=0.0079 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4121 | ema=0.2031 | best_ema=0.2031 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00063_shp1p485_actor.weights.h5 (Sharpe=1.485, MDD=9.51%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00064_shp1p081_actor.weights.h5 (Sharpe=1.081, MDD=11.83%)
[CYCLE] Update 48/219 | Step 48,384/300,000 | Episode 64 | Time: 3917.2s
   📊 Metrics: Return=+51.21% | Sharpe=1.081 | DD=11.83% | Turnover=32.34%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0842 | critic_loss=0.0496 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0248 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0365 | balance_loss=0.0009 | separation_loss=0.0079 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0814 | ema=0.2909 | best_ema=0.2909 | no_improve=0
   🔬 Alpha Diversity: mean=3.29 | std=0.82 | range=[0.53, 3.80] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.60 | PG=3.58 | CAT=3.56  BOT: NEE=3.53 | JPM=3.49 | MSFT=3.49
   🎛️ Mixture Usage: C0=40.8% | C1=41.1% | C2=18.2%
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=23 (33.8%), medium_vol=22 (32.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5171
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00582) | SPY bonus=0.010 (SPY ret=0.00130)
[CYCLE] Update 49/219 | Step 49,392/300,000 | Episode 64 | Time: 3994.5s
   📊 Metrics: Return=+1.79% | Sharpe=0.061 | DD=19.36% | Turnover=33.47%
   🎚️ Intra-Step TAPE: potential=0.7500 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0812 | critic_loss=0.0545 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0273 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0197 | balance_loss=0.0011 | separation_loss=0.0078 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0612 | ema=0.2679 | best_ema=0.2679 | no_improve=0

📚 EPISODE HORIZON UPDATE at 50,400 steps:
   Episode horizon: 766 steps
[CYCLE] Update 50/219 | Step 50,400/300,000 | Episode 64 | Time: 4072.7s
   📊 Metrics: Return=+5.36% | Sharpe=0.139 | DD=26.12% | Turnover=33.74%
   🎚️ Intra-Step TAPE: potential=0.2316 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0837 | critic_loss=0.0542 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0271 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0193 | balance_loss=0.0011 | separation_loss=0.0077 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1390 | ema=0.2550 | best_ema=0.2550 | no_improve=0
   🔬 Alpha Diversity: mean=3.08 | std=0.78 | range=[0.58, 3.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.38 | GLD=3.35 | CAT=3.34  BOT: XOM=3.32 | JPM=3.27 | MSFT=3.25
   🎛️ Mixture Usage: C0=42.9% | C1=43.5% | C2=13.7%
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=23 (33.8%), medium_vol=22 (32.4%)

📚 EPISODE HORIZON UPDATE at 51,408 steps:
   Episode horizon: 791 steps
[CYCLE] Update 51/219 | Step 51,408/300,000 | Episode 64 | Time: 4150.7s
   📊 Metrics: Return=+37.04% | Sharpe=0.520 | DD=26.12% | Turnover=33.62%
   🎚️ Intra-Step TAPE: potential=0.6122 | delta_reward=+0.0023
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0834 | critic_loss=0.0348 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0174 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0190 | balance_loss=0.0011 | separation_loss=0.0078 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5201 | ema=0.2815 | best_ema=0.2815 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00067_shp0p669_actor.weights.h5 (Sharpe=0.669, MDD=12.10%)

📚 EPISODE HORIZON UPDATE at 52,416 steps:
   Episode horizon: 817 steps
[CYCLE] Update 52/219 | Step 52,416/300,000 | Episode 68 | Time: 4228.7s
   📊 Metrics: Return=+34.36% | Sharpe=0.478 | DD=25.96% | Turnover=33.15%
   🎚️ Intra-Step TAPE: potential=0.2599 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0826 | critic_loss=0.0312 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0156 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0235 | balance_loss=0.0011 | separation_loss=0.0077 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4785 | ema=0.3012 | best_ema=0.3012 | no_improve=0
   🔬 Alpha Diversity: mean=3.10 | std=0.81 | range=[0.43, 3.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.41 | GLD=3.40 | AMZN=3.36  BOT: XOM=3.35 | JPM=3.30 | MSFT=3.30
   🎛️ Mixture Usage: C0=39.1% | C1=45.1% | C2=15.8%
   🧭 Regime Start Dist (train resets): high_vol=24 (33.3%), low_vol=24 (33.3%), medium_vol=24 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 5.30% / trig 25.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2669

📚 EPISODE HORIZON UPDATE at 53,424 steps:
   Episode horizon: 842 steps
[CYCLE] Update 53/219 | Step 53,424/300,000 | Episode 68 | Time: 4307.1s
   📊 Metrics: Return=+6.60% | Sharpe=0.180 | DD=27.26% | Turnover=32.39%
   🎚️ Intra-Step TAPE: potential=0.7203 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0814 | critic_loss=0.0286 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0143 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0309 | balance_loss=0.0009 | separation_loss=0.0077 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1799 | ema=0.2891 | best_ema=0.2891 | no_improve=0

📚 EPISODE HORIZON UPDATE at 54,432 steps:
   Episode horizon: 868 steps
[CYCLE] Update 54/219 | Step 54,432/300,000 | Episode 68 | Time: 4385.9s
   📊 Metrics: Return=+41.30% | Sharpe=0.590 | DD=27.26% | Turnover=32.02%
   🎚️ Intra-Step TAPE: potential=0.7348 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0825 | critic_loss=0.0273 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0136 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0215 | balance_loss=0.0011 | separation_loss=0.0078 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5901 | ema=0.3192 | best_ema=0.3192 | no_improve=0
   🔬 Alpha Diversity: mean=3.13 | std=0.74 | range=[0.61, 3.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.42 | XOM=3.39 | GLD=3.38  BOT: NEE=3.36 | JPM=3.32 | MSFT=3.31
   🎛️ Mixture Usage: C0=43.7% | C1=39.3% | C2=17.1%
   🧭 Regime Start Dist (train resets): high_vol=24 (33.3%), low_vol=24 (33.3%), medium_vol=24 (33.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00069_shp0p644_actor.weights.h5 (Sharpe=0.644, MDD=27.26%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00070_shp0p976_actor.weights.h5 (Sharpe=0.976, MDD=12.29%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00071_shp0p609_actor.weights.h5 (Sharpe=0.609, MDD=26.66%)

📚 EPISODE HORIZON UPDATE at 55,440 steps:
   Episode horizon: 893 steps
[CYCLE] Update 55/219 | Step 55,440/300,000 | Episode 72 | Time: 4465.4s
   📊 Metrics: Return=+30.61% | Sharpe=0.562 | DD=13.89% | Turnover=33.35%
   🎚️ Intra-Step TAPE: potential=0.2221 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0761 | critic_loss=0.0369 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0184 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0122 | balance_loss=0.0012 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5622 | ema=0.3435 | best_ema=0.3435 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 6.16% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3272

📚 EPISODE HORIZON UPDATE at 56,448 steps:
   Episode horizon: 918 steps
[CYCLE] Update 56/219 | Step 56,448/300,000 | Episode 72 | Time: 4543.7s
   📊 Metrics: Return=+12.31% | Sharpe=0.503 | DD=15.97% | Turnover=36.46%
   🎚️ Intra-Step TAPE: potential=0.7247 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0833 | critic_loss=0.0304 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0152 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0131 | balance_loss=0.0012 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5025 | ema=0.3594 | best_ema=0.3594 | no_improve=0
   🔬 Alpha Diversity: mean=2.98 | std=0.55 | range=[1.12, 3.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.20 | GLD=3.18 | PG=3.16  BOT: NEE=3.14 | MSFT=3.11 | JPM=3.10
   🎛️ Mixture Usage: C0=48.7% | C1=38.5% | C2=12.8%
   🧭 Regime Start Dist (train resets): high_vol=26 (34.2%), low_vol=26 (34.2%), medium_vol=24 (31.6%)

📚 EPISODE HORIZON UPDATE at 57,456 steps:
   Episode horizon: 944 steps
[CYCLE] Update 57/219 | Step 57,456/300,000 | Episode 72 | Time: 4622.3s
   📊 Metrics: Return=+13.31% | Sharpe=0.257 | DD=23.59% | Turnover=36.24%
   🎚️ Intra-Step TAPE: potential=0.2220 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0842 | critic_loss=0.0296 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0148 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0260 | balance_loss=0.0010 | separation_loss=0.0078 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2574 | ema=0.3492 | best_ema=0.3492 | no_improve=0

📚 EPISODE HORIZON UPDATE at 58,464 steps:
   Episode horizon: 969 steps
[CYCLE] Update 58/219 | Step 58,464/300,000 | Episode 72 | Time: 4700.2s
   📊 Metrics: Return=+45.03% | Sharpe=0.560 | DD=23.59% | Turnover=35.63%
   🎚️ Intra-Step TAPE: potential=0.5764 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0791 | critic_loss=0.0233 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0116 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0294 | balance_loss=0.0010 | separation_loss=0.0078 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5597 | ema=0.3703 | best_ema=0.3703 | no_improve=0
   🔬 Alpha Diversity: mean=3.23 | std=0.73 | range=[0.72, 3.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.51 | PG=3.47 | XOM=3.47  BOT: NEE=3.44 | JPM=3.42 | MSFT=3.42
   🎛️ Mixture Usage: C0=45.6% | C1=39.2% | C2=15.2%
   🧭 Regime Start Dist (train resets): high_vol=26 (34.2%), low_vol=26 (34.2%), medium_vol=24 (31.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp0p603_actor.weights.h5 (Sharpe=0.603, MDD=23.59%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00074_shp1p255_actor.weights.h5 (Sharpe=1.255, MDD=15.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00076_shp0p694_actor.weights.h5 (Sharpe=0.694, MDD=15.96%)

📚 EPISODE HORIZON UPDATE at 59,472 steps:
   Episode horizon: 995 steps
[CYCLE] Update 59/219 | Step 59,472/300,000 | Episode 76 | Time: 4779.4s
   📊 Metrics: Return=+42.73% | Sharpe=0.694 | DD=15.96% | Turnover=35.18%
   🎚️ Intra-Step TAPE: potential=0.6144 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0814 | critic_loss=0.0460 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0230 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0315 | balance_loss=0.0009 | separation_loss=0.0079 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6936 | ema=0.4026 | best_ema=0.4026 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.04% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3596

📚 TURNOVER CURRICULUM UPDATE at 60,480 steps:
   Turnover penalty scalar: 0.15

🎛️ EXECUTION BETA UPDATE at 60,480 steps:
   action_execution_beta: 0.650 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 60,480 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 60/219 | Step 60,480/300,000 | Episode 76 | Time: 4857.7s
   📊 Metrics: Return=+41.56% | Sharpe=1.668 | DD=8.33% | Turnover=32.07%
   🎚️ Intra-Step TAPE: potential=0.4318 | delta_reward=+0.0018
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0812 | critic_loss=0.0289 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0145 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0423 | balance_loss=0.0008 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6678 | ema=0.5291 | best_ema=0.5291 | no_improve=0
   🔬 Alpha Diversity: mean=3.62 | std=0.63 | range=[1.49, 4.15] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.86 | GLD=3.84 | XOM=3.82  BOT: NEE=3.79 | MSFT=3.78 | JPM=3.75
   🎛️ Mixture Usage: C0=43.1% | C1=39.4% | C2=17.6%
   🧭 Regime Start Dist (train resets): high_vol=27 (33.8%), low_vol=27 (33.8%), medium_vol=26 (32.5%)
[CYCLE] Update 61/219 | Step 61,488/300,000 | Episode 76 | Time: 4937.0s
   📊 Metrics: Return=+58.57% | Sharpe=1.381 | DD=8.93% | Turnover=36.37%
   🎚️ Intra-Step TAPE: potential=0.2249 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0793 | critic_loss=0.0229 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0114 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0623 | balance_loss=0.0005 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3814 | ema=0.6143 | best_ema=0.6143 | no_improve=0
[CYCLE] Update 62/219 | Step 62,496/300,000 | Episode 76 | Time: 5014.3s
   📊 Metrics: Return=+53.37% | Sharpe=0.844 | DD=22.84% | Turnover=37.97%
   🎚️ Intra-Step TAPE: potential=0.7365 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0790 | critic_loss=0.0256 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0128 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0785 | balance_loss=0.0003 | separation_loss=0.0077 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8437 | ema=0.6373 | best_ema=0.6373 | no_improve=0
   🔬 Alpha Diversity: mean=4.65 | std=0.68 | range=[2.01, 5.17] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.93 | XOM=4.87 | NVDA=4.87  BOT: NEE=4.83 | JPM=4.81 | MSFT=4.80
   🎛️ Mixture Usage: C0=38.0% | C1=38.1% | C2=23.9%
   🧭 Regime Start Dist (train resets): high_vol=27 (33.8%), low_vol=27 (33.8%), medium_vol=26 (32.5%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00077_shp0p690_actor.weights.h5 (Sharpe=0.690, MDD=22.84%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00078_shp0p747_actor.weights.h5 (Sharpe=0.747, MDD=11.90%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00079_shp0p833_actor.weights.h5 (Sharpe=0.833, MDD=11.33%)
[CYCLE] Update 63/219 | Step 63,504/300,000 | Episode 80 | Time: 5094.0s
   📊 Metrics: Return=+37.10% | Sharpe=0.563 | DD=12.71% | Turnover=38.60%
   🎚️ Intra-Step TAPE: potential=0.3612 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0841 | critic_loss=0.0324 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0162 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0741 | balance_loss=0.0003 | separation_loss=0.0077 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5634 | ema=0.6299 | best_ema=0.6299 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3180
[CYCLE] Update 64/219 | Step 64,512/300,000 | Episode 80 | Time: 5172.2s
   📊 Metrics: Return=+6.66% | Sharpe=0.248 | DD=6.07% | Turnover=41.43%
   🎚️ Intra-Step TAPE: potential=0.2269 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0804 | critic_loss=0.0253 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0127 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0660 | balance_loss=0.0004 | separation_loss=0.0079 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2481 | ema=0.5917 | best_ema=0.5917 | no_improve=0
   🔬 Alpha Diversity: mean=4.23 | std=0.41 | range=[2.70, 4.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.43 | XOM=4.39 | GLD=4.38  BOT: NEE=4.34 | MSFT=4.31 | JPM=4.31
   🎛️ Mixture Usage: C0=38.0% | C1=38.4% | C2=23.6%
   🧭 Regime Start Dist (train resets): high_vol=28 (33.3%), low_vol=28 (33.3%), medium_vol=28 (33.3%)
[CYCLE] Update 65/219 | Step 65,520/300,000 | Episode 80 | Time: 5248.1s
   📊 Metrics: Return=+4.19% | Sharpe=0.015 | DD=9.93% | Turnover=41.70%
   🎚️ Intra-Step TAPE: potential=0.2337 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0833 | critic_loss=0.0516 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0258 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0523 | balance_loss=0.0006 | separation_loss=0.0081 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0149 | ema=0.5340 | best_ema=0.5340 | no_improve=0
[CYCLE] Update 66/219 | Step 66,528/300,000 | Episode 80 | Time: 5322.0s
   📊 Metrics: Return=+10.14% | Sharpe=0.119 | DD=14.29% | Turnover=42.00%
   🎚️ Intra-Step TAPE: potential=0.7223 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0826 | critic_loss=0.0271 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0136 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0502 | balance_loss=0.0007 | separation_loss=0.0081 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1188 | ema=0.4925 | best_ema=0.4925 | no_improve=0
   🔬 Alpha Diversity: mean=4.04 | std=0.16 | range=[3.51, 4.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.12 | XOM=4.08 | GLD=4.06  BOT: NEE=4.02 | MSFT=4.02 | JPM=4.00
   🎛️ Mixture Usage: C0=41.1% | C1=37.6% | C2=21.3%
   🧭 Regime Start Dist (train resets): high_vol=28 (33.3%), low_vol=28 (33.3%), medium_vol=28 (33.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 66 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00083_shp0p718_actor.weights.h5 (Sharpe=0.718, MDD=18.97%)
[CYCLE] Update 67/219 | Step 67,536/300,000 | Episode 84 | Time: 5397.5s
   📊 Metrics: Return=+25.97% | Sharpe=0.381 | DD=15.19% | Turnover=42.54%
   🎚️ Intra-Step TAPE: potential=0.5952 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0804 | critic_loss=0.0208 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0104 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0564 | balance_loss=0.0006 | separation_loss=0.0081 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3812 | ema=0.4814 | best_ema=0.4814 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.25% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2823
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00078) | SPY bonus=0.000 (SPY ret=0.00093)
[CYCLE] Update 68/219 | Step 68,544/300,000 | Episode 84 | Time: 5470.6s
   📊 Metrics: Return=+23.45% | Sharpe=1.067 | DD=9.88% | Turnover=42.93%
   🎚️ Intra-Step TAPE: potential=0.2406 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0833 | critic_loss=0.0126 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0063 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0618 | balance_loss=0.0005 | separation_loss=0.0081 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0665 | ema=0.5399 | best_ema=0.5399 | no_improve=0
   🔬 Alpha Diversity: mean=4.23 | std=0.14 | range=[3.87, 4.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.27 | XOM=4.23 | PG=4.22  BOT: NEE=4.19 | MSFT=4.18 | JPM=4.17
   🎛️ Mixture Usage: C0=41.5% | C1=37.9% | C2=20.6%
   🧭 Regime Start Dist (train resets): high_vol=30 (34.1%), low_vol=28 (31.8%), medium_vol=30 (34.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 68 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 69/219 | Step 69,552/300,000 | Episode 84 | Time: 5543.8s
   📊 Metrics: Return=+45.99% | Sharpe=1.193 | DD=9.88% | Turnover=42.74%
   🎚️ Intra-Step TAPE: potential=0.2235 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0837 | critic_loss=0.0170 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0085 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0545 | balance_loss=0.0006 | separation_loss=0.0082 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1930 | ema=0.6052 | best_ema=0.6052 | no_improve=0
[CYCLE] Update 70/219 | Step 70,560/300,000 | Episode 84 | Time: 5621.8s
   📊 Metrics: Return=+50.14% | Sharpe=0.824 | DD=20.12% | Turnover=42.71%
   🎚️ Intra-Step TAPE: potential=0.7184 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0820 | critic_loss=0.0166 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0445 | balance_loss=0.0008 | separation_loss=0.0081 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8239 | ema=0.6271 | best_ema=0.6271 | no_improve=0
   🔬 Alpha Diversity: mean=3.83 | std=0.21 | range=[3.17, 4.17] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.92 | XOM=3.89 | PG=3.88  BOT: JPM=3.82 | NVDA=3.81 | MSFT=3.81
   🎛️ Mixture Usage: C0=38.4% | C1=41.6% | C2=20.0%
   🧭 Regime Start Dist (train resets): high_vol=30 (34.1%), low_vol=28 (31.8%), medium_vol=30 (34.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 70 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00085_shp0p694_actor.weights.h5 (Sharpe=0.694, MDD=20.12%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00087_shp0p694_actor.weights.h5 (Sharpe=0.694, MDD=16.29%)
[CYCLE] Update 71/219 | Step 71,568/300,000 | Episode 88 | Time: 5700.7s
   📊 Metrics: Return=+33.03% | Sharpe=0.379 | DD=27.73% | Turnover=43.24%
   🎚️ Intra-Step TAPE: potential=0.2155 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0826 | critic_loss=0.0345 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0173 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0447 | balance_loss=0.0008 | separation_loss=0.0081 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3785 | ema=0.6022 | best_ema=0.6022 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 10.00% / trig 25.00%) | terminal=0.000 (peak 0.003) | TAPE=0.2413
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00038) | SPY bonus=0.014 (SPY ret=-0.00644)
[CYCLE] Update 72/219 | Step 72,576/300,000 | Episode 88 | Time: 5778.0s
   📊 Metrics: Return=+3.91% | Sharpe=0.100 | DD=21.98% | Turnover=44.01%
   🎚️ Intra-Step TAPE: potential=0.6937 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0832 | critic_loss=0.0327 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0164 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0462 | balance_loss=0.0007 | separation_loss=0.0080 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0997 | ema=0.5520 | best_ema=0.5520 | no_improve=0
   🔬 Alpha Diversity: mean=3.86 | std=0.19 | range=[3.20, 4.20] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.93 | XOM=3.91 | PG=3.91  BOT: MSFT=3.84 | JPM=3.84 | AMZN=3.84
   🎛️ Mixture Usage: C0=38.3% | C1=44.6% | C2=17.1%
   🧭 Regime Start Dist (train resets): high_vol=30 (32.6%), low_vol=32 (34.8%), medium_vol=30 (32.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 72 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 73/219 | Step 73,584/300,000 | Episode 88 | Time: 5856.0s
   📊 Metrics: Return=-0.49% | Sharpe=-0.021 | DD=27.52% | Turnover=43.78%
   🎚️ Intra-Step TAPE: potential=0.2080 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0826 | critic_loss=0.0268 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0134 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0658 | balance_loss=0.0004 | separation_loss=0.0080 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0210 | ema=0.4947 | best_ema=0.4947 | no_improve=0
[CYCLE] Update 74/219 | Step 74,592/300,000 | Episode 88 | Time: 5933.4s
   📊 Metrics: Return=+30.09% | Sharpe=0.379 | DD=27.52% | Turnover=43.75%
   🎚️ Intra-Step TAPE: potential=0.5591 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0804 | critic_loss=0.0270 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0135 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0733 | balance_loss=0.0003 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3793 | ema=0.4831 | best_ema=0.4831 | no_improve=0
   🔬 Alpha Diversity: mean=4.60 | std=0.35 | range=[3.21, 5.21] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.70 | XOM=4.66 | PG=4.65  BOT: NEE=4.61 | MSFT=4.60 | NVDA=4.58
   🎛️ Mixture Usage: C0=38.5% | C1=39.1% | C2=22.4%
   🧭 Regime Start Dist (train resets): high_vol=30 (32.6%), low_vol=32 (34.8%), medium_vol=30 (32.6%)
[CYCLE] Update 75/219 | Step 75,600/300,000 | Episode 92 | Time: 6012.2s
   📊 Metrics: Return=+43.10% | Sharpe=0.473 | DD=27.67% | Turnover=43.77%
   🎚️ Intra-Step TAPE: potential=0.2197 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0828 | critic_loss=0.0237 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0119 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0840 | balance_loss=0.0002 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4729 | ema=0.4821 | best_ema=0.4821 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 6.02% / trig 25.00%) | terminal=0.000 (peak 0.004) | TAPE=0.2550
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00633) | SPY bonus=0.022 (SPY ret=0.00116)
[CYCLE] Update 76/219 | Step 76,608/300,000 | Episode 92 | Time: 6092.4s
   📊 Metrics: Return=-13.74% | Sharpe=-0.880 | DD=19.55% | Turnover=41.01%
   🎚️ Intra-Step TAPE: potential=0.2373 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0813 | critic_loss=0.0257 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0128 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0824 | balance_loss=0.0002 | separation_loss=0.0082 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.8800 | ema=0.3459 | best_ema=0.3459 | no_improve=0
   🔬 Alpha Diversity: mean=4.92 | std=0.14 | range=[4.55, 5.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.95 | XOM=4.94 | CAT=4.94  BOT: NEE=4.89 | MSFT=4.88 | JPM=4.87
   🎛️ Mixture Usage: C0=34.7% | C1=38.9% | C2=26.4%
   🧭 Regime Start Dist (train resets): high_vol=32 (33.3%), low_vol=32 (33.3%), medium_vol=32 (33.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 76 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 77/219 | Step 77,616/300,000 | Episode 92 | Time: 6184.6s
   📊 Metrics: Return=-1.24% | Sharpe=-0.146 | DD=19.55% | Turnover=42.47%
   🎚️ Intra-Step TAPE: potential=0.5182 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0834 | critic_loss=0.0310 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0155 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0773 | balance_loss=0.0003 | separation_loss=0.0082 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1458 | ema=0.2967 | best_ema=0.2967 | no_improve=0
[CYCLE] Update 78/219 | Step 78,624/300,000 | Episode 92 | Time: 6268.4s
   📊 Metrics: Return=+11.87% | Sharpe=0.158 | DD=19.55% | Turnover=42.67%
   🎚️ Intra-Step TAPE: potential=0.6793 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0856 | critic_loss=0.0207 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0103 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0755 | balance_loss=0.0003 | separation_loss=0.0078 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1584 | ema=0.2829 | best_ema=0.2829 | no_improve=0
   🔬 Alpha Diversity: mean=4.60 | std=0.31 | range=[3.97, 5.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.58 | XOM=4.55 | PG=4.54  BOT: NVDA=4.52 | MSFT=4.51 | JPM=4.50
   🎛️ Mixture Usage: C0=36.7% | C1=40.2% | C2=23.1%
   🧭 Regime Start Dist (train resets): high_vol=32 (33.3%), low_vol=32 (33.3%), medium_vol=32 (33.3%)
[CYCLE] Update 79/219 | Step 79,632/300,000 | Episode 96 | Time: 6347.6s
   📊 Metrics: Return=+37.94% | Sharpe=0.542 | DD=18.21% | Turnover=42.62%
   🎚️ Intra-Step TAPE: potential=0.6197 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0795 | critic_loss=0.0249 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0124 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0774 | balance_loss=0.0003 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5425 | ema=0.3089 | best_ema=0.3089 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.84% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3058
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00290) | SPY bonus=0.002 (SPY ret=0.00136)
[CYCLE] Update 80/219 | Step 80,640/300,000 | Episode 96 | Time: 6426.7s
   📊 Metrics: Return=+10.39% | Sharpe=0.478 | DD=10.50% | Turnover=49.83%
   🎚️ Intra-Step TAPE: potential=0.6426 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0829 | critic_loss=0.0218 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0109 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0839 | balance_loss=0.0001 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4783 | ema=0.3258 | best_ema=0.3258 | no_improve=0
   🔬 Alpha Diversity: mean=4.84 | std=0.19 | range=[4.08, 5.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.86 | XOM=4.83 | PG=4.82  BOT: NVDA=4.80 | JPM=4.79 | MSFT=4.79
   🎛️ Mixture Usage: C0=33.7% | C1=38.9% | C2=27.4%
   🧭 Regime Start Dist (train resets): high_vol=34 (34.0%), low_vol=33 (33.0%), medium_vol=33 (33.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 80 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 81/219 | Step 81,648/300,000 | Episode 96 | Time: 6506.4s
   📊 Metrics: Return=+13.91% | Sharpe=0.351 | DD=10.50% | Turnover=48.74%
   🎚️ Intra-Step TAPE: potential=0.2293 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0838 | critic_loss=0.0334 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0167 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0772 | balance_loss=0.0001 | separation_loss=0.0075 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3507 | ema=0.3283 | best_ema=0.3283 | no_improve=0
[CYCLE] Update 82/219 | Step 82,656/300,000 | Episode 96 | Time: 6586.1s
   📊 Metrics: Return=+7.98% | Sharpe=0.071 | DD=23.59% | Turnover=47.66%
   🎚️ Intra-Step TAPE: potential=0.2316 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0820 | critic_loss=0.0204 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0102 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0674 | balance_loss=0.0002 | separation_loss=0.0080 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0707 | ema=0.3025 | best_ema=0.3025 | no_improve=0
   🔬 Alpha Diversity: mean=4.15 | std=0.66 | range=[1.36, 4.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=4.39 | XOM=4.37 | PG=4.37  BOT: JPM=4.33 | MSFT=4.32 | NVDA=4.31
   🎛️ Mixture Usage: C0=36.6% | C1=40.8% | C2=22.6%
   🧭 Regime Start Dist (train resets): high_vol=34 (34.0%), low_vol=33 (33.0%), medium_vol=33 (33.0%)
[CYCLE] Update 83/219 | Step 83,664/300,000 | Episode 100 | Time: 6666.5s
   📊 Metrics: Return=-10.61% | Sharpe=-0.383 | DD=16.78% | Turnover=47.98%
   🎚️ Intra-Step TAPE: potential=0.2327 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0868 | critic_loss=0.0283 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0142 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0630 | balance_loss=0.0003 | separation_loss=0.0080 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3834 | ema=0.2339 | best_ema=0.2339 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.81% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2279
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01772) | SPY bonus=0.005 (SPY ret=-0.01905)
[CYCLE] Update 84/219 | Step 84,672/300,000 | Episode 100 | Time: 6748.1s
   📊 Metrics: Return=-3.24% | Sharpe=-0.282 | DD=15.83% | Turnover=44.69%
   🎚️ Intra-Step TAPE: potential=0.3255 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0827 | critic_loss=0.0158 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0079 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0611 | balance_loss=0.0003 | separation_loss=0.0077 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2820 | ema=0.1823 | best_ema=0.1823 | no_improve=0
   🔬 Alpha Diversity: mean=4.22 | std=0.39 | range=[2.20, 4.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=4.36 | PG=4.35 | JNJ=4.35  BOT: JPM=4.29 | MSFT=4.28 | NVDA=4.27
   🎛️ Mixture Usage: C0=35.0% | C1=43.9% | C2=21.0%
   🧭 Regime Start Dist (train resets): high_vol=35 (33.7%), low_vol=35 (33.7%), medium_vol=34 (32.7%)
[CYCLE] Update 85/219 | Step 85,680/300,000 | Episode 100 | Time: 6829.4s
   📊 Metrics: Return=+3.97% | Sharpe=0.015 | DD=15.83% | Turnover=46.45%
   🎚️ Intra-Step TAPE: potential=0.2369 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0825 | critic_loss=0.0171 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0085 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0602 | balance_loss=0.0003 | separation_loss=0.0070 | component_dispersion_loss=0.0097
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0150 | ema=0.1656 | best_ema=0.1656 | no_improve=0
[CYCLE] Update 86/219 | Step 86,688/300,000 | Episode 100 | Time: 6909.6s
   📊 Metrics: Return=+17.05% | Sharpe=0.284 | DD=15.83% | Turnover=48.02%
   🎚️ Intra-Step TAPE: potential=0.6859 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0831 | critic_loss=0.0124 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0062 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   🧩 Mixture Head: gate_entropy=1.0560 | balance_loss=0.0003 | separation_loss=0.0070 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2837 | ema=0.1774 | best_ema=0.1774 | no_improve=0
   🔬 Alpha Diversity: mean=3.90 | std=0.31 | range=[2.60, 4.43] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.96 | PG=3.96 | XOM=3.95  BOT: MSFT=3.90 | JPM=3.90 | NVDA=3.87
   🎛️ Mixture Usage: C0=39.5% | C1=40.1% | C2=20.4%
   🧭 Regime Start Dist (train resets): high_vol=35 (33.7%), low_vol=35 (33.7%), medium_vol=34 (32.7%)
[CYCLE] Update 87/219 | Step 87,696/300,000 | Episode 104 | Time: 6990.1s
   📊 Metrics: Return=+11.57% | Sharpe=0.125 | DD=16.45% | Turnover=48.83%
   🎚️ Intra-Step TAPE: potential=0.7474 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0820 | critic_loss=0.0261 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0131 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0584 | balance_loss=0.0003 | separation_loss=0.0073 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1251 | ema=0.1722 | best_ema=0.1722 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2403
[CYCLE] Update 88/219 | Step 88,704/300,000 | Episode 104 | Time: 7072.3s
   📊 Metrics: Return=+1.90% | Sharpe=-0.009 | DD=17.80% | Turnover=50.77%
   🎚️ Intra-Step TAPE: potential=0.2336 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0881 | critic_loss=0.0241 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0120 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0434 | balance_loss=0.0004 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0085 | ema=0.1541 | best_ema=0.1541 | no_improve=0
   🔬 Alpha Diversity: mean=3.46 | std=0.52 | range=[1.58, 3.94] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.63 | XOM=3.63 | PG=3.63  BOT: JPM=3.59 | MSFT=3.58 | NVDA=3.58
   🎛️ Mixture Usage: C0=41.6% | C1=39.1% | C2=19.3%
   🧭 Regime Start Dist (train resets): high_vol=36 (33.3%), low_vol=36 (33.3%), medium_vol=36 (33.3%)
[CYCLE] Update 89/219 | Step 89,712/300,000 | Episode 104 | Time: 7154.3s
   📊 Metrics: Return=+18.07% | Sharpe=0.452 | DD=17.80% | Turnover=50.47%
   🎚️ Intra-Step TAPE: potential=0.7390 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0774 | critic_loss=0.0174 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0087 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0405 | balance_loss=0.0004 | separation_loss=0.0076 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4521 | ema=0.1839 | best_ema=0.1839 | no_improve=0
[CYCLE] Update 90/219 | Step 90,720/300,000 | Episode 104 | Time: 7235.1s
   📊 Metrics: Return=+21.77% | Sharpe=0.289 | DD=27.01% | Turnover=50.32%
   🎚️ Intra-Step TAPE: potential=0.3074 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0808 | critic_loss=0.0247 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0124 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0379 | balance_loss=0.0004 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2890 | ema=0.1944 | best_ema=0.1944 | no_improve=0
   🔬 Alpha Diversity: mean=3.41 | std=0.57 | range=[1.12, 4.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.59 | PG=3.57 | GLD=3.56  BOT: NVDA=3.54 | MSFT=3.54 | JPM=3.53
   🎛️ Mixture Usage: C0=44.0% | C1=38.8% | C2=17.2%
   🧭 Regime Start Dist (train resets): high_vol=36 (33.3%), low_vol=36 (33.3%), medium_vol=36 (33.3%)
[CYCLE] Update 91/219 | Step 91,728/300,000 | Episode 108 | Time: 7315.3s
   📊 Metrics: Return=+22.95% | Sharpe=0.369 | DD=14.24% | Turnover=49.23%
   🎚️ Intra-Step TAPE: potential=0.6990 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0820 | critic_loss=0.0221 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0110 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0498 | balance_loss=0.0004 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3692 | ema=0.2119 | best_ema=0.2119 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2774
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.01218) | SPY bonus=0.013 (SPY ret=0.00780)
[CYCLE] Update 92/219 | Step 92,736/300,000 | Episode 108 | Time: 7396.2s
   📊 Metrics: Return=+10.99% | Sharpe=0.506 | DD=7.77% | Turnover=49.05%
   🎚️ Intra-Step TAPE: potential=0.2298 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0756 | critic_loss=0.0262 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0131 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0421 | balance_loss=0.0004 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5058 | ema=0.2413 | best_ema=0.2413 | no_improve=0
   🔬 Alpha Diversity: mean=3.36 | std=0.73 | range=[0.89, 3.90] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.62 | PG=3.60 | XOM=3.59  BOT: MSFT=3.57 | JPM=3.56 | NVDA=3.56
   🎛️ Mixture Usage: C0=43.0% | C1=37.9% | C2=19.1%
   🧭 Regime Start Dist (train resets): high_vol=37 (33.0%), low_vol=37 (33.0%), medium_vol=38 (33.9%)
[CYCLE] Update 93/219 | Step 93,744/300,000 | Episode 108 | Time: 7475.1s
   📊 Metrics: Return=+28.57% | Sharpe=0.771 | DD=7.77% | Turnover=48.43%
   🎚️ Intra-Step TAPE: potential=0.2909 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0798 | critic_loss=0.0169 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0084 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0417 | balance_loss=0.0004 | separation_loss=0.0080 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7710 | ema=0.2943 | best_ema=0.2943 | no_improve=0
[CYCLE] Update 94/219 | Step 94,752/300,000 | Episode 108 | Time: 7551.1s
   📊 Metrics: Return=+34.22% | Sharpe=0.583 | DD=14.05% | Turnover=48.19%
   🎚️ Intra-Step TAPE: potential=0.2404 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0835 | critic_loss=0.0190 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0238 | balance_loss=0.0006 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5833 | ema=0.3232 | best_ema=0.3232 | no_improve=0
   🔬 Alpha Diversity: mean=3.15 | std=0.69 | range=[0.77, 3.77] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.39 | PG=3.36 | GLD=3.36  BOT: MSFT=3.33 | JPM=3.32 | NVDA=3.30
   🎛️ Mixture Usage: C0=46.2% | C1=38.6% | C2=15.2%
   🧭 Regime Start Dist (train resets): high_vol=37 (33.0%), low_vol=37 (33.0%), medium_vol=38 (33.9%)
[CYCLE] Update 95/219 | Step 95,760/300,000 | Episode 112 | Time: 7629.0s
   📊 Metrics: Return=+17.12% | Sharpe=0.201 | DD=28.87% | Turnover=48.97%
   🎚️ Intra-Step TAPE: potential=0.2381 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0824 | critic_loss=0.0283 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0141 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0170 | balance_loss=0.0006 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2005 | ema=0.3109 | best_ema=0.3109 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.02% / trig 25.00%) | terminal=0.000 (peak 0.008) | TAPE=0.2139
[CYCLE] Update 96/219 | Step 96,768/300,000 | Episode 112 | Time: 7707.8s
   📊 Metrics: Return=+30.02% | Sharpe=1.596 | DD=4.28% | Turnover=44.03%
   🎚️ Intra-Step TAPE: potential=0.7052 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0782 | critic_loss=0.0197 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0099 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0094 | balance_loss=0.0007 | separation_loss=0.0081 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5962 | ema=0.4394 | best_ema=0.4394 | no_improve=0
   🔬 Alpha Diversity: mean=3.09 | std=0.62 | range=[0.90, 3.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.33 | PG=3.30 | XOM=3.30  BOT: AMZN=3.24 | JPM=3.24 | NVDA=3.23
   🎛️ Mixture Usage: C0=42.3% | C1=41.0% | C2=16.8%
   🧭 Regime Start Dist (train resets): high_vol=39 (33.6%), low_vol=38 (32.8%), medium_vol=39 (33.6%)
[CYCLE] Update 97/219 | Step 97,776/300,000 | Episode 112 | Time: 7785.4s
   📊 Metrics: Return=+30.77% | Sharpe=0.832 | DD=9.67% | Turnover=43.75%
   🎚️ Intra-Step TAPE: potential=0.2206 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0754 | critic_loss=0.0165 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0082 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0079 | balance_loss=0.0007 | separation_loss=0.0082 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8322 | ema=0.4787 | best_ema=0.4787 | no_improve=0
[CYCLE] Update 98/219 | Step 98,784/300,000 | Episode 112 | Time: 7862.6s
   📊 Metrics: Return=+31.59% | Sharpe=0.525 | DD=20.26% | Turnover=43.20%
   🎚️ Intra-Step TAPE: potential=0.2415 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0781 | critic_loss=0.0171 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0085 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0229 | balance_loss=0.0006 | separation_loss=0.0081 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5250 | ema=0.4833 | best_ema=0.4833 | no_improve=0
   🔬 Alpha Diversity: mean=3.39 | std=0.78 | range=[0.58, 3.91] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.69 | PG=3.66 | XOM=3.66  BOT: JPM=3.61 | AMZN=3.60 | NVDA=3.58
   🎛️ Mixture Usage: C0=45.2% | C1=39.8% | C2=15.0%
   🧭 Regime Start Dist (train resets): high_vol=39 (33.6%), low_vol=38 (32.8%), medium_vol=39 (33.6%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00115_shp0p645_actor.weights.h5 (Sharpe=0.645, MDD=23.15%)
[CYCLE] Update 99/219 | Step 99,792/300,000 | Episode 116 | Time: 7940.0s
   📊 Metrics: Return=+32.40% | Sharpe=0.469 | DD=14.50% | Turnover=44.38%
   🎚️ Intra-Step TAPE: potential=0.2335 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0842 | critic_loss=0.0361 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0180 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0329 | balance_loss=0.0005 | separation_loss=0.0081 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4687 | ema=0.4819 | best_ema=0.4819 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.24% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2926
   [TOOL] Actor learning rate adjusted to 0.000020 at step 100,000
   [TOOL] Critic learning rate adjusted to 0.000120 at step 100,000
[CYCLE] Update 100/219 | Step 100,800/300,000 | Episode 116 | Time: 8017.6s
   📊 Metrics: Return=-1.80% | Sharpe=-0.227 | DD=10.13% | Turnover=40.25%
   🎚️ Intra-Step TAPE: potential=0.2399 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0827 | critic_loss=0.0207 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0104 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0256 | balance_loss=0.0006 | separation_loss=0.0082 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2267 | ema=0.4110 | best_ema=0.4110 | no_improve=0
   🔬 Alpha Diversity: mean=3.59 | std=0.73 | range=[0.66, 4.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.86 | PG=3.85 | XOM=3.84  BOT: NEE=3.78 | JPM=3.77 | AMZN=3.75
   🎛️ Mixture Usage: C0=41.5% | C1=43.4% | C2=15.2%
   🧭 Regime Start Dist (train resets): high_vol=40 (33.3%), low_vol=40 (33.3%), medium_vol=40 (33.3%)

📚 PPO ROLLOUT UPDATE at 100,800 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 100,800 steps:
   Batch size: 336

[DOWN] PPO GAMMA UPDATE at 100,800 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 100,800 steps:
   gae_lambda: 0.9500

🧪 AUX-RETURN COEF UPDATE at 100,800 steps:
   aux_return_pred_coef: 0.3000

🌡️ TEMPERATURE UPDATE at 100,800 steps:
   temperature: 0.9000
[CYCLE] Update 101/219 | Step 102,312/300,000 | Episode 116 | Time: 8141.2s
   📊 Metrics: Return=+17.10% | Sharpe=0.312 | DD=14.80% | Turnover=40.17%
   🎚️ Intra-Step TAPE: potential=0.2446 | delta_reward=-0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0769 | critic_loss=0.0216 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0136 | balance_loss=0.0006 | separation_loss=0.0080 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3125 | ema=0.4012 | best_ema=0.4110 | no_improve=1
[CYCLE] Update 102/219 | Step 103,824/300,000 | Episode 120 | Time: 8252.1s
   📊 Metrics: Return=+6.45% | Sharpe=0.026 | DD=15.72% | Turnover=39.29%
   🎚️ Intra-Step TAPE: potential=0.6620 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0830 | critic_loss=0.0194 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0097 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0090 | balance_loss=0.0007 | separation_loss=0.0079 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0264 | ema=0.3637 | best_ema=0.4110 | no_improve=2
   🔬 Alpha Diversity: mean=3.30 | std=0.79 | range=[0.53, 3.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=3.60 | JNJ=3.60 | GLD=3.57  BOT: JPM=3.51 | NVDA=3.48 | AMZN=3.48
   🎛️ Mixture Usage: C0=42.3% | C1=42.5% | C2=15.1%
   🧭 Regime Start Dist (train resets): high_vol=42 (33.9%), low_vol=42 (33.9%), medium_vol=40 (32.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.92% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2434
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00759) | SPY bonus=0.011 (SPY ret=0.00366)
[CYCLE] Update 103/219 | Step 105,336/300,000 | Episode 120 | Time: 8362.5s
   📊 Metrics: Return=+52.22% | Sharpe=1.830 | DD=7.46% | Turnover=40.36%
   🎚️ Intra-Step TAPE: potential=0.4140 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0776 | critic_loss=0.0121 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0187 | balance_loss=0.0006 | separation_loss=0.0080 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.8297 | ema=0.5103 | best_ema=0.5103 | no_improve=0
[CYCLE] Update 104/219 | Step 106,848/300,000 | Episode 120 | Time: 8471.1s
   📊 Metrics: Return=+44.70% | Sharpe=0.746 | DD=19.88% | Turnover=41.15%
   🎚️ Intra-Step TAPE: potential=0.2321 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0774 | critic_loss=0.0149 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0081 | balance_loss=0.0007 | separation_loss=0.0080 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7462 | ema=0.5339 | best_ema=0.5339 | no_improve=0
   🔬 Alpha Diversity: mean=3.18 | std=0.67 | range=[0.57, 3.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=3.43 | JNJ=3.43 | GLD=3.42  BOT: CAT=3.35 | AMZN=3.33 | NVDA=3.29
   🎛️ Mixture Usage: C0=44.6% | C1=42.0% | C2=13.4%
   🧭 Regime Start Dist (train resets): high_vol=42 (33.9%), low_vol=42 (33.9%), medium_vol=40 (32.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00121_shp0p858_actor.weights.h5 (Sharpe=0.858, MDD=19.88%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00123_shp0p909_actor.weights.h5 (Sharpe=0.909, MDD=20.49%)
[CYCLE] Update 105/219 | Step 108,360/300,000 | Episode 124 | Time: 8581.6s
   📊 Metrics: Return=+36.16% | Sharpe=0.524 | DD=19.71% | Turnover=41.57%
   🎚️ Intra-Step TAPE: potential=0.2396 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0800 | critic_loss=0.0270 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0135 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0192 | balance_loss=0.0006 | separation_loss=0.0081 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5236 | ema=0.5329 | best_ema=0.5339 | no_improve=1
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 10.54% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2927
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.02418) | SPY bonus=0.022 (SPY ret=-0.03007)
[CYCLE] Update 106/219 | Step 109,872/300,000 | Episode 124 | Time: 8689.9s
   📊 Metrics: Return=+5.93% | Sharpe=0.081 | DD=19.05% | Turnover=42.23%
   🎚️ Intra-Step TAPE: potential=0.7135 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0795 | critic_loss=0.0119 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0059 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0079 | balance_loss=0.0007 | separation_loss=0.0081 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0811 | ema=0.4877 | best_ema=0.5339 | no_improve=2
   🔬 Alpha Diversity: mean=3.23 | std=0.52 | range=[1.03, 3.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=3.44 | JNJ=3.43 | XOM=3.42  BOT: JPM=3.35 | AMZN=3.34 | NVDA=3.29
   🎛️ Mixture Usage: C0=41.3% | C1=43.2% | C2=15.5%
   🧭 Regime Start Dist (train resets): high_vol=44 (34.4%), low_vol=43 (33.6%), medium_vol=41 (32.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00126_shp0p777_actor.weights.h5 (Sharpe=0.777, MDD=16.68%)
[CYCLE] Update 107/219 | Step 111,384/300,000 | Episode 128 | Time: 8801.2s
   📊 Metrics: Return=+33.08% | Sharpe=0.464 | DD=23.74% | Turnover=42.90%
   🎚️ Intra-Step TAPE: potential=0.2297 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0701 | critic_loss=0.0251 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0016 | balance_loss=0.0007 | separation_loss=0.0081 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4639 | ema=0.4853 | best_ema=0.5339 | no_improve=3
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.98% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2660
[CYCLE] Update 108/219 | Step 112,896/300,000 | Episode 128 | Time: 8911.3s
   📊 Metrics: Return=-0.23% | Sharpe=-0.104 | DD=15.76% | Turnover=43.79%
   🎚️ Intra-Step TAPE: potential=0.7141 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0845 | critic_loss=0.0240 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0120 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=1.0036 | balance_loss=0.0007 | separation_loss=0.0081 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1040 | ema=0.4264 | best_ema=0.5339 | no_improve=4
   🔬 Alpha Diversity: mean=3.05 | std=0.48 | range=[1.09, 3.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=3.23 | JNJ=3.23 | XOM=3.22  BOT: NEE=3.17 | JPM=3.16 | AMZN=3.14
   🎛️ Mixture Usage: C0=42.1% | C1=42.4% | C2=15.5%
   🧭 Regime Start Dist (train resets): high_vol=44 (33.3%), low_vol=44 (33.3%), medium_vol=44 (33.3%)
[CYCLE] Update 109/219 | Step 114,408/300,000 | Episode 128 | Time: 9022.6s
   📊 Metrics: Return=+27.09% | Sharpe=0.542 | DD=15.76% | Turnover=44.30%
   🎚️ Intra-Step TAPE: potential=0.4964 | delta_reward=+0.0022
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0833 | critic_loss=0.0174 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0087 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9906 | balance_loss=0.0008 | separation_loss=0.0079 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5422 | ema=0.4380 | best_ema=0.5339 | no_improve=5
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00131_shp0p811_actor.weights.h5 (Sharpe=0.811, MDD=13.11%)
[CYCLE] Update 110/219 | Step 115,920/300,000 | Episode 132 | Time: 9139.9s
   📊 Metrics: Return=+28.88% | Sharpe=0.435 | DD=17.23% | Turnover=45.07%
   🎚️ Intra-Step TAPE: potential=0.2434 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0828 | critic_loss=0.0261 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0130 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9941 | balance_loss=0.0008 | separation_loss=0.0078 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4346 | ema=0.4376 | best_ema=0.5339 | no_improve=6
   🔬 Alpha Diversity: mean=2.80 | std=0.50 | range=[0.99, 3.18] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=2.99 | JNJ=2.99 | XOM=2.98  BOT: AMZN=2.94 | JPM=2.94 | NVDA=2.92
   🎛️ Mixture Usage: C0=41.1% | C1=43.9% | C2=15.0%
   🧭 Regime Start Dist (train resets): high_vol=45 (33.1%), low_vol=45 (33.1%), medium_vol=46 (33.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 5.49% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2823
[CYCLE] Update 111/219 | Step 117,432/300,000 | Episode 132 | Time: 9258.2s
   📊 Metrics: Return=-9.06% | Sharpe=-0.575 | DD=13.79% | Turnover=47.39%
   🎚️ Intra-Step TAPE: potential=0.2272 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0708 | critic_loss=0.0244 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0122 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9875 | balance_loss=0.0009 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.5754 | ema=0.3363 | best_ema=0.5339 | no_improve=7
[CYCLE] Update 112/219 | Step 118,944/300,000 | Episode 132 | Time: 9374.1s
   📊 Metrics: Return=-1.18% | Sharpe=-0.144 | DD=22.17% | Turnover=47.38%
   🎚️ Intra-Step TAPE: potential=0.2659 | delta_reward=-0.0020
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0759 | critic_loss=0.0132 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9823 | balance_loss=0.0009 | separation_loss=0.0078 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1435 | ema=0.2883 | best_ema=0.5339 | no_improve=8
   🔬 Alpha Diversity: mean=2.63 | std=0.54 | range=[0.74, 3.10] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.82 | GLD=2.81 | PG=2.81  BOT: NEE=2.77 | AMZN=2.76 | JPM=2.76
   🎛️ Mixture Usage: C0=40.3% | C1=46.8% | C2=12.9%
   🧭 Regime Start Dist (train resets): high_vol=45 (33.1%), low_vol=45 (33.1%), medium_vol=46 (33.8%)
[CYCLE] Update 113/219 | Step 120,456/300,000 | Episode 136 | Time: 9491.9s
   📊 Metrics: Return=+24.83% | Sharpe=0.381 | DD=17.91% | Turnover=47.81%
   🎚️ Intra-Step TAPE: potential=0.2532 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0816 | critic_loss=0.0199 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0099 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9766 | balance_loss=0.0009 | separation_loss=0.0078 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3809 | ema=0.2976 | best_ema=0.5339 | no_improve=9
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.54% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2716
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00669) | SPY bonus=0.014 (SPY ret=0.00176)
[CYCLE] Update 114/219 | Step 121,968/300,000 | Episode 136 | Time: 9610.1s
   📊 Metrics: Return=+34.33% | Sharpe=0.833 | DD=12.56% | Turnover=45.79%
   🎚️ Intra-Step TAPE: potential=0.6486 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0820 | critic_loss=0.0104 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0052 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=0.9629 | balance_loss=0.0010 | separation_loss=0.0078 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8331 | ema=0.3511 | best_ema=0.5339 | no_improve=10
   🔬 Alpha Diversity: mean=2.55 | std=0.61 | range=[0.56, 2.99] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.77 | GLD=2.77 | PG=2.75  BOT: NEE=2.72 | AMZN=2.72 | JPM=2.71
   🎛️ Mixture Usage: C0=39.6% | C1=48.3% | C2=12.1%
   🧭 Regime Start Dist (train resets): high_vol=46 (32.9%), low_vol=46 (32.9%), medium_vol=48 (34.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00138_shp0p663_actor.weights.h5 (Sharpe=0.663, MDD=19.60%)
[CYCLE] Update 115/219 | Step 123,480/300,000 | Episode 140 | Time: 9727.0s
   📊 Metrics: Return=+37.24% | Sharpe=0.416 | DD=26.14% | Turnover=46.67%
   🎚️ Intra-Step TAPE: potential=0.7153 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0782 | critic_loss=0.0244 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0122 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=0.9619 | balance_loss=0.0010 | separation_loss=0.0079 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4163 | ema=0.3577 | best_ema=0.5339 | no_improve=11
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2519
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00106) | SPY bonus=0.007 (SPY ret=-0.00024)
[CYCLE] Update 116/219 | Step 124,992/300,000 | Episode 140 | Time: 9843.2s
   📊 Metrics: Return=+49.75% | Sharpe=2.358 | DD=3.49% | Turnover=41.36%
   🎚️ Intra-Step TAPE: potential=0.7460 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0859 | critic_loss=0.0121 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=0.9750 | balance_loss=0.0010 | separation_loss=0.0080 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.3584 | ema=0.5577 | best_ema=0.5577 | no_improve=0
   🔬 Alpha Diversity: mean=2.81 | std=0.65 | range=[0.65, 3.16] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.06 | PG=3.03 | GLD=3.03  BOT: AMZN=2.99 | JPM=2.99 | NEE=2.99
   🎛️ Mixture Usage: C0=39.4% | C1=47.8% | C2=12.8%
   🧭 Regime Start Dist (train resets): high_vol=48 (33.3%), low_vol=48 (33.3%), medium_vol=48 (33.3%)
[CYCLE] Update 117/219 | Step 126,504/300,000 | Episode 140 | Time: 9954.2s
   📊 Metrics: Return=+47.65% | Sharpe=0.914 | DD=17.26% | Turnover=42.45%
   🎚️ Intra-Step TAPE: potential=0.2376 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0815 | critic_loss=0.0201 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0100 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9566 | balance_loss=0.0011 | separation_loss=0.0079 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9138 | ema=0.5933 | best_ema=0.5933 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00141_shp0p640_actor.weights.h5 (Sharpe=0.640, MDD=25.04%)
[CYCLE] Update 118/219 | Step 128,016/300,000 | Episode 144 | Time: 10070.0s
   📊 Metrics: Return=+38.35% | Sharpe=0.553 | DD=25.89% | Turnover=44.09%
   🎚️ Intra-Step TAPE: potential=0.2482 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0747 | critic_loss=0.0138 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0069 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9581 | balance_loss=0.0011 | separation_loss=0.0078 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5530 | ema=0.5893 | best_ema=0.5933 | no_improve=1
   🔬 Alpha Diversity: mean=2.53 | std=0.47 | range=[0.73, 2.87] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.70 | PG=2.68 | GLD=2.68  BOT: NEE=2.65 | JPM=2.65 | AMZN=2.64
   🎛️ Mixture Usage: C0=38.0% | C1=50.9% | C2=11.1%
   🧭 Regime Start Dist (train resets): high_vol=48 (32.4%), low_vol=50 (33.8%), medium_vol=50 (33.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.68% / trig 25.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2754
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.01060) | SPY bonus=0.001 (SPY ret=0.00862)
[CYCLE] Update 119/219 | Step 129,528/300,000 | Episode 144 | Time: 10183.2s
   📊 Metrics: Return=+16.59% | Sharpe=0.558 | DD=12.56% | Turnover=46.80%
   🎚️ Intra-Step TAPE: potential=0.5275 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0805 | critic_loss=0.0121 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9475 | balance_loss=0.0012 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5579 | ema=0.5862 | best_ema=0.5933 | no_improve=2
[CYCLE] Update 120/219 | Step 131,040/300,000 | Episode 144 | Time: 10294.1s
   📊 Metrics: Return=-4.33% | Sharpe=-0.158 | DD=23.65% | Turnover=47.58%
   🎚️ Intra-Step TAPE: potential=0.2004 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0808 | critic_loss=0.0105 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0053 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=0.9584 | balance_loss=0.0011 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1582 | ema=0.5117 | best_ema=0.5933 | no_improve=3
   🔬 Alpha Diversity: mean=2.62 | std=0.22 | range=[2.14, 3.84] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.60 | PG=2.59 | GLD=2.58  BOT: NEE=2.56 | AMZN=2.55 | JPM=2.55
   🎛️ Mixture Usage: C0=39.0% | C1=51.1% | C2=9.9%
   🧭 Regime Start Dist (train resets): high_vol=48 (32.4%), low_vol=50 (33.8%), medium_vol=50 (33.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 120 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 121/219 | Step 132,552/300,000 | Episode 148 | Time: 10403.9s
   📊 Metrics: Return=+27.67% | Sharpe=0.442 | DD=13.26% | Turnover=47.75%
   🎚️ Intra-Step TAPE: potential=0.2245 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0796 | critic_loss=0.0323 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0162 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9590 | balance_loss=0.0011 | separation_loss=0.0071 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4417 | ema=0.5047 | best_ema=0.5933 | no_improve=4
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.06% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2889
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.03983) | SPY bonus=0.025 (SPY ret=-0.04182)
[CYCLE] Update 122/219 | Step 134,064/300,000 | Episode 148 | Time: 10512.9s
   📊 Metrics: Return=+23.02% | Sharpe=0.666 | DD=7.23% | Turnover=47.50%
   🎚️ Intra-Step TAPE: potential=0.2473 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0821 | critic_loss=0.0100 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=0.9688 | balance_loss=0.0010 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6662 | ema=0.5209 | best_ema=0.5933 | no_improve=5
   🔬 Alpha Diversity: mean=2.80 | std=0.20 | range=[1.98, 3.30] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.84 | PG=2.83 | GLD=2.83  BOT: NEE=2.80 | JPM=2.79 | AMZN=2.79
   🎛️ Mixture Usage: C0=43.0% | C1=47.3% | C2=9.7%
   🧭 Regime Start Dist (train resets): high_vol=51 (33.6%), low_vol=51 (33.6%), medium_vol=50 (32.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 122 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 123/219 | Step 135,576/300,000 | Episode 152 | Time: 10620.5s
   📊 Metrics: Return=+15.43% | Sharpe=0.180 | DD=25.41% | Turnover=47.97%
   🎚️ Intra-Step TAPE: potential=0.2438 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0773 | critic_loss=0.0193 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0096 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9589 | balance_loss=0.0011 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1805 | ema=0.4868 | best_ema=0.5933 | no_improve=6
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.21% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2319
[CYCLE] Update 124/219 | Step 137,088/300,000 | Episode 152 | Time: 10730.2s
   📊 Metrics: Return=+5.85% | Sharpe=0.208 | DD=7.23% | Turnover=45.01%
   🎚️ Intra-Step TAPE: potential=0.4497 | delta_reward=+0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0895 | critic_loss=0.0132 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9656 | balance_loss=0.0010 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2081 | ema=0.4590 | best_ema=0.5933 | no_improve=7
   🔬 Alpha Diversity: mean=2.74 | std=0.35 | range=[1.40, 3.02] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.87 | NVDA=2.85 | PG=2.85  BOT: NEE=2.82 | JPM=2.81 | AMZN=2.80
   🎛️ Mixture Usage: C0=39.5% | C1=48.7% | C2=11.8%
   🧭 Regime Start Dist (train resets): high_vol=52 (33.3%), low_vol=52 (33.3%), medium_vol=52 (33.3%)
[CYCLE] Update 125/219 | Step 138,600/300,000 | Episode 152 | Time: 10841.1s
   📊 Metrics: Return=-1.82% | Sharpe=-0.189 | DD=18.53% | Turnover=45.39%
   🎚️ Intra-Step TAPE: potential=0.2876 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0753 | critic_loss=0.0113 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0057 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9677 | balance_loss=0.0010 | separation_loss=0.0075 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1892 | ema=0.3941 | best_ema=0.5933 | no_improve=8

📚 TURNOVER CURRICULUM UPDATE at 140,112 steps:
   Turnover penalty scalar: 0.2

🎛️ EXECUTION BETA UPDATE at 140,112 steps:
   action_execution_beta: 0.800 (w_exec=(1-β)w_prev + βw_raw)
[CYCLE] Update 126/219 | Step 140,112/300,000 | Episode 156 | Time: 10951.6s
   📊 Metrics: Return=+19.89% | Sharpe=0.271 | DD=21.25% | Turnover=45.57%
   🎚️ Intra-Step TAPE: potential=0.3448 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0790 | critic_loss=0.0128 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0064 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9696 | balance_loss=0.0010 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2712 | ema=0.3818 | best_ema=0.5933 | no_improve=9
   🔬 Alpha Diversity: mean=2.83 | std=0.32 | range=[1.45, 3.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.94 | NVDA=2.93 | MSFT=2.92  BOT: CAT=2.88 | AMZN=2.88 | JPM=2.87
   🎛️ Mixture Usage: C0=40.1% | C1=48.0% | C2=11.8%
   🧭 Regime Start Dist (train resets): high_vol=55 (34.4%), low_vol=52 (32.5%), medium_vol=53 (33.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.32% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2503
[CYCLE] Update 127/219 | Step 141,624/300,000 | Episode 156 | Time: 11062.1s
   📊 Metrics: Return=+23.12% | Sharpe=0.735 | DD=11.14% | Turnover=53.54%
   🎚️ Intra-Step TAPE: potential=0.6083 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0843 | critic_loss=0.0068 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9920 | balance_loss=0.0008 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7353 | ema=0.4172 | best_ema=0.5933 | no_improve=10
[CYCLE] Update 128/219 | Step 143,136/300,000 | Episode 156 | Time: 11171.8s
   📊 Metrics: Return=+25.95% | Sharpe=0.448 | DD=13.74% | Turnover=55.42%
   🎚️ Intra-Step TAPE: potential=0.2195 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0764 | critic_loss=0.0096 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0006 | balance_loss=0.0008 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4482 | ema=0.4203 | best_ema=0.5933 | no_improve=11
   🔬 Alpha Diversity: mean=3.27 | std=0.22 | range=[2.24, 3.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=3.33 | MSFT=3.32 | GLD=3.32  BOT: JPM=3.29 | CAT=3.29 | AMZN=3.28
   🎛️ Mixture Usage: C0=35.1% | C1=50.7% | C2=14.2%
   🧭 Regime Start Dist (train resets): high_vol=55 (34.4%), low_vol=52 (32.5%), medium_vol=53 (33.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 128 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 129/219 | Step 144,648/300,000 | Episode 160 | Time: 11280.9s
   📊 Metrics: Return=+7.96% | Sharpe=0.053 | DD=15.16% | Turnover=55.88%
   🎚️ Intra-Step TAPE: potential=0.2436 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0827 | critic_loss=0.0130 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0065 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0017
   🧩 Mixture Head: gate_entropy=1.0091 | balance_loss=0.0007 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0531 | ema=0.3836 | best_ema=0.5933 | no_improve=12
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 7.13% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2436
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.01514) | SPY bonus=0.009 (SPY ret=0.01044)
   🛑 Early-stop triggered: low_advantage_stagnation (|mean_adv|<=1.0e-04 for 30 updates) (step=144,648, update=129)

[OK] THREE-COMPONENT TAPE v3 training completed!
   🛑 Stop reason: low_advantage_stagnation (|mean_adv|<=1.0e-04 for 30 updates)
   Total episodes: 160
   Total timesteps: 144,648
   Training time: 11280.87s (188.01min)
📊 Training summary saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260314_150216_summary.csv
💾 Final models saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00160_shp0p053_actor.weights.h5, /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00160_shp0p053_critic.weights.h5
🎯 Default selected checkpoint: final high-watermark-style checkpoint
[OK] Training complete
checkpoint_prefix: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00160_shp0p053