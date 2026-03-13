[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4

================================================================================
EXPERIMENT 6: TCN_FUSION Enhanced + TAPE Three-Component
================================================================================
Architecture: TCN + Fusion
Results root: C:\Users\Owner\tcn_tape_vectorized_version_clean\tcn_fusion_results
Working dir: C:\Users\Owner\tcn_tape_vectorized_version_clean
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
   Train shape: (40593, 66)
   Test shape: (14230, 66)
   🧮 Actuarial columns: 4 detected (enabled=True) | total non-null=219292
      {'Actuarial_Expected_Recovery': 54823, 'Actuarial_Prob_30d': 54823, 'Actuarial_Prob_60d': 54823, 'Actuarial_Reserve_Severity': 54823}

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.35, band=±0.20, scalar=0.35 -> 0.55 => 0.75 => 0.90 => 1.00)
      ↳ Schedule: 0.35@0 => 0.55@100,000 => 0.75@200,000 => 0.90@300,000 => 1.00@400,000
   ⚙️  Component 4: Execution Inertia (beta=0.25 -> 0.35 => 0.45 => 0.50, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.25@0 => 0.35@100,000 => 0.45@200,000 => 0.50@350,000
   ⚡ Parallel rollout envs: 4
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 25.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🌊 DSR Regime Scaling: ENABLED | low_mult=0.3 (vol<0.12) | mid_mult=1.0 | high_mult=1.5 (vol>0.25)
   📈 Outperformance Bonus (SPY): ENABLED | scalar=3.0
   🔐 Lagrangian CVaR: ENABLED | threshold=-0.025 | lr=0.004 | lambda_max=5.0 | penalty_scale=5.0
   Tail-Aware Advantage: ENABLED | weight=0.1 | bottom_k=4
   Alpha Regularization: hhi_coef=0.01 | dispersion_coef=0.05 | target_std=0.07
   🧪 Aux Per-Asset Return Head: ENABLED | coef=0.25
   🔒 Dirichlet Alpha Cap: 16.0
   🔒 Drawdown dual controller (requested): target=15.00%, tolerance=-1.00% (trigger boundary ≈ 14.00%), lr=0.100, λ_init=0.10, λ_floor=0.00, λ_max=5.00, penalty_coef=2.50
   📐 Position constraints: max_single_asset=25%, min_cash=5%
   [DEBUG] Regime-balanced sampling: use_curriculum_learning=True, volatility_regime pre-existing=False
   🎲 Volatility regimes ready for sampling (computed):
      high_vol: 1345 dates (32.9%)
      low_vol: 1345 dates (32.9%)
      medium_vol: 1400 dates (34.2%)
   🧭 Regime start buckets (train env):
      high_vol: 1345 dates (32.9%)
      low_vol: 1345 dates (32.9%)
      medium_vol: 1400 dates (34.2%)
   [OK] Drawdown controller armed in env: target=15.00%, trigger=14.00%, λ_init=0.100, λ_floor=0.000, λ_max=5.00, penalty_coef=2.50
[OK] THREE-COMPONENT TAPE v3 Environments created:
   Training: 4090 days
   Parallel train env instances: 4
   Testing: 1423 days

🤖 Creating TCN_FUSION agent with Dirichlet distribution for Exp 6...
[OK] Agent created: PPOAgentTF
   [RAND] Dirichlet Distribution: ENABLED
   [TOOL] Actor LR schedule: 0.000030@0 => 0.000020@150,000 => 0.000010@350,000
   [TOOL] Critic LR schedule: 0.000150@0 => 0.000120@150,000 => 0.000100@350,000
   State dim: 437
   Action dim: 10
   Actor LR (configured): 3e-05
   Actor LR (active): 0.000030
   Critic LR (active): 0.000150
   🧱 TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Cross-Asset Mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Recurrent memory: enabled=False | units=64 | dropout=0.1
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
   🌡️ Temperature schedule: 1.2000@0 => 1.0000@150,000 => 0.9000@300,000
   📐 PPO rollout schedule: 1008@0 => 1512@150,000 => 2016@300,000
   🧺 PPO batch-size schedule: 252@0 => 336@150,000 => 504@300,000
📊 Training metrics will stream to C:\Users\Owner\tcn_tape_vectorized_version_clean\tcn_fusion_results\logs\Exp6_TCN_FUSION_Enhanced_TAPE_training_20260312_142920_episodes.csv
🧪 Step diagnostics will stream to C:\Users\Owner\tcn_tape_vectorized_version_clean\tcn_fusion_results\logs\Exp6_TCN_FUSION_Enhanced_TAPE_training_20260312_142920_step_diagnostics.csv

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
      0+ steps: scalar=0.35
      100,000+ steps: scalar=0.55
      200,000+ steps: scalar=0.75
      300,000+ steps: scalar=0.90
      400,000+ steps: scalar=1.00
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.25
      100,000+ steps: beta=0.35
      200,000+ steps: beta=0.45
      350,000+ steps: beta=0.50
   🏆 Deterministic-validation checkpoints: enabled (every 5 episodes | mode=mean | min_sharpe=0.50 | min_delta=0.000 | alpha_diag=True | horizon=scheduled (0@756 => 100,000@1008 => 250,000@1500 => 400,000@full))
      ↳ Multi-horizon selector: enabled (252:0.35, 504:0.30, 756:0.20, 1008:0.15) | dd_penalty_coef=0.250
      ↳ Stochastic sanity gate: enabled (runs=5, horizon=252, min_mean_sharpe=0.20, max_std=1.00)
      ↳ SPY outperformance gate: enabled (required>0.00% over the same validation horizon)
   🧷 Legacy checkpoint routes: disabled (high-watermark/step/periodic/tape/rare)
   [OK] Checkpoint selector default: deterministic validation multi-horizon composite score
   💾 High-watermark checkpoints: disabled
[RCPT] Active feature manifest saved: C:\Users\Owner\tcn_tape_vectorized_version_clean\tcn_fusion_results\logs\Exp6_TCN_FUSION_Enhanced_TAPE_training_20260312_142920_active_feature_manifest.json
[RCPT] Training metadata saved: C:\Users\Owner\tcn_tape_vectorized_version_clean\tcn_fusion_results\logs\Exp6_TCN_FUSION_Enhanced_TAPE_training_20260312_142920_metadata.json
[CYCLE] Update 1/348 | Step 1,008/500,000 | Episode 0 | Time: 425.4s
   📊 Metrics: Return=+1.90% | Sharpe=0.102 | DD=15.37% | Turnover=10.04%
   🎚️ Intra-Step TAPE: potential=0.4651 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1233 | critic_loss=0.3347 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1673 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01521
[CYCLE] Update 2/348 | Step 2,016/500,000 | Episode 0 | Time: 826.9s
   📊 Metrics: Return=+9.72% | Sharpe=0.239 | DD=15.37% | Turnover=10.06%
   🎚️ Intra-Step TAPE: potential=0.6295 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1065 | critic_loss=0.1967 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0983 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.61 | std=0.66 | range=[0.57, 4.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=3.10 | NVDA=3.00 | AMZN=2.94  BOT: MSFT=2.62 | JNJ=2.41 | NEE=2.27
   🧭 Regime Start Dist (train resets): high_vol=1 (25.0%), low_vol=2 (50.0%), medium_vol=1 (25.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01537
[CYCLE] Update 3/348 | Step 3,024/500,000 | Episode 4 | Time: 1226.0s
   📊 Metrics: Return=+58.92% | Sharpe=1.048 | DD=12.60% | Turnover=11.13%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0985 | critic_loss=0.2636 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1318 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.100) | TAPE=0.5328
[CYCLE] Update 4/348 | Step 4,032/500,000 | Episode 4 | Time: 1652.0s
   📊 Metrics: Return=-23.72% | Sharpe=-0.541 | DD=40.59% | Turnover=13.13%
   🎚️ Intra-Step TAPE: potential=0.2358 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0873 | critic_loss=0.3086 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1543 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.08 | std=0.43 | range=[0.69, 3.73] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.43 | NVDA=2.40 | CAT=2.40  BOT: PG=1.99 | JNJ=1.87 | NEE=1.83
   🧭 Regime Start Dist (train resets): high_vol=3 (37.5%), low_vol=4 (50.0%), medium_vol=1 (12.5%)
   🔐 Lagrangian CVaR: λ=0.0061 | penalty=-0.0001 | rolling_cvar=-0.01851
[CYCLE] Update 5/348 | Step 5,040/500,000 | Episode 4 | Time: 2068.8s
   📊 Metrics: Return=+12.50% | Sharpe=0.281 | DD=40.59% | Turnover=12.98%
   🎚️ Intra-Step TAPE: potential=0.2503 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0872 | critic_loss=0.1669 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0835 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0161 | penalty=-0.0004 | rolling_cvar=-0.02246
      🧪 Deterministic validation: Sharpe=0.916 | Return=+104.74% | DD=26.48%
         Multi-horizon: score=0.870 | details=252:0.873/26.5%, 504:1.175/26.5%, 756:0.701/26.5%, 1008:0.916/26.5%
         SPY relative: spy_return=+53.67% | outperformance=+51.07%
         Stochastic sanity: mean_sharpe=0.579 | std=0.525 | runs=5
      💾 Deterministic-validation checkpoint saved: C:\Users\Owner\tcn_tape_vectorized_version_clean\tcn_fusion_results\high_watermark_checkpoints\exp6_tape_hw_ep00005_shp0p916_actor.weights.h5 (val_sharpe=0.916, score=0.870)
[CYCLE] Update 6/348 | Step 6,048/500,000 | Episode 8 | Time: 3928.2s
   📊 Metrics: Return=+11.15% | Sharpe=0.190 | DD=46.31% | Turnover=13.62%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0812 | critic_loss=0.3068 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1534 | risk_aux_total=0.0001 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0001 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.59 | std=0.32 | range=[0.96, 4.18] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.87 | JPM=1.66 | CAT=1.60  BOT: MSFT=1.47 | JNJ=1.42 | NEE=1.39
   🧭 Regime Start Dist (train resets): high_vol=6 (50.0%), low_vol=4 (33.3%), medium_vol=2 (16.7%)
   🔒 Drawdown λ snapshot=0.592 (peak 0.592, dd 0.00% / trig 14.00%) | terminal=4.206 (peak 4.206) | TAPE=0.2397
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00975) | SPY bonus=0.011 (SPY ret=-0.01356)
   🔐 Lagrangian CVaR: λ=0.0277 | penalty=-0.0007 | rolling_cvar=-0.03954