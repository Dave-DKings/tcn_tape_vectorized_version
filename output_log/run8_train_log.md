[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
num_parallel_envs: 4
[OK] Actuarial feature check passed: {'Actuarial_Reserve_Severity': 54703, 'Actuarial_Expected_Recovery': 54703, 'Actuarial_Prob_60d': 54703, 'Actuarial_Prob_30d': 54703}
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
   Train shape: (40473, 62)
   Test shape: (14230, 62)
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
   📐 Position constraints: max_single_asset=25%, min_cash=5%
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
   State dim: 433
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
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260311_054205_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260311_054205_step_diagnostics.csv

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
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260311_054205_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260311_054205_metadata.json
[CYCLE] Update 1/348 | Step 1,008/500,000 | Episode 0 | Time: 57.2s
   📊 Metrics: Return=-0.59% | Sharpe=-0.028 | DD=15.67% | Turnover=21.71%
   🎚️ Intra-Step TAPE: potential=0.3801 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0129 | critic_loss=1.2797 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6398 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 2/348 | Step 2,016/500,000 | Episode 0 | Time: 112.6s
   📊 Metrics: Return=+6.72% | Sharpe=0.159 | DD=15.67% | Turnover=26.08%
   🎚️ Intra-Step TAPE: potential=0.5601 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0101 | critic_loss=0.7000 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3500 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.67 | std=0.58 | range=[0.59, 3.55]
   🏷️ Alpha Per-Asset  TOP: XOM=2.06 | GLD=2.04 | JNJ=2.01  BOT: CAT=1.43 | MSFT=1.42 | NVDA=1.25
   🧭 Regime Start Dist (train resets): high_vol=1 (25.0%), low_vol=2 (50.0%), medium_vol=1 (25.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp0p931_actor.weights.h5 (Sharpe=0.931, MDD=9.93%)
[CYCLE] Update 3/348 | Step 3,024/500,000 | Episode 4 | Time: 168.8s
   📊 Metrics: Return=+33.43% | Sharpe=0.617 | DD=16.09% | Turnover=35.36%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0115 | critic_loss=1.4532 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7266 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.250) | TAPE=0.3433
   📊 Episode CVaR: regime=mid | CVaR=-0.02028 | threshold=-0.01700 | passed=❌ | bonus=-0.33
[CYCLE] Update 4/348 | Step 4,032/500,000 | Episode 4 | Time: 224.9s
   📊 Metrics: Return=-26.86% | Sharpe=-0.519 | DD=44.65% | Turnover=47.07%
   🎚️ Intra-Step TAPE: potential=0.2387 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0043 | critic_loss=1.4963 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7482 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.59 | std=0.40 | range=[0.33, 4.76]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.91 | AMZN=0.82 | CAT=0.61  BOT: JNJ=0.48 | NEE=0.47 | PG=0.46
   🧭 Regime Start Dist (train resets): high_vol=3 (37.5%), low_vol=4 (50.0%), medium_vol=1 (12.5%)
[CYCLE] Update 5/348 | Step 5,040/500,000 | Episode 4 | Time: 280.0s
   📊 Metrics: Return=+5.89% | Sharpe=0.202 | DD=44.65% | Turnover=49.85%
   🎚️ Intra-Step TAPE: potential=0.2194 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0109 | critic_loss=0.6448 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3224 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 6/348 | Step 6,048/500,000 | Episode 8 | Time: 335.7s
   📊 Metrics: Return=-3.23% | Sharpe=-0.007 | DD=42.05% | Turnover=52.99%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0093 | critic_loss=1.1027 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5514 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.56 | std=0.27 | range=[0.33, 2.95]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.94 | GLD=0.64 | JPM=0.60  BOT: AMZN=0.47 | CAT=0.47 | PG=0.44
   🧭 Regime Start Dist (train resets): high_vol=6 (50.0%), low_vol=4 (33.3%), medium_vol=2 (16.7%)
   🔒 Drawdown λ snapshot=0.349 (peak 0.349, dd 0.00% / trig 21.00%) | terminal=0.420 (peak 0.420) | TAPE=0.2147
   📊 Episode CVaR: regime=mid | CVaR=-0.03593 | threshold=-0.01700 | passed=❌ | bonus=-1.89
[CYCLE] Update 7/348 | Step 7,056/500,000 | Episode 8 | Time: 391.7s
   📊 Metrics: Return=-25.29% | Sharpe=-0.438 | DD=46.73% | Turnover=45.69%
   🎚️ Intra-Step TAPE: potential=0.5623 | delta_reward=-0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0110 | critic_loss=1.0252 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5126 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 8/348 | Step 8,064/500,000 | Episode 8 | Time: 448.0s
   📊 Metrics: Return=-18.41% | Sharpe=-0.172 | DD=46.73% | Turnover=48.00%
   🎚️ Intra-Step TAPE: potential=0.2277 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0067 | critic_loss=0.6295 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3147 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.91 | std=0.33 | range=[0.41, 2.62]
   🏷️ Alpha Per-Asset  TOP: XOM=1.08 | GLD=1.03 | NVDA=0.99  BOT: CAT=0.83 | PG=0.82 | AMZN=0.72
   🧭 Regime Start Dist (train resets): high_vol=6 (50.0%), low_vol=4 (33.3%), medium_vol=2 (16.7%)
[CYCLE] Update 9/348 | Step 9,072/500,000 | Episode 12 | Time: 502.5s
   📊 Metrics: Return=+14.47% | Sharpe=0.233 | DD=17.75% | Turnover=48.48%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0121 | critic_loss=0.8948 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4474 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=1.099 (peak 1.099, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.315) | TAPE=0.2480
   📊 Episode CVaR: regime=mid | CVaR=-0.02548 | threshold=-0.01700 | passed=❌ | bonus=-0.85
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 557.1s
   📊 Metrics: Return=-2.41% | Sharpe=-0.413 | DD=11.05% | Turnover=42.96%
   🎚️ Intra-Step TAPE: potential=0.2383 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0104 | critic_loss=0.7747 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3873 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.06 | std=0.61 | range=[0.40, 5.74]
   🏷️ Alpha Per-Asset  TOP: GLD=1.63 | NVDA=1.58 | AMZN=1.20  BOT: MSFT=0.84 | NEE=0.84 | PG=0.76
   🧭 Regime Start Dist (train resets): high_vol=6 (37.5%), low_vol=4 (25.0%), medium_vol=6 (37.5%)
[CYCLE] Update 11/348 | Step 11,088/500,000 | Episode 12 | Time: 611.5s
   📊 Metrics: Return=-10.91% | Sharpe=-0.596 | DD=21.53% | Turnover=43.91%
   🎚️ Intra-Step TAPE: potential=0.6464 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0058 | critic_loss=0.8128 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4064 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 12/348 | Step 12,096/500,000 | Episode 16 | Time: 666.2s
   📊 Metrics: Return=-12.17% | Sharpe=-0.297 | DD=22.60% | Turnover=49.13%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0126 | critic_loss=0.9447 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4724 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.34 | std=0.10 | range=[0.26, 1.17]
   🏷️ Alpha Per-Asset  TOP: GLD=0.44 | AMZN=0.39 | CAT=0.38  BOT: JNJ=0.29 | NEE=0.29 | JPM=0.29
   🧭 Regime Start Dist (train resets): high_vol=9 (45.0%), low_vol=4 (20.0%), medium_vol=7 (35.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 12 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.002) | TAPE=0.2150
   📊 Episode CVaR: regime=mid | CVaR=-0.02571 | threshold=-0.01700 | passed=❌ | bonus=-0.87
[CYCLE] Update 13/348 | Step 13,104/500,000 | Episode 16 | Time: 721.1s
   📊 Metrics: Return=-39.19% | Sharpe=-0.992 | DD=46.49% | Turnover=56.58%
   🎚️ Intra-Step TAPE: potential=0.2185 | delta_reward=-0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0065 | critic_loss=1.1801 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5901 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 14/348 | Step 14,112/500,000 | Episode 16 | Time: 775.8s
   📊 Metrics: Return=-18.01% | Sharpe=-0.158 | DD=46.49% | Turnover=59.18%
   🎚️ Intra-Step TAPE: potential=0.2012 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0096 | critic_loss=0.3913 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1957 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.31 | std=0.07 | range=[0.25, 0.77]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.39 | AMZN=0.33 | JPM=0.32  BOT: NEE=0.29 | JNJ=0.28 | PG=0.28
   🧭 Regime Start Dist (train resets): high_vol=9 (45.0%), low_vol=4 (20.0%), medium_vol=7 (35.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 14 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 15/348 | Step 15,120/500,000 | Episode 20 | Time: 829.8s
   📊 Metrics: Return=+20.87% | Sharpe=0.359 | DD=13.92% | Turnover=61.53%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0079 | critic_loss=0.4031 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2016 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=2.059 (peak 2.059, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2661
   📊 Episode CVaR: regime=mid | CVaR=-0.02261 | threshold=-0.01700 | passed=❌ | bonus=-0.56
[CYCLE] Update 16/348 | Step 16,128/500,000 | Episode 20 | Time: 885.1s
   📊 Metrics: Return=-2.40% | Sharpe=-0.205 | DD=18.85% | Turnover=58.46%
   🎚️ Intra-Step TAPE: potential=0.2226 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0097 | critic_loss=0.4550 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2275 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.35 | std=0.11 | range=[0.26, 1.29]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.45 | GLD=0.41 | AMZN=0.38  BOT: JPM=0.31 | NEE=0.31 | JNJ=0.30
   🧭 Regime Start Dist (train resets): high_vol=10 (41.7%), low_vol=6 (25.0%), medium_vol=8 (33.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 16 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 17/348 | Step 17,136/500,000 | Episode 20 | Time: 941.4s
   📊 Metrics: Return=-0.15% | Sharpe=-0.075 | DD=18.85% | Turnover=58.49%
   🎚️ Intra-Step TAPE: potential=0.2340 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0110 | critic_loss=0.5129 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2565 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 18/348 | Step 18,144/500,000 | Episode 24 | Time: 997.4s
   📊 Metrics: Return=+16.52% | Sharpe=0.300 | DD=23.66% | Turnover=60.71%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0090 | critic_loss=0.8240 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4120 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.33 | std=0.14 | range=[0.25, 1.47]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.48 | AMZN=0.40 | CAT=0.35  BOT: PG=0.29 | JPM=0.27 | NEE=0.27
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=9 (32.1%), medium_vol=9 (32.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 18 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.003) | TAPE=0.2298
   📊 Episode CVaR: regime=mid | CVaR=-0.02191 | threshold=-0.01700 | passed=❌ | bonus=-0.49
[CYCLE] Update 19/348 | Step 19,152/500,000 | Episode 24 | Time: 1052.2s
   📊 Metrics: Return=-4.73% | Sharpe=-0.520 | DD=11.86% | Turnover=61.11%
   🎚️ Intra-Step TAPE: potential=0.2340 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0098 | critic_loss=0.3288 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1644 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1107.6s
   📊 Metrics: Return=+7.69% | Sharpe=0.192 | DD=17.07% | Turnover=61.51%
   🎚️ Intra-Step TAPE: potential=0.6886 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0072 | critic_loss=0.5761 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2880 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.37 | std=0.23 | range=[0.25, 3.10]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.63 | AMZN=0.43 | CAT=0.42  BOT: PG=0.30 | NEE=0.28 | JNJ=0.28
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=9 (32.1%), medium_vol=9 (32.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 20 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 21/348 | Step 21,168/500,000 | Episode 28 | Time: 1162.9s
   📊 Metrics: Return=-4.93% | Sharpe=0.051 | DD=55.99% | Turnover=54.06%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0010 | critic_loss=0.4031 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2015 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2177
   📊 Episode CVaR: regime=high | CVaR=-0.04828 | threshold=-0.02400 | passed=❌ | bonus=-2.43
[CYCLE] Update 22/348 | Step 22,176/500,000 | Episode 28 | Time: 1218.3s
   📊 Metrics: Return=+20.43% | Sharpe=1.087 | DD=11.30% | Turnover=56.93%
   🎚️ Intra-Step TAPE: potential=0.7141 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0115 | critic_loss=0.3074 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1537 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.55 | std=0.49 | range=[0.25, 3.83]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.97 | AMZN=0.92 | JPM=0.68  BOT: PG=0.34 | GLD=0.34 | JNJ=0.32
   🧭 Regime Start Dist (train resets): high_vol=11 (34.4%), low_vol=11 (34.4%), medium_vol=10 (31.2%)
[CYCLE] Update 23/348 | Step 23,184/500,000 | Episode 28 | Time: 1273.1s
   📊 Metrics: Return=+40.64% | Sharpe=1.118 | DD=11.30% | Turnover=57.23%
   🎚️ Intra-Step TAPE: potential=0.7369 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0102 | critic_loss=0.1646 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0823 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00029_shp0p844_actor.weights.h5 (Sharpe=0.844, MDD=12.03%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p709_actor.weights.h5 (Sharpe=0.709, MDD=15.87%)
[CYCLE] Update 24/348 | Step 24,192/500,000 | Episode 32 | Time: 1328.3s
   📊 Metrics: Return=+45.80% | Sharpe=0.709 | DD=15.87% | Turnover=52.75%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0011 | critic_loss=0.4430 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2215 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.54 | std=0.41 | range=[0.25, 3.18]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.04 | JPM=0.69 | AMZN=0.65  BOT: JNJ=0.36 | PG=0.36 | GLD=0.35
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=14 (38.9%), medium_vol=10 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.495 (peak 3.750) | TAPE=0.3917
   📊 Episode CVaR: regime=mid | CVaR=-0.02303 | threshold=-0.01700 | passed=❌ | bonus=-0.60
[CYCLE] Update 25/348 | Step 25,200/500,000 | Episode 32 | Time: 1384.4s
   📊 Metrics: Return=+20.14% | Sharpe=1.616 | DD=3.96% | Turnover=61.19%
   🎚️ Intra-Step TAPE: potential=0.2831 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0132 | critic_loss=0.1106 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0553 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 26/348 | Step 26,208/500,000 | Episode 32 | Time: 1439.8s
   📊 Metrics: Return=+28.91% | Sharpe=0.977 | DD=9.88% | Turnover=61.27%
   🎚️ Intra-Step TAPE: potential=0.2174 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0098 | critic_loss=0.1855 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0928 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.34 | std=0.11 | range=[0.25, 1.09]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.44 | CAT=0.41 | GLD=0.37  BOT: PG=0.29 | JNJ=0.28 | NEE=0.28
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=14 (38.9%), medium_vol=10 (27.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 26 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 27/348 | Step 27,216/500,000 | Episode 36 | Time: 1494.7s
   📊 Metrics: Return=-1.32% | Sharpe=-0.123 | DD=15.10% | Turnover=59.05%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0086 | critic_loss=0.3294 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1647 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.371) | TAPE=0.2277
   📊 Episode CVaR: regime=mid | CVaR=-0.01897 | threshold=-0.01700 | passed=❌ | bonus=-0.20
[CYCLE] Update 28/348 | Step 28,224/500,000 | Episode 36 | Time: 1550.0s
   📊 Metrics: Return=-35.10% | Sharpe=-0.776 | DD=52.61% | Turnover=43.70%
   🎚️ Intra-Step TAPE: potential=0.4911 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0070 | critic_loss=0.4180 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2090 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.87 | std=0.57 | range=[0.30, 4.62]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.12 | GLD=1.04 | AMZN=1.02  BOT: NEE=0.79 | JNJ=0.64 | PG=0.64
   🧭 Regime Start Dist (train resets): high_vol=14 (35.0%), low_vol=15 (37.5%), medium_vol=11 (27.5%)
[CYCLE] Update 29/348 | Step 29,232/500,000 | Episode 36 | Time: 1605.6s
   📊 Metrics: Return=-21.26% | Sharpe=-0.242 | DD=52.61% | Turnover=46.96%
   🎚️ Intra-Step TAPE: potential=0.5647 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0120 | critic_loss=0.1383 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0691 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 1660.5s
   📊 Metrics: Return=-0.27% | Sharpe=-0.095 | DD=12.05% | Turnover=46.68%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0112 | critic_loss=0.1094 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0547 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.73 | std=0.50 | range=[0.31, 5.10]
   🏷️ Alpha Per-Asset  TOP: GLD=1.24 | NVDA=0.83 | XOM=0.77  BOT: PG=0.57 | JNJ=0.57 | AMZN=0.55
   🧭 Regime Start Dist (train resets): high_vol=14 (31.8%), low_vol=18 (40.9%), medium_vol=12 (27.3%)
   🔒 Drawdown λ snapshot=3.750 (peak 3.750, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2426
   📊 Episode CVaR: regime=mid | CVaR=-0.01810 | threshold=-0.01700 | passed=❌ | bonus=-0.11
[CYCLE] Update 31/348 | Step 31,248/500,000 | Episode 40 | Time: 1715.7s
   📊 Metrics: Return=+11.78% | Sharpe=0.610 | DD=12.39% | Turnover=53.85%
   🎚️ Intra-Step TAPE: potential=0.2264 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0115 | critic_loss=0.0732 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0366 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 32/348 | Step 32,256/500,000 | Episode 40 | Time: 1771.7s
   📊 Metrics: Return=-19.71% | Sharpe=-0.277 | DD=47.55% | Turnover=50.63%
   🎚️ Intra-Step TAPE: potential=0.2412 | delta_reward=-0.0024
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0059 | critic_loss=0.2654 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1327 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.77 | std=0.40 | range=[0.27, 2.45]
   🏷️ Alpha Per-Asset  TOP: CAT=0.90 | NVDA=0.85 | XOM=0.84  BOT: JPM=0.64 | JNJ=0.62 | AMZN=0.61
   🧭 Regime Start Dist (train resets): high_vol=14 (31.8%), low_vol=18 (40.9%), medium_vol=12 (27.3%)
[CYCLE] Update 33/348 | Step 33,264/500,000 | Episode 44 | Time: 1827.4s
   📊 Metrics: Return=-21.21% | Sharpe=-0.207 | DD=45.48% | Turnover=51.80%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0083 | critic_loss=0.0664 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0332 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=3.748 (peak 3.748, dd 0.00% / trig 21.00%) | terminal=3.081 (peak 3.081) | TAPE=0.2109
   📊 Episode CVaR: regime=high | CVaR=-0.04199 | threshold=-0.02400 | passed=❌ | bonus=-1.80
[CYCLE] Update 34/348 | Step 34,272/500,000 | Episode 44 | Time: 1883.2s
   📊 Metrics: Return=-3.41% | Sharpe=-0.337 | DD=14.64% | Turnover=57.72%
   🎚️ Intra-Step TAPE: potential=0.2213 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0076 | critic_loss=0.1307 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0653 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.48 | std=0.26 | range=[0.26, 2.29]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.68 | JPM=0.51 | AMZN=0.50  BOT: GLD=0.43 | NEE=0.43 | JNJ=0.41
   🧭 Regime Start Dist (train resets): high_vol=16 (33.3%), low_vol=19 (39.6%), medium_vol=13 (27.1%)
[CYCLE] Update 35/348 | Step 35,280/500,000 | Episode 44 | Time: 1939.0s
   📊 Metrics: Return=-1.30% | Sharpe=-0.160 | DD=14.64% | Turnover=58.47%
   🎚️ Intra-Step TAPE: potential=0.3736 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0145 | critic_loss=0.1071 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0535 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 36/348 | Step 36,288/500,000 | Episode 48 | Time: 1995.6s
   📊 Metrics: Return=-12.25% | Sharpe=-0.091 | DD=40.40% | Turnover=57.05%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0102 | critic_loss=0.0996 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0498 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.36 | std=0.15 | range=[0.25, 1.62]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.50 | GLD=0.46 | AMZN=0.44  BOT: MSFT=0.31 | PG=0.30 | JNJ=0.30
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=21 (40.4%), medium_vol=14 (26.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 36 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.814 (peak 0.814, dd 0.00% / trig 21.00%) | terminal=2.380 (peak 3.234) | TAPE=0.2091
   📊 Episode CVaR: regime=high | CVaR=-0.04295 | threshold=-0.02400 | passed=❌ | bonus=-1.89
[CYCLE] Update 37/348 | Step 37,296/500,000 | Episode 48 | Time: 2053.0s
   📊 Metrics: Return=-5.19% | Sharpe=-0.589 | DD=10.38% | Turnover=60.86%
   🎚️ Intra-Step TAPE: potential=0.2181 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0113 | critic_loss=0.0981 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0491 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 38/348 | Step 38,304/500,000 | Episode 48 | Time: 2109.6s
   📊 Metrics: Return=-0.60% | Sharpe=-0.157 | DD=11.61% | Turnover=60.46%
   🎚️ Intra-Step TAPE: potential=0.2450 | delta_reward=-0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0200 | critic_loss=0.0807 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0403 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.34 | std=0.14 | range=[0.24, 1.66]
   🏷️ Alpha Per-Asset  TOP: AMZN=0.39 | NVDA=0.37 | CAT=0.36  BOT: PG=0.31 | NEE=0.30 | JNJ=0.30
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=21 (40.4%), medium_vol=14 (26.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 38 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 39/348 | Step 39,312/500,000 | Episode 52 | Time: 2167.2s
   📊 Metrics: Return=+9.35% | Sharpe=0.144 | DD=24.22% | Turnover=59.55%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0106 | critic_loss=0.0999 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0499 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.001 (peak 0.001, dd 0.00% / trig 21.00%) | terminal=0.009 (peak 1.785) | TAPE=0.2274
   📊 Episode CVaR: regime=mid | CVaR=-0.02471 | threshold=-0.01700 | passed=❌ | bonus=-0.77
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 2224.2s
   📊 Metrics: Return=+2.64% | Sharpe=0.123 | DD=19.95% | Turnover=40.76%
   🎚️ Intra-Step TAPE: potential=0.7309 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0110 | critic_loss=0.1340 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0670 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.12 | std=1.09 | range=[0.71, 8.37]
   🏷️ Alpha Per-Asset  TOP: AMZN=2.63 | NVDA=2.58 | JPM=2.21  BOT: NEE=1.88 | PG=1.83 | JNJ=1.71
   🧭 Regime Start Dist (train resets): high_vol=19 (33.9%), low_vol=21 (37.5%), medium_vol=16 (28.6%)
[CYCLE] Update 41/348 | Step 41,328/500,000 | Episode 52 | Time: 2281.2s
   📊 Metrics: Return=+17.36% | Sharpe=0.474 | DD=19.95% | Turnover=36.07%
   🎚️ Intra-Step TAPE: potential=0.2564 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0115 | critic_loss=0.0895 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0447 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 42/348 | Step 42,336/500,000 | Episode 56 | Time: 2337.7s
   📊 Metrics: Return=+2.97% | Sharpe=-0.024 | DD=15.31% | Turnover=34.12%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0128 | critic_loss=0.0951 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0475 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.34 | std=1.41 | range=[1.10, 10.60]
   🏷️ Alpha Per-Asset  TOP: GLD=3.80 | XOM=3.69 | JPM=3.62  BOT: MSFT=3.22 | PG=2.86 | JNJ=2.64
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=21 (35.0%), medium_vol=19 (31.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.007) | TAPE=0.2414
   📊 Episode CVaR: regime=low | CVaR=-0.01704 | threshold=-0.01200 | passed=❌ | bonus=-0.50
[CYCLE] Update 43/348 | Step 43,344/500,000 | Episode 56 | Time: 2394.6s
   📊 Metrics: Return=-3.16% | Sharpe=-0.127 | DD=19.91% | Turnover=28.66%
   🎚️ Intra-Step TAPE: potential=0.6138 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0103 | critic_loss=0.1710 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0855 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 44/348 | Step 44,352/500,000 | Episode 56 | Time: 2451.1s
   📊 Metrics: Return=-3.71% | Sharpe=-0.126 | DD=19.91% | Turnover=29.96%
   🎚️ Intra-Step TAPE: potential=0.2566 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0090 | critic_loss=0.1497 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0749 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.14 | std=0.91 | range=[0.79, 7.23]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.61 | GLD=2.57 | JPM=2.44  BOT: PG=1.84 | MSFT=1.80 | JNJ=1.77
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=21 (35.0%), medium_vol=19 (31.7%)
[CYCLE] Update 45/348 | Step 45,360/500,000 | Episode 60 | Time: 2507.0s
   📊 Metrics: Return=+15.64% | Sharpe=0.256 | DD=19.49% | Turnover=34.17%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0103 | critic_loss=0.1945 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0973 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2515
   📊 Episode CVaR: regime=mid | CVaR=-0.02473 | threshold=-0.01700 | passed=❌ | bonus=-0.77
[CYCLE] Update 46/348 | Step 46,368/500,000 | Episode 60 | Time: 2562.9s
   📊 Metrics: Return=+9.96% | Sharpe=0.488 | DD=19.95% | Turnover=55.79%
   🎚️ Intra-Step TAPE: potential=0.2227 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0142 | critic_loss=0.2231 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1115 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.49 | std=0.18 | range=[0.29, 2.26]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.60 | CAT=0.56 | AMZN=0.55  BOT: MSFT=0.44 | PG=0.43 | JNJ=0.41
   🧭 Regime Start Dist (train resets): high_vol=22 (34.4%), low_vol=23 (35.9%), medium_vol=19 (29.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 46 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 47/348 | Step 47,376/500,000 | Episode 60 | Time: 2618.9s
   📊 Metrics: Return=+18.89% | Sharpe=0.475 | DD=23.18% | Turnover=56.50%
   🎚️ Intra-Step TAPE: potential=0.2225 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0060 | critic_loss=0.5315 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2658 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 48/348 | Step 48,384/500,000 | Episode 64 | Time: 2674.7s
   📊 Metrics: Return=-17.99% | Sharpe=-0.116 | DD=57.60% | Turnover=54.65%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0008 | critic_loss=0.5838 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2919 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.31 | std=0.08 | range=[0.24, 0.90]
   🏷️ Alpha Per-Asset  TOP: JPM=0.40 | NVDA=0.40 | CAT=0.34  BOT: GLD=0.27 | PG=0.26 | JNJ=0.26
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=24 (35.3%), medium_vol=21 (30.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 48 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2089
   📊 Episode CVaR: regime=high | CVaR=-0.04744 | threshold=-0.02400 | passed=❌ | bonus=-2.34
[CYCLE] Update 49/348 | Step 49,392/500,000 | Episode 64 | Time: 2730.7s
   📊 Metrics: Return=+9.39% | Sharpe=0.641 | DD=8.72% | Turnover=62.01%
   🎚️ Intra-Step TAPE: potential=0.5495 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0201 | critic_loss=0.1534 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0767 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 2787.1s
   📊 Metrics: Return=+10.31% | Sharpe=0.317 | DD=8.72% | Turnover=61.75%
   🎚️ Intra-Step TAPE: potential=0.4634 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0124 | critic_loss=0.1743 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0872 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.30 | std=0.07 | range=[0.24, 0.83]
   🏷️ Alpha Per-Asset  TOP: GLD=0.36 | AMZN=0.36 | NVDA=0.35  BOT: PG=0.26 | JNJ=0.25 | NEE=0.25
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=24 (35.3%), medium_vol=21 (30.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 50 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 51/348 | Step 51,408/500,000 | Episode 68 | Time: 2842.5s
   📊 Metrics: Return=-0.21% | Sharpe=-0.092 | DD=25.02% | Turnover=62.60%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0097 | critic_loss=0.1034 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0517 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=2.061 (peak 3.750) | TAPE=0.2109
   📊 Episode CVaR: regime=mid | CVaR=-0.01894 | threshold=-0.01700 | passed=❌ | bonus=-0.19
[CYCLE] Update 52/348 | Step 52,416/500,000 | Episode 68 | Time: 2898.9s
   📊 Metrics: Return=-3.40% | Sharpe=-0.235 | DD=19.65% | Turnover=55.57%
   🎚️ Intra-Step TAPE: potential=0.5474 | delta_reward=+0.0021
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0036 | critic_loss=0.0540 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0270 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.71 | std=0.43 | range=[0.29, 3.10]
   🏷️ Alpha Per-Asset  TOP: GLD=1.40 | AMZN=0.91 | NVDA=0.89  BOT: NEE=0.50 | PG=0.50 | JNJ=0.48
   🧭 Regime Start Dist (train resets): high_vol=23 (31.9%), low_vol=27 (37.5%), medium_vol=22 (30.6%)
[CYCLE] Update 53/348 | Step 53,424/500,000 | Episode 68 | Time: 2955.4s
   📊 Metrics: Return=-17.53% | Sharpe=-0.471 | DD=25.48% | Turnover=53.47%
   🎚️ Intra-Step TAPE: potential=0.2350 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0133 | critic_loss=0.0592 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0296 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 54/348 | Step 54,432/500,000 | Episode 72 | Time: 3011.7s
   📊 Metrics: Return=-5.01% | Sharpe=-0.257 | DD=12.60% | Turnover=48.84%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0096 | critic_loss=0.1307 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0653 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.67 | std=0.47 | range=[0.28, 3.57]
   🏷️ Alpha Per-Asset  TOP: GLD=1.52 | NVDA=1.03 | AMZN=0.82  BOT: PG=0.38 | NEE=0.38 | JNJ=0.36
   🧭 Regime Start Dist (train resets): high_vol=25 (32.9%), low_vol=29 (38.2%), medium_vol=22 (28.9%)
   🔒 Drawdown λ snapshot=0.062 (peak 0.062, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 1.546) | TAPE=0.2346
   📊 Episode CVaR: regime=low | CVaR=-0.01615 | threshold=-0.01200 | passed=❌ | bonus=-0.41
[CYCLE] Update 55/348 | Step 55,440/500,000 | Episode 72 | Time: 3067.7s
   📊 Metrics: Return=-2.99% | Sharpe=-0.238 | DD=14.98% | Turnover=47.38%
   🎚️ Intra-Step TAPE: potential=0.4951 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0117 | critic_loss=0.0994 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0497 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 56/348 | Step 56,448/500,000 | Episode 72 | Time: 3124.3s
   📊 Metrics: Return=+28.20% | Sharpe=0.698 | DD=14.98% | Turnover=45.45%
   🎚️ Intra-Step TAPE: potential=0.3655 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0109 | critic_loss=0.0381 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0190 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.06 | std=0.73 | range=[0.32, 4.41]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.29 | AMZN=1.49 | CAT=1.24  BOT: MSFT=0.74 | JNJ=0.55 | PG=0.53
   🧭 Regime Start Dist (train resets): high_vol=25 (32.9%), low_vol=29 (38.2%), medium_vol=22 (28.9%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00075_shp1p195_actor.weights.h5 (Sharpe=1.195, MDD=9.51%)
[CYCLE] Update 57/348 | Step 57,456/500,000 | Episode 76 | Time: 3180.4s
   📊 Metrics: Return=-6.54% | Sharpe=-0.103 | DD=26.67% | Turnover=44.64%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0111 | critic_loss=0.0720 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0360 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.308 (peak 0.308, dd 0.00% / trig 21.00%) | terminal=0.095 (peak 0.120) | TAPE=0.2129
   📊 Episode CVaR: regime=mid | CVaR=-0.03045 | threshold=-0.01700 | passed=❌ | bonus=-1.35
[CYCLE] Update 58/348 | Step 58,464/500,000 | Episode 76 | Time: 3236.9s
   📊 Metrics: Return=+18.04% | Sharpe=0.866 | DD=14.40% | Turnover=33.22%
   🎚️ Intra-Step TAPE: potential=0.6896 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0071 | critic_loss=0.1248 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0624 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.67 | std=1.17 | range=[0.40, 6.19]
   🏷️ Alpha Per-Asset  TOP: NVDA=3.61 | AMZN=2.24 | JPM=2.08  BOT: GLD=1.13 | JNJ=0.78 | PG=0.74
   🧭 Regime Start Dist (train resets): high_vol=28 (35.0%), low_vol=30 (37.5%), medium_vol=22 (27.5%)
[CYCLE] Update 59/348 | Step 59,472/500,000 | Episode 76 | Time: 3292.8s
   📊 Metrics: Return=+18.38% | Sharpe=0.401 | DD=30.14% | Turnover=36.44%
   🎚️ Intra-Step TAPE: potential=0.2605 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0101 | critic_loss=0.1028 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0514 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 3348.6s
   📊 Metrics: Return=+15.11% | Sharpe=0.239 | DD=24.29% | Turnover=39.36%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0093 | critic_loss=0.1543 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0771 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.02 | std=0.56 | range=[0.34, 3.64]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.87 | JPM=1.26 | GLD=1.22  BOT: NEE=0.68 | PG=0.62 | JNJ=0.56
   🧭 Regime Start Dist (train resets): high_vol=31 (36.9%), low_vol=30 (35.7%), medium_vol=23 (27.4%)
   🔒 Drawdown λ snapshot=3.750 (peak 3.750, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.071) | TAPE=0.2423
   📊 Episode CVaR: regime=mid | CVaR=-0.02770 | threshold=-0.01700 | passed=❌ | bonus=-1.07
[CYCLE] Update 61/348 | Step 61,488/500,000 | Episode 80 | Time: 3404.9s
   📊 Metrics: Return=+10.92% | Sharpe=0.533 | DD=12.08% | Turnover=44.26%
   🎚️ Intra-Step TAPE: potential=0.6155 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0149 | critic_loss=0.0557 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0278 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 62/348 | Step 62,496/500,000 | Episode 80 | Time: 3462.0s
   📊 Metrics: Return=-0.28% | Sharpe=-0.055 | DD=13.05% | Turnover=48.28%
   🎚️ Intra-Step TAPE: potential=0.2385 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0113 | critic_loss=0.0467 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0233 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.69 | std=0.30 | range=[0.33, 2.04]
   🏷️ Alpha Per-Asset  TOP: GLD=1.05 | NVDA=0.96 | AMZN=0.92  BOT: PG=0.45 | NEE=0.44 | JNJ=0.43
   🧭 Regime Start Dist (train resets): high_vol=31 (36.9%), low_vol=30 (35.7%), medium_vol=23 (27.4%)
[CYCLE] Update 63/348 | Step 63,504/500,000 | Episode 84 | Time: 3519.0s
   📊 Metrics: Return=+4.78% | Sharpe=0.063 | DD=24.15% | Turnover=48.84%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0112 | critic_loss=0.1544 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0772 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.916 (peak 0.916, dd 0.00% / trig 21.00%) | terminal=0.022 (peak 0.029) | TAPE=0.2250
   📊 Episode CVaR: regime=mid | CVaR=-0.02620 | threshold=-0.01700 | passed=❌ | bonus=-0.92
[CYCLE] Update 64/348 | Step 64,512/500,000 | Episode 84 | Time: 3576.0s
   📊 Metrics: Return=-6.49% | Sharpe=-0.254 | DD=22.55% | Turnover=46.55%
   🎚️ Intra-Step TAPE: potential=0.7021 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0075 | critic_loss=0.0554 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0277 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.68 | std=0.37 | range=[0.29, 2.21]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.08 | AMZN=1.07 | GLD=0.90  BOT: NEE=0.48 | JNJ=0.41 | PG=0.40
   🧭 Regime Start Dist (train resets): high_vol=33 (37.5%), low_vol=31 (35.2%), medium_vol=24 (27.3%)
[CYCLE] Update 65/348 | Step 65,520/500,000 | Episode 84 | Time: 3632.8s
   📊 Metrics: Return=-15.08% | Sharpe=-0.428 | DD=26.23% | Turnover=48.84%
   🎚️ Intra-Step TAPE: potential=0.2493 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0083 | critic_loss=0.0666 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0333 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 66/348 | Step 66,528/500,000 | Episode 88 | Time: 3688.4s
   📊 Metrics: Return=-4.75% | Sharpe=-0.253 | DD=14.38% | Turnover=50.31%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0119 | critic_loss=0.0336 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0168 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.50 | std=0.19 | range=[0.28, 1.31]
   🏷️ Alpha Per-Asset  TOP: GLD=0.75 | NVDA=0.67 | AMZN=0.57  BOT: PG=0.38 | NEE=0.38 | JNJ=0.37
   🧭 Regime Start Dist (train resets): high_vol=35 (38.0%), low_vol=33 (35.9%), medium_vol=24 (26.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 66 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.333 (peak 0.333, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.016) | TAPE=0.2290
   📊 Episode CVaR: regime=low | CVaR=-0.01681 | threshold=-0.01200 | passed=❌ | bonus=-0.48
[CYCLE] Update 67/348 | Step 67,536/500,000 | Episode 88 | Time: 3744.6s
   📊 Metrics: Return=-5.93% | Sharpe=-0.356 | DD=21.88% | Turnover=56.44%
   🎚️ Intra-Step TAPE: potential=0.7353 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0091 | critic_loss=0.0532 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0266 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 68/348 | Step 68,544/500,000 | Episode 88 | Time: 3800.5s
   📊 Metrics: Return=-10.31% | Sharpe=-0.281 | DD=21.88% | Turnover=56.67%
   🎚️ Intra-Step TAPE: potential=0.2224 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0112 | critic_loss=0.0401 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0201 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.60 | std=0.17 | range=[0.36, 1.40]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.81 | AMZN=0.77 | GLD=0.71  BOT: NEE=0.50 | JNJ=0.46 | PG=0.46
   🧭 Regime Start Dist (train resets): high_vol=35 (38.0%), low_vol=33 (35.9%), medium_vol=24 (26.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 68 updates. TCN may not be learning asset discrimination.
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00090_shp0p982_actor.weights.h5 (Sharpe=0.982, MDD=11.54%)
[CYCLE] Update 69/348 | Step 69,552/500,000 | Episode 92 | Time: 3856.1s
   📊 Metrics: Return=-30.17% | Sharpe=-0.335 | DD=54.14% | Turnover=53.62%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0091 | critic_loss=0.0677 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0338 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=3.621 (peak 3.621) | TAPE=0.2073
   📊 Episode CVaR: regime=high | CVaR=-0.04342 | threshold=-0.02400 | passed=❌ | bonus=-1.94
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 3911.3s
   📊 Metrics: Return=+18.80% | Sharpe=1.237 | DD=11.26% | Turnover=50.34%
   🎚️ Intra-Step TAPE: potential=0.7072 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0090 | critic_loss=0.0357 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0178 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.75 | std=0.21 | range=[0.38, 1.63]
   🏷️ Alpha Per-Asset  TOP: GLD=0.94 | NVDA=0.90 | AMZN=0.82  BOT: PG=0.63 | NEE=0.61 | JNJ=0.56
   🧭 Regime Start Dist (train resets): high_vol=38 (39.6%), low_vol=33 (34.4%), medium_vol=25 (26.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 70 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 71/348 | Step 71,568/500,000 | Episode 92 | Time: 3967.4s
   📊 Metrics: Return=+42.92% | Sharpe=1.398 | DD=11.26% | Turnover=51.06%
   🎚️ Intra-Step TAPE: potential=0.6187 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0133 | critic_loss=0.0252 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0126 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00093_shp0p972_actor.weights.h5 (Sharpe=0.972, MDD=11.26%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00095_shp0p736_actor.weights.h5 (Sharpe=0.736, MDD=12.36%)
[CYCLE] Update 72/348 | Step 72,576/500,000 | Episode 96 | Time: 4023.5s
   📊 Metrics: Return=-0.88% | Sharpe=0.066 | DD=34.42% | Turnover=51.83%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0105 | critic_loss=0.0265 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0133 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.67 | std=0.28 | range=[0.33, 2.01]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.18 | GLD=0.75 | CAT=0.73  BOT: JNJ=0.51 | NEE=0.49 | PG=0.49
   🧭 Regime Start Dist (train resets): high_vol=40 (40.0%), low_vol=34 (34.0%), medium_vol=26 (26.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.935 (peak 2.949) | TAPE=0.2174
   📊 Episode CVaR: regime=high | CVaR=-0.04451 | threshold=-0.02400 | passed=❌ | bonus=-2.05
[CYCLE] Update 73/348 | Step 73,584/500,000 | Episode 96 | Time: 4079.5s
   📊 Metrics: Return=+2.02% | Sharpe=0.061 | DD=7.56% | Turnover=47.90%
   🎚️ Intra-Step TAPE: potential=0.3424 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0113 | critic_loss=0.0381 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0191 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 74/348 | Step 74,592/500,000 | Episode 96 | Time: 4135.0s
   📊 Metrics: Return=+0.22% | Sharpe=-0.105 | DD=9.76% | Turnover=47.23%
   🎚️ Intra-Step TAPE: potential=0.2354 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0125 | critic_loss=0.0291 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0146 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.78 | std=0.44 | range=[0.33, 3.09]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.26 | GLD=1.25 | AMZN=1.04  BOT: NEE=0.48 | PG=0.46 | JNJ=0.44
   🧭 Regime Start Dist (train resets): high_vol=40 (40.0%), low_vol=34 (34.0%), medium_vol=26 (26.0%)
[CYCLE] Update 75/348 | Step 75,600/500,000 | Episode 100 | Time: 4190.3s
   📊 Metrics: Return=-1.38% | Sharpe=-0.095 | DD=16.10% | Turnover=46.52%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0055 | critic_loss=0.0877 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0439 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.701) | TAPE=0.2381
   📊 Episode CVaR: regime=mid | CVaR=-0.02050 | threshold=-0.01700 | passed=❌ | bonus=-0.35
[CYCLE] Update 76/348 | Step 76,608/500,000 | Episode 100 | Time: 4245.6s
   📊 Metrics: Return=+13.54% | Sharpe=0.995 | DD=5.36% | Turnover=41.75%
   🎚️ Intra-Step TAPE: potential=0.2773 | delta_reward=-0.0021
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0064 | critic_loss=0.0434 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0217 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.23 | std=0.88 | range=[0.38, 5.07]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.64 | AMZN=2.18 | JPM=1.28  BOT: NEE=0.78 | PG=0.62 | JNJ=0.58
   🧭 Regime Start Dist (train resets): high_vol=40 (38.5%), low_vol=36 (34.6%), medium_vol=28 (26.9%)
[CYCLE] Update 77/348 | Step 77,616/500,000 | Episode 100 | Time: 4300.8s
   📊 Metrics: Return=+9.83% | Sharpe=0.294 | DD=11.57% | Turnover=40.94%
   🎚️ Intra-Step TAPE: potential=0.2341 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0084 | critic_loss=0.0530 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0265 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00104_shp0p725_actor.weights.h5 (Sharpe=0.725, MDD=17.21%)
[CYCLE] Update 78/348 | Step 78,624/500,000 | Episode 104 | Time: 4356.0s
   📊 Metrics: Return=+49.72% | Sharpe=0.725 | DD=17.21% | Turnover=36.68%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0122 | critic_loss=0.0383 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0192 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.47 | std=1.18 | range=[0.78, 7.29]
   🏷️ Alpha Per-Asset  TOP: AMZN=3.94 | NVDA=3.65 | CAT=2.86  BOT: NEE=1.73 | PG=1.53 | JNJ=1.39
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=36 (33.3%), medium_vol=30 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3962
   📊 Episode CVaR: regime=mid | CVaR=-0.02508 | threshold=-0.01700 | passed=❌ | bonus=-0.81
[CYCLE] Update 79/348 | Step 79,632/500,000 | Episode 104 | Time: 4411.6s
   📊 Metrics: Return=+4.85% | Sharpe=0.241 | DD=22.25% | Turnover=31.47%
   🎚️ Intra-Step TAPE: potential=0.2448 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0072 | critic_loss=0.0685 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0342 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 4467.6s
   📊 Metrics: Return=+14.74% | Sharpe=0.383 | DD=22.25% | Turnover=33.53%
   🎚️ Intra-Step TAPE: potential=0.2183 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0113 | critic_loss=0.0758 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0379 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.87 | std=0.79 | range=[0.68, 5.06]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.97 | AMZN=2.69 | CAT=2.32  BOT: NEE=1.24 | JNJ=1.08 | PG=1.00
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=36 (33.3%), medium_vol=30 (27.8%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00105_shp0p883_actor.weights.h5 (Sharpe=0.883, MDD=22.25%)
[CYCLE] Update 81/348 | Step 81,648/500,000 | Episode 108 | Time: 4523.2s
   📊 Metrics: Return=+5.44% | Sharpe=0.081 | DD=24.60% | Turnover=34.76%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0111 | critic_loss=0.1874 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0937 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.024) | TAPE=0.2253
   📊 Episode CVaR: regime=mid | CVaR=-0.02775 | threshold=-0.01700 | passed=❌ | bonus=-1.07
[CYCLE] Update 82/348 | Step 82,656/500,000 | Episode 108 | Time: 4579.4s
   📊 Metrics: Return=+23.34% | Sharpe=1.754 | DD=5.04% | Turnover=40.58%
   🎚️ Intra-Step TAPE: potential=0.3233 | delta_reward=-0.0027
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0083 | critic_loss=0.0880 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0440 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.22 | std=0.53 | range=[0.55, 3.15]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.27 | GLD=1.78 | JPM=1.28  BOT: MSFT=0.89 | PG=0.79 | JNJ=0.78
   🧭 Regime Start Dist (train resets): high_vol=43 (38.4%), low_vol=39 (34.8%), medium_vol=30 (26.8%)
[CYCLE] Update 83/348 | Step 83,664/500,000 | Episode 108 | Time: 4634.9s
   📊 Metrics: Return=+45.54% | Sharpe=1.436 | DD=10.07% | Turnover=43.15%
   🎚️ Intra-Step TAPE: potential=0.2300 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0120 | critic_loss=0.2578 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1289 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00109_shp0p728_actor.weights.h5 (Sharpe=0.728, MDD=22.21%)
[CYCLE] Update 84/348 | Step 84,672/500,000 | Episode 112 | Time: 4689.6s
   📊 Metrics: Return=+9.76% | Sharpe=0.155 | DD=12.70% | Turnover=42.81%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0101 | critic_loss=0.7018 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3509 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.21 | std=0.43 | range=[0.53, 2.81]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.79 | AMZN=1.55 | GLD=1.51  BOT: JPM=0.94 | PG=0.91 | NEE=0.74
   🧭 Regime Start Dist (train resets): high_vol=45 (38.8%), low_vol=40 (34.5%), medium_vol=31 (26.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2496
   📊 Episode CVaR: regime=low | CVaR=-0.01618 | threshold=-0.01200 | passed=❌ | bonus=-0.42
[CYCLE] Update 85/348 | Step 85,680/500,000 | Episode 112 | Time: 4745.4s
   📊 Metrics: Return=+6.93% | Sharpe=0.344 | DD=22.45% | Turnover=43.94%
   🎚️ Intra-Step TAPE: potential=0.3155 | delta_reward=-0.0023
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0086 | critic_loss=0.0858 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0429 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 86/348 | Step 86,688/500,000 | Episode 112 | Time: 4801.6s
   📊 Metrics: Return=+1.22% | Sharpe=0.034 | DD=24.26% | Turnover=44.32%
   🎚️ Intra-Step TAPE: potential=0.6033 | delta_reward=+0.0018
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0071 | critic_loss=0.0692 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0346 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.17 | std=0.36 | range=[0.62, 2.77]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.68 | GLD=1.47 | AMZN=1.41  BOT: NEE=0.94 | JNJ=0.88 | PG=0.85
   🧭 Regime Start Dist (train resets): high_vol=45 (38.8%), low_vol=40 (34.5%), medium_vol=31 (26.7%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00114_shp1p209_actor.weights.h5 (Sharpe=1.209, MDD=11.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00115_shp1p263_actor.weights.h5 (Sharpe=1.263, MDD=13.30%)
[CYCLE] Update 87/348 | Step 87,696/500,000 | Episode 116 | Time: 4857.8s
   📊 Metrics: Return=+27.81% | Sharpe=0.543 | DD=15.22% | Turnover=43.92%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0085 | critic_loss=0.0823 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0411 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.148 (peak 0.148, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3181
   📊 Episode CVaR: regime=mid | CVaR=-0.01890 | threshold=-0.01700 | passed=❌ | bonus=-0.19
[CYCLE] Update 88/348 | Step 88,704/500,000 | Episode 116 | Time: 4914.1s
   📊 Metrics: Return=-12.19% | Sharpe=-0.577 | DD=23.70% | Turnover=43.47%
   🎚️ Intra-Step TAPE: potential=0.2799 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0095 | critic_loss=0.0904 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0452 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.12 | std=0.31 | range=[0.57, 2.88]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.44 | AMZN=1.29 | CAT=1.23  BOT: GLD=1.00 | JNJ=0.94 | PG=0.94
   🧭 Regime Start Dist (train resets): high_vol=47 (39.2%), low_vol=42 (35.0%), medium_vol=31 (25.8%)
[CYCLE] Update 89/348 | Step 89,712/500,000 | Episode 116 | Time: 4969.6s
   📊 Metrics: Return=-11.72% | Sharpe=-0.369 | DD=23.70% | Turnover=45.74%
   🎚️ Intra-Step TAPE: potential=0.3819 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0097 | critic_loss=0.0848 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0424 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 5024.6s
   📊 Metrics: Return=-0.43% | Sharpe=-0.042 | DD=20.84% | Turnover=47.58%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0109 | critic_loss=0.0940 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0470 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.65 | std=0.10 | range=[0.46, 1.06]
   🏷️ Alpha Per-Asset  TOP: GLD=0.75 | AMZN=0.71 | NVDA=0.69  BOT: NEE=0.59 | JNJ=0.58 | PG=0.58
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=42 (33.9%), medium_vol=34 (27.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 90 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2248
   📊 Episode CVaR: regime=mid | CVaR=-0.02505 | threshold=-0.01700 | passed=❌ | bonus=-0.81

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps
[CYCLE] Update 91/348 | Step 91,728/500,000 | Episode 120 | Time: 5080.1s
   📊 Metrics: Return=+16.27% | Sharpe=1.373 | DD=4.81% | Turnover=53.04%
   🎚️ Intra-Step TAPE: potential=0.2407 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0071 | critic_loss=0.0595 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0297 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps
[CYCLE] Update 92/348 | Step 92,736/500,000 | Episode 120 | Time: 5136.3s
   📊 Metrics: Return=+31.06% | Sharpe=1.100 | DD=9.91% | Turnover=54.17%
   🎚️ Intra-Step TAPE: potential=0.2119 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0051 | critic_loss=0.0564 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0282 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.62 | std=0.11 | range=[0.39, 1.48]
   🏷️ Alpha Per-Asset  TOP: AMZN=0.71 | NVDA=0.69 | GLD=0.65  BOT: MSFT=0.59 | PG=0.54 | JNJ=0.53
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=42 (33.9%), medium_vol=34 (27.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 92 updates. TCN may not be learning asset discrimination.

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps
[CYCLE] Update 93/348 | Step 93,744/500,000 | Episode 120 | Time: 5192.0s
   📊 Metrics: Return=+33.31% | Sharpe=0.634 | DD=19.48% | Turnover=52.49%
   🎚️ Intra-Step TAPE: potential=0.6159 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0086 | critic_loss=0.0717 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0359 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps
[CYCLE] Update 94/348 | Step 94,752/500,000 | Episode 124 | Time: 5247.9s
   📊 Metrics: Return=-10.97% | Sharpe=-0.081 | DD=44.30% | Turnover=51.88%
   🎚️ Intra-Step TAPE: potential=0.5915 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0074 | critic_loss=0.0457 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0229 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.07 | std=0.26 | range=[0.64, 2.98]
   🏷️ Alpha Per-Asset  TOP: AMZN=1.27 | NVDA=1.21 | GLD=1.17  BOT: NEE=0.99 | PG=0.89 | JNJ=0.89
   🧭 Regime Start Dist (train resets): high_vol=50 (39.1%), low_vol=43 (33.6%), medium_vol=35 (27.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.10% / trig 21.00%) | terminal=1.552 (peak 1.552) | TAPE=0.2151
   📊 Episode CVaR: regime=high | CVaR=-0.03910 | threshold=-0.02400 | passed=❌ | bonus=-1.51

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps
[CYCLE] Update 95/348 | Step 95,760/500,000 | Episode 124 | Time: 5303.5s
   📊 Metrics: Return=-23.82% | Sharpe=-0.540 | DD=43.38% | Turnover=45.84%
   🎚️ Intra-Step TAPE: potential=0.2125 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0093 | critic_loss=0.0330 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0165 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps
[CYCLE] Update 96/348 | Step 96,768/500,000 | Episode 124 | Time: 5359.1s
   📊 Metrics: Return=-2.72% | Sharpe=0.054 | DD=49.69% | Turnover=44.78%
   🎚️ Intra-Step TAPE: potential=0.4288 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0108 | critic_loss=0.0251 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.05 | std=0.23 | range=[0.61, 2.49]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.28 | AMZN=1.24 | JPM=1.12  BOT: NEE=0.91 | PG=0.88 | JNJ=0.86
   🧭 Regime Start Dist (train resets): high_vol=50 (39.1%), low_vol=43 (33.6%), medium_vol=35 (27.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 96 updates. TCN may not be learning asset discrimination.

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps
[CYCLE] Update 97/348 | Step 97,776/500,000 | Episode 124 | Time: 5415.1s
   📊 Metrics: Return=+1.25% | Sharpe=0.078 | DD=49.69% | Turnover=45.63%
   🎚️ Intra-Step TAPE: potential=0.6927 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0090 | critic_loss=0.0282 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0141 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00128_shp0p711_actor.weights.h5 (Sharpe=0.711, MDD=15.51%)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps
[CYCLE] Update 98/348 | Step 98,784/500,000 | Episode 128 | Time: 5470.7s
   📊 Metrics: Return=+46.92% | Sharpe=0.711 | DD=15.51% | Turnover=45.76%
   🎚️ Intra-Step TAPE: potential=0.7423 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0067 | critic_loss=0.1417 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0709 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.90 | std=0.33 | range=[0.47, 3.25]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.21 | AMZN=1.20 | CAT=1.06  BOT: MSFT=0.79 | JNJ=0.67 | PG=0.66
   🧭 Regime Start Dist (train resets): high_vol=51 (38.6%), low_vol=45 (34.1%), medium_vol=36 (27.3%)
   🔒 Drawdown λ snapshot=1.988 (peak 2.600, dd 1.06% / trig 21.00%) | terminal=0.000 (peak 1.164) | TAPE=0.3776
   📊 Episode CVaR: regime=mid | CVaR=-0.01834 | threshold=-0.01700 | passed=❌ | bonus=-0.13

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps
[CYCLE] Update 99/348 | Step 99,792/500,000 | Episode 128 | Time: 5526.4s
   📊 Metrics: Return=-4.14% | Sharpe=-0.122 | DD=19.51% | Turnover=48.87%
   🎚️ Intra-Step TAPE: potential=0.2383 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0088 | critic_loss=0.0977 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0488 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.5

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 5582.0s
   📊 Metrics: Return=-3.78% | Sharpe=-0.106 | DD=20.28% | Turnover=49.13%
   🎚️ Intra-Step TAPE: potential=0.4807 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0062 | critic_loss=0.0477 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0238 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.78 | std=0.13 | range=[0.52, 1.20]
   🏷️ Alpha Per-Asset  TOP: JPM=0.90 | NVDA=0.85 | AMZN=0.84  BOT: NEE=0.72 | JNJ=0.70 | PG=0.69
   🧭 Regime Start Dist (train resets): high_vol=51 (38.6%), low_vol=45 (34.1%), medium_vol=36 (27.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 100 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 101/348 | Step 101,808/500,000 | Episode 128 | Time: 5638.5s
   📊 Metrics: Return=-4.65% | Sharpe=-0.123 | DD=20.28% | Turnover=50.04%
   🎚️ Intra-Step TAPE: potential=0.2553 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0082 | critic_loss=0.0403 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0202 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 102/348 | Step 102,816/500,000 | Episode 132 | Time: 5694.9s
   📊 Metrics: Return=-11.19% | Sharpe=-0.266 | DD=16.82% | Turnover=50.16%
   🎚️ Intra-Step TAPE: potential=0.7204 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0074 | critic_loss=0.0912 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0456 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.58 | std=0.14 | range=[0.37, 1.91]
   🏷️ Alpha Per-Asset  TOP: NVDA=0.73 | AMZN=0.71 | CAT=0.61  BOT: NEE=0.51 | JNJ=0.48 | PG=0.47
   🧭 Regime Start Dist (train resets): high_vol=52 (38.2%), low_vol=47 (34.6%), medium_vol=37 (27.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 102 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.242, dd 0.00% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2296
   📊 Episode CVaR: regime=mid | CVaR=-0.02132 | threshold=-0.01700 | passed=❌ | bonus=-0.43
[CYCLE] Update 103/348 | Step 103,824/500,000 | Episode 132 | Time: 5751.0s
   📊 Metrics: Return=+50.67% | Sharpe=1.665 | DD=12.62% | Turnover=53.10%
   🎚️ Intra-Step TAPE: potential=0.7229 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0062 | critic_loss=0.0387 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0193 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 104/348 | Step 104,832/500,000 | Episode 132 | Time: 5806.6s
   📊 Metrics: Return=+58.75% | Sharpe=1.155 | DD=12.93% | Turnover=51.55%
   🎚️ Intra-Step TAPE: potential=0.3964 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0101 | critic_loss=0.0295 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0148 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.09 | std=0.41 | range=[0.61, 3.55]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.83 | AMZN=1.22 | JPM=1.20  BOT: NEE=0.87 | JNJ=0.83 | PG=0.82
   🧭 Regime Start Dist (train resets): high_vol=52 (38.2%), low_vol=47 (34.6%), medium_vol=37 (27.2%)
[CYCLE] Update 105/348 | Step 105,840/500,000 | Episode 132 | Time: 5862.6s
   📊 Metrics: Return=+60.37% | Sharpe=0.784 | DD=23.04% | Turnover=49.18%
   🎚️ Intra-Step TAPE: potential=0.2407 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0124 | critic_loss=0.0226 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0113 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00133_shp0p765_actor.weights.h5 (Sharpe=0.765, MDD=23.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00136_shp0p711_actor.weights.h5 (Sharpe=0.711, MDD=20.78%)
[CYCLE] Update 106/348 | Step 106,848/500,000 | Episode 136 | Time: 5918.8s
   📊 Metrics: Return=+54.42% | Sharpe=0.711 | DD=20.78% | Turnover=48.35%
   🎚️ Intra-Step TAPE: potential=0.7053 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0103 | critic_loss=0.0702 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0351 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.15 | std=0.67 | range=[1.06, 5.14]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.75 | AMZN=2.63 | MSFT=2.25  BOT: NEE=1.90 | JNJ=1.80 | PG=1.75
   🧭 Regime Start Dist (train resets): high_vol=54 (38.6%), low_vol=48 (34.3%), medium_vol=38 (27.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.18% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3689
   📊 Episode CVaR: regime=mid | CVaR=-0.01999 | threshold=-0.01700 | passed=❌ | bonus=-0.30
[CYCLE] Update 107/348 | Step 107,856/500,000 | Episode 136 | Time: 5974.6s
   📊 Metrics: Return=+27.26% | Sharpe=0.841 | DD=15.31% | Turnover=34.30%
   🎚️ Intra-Step TAPE: potential=0.7038 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0104 | critic_loss=0.0223 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0112 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 108/348 | Step 108,864/500,000 | Episode 136 | Time: 6030.6s
   📊 Metrics: Return=+67.11% | Sharpe=1.108 | DD=15.31% | Turnover=32.21%
   🎚️ Intra-Step TAPE: potential=0.5916 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0104 | critic_loss=0.0287 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0143 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.63 | std=1.34 | range=[1.80, 10.72]
   🏷️ Alpha Per-Asset  TOP: AMZN=5.67 | NVDA=5.15 | CAT=3.90  BOT: NEE=3.07 | JNJ=2.52 | PG=2.39
   🧭 Regime Start Dist (train resets): high_vol=54 (38.6%), low_vol=48 (34.3%), medium_vol=38 (27.1%)
[CYCLE] Update 109/348 | Step 109,872/500,000 | Episode 136 | Time: 6086.1s
   📊 Metrics: Return=+32.33% | Sharpe=0.391 | DD=26.54% | Turnover=31.08%
   🎚️ Intra-Step TAPE: potential=0.2379 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0118 | critic_loss=0.0262 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0131 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00140_shp0p832_actor.weights.h5 (Sharpe=0.832, MDD=12.82%)
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 6142.8s
   📊 Metrics: Return=+64.27% | Sharpe=0.832 | DD=12.82% | Turnover=30.87%
   🎚️ Intra-Step TAPE: potential=0.2260 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0112 | critic_loss=0.1221 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0611 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.59 | std=1.02 | range=[0.92, 8.39]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.23 | AMZN=3.08 | CAT=3.03  BOT: NEE=2.05 | JNJ=1.71 | PG=1.71
   🧭 Regime Start Dist (train resets): high_vol=55 (38.2%), low_vol=51 (35.4%), medium_vol=38 (26.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.320, dd 2.17% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4501
   📊 Episode CVaR: regime=mid | CVaR=-0.01957 | threshold=-0.01700 | passed=❌ | bonus=-0.26
[CYCLE] Update 111/348 | Step 111,888/500,000 | Episode 140 | Time: 6199.4s
   📊 Metrics: Return=+13.62% | Sharpe=0.355 | DD=18.05% | Turnover=31.12%
   🎚️ Intra-Step TAPE: potential=0.2189 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0087 | critic_loss=0.0399 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0200 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 112/348 | Step 112,896/500,000 | Episode 140 | Time: 6255.6s
   📊 Metrics: Return=-23.68% | Sharpe=-0.260 | DD=49.40% | Turnover=34.60%
   🎚️ Intra-Step TAPE: potential=0.2253 | delta_reward=-0.0020
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0089 | critic_loss=0.0449 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0225 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.95 | std=0.33 | range=[0.51, 2.10]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.34 | JPM=1.24 | AMZN=1.22  BOT: NEE=0.79 | JNJ=0.66 | PG=0.66
   🧭 Regime Start Dist (train resets): high_vol=55 (38.2%), low_vol=51 (35.4%), medium_vol=38 (26.4%)
[CYCLE] Update 113/348 | Step 113,904/500,000 | Episode 140 | Time: 6311.7s
   📊 Metrics: Return=+5.65% | Sharpe=0.122 | DD=49.40% | Turnover=37.31%
   🎚️ Intra-Step TAPE: potential=0.2148 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0128 | critic_loss=0.0186 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0093 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 114/348 | Step 114,912/500,000 | Episode 144 | Time: 6368.2s
   📊 Metrics: Return=+12.90% | Sharpe=0.176 | DD=48.74% | Turnover=37.38%
   🎚️ Intra-Step TAPE: potential=0.2245 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0113 | critic_loss=0.1026 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0513 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.16 | std=0.63 | range=[0.43, 4.08]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.39 | AMZN=1.71 | CAT=1.48  BOT: NEE=0.77 | JNJ=0.73 | PG=0.67
   🧭 Regime Start Dist (train resets): high_vol=57 (38.5%), low_vol=51 (34.5%), medium_vol=40 (27.0%)
   🔒 Drawdown λ snapshot=1.780 (peak 2.435, dd 17.99% / trig 21.00%) | terminal=2.584 (peak 2.756) | TAPE=0.2328
   📊 Episode CVaR: regime=high | CVaR=-0.03973 | threshold=-0.02400 | passed=❌ | bonus=-1.57
[CYCLE] Update 115/348 | Step 115,920/500,000 | Episode 144 | Time: 6424.1s
   📊 Metrics: Return=+0.80% | Sharpe=0.025 | DD=23.78% | Turnover=43.10%
   🎚️ Intra-Step TAPE: potential=0.7382 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0080 | critic_loss=0.0538 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0269 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 116/348 | Step 116,928/500,000 | Episode 144 | Time: 6479.9s
   📊 Metrics: Return=-1.76% | Sharpe=-0.060 | DD=23.78% | Turnover=41.54%
   🎚️ Intra-Step TAPE: potential=0.2453 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0096 | critic_loss=0.0690 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0345 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.30 | std=0.80 | range=[1.10, 6.53]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.88 | AMZN=2.88 | JPM=2.61  BOT: NEE=1.95 | XOM=1.88 | PG=1.87
   🧭 Regime Start Dist (train resets): high_vol=57 (38.5%), low_vol=51 (34.5%), medium_vol=40 (27.0%)
[CYCLE] Update 117/348 | Step 117,936/500,000 | Episode 144 | Time: 6535.7s
   📊 Metrics: Return=+5.14% | Sharpe=0.039 | DD=23.78% | Turnover=38.93%
   🎚️ Intra-Step TAPE: potential=0.2332 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0114 | critic_loss=0.0423 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0211 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00147_shp0p741_actor.weights.h5 (Sharpe=0.741, MDD=21.44%)
[CYCLE] Update 118/348 | Step 118,944/500,000 | Episode 148 | Time: 6592.0s
   📊 Metrics: Return=-3.32% | Sharpe=-0.101 | DD=23.79% | Turnover=39.59%
   🎚️ Intra-Step TAPE: potential=0.7087 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0094 | critic_loss=0.1337 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0669 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.19 | std=1.22 | range=[0.72, 9.67]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.09 | AMZN=3.35 | CAT=2.69  BOT: NEE=1.61 | JNJ=1.24 | PG=1.14
   🧭 Regime Start Dist (train resets): high_vol=59 (38.8%), low_vol=51 (33.6%), medium_vol=42 (27.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.185, dd 1.86% / trig 21.00%) | terminal=0.000 (peak 1.938) | TAPE=0.2202
   📊 Episode CVaR: regime=mid | CVaR=-0.02351 | threshold=-0.01700 | passed=❌ | bonus=-0.65
[CYCLE] Update 119/348 | Step 119,952/500,000 | Episode 148 | Time: 6648.0s
   📊 Metrics: Return=+1.81% | Sharpe=0.059 | DD=27.84% | Turnover=31.95%
   🎚️ Intra-Step TAPE: potential=0.2263 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0102 | critic_loss=0.0873 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0437 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 148 | Time: 6704.6s
   📊 Metrics: Return=-11.91% | Sharpe=-0.015 | DD=53.09% | Turnover=32.30%
   🎚️ Intra-Step TAPE: potential=0.2465 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0092 | critic_loss=0.0352 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0176 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.65 | std=1.26 | range=[0.48, 9.81]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.98 | JPM=2.84 | AMZN=2.83  BOT: NEE=0.88 | PG=0.75 | JNJ=0.71
   🧭 Regime Start Dist (train resets): high_vol=59 (38.8%), low_vol=51 (33.6%), medium_vol=42 (27.6%)
[CYCLE] Update 121/348 | Step 121,968/500,000 | Episode 148 | Time: 6760.7s
   📊 Metrics: Return=+2.82% | Sharpe=0.120 | DD=53.09% | Turnover=31.22%
   🎚️ Intra-Step TAPE: potential=0.2172 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0093 | critic_loss=0.0275 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 122/348 | Step 122,976/500,000 | Episode 152 | Time: 6816.5s
   📊 Metrics: Return=-1.64% | Sharpe=-0.041 | DD=25.13% | Turnover=36.15%
   🎚️ Intra-Step TAPE: potential=0.2294 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0087 | critic_loss=0.0379 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0189 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.42 | std=1.54 | range=[0.38, 12.95]
   🏷️ Alpha Per-Asset  TOP: AMZN=4.02 | NVDA=2.50 | JPM=1.48  BOT: NEE=0.78 | PG=0.68 | JNJ=0.65
   🧭 Regime Start Dist (train resets): high_vol=60 (38.5%), low_vol=51 (32.7%), medium_vol=45 (28.8%)
   🔒 Drawdown λ snapshot=2.257 (peak 3.228, dd 4.40% / trig 21.00%) | terminal=0.000 (peak 0.038) | TAPE=0.2213
   📊 Episode CVaR: regime=mid | CVaR=-0.02743 | threshold=-0.01700 | passed=❌ | bonus=-1.04
[CYCLE] Update 123/348 | Step 123,984/500,000 | Episode 152 | Time: 6872.3s
   📊 Metrics: Return=+12.47% | Sharpe=0.404 | DD=10.44% | Turnover=41.02%
   🎚️ Intra-Step TAPE: potential=0.2265 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0095 | critic_loss=0.0268 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0134 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 124/348 | Step 124,992/500,000 | Episode 152 | Time: 6927.8s
   📊 Metrics: Return=+8.31% | Sharpe=0.128 | DD=11.37% | Turnover=40.00%
   🎚️ Intra-Step TAPE: potential=0.2648 | delta_reward=-0.0022
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0114 | critic_loss=0.0238 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0119 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.65 | std=2.44 | range=[0.34, 15.07]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.28 | AMZN=3.35 | JPM=2.03  BOT: XOM=0.54 | JNJ=0.53 | PG=0.48
   🧭 Regime Start Dist (train resets): high_vol=60 (38.5%), low_vol=51 (32.7%), medium_vol=45 (28.8%)
[CYCLE] Update 125/348 | Step 126,000/500,000 | Episode 152 | Time: 6984.3s
   📊 Metrics: Return=+34.94% | Sharpe=0.465 | DD=15.65% | Turnover=38.15%
   🎚️ Intra-Step TAPE: potential=0.7377 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0100 | critic_loss=0.0358 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0179 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 126/348 | Step 127,008/500,000 | Episode 156 | Time: 7040.1s
   📊 Metrics: Return=+45.23% | Sharpe=0.571 | DD=17.66% | Turnover=37.28%
   🎚️ Intra-Step TAPE: potential=0.2396 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0138 | critic_loss=0.1008 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0504 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.64 | std=2.51 | range=[0.27, 15.80]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.42 | AMZN=4.24 | JPM=2.25  BOT: NEE=0.43 | PG=0.32 | JNJ=0.30
   🧭 Regime Start Dist (train resets): high_vol=61 (38.1%), low_vol=52 (32.5%), medium_vol=47 (29.4%)
   🔒 Drawdown λ snapshot=0.043 (peak 0.046, dd 21.71% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3187
   📊 Episode CVaR: regime=mid | CVaR=-0.02196 | threshold=-0.01700 | passed=❌ | bonus=-0.50
[CYCLE] Update 127/348 | Step 128,016/500,000 | Episode 156 | Time: 7095.5s
   📊 Metrics: Return=-18.21% | Sharpe=-0.061 | DD=56.00% | Turnover=28.45%
   🎚️ Intra-Step TAPE: potential=0.6274 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0109 | critic_loss=0.0368 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0184 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 128/348 | Step 129,024/500,000 | Episode 156 | Time: 7151.2s
   📊 Metrics: Return=+25.26% | Sharpe=0.346 | DD=56.00% | Turnover=26.42%
   🎚️ Intra-Step TAPE: potential=0.5450 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0147 | critic_loss=0.0316 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0158 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.68 | std=2.41 | range=[0.28, 14.38]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.34 | AMZN=3.77 | JPM=2.74  BOT: NEE=0.42 | JNJ=0.39 | PG=0.38
   🧭 Regime Start Dist (train resets): high_vol=61 (38.1%), low_vol=52 (32.5%), medium_vol=47 (29.4%)
[CYCLE] Update 129/348 | Step 130,032/500,000 | Episode 156 | Time: 7207.0s
   📊 Metrics: Return=+36.05% | Sharpe=0.346 | DD=56.00% | Turnover=26.73%
   🎚️ Intra-Step TAPE: potential=0.2269 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0085 | critic_loss=0.0306 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0153 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 160 | Time: 7264.0s
   📊 Metrics: Return=+43.51% | Sharpe=0.426 | DD=30.19% | Turnover=30.92%
   🎚️ Intra-Step TAPE: potential=0.2170 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0107 | critic_loss=0.1140 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0570 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.88 | std=2.81 | range=[0.30, 16.44]
   🏷️ Alpha Per-Asset  TOP: NVDA=6.72 | AMZN=4.69 | CAT=2.51  BOT: NEE=0.55 | JNJ=0.40 | PG=0.36
   🧭 Regime Start Dist (train resets): high_vol=64 (39.0%), low_vol=52 (31.7%), medium_vol=48 (29.3%)
   🔒 Drawdown λ snapshot=1.320 (peak 2.208, dd 21.16% / trig 21.00%) | terminal=0.000 (peak 0.113) | TAPE=0.2611
   📊 Episode CVaR: regime=mid | CVaR=-0.03342 | threshold=-0.01700 | passed=❌ | bonus=-1.64
[CYCLE] Update 131/348 | Step 132,048/500,000 | Episode 160 | Time: 7320.6s
   📊 Metrics: Return=-35.95% | Sharpe=-0.408 | DD=57.83% | Turnover=25.52%
   🎚️ Intra-Step TAPE: potential=0.4780 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0065 | critic_loss=0.0580 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0290 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 132/348 | Step 133,056/500,000 | Episode 160 | Time: 7375.8s
   📊 Metrics: Return=+15.52% | Sharpe=0.276 | DD=57.83% | Turnover=22.57%
   🎚️ Intra-Step TAPE: potential=0.2356 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0158 | critic_loss=0.0411 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0205 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.93 | std=2.59 | range=[0.28, 15.44]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.95 | JPM=4.66 | CAT=3.02  BOT: NEE=0.45 | PG=0.40 | JNJ=0.35
   🧭 Regime Start Dist (train resets): high_vol=64 (39.0%), low_vol=52 (31.7%), medium_vol=48 (29.3%)
[CYCLE] Update 133/348 | Step 134,064/500,000 | Episode 160 | Time: 7431.4s
   📊 Metrics: Return=+58.57% | Sharpe=0.456 | DD=57.83% | Turnover=23.57%
   🎚️ Intra-Step TAPE: potential=0.7515 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0103 | critic_loss=0.0247 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0123 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 134/348 | Step 135,072/500,000 | Episode 164 | Time: 7487.5s
   📊 Metrics: Return=-0.97% | Sharpe=-0.023 | DD=23.17% | Turnover=32.26%
   🎚️ Intra-Step TAPE: potential=0.7141 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0085 | critic_loss=0.0952 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0476 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.31 | std=3.98 | range=[0.26, 19.47]
   🏷️ Alpha Per-Asset  TOP: NVDA=9.87 | AMZN=6.83 | CAT=2.43  BOT: NEE=0.44 | JNJ=0.37 | PG=0.36
   🧭 Regime Start Dist (train resets): high_vol=67 (39.9%), low_vol=53 (31.5%), medium_vol=48 (28.6%)
   🔒 Drawdown λ snapshot=2.018 (peak 3.003, dd 2.46% / trig 21.00%) | terminal=0.000 (peak 0.002) | TAPE=0.2302
   📊 Episode CVaR: regime=mid | CVaR=-0.02810 | threshold=-0.01700 | passed=❌ | bonus=-1.11
[CYCLE] Update 135/348 | Step 136,080/500,000 | Episode 164 | Time: 7543.8s
   📊 Metrics: Return=+8.16% | Sharpe=0.218 | DD=39.53% | Turnover=22.96%
   🎚️ Intra-Step TAPE: potential=0.2148 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0084 | critic_loss=0.1375 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0688 | risk_aux_total=0.0009 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 136/348 | Step 137,088/500,000 | Episode 164 | Time: 7599.8s
   📊 Metrics: Return=+15.58% | Sharpe=0.277 | DD=60.14% | Turnover=21.89%
   🎚️ Intra-Step TAPE: potential=0.6069 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0076 | critic_loss=0.0359 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0179 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.59 | std=2.50 | range=[0.24, 14.81]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.40 | JPM=3.85 | AMZN=2.92  BOT: GLD=0.35 | PG=0.29 | JNJ=0.29
   🧭 Regime Start Dist (train resets): high_vol=67 (39.9%), low_vol=53 (31.5%), medium_vol=48 (28.6%)
[CYCLE] Update 137/348 | Step 138,096/500,000 | Episode 164 | Time: 7655.9s
   📊 Metrics: Return=+18.47% | Sharpe=0.249 | DD=60.14% | Turnover=24.58%
   🎚️ Intra-Step TAPE: potential=0.2312 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0127 | critic_loss=0.0567 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0284 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 138/348 | Step 139,104/500,000 | Episode 168 | Time: 7712.2s
   📊 Metrics: Return=+35.33% | Sharpe=0.376 | DD=30.67% | Turnover=33.80%
   🎚️ Intra-Step TAPE: potential=0.7458 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0086 | critic_loss=0.0574 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0287 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.73 | std=2.85 | range=[0.31, 19.07]
   🏷️ Alpha Per-Asset  TOP: AMZN=6.33 | NVDA=5.44 | CAT=1.46  BOT: PG=0.48 | NEE=0.48 | JNJ=0.43
   🧭 Regime Start Dist (train resets): high_vol=67 (39.0%), low_vol=55 (32.0%), medium_vol=50 (29.1%)
   🔒 Drawdown λ snapshot=2.714 (peak 3.642, dd 2.34% / trig 21.00%) | terminal=0.000 (peak 0.167) | TAPE=0.2528
   📊 Episode CVaR: regime=mid | CVaR=-0.03021 | threshold=-0.01700 | passed=❌ | bonus=-1.32
[CYCLE] Update 139/348 | Step 140,112/500,000 | Episode 168 | Time: 7767.8s
   📊 Metrics: Return=+67.38% | Sharpe=1.645 | DD=15.41% | Turnover=36.60%
   🎚️ Intra-Step TAPE: potential=0.2274 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0116 | critic_loss=0.1065 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0532 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 168 | Time: 7824.6s
   📊 Metrics: Return=+134.25% | Sharpe=1.756 | DD=15.41% | Turnover=36.63%
   🎚️ Intra-Step TAPE: potential=0.3930 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0106 | critic_loss=0.1241 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0620 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.84 | std=4.30 | range=[0.36, 20.94]
   🏷️ Alpha Per-Asset  TOP: NVDA=10.54 | AMZN=8.50 | CAT=2.45  BOT: XOM=0.77 | JNJ=0.59 | PG=0.52
   🧭 Regime Start Dist (train resets): high_vol=67 (39.0%), low_vol=55 (32.0%), medium_vol=50 (29.1%)
[CYCLE] Update 141/348 | Step 142,128/500,000 | Episode 168 | Time: 7880.7s
   📊 Metrics: Return=+135.80% | Sharpe=1.172 | DD=27.93% | Turnover=33.28%
   🎚️ Intra-Step TAPE: potential=0.7353 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0074 | critic_loss=0.0400 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0200 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00171_shp1p431_actor.weights.h5 (Sharpe=1.431, MDD=14.15%)
[CYCLE] Update 142/348 | Step 143,136/500,000 | Episode 172 | Time: 7937.4s
   📊 Metrics: Return=+25.61% | Sharpe=0.281 | DD=58.67% | Turnover=24.98%
   🎚️ Intra-Step TAPE: potential=0.2250 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0127 | critic_loss=0.0869 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0434 | risk_aux_total=0.0009 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.85 | std=3.61 | range=[0.40, 18.12]
   🏷️ Alpha Per-Asset  TOP: NVDA=10.05 | JPM=5.20 | AMZN=4.18  BOT: NEE=0.72 | JNJ=0.57 | PG=0.53
   🧭 Regime Start Dist (train resets): high_vol=68 (38.6%), low_vol=56 (31.8%), medium_vol=52 (29.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 11.18% / trig 21.00%) | terminal=4.931 (peak 4.931) | TAPE=0.2454
   📊 Episode CVaR: regime=high | CVaR=-0.05206 | threshold=-0.02400 | passed=❌ | bonus=-2.81
[CYCLE] Update 143/348 | Step 144,144/500,000 | Episode 172 | Time: 7993.3s
   📊 Metrics: Return=+60.75% | Sharpe=1.464 | DD=14.05% | Turnover=26.73%
   🎚️ Intra-Step TAPE: potential=0.7022 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0106 | critic_loss=0.0372 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0186 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 144/348 | Step 145,152/500,000 | Episode 172 | Time: 8050.2s
   📊 Metrics: Return=+127.51% | Sharpe=1.739 | DD=14.05% | Turnover=30.40%
   🎚️ Intra-Step TAPE: potential=0.6255 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0104 | critic_loss=0.0463 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0232 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.75 | std=2.34 | range=[0.37, 14.27]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.60 | AMZN=2.58 | GLD=2.58  BOT: PG=0.52 | XOM=0.50 | JNJ=0.47
   🧭 Regime Start Dist (train resets): high_vol=68 (38.6%), low_vol=56 (31.8%), medium_vol=52 (29.5%)
[CYCLE] Update 145/348 | Step 146,160/500,000 | Episode 172 | Time: 8106.7s
   📊 Metrics: Return=+186.90% | Sharpe=1.664 | DD=14.05% | Turnover=31.60%
   🎚️ Intra-Step TAPE: potential=0.5672 | delta_reward=+0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0078 | critic_loss=0.0800 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0400 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00173_shp1p581_actor.weights.h5 (Sharpe=1.581, MDD=14.05%)
[CYCLE] Update 146/348 | Step 147,168/500,000 | Episode 176 | Time: 8163.7s
   📊 Metrics: Return=+34.60% | Sharpe=0.395 | DD=15.98% | Turnover=25.92%
   🎚️ Intra-Step TAPE: potential=0.7409 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0154 | critic_loss=0.1213 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0607 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.65 | std=4.61 | range=[0.43, 21.70]
   🏷️ Alpha Per-Asset  TOP: NVDA=10.85 | JPM=8.03 | AMZN=6.62  BOT: GLD=1.02 | PG=0.79 | JNJ=0.69
   🧭 Regime Start Dist (train resets): high_vol=72 (40.0%), low_vol=56 (31.1%), medium_vol=52 (28.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.006, dd 7.36% / trig 21.00%) | terminal=0.000 (peak 3.698) | TAPE=0.2902
   📊 Episode CVaR: regime=mid | CVaR=-0.02526 | threshold=-0.01700 | passed=❌ | bonus=-0.83
[CYCLE] Update 147/348 | Step 148,176/500,000 | Episode 176 | Time: 8220.6s
   📊 Metrics: Return=+74.29% | Sharpe=0.969 | DD=24.12% | Turnover=19.29%
   🎚️ Intra-Step TAPE: potential=0.6034 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0095 | critic_loss=0.0368 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0184 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 148/348 | Step 149,184/500,000 | Episode 176 | Time: 8276.4s
   📊 Metrics: Return=+71.99% | Sharpe=0.694 | DD=26.93% | Turnover=25.17%
   🎚️ Intra-Step TAPE: potential=0.2359 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0094 | critic_loss=0.0636 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0318 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.89 | std=2.86 | range=[0.37, 15.71]
   🏷️ Alpha Per-Asset  TOP: NVDA=8.75 | JPM=2.54 | CAT=2.47  BOT: XOM=0.54 | PG=0.47 | JNJ=0.46
   🧭 Regime Start Dist (train resets): high_vol=72 (40.0%), low_vol=56 (31.1%), medium_vol=52 (28.9%)
   [TOOL] Actor learning rate adjusted to 0.000020 at step 150,000
[CYCLE] Update 149/348 | Step 150,192/500,000 | Episode 176 | Time: 8333.9s
   📊 Metrics: Return=+120.00% | Sharpe=0.768 | DD=29.11% | Turnover=24.52%
   🎚️ Intra-Step TAPE: potential=0.6194 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0091 | critic_loss=0.0414 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0207 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200

📚 PPO ROLLOUT UPDATE at 150,192 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 150,192 steps:
   Batch size: 336

[DOWN] PPO GAMMA UPDATE at 150,192 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 150,192 steps:
   gae_lambda: 0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00179_shp1p184_actor.weights.h5 (Sharpe=1.184, MDD=24.34%)
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 180 | Time: 8429.0s
   📊 Metrics: Return=+15.38% | Sharpe=0.224 | DD=57.94% | Turnover=23.63%
   🎚️ Intra-Step TAPE: potential=0.2308 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0021 | critic_loss=0.0966 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0483 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.70 | std=2.50 | range=[0.35, 16.24]
   🏷️ Alpha Per-Asset  TOP: AMZN=5.26 | NVDA=4.23 | CAT=2.06  BOT: NEE=0.51 | PG=0.47 | JNJ=0.47
   🧭 Regime Start Dist (train resets): high_vol=72 (39.1%), low_vol=57 (31.0%), medium_vol=55 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.11% / trig 21.00%) | terminal=2.917 (peak 4.361) | TAPE=0.2392
   📊 Episode CVaR: regime=high | CVaR=-0.05221 | threshold=-0.02400 | passed=❌ | bonus=-2.82
[CYCLE] Update 151/348 | Step 153,216/500,000 | Episode 180 | Time: 8512.2s
   📊 Metrics: Return=+18.14% | Sharpe=0.345 | DD=11.42% | Turnover=36.19%
   🎚️ Intra-Step TAPE: potential=0.7403 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0024 | critic_loss=0.0690 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0345 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00181_shp0p995_actor.weights.h5 (Sharpe=0.995, MDD=12.52%)
[CYCLE] Update 152/348 | Step 154,728/500,000 | Episode 184 | Time: 8594.5s
   📊 Metrics: Return=+45.85% | Sharpe=0.390 | DD=56.66% | Turnover=28.52%
   🎚️ Intra-Step TAPE: potential=0.2129 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0070 | critic_loss=0.0864 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0432 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.21 | std=3.14 | range=[0.31, 19.06]
   🏷️ Alpha Per-Asset  TOP: NVDA=8.28 | JPM=3.89 | AMZN=3.26  BOT: GLD=0.62 | JNJ=0.49 | PG=0.47
   🧭 Regime Start Dist (train resets): high_vol=75 (39.9%), low_vol=57 (30.3%), medium_vol=56 (29.8%)
   🔒 Drawdown λ snapshot=0.217 (peak 0.217, dd 28.33% / trig 21.00%) | terminal=3.959 (peak 3.959) | TAPE=0.2594
   📊 Episode CVaR: regime=high | CVaR=-0.05001 | threshold=-0.02400 | passed=❌ | bonus=-2.60
[CYCLE] Update 153/348 | Step 156,240/500,000 | Episode 184 | Time: 8678.0s
   📊 Metrics: Return=+6.12% | Sharpe=0.246 | DD=41.03% | Turnover=23.44%
   🎚️ Intra-Step TAPE: potential=0.2225 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0060 | critic_loss=0.1811 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0906 | risk_aux_total=0.0009 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 154/348 | Step 157,752/500,000 | Episode 184 | Time: 8761.5s
   📊 Metrics: Return=+32.22% | Sharpe=0.356 | DD=41.03% | Turnover=29.75%
   🎚️ Intra-Step TAPE: potential=0.3196 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0136 | critic_loss=0.0952 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0476 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.51 | std=2.64 | range=[0.27, 14.79]
   🏷️ Alpha Per-Asset  TOP: NVDA=6.88 | AMZN=2.96 | CAT=1.69  BOT: XOM=0.37 | JNJ=0.31 | PG=0.31
   🧭 Regime Start Dist (train resets): high_vol=75 (39.9%), low_vol=57 (30.3%), medium_vol=56 (29.8%)
[CYCLE] Update 155/348 | Step 159,264/500,000 | Episode 188 | Time: 8844.2s
   📊 Metrics: Return=+0.56% | Sharpe=0.128 | DD=56.58% | Turnover=29.01%
   🎚️ Intra-Step TAPE: potential=0.6088 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0080 | critic_loss=0.1253 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0627 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.48% / trig 21.00%) | terminal=3.579 (peak 5.000) | TAPE=0.2291
   📊 Episode CVaR: regime=high | CVaR=-0.05257 | threshold=-0.02400 | passed=❌ | bonus=-2.86
[CYCLE] Update 156/348 | Step 160,776/500,000 | Episode 188 | Time: 8930.7s
   📊 Metrics: Return=-9.85% | Sharpe=0.018 | DD=57.42% | Turnover=24.37%
   🎚️ Intra-Step TAPE: potential=0.4247 | delta_reward=+0.0017
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0089 | critic_loss=0.0593 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0296 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.35 | std=3.38 | range=[0.37, 18.23]
   🏷️ Alpha Per-Asset  TOP: NVDA=8.72 | AMZN=5.97 | JPM=1.89  BOT: NEE=0.75 | JNJ=0.57 | PG=0.56
   🧭 Regime Start Dist (train resets): high_vol=75 (39.1%), low_vol=59 (30.7%), medium_vol=58 (30.2%)
[CYCLE] Update 157/348 | Step 162,288/500,000 | Episode 188 | Time: 9014.9s
   📊 Metrics: Return=+31.57% | Sharpe=0.322 | DD=57.42% | Turnover=23.65%
   🎚️ Intra-Step TAPE: potential=0.2380 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0070 | critic_loss=0.0530 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0265 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00190_shp1p480_actor.weights.h5 (Sharpe=1.480, MDD=13.64%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00191_shp1p207_actor.weights.h5 (Sharpe=1.207, MDD=22.36%)
[CYCLE] Update 158/348 | Step 163,800/500,000 | Episode 192 | Time: 9099.3s
   📊 Metrics: Return=+78.72% | Sharpe=0.679 | DD=27.99% | Turnover=27.49%
   🎚️ Intra-Step TAPE: potential=0.6554 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0145 | critic_loss=0.1103 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0552 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.94 | std=2.49 | range=[0.39, 16.67]
   🏷️ Alpha Per-Asset  TOP: NVDA=6.14 | AMZN=3.48 | CAT=2.67  BOT: NEE=0.70 | PG=0.61 | JNJ=0.59
   🧭 Regime Start Dist (train resets): high_vol=77 (39.3%), low_vol=61 (31.1%), medium_vol=58 (29.6%)
   🔒 Drawdown λ snapshot=1.547 (peak 3.042, dd 0.36% / trig 21.00%) | terminal=0.063 (peak 2.684) | TAPE=0.3432
   📊 Episode CVaR: regime=mid | CVaR=-0.03121 | threshold=-0.01700 | passed=❌ | bonus=-1.42
[CYCLE] Update 159/348 | Step 165,312/500,000 | Episode 192 | Time: 9182.8s
   📊 Metrics: Return=+49.83% | Sharpe=0.873 | DD=14.15% | Turnover=31.15%
   🎚️ Intra-Step TAPE: potential=0.5251 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0065 | critic_loss=0.0377 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0189 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00193_shp1p194_actor.weights.h5 (Sharpe=1.194, MDD=14.15%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00195_shp1p413_actor.weights.h5 (Sharpe=1.413, MDD=16.73%)
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 196 | Time: 9266.2s
   📊 Metrics: Return=+18.41% | Sharpe=0.212 | DD=28.01% | Turnover=30.05%
   🎚️ Intra-Step TAPE: potential=0.6426 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0183 | critic_loss=0.0722 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0361 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.82 | std=2.30 | range=[0.41, 12.95]
   🏷️ Alpha Per-Asset  TOP: NVDA=6.35 | JPM=2.57 | CAT=2.19  BOT: JNJ=0.66 | PG=0.66 | XOM=0.65
   🧭 Regime Start Dist (train resets): high_vol=79 (39.5%), low_vol=61 (30.5%), medium_vol=60 (30.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.007, dd 2.91% / trig 21.00%) | terminal=0.000 (peak 0.073) | TAPE=0.2364
   📊 Episode CVaR: regime=mid | CVaR=-0.03006 | threshold=-0.01700 | passed=❌ | bonus=-1.31
[CYCLE] Update 161/348 | Step 168,336/500,000 | Episode 196 | Time: 9349.6s
   📊 Metrics: Return=+49.57% | Sharpe=0.771 | DD=24.06% | Turnover=25.65%
   🎚️ Intra-Step TAPE: potential=0.5642 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0200 | critic_loss=0.0861 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0430 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 162/348 | Step 169,848/500,000 | Episode 196 | Time: 9432.8s
   📊 Metrics: Return=+78.02% | Sharpe=0.670 | DD=27.71% | Turnover=28.30%
   🎚️ Intra-Step TAPE: potential=0.2697 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0105 | critic_loss=0.0477 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0239 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.70 | std=2.06 | range=[0.41, 15.10]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.89 | JPM=2.72 | AMZN=2.46  BOT: NEE=0.65 | PG=0.56 | JNJ=0.52
   🧭 Regime Start Dist (train resets): high_vol=79 (39.5%), low_vol=61 (30.5%), medium_vol=60 (30.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00200_shp0p712_actor.weights.h5 (Sharpe=0.712, MDD=13.79%)
[CYCLE] Update 163/348 | Step 171,360/500,000 | Episode 200 | Time: 9517.2s
   📊 Metrics: Return=+57.08% | Sharpe=0.712 | DD=13.79% | Turnover=32.78%
   🎚️ Intra-Step TAPE: potential=0.2234 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0104 | critic_loss=0.0453 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0227 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 13.30% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3821
   📊 Episode CVaR: regime=mid | CVaR=-0.02130 | threshold=-0.01700 | passed=❌ | bonus=-0.43
[CYCLE] Update 164/348 | Step 172,872/500,000 | Episode 200 | Time: 9600.2s
   📊 Metrics: Return=+22.22% | Sharpe=0.409 | DD=26.27% | Turnover=29.11%
   🎚️ Intra-Step TAPE: potential=0.5849 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0064 | critic_loss=0.0400 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0200 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.23 | std=2.86 | range=[0.41, 16.59]
   🏷️ Alpha Per-Asset  TOP: NVDA=6.76 | AMZN=4.62 | JPM=3.43  BOT: NEE=0.70 | PG=0.58 | JNJ=0.54
   🧭 Regime Start Dist (train resets): high_vol=79 (38.7%), low_vol=62 (30.4%), medium_vol=63 (30.9%)
[CYCLE] Update 165/348 | Step 174,384/500,000 | Episode 200 | Time: 9683.4s
   📊 Metrics: Return=+22.88% | Sharpe=0.274 | DD=26.27% | Turnover=31.14%
   🎚️ Intra-Step TAPE: potential=0.2392 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0072 | critic_loss=0.0185 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0092 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00202_shp1p326_actor.weights.h5 (Sharpe=1.326, MDD=14.12%)
[CYCLE] Update 166/348 | Step 175,896/500,000 | Episode 204 | Time: 9768.4s
   📊 Metrics: Return=+22.15% | Sharpe=0.259 | DD=55.88% | Turnover=27.06%
   🎚️ Intra-Step TAPE: potential=0.5101 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0151 | critic_loss=0.1348 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0674 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.70 | std=2.16 | range=[0.41, 15.07]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.43 | AMZN=4.40 | GLD=1.87  BOT: NEE=0.60 | PG=0.60 | JNJ=0.60
   🧭 Regime Start Dist (train resets): high_vol=79 (38.0%), low_vol=64 (30.8%), medium_vol=65 (31.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.05% / trig 21.00%) | terminal=3.701 (peak 4.779) | TAPE=0.2420
   📊 Episode CVaR: regime=high | CVaR=-0.04891 | threshold=-0.02400 | passed=❌ | bonus=-2.49
[CYCLE] Update 167/348 | Step 177,408/500,000 | Episode 204 | Time: 9851.9s
   📊 Metrics: Return=+24.40% | Sharpe=0.468 | DD=11.06% | Turnover=34.90%
   🎚️ Intra-Step TAPE: potential=0.6687 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0007 | critic_loss=0.0394 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0197 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00205_shp0p947_actor.weights.h5 (Sharpe=0.947, MDD=14.48%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00206_shp1p087_actor.weights.h5 (Sharpe=1.087, MDD=14.67%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00208_shp1p053_actor.weights.h5 (Sharpe=1.053, MDD=22.35%)
[CYCLE] Update 168/348 | Step 178,920/500,000 | Episode 208 | Time: 9936.0s
   📊 Metrics: Return=+114.02% | Sharpe=1.053 | DD=22.35% | Turnover=35.87%
   🎚️ Intra-Step TAPE: potential=0.2414 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0078 | critic_loss=0.0635 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0317 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.63 | std=2.04 | range=[0.45, 14.34]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.64 | AMZN=2.61 | CAT=1.97  BOT: NEE=0.75 | JNJ=0.67 | PG=0.63
   🧭 Regime Start Dist (train resets): high_vol=80 (37.7%), low_vol=67 (31.6%), medium_vol=65 (30.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 11.02% / trig 21.00%) | terminal=0.000 (peak 2.775) | TAPE=0.5019
   📊 Episode CVaR: regime=mid | CVaR=-0.02678 | threshold=-0.01700 | passed=❌ | bonus=-0.98
[CYCLE] Update 169/348 | Step 180,432/500,000 | Episode 208 | Time: 10020.5s
   📊 Metrics: Return=-33.28% | Sharpe=-0.349 | DD=56.02% | Turnover=29.05%
   🎚️ Intra-Step TAPE: potential=0.2403 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0067 | critic_loss=0.0134 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0067 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 208 | Time: 10103.9s
   📊 Metrics: Return=+6.00% | Sharpe=0.167 | DD=56.02% | Turnover=28.58%
   🎚️ Intra-Step TAPE: potential=0.7465 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0151 | critic_loss=0.0249 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0125 | risk_aux_total=0.0004 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0004 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.07 | std=2.16 | range=[0.70, 12.48]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.95 | CAT=2.95 | JPM=2.73  BOT: GLD=1.05 | PG=0.96 | JNJ=0.92
   🧭 Regime Start Dist (train resets): high_vol=80 (37.7%), low_vol=67 (31.6%), medium_vol=65 (30.7%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00211_shp1p198_actor.weights.h5 (Sharpe=1.198, MDD=14.33%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00212_shp0p882_actor.weights.h5 (Sharpe=0.882, MDD=11.92%)
[CYCLE] Update 171/348 | Step 183,456/500,000 | Episode 212 | Time: 10188.3s
   📊 Metrics: Return=+72.93% | Sharpe=0.882 | DD=11.92% | Turnover=35.67%
   🎚️ Intra-Step TAPE: potential=0.7350 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0064 | critic_loss=0.1353 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0677 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=2.425 (peak 3.302, dd 0.11% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4759
   📊 Episode CVaR: regime=mid | CVaR=-0.02069 | threshold=-0.01700 | passed=❌ | bonus=-0.37
[CYCLE] Update 172/348 | Step 184,968/500,000 | Episode 212 | Time: 10271.6s
   📊 Metrics: Return=+78.64% | Sharpe=0.883 | DD=21.86% | Turnover=35.51%
   🎚️ Intra-Step TAPE: potential=0.5391 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0121 | critic_loss=0.0451 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0226 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.00 | std=1.44 | range=[0.33, 12.16]
   🏷️ Alpha Per-Asset  TOP: NVDA=3.48 | AMZN=1.58 | CAT=1.22  BOT: XOM=0.42 | PG=0.41 | JNJ=0.39
   🧭 Regime Start Dist (train resets): high_vol=83 (38.4%), low_vol=67 (31.0%), medium_vol=66 (30.6%)
[CYCLE] Update 173/348 | Step 186,480/500,000 | Episode 212 | Time: 10355.2s
   📊 Metrics: Return=+64.11% | Sharpe=0.527 | DD=26.02% | Turnover=37.51%
   🎚️ Intra-Step TAPE: potential=0.4276 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0063 | critic_loss=0.0377 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0189 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00214_shp1p051_actor.weights.h5 (Sharpe=1.051, MDD=12.52%)
[CYCLE] Update 174/348 | Step 187,992/500,000 | Episode 216 | Time: 10439.7s
   📊 Metrics: Return=+36.94% | Sharpe=0.358 | DD=28.55% | Turnover=37.32%
   🎚️ Intra-Step TAPE: potential=0.2172 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0174 | critic_loss=0.0246 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0123 | risk_aux_total=0.0009 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0009 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.42 | std=1.65 | range=[0.47, 12.80]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.00 | AMZN=3.03 | JPM=1.71  BOT: PG=0.65 | XOM=0.65 | JNJ=0.63
   🧭 Regime Start Dist (train resets): high_vol=84 (38.2%), low_vol=67 (30.5%), medium_vol=69 (31.4%)
   🔒 Drawdown λ snapshot=3.050 (peak 3.050, dd 50.64% / trig 21.00%) | terminal=0.022 (peak 0.086) | TAPE=0.2558
   📊 Episode CVaR: regime=high | CVaR=-0.03677 | threshold=-0.02400 | passed=❌ | bonus=-1.28
[CYCLE] Update 175/348 | Step 189,504/500,000 | Episode 216 | Time: 10522.8s
   📊 Metrics: Return=-28.49% | Sharpe=-0.192 | DD=59.06% | Turnover=30.97%
   🎚️ Intra-Step TAPE: potential=0.2216 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0064 | critic_loss=0.0261 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0131 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00218_shp1p110_actor.weights.h5 (Sharpe=1.110, MDD=14.07%)
[CYCLE] Update 176/348 | Step 191,016/500,000 | Episode 220 | Time: 10606.4s
   📊 Metrics: Return=+40.54% | Sharpe=0.532 | DD=12.16% | Turnover=39.89%
   🎚️ Intra-Step TAPE: potential=0.2107 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0080 | critic_loss=0.0434 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0217 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.03 | std=2.72 | range=[0.64, 16.44]
   🏷️ Alpha Per-Asset  TOP: NVDA=8.55 | AMZN=2.12 | JPM=2.02  BOT: GLD=0.99 | PG=0.85 | JNJ=0.84
   🧭 Regime Start Dist (train resets): high_vol=86 (38.4%), low_vol=68 (30.4%), medium_vol=70 (31.2%)
   🔒 Drawdown λ snapshot=3.697 (peak 3.697, dd 26.88% / trig 21.00%) | terminal=0.000 (peak 0.017) | TAPE=0.3146
   📊 Episode CVaR: regime=mid | CVaR=-0.02053 | threshold=-0.01700 | passed=❌ | bonus=-0.35
[CYCLE] Update 177/348 | Step 192,528/500,000 | Episode 220 | Time: 10689.5s
   📊 Metrics: Return=+11.33% | Sharpe=0.298 | DD=38.41% | Turnover=25.53%
   🎚️ Intra-Step TAPE: potential=0.2251 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0116 | critic_loss=0.1163 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0582 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 178/348 | Step 194,040/500,000 | Episode 220 | Time: 10770.7s
   📊 Metrics: Return=+27.00% | Sharpe=0.322 | DD=38.41% | Turnover=27.96%
   🎚️ Intra-Step TAPE: potential=0.2420 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0155 | critic_loss=0.0205 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0102 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.25 | std=2.46 | range=[0.79, 18.46]
   🏷️ Alpha Per-Asset  TOP: NVDA=7.28 | AMZN=2.96 | CAT=2.35  BOT: XOM=1.13 | PG=1.09 | JNJ=1.07
   🧭 Regime Start Dist (train resets): high_vol=86 (38.4%), low_vol=68 (30.4%), medium_vol=70 (31.2%)
[CYCLE] Update 179/348 | Step 195,552/500,000 | Episode 224 | Time: 10851.9s
   📊 Metrics: Return=+14.69% | Sharpe=0.172 | DD=14.94% | Turnover=33.63%
   🎚️ Intra-Step TAPE: potential=0.2319 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0115 | critic_loss=0.0273 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0137 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.346 (peak 1.328, dd 1.11% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2566
   📊 Episode CVaR: regime=mid | CVaR=-0.02116 | threshold=-0.01700 | passed=❌ | bonus=-0.42
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 224 | Time: 10933.1s
   📊 Metrics: Return=+28.82% | Sharpe=0.504 | DD=24.96% | Turnover=27.33%
   🎚️ Intra-Step TAPE: potential=0.2333 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0113 | critic_loss=0.0412 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0206 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.16 | std=2.83 | range=[1.12, 18.28]
   🏷️ Alpha Per-Asset  TOP: NVDA=7.90 | JPM=4.70 | AMZN=4.30  BOT: GLD=1.67 | PG=1.50 | JNJ=1.45
   🧭 Regime Start Dist (train resets): high_vol=89 (39.0%), low_vol=68 (29.8%), medium_vol=71 (31.1%)
[CYCLE] Update 181/348 | Step 198,576/500,000 | Episode 224 | Time: 11014.1s
   📊 Metrics: Return=+41.18% | Sharpe=0.437 | DD=27.68% | Turnover=28.09%
   🎚️ Intra-Step TAPE: potential=0.2418 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0064 | critic_loss=0.0338 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0169 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00227_shp1p099_actor.weights.h5 (Sharpe=1.099, MDD=14.46%)

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.75
[CYCLE] Update 182/348 | Step 200,088/500,000 | Episode 228 | Time: 11096.1s
   📊 Metrics: Return=-1.42% | Sharpe=0.094 | DD=54.25% | Turnover=26.01%
   🎚️ Intra-Step TAPE: potential=0.2526 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0127 | critic_loss=0.0352 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0176 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=3.14 | std=2.63 | range=[1.20, 19.29]
   🏷️ Alpha Per-Asset  TOP: NVDA=7.30 | AMZN=6.12 | JPM=4.12  BOT: XOM=1.76 | PG=1.70 | JNJ=1.66
   🧭 Regime Start Dist (train resets): high_vol=90 (38.8%), low_vol=70 (30.2%), medium_vol=72 (31.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.26% / trig 21.00%) | terminal=3.136 (peak 4.339) | TAPE=0.2277
   📊 Episode CVaR: regime=high | CVaR=-0.04791 | threshold=-0.02400 | passed=❌ | bonus=-2.39
[CYCLE] Update 183/348 | Step 201,600/500,000 | Episode 228 | Time: 11177.6s
   📊 Metrics: Return=+19.11% | Sharpe=0.385 | DD=12.77% | Turnover=31.00%
   🎚️ Intra-Step TAPE: potential=0.3377 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0106 | critic_loss=0.0176 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0088 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 184/348 | Step 203,112/500,000 | Episode 232 | Time: 11261.7s
   📊 Metrics: Return=+22.80% | Sharpe=0.256 | DD=57.02% | Turnover=25.20%
   🎚️ Intra-Step TAPE: potential=0.7021 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0002 | critic_loss=0.0386 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0193 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.23 | std=1.91 | range=[0.82, 14.92]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.45 | AMZN=3.63 | JPM=2.58  BOT: XOM=1.48 | PG=1.31 | JNJ=1.29
   🧭 Regime Start Dist (train resets): high_vol=92 (39.0%), low_vol=72 (30.5%), medium_vol=72 (30.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.98% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2411
   📊 Episode CVaR: regime=high | CVaR=-0.04536 | threshold=-0.02400 | passed=❌ | bonus=-2.14
[CYCLE] Update 185/348 | Step 204,624/500,000 | Episode 232 | Time: 11345.7s
   📊 Metrics: Return=+1.45% | Sharpe=0.175 | DD=48.14% | Turnover=28.27%
   🎚️ Intra-Step TAPE: potential=0.6070 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0066 | critic_loss=0.0422 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0211 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 186/348 | Step 206,136/500,000 | Episode 232 | Time: 11429.1s
   📊 Metrics: Return=+7.70% | Sharpe=0.172 | DD=48.14% | Turnover=31.52%
   🎚️ Intra-Step TAPE: potential=0.2232 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0123 | critic_loss=0.0373 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0187 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.86 | std=1.61 | range=[0.73, 11.60]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.74 | JPM=2.93 | AMZN=2.50  BOT: PG=1.08 | JNJ=1.06 | GLD=1.04
   🧭 Regime Start Dist (train resets): high_vol=92 (39.0%), low_vol=72 (30.5%), medium_vol=72 (30.5%)
[CYCLE] Update 187/348 | Step 207,648/500,000 | Episode 236 | Time: 11512.9s
   📊 Metrics: Return=+30.11% | Sharpe=0.303 | DD=53.86% | Turnover=30.86%
   🎚️ Intra-Step TAPE: potential=0.2266 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0085 | critic_loss=0.0800 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0400 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.036 (peak 0.922, dd 6.09% / trig 21.00%) | terminal=4.815 (peak 5.000) | TAPE=0.2433
   📊 Episode CVaR: regime=high | CVaR=-0.04545 | threshold=-0.02400 | passed=❌ | bonus=-2.15
[CYCLE] Update 188/348 | Step 209,160/500,000 | Episode 236 | Time: 11596.9s
   📊 Metrics: Return=+16.75% | Sharpe=0.406 | DD=15.57% | Turnover=50.69%
   🎚️ Intra-Step TAPE: potential=0.2316 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0114 | critic_loss=0.0690 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0345 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=0.70 | std=0.83 | range=[0.37, 9.57]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.95 | AMZN=0.98 | JPM=0.59  BOT: PG=0.49 | JNJ=0.48 | XOM=0.47
   🧭 Regime Start Dist (train resets): high_vol=95 (39.6%), low_vol=73 (30.4%), medium_vol=72 (30.0%)
[CYCLE] Update 189/348 | Step 210,672/500,000 | Episode 236 | Time: 11680.5s
   📊 Metrics: Return=+57.77% | Sharpe=0.771 | DD=15.57% | Turnover=48.80%
   🎚️ Intra-Step TAPE: potential=0.2157 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0163 | critic_loss=0.0990 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0495 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00237_shp0p799_actor.weights.h5 (Sharpe=0.799, MDD=15.57%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00239_shp0p732_actor.weights.h5 (Sharpe=0.732, MDD=24.21%)
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 240 | Time: 11763.1s
   📊 Metrics: Return=+50.22% | Sharpe=0.552 | DD=23.82% | Turnover=44.01%
   🎚️ Intra-Step TAPE: potential=0.2370 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0093 | critic_loss=0.2629 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1314 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.20 | std=1.18 | range=[0.44, 9.20]
   🏷️ Alpha Per-Asset  TOP: NVDA=3.02 | JPM=2.06 | AMZN=1.29  BOT: PG=0.67 | JNJ=0.66 | GLD=0.64
   🧭 Regime Start Dist (train resets): high_vol=98 (40.2%), low_vol=74 (30.3%), medium_vol=72 (29.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 10.71% / trig 21.00%) | terminal=0.000 (peak 3.611) | TAPE=0.3003
   📊 Episode CVaR: regime=mid | CVaR=-0.02436 | threshold=-0.01700 | passed=❌ | bonus=-0.74
[CYCLE] Update 191/348 | Step 213,696/500,000 | Episode 240 | Time: 11844.4s
   📊 Metrics: Return=+54.83% | Sharpe=0.973 | DD=13.26% | Turnover=46.50%
   🎚️ Intra-Step TAPE: potential=0.7487 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0086 | critic_loss=0.0219 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0110 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00241_shp1p021_actor.weights.h5 (Sharpe=1.021, MDD=13.26%)
[CYCLE] Update 192/348 | Step 215,208/500,000 | Episode 244 | Time: 11928.0s
   📊 Metrics: Return=+27.22% | Sharpe=0.285 | DD=40.87% | Turnover=39.77%
   🎚️ Intra-Step TAPE: potential=0.7030 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0022 | critic_loss=0.0928 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0464 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.44 | std=1.43 | range=[0.67, 13.13]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.05 | AMZN=1.84 | JPM=1.65  BOT: JNJ=0.90 | PG=0.89 | XOM=0.84
   🧭 Regime Start Dist (train resets): high_vol=98 (39.5%), low_vol=75 (30.2%), medium_vol=75 (30.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.57% / trig 21.00%) | terminal=0.000 (peak 0.577) | TAPE=0.2406
   📊 Episode CVaR: regime=high | CVaR=-0.04631 | threshold=-0.02400 | passed=❌ | bonus=-2.23
[CYCLE] Update 193/348 | Step 216,720/500,000 | Episode 244 | Time: 12011.8s
   📊 Metrics: Return=+34.31% | Sharpe=0.875 | DD=15.07% | Turnover=32.36%
   🎚️ Intra-Step TAPE: potential=0.2293 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0074 | critic_loss=0.0847 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0423 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 194/348 | Step 218,232/500,000 | Episode 244 | Time: 12094.9s
   📊 Metrics: Return=+111.86% | Sharpe=1.135 | DD=15.07% | Turnover=31.24%
   🎚️ Intra-Step TAPE: potential=0.2846 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0037 | critic_loss=0.0241 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0120 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.59 | std=1.98 | range=[0.57, 14.86]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.84 | AMZN=3.26 | JPM=1.60  BOT: GLD=0.80 | PG=0.73 | JNJ=0.72
   🧭 Regime Start Dist (train resets): high_vol=98 (39.5%), low_vol=75 (30.2%), medium_vol=75 (30.2%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00248_shp0p828_actor.weights.h5 (Sharpe=0.828, MDD=11.36%)
[CYCLE] Update 195/348 | Step 219,744/500,000 | Episode 248 | Time: 12177.2s
   📊 Metrics: Return=+64.15% | Sharpe=0.828 | DD=11.36% | Turnover=40.29%
   🎚️ Intra-Step TAPE: potential=0.2549 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0115 | critic_loss=0.1254 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0627 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.083, dd 2.91% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4508
   📊 Episode CVaR: regime=mid | CVaR=-0.01921 | threshold=-0.01700 | passed=❌ | bonus=-0.22
[CYCLE] Update 196/348 | Step 221,256/500,000 | Episode 248 | Time: 12258.6s
   📊 Metrics: Return=-1.11% | Sharpe=-0.028 | DD=19.52% | Turnover=37.12%
   🎚️ Intra-Step TAPE: potential=0.2712 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0102 | critic_loss=0.0145 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0072 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.76 | std=1.65 | range=[0.76, 15.61]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.20 | AMZN=3.15 | JPM=1.99  BOT: XOM=0.99 | PG=0.99 | JNJ=0.94
   🧭 Regime Start Dist (train resets): high_vol=98 (38.9%), low_vol=77 (30.6%), medium_vol=77 (30.6%)
[CYCLE] Update 197/348 | Step 222,768/500,000 | Episode 248 | Time: 12339.6s
   📊 Metrics: Return=+2.17% | Sharpe=0.005 | DD=19.52% | Turnover=37.38%
   🎚️ Intra-Step TAPE: potential=0.4693 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0123 | critic_loss=0.0230 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0115 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00251_shp1p195_actor.weights.h5 (Sharpe=1.195, MDD=14.25%)
[CYCLE] Update 198/348 | Step 224,280/500,000 | Episode 252 | Time: 12421.2s
   📊 Metrics: Return=+0.16% | Sharpe=-0.028 | DD=24.05% | Turnover=37.23%
   🎚️ Intra-Step TAPE: potential=0.7084 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0135 | critic_loss=0.0331 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0165 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.99 | std=1.81 | range=[0.83, 13.45]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.62 | AMZN=3.81 | JPM=2.36  BOT: NEE=1.19 | PG=1.07 | JNJ=1.05
   🧭 Regime Start Dist (train resets): high_vol=101 (39.5%), low_vol=78 (30.5%), medium_vol=77 (30.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.06% / trig 21.00%) | terminal=0.000 (peak 0.004) | TAPE=0.2250
   📊 Episode CVaR: regime=mid | CVaR=-0.02566 | threshold=-0.01700 | passed=❌ | bonus=-0.87
[CYCLE] Update 199/348 | Step 225,792/500,000 | Episode 252 | Time: 12502.0s
   📊 Metrics: Return=+82.29% | Sharpe=1.365 | DD=11.69% | Turnover=36.39%
   🎚️ Intra-Step TAPE: potential=0.7447 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0111 | critic_loss=0.0114 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0057 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00253_shp1p272_actor.weights.h5 (Sharpe=1.272, MDD=11.69%)
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 256 | Time: 12583.9s
   📊 Metrics: Return=+3.94% | Sharpe=0.132 | DD=50.75% | Turnover=31.56%
   🎚️ Intra-Step TAPE: potential=0.2381 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0121 | critic_loss=0.0310 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0155 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.64 | std=1.63 | range=[0.73, 12.88]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.81 | AMZN=2.04 | JPM=1.93  BOT: XOM=0.96 | PG=0.94 | JNJ=0.93
   🧭 Regime Start Dist (train resets): high_vol=102 (39.2%), low_vol=79 (30.4%), medium_vol=79 (30.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.03% / trig 21.00%) | terminal=1.052 (peak 2.644) | TAPE=0.2285
   📊 Episode CVaR: regime=high | CVaR=-0.04832 | threshold=-0.02400 | passed=❌ | bonus=-2.43
[CYCLE] Update 201/348 | Step 228,816/500,000 | Episode 256 | Time: 12665.1s
   📊 Metrics: Return=+46.95% | Sharpe=1.295 | DD=11.59% | Turnover=40.32%
   🎚️ Intra-Step TAPE: potential=0.7189 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0132 | critic_loss=0.0115 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0057 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 202/348 | Step 230,328/500,000 | Episode 256 | Time: 12746.1s
   📊 Metrics: Return=+134.28% | Sharpe=1.631 | DD=11.59% | Turnover=39.90%
   🎚️ Intra-Step TAPE: potential=0.5773 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0089 | critic_loss=0.0139 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0069 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.37 | std=1.45 | range=[0.61, 10.78]
   🏷️ Alpha Per-Asset  TOP: NVDA=3.60 | AMZN=2.18 | JPM=1.55  BOT: XOM=0.78 | PG=0.75 | JNJ=0.74
   🧭 Regime Start Dist (train resets): high_vol=102 (39.2%), low_vol=79 (30.4%), medium_vol=79 (30.4%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00257_shp1p327_actor.weights.h5 (Sharpe=1.327, MDD=11.59%)
[CYCLE] Update 203/348 | Step 231,840/500,000 | Episode 260 | Time: 12827.5s
   📊 Metrics: Return=+28.18% | Sharpe=0.368 | DD=12.84% | Turnover=41.45%
   🎚️ Intra-Step TAPE: potential=0.4692 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0071 | critic_loss=0.1385 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0692 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.48% / trig 21.00%) | terminal=0.000 (peak 0.789) | TAPE=0.2825
   📊 Episode CVaR: regime=mid | CVaR=-0.01987 | threshold=-0.01700 | passed=❌ | bonus=-0.29
[CYCLE] Update 204/348 | Step 233,352/500,000 | Episode 260 | Time: 12908.7s
   📊 Metrics: Return=+70.71% | Sharpe=1.284 | DD=14.67% | Turnover=33.48%
   🎚️ Intra-Step TAPE: potential=0.7286 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0132 | critic_loss=0.0580 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0290 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.48 | std=1.47 | range=[0.63, 12.79]
   🏷️ Alpha Per-Asset  TOP: NVDA=3.63 | AMZN=2.82 | GLD=1.42  BOT: XOM=0.83 | PG=0.82 | JNJ=0.81
   🧭 Regime Start Dist (train resets): high_vol=105 (39.8%), low_vol=80 (30.3%), medium_vol=79 (29.9%)
[CYCLE] Update 205/348 | Step 234,864/500,000 | Episode 260 | Time: 12989.6s
   📊 Metrics: Return=+87.21% | Sharpe=0.814 | DD=26.74% | Turnover=32.37%
   🎚️ Intra-Step TAPE: potential=0.3718 | delta_reward=-0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0090 | critic_loss=0.0171 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0086 | risk_aux_total=0.0005 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0005 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 206/348 | Step 236,376/500,000 | Episode 264 | Time: 13071.4s
   📊 Metrics: Return=+51.79% | Sharpe=0.667 | DD=11.44% | Turnover=40.63%
   🎚️ Intra-Step TAPE: potential=0.3007 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0108 | critic_loss=0.0599 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0299 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.65 | std=1.47 | range=[0.59, 10.73]
   🏷️ Alpha Per-Asset  TOP: NVDA=3.85 | AMZN=3.18 | JPM=2.04  BOT: NEE=1.00 | PG=0.88 | JNJ=0.86
   🧭 Regime Start Dist (train resets): high_vol=108 (40.3%), low_vol=80 (29.9%), medium_vol=80 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.284, dd 0.41% / trig 21.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3707
   📊 Episode CVaR: regime=mid | CVaR=-0.02006 | threshold=-0.01700 | passed=❌ | bonus=-0.31
[CYCLE] Update 207/348 | Step 237,888/500,000 | Episode 264 | Time: 13153.5s
   📊 Metrics: Return=+3.99% | Sharpe=0.017 | DD=11.20% | Turnover=38.96%
   🎚️ Intra-Step TAPE: potential=0.2940 | delta_reward=-0.0024
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0088 | critic_loss=0.0141 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0071 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 208/348 | Step 239,400/500,000 | Episode 268 | Time: 13237.0s
   📊 Metrics: Return=+20.98% | Sharpe=0.247 | DD=57.77% | Turnover=34.30%
   🎚️ Intra-Step TAPE: potential=0.2640 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0155 | critic_loss=0.0340 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0170 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.27 | std=1.17 | range=[0.57, 10.03]
   🏷️ Alpha Per-Asset  TOP: NVDA=3.75 | AMZN=1.48 | JPM=1.42  BOT: NEE=0.80 | PG=0.72 | JNJ=0.71
   🧭 Regime Start Dist (train resets): high_vol=109 (40.1%), low_vol=81 (29.8%), medium_vol=82 (30.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.90% / trig 21.00%) | terminal=4.684 (peak 5.000) | TAPE=0.2371
   📊 Episode CVaR: regime=high | CVaR=-0.04632 | threshold=-0.02400 | passed=❌ | bonus=-2.23

📚 EPISODE HORIZON UPDATE at 240,912 steps:
   Episode horizon: 1053 steps
[CYCLE] Update 209/348 | Step 240,912/500,000 | Episode 268 | Time: 13320.9s
   📊 Metrics: Return=+51.23% | Sharpe=1.371 | DD=11.25% | Turnover=44.99%
   🎚️ Intra-Step TAPE: potential=0.7328 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0126 | critic_loss=0.0317 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0158 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500

📚 EPISODE HORIZON UPDATE at 242,424 steps:
   Episode horizon: 1127 steps
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 268 | Time: 13405.3s
   📊 Metrics: Return=+102.15% | Sharpe=1.340 | DD=11.25% | Turnover=43.73%
   🎚️ Intra-Step TAPE: potential=0.3454 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0038 | critic_loss=0.0197 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0099 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.34 | std=1.47 | range=[0.51, 10.82]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.45 | JPM=2.09 | CAT=1.29  BOT: GLD=0.71 | JNJ=0.66 | PG=0.66
   🧭 Regime Start Dist (train resets): high_vol=109 (40.1%), low_vol=81 (29.8%), medium_vol=82 (30.1%)

📚 EPISODE HORIZON UPDATE at 243,936 steps:
   Episode horizon: 1202 steps
[CYCLE] Update 211/348 | Step 243,936/500,000 | Episode 272 | Time: 13488.4s
   📊 Metrics: Return=-3.40% | Sharpe=0.068 | DD=58.15% | Turnover=36.29%
   🎚️ Intra-Step TAPE: potential=0.2852 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0139 | critic_loss=0.0468 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0234 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.52% / trig 21.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2224
   📊 Episode CVaR: regime=high | CVaR=-0.04602 | threshold=-0.02400 | passed=❌ | bonus=-2.20

📚 EPISODE HORIZON UPDATE at 245,448 steps:
   Episode horizon: 1276 steps
[CYCLE] Update 212/348 | Step 245,448/500,000 | Episode 272 | Time: 13570.7s
   📊 Metrics: Return=+9.83% | Sharpe=0.255 | DD=14.69% | Turnover=43.50%
   🎚️ Intra-Step TAPE: potential=0.2883 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0064 | critic_loss=0.0128 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0064 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.08 | std=1.18 | range=[0.40, 9.62]
   🏷️ Alpha Per-Asset  TOP: NVDA=2.68 | AMZN=2.55 | JPM=1.33  BOT: NEE=0.58 | PG=0.51 | JNJ=0.51
   🧭 Regime Start Dist (train resets): high_vol=110 (39.9%), low_vol=81 (29.3%), medium_vol=85 (30.8%)

📚 EPISODE HORIZON UPDATE at 246,960 steps:
   Episode horizon: 1350 steps
[CYCLE] Update 213/348 | Step 246,960/500,000 | Episode 272 | Time: 13653.0s
   📊 Metrics: Return=+10.66% | Sharpe=0.144 | DD=14.69% | Turnover=44.37%
   🎚️ Intra-Step TAPE: potential=0.5071 | delta_reward=+0.0026
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0137 | critic_loss=0.0112 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0056 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500

📚 EPISODE HORIZON UPDATE at 248,472 steps:
   Episode horizon: 1425 steps
[CYCLE] Update 214/348 | Step 248,472/500,000 | Episode 272 | Time: 13736.2s
   📊 Metrics: Return=+52.01% | Sharpe=0.493 | DD=14.69% | Turnover=44.13%
   🎚️ Intra-Step TAPE: potential=0.7303 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0090 | critic_loss=0.0286 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0143 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.45 | std=1.86 | range=[0.42, 13.37]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.23 | JPM=2.24 | AMZN=1.50  BOT: NEE=0.67 | PG=0.57 | JNJ=0.56
   🧭 Regime Start Dist (train resets): high_vol=110 (39.9%), low_vol=81 (29.3%), medium_vol=85 (30.8%)

📚 EPISODE HORIZON UPDATE at 249,984 steps:
   Episode horizon: 1499 steps
[CYCLE] Update 215/348 | Step 249,984/500,000 | Episode 276 | Time: 13818.0s
   📊 Metrics: Return=+69.93% | Sharpe=0.395 | DD=59.78% | Turnover=36.05%
   🎚️ Intra-Step TAPE: potential=0.7356 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0098 | critic_loss=0.0404 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0202 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=4.298 (peak 5.000) | TAPE=0.2580
   📊 Episode CVaR: regime=high | CVaR=-0.04459 | threshold=-0.02400 | passed=❌ | bonus=-2.06

📚 EPISODE HORIZON UPDATE at 251,496 steps:
   Episode horizon: 1500 steps
[CYCLE] Update 216/348 | Step 251,496/500,000 | Episode 276 | Time: 13900.1s
   📊 Metrics: Return=-16.00% | Sharpe=-0.048 | DD=56.07% | Turnover=31.77%
   🎚️ Intra-Step TAPE: potential=0.4405 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0076 | critic_loss=0.0198 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0099 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.50 | std=1.86 | range=[0.43, 10.44]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.83 | AMZN=2.97 | JPM=2.10  BOT: NEE=0.70 | PG=0.57 | JNJ=0.55
   🧭 Regime Start Dist (train resets): high_vol=111 (39.6%), low_vol=83 (29.6%), medium_vol=86 (30.7%)
[CYCLE] Update 217/348 | Step 253,008/500,000 | Episode 276 | Time: 13982.6s
   📊 Metrics: Return=+28.97% | Sharpe=0.313 | DD=56.07% | Turnover=32.04%
   🎚️ Intra-Step TAPE: potential=0.7289 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0114 | critic_loss=0.0328 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0164 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 218/348 | Step 254,520/500,000 | Episode 276 | Time: 14066.0s
   📊 Metrics: Return=+58.32% | Sharpe=0.373 | DD=56.07% | Turnover=33.11%
   🎚️ Intra-Step TAPE: potential=0.7490 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0088 | critic_loss=0.0345 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0172 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.65 | std=2.27 | range=[0.55, 13.98]
   🏷️ Alpha Per-Asset  TOP: NVDA=7.37 | JPM=1.51 | CAT=1.46  BOT: XOM=0.82 | JNJ=0.81 | PG=0.76
   🧭 Regime Start Dist (train resets): high_vol=111 (39.6%), low_vol=83 (29.6%), medium_vol=86 (30.7%)
[CYCLE] Update 219/348 | Step 256,032/500,000 | Episode 280 | Time: 14149.5s
   📊 Metrics: Return=+67.20% | Sharpe=0.371 | DD=56.00% | Turnover=33.04%
   🎚️ Intra-Step TAPE: potential=0.2313 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0085 | critic_loss=0.0377 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0189 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=1.272 (peak 2.028, dd 8.31% / trig 21.00%) | terminal=3.324 (peak 5.000) | TAPE=0.2545
   📊 Episode CVaR: regime=high | CVaR=-0.04436 | threshold=-0.02400 | passed=❌ | bonus=-2.04
[CYCLE] Update 220/348 | Step 257,544/500,000 | Episode 280 | Time: 14231.0s
   📊 Metrics: Return=+8.44% | Sharpe=0.186 | DD=13.61% | Turnover=35.63%
   🎚️ Intra-Step TAPE: potential=0.2370 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0150 | critic_loss=0.0335 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0167 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.16 | std=2.44 | range=[0.57, 14.36]
   🏷️ Alpha Per-Asset  TOP: NVDA=6.16 | JPM=4.35 | CAT=2.67  BOT: XOM=0.96 | PG=0.80 | JNJ=0.77
   🧭 Regime Start Dist (train resets): high_vol=113 (39.8%), low_vol=85 (29.9%), medium_vol=86 (30.3%)
[CYCLE] Update 221/348 | Step 259,056/500,000 | Episode 280 | Time: 14311.6s
   📊 Metrics: Return=+15.22% | Sharpe=0.197 | DD=13.61% | Turnover=36.29%
   🎚️ Intra-Step TAPE: potential=0.7445 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0084 | critic_loss=0.0303 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0151 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 222/348 | Step 260,568/500,000 | Episode 280 | Time: 14392.4s
   📊 Metrics: Return=+73.02% | Sharpe=0.664 | DD=13.61% | Turnover=37.34%
   🎚️ Intra-Step TAPE: potential=0.7499 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0193 | critic_loss=0.0237 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0119 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.36 | std=1.67 | range=[0.47, 14.87]
   🏷️ Alpha Per-Asset  TOP: NVDA=4.86 | JPM=1.65 | CAT=1.53  BOT: NEE=0.63 | PG=0.63 | JNJ=0.60
   🧭 Regime Start Dist (train resets): high_vol=113 (39.8%), low_vol=85 (29.9%), medium_vol=86 (30.3%)
[CYCLE] Update 223/348 | Step 262,080/500,000 | Episode 284 | Time: 14476.7s
   📊 Metrics: Return=+29.90% | Sharpe=0.228 | DD=50.51% | Turnover=31.92%
   🎚️ Intra-Step TAPE: potential=0.7508 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0085 | critic_loss=0.0334 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0167 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 21.00%) | terminal=2.013 (peak 4.745) | TAPE=0.2375
   📊 Episode CVaR: regime=high | CVaR=-0.04366 | threshold=-0.02400 | passed=❌ | bonus=-1.97
[CYCLE] Update 224/348 | Step 263,592/500,000 | Episode 284 | Time: 14560.0s
   📊 Metrics: Return=-3.85% | Sharpe=-0.046 | DD=29.33% | Turnover=35.77%
   🎚️ Intra-Step TAPE: potential=0.2376 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0061 | critic_loss=0.0192 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0096 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.69 | std=2.22 | range=[0.52, 15.96]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.12 | AMZN=2.91 | JPM=2.51  BOT: XOM=0.75 | PG=0.69 | JNJ=0.66
   🧭 Regime Start Dist (train resets): high_vol=113 (39.2%), low_vol=87 (30.2%), medium_vol=88 (30.6%)
[CYCLE] Update 225/348 | Step 265,104/500,000 | Episode 284 | Time: 14644.0s
   📊 Metrics: Return=+4.81% | Sharpe=0.059 | DD=29.33% | Turnover=37.32%
   🎚️ Intra-Step TAPE: potential=0.2956 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0138 | critic_loss=0.0094 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0047 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 226/348 | Step 266,616/500,000 | Episode 284 | Time: 14727.8s
   📊 Metrics: Return=+3.50% | Sharpe=0.013 | DD=29.33% | Turnover=38.61%
   🎚️ Intra-Step TAPE: potential=0.2407 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0118 | critic_loss=0.0170 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0085 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.51 | std=1.84 | range=[0.50, 15.16]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.02 | JPM=1.80 | AMZN=1.79  BOT: NEE=0.78 | PG=0.71 | JNJ=0.70
   🧭 Regime Start Dist (train resets): high_vol=113 (39.2%), low_vol=87 (30.2%), medium_vol=88 (30.6%)
[CYCLE] Update 227/348 | Step 268,128/500,000 | Episode 288 | Time: 14812.0s
   📊 Metrics: Return=+71.77% | Sharpe=0.587 | DD=12.05% | Turnover=40.39%
   🎚️ Intra-Step TAPE: potential=0.2322 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0126 | critic_loss=0.0415 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0208 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 18.78% / trig 21.00%) | terminal=0.000 (peak 1.509) | TAPE=0.3296
   📊 Episode CVaR: regime=mid | CVaR=-0.01982 | threshold=-0.01700 | passed=❌ | bonus=-0.28
[CYCLE] Update 228/348 | Step 269,640/500,000 | Episode 288 | Time: 14896.5s
   📊 Metrics: Return=+7.46% | Sharpe=0.233 | DD=58.25% | Turnover=27.08%
   🎚️ Intra-Step TAPE: potential=0.6264 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0086 | critic_loss=0.0125 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0062 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.91 | std=2.73 | range=[0.46, 19.91]
   🏷️ Alpha Per-Asset  TOP: NVDA=5.71 | AMZN=3.28 | JPM=2.88  BOT: NEE=0.75 | PG=0.67 | JNJ=0.62
   🧭 Regime Start Dist (train resets): high_vol=114 (39.0%), low_vol=87 (29.8%), medium_vol=91 (31.2%)
[CYCLE] Update 229/348 | Step 271,152/500,000 | Episode 288 | Time: 14979.6s
   📊 Metrics: Return=+49.16% | Sharpe=0.413 | DD=58.25% | Turnover=29.64%
   🎚️ Intra-Step TAPE: potential=0.7524 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0095 | critic_loss=0.0173 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0086 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 230/348 | Step 272,664/500,000 | Episode 288 | Time: 15063.2s
   📊 Metrics: Return=+28.66% | Sharpe=0.245 | DD=58.25% | Turnover=31.16%
   🎚️ Intra-Step TAPE: potential=0.2379 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0100 | critic_loss=0.0156 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0078 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.27 | std=1.24 | range=[0.57, 12.67]
   🏷️ Alpha Per-Asset  TOP: NVDA=3.61 | JPM=1.41 | CAT=1.34  BOT: JNJ=0.87 | NEE=0.87 | MSFT=0.86
   🧭 Regime Start Dist (train resets): high_vol=114 (39.0%), low_vol=87 (29.8%), medium_vol=91 (31.2%)
[CYCLE] Update 231/348 | Step 274,176/500,000 | Episode 292 | Time: 15147.3s
   📊 Metrics: Return=+72.78% | Sharpe=0.545 | DD=28.83% | Turnover=40.12%
   🎚️ Intra-Step TAPE: potential=0.2206 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0148 | critic_loss=0.0551 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0276 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=1.662 (peak 2.589, dd 22.07% / trig 21.00%) | terminal=0.000 (peak 0.056) | TAPE=0.2866
   📊 Episode CVaR: regime=mid | CVaR=-0.02329 | threshold=-0.01700 | passed=❌ | bonus=-0.63
[CYCLE] Update 232/348 | Step 275,688/500,000 | Episode 292 | Time: 15230.1s
   📊 Metrics: Return=+9.80% | Sharpe=0.197 | DD=27.26% | Turnover=38.03%
   🎚️ Intra-Step TAPE: potential=0.4621 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0103 | critic_loss=0.0888 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0444 | risk_aux_total=0.0008 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0008 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.59 | std=2.23 | range=[0.55, 16.58]
   🏷️ Alpha Per-Asset  TOP: NVDA=6.23 | AMZN=2.27 | JPM=1.48  BOT: JNJ=0.78 | PG=0.77 | GLD=0.71
   🧭 Regime Start Dist (train resets): high_vol=117 (39.5%), low_vol=87 (29.4%), medium_vol=92 (31.1%)
[CYCLE] Update 233/348 | Step 277,200/500,000 | Episode 292 | Time: 15313.1s
   📊 Metrics: Return=+18.12% | Sharpe=0.214 | DD=27.26% | Turnover=37.50%
   🎚️ Intra-Step TAPE: potential=0.2197 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0114 | critic_loss=0.0158 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0079 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 234/348 | Step 278,712/500,000 | Episode 292 | Time: 15398.8s
   📊 Metrics: Return=+16.34% | Sharpe=0.136 | DD=27.26% | Turnover=39.77%
   🎚️ Intra-Step TAPE: potential=0.2310 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0102 | critic_loss=0.0248 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0124 | risk_aux_total=0.0006 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0006 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.13 | std=1.12 | range=[0.48, 12.75]
   🏷️ Alpha Per-Asset  TOP: NVDA=1.91 | AMZN=1.79 | JPM=1.43  BOT: XOM=0.75 | NEE=0.74 | JNJ=0.68
   🧭 Regime Start Dist (train resets): high_vol=117 (39.5%), low_vol=87 (29.4%), medium_vol=92 (31.1%)
[CYCLE] Update 235/348 | Step 280,224/500,000 | Episode 296 | Time: 15483.8s
   📊 Metrics: Return=+66.17% | Sharpe=0.374 | DD=51.56% | Turnover=35.67%
   🎚️ Intra-Step TAPE: potential=0.6387 | delta_reward=+0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0096 | critic_loss=0.0667 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0333 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.015, dd 15.04% / trig 21.00%) | terminal=4.152 (peak 4.152) | TAPE=0.2527
   📊 Episode CVaR: regime=high | CVaR=-0.04218 | threshold=-0.02400 | passed=❌ | bonus=-1.82
[CYCLE] Update 236/348 | Step 281,736/500,000 | Episode 296 | Time: 15568.1s
   📊 Metrics: Return=+13.45% | Sharpe=0.256 | DD=25.39% | Turnover=32.76%
   🎚️ Intra-Step TAPE: potential=0.2285 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0063 | critic_loss=0.0172 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0086 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.52 | std=2.96 | range=[0.63, 20.62]
   🏷️ Alpha Per-Asset  TOP: NVDA=8.15 | JPM=4.05 | AMZN=3.66  BOT: XOM=1.10 | PG=1.01 | JNJ=0.98
   🧭 Regime Start Dist (train resets): high_vol=117 (39.0%), low_vol=87 (29.0%), medium_vol=96 (32.0%)
[CYCLE] Update 237/348 | Step 283,248/500,000 | Episode 296 | Time: 15652.5s
   📊 Metrics: Return=+20.40% | Sharpe=0.242 | DD=25.39% | Turnover=32.52%
   🎚️ Intra-Step TAPE: potential=0.2434 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0136 | critic_loss=0.0164 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0082 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 238/348 | Step 284,760/500,000 | Episode 296 | Time: 15736.7s
   📊 Metrics: Return=+49.93% | Sharpe=0.401 | DD=25.39% | Turnover=32.45%
   🎚️ Intra-Step TAPE: potential=0.7446 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0122 | critic_loss=0.0153 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0076 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.10 | std=3.05 | range=[0.45, 22.50]
   🏷️ Alpha Per-Asset  TOP: NVDA=7.79 | CAT=2.88 | JPM=2.46  BOT: NEE=0.81 | PG=0.81 | JNJ=0.74
   🧭 Regime Start Dist (train resets): high_vol=117 (39.0%), low_vol=87 (29.0%), medium_vol=96 (32.0%)
[CYCLE] Update 239/348 | Step 286,272/500,000 | Episode 300 | Time: 15821.1s
   📊 Metrics: Return=+72.61% | Sharpe=0.388 | DD=54.27% | Turnover=29.51%
   🎚️ Intra-Step TAPE: potential=0.7528 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0041 | critic_loss=0.0462 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0231 | risk_aux_total=0.0007 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0007 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.05% / trig 21.00%) | terminal=2.503 (peak 4.098) | TAPE=0.2586
   📊 Episode CVaR: regime=high | CVaR=-0.04558 | threshold=-0.02400 | passed=❌ | bonus=-2.16