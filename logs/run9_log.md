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
   Gate A: enabled (Sharpe <= 0.00 or MDD >= 25.0% -> force non-positive terminal bonus)
   Neutral Band: enabled (±0.020 around baseline)
   [CYCLE] Profile Manager: disabled (static profile only)
[RAND] Experiment Seed: 6042 (Base: 42, Offset: 6000)
[OK] Features: Enhanced (includes 2 covariance eigenvalues)
   Eigenvalues: ['Covariance_Eigenvalue_0', 'Covariance_Eigenvalue_1']
   Train shape: (40473, 66)
   Test shape: (14230, 66)
   🧮 Actuarial columns: 4 detected (enabled=True) | total non-null=218812
      {'Actuarial_Expected_Recovery': 54703, 'Actuarial_Prob_30d': 54703, 'Actuarial_Prob_60d': 54703, 'Actuarial_Reserve_Severity': 54703}

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.35, band=±0.20, scalar=0.50 -> 0.75 => 0.90 => 1.00 => 1.00)
      ↳ Schedule: 0.50@0 => 0.75@100,000 => 0.90@200,000 => 1.00@300,000 => 1.00@400,000
   ⚙️  Component 4: Execution Inertia (beta=0.35 -> 0.45 => 0.55 => 0.55, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.35@0 => 0.45@100,000 => 0.55@200,000 => 0.55@350,000
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
      high_vol: 1341 dates (32.9%)
      low_vol: 1341 dates (32.9%)
      medium_vol: 1396 dates (34.2%)
   🧭 Regime start buckets (train env):
      high_vol: 1341 dates (32.9%)
      low_vol: 1341 dates (32.9%)
      medium_vol: 1396 dates (34.2%)
   [OK] Drawdown controller armed in env: target=15.00%, trigger=14.00%, λ_init=0.100, λ_floor=0.000, λ_max=5.00, penalty_coef=2.50
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
   🔀 Cross-Asset Mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Regime conditioning: enabled=False | mode=concat | hidden_dim=32 | dropout=0.0
   [DNA] State augmentation: enabled=False
   [DOWN] Distributional critic: enabled=True | num_quantiles=17
   🎛️ Dirichlet controls: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Dual-head consistency coef: 0.0
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0030
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@150,000 => 0.9980@350,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@150,000 => 0.9700@350,000
   🎯 Entropy coef schedule: 0.0030@0 => 0.0020@100,000 => 0.0015@250,000 => 0.0010@400,000
   🌡️ Temperature schedule: 1.2000@0 => 1.0000@150,000 => 0.9000@300,000
   📐 PPO rollout schedule: 1008@0 => 1512@150,000 => 2016@300,000
   🧺 PPO batch-size schedule: 252@0 => 336@150,000 => 504@300,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260312_160017_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260312_160017_step_diagnostics.csv

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
      0+ steps: scalar=0.50
      100,000+ steps: scalar=0.75
      200,000+ steps: scalar=0.90
      300,000+ steps: scalar=1.00
      400,000+ steps: scalar=1.00
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.35
      100,000+ steps: beta=0.45
      200,000+ steps: beta=0.55
      350,000+ steps: beta=0.55
   🏆 Deterministic-validation checkpoints: enabled (every 5 episodes | mode=mean | min_sharpe=0.50 | min_delta=0.000 | alpha_diag=True | horizon=scheduled (0@756 => 100,000@1008 => 250,000@1500 => 400,000@full))
      ↳ Multi-horizon selector: enabled (252:0.35, 504:0.30, 756:0.20, 1008:0.15) | dd_penalty_coef=0.250
      ↳ Stochastic sanity gate: enabled (runs=5, horizon=252, min_mean_sharpe=0.20, max_std=1.00)
      ↳ SPY outperformance gate: enabled (required>0.00% over the same validation horizon)
   🧷 Legacy checkpoint routes: disabled (high-watermark/step/periodic/tape/rare)
   [OK] Checkpoint selector default: deterministic validation multi-horizon composite score
   💾 High-watermark checkpoints: disabled
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260312_160017_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260312_160017_metadata.json
[CYCLE] Update 1/348 | Step 1,008/500,000 | Episode 0 | Time: 56.4s
   📊 Metrics: Return=+0.38% | Sharpe=0.042 | DD=18.50% | Turnover=9.85%
   🎚️ Intra-Step TAPE: potential=0.4169 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=1.3284 | critic_loss=0.3093 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1546 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01520
[CYCLE] Update 2/348 | Step 2,016/500,000 | Episode 0 | Time: 101.7s
   📊 Metrics: Return=+8.85% | Sharpe=0.215 | DD=18.50% | Turnover=9.29%
   🎚️ Intra-Step TAPE: potential=0.6885 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1834 | critic_loss=0.1707 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0853 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=8.54 | std=3.38 | range=[0.32, 16.00] | cap_hit=2.3%
   🏷️ Alpha Per-Asset  TOP: NVDA=11.94 | AMZN=10.68 | GLD=10.53  BOT: PG=8.24 | JNJ=7.88 | XOM=7.67
   🧭 Regime Start Dist (train resets): high_vol=1 (25.0%), low_vol=2 (50.0%), medium_vol=1 (25.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01745
[CYCLE] Update 3/348 | Step 3,024/500,000 | Episode 4 | Time: 146.0s
   📊 Metrics: Return=+47.65% | Sharpe=0.791 | DD=17.89% | Turnover=9.27%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1141 | critic_loss=0.2754 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1377 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.014 (peak 0.100) | TAPE=0.4231
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00508) | SPY bonus=0.021 (SPY ret=-0.01030)
[CYCLE] Update 4/348 | Step 4,032/500,000 | Episode 4 | Time: 190.4s
   📊 Metrics: Return=-19.35% | Sharpe=-0.293 | DD=42.59% | Turnover=11.39%
   🎚️ Intra-Step TAPE: potential=0.2684 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0959 | critic_loss=0.2944 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1472 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=3.74 | std=1.78 | range=[0.54, 11.75] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.67 | AMZN=5.43 | GLD=4.90  BOT: PG=3.19 | JNJ=3.19 | XOM=2.83
   🧭 Regime Start Dist (train resets): high_vol=3 (37.5%), low_vol=4 (50.0%), medium_vol=1 (12.5%)
   🔐 Lagrangian CVaR: λ=0.0081 | penalty=-0.0001 | rolling_cvar=-0.01882
[CYCLE] Update 5/348 | Step 5,040/500,000 | Episode 4 | Time: 232.2s
   📊 Metrics: Return=+26.69% | Sharpe=0.452 | DD=42.59% | Turnover=14.20%
   🎚️ Intra-Step TAPE: potential=0.2598 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0871 | critic_loss=0.1527 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0763 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0220 | penalty=-0.0006 | rolling_cvar=-0.02035
      🧪 Deterministic validation: Sharpe=0.828 | Return=+98.03% | DD=26.80%
         Multi-horizon: score=0.813 | details=252:0.847/26.8%, 504:1.109/26.8%, 756:0.633/26.8%, 1008:0.828/26.8%
         SPY relative: spy_return=+53.67% | outperformance=+44.36%
         Stochastic sanity: mean_sharpe=0.518 | std=0.627 | runs=5
      💾 Deterministic-validation checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00005_shp0p828_actor.weights.h5 (val_sharpe=0.828, score=0.813)
[CYCLE] Update 6/348 | Step 6,048/500,000 | Episode 8 | Time: 760.3s
   📊 Metrics: Return=+10.25% | Sharpe=0.168 | DD=43.59% | Turnover=16.62%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0776 | critic_loss=0.2874 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1437 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.11 | std=0.37 | range=[0.65, 3.18] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.83 | GLD=1.12 | AMZN=1.09  BOT: PG=0.92 | JNJ=0.91 | XOM=0.83
   🧭 Regime Start Dist (train resets): high_vol=6 (50.0%), low_vol=4 (33.3%), medium_vol=2 (16.7%)
   🔒 Drawdown λ snapshot=0.509 (peak 0.509, dd 0.00% / trig 14.00%) | terminal=1.560 (peak 1.560) | TAPE=0.2387
   🔐 Lagrangian CVaR: λ=0.0303 | penalty=-0.0008 | rolling_cvar=-0.03201
[CYCLE] Update 7/348 | Step 7,056/500,000 | Episode 8 | Time: 803.8s
   📊 Metrics: Return=-8.77% | Sharpe=-0.088 | DD=33.15% | Turnover=22.49%
   🎚️ Intra-Step TAPE: potential=0.6273 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0773 | critic_loss=0.2352 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1176 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0613 | penalty=-0.0025 | rolling_cvar=-0.02550
[CYCLE] Update 8/348 | Step 8,064/500,000 | Episode 8 | Time: 847.3s
   📊 Metrics: Return=+2.90% | Sharpe=0.130 | DD=33.15% | Turnover=22.97%
   🎚️ Intra-Step TAPE: potential=0.2404 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0693 | critic_loss=0.1824 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0912 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.16 | std=0.29 | range=[0.67, 3.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.34 | GLD=1.27 | AMZN=1.22  BOT: JNJ=1.02 | MSFT=0.99 | XOM=0.99
   🧭 Regime Start Dist (train resets): high_vol=6 (50.0%), low_vol=4 (33.3%), medium_vol=2 (16.7%)
   🔐 Lagrangian CVaR: λ=0.0836 | penalty=-0.0027 | rolling_cvar=-0.02677
      🧪 Deterministic validation: Sharpe=0.821 | Return=+91.42% | DD=26.26%
         Multi-horizon: score=0.817 | details=252:0.854/26.3%, 504:1.098/26.3%, 756:0.655/26.3%, 1008:0.821/26.3%
         SPY relative: spy_return=+53.67% | outperformance=+37.75%
         Stochastic sanity: mean_sharpe=-0.047 | std=0.434 | runs=5
         [WARN] Sanity gate rejected checkpoint (stochastic robustness failed).
[CYCLE] Update 9/348 | Step 9,072/500,000 | Episode 12 | Time: 1379.0s
   📊 Metrics: Return=+19.64% | Sharpe=0.328 | DD=18.80% | Turnover=23.56%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0781 | critic_loss=0.2248 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1124 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.096 (peak 0.096, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.624) | TAPE=0.2640
   🔐 Lagrangian CVaR: λ=0.0945 | penalty=-0.0022 | rolling_cvar=-0.02449
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 12 | Time: 1423.9s
   📊 Metrics: Return=+3.74% | Sharpe=0.226 | DD=8.31% | Turnover=23.21%
   🎚️ Intra-Step TAPE: potential=0.2585 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0704 | critic_loss=0.2334 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1167 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.13 | std=0.29 | range=[0.64, 3.15] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.46 | NVDA=1.26 | AMZN=1.14  BOT: MSFT=1.00 | XOM=0.98 | CAT=0.96
   🧭 Regime Start Dist (train resets): high_vol=6 (37.5%), low_vol=4 (25.0%), medium_vol=6 (37.5%)
   🔐 Lagrangian CVaR: λ=0.0753 | penalty=-0.0006 | rolling_cvar=-0.02729
[CYCLE] Update 11/348 | Step 11,088/500,000 | Episode 12 | Time: 1469.1s
   📊 Metrics: Return=+7.52% | Sharpe=0.203 | DD=9.03% | Turnover=24.16%
   🎚️ Intra-Step TAPE: potential=0.7402 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0735 | critic_loss=0.2468 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1234 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0462 | penalty=-0.0000 | rolling_cvar=-0.02308
      🧪 Deterministic validation: Sharpe=0.819 | Return=+90.88% | DD=25.93%
         Multi-horizon: score=0.822 | details=252:0.861/25.9%, 504:1.109/25.9%, 756:0.647/25.9%, 1008:0.819/25.9%
         SPY relative: spy_return=+53.67% | outperformance=+37.20%
         Stochastic sanity: mean_sharpe=0.443 | std=0.719 | runs=5
      💾 Deterministic-validation checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00015_shp0p819_actor.weights.h5 (val_sharpe=0.819, score=0.822)
[CYCLE] Update 12/348 | Step 12,096/500,000 | Episode 16 | Time: 2010.9s
   📊 Metrics: Return=+19.26% | Sharpe=0.347 | DD=15.39% | Turnover=24.37%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0701 | critic_loss=0.2735 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1367 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.86 | std=0.15 | range=[0.57, 1.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=0.94 | NVDA=0.91 | GLD=0.90  BOT: PG=0.82 | XOM=0.75 | CAT=0.72
   🧭 Regime Start Dist (train resets): high_vol=9 (45.0%), low_vol=4 (20.0%), medium_vol=7 (35.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 12 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2784
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00092) | SPY bonus=0.005 (SPY ret=-0.00234)
   🔐 Lagrangian CVaR: λ=0.0161 | penalty=0.0000 | rolling_cvar=-0.02084
[CYCLE] Update 13/348 | Step 13,104/500,000 | Episode 16 | Time: 2055.2s
   📊 Metrics: Return=-29.83% | Sharpe=-0.912 | DD=35.88% | Turnover=24.90%
   🎚️ Intra-Step TAPE: potential=0.2257 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0670 | critic_loss=0.3010 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1505 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0077 | penalty=-0.0001 | rolling_cvar=-0.01347
[CYCLE] Update 14/348 | Step 14,112/500,000 | Episode 16 | Time: 2099.2s
   📊 Metrics: Return=-3.16% | Sharpe=0.011 | DD=37.79% | Turnover=25.48%
   🎚️ Intra-Step TAPE: potential=0.2270 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0633 | critic_loss=0.1598 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0799 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.79 | std=0.21 | range=[0.53, 3.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.89 | GLD=0.84 | AMZN=0.77  BOT: JNJ=0.72 | XOM=0.70 | MSFT=0.69
   🧭 Regime Start Dist (train resets): high_vol=9 (45.0%), low_vol=4 (20.0%), medium_vol=7 (35.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 14 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0093 | penalty=-0.0003 | rolling_cvar=-0.01473
      🧪 Deterministic validation: Sharpe=0.821 | Return=+89.52% | DD=25.82%
         Multi-horizon: score=0.819 | details=252:0.854/25.8%, 504:1.107/25.8%, 756:0.647/25.8%, 1008:0.821/25.8%
         SPY relative: spy_return=+53.67% | outperformance=+35.84%
[CYCLE] Update 15/348 | Step 15,120/500,000 | Episode 20 | Time: 2477.8s
   📊 Metrics: Return=+30.86% | Sharpe=0.608 | DD=11.35% | Turnover=26.59%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0662 | critic_loss=0.1870 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0935 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.771 (peak 0.771, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3437
   🔐 Lagrangian CVaR: λ=0.0064 | penalty=-0.0002 | rolling_cvar=-0.01829
[CYCLE] Update 16/348 | Step 16,128/500,000 | Episode 20 | Time: 2523.9s
   📊 Metrics: Return=+9.00% | Sharpe=0.530 | DD=13.90% | Turnover=25.35%
   🎚️ Intra-Step TAPE: potential=0.7260 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0636 | critic_loss=0.1572 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0786 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.87 | std=0.21 | range=[0.53, 2.16] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.11 | NVDA=0.99 | AMZN=0.93  BOT: MSFT=0.79 | CAT=0.75 | XOM=0.75
   🧭 Regime Start Dist (train resets): high_vol=10 (41.7%), low_vol=6 (25.0%), medium_vol=8 (33.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 16 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01288
[CYCLE] Update 17/348 | Step 17,136/500,000 | Episode 20 | Time: 2568.3s
   📊 Metrics: Return=+21.68% | Sharpe=0.675 | DD=13.90% | Turnover=25.62%
   🎚️ Intra-Step TAPE: potential=0.5684 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0641 | critic_loss=0.1666 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0833 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 18/348 | Step 18,144/500,000 | Episode 24 | Time: 2612.7s
   📊 Metrics: Return=+61.20% | Sharpe=1.210 | DD=17.63% | Turnover=25.67%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0644 | critic_loss=0.2250 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1125 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.92 | std=0.25 | range=[0.62, 1.91] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=0.96 | NEE=0.96 | AMZN=0.90  BOT: MSFT=0.82 | JNJ=0.81 | XOM=0.76
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=9 (32.1%), medium_vol=9 (32.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.006) | TAPE=0.5272
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00962) | SPY bonus=0.004 (SPY ret=0.00662)
[CYCLE] Update 19/348 | Step 19,152/500,000 | Episode 24 | Time: 2656.9s
   📊 Metrics: Return=-1.51% | Sharpe=-0.317 | DD=8.12% | Turnover=25.87%
   🎚️ Intra-Step TAPE: potential=0.2504 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0676 | critic_loss=0.1196 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0598 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 2701.5s
   📊 Metrics: Return=+18.23% | Sharpe=0.631 | DD=12.79% | Turnover=25.21%
   🎚️ Intra-Step TAPE: potential=0.7249 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0653 | critic_loss=0.2105 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1053 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.01 | std=0.36 | range=[0.68, 2.76] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.99 | AMZN=0.97 | NEE=0.94  BOT: MSFT=0.89 | CAT=0.82 | XOM=0.82
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=9 (32.1%), medium_vol=9 (32.1%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03100
      🧪 Deterministic validation: Sharpe=0.825 | Return=+86.06% | DD=24.86%
         Multi-horizon: score=0.845 | details=252:0.897/24.9%, 504:1.120/24.9%, 756:0.669/24.9%, 1008:0.825/24.9%
         SPY relative: spy_return=+53.67% | outperformance=+32.39%
         Stochastic sanity: mean_sharpe=0.845 | std=0.918 | runs=5
      💾 Deterministic-validation checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp0p825_actor.weights.h5 (val_sharpe=0.825, score=0.845)
[CYCLE] Update 21/348 | Step 21,168/500,000 | Episode 28 | Time: 3239.9s
   📊 Metrics: Return=+7.92% | Sharpe=0.141 | DD=39.99% | Turnover=24.60%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0594 | critic_loss=0.1285 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0642 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=3.236 (peak 3.236) | TAPE=0.2347
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.02199) | SPY bonus=0.088 (SPY ret=-0.01143)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03529
[CYCLE] Update 22/348 | Step 22,176/500,000 | Episode 28 | Time: 3285.3s
   📊 Metrics: Return=+24.35% | Sharpe=1.532 | DD=7.89% | Turnover=24.08%
   🎚️ Intra-Step TAPE: potential=0.7325 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0617 | critic_loss=0.0806 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0403 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.29 | std=0.36 | range=[0.83, 3.14] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.30 | GLD=1.29 | PG=1.25  BOT: AMZN=1.14 | NVDA=1.13 | CAT=1.08
   🧭 Regime Start Dist (train resets): high_vol=11 (34.4%), low_vol=11 (34.4%), medium_vol=10 (31.2%)
   🔐 Lagrangian CVaR: λ=0.0094 | penalty=-0.0003 | rolling_cvar=-0.01362
[CYCLE] Update 23/348 | Step 23,184/500,000 | Episode 28 | Time: 3330.9s
   📊 Metrics: Return=+52.47% | Sharpe=1.773 | DD=7.89% | Turnover=23.53%
   🎚️ Intra-Step TAPE: potential=0.7370 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0608 | critic_loss=0.0749 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0375 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0076 | penalty=-0.0003 | rolling_cvar=-0.01419
      🧪 Deterministic validation: Sharpe=0.817 | Return=+78.72% | DD=23.34%
         Multi-horizon: score=0.858 | details=252:0.919/23.3%, 504:1.122/23.3%, 756:0.679/23.3%, 1008:0.817/23.3%
         SPY relative: spy_return=+53.67% | outperformance=+25.05%
         Stochastic sanity: mean_sharpe=-0.061 | std=0.625 | runs=5
         [WARN] Sanity gate rejected checkpoint (stochastic robustness failed).
[CYCLE] Update 24/348 | Step 24,192/500,000 | Episode 32 | Time: 3877.6s
   📊 Metrics: Return=+40.69% | Sharpe=0.869 | DD=10.47% | Turnover=22.76%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0646 | critic_loss=0.0836 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0418 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.41 | std=0.68 | range=[0.80, 4.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.37 | NEE=1.33 | PG=1.32  BOT: JPM=1.12 | CAT=1.11 | NVDA=1.02
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=14 (38.9%), medium_vol=10 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 1.295) | TAPE=0.4764
   🔐 Lagrangian CVaR: λ=0.0112 | penalty=-0.0003 | rolling_cvar=-0.01640
[CYCLE] Update 25/348 | Step 25,200/500,000 | Episode 32 | Time: 3921.9s
   📊 Metrics: Return=+19.09% | Sharpe=1.969 | DD=3.21% | Turnover=22.74%
   🎚️ Intra-Step TAPE: potential=0.3781 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0615 | critic_loss=0.0384 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0192 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0013 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01193
[CYCLE] Update 26/348 | Step 26,208/500,000 | Episode 32 | Time: 3965.9s
   📊 Metrics: Return=+32.37% | Sharpe=1.489 | DD=7.17% | Turnover=22.63%
   🎚️ Intra-Step TAPE: potential=0.2276 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0645 | critic_loss=0.0724 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0362 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0015 | dispersion_loss=0.0004
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.19 | std=1.04 | range=[0.61, 5.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=0.99 | JNJ=0.94 | PG=0.92  BOT: AMZN=0.82 | CAT=0.79 | NVDA=0.75
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=14 (38.9%), medium_vol=10 (27.8%)
      🧪 Deterministic validation: Sharpe=0.777 | Return=+62.77% | DD=20.35%
         Multi-horizon: score=0.827 | details=252:0.885/20.3%, 504:1.073/20.3%, 756:0.648/20.3%, 1008:0.777/20.3%
         SPY relative: spy_return=+53.67% | outperformance=+9.09%
[CYCLE] Update 27/348 | Step 27,216/500,000 | Episode 36 | Time: 4340.1s
   📊 Metrics: Return=+5.91% | Sharpe=0.036 | DD=9.55% | Turnover=22.02%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0650 | critic_loss=0.1339 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0669 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0014 | dispersion_loss=0.0005
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2500
[CYCLE] Update 28/348 | Step 28,224/500,000 | Episode 36 | Time: 4385.0s
   📊 Metrics: Return=-20.22% | Sharpe=-0.630 | DD=32.04% | Turnover=23.94%
   🎚️ Intra-Step TAPE: potential=0.3567 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0632 | critic_loss=0.1108 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0554 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0013 | dispersion_loss=0.0008
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.16 | std=0.82 | range=[0.66, 4.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=0.99 | PG=0.99 | NEE=0.98  BOT: CAT=0.83 | NVDA=0.82 | AMZN=0.80
   🧭 Regime Start Dist (train resets): high_vol=14 (35.0%), low_vol=15 (37.5%), medium_vol=11 (27.5%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01241
[CYCLE] Update 29/348 | Step 29,232/500,000 | Episode 36 | Time: 4430.1s
   📊 Metrics: Return=-8.22% | Sharpe=-0.148 | DD=32.04% | Turnover=23.16%
   🎚️ Intra-Step TAPE: potential=0.4293 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0610 | critic_loss=0.0530 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0265 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01166
      🧪 Deterministic validation: Sharpe=0.802 | Return=+73.28% | DD=22.72%
         Multi-horizon: score=0.836 | details=252:0.889/22.7%, 504:1.097/22.7%, 756:0.663/22.7%, 1008:0.802/22.7%
         SPY relative: spy_return=+53.67% | outperformance=+19.61%
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 4808.0s
   📊 Metrics: Return=+20.30% | Sharpe=0.525 | DD=8.97% | Turnover=22.90%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0627 | critic_loss=0.1072 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0536 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.51 | std=0.64 | range=[0.94, 4.28] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.44 | JNJ=1.43 | GLD=1.41  BOT: JPM=1.24 | AMZN=1.23 | NVDA=1.18
   🧭 Regime Start Dist (train resets): high_vol=14 (31.8%), low_vol=18 (40.9%), medium_vol=12 (27.3%)
   🔒 Drawdown λ snapshot=0.708 (peak 0.708, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3287
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01202
[CYCLE] Update 31/348 | Step 31,248/500,000 | Episode 40 | Time: 4853.4s
   📊 Metrics: Return=+17.74% | Sharpe=1.097 | DD=5.86% | Turnover=20.85%
   🎚️ Intra-Step TAPE: potential=0.2577 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0583 | critic_loss=0.0790 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0395 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 32/348 | Step 32,256/500,000 | Episode 40 | Time: 4898.7s
   📊 Metrics: Return=-4.03% | Sharpe=-0.047 | DD=33.65% | Turnover=21.27%
   🎚️ Intra-Step TAPE: potential=0.2345 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0626 | critic_loss=0.0977 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0489 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.32 | std=0.57 | range=[0.87, 3.98] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.42 | GLD=1.35 | PG=1.29  BOT: AMZN=1.04 | CAT=1.03 | NVDA=1.00
   🧭 Regime Start Dist (train resets): high_vol=14 (31.8%), low_vol=18 (40.9%), medium_vol=12 (27.3%)
   🔐 Lagrangian CVaR: λ=0.0060 | penalty=-0.0000 | rolling_cvar=-0.03731
[CYCLE] Update 33/348 | Step 33,264/500,000 | Episode 44 | Time: 4943.3s
   📊 Metrics: Return=+9.33% | Sharpe=0.155 | DD=34.83% | Turnover=22.03%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0582 | critic_loss=0.0258 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0129 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.631 (peak 0.631, dd 0.00% / trig 14.00%) | terminal=1.704 (peak 2.002) | TAPE=0.2351
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01873) | SPY bonus=0.023 (SPY ret=-0.02365)
   🔐 Lagrangian CVaR: λ=0.0273 | penalty=-0.0007 | rolling_cvar=-0.03296
[CYCLE] Update 34/348 | Step 34,272/500,000 | Episode 44 | Time: 4988.3s
   📊 Metrics: Return=+4.49% | Sharpe=0.283 | DD=8.16% | Turnover=22.46%
   🎚️ Intra-Step TAPE: potential=0.2334 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0634 | critic_loss=0.0314 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0157 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.37 | std=0.25 | range=[0.78, 2.36] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.46 | JNJ=1.45 | GLD=1.43  BOT: AMZN=1.24 | NVDA=1.19 | CAT=1.18
   🧭 Regime Start Dist (train resets): high_vol=16 (33.3%), low_vol=19 (39.6%), medium_vol=13 (27.1%)
   🔐 Lagrangian CVaR: λ=0.0189 | penalty=-0.0007 | rolling_cvar=-0.05157
[CYCLE] Update 35/348 | Step 35,280/500,000 | Episode 44 | Time: 5033.6s
   📊 Metrics: Return=+16.78% | Sharpe=0.627 | DD=8.16% | Turnover=22.54%
   🎚️ Intra-Step TAPE: potential=0.7340 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0613 | critic_loss=0.0288 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0144 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0078 | penalty=-0.0004 | rolling_cvar=-0.04274
      🧪 Deterministic validation: Sharpe=0.851 | Return=+91.05% | DD=24.87%
         Multi-horizon: score=0.889 | details=252:0.954/24.9%, 504:1.167/24.9%, 756:0.696/24.9%, 1008:0.851/24.9%
         SPY relative: spy_return=+53.67% | outperformance=+37.37%
         Stochastic sanity: mean_sharpe=1.341 | std=1.265 | runs=5
         [WARN] Sanity gate rejected checkpoint (stochastic robustness failed).
[CYCLE] Update 36/348 | Step 36,288/500,000 | Episode 48 | Time: 5574.8s
   📊 Metrics: Return=+11.81% | Sharpe=0.193 | DD=33.47% | Turnover=23.32%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0592 | critic_loss=0.0517 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0258 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.34 | std=0.16 | range=[1.01, 1.91] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.46 | PG=1.42 | JNJ=1.40  BOT: CAT=1.26 | JPM=1.26 | NVDA=1.19
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=21 (40.4%), medium_vol=14 (26.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 36 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.474 (peak 1.681) | TAPE=0.2383
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03739
[CYCLE] Update 37/348 | Step 37,296/500,000 | Episode 48 | Time: 5619.6s
   📊 Metrics: Return=+6.24% | Sharpe=0.453 | DD=6.35% | Turnover=22.46%
   🎚️ Intra-Step TAPE: potential=0.2436 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0595 | critic_loss=0.0477 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0238 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.01584
[CYCLE] Update 38/348 | Step 38,304/500,000 | Episode 48 | Time: 5664.6s
   📊 Metrics: Return=+23.48% | Sharpe=0.941 | DD=6.35% | Turnover=22.03%
   🎚️ Intra-Step TAPE: potential=0.5852 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0583 | critic_loss=0.0242 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0121 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.28 | std=0.18 | range=[0.65, 1.88] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.41 | JNJ=1.36 | JPM=1.32  BOT: AMZN=1.22 | CAT=1.17 | NVDA=1.12
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=21 (40.4%), medium_vol=14 (26.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 38 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01577
      🧪 Deterministic validation: Sharpe=0.837 | Return=+89.47% | DD=25.24%
         Multi-horizon: score=0.873 | details=252:0.937/25.2%, 504:1.149/25.2%, 756:0.688/25.2%, 1008:0.837/25.2%
         SPY relative: spy_return=+53.67% | outperformance=+35.79%
         Stochastic sanity: mean_sharpe=1.122 | std=0.235 | runs=5
      💾 Deterministic-validation checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00050_shp0p837_actor.weights.h5 (val_sharpe=0.837, score=0.873)
[CYCLE] Update 39/348 | Step 39,312/500,000 | Episode 52 | Time: 6205.7s
   📊 Metrics: Return=+24.07% | Sharpe=0.445 | DD=19.70% | Turnover=22.00%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0602 | critic_loss=0.0401 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0200 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.041 (peak 0.190) | TAPE=0.2879
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01973
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 52 | Time: 6249.8s
   📊 Metrics: Return=+0.05% | Sharpe=-0.119 | DD=13.34% | Turnover=21.69%
   🎚️ Intra-Step TAPE: potential=0.7310 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0599 | critic_loss=0.0325 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0163 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.12 | std=0.30 | range=[0.71, 2.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.51 | JNJ=1.13 | PG=1.12  BOT: AMZN=0.98 | NVDA=0.96 | CAT=0.95
   🧭 Regime Start Dist (train resets): high_vol=19 (33.9%), low_vol=21 (37.5%), medium_vol=16 (28.6%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01308
[CYCLE] Update 41/348 | Step 41,328/500,000 | Episode 52 | Time: 6294.3s
   📊 Metrics: Return=+19.47% | Sharpe=0.621 | DD=13.34% | Turnover=22.95%
   🎚️ Intra-Step TAPE: potential=0.3163 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0597 | critic_loss=0.0460 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0230 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01346
      🧪 Deterministic validation: Sharpe=0.830 | Return=+85.07% | DD=24.76%
         Multi-horizon: score=0.863 | details=252:0.921/24.8%, 504:1.132/24.8%, 756:0.690/24.8%, 1008:0.830/24.8%
         SPY relative: spy_return=+53.67% | outperformance=+31.40%
[CYCLE] Update 42/348 | Step 42,336/500,000 | Episode 56 | Time: 6664.9s
   📊 Metrics: Return=+13.27% | Sharpe=0.256 | DD=10.18% | Turnover=24.81%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0576 | critic_loss=0.0682 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0341 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.91 | std=0.21 | range=[0.64, 1.87] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.96 | JNJ=0.92 | PG=0.91  BOT: AMZN=0.82 | CAT=0.79 | NVDA=0.76
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=21 (35.0%), medium_vol=19 (31.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 42 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.017) | TAPE=0.2707
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01522
[CYCLE] Update 43/348 | Step 43,344/500,000 | Episode 56 | Time: 6710.2s
   📊 Metrics: Return=+1.57% | Sharpe=0.063 | DD=13.56% | Turnover=25.42%
   🎚️ Intra-Step TAPE: potential=0.5504 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0568 | critic_loss=0.0576 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0288 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0026 | penalty=-0.0000 | rolling_cvar=-0.01826
[CYCLE] Update 44/348 | Step 44,352/500,000 | Episode 56 | Time: 6755.4s
   📊 Metrics: Return=+3.99% | Sharpe=0.068 | DD=13.56% | Turnover=24.69%
   🎚️ Intra-Step TAPE: potential=0.5440 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0565 | critic_loss=0.0384 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0192 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.01 | std=0.48 | range=[0.62, 2.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.02 | PG=1.01 | NEE=0.97  BOT: JPM=0.76 | CAT=0.73 | NVDA=0.68
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=21 (35.0%), medium_vol=19 (31.7%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02075
      🧪 Deterministic validation: Sharpe=0.824 | Return=+77.92% | DD=23.14%
         Multi-horizon: score=0.868 | details=252:0.929/23.1%, 504:1.129/23.1%, 756:0.691/23.1%, 1008:0.824/23.1%
         SPY relative: spy_return=+53.67% | outperformance=+24.25%
[CYCLE] Update 45/348 | Step 45,360/500,000 | Episode 60 | Time: 7131.4s
   📊 Metrics: Return=+13.45% | Sharpe=0.239 | DD=16.12% | Turnover=25.59%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0561 | critic_loss=0.0374 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0187 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.004) | TAPE=0.2602
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01210) | SPY bonus=0.010 (SPY ret=-0.01435)
[CYCLE] Update 46/348 | Step 46,368/500,000 | Episode 60 | Time: 7176.5s
   📊 Metrics: Return=+9.57% | Sharpe=0.568 | DD=12.75% | Turnover=26.63%
   🎚️ Intra-Step TAPE: potential=0.2363 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0527 | critic_loss=0.0707 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0354 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.84 | std=0.24 | range=[0.60, 1.99] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=0.84 | GLD=0.84 | PG=0.84  BOT: JPM=0.74 | CAT=0.72 | NVDA=0.69
   🧭 Regime Start Dist (train resets): high_vol=22 (34.4%), low_vol=23 (35.9%), medium_vol=19 (29.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 46 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 47/348 | Step 47,376/500,000 | Episode 60 | Time: 7222.0s
   📊 Metrics: Return=+26.74% | Sharpe=0.816 | DD=14.48% | Turnover=26.56%
   🎚️ Intra-Step TAPE: potential=0.2374 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0586 | critic_loss=0.0945 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0473 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0029 | penalty=-0.0000 | rolling_cvar=-0.03990
[CYCLE] Update 48/348 | Step 48,384/500,000 | Episode 64 | Time: 7267.2s
   📊 Metrics: Return=+16.59% | Sharpe=0.250 | DD=39.36% | Turnover=26.29%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0508 | critic_loss=0.0422 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0211 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.93 | std=0.34 | range=[0.65, 2.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.97 | JNJ=0.91 | PG=0.89  BOT: CAT=0.76 | JPM=0.75 | NVDA=0.73
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=24 (35.3%), medium_vol=21 (30.9%)
   🔒 Drawdown λ snapshot=0.004 (peak 0.004, dd 0.00% / trig 14.00%) | terminal=2.451 (peak 2.563) | TAPE=0.2433
   🔐 Lagrangian CVaR: λ=0.0265 | penalty=-0.0005 | rolling_cvar=-0.03731
[CYCLE] Update 49/348 | Step 49,392/500,000 | Episode 64 | Time: 7312.3s
   📊 Metrics: Return=+8.10% | Sharpe=0.662 | DD=7.27% | Turnover=24.80%
   🎚️ Intra-Step TAPE: potential=0.6434 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0614 | critic_loss=0.0259 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0129 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 7356.8s
   📊 Metrics: Return=+13.93% | Sharpe=0.572 | DD=7.27% | Turnover=24.72%
   🎚️ Intra-Step TAPE: potential=0.2933 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0566 | critic_loss=0.0576 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0288 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.07 | std=0.53 | range=[0.71, 3.14] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=0.96 | NEE=0.96 | GLD=0.94  BOT: AMZN=0.87 | NVDA=0.86 | CAT=0.84
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=24 (35.3%), medium_vol=21 (30.9%)
      🧪 Deterministic validation: Sharpe=0.833 | Return=+77.80% | DD=22.57%
         Multi-horizon: score=0.880 | details=252:0.944/22.6%, 504:1.143/22.6%, 756:0.690/22.6%, 1008:0.833/22.6%
         SPY relative: spy_return=+53.67% | outperformance=+24.13%
         Stochastic sanity: mean_sharpe=0.523 | std=1.036 | runs=5
         [WARN] Sanity gate rejected checkpoint (stochastic robustness failed).
[CYCLE] Update 51/348 | Step 51,408/500,000 | Episode 68 | Time: 7899.5s
   📊 Metrics: Return=+29.66% | Sharpe=0.732 | DD=13.09% | Turnover=24.32%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0559 | critic_loss=0.0590 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0295 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.980) | TAPE=0.3926
[CYCLE] Update 52/348 | Step 52,416/500,000 | Episode 68 | Time: 7944.6s
   📊 Metrics: Return=+5.93% | Sharpe=0.365 | DD=13.25% | Turnover=23.14%
   🎚️ Intra-Step TAPE: potential=0.7482 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0642 | critic_loss=0.0531 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0266 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0013 | dispersion_loss=0.0007
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.28 | std=0.99 | range=[0.79, 4.98] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.03 | PG=1.02 | JNJ=1.02  BOT: JPM=0.95 | CAT=0.93 | NVDA=0.91
   🧭 Regime Start Dist (train resets): high_vol=23 (31.9%), low_vol=27 (37.5%), medium_vol=22 (30.6%)
[CYCLE] Update 53/348 | Step 53,424/500,000 | Episode 68 | Time: 7990.1s
   📊 Metrics: Return=+9.79% | Sharpe=0.267 | DD=13.25% | Turnover=22.80%
   🎚️ Intra-Step TAPE: potential=0.5768 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0587 | critic_loss=0.0950 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0475 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0015 | dispersion_loss=0.0004
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      🧪 Deterministic validation: Sharpe=0.837 | Return=+67.97% | DD=19.48%
         Multi-horizon: score=0.905 | details=252:0.980/19.5%, 504:1.157/19.5%, 756:0.690/19.5%, 1008:0.837/19.5%
         SPY relative: spy_return=+53.67% | outperformance=+14.30%
         Stochastic sanity: mean_sharpe=0.826 | std=0.602 | runs=5
      💾 Deterministic-validation checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00070_shp0p837_actor.weights.h5 (val_sharpe=0.837, score=0.905)
[CYCLE] Update 54/348 | Step 54,432/500,000 | Episode 72 | Time: 8536.3s
   📊 Metrics: Return=+11.33% | Sharpe=0.244 | DD=8.11% | Turnover=22.37%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0622 | critic_loss=0.0942 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0471 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0015 | dispersion_loss=0.0004
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.97 | std=0.90 | range=[0.58, 4.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.71 | NEE=0.71 | JNJ=0.70  BOT: AMZN=0.68 | XOM=0.67 | CAT=0.66
   🧭 Regime Start Dist (train resets): high_vol=25 (32.9%), low_vol=29 (38.2%), medium_vol=22 (28.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2684
[CYCLE] Update 55/348 | Step 55,440/500,000 | Episode 72 | Time: 8581.0s
   📊 Metrics: Return=+1.16% | Sharpe=-0.040 | DD=8.88% | Turnover=24.41%
   🎚️ Intra-Step TAPE: potential=0.6542 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0622 | critic_loss=0.0722 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0361 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0084 | penalty=-0.0003 | rolling_cvar=-0.01931
[CYCLE] Update 56/348 | Step 56,448/500,000 | Episode 72 | Time: 8628.8s
   📊 Metrics: Return=+17.76% | Sharpe=0.659 | DD=8.88% | Turnover=25.46%
   🎚️ Intra-Step TAPE: potential=0.3164 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0571 | critic_loss=0.0304 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0152 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.85 | std=0.30 | range=[0.62, 2.11] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.78 | NEE=0.78 | JNJ=0.77  BOT: AMZN=0.74 | CAT=0.73 | NVDA=0.73
   🧭 Regime Start Dist (train resets): high_vol=25 (32.9%), low_vol=29 (38.2%), medium_vol=22 (28.9%)
   🔐 Lagrangian CVaR: λ=0.0003 | penalty=-0.0001 | rolling_cvar=-0.02042
      🧪 Deterministic validation: Sharpe=0.852 | Return=+85.43% | DD=23.63%
         Multi-horizon: score=0.883 | details=252:0.937/23.6%, 504:1.161/23.6%, 756:0.690/23.6%, 1008:0.852/23.6%
         SPY relative: spy_return=+53.67% | outperformance=+31.76%
[CYCLE] Update 57/348 | Step 57,456/500,000 | Episode 76 | Time: 9003.6s
   📊 Metrics: Return=+13.00% | Sharpe=0.223 | DD=14.12% | Turnover=26.66%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0537 | critic_loss=0.0457 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0229 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.071 (peak 0.071, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2615
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01985
[CYCLE] Update 58/348 | Step 58,464/500,000 | Episode 76 | Time: 9047.5s
   📊 Metrics: Return=+14.48% | Sharpe=1.044 | DD=9.43% | Turnover=24.39%
   🎚️ Intra-Step TAPE: potential=0.6273 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0596 | critic_loss=0.0366 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0183 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.10 | std=0.28 | range=[0.69, 2.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.11 | JNJ=1.06 | NEE=1.06  BOT: JPM=0.99 | AMZN=0.99 | NVDA=0.99
   🧭 Regime Start Dist (train resets): high_vol=28 (35.0%), low_vol=30 (37.5%), medium_vol=22 (27.5%)
   🔐 Lagrangian CVaR: λ=0.0051 | penalty=-0.0001 | rolling_cvar=-0.02139
[CYCLE] Update 59/348 | Step 59,472/500,000 | Episode 76 | Time: 9090.8s
   📊 Metrics: Return=+24.96% | Sharpe=0.713 | DD=13.96% | Turnover=23.94%
   🎚️ Intra-Step TAPE: potential=0.5875 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0552 | critic_loss=0.0164 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0082 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0146 | penalty=-0.0003 | rolling_cvar=-0.02103
      🧪 Deterministic validation: Sharpe=0.856 | Return=+87.11% | DD=23.85%
         Multi-horizon: score=0.889 | details=252:0.944/23.9%, 504:1.168/23.9%, 756:0.695/23.9%, 1008:0.856/23.9%
         SPY relative: spy_return=+53.67% | outperformance=+33.44%
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 9458.1s
   📊 Metrics: Return=+22.25% | Sharpe=0.423 | DD=15.05% | Turnover=24.08%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0579 | critic_loss=0.0316 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0158 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.19 | std=0.25 | range=[0.71, 2.36] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.23 | JNJ=1.22 | PG=1.19  BOT: AMZN=1.07 | CAT=1.06 | NVDA=1.03
   🧭 Regime Start Dist (train resets): high_vol=31 (36.9%), low_vol=30 (35.7%), medium_vol=23 (27.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 60 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.840 (peak 0.840, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2920
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00345) | SPY bonus=0.002 (SPY ret=0.00314)
   🔐 Lagrangian CVaR: λ=0.0238 | penalty=-0.0005 | rolling_cvar=-0.01950
[CYCLE] Update 61/348 | Step 61,488/500,000 | Episode 80 | Time: 9505.1s
   📊 Metrics: Return=+9.73% | Sharpe=0.594 | DD=9.16% | Turnover=24.41%
   🎚️ Intra-Step TAPE: potential=0.6081 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0529 | critic_loss=0.0192 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0096 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 62/348 | Step 62,496/500,000 | Episode 80 | Time: 9551.6s
   📊 Metrics: Return=+11.51% | Sharpe=0.353 | DD=9.16% | Turnover=24.80%
   🎚️ Intra-Step TAPE: potential=0.2488 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0559 | critic_loss=0.0247 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0124 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.87 | std=0.30 | range=[0.59, 2.22] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=0.86 | JNJ=0.85 | PG=0.84  BOT: AMZN=0.73 | CAT=0.71 | NVDA=0.69
   🧭 Regime Start Dist (train resets): high_vol=31 (36.9%), low_vol=30 (35.7%), medium_vol=23 (27.4%)
[CYCLE] Update 63/348 | Step 63,504/500,000 | Episode 84 | Time: 9597.1s
   📊 Metrics: Return=+27.92% | Sharpe=0.555 | DD=13.00% | Turnover=25.55%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0563 | critic_loss=0.0466 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0233 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3265
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00291) | SPY bonus=0.004 (SPY ret=0.00048)
[CYCLE] Update 64/348 | Step 64,512/500,000 | Episode 84 | Time: 9642.4s
   📊 Metrics: Return=+5.54% | Sharpe=0.282 | DD=13.93% | Turnover=26.41%
   🎚️ Intra-Step TAPE: potential=0.7477 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0574 | critic_loss=0.0312 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0156 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.89 | std=0.17 | range=[0.63, 1.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.92 | JNJ=0.90 | PG=0.88  BOT: AMZN=0.81 | CAT=0.80 | NVDA=0.75
   🧭 Regime Start Dist (train resets): high_vol=33 (37.5%), low_vol=31 (35.2%), medium_vol=24 (27.3%)
   [WARN]  WARNING: Alpha std < 0.25 after 64 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01414
[CYCLE] Update 65/348 | Step 65,520/500,000 | Episode 84 | Time: 9687.1s
   📊 Metrics: Return=+6.33% | Sharpe=0.148 | DD=13.93% | Turnover=26.04%
   🎚️ Intra-Step TAPE: potential=0.3846 | delta_reward=-0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0528 | critic_loss=0.0395 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0197 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01270
      🧪 Deterministic validation: Sharpe=0.848 | Return=+90.15% | DD=24.93%
         Multi-horizon: score=0.876 | details=252:0.930/24.9%, 504:1.160/24.9%, 756:0.688/24.9%, 1008:0.848/24.9%
         SPY relative: spy_return=+53.67% | outperformance=+36.48%
[CYCLE] Update 66/348 | Step 66,528/500,000 | Episode 88 | Time: 10070.8s
   📊 Metrics: Return=+14.84% | Sharpe=0.314 | DD=8.68% | Turnover=25.31%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0561 | critic_loss=0.0226 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0113 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.10 | std=0.14 | range=[0.74, 1.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.16 | JNJ=1.15 | NEE=1.13  BOT: JPM=1.03 | CAT=0.99 | NVDA=0.96
   🧭 Regime Start Dist (train resets): high_vol=35 (38.0%), low_vol=33 (35.9%), medium_vol=24 (26.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 66 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2726
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01437
[CYCLE] Update 67/348 | Step 67,536/500,000 | Episode 88 | Time: 10115.9s
   📊 Metrics: Return=+1.83% | Sharpe=0.062 | DD=15.76% | Turnover=24.53%
   🎚️ Intra-Step TAPE: potential=0.7470 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0561 | critic_loss=0.0319 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0160 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 68/348 | Step 68,544/500,000 | Episode 88 | Time: 10160.2s
   📊 Metrics: Return=-1.48% | Sharpe=-0.096 | DD=15.76% | Turnover=25.34%
   🎚️ Intra-Step TAPE: potential=0.2375 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0534 | critic_loss=0.0414 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0207 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.83 | std=0.20 | range=[0.63, 1.76] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.83 | JNJ=0.79 | NEE=0.78  BOT: JPM=0.75 | CAT=0.75 | NVDA=0.74
   🧭 Regime Start Dist (train resets): high_vol=35 (38.0%), low_vol=33 (35.9%), medium_vol=24 (26.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 68 updates. TCN may not be learning asset discrimination.
      🧪 Deterministic validation: Sharpe=0.849 | Return=+85.62% | DD=23.67%
         Multi-horizon: score=0.886 | details=252:0.939/23.7%, 504:1.170/23.7%, 756:0.692/23.7%, 1008:0.849/23.7%
         SPY relative: spy_return=+53.67% | outperformance=+31.95%
[CYCLE] Update 69/348 | Step 69,552/500,000 | Episode 92 | Time: 10546.9s
   📊 Metrics: Return=+2.50% | Sharpe=0.070 | DD=39.61% | Turnover=24.86%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0532 | critic_loss=0.0454 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0227 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=2.447 (peak 2.447) | TAPE=0.2310
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00018) | SPY bonus=0.015 (SPY ret=-0.00315)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03507
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 92 | Time: 10594.3s
   📊 Metrics: Return=+24.12% | Sharpe=1.830 | DD=7.81% | Turnover=26.50%
   🎚️ Intra-Step TAPE: potential=0.7312 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0573 | critic_loss=0.0134 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0067 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.88 | std=0.20 | range=[0.62, 1.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=0.92 | JNJ=0.90 | NEE=0.88  BOT: CAT=0.79 | NVDA=0.79 | JPM=0.78
   🧭 Regime Start Dist (train resets): high_vol=38 (39.6%), low_vol=33 (34.4%), medium_vol=25 (26.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 70 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0136 | penalty=-0.0003 | rolling_cvar=-0.05093
[CYCLE] Update 71/348 | Step 71,568/500,000 | Episode 92 | Time: 10641.8s
   📊 Metrics: Return=+46.48% | Sharpe=1.822 | DD=7.81% | Turnover=26.42%
   🎚️ Intra-Step TAPE: potential=0.5854 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0550 | critic_loss=0.0148 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0074 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0312 | penalty=-0.0010 | rolling_cvar=-0.04169
      🧪 Deterministic validation: Sharpe=0.858 | Return=+90.42% | DD=24.44%
         Multi-horizon: score=0.889 | details=252:0.941/24.4%, 504:1.177/24.4%, 756:0.695/24.4%, 1008:0.858/24.4%
         SPY relative: spy_return=+53.67% | outperformance=+36.74%
[CYCLE] Update 72/348 | Step 72,576/500,000 | Episode 96 | Time: 11037.6s
   📊 Metrics: Return=+5.68% | Sharpe=0.117 | DD=29.21% | Turnover=25.88%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0533 | critic_loss=0.0187 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0094 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.84 | std=0.14 | range=[0.67, 1.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=0.82 | JNJ=0.82 | GLD=0.82  BOT: JPM=0.79 | XOM=0.79 | NVDA=0.77
   🧭 Regime Start Dist (train resets): high_vol=40 (40.0%), low_vol=34 (34.0%), medium_vol=26 (26.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 72 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.350 (peak 1.521) | TAPE=0.2320
   🔐 Lagrangian CVaR: λ=0.0401 | penalty=-0.0013 | rolling_cvar=-0.03817
[CYCLE] Update 73/348 | Step 73,584/500,000 | Episode 96 | Time: 11085.0s
   📊 Metrics: Return=+12.85% | Sharpe=1.105 | DD=6.14% | Turnover=27.04%
   🎚️ Intra-Step TAPE: potential=0.2592 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0579 | critic_loss=0.0141 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0071 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0168 | penalty=-0.0000 | rolling_cvar=-0.01867
[CYCLE] Update 74/348 | Step 74,592/500,000 | Episode 96 | Time: 11132.3s
   📊 Metrics: Return=+18.46% | Sharpe=0.748 | DD=7.26% | Turnover=26.17%
   🎚️ Intra-Step TAPE: potential=0.2449 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0565 | critic_loss=0.0182 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0091 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.99 | std=0.18 | range=[0.74, 1.73] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.01 | PG=0.98 | NEE=0.97  BOT: JPM=0.92 | CAT=0.88 | NVDA=0.83
   🧭 Regime Start Dist (train resets): high_vol=40 (40.0%), low_vol=34 (34.0%), medium_vol=26 (26.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 74 updates. TCN may not be learning asset discrimination.
      🧪 Deterministic validation: Sharpe=0.840 | Return=+86.37% | DD=24.45%
         Multi-horizon: score=0.872 | details=252:0.924/24.4%, 504:1.152/24.4%, 756:0.690/24.4%, 1008:0.840/24.4%
         SPY relative: spy_return=+53.67% | outperformance=+32.69%
[CYCLE] Update 75/348 | Step 75,600/500,000 | Episode 100 | Time: 11527.0s
   📊 Metrics: Return=+12.21% | Sharpe=0.223 | DD=10.54% | Turnover=25.64%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0502 | critic_loss=0.0384 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0192 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.140) | TAPE=0.2675
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01322) | SPY bonus=0.009 (SPY ret=-0.01544)
[CYCLE] Update 76/348 | Step 76,608/500,000 | Episode 100 | Time: 11573.8s
   📊 Metrics: Return=+14.64% | Sharpe=1.273 | DD=6.44% | Turnover=23.98%
   🎚️ Intra-Step TAPE: potential=0.6938 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0589 | critic_loss=0.0262 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0131 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.18 | std=0.18 | range=[0.85, 2.08] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.23 | JNJ=1.21 | PG=1.20  BOT: CAT=1.09 | JPM=1.08 | NVDA=0.99
   🧭 Regime Start Dist (train resets): high_vol=40 (38.5%), low_vol=36 (34.6%), medium_vol=28 (26.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 76 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01299
[CYCLE] Update 77/348 | Step 77,616/500,000 | Episode 100 | Time: 11620.9s
   📊 Metrics: Return=+23.85% | Sharpe=0.985 | DD=7.47% | Turnover=23.32%
   🎚️ Intra-Step TAPE: potential=0.2531 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0590 | critic_loss=0.0271 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0136 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01440
[CYCLE] Update 78/348 | Step 78,624/500,000 | Episode 104 | Time: 11668.1s
   📊 Metrics: Return=+35.52% | Sharpe=0.705 | DD=12.75% | Turnover=22.39%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0559 | critic_loss=0.0141 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0071 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.57 | std=0.18 | range=[1.19, 2.36] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.62 | GLD=1.58 | PG=1.58  BOT: JPM=1.52 | CAT=1.45 | NVDA=1.38
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=36 (33.3%), medium_vol=30 (27.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 78 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3885
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00207) | SPY bonus=0.010 (SPY ret=-0.00736)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01796
[CYCLE] Update 79/348 | Step 79,632/500,000 | Episode 104 | Time: 11715.4s
   📊 Metrics: Return=+11.57% | Sharpe=0.836 | DD=10.91% | Turnover=21.03%
   🎚️ Intra-Step TAPE: potential=0.2533 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0575 | critic_loss=0.0182 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0091 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 11762.2s
   📊 Metrics: Return=+25.98% | Sharpe=0.934 | DD=10.91% | Turnover=21.15%
   🎚️ Intra-Step TAPE: potential=0.2298 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0563 | critic_loss=0.0164 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0082 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.64 | std=0.23 | range=[1.12, 2.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.79 | PG=1.71 | JNJ=1.67  BOT: CAT=1.50 | JPM=1.47 | NVDA=1.34
   🧭 Regime Start Dist (train resets): high_vol=42 (38.9%), low_vol=36 (33.3%), medium_vol=30 (27.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 80 updates. TCN may not be learning asset discrimination.
      🧪 Deterministic validation: Sharpe=0.846 | Return=+88.87% | DD=25.01%
         Multi-horizon: score=0.868 | details=252:0.919/25.0%, 504:1.145/25.0%, 756:0.693/25.0%, 1008:0.846/25.0%
         SPY relative: spy_return=+53.67% | outperformance=+35.19%
[CYCLE] Update 81/348 | Step 81,648/500,000 | Episode 108 | Time: 12155.3s
   📊 Metrics: Return=+27.77% | Sharpe=0.527 | DD=11.84% | Turnover=20.84%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0550 | critic_loss=0.0409 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0205 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3162
[CYCLE] Update 82/348 | Step 82,656/500,000 | Episode 108 | Time: 12202.2s
   📊 Metrics: Return=+23.05% | Sharpe=2.171 | DD=3.22% | Turnover=18.85%
   🎚️ Intra-Step TAPE: potential=0.4675 | delta_reward=-0.0022
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0612 | critic_loss=0.0660 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0330 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.02 | std=0.16 | range=[1.50, 2.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=2.13 | JNJ=2.11 | JPM=2.10  BOT: XOM=1.99 | CAT=1.97 | NVDA=1.86
   🧭 Regime Start Dist (train resets): high_vol=43 (38.4%), low_vol=39 (34.8%), medium_vol=30 (26.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 82 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 83/348 | Step 83,664/500,000 | Episode 108 | Time: 12249.2s
   📊 Metrics: Return=+46.67% | Sharpe=1.715 | DD=8.45% | Turnover=18.89%
   🎚️ Intra-Step TAPE: potential=0.2564 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0549 | critic_loss=0.0646 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0323 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      🧪 Deterministic validation: Sharpe=0.859 | Return=+94.53% | DD=25.65%
         Multi-horizon: score=0.870 | details=252:0.915/25.7%, 504:1.156/25.7%, 756:0.691/25.7%, 1008:0.859/25.7%
         SPY relative: spy_return=+53.67% | outperformance=+40.86%
[CYCLE] Update 84/348 | Step 84,672/500,000 | Episode 112 | Time: 12634.5s
   📊 Metrics: Return=+22.63% | Sharpe=0.525 | DD=9.01% | Turnover=18.86%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0564 | critic_loss=0.1662 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0831 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.10 | std=0.17 | range=[1.55, 2.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=2.23 | JNJ=2.20 | PG=2.17  BOT: GLD=2.00 | CAT=2.00 | NVDA=1.87
   🧭 Regime Start Dist (train resets): high_vol=45 (38.8%), low_vol=40 (34.5%), medium_vol=31 (26.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 84 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3249
[CYCLE] Update 85/348 | Step 85,680/500,000 | Episode 112 | Time: 12679.7s
   📊 Metrics: Return=+10.34% | Sharpe=0.604 | DD=15.18% | Turnover=19.23%
   🎚️ Intra-Step TAPE: potential=0.3806 | delta_reward=-0.0025
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0546 | critic_loss=0.0293 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0146 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01273
[CYCLE] Update 86/348 | Step 86,688/500,000 | Episode 112 | Time: 12725.4s
   📊 Metrics: Return=+16.82% | Sharpe=0.431 | DD=15.18% | Turnover=19.95%
   🎚️ Intra-Step TAPE: potential=0.7451 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0575 | critic_loss=0.0412 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0206 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.56 | std=0.29 | range=[1.25, 2.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.52 | GLD=1.51 | CAT=1.48  BOT: PG=1.45 | NEE=1.44 | XOM=1.44
   🧭 Regime Start Dist (train resets): high_vol=45 (38.8%), low_vol=40 (34.5%), medium_vol=31 (26.7%)
      🧪 Deterministic validation: Sharpe=0.868 | Return=+88.26% | DD=23.53%
         Multi-horizon: score=0.894 | details=252:0.945/23.5%, 504:1.177/23.5%, 756:0.693/23.5%, 1008:0.868/23.5%
         SPY relative: spy_return=+53.67% | outperformance=+34.59%
[CYCLE] Update 87/348 | Step 87,696/500,000 | Episode 116 | Time: 13117.0s
   📊 Metrics: Return=+42.04% | Sharpe=0.934 | DD=8.74% | Turnover=20.44%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0547 | critic_loss=0.0371 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0186 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5022
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00289) | SPY bonus=0.000 (SPY ret=-0.00284)
[CYCLE] Update 88/348 | Step 88,704/500,000 | Episode 116 | Time: 13164.1s
   📊 Metrics: Return=+4.03% | Sharpe=0.200 | DD=12.54% | Turnover=22.98%
   🎚️ Intra-Step TAPE: potential=0.5721 | delta_reward=+0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0533 | critic_loss=0.0215 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.30 | std=0.42 | range=[0.99, 3.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.27 | JNJ=1.19 | CAT=1.18  BOT: JPM=1.15 | NVDA=1.14 | NEE=1.14
   🧭 Regime Start Dist (train resets): high_vol=47 (39.2%), low_vol=42 (35.0%), medium_vol=31 (25.8%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02038
[CYCLE] Update 89/348 | Step 89,712/500,000 | Episode 116 | Time: 13210.3s
   📊 Metrics: Return=+9.68% | Sharpe=0.255 | DD=12.54% | Turnover=22.84%
   🎚️ Intra-Step TAPE: potential=0.5837 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0530 | critic_loss=0.0181 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0091 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      🧪 Deterministic validation: Sharpe=0.868 | Return=+88.33% | DD=23.42%
         Multi-horizon: score=0.892 | details=252:0.943/23.4%, 504:1.175/23.4%, 756:0.689/23.4%, 1008:0.868/23.4%
         SPY relative: spy_return=+53.67% | outperformance=+34.65%

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon: 774 steps
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 13590.0s
   📊 Metrics: Return=+15.26% | Sharpe=0.266 | DD=15.21% | Turnover=22.15%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0575 | critic_loss=0.0317 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0158 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.86 | std=0.61 | range=[1.45, 4.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.76 | AMZN=1.75 | JPM=1.69  BOT: PG=1.65 | XOM=1.63 | NEE=1.62
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=42 (33.9%), medium_vol=34 (27.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.004) | TAPE=0.2636

📚 EPISODE HORIZON UPDATE at 91,728 steps:
   Episode horizon: 800 steps
[CYCLE] Update 91/348 | Step 91,728/500,000 | Episode 120 | Time: 13636.4s
   📊 Metrics: Return=+25.49% | Sharpe=2.418 | DD=2.76% | Turnover=19.81%
   🎚️ Intra-Step TAPE: potential=0.2594 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0552 | critic_loss=0.0257 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0129 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01351

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon: 825 steps
[CYCLE] Update 92/348 | Step 92,736/500,000 | Episode 120 | Time: 13682.5s
   📊 Metrics: Return=+49.78% | Sharpe=2.084 | DD=7.75% | Turnover=20.17%
   🎚️ Intra-Step TAPE: potential=0.2338 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0532 | critic_loss=0.0244 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0122 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.75 | std=0.47 | range=[1.39, 3.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=1.66 | AMZN=1.65 | GLD=1.64  BOT: MSFT=1.58 | XOM=1.58 | NEE=1.57
   🧭 Regime Start Dist (train resets): high_vol=48 (38.7%), low_vol=42 (33.9%), medium_vol=34 (27.4%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01573

📚 EPISODE HORIZON UPDATE at 93,744 steps:
   Episode horizon: 850 steps
[CYCLE] Update 93/348 | Step 93,744/500,000 | Episode 120 | Time: 13728.4s
   📊 Metrics: Return=+51.44% | Sharpe=1.127 | DD=17.56% | Turnover=20.19%
   🎚️ Intra-Step TAPE: potential=0.7291 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0544 | critic_loss=0.0434 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0217 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02792

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon: 876 steps
[CYCLE] Update 94/348 | Step 94,752/500,000 | Episode 124 | Time: 13774.2s
   📊 Metrics: Return=-5.95% | Sharpe=-0.055 | DD=43.07% | Turnover=20.15%
   🎚️ Intra-Step TAPE: potential=0.5885 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0593 | critic_loss=0.0230 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0115 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.95 | std=0.42 | range=[1.40, 3.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.89 | AMZN=1.88 | CAT=1.85  BOT: JNJ=1.81 | NEE=1.80 | NVDA=1.79
   🧭 Regime Start Dist (train resets): high_vol=50 (39.1%), low_vol=43 (33.6%), medium_vol=35 (27.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.04% / trig 14.00%) | terminal=2.352 (peak 2.352) | TAPE=0.2226
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01459

📚 EPISODE HORIZON UPDATE at 95,760 steps:
   Episode horizon: 901 steps
[CYCLE] Update 95/348 | Step 95,760/500,000 | Episode 124 | Time: 13820.7s
   📊 Metrics: Return=-10.30% | Sharpe=-0.252 | DD=35.79% | Turnover=20.06%
   🎚️ Intra-Step TAPE: potential=0.2280 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0580 | critic_loss=0.0206 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0103 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01704

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon: 927 steps
[CYCLE] Update 96/348 | Step 96,768/500,000 | Episode 124 | Time: 13866.2s
   📊 Metrics: Return=+16.97% | Sharpe=0.282 | DD=42.01% | Turnover=20.01%
   🎚️ Intra-Step TAPE: potential=0.5898 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0574 | critic_loss=0.0103 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0052 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.85 | std=0.35 | range=[1.17, 3.27] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.87 | NVDA=1.83 | GLD=1.79  BOT: JNJ=1.71 | PG=1.70 | NEE=1.68
   🧭 Regime Start Dist (train resets): high_vol=50 (39.1%), low_vol=43 (33.6%), medium_vol=35 (27.3%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01704

📚 EPISODE HORIZON UPDATE at 97,776 steps:
   Episode horizon: 952 steps
[CYCLE] Update 97/348 | Step 97,776/500,000 | Episode 124 | Time: 13912.1s
   📊 Metrics: Return=+24.22% | Sharpe=0.286 | DD=42.01% | Turnover=19.88%
   🎚️ Intra-Step TAPE: potential=0.7328 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0574 | critic_loss=0.0089 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01586
      🧪 Deterministic validation: Sharpe=0.873 | Return=+94.26% | DD=24.46%
         Multi-horizon: score=0.884 | details=252:0.932/24.5%, 504:1.174/24.5%, 756:0.681/24.5%, 1008:0.873/24.5%
         SPY relative: spy_return=+53.67% | outperformance=+40.59%

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon: 977 steps
[CYCLE] Update 98/348 | Step 98,784/500,000 | Episode 128 | Time: 14289.6s
   📊 Metrics: Return=+52.73% | Sharpe=0.933 | DD=12.48% | Turnover=19.74%
   🎚️ Intra-Step TAPE: potential=0.7540 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0514 | critic_loss=0.0150 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.90 | std=0.37 | range=[1.52, 3.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.92 | AMZN=1.88 | CAT=1.88  BOT: PG=1.72 | JNJ=1.71 | NEE=1.69
   🧭 Regime Start Dist (train resets): high_vol=51 (38.6%), low_vol=45 (34.1%), medium_vol=36 (27.3%)
   🔒 Drawdown λ snapshot=0.551 (peak 0.994, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.941) | TAPE=0.4882
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00150) | SPY bonus=0.003 (SPY ret=-0.00389)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02749

📚 EPISODE HORIZON UPDATE at 99,792 steps:
   Episode horizon: 1003 steps
[CYCLE] Update 99/348 | Step 99,792/500,000 | Episode 128 | Time: 14335.2s
   📊 Metrics: Return=+17.71% | Sharpe=0.491 | DD=14.66% | Turnover=19.68%
   🎚️ Intra-Step TAPE: potential=0.5869 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0625 | critic_loss=0.0290 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0145 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.02215

📚 TURNOVER CURRICULUM UPDATE at 100,800 steps:
   Turnover penalty scalar: 0.75

🎛️ EXECUTION BETA UPDATE at 100,800 steps:
   action_execution_beta: 0.450 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 100,800 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 14380.5s
   📊 Metrics: Return=+21.37% | Sharpe=0.395 | DD=14.66% | Turnover=19.25%
   🎚️ Intra-Step TAPE: potential=0.6355 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0594 | critic_loss=0.0089 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.31 | std=0.28 | range=[0.87, 3.13] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.45 | GLD=2.40 | AMZN=2.39  BOT: PG=2.17 | JNJ=2.15 | NEE=2.13
   🧭 Regime Start Dist (train resets): high_vol=51 (38.6%), low_vol=45 (34.1%), medium_vol=36 (27.3%)
   🔐 Lagrangian CVaR: λ=0.0121 | penalty=-0.0001 | rolling_cvar=-0.01998

🎯 ENTROPY COEF UPDATE at 100,800 steps:
   entropy_coef: 0.0020
[CYCLE] Update 101/348 | Step 101,808/500,000 | Episode 128 | Time: 14425.6s
   📊 Metrics: Return=+29.89% | Sharpe=0.416 | DD=14.66% | Turnover=20.47%
   🎚️ Intra-Step TAPE: potential=0.3153 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0448 | critic_loss=0.0044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0150 | penalty=-0.0003 | rolling_cvar=-0.01882
      🧪 Deterministic validation: Sharpe=0.873 | Return=+101.31% | DD=26.04%
         Multi-horizon: score=0.874 | details=252:0.919/26.0%, 504:1.171/26.0%, 756:0.676/26.0%, 1008:0.873/26.0%
         SPY relative: spy_return=+53.67% | outperformance=+47.63%
[CYCLE] Update 102/348 | Step 102,816/500,000 | Episode 132 | Time: 14799.7s
   📊 Metrics: Return=+22.56% | Sharpe=0.309 | DD=13.54% | Turnover=20.41%
   🎚️ Intra-Step TAPE: potential=0.7286 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0422 | critic_loss=0.0189 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0094 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.18 | std=0.22 | range=[1.23, 2.75] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.37 | AMZN=2.36 | NVDA=2.35  BOT: JPM=2.14 | PG=2.11 | NEE=2.03
   🧭 Regime Start Dist (train resets): high_vol=52 (38.2%), low_vol=47 (34.6%), medium_vol=37 (27.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 102 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2724
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00038) | SPY bonus=0.003 (SPY ret=-0.00118)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0001 | rolling_cvar=-0.01723
[CYCLE] Update 103/348 | Step 103,824/500,000 | Episode 132 | Time: 14844.7s
   📊 Metrics: Return=+56.13% | Sharpe=2.096 | DD=9.75% | Turnover=23.61%
   🎚️ Intra-Step TAPE: potential=0.7333 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0412 | critic_loss=0.0202 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0101 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01873
[CYCLE] Update 104/348 | Step 104,832/500,000 | Episode 132 | Time: 14891.4s
   📊 Metrics: Return=+75.50% | Sharpe=1.631 | DD=9.75% | Turnover=22.98%
   🎚️ Intra-Step TAPE: potential=0.6758 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0432 | critic_loss=0.0131 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.76 | std=0.46 | range=[0.64, 4.18] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.23 | GLD=3.09 | JPM=3.03  BOT: MSFT=2.66 | PG=2.66 | NEE=2.63
   🧭 Regime Start Dist (train resets): high_vol=52 (38.2%), low_vol=47 (34.6%), medium_vol=37 (27.2%)
   🔐 Lagrangian CVaR: λ=0.0013 | penalty=-0.0000 | rolling_cvar=-0.01735
[CYCLE] Update 105/348 | Step 105,840/500,000 | Episode 132 | Time: 14938.8s
   📊 Metrics: Return=+88.44% | Sharpe=1.212 | DD=18.25% | Turnover=22.69%
   🎚️ Intra-Step TAPE: potential=0.3496 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0433 | critic_loss=0.0069 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0007 | penalty=-0.0000 | rolling_cvar=-0.01776
      🧪 Deterministic validation: Sharpe=0.883 | Return=+105.37% | DD=26.36%
         Multi-horizon: score=0.878 | details=252:0.920/26.4%, 504:1.182/26.4%, 756:0.674/26.4%, 1008:0.883/26.4%
         SPY relative: spy_return=+53.67% | outperformance=+51.70%
[CYCLE] Update 106/348 | Step 106,848/500,000 | Episode 136 | Time: 15318.9s
   📊 Metrics: Return=+72.25% | Sharpe=1.040 | DD=10.34% | Turnover=22.83%
   🎚️ Intra-Step TAPE: potential=0.6930 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0472 | critic_loss=0.0088 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0044 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.52 | std=0.34 | range=[0.65, 3.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.77 | GLD=2.75 | CAT=2.69  BOT: JNJ=2.44 | PG=2.40 | NEE=2.36
   🧭 Regime Start Dist (train resets): high_vol=54 (38.6%), low_vol=48 (34.3%), medium_vol=38 (27.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.50% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5231
   🔐 Lagrangian CVaR: λ=0.0074 | penalty=-0.0002 | rolling_cvar=-0.01406
[CYCLE] Update 107/348 | Step 107,856/500,000 | Episode 136 | Time: 15364.0s
   📊 Metrics: Return=+26.79% | Sharpe=0.964 | DD=9.98% | Turnover=22.71%
   🎚️ Intra-Step TAPE: potential=0.7074 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0373 | critic_loss=0.0040 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0018 | penalty=-0.0002 | rolling_cvar=-0.01392
[CYCLE] Update 108/348 | Step 108,864/500,000 | Episode 136 | Time: 15408.8s
   📊 Metrics: Return=+62.41% | Sharpe=1.270 | DD=9.98% | Turnover=23.51%
   🎚️ Intra-Step TAPE: potential=0.5605 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0411 | critic_loss=0.0138 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0069 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.01 | std=0.17 | range=[1.38, 2.53] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.21 | AMZN=2.17 | GLD=2.14  BOT: JNJ=1.90 | PG=1.89 | NEE=1.86
   🧭 Regime Start Dist (train resets): high_vol=54 (38.6%), low_vol=48 (34.3%), medium_vol=38 (27.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 108 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01605
[CYCLE] Update 109/348 | Step 109,872/500,000 | Episode 136 | Time: 15455.5s
   📊 Metrics: Return=+27.09% | Sharpe=0.359 | DD=26.18% | Turnover=23.91%
   🎚️ Intra-Step TAPE: potential=0.2359 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0399 | critic_loss=0.0145 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0073 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01652
      🧪 Deterministic validation: Sharpe=0.885 | Return=+104.41% | DD=26.16%
         Multi-horizon: score=0.885 | details=252:0.929/26.2%, 504:1.187/26.2%, 756:0.680/26.2%, 1008:0.885/26.2%
         SPY relative: spy_return=+53.67% | outperformance=+50.74%
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 140 | Time: 15833.3s
   📊 Metrics: Return=+50.95% | Sharpe=0.775 | DD=13.01% | Turnover=23.77%
   🎚️ Intra-Step TAPE: potential=0.2338 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0433 | critic_loss=0.0348 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0174 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.11 | std=0.26 | range=[0.81, 2.87] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.43 | AMZN=2.33 | GLD=2.26  BOT: XOM=2.01 | NEE=2.00 | PG=1.99
   🧭 Regime Start Dist (train resets): high_vol=55 (38.2%), low_vol=51 (35.4%), medium_vol=38 (26.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.416, dd 0.18% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4202
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01689
[CYCLE] Update 111/348 | Step 111,888/500,000 | Episode 140 | Time: 15880.5s
   📊 Metrics: Return=+27.37% | Sharpe=0.767 | DD=12.78% | Turnover=23.99%
   🎚️ Intra-Step TAPE: potential=0.2286 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0390 | critic_loss=0.0104 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0052 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02118
[CYCLE] Update 112/348 | Step 112,896/500,000 | Episode 140 | Time: 15926.1s
   📊 Metrics: Return=-14.16% | Sharpe=-0.146 | DD=44.45% | Turnover=24.37%
   🎚️ Intra-Step TAPE: potential=0.2271 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0444 | critic_loss=0.0112 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0056 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.00 | std=0.30 | range=[0.64, 2.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.29 | AMZN=2.21 | JPM=2.20  BOT: NEE=1.95 | PG=1.90 | JNJ=1.88
   🧭 Regime Start Dist (train resets): high_vol=55 (38.2%), low_vol=51 (35.4%), medium_vol=38 (26.4%)
   🔐 Lagrangian CVaR: λ=0.0055 | penalty=-0.0000 | rolling_cvar=-0.03956
[CYCLE] Update 113/348 | Step 113,904/500,000 | Episode 140 | Time: 15973.2s
   📊 Metrics: Return=+25.67% | Sharpe=0.282 | DD=44.45% | Turnover=24.44%
   🎚️ Intra-Step TAPE: potential=0.2285 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0417 | critic_loss=0.0049 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0257 | penalty=-0.0006 | rolling_cvar=-0.03754
[CYCLE] Update 114/348 | Step 114,912/500,000 | Episode 144 | Time: 16019.9s
   📊 Metrics: Return=+38.77% | Sharpe=0.374 | DD=42.42% | Turnover=24.45%
   🎚️ Intra-Step TAPE: potential=0.2353 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0433 | critic_loss=0.0165 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.07 | std=0.13 | range=[1.49, 2.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.13 | NVDA=2.12 | CAT=2.11  BOT: NEE=2.02 | PG=2.01 | JNJ=2.01
   🧭 Regime Start Dist (train resets): high_vol=57 (38.5%), low_vol=51 (34.5%), medium_vol=40 (27.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 114 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=1.161 (peak 1.634, dd 14.33% / trig 14.00%) | terminal=3.229 (peak 3.525) | TAPE=0.2573
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00295) | SPY bonus=0.008 (SPY ret=-0.00571)
   🔐 Lagrangian CVaR: λ=0.0173 | penalty=-0.0002 | rolling_cvar=-0.03010
[CYCLE] Update 115/348 | Step 115,920/500,000 | Episode 144 | Time: 16066.1s
   📊 Metrics: Return=+8.62% | Sharpe=0.234 | DD=18.20% | Turnover=25.15%
   🎚️ Intra-Step TAPE: potential=0.7451 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0412 | critic_loss=0.0112 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0056 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0138 | penalty=-0.0001 | rolling_cvar=-0.02378
[CYCLE] Update 116/348 | Step 116,928/500,000 | Episode 144 | Time: 16111.8s
   📊 Metrics: Return=+8.82% | Sharpe=0.141 | DD=18.20% | Turnover=24.77%
   🎚️ Intra-Step TAPE: potential=0.2494 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0396 | critic_loss=0.0239 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0119 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.25 | std=0.26 | range=[1.73, 3.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.30 | CAT=2.20 | JNJ=2.20  BOT: JPM=2.14 | NEE=2.14 | XOM=2.13
   🧭 Regime Start Dist (train resets): high_vol=57 (38.5%), low_vol=51 (34.5%), medium_vol=40 (27.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.02144
[CYCLE] Update 117/348 | Step 117,936/500,000 | Episode 144 | Time: 16157.7s
   📊 Metrics: Return=+18.31% | Sharpe=0.246 | DD=18.20% | Turnover=24.67%
   🎚️ Intra-Step TAPE: potential=0.2407 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0405 | critic_loss=0.0301 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0151 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0024
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      🧪 Deterministic validation: Sharpe=0.854 | Return=+94.45% | DD=25.84%
         Multi-horizon: score=0.863 | details=252:0.909/25.8%, 504:1.150/25.8%, 756:0.680/25.8%, 1008:0.854/25.8%
         SPY relative: spy_return=+53.67% | outperformance=+40.78%
[CYCLE] Update 118/348 | Step 118,944/500,000 | Episode 148 | Time: 16539.4s
   📊 Metrics: Return=+19.79% | Sharpe=0.256 | DD=14.06% | Turnover=24.69%
   🎚️ Intra-Step TAPE: potential=0.7550 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0421 | critic_loss=0.0332 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0166 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.36 | std=0.21 | range=[0.97, 2.87] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.50 | XOM=2.45 | JNJ=2.44  BOT: CAT=2.38 | AMZN=2.32 | NVDA=2.16
   🧭 Regime Start Dist (train resets): high_vol=59 (38.8%), low_vol=51 (33.6%), medium_vol=42 (27.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 118 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.82% / trig 14.00%) | terminal=0.000 (peak 1.292) | TAPE=0.2676
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00038) | SPY bonus=0.002 (SPY ret=-0.00118)
   🔐 Lagrangian CVaR: λ=0.0004 | penalty=-0.0000 | rolling_cvar=-0.02441
[CYCLE] Update 119/348 | Step 119,952/500,000 | Episode 148 | Time: 16585.8s
   📊 Metrics: Return=+14.26% | Sharpe=0.408 | DD=18.54% | Turnover=23.76%
   🎚️ Intra-Step TAPE: potential=0.2406 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0468 | critic_loss=0.0090 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0186 | penalty=-0.0003 | rolling_cvar=-0.02628
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 148 | Time: 16632.5s
   📊 Metrics: Return=-4.79% | Sharpe=-0.006 | DD=46.36% | Turnover=23.28%
   🎚️ Intra-Step TAPE: potential=0.3156 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0411 | critic_loss=0.0059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0030 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=2.44 | std=0.26 | range=[0.79, 2.89] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.63 | JNJ=2.56 | NEE=2.55  BOT: AMZN=2.42 | JPM=2.40 | NVDA=2.33
   🧭 Regime Start Dist (train resets): high_vol=59 (38.8%), low_vol=51 (33.6%), medium_vol=42 (27.6%)
   🔐 Lagrangian CVaR: λ=0.0444 | penalty=-0.0012 | rolling_cvar=-0.02394
[CYCLE] Update 121/348 | Step 121,968/500,000 | Episode 148 | Time: 16679.0s
   📊 Metrics: Return=+8.74% | Sharpe=0.130 | DD=46.36% | Turnover=23.42%
   🎚️ Intra-Step TAPE: potential=0.2394 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0418 | critic_loss=0.0049 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0023
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0643 | penalty=-0.0018 | rolling_cvar=-0.02204
      🧪 Deterministic validation: Sharpe=0.828 | Return=+91.14% | DD=26.51%
         Multi-horizon: score=0.832 | details=252:0.877/26.5%, 504:1.113/26.5%, 756:0.668/26.5%, 1008:0.828/26.5%
         SPY relative: spy_return=+53.67% | outperformance=+37.47%
[CYCLE] Update 122/348 | Step 122,976/500,000 | Episode 152 | Time: 17062.6s
   📊 Metrics: Return=+23.02% | Sharpe=0.294 | DD=15.89% | Turnover=23.05%
   🎚️ Intra-Step TAPE: potential=0.2280 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0388 | critic_loss=0.0089 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.96 | std=0.22 | range=[0.97, 2.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.11 | GLD=2.10 | PG=2.08  BOT: JPM=1.94 | NVDA=1.80 | AMZN=1.79
   🧭 Regime Start Dist (train resets): high_vol=60 (38.5%), low_vol=51 (32.7%), medium_vol=45 (28.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 122 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=1.339 (peak 2.000, dd 3.17% / trig 14.00%) | terminal=0.000 (peak 0.007) | TAPE=0.2651
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00108) | SPY bonus=0.009 (SPY ret=-0.00290)
   🔐 Lagrangian CVaR: λ=0.0458 | penalty=-0.0003 | rolling_cvar=-0.01593
[CYCLE] Update 123/348 | Step 123,984/500,000 | Episode 152 | Time: 17109.1s
   📊 Metrics: Return=+23.22% | Sharpe=0.923 | DD=7.08% | Turnover=25.55%
   🎚️ Intra-Step TAPE: potential=0.5470 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0379 | critic_loss=0.0064 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0032 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0255 | penalty=-0.0003 | rolling_cvar=-0.01427
[CYCLE] Update 124/348 | Step 124,992/500,000 | Episode 152 | Time: 17154.8s
   📊 Metrics: Return=+19.36% | Sharpe=0.448 | DD=8.78% | Turnover=26.19%
   🎚️ Intra-Step TAPE: potential=0.2333 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0393 | critic_loss=0.0035 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0018 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.58 | std=0.22 | range=[0.67, 1.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.77 | NEE=1.76 | XOM=1.73  BOT: CAT=1.51 | AMZN=1.47 | NVDA=1.32
   🧭 Regime Start Dist (train resets): high_vol=60 (38.5%), low_vol=51 (32.7%), medium_vol=45 (28.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 124 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0124 | penalty=-0.0004 | rolling_cvar=-0.01608
[CYCLE] Update 125/348 | Step 126,000/500,000 | Episode 152 | Time: 17201.0s
   📊 Metrics: Return=+32.31% | Sharpe=0.516 | DD=12.47% | Turnover=26.69%
   🎚️ Intra-Step TAPE: potential=0.7456 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0380 | critic_loss=0.0115 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0057 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0022
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0001 | rolling_cvar=-0.01667
      🧪 Deterministic validation: Sharpe=0.807 | Return=+82.72% | DD=25.46%
         Multi-horizon: score=0.821 | details=252:0.869/25.5%, 504:1.089/25.5%, 756:0.666/25.5%, 1008:0.807/25.5%
         SPY relative: spy_return=+53.67% | outperformance=+29.05%
[CYCLE] Update 126/348 | Step 127,008/500,000 | Episode 156 | Time: 17576.0s
   📊 Metrics: Return=+36.41% | Sharpe=0.568 | DD=10.86% | Turnover=26.57%
   🎚️ Intra-Step TAPE: potential=0.2470 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0392 | critic_loss=0.0150 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.42 | std=0.24 | range=[0.79, 2.23] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.57 | PG=1.55 | NEE=1.52  BOT: CAT=1.25 | AMZN=1.19 | NVDA=1.05
   🧭 Regime Start Dist (train resets): high_vol=61 (38.1%), low_vol=52 (32.5%), medium_vol=47 (29.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 126 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.002, dd 10.07% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3259
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00269) | SPY bonus=0.005 (SPY ret=-0.00347)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02116
[CYCLE] Update 127/348 | Step 128,016/500,000 | Episode 156 | Time: 17620.7s
   📊 Metrics: Return=-21.57% | Sharpe=-0.364 | DD=41.67% | Turnover=28.33%
   🎚️ Intra-Step TAPE: potential=0.5332 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0348 | critic_loss=0.0050 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0007 | penalty=-0.0000 | rolling_cvar=-0.02084
[CYCLE] Update 128/348 | Step 129,024/500,000 | Episode 156 | Time: 17665.2s
   📊 Metrics: Return=+4.20% | Sharpe=0.105 | DD=41.67% | Turnover=28.45%
   🎚️ Intra-Step TAPE: potential=0.4772 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0390 | critic_loss=0.0035 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0021
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.30 | std=0.27 | range=[0.72, 2.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.37 | NEE=1.34 | PG=1.33  BOT: CAT=1.14 | AMZN=1.11 | NVDA=1.05
   🧭 Regime Start Dist (train resets): high_vol=61 (38.1%), low_vol=52 (32.5%), medium_vol=47 (29.4%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02248
[CYCLE] Update 129/348 | Step 130,032/500,000 | Episode 156 | Time: 17709.9s
   📊 Metrics: Return=+7.38% | Sharpe=0.109 | DD=41.67% | Turnover=29.18%
   🎚️ Intra-Step TAPE: potential=0.2270 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0375 | critic_loss=0.0053 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0027 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02088
      🧪 Deterministic validation: Sharpe=0.803 | Return=+76.51% | DD=23.82%
         Multi-horizon: score=0.832 | details=252:0.888/23.8%, 504:1.091/23.8%, 756:0.667/23.8%, 1008:0.803/23.8%
         SPY relative: spy_return=+53.67% | outperformance=+22.84%
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 160 | Time: 18080.6s
   📊 Metrics: Return=+41.20% | Sharpe=0.546 | DD=14.20% | Turnover=29.92%
   🎚️ Intra-Step TAPE: potential=0.2290 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0372 | critic_loss=0.0097 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.13 | std=0.39 | range=[0.59, 3.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.17 | JNJ=1.14 | NEE=1.12  BOT: CAT=0.92 | AMZN=0.87 | NVDA=0.75
   🧭 Regime Start Dist (train resets): high_vol=64 (39.0%), low_vol=52 (31.7%), medium_vol=48 (29.3%)
   🔒 Drawdown λ snapshot=0.913 (peak 1.532, dd 10.40% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3145
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00701) | SPY bonus=0.019 (SPY ret=-0.01264)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02463
[CYCLE] Update 131/348 | Step 132,048/500,000 | Episode 160 | Time: 18125.2s
   📊 Metrics: Return=-17.43% | Sharpe=-0.313 | DD=37.62% | Turnover=31.47%
   🎚️ Intra-Step TAPE: potential=0.2958 | delta_reward=-0.0027
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0333 | critic_loss=0.0079 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0016 | penalty=-0.0000 | rolling_cvar=-0.01954
[CYCLE] Update 132/348 | Step 133,056/500,000 | Episode 160 | Time: 18170.8s
   📊 Metrics: Return=+3.00% | Sharpe=0.087 | DD=39.30% | Turnover=32.10%
   🎚️ Intra-Step TAPE: potential=0.2232 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0385 | critic_loss=0.0030 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0015 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.03 | std=0.27 | range=[0.58, 2.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.09 | NEE=1.07 | PG=1.04  BOT: JPM=0.84 | CAT=0.83 | NVDA=0.79
   🧭 Regime Start Dist (train resets): high_vol=64 (39.0%), low_vol=52 (31.7%), medium_vol=48 (29.3%)
   🔐 Lagrangian CVaR: λ=0.0037 | penalty=-0.0001 | rolling_cvar=-0.01757
[CYCLE] Update 133/348 | Step 134,064/500,000 | Episode 160 | Time: 18217.4s
   📊 Metrics: Return=+21.33% | Sharpe=0.247 | DD=39.30% | Turnover=32.34%
   🎚️ Intra-Step TAPE: potential=0.7537 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0384 | critic_loss=0.0042 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0021 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01668
[CYCLE] Update 134/348 | Step 135,072/500,000 | Episode 164 | Time: 18263.7s
   📊 Metrics: Return=+6.52% | Sharpe=0.023 | DD=11.49% | Turnover=31.57%
   🎚️ Intra-Step TAPE: potential=0.2863 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0418 | critic_loss=0.0141 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0071 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.93 | std=0.28 | range=[0.53, 2.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.29 | PG=0.97 | NEE=0.96  BOT: CAT=0.83 | AMZN=0.74 | NVDA=0.67
   🧭 Regime Start Dist (train resets): high_vol=67 (39.9%), low_vol=53 (31.5%), medium_vol=48 (28.6%)
   🔒 Drawdown λ snapshot=0.879 (peak 1.558, dd 3.33% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2471
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01604
[CYCLE] Update 135/348 | Step 136,080/500,000 | Episode 164 | Time: 18309.3s
   📊 Metrics: Return=+7.85% | Sharpe=0.215 | DD=20.35% | Turnover=33.78%
   🎚️ Intra-Step TAPE: potential=0.2352 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0400 | critic_loss=0.0155 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0077 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 136/348 | Step 137,088/500,000 | Episode 164 | Time: 18354.7s
   📊 Metrics: Return=-13.62% | Sharpe=-0.161 | DD=48.72% | Turnover=34.07%
   🎚️ Intra-Step TAPE: potential=0.5644 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0399 | critic_loss=0.0117 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0059 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=0.84 | std=0.13 | range=[0.50, 1.14] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=0.96 | PG=0.94 | NEE=0.91  BOT: AMZN=0.76 | JPM=0.75 | NVDA=0.66
   🧭 Regime Start Dist (train resets): high_vol=67 (39.9%), low_vol=53 (31.5%), medium_vol=48 (28.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 136 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0067 | penalty=-0.0001 | rolling_cvar=-0.02065
[CYCLE] Update 137/348 | Step 138,096/500,000 | Episode 164 | Time: 18401.8s
   📊 Metrics: Return=-15.40% | Sharpe=-0.162 | DD=48.72% | Turnover=34.20%
   🎚️ Intra-Step TAPE: potential=0.2386 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0368 | critic_loss=0.0063 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0137 | penalty=-0.0003 | rolling_cvar=-0.01924
      🧪 Deterministic validation: Sharpe=0.800 | Return=+83.27% | DD=25.91%
         Multi-horizon: score=0.811 | details=252:0.856/25.9%, 504:1.082/25.9%, 756:0.659/25.9%, 1008:0.800/25.9%
         SPY relative: spy_return=+53.67% | outperformance=+29.60%
[CYCLE] Update 138/348 | Step 139,104/500,000 | Episode 168 | Time: 18785.9s
   📊 Metrics: Return=+33.34% | Sharpe=0.468 | DD=16.03% | Turnover=33.68%
   🎚️ Intra-Step TAPE: potential=0.7465 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0359 | critic_loss=0.0162 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0081 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.09 | std=0.31 | range=[0.59, 3.20] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.44 | NEE=1.12 | JNJ=1.12  BOT: CAT=1.02 | NVDA=0.87 | AMZN=0.86
   🧭 Regime Start Dist (train resets): high_vol=67 (39.0%), low_vol=55 (32.0%), medium_vol=50 (29.1%)
   🔒 Drawdown λ snapshot=1.364 (peak 2.000, dd 2.28% / trig 14.00%) | terminal=0.000 (peak 0.003) | TAPE=0.2906
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0001 | rolling_cvar=-0.01385
[CYCLE] Update 139/348 | Step 140,112/500,000 | Episode 168 | Time: 18832.5s
   📊 Metrics: Return=+25.42% | Sharpe=0.952 | DD=9.08% | Turnover=32.30%
   🎚️ Intra-Step TAPE: potential=0.2494 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0437 | critic_loss=0.0122 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0061 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 168 | Time: 18878.1s
   📊 Metrics: Return=+40.83% | Sharpe=0.945 | DD=9.08% | Turnover=32.25%
   🎚️ Intra-Step TAPE: potential=0.2304 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0385 | critic_loss=0.0086 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0043 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.02 | std=0.21 | range=[0.58, 1.88] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.04 | XOM=1.04 | JNJ=1.03  BOT: GLD=0.94 | AMZN=0.86 | NVDA=0.75
   🧭 Regime Start Dist (train resets): high_vol=67 (39.0%), low_vol=55 (32.0%), medium_vol=50 (29.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 140 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 141/348 | Step 142,128/500,000 | Episode 168 | Time: 18924.1s
   📊 Metrics: Return=+46.41% | Sharpe=0.731 | DD=16.82% | Turnover=32.40%
   🎚️ Intra-Step TAPE: potential=0.6682 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0336 | critic_loss=0.0077 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0038 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03290
      🧪 Deterministic validation: Sharpe=0.813 | Return=+81.16% | DD=24.54%
         Multi-horizon: score=0.839 | details=252:0.888/24.5%, 504:1.108/24.5%, 756:0.673/24.5%, 1008:0.813/24.5%
         SPY relative: spy_return=+53.67% | outperformance=+27.49%
[CYCLE] Update 142/348 | Step 143,136/500,000 | Episode 172 | Time: 19308.3s
   📊 Metrics: Return=+1.80% | Sharpe=0.034 | DD=41.80% | Turnover=32.23%
   🎚️ Intra-Step TAPE: potential=0.2188 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0362 | critic_loss=0.0111 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0055 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.05 | std=0.18 | range=[0.64, 1.89] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.13 | PG=1.12 | JNJ=1.12  BOT: AMZN=0.93 | CAT=0.90 | NVDA=0.83
   🧭 Regime Start Dist (train resets): high_vol=68 (38.6%), low_vol=56 (31.8%), medium_vol=52 (29.5%)
   [WARN]  WARNING: Alpha std < 0.25 after 142 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 13.74% / trig 14.00%) | terminal=2.894 (peak 2.894) | TAPE=0.2236
   🔐 Lagrangian CVaR: λ=0.0020 | penalty=-0.0000 | rolling_cvar=-0.02238
[CYCLE] Update 143/348 | Step 144,144/500,000 | Episode 172 | Time: 19355.4s
   📊 Metrics: Return=+21.75% | Sharpe=0.740 | DD=13.74% | Turnover=32.18%
   🎚️ Intra-Step TAPE: potential=0.6948 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0364 | critic_loss=0.0061 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0030 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01936
[CYCLE] Update 144/348 | Step 145,152/500,000 | Episode 172 | Time: 19402.7s
   📊 Metrics: Return=+48.69% | Sharpe=1.087 | DD=13.74% | Turnover=31.89%
   🎚️ Intra-Step TAPE: potential=0.6276 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0413 | critic_loss=0.0102 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0051 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.11 | std=0.13 | range=[0.70, 1.43] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.18 | NEE=1.17 | MSFT=1.15  BOT: AMZN=1.06 | GLD=0.95 | NVDA=0.95
   🧭 Regime Start Dist (train resets): high_vol=68 (38.6%), low_vol=56 (31.8%), medium_vol=52 (29.5%)
   [WARN]  WARNING: Alpha std < 0.25 after 144 updates. TCN may not be learning asset discrimination.
[CYCLE] Update 145/348 | Step 146,160/500,000 | Episode 172 | Time: 19449.4s
   📊 Metrics: Return=+73.08% | Sharpe=1.131 | DD=13.74% | Turnover=31.61%
   🎚️ Intra-Step TAPE: potential=0.6523 | delta_reward=+0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0344 | critic_loss=0.0298 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0149 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
      🧪 Deterministic validation: Sharpe=0.817 | Return=+85.44% | DD=25.72%
         Multi-horizon: score=0.839 | details=252:0.887/25.7%, 504:1.111/25.7%, 756:0.683/25.7%, 1008:0.817/25.7%
         SPY relative: spy_return=+53.67% | outperformance=+31.77%
[CYCLE] Update 146/348 | Step 147,168/500,000 | Episode 176 | Time: 19833.8s
   📊 Metrics: Return=+10.11% | Sharpe=0.095 | DD=9.65% | Turnover=31.78%
   🎚️ Intra-Step TAPE: potential=0.7371 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0413 | critic_loss=0.0187 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0093 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.22 | std=0.21 | range=[0.52, 1.85] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.46 | PG=1.38 | NEE=1.35  BOT: AMZN=1.12 | JPM=1.11 | NVDA=0.97
   🧭 Regime Start Dist (train resets): high_vol=72 (40.0%), low_vol=56 (31.1%), medium_vol=52 (28.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 146 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.071, dd 4.74% / trig 14.00%) | terminal=0.000 (peak 1.158) | TAPE=0.2542
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00200) | SPY bonus=0.003 (SPY ret=-0.00290)
   🔐 Lagrangian CVaR: λ=0.0094 | penalty=-0.0001 | rolling_cvar=-0.02246
[CYCLE] Update 147/348 | Step 148,176/500,000 | Episode 176 | Time: 19879.9s
   📊 Metrics: Return=+15.32% | Sharpe=0.374 | DD=23.36% | Turnover=29.33%
   🎚️ Intra-Step TAPE: potential=0.6246 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0412 | critic_loss=0.0097 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.0532 | penalty=-0.0020 | rolling_cvar=-0.04476
[CYCLE] Update 148/348 | Step 149,184/500,000 | Episode 176 | Time: 19926.0s
   📊 Metrics: Return=+17.42% | Sharpe=0.285 | DD=23.36% | Turnover=29.35%
   🎚️ Intra-Step TAPE: potential=0.2392 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0334 | critic_loss=0.0057 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔬 Alpha Diversity: mean=1.34 | std=0.22 | range=[0.67, 1.76] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.54 | PG=1.52 | XOM=1.49  BOT: JPM=1.28 | CAT=1.23 | NVDA=0.92
   🧭 Regime Start Dist (train resets): high_vol=72 (40.0%), low_vol=56 (31.1%), medium_vol=52 (28.9%)
   [WARN]  WARNING: Alpha std < 0.25 after 148 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0832 | penalty=-0.0033 | rolling_cvar=-0.03875
   [TOOL] Actor learning rate adjusted to 0.000020 at step 150,000
[CYCLE] Update 149/348 | Step 150,192/500,000 | Episode 176 | Time: 19971.7s
   📊 Metrics: Return=+32.76% | Sharpe=0.385 | DD=23.36% | Turnover=29.20%
   🎚️ Intra-Step TAPE: potential=0.7073 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0345 | critic_loss=0.0118 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0059 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   🔐 Lagrangian CVaR: λ=0.1026 | penalty=-0.0032 | rolling_cvar=-0.03476

📚 PPO ROLLOUT UPDATE at 150,192 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 150,192 steps:
   Batch size: 336

[DOWN] PPO GAMMA UPDATE at 150,192 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 150,192 steps:
   gae_lambda: 0.9500

🌡️ TEMPERATURE UPDATE at 150,192 steps:
   temperature: 1.0000
      🧪 Deterministic validation: Sharpe=0.791 | Return=+83.47% | DD=26.53%
         Multi-horizon: score=0.805 | details=252:0.849/26.5%, 504:1.073/26.5%, 756:0.667/26.5%, 1008:0.791/26.5%
         SPY relative: spy_return=+53.67% | outperformance=+29.80%
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 180 | Time: 20384.4s
   📊 Metrics: Return=-9.52% | Sharpe=-0.077 | DD=44.83% | Turnover=29.84%
   🎚️ Intra-Step TAPE: potential=0.4890 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0364 | critic_loss=0.0223 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0111 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.82 | std=0.37 | range=[0.71, 2.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=2.08 | JNJ=2.08 | XOM=2.08  BOT: GLD=1.73 | AMZN=1.57 | NVDA=1.40
   🧭 Regime Start Dist (train resets): high_vol=72 (39.1%), low_vol=57 (31.0%), medium_vol=55 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.68% / trig 14.00%) | terminal=4.995 (peak 5.000) | TAPE=0.2199
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.01952) | SPY bonus=0.006 (SPY ret=0.01453)
   🔐 Lagrangian CVaR: λ=0.0662 | penalty=-0.0004 | rolling_cvar=-0.01534
[CYCLE] Update 151/348 | Step 153,216/500,000 | Episode 180 | Time: 20450.5s
   📊 Metrics: Return=+15.63% | Sharpe=0.328 | DD=15.11% | Turnover=25.75%
   🎚️ Intra-Step TAPE: potential=0.7473 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0327 | critic_loss=0.0119 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0059 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0259 | penalty=-0.0001 | rolling_cvar=-0.01930
[CYCLE] Update 152/348 | Step 154,728/500,000 | Episode 184 | Time: 20517.9s
   📊 Metrics: Return=+10.75% | Sharpe=0.134 | DD=41.32% | Turnover=24.79%
   🎚️ Intra-Step TAPE: potential=0.2181 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0437 | critic_loss=0.0113 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0056 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.79 | std=0.57 | range=[0.31, 4.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.24 | PG=2.17 | GLD=2.12  BOT: JPM=1.60 | AMZN=1.57 | NVDA=1.17
   🧭 Regime Start Dist (train resets): high_vol=75 (39.9%), low_vol=57 (30.3%), medium_vol=56 (29.8%)
   🔒 Drawdown λ snapshot=0.322 (peak 0.322, dd 22.09% / trig 14.00%) | terminal=2.725 (peak 2.725) | TAPE=0.2325
   🔐 Lagrangian CVaR: λ=0.0346 | penalty=-0.0007 | rolling_cvar=-0.02063
[CYCLE] Update 153/348 | Step 156,240/500,000 | Episode 184 | Time: 20584.4s
   📊 Metrics: Return=-6.87% | Sharpe=-0.052 | DD=32.16% | Turnover=24.99%
   🎚️ Intra-Step TAPE: potential=0.2346 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0470 | critic_loss=0.0119 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.1118 | penalty=-0.0058 | rolling_cvar=-0.04359
[CYCLE] Update 154/348 | Step 157,752/500,000 | Episode 184 | Time: 20651.3s
   📊 Metrics: Return=+1.81% | Sharpe=0.062 | DD=32.16% | Turnover=26.45%
   🎚️ Intra-Step TAPE: potential=0.2644 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0388 | critic_loss=0.0091 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.41 | std=0.23 | range=[0.69, 1.89] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: PG=1.60 | JNJ=1.58 | XOM=1.53  BOT: CAT=1.23 | AMZN=1.21 | NVDA=0.92
   🧭 Regime Start Dist (train resets): high_vol=75 (39.9%), low_vol=57 (30.3%), medium_vol=56 (29.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 154 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.1568 | penalty=-0.0068 | rolling_cvar=-0.03542
      🧪 Deterministic validation: Sharpe=0.801 | Return=+82.35% | DD=25.40%
         Multi-horizon: score=0.830 | details=252:0.886/25.4%, 504:1.097/25.4%, 756:0.674/25.4%, 1008:0.801/25.4%
         SPY relative: spy_return=+53.67% | outperformance=+28.67%
[CYCLE] Update 155/348 | Step 159,264/500,000 | Episode 188 | Time: 21053.4s
   📊 Metrics: Return=-4.62% | Sharpe=-0.023 | DD=41.05% | Turnover=26.93%
   🎚️ Intra-Step TAPE: potential=0.2577 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0322 | critic_loss=0.0300 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0150 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.59% / trig 14.00%) | terminal=3.089 (peak 3.715) | TAPE=0.2250
   🔐 Lagrangian CVaR: λ=0.1434 | penalty=-0.0028 | rolling_cvar=-0.01144
[CYCLE] Update 156/348 | Step 160,776/500,000 | Episode 188 | Time: 21120.0s
   📊 Metrics: Return=-11.58% | Sharpe=-0.153 | DD=40.71% | Turnover=29.08%
   🎚️ Intra-Step TAPE: potential=0.3987 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0355 | critic_loss=0.0081 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0041 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.34 | std=0.22 | range=[0.35, 2.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.48 | PG=1.46 | NEE=1.43  BOT: GLD=1.26 | AMZN=1.17 | NVDA=0.98
   🧭 Regime Start Dist (train resets): high_vol=75 (39.1%), low_vol=59 (30.7%), medium_vol=58 (30.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 156 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0971 | penalty=-0.0003 | rolling_cvar=-0.01359
[CYCLE] Update 157/348 | Step 162,288/500,000 | Episode 188 | Time: 21186.6s
   📊 Metrics: Return=+4.95% | Sharpe=0.085 | DD=40.79% | Turnover=28.94%
   🎚️ Intra-Step TAPE: potential=0.2379 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0318 | critic_loss=0.0073 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0036 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0755 | penalty=-0.0014 | rolling_cvar=-0.01701
      🧪 Deterministic validation: Sharpe=0.793 | Return=+81.85% | DD=25.77%
         Multi-horizon: score=0.816 | details=252:0.868/25.8%, 504:1.081/25.8%, 756:0.665/25.8%, 1008:0.793/25.8%
         SPY relative: spy_return=+53.67% | outperformance=+28.18%
[CYCLE] Update 158/348 | Step 163,800/500,000 | Episode 192 | Time: 21588.5s
   📊 Metrics: Return=+58.29% | Sharpe=0.775 | DD=14.25% | Turnover=28.81%
   🎚️ Intra-Step TAPE: potential=0.3897 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0442 | critic_loss=0.0132 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.27 | std=0.24 | range=[0.46, 2.27] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.48 | PG=1.42 | NEE=1.37  BOT: AMZN=1.12 | CAT=1.11 | NVDA=0.99
   🧭 Regime Start Dist (train resets): high_vol=77 (39.3%), low_vol=61 (31.1%), medium_vol=58 (29.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 158 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.458 (peak 1.451, dd 2.66% / trig 14.00%) | terminal=0.000 (peak 1.236) | TAPE=0.4463
   🔐 Lagrangian CVaR: λ=0.0528 | penalty=-0.0005 | rolling_cvar=-0.01960
[CYCLE] Update 159/348 | Step 165,312/500,000 | Episode 192 | Time: 21654.5s
   📊 Metrics: Return=+21.31% | Sharpe=0.469 | DD=11.12% | Turnover=29.62%
   🎚️ Intra-Step TAPE: potential=0.2256 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0373 | critic_loss=0.0125 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0062 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0261 | penalty=-0.0001 | rolling_cvar=-0.02140
      🧪 Deterministic validation: Sharpe=0.787 | Return=+81.86% | DD=26.14%
         Multi-horizon: score=0.806 | details=252:0.855/26.1%, 504:1.071/26.1%, 756:0.662/26.1%, 1008:0.787/26.1%
         SPY relative: spy_return=+53.67% | outperformance=+28.19%
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 196 | Time: 22051.3s
   📊 Metrics: Return=+17.79% | Sharpe=0.226 | DD=16.45% | Turnover=29.64%
   🎚️ Intra-Step TAPE: potential=0.2569 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0421 | critic_loss=0.0159 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0079 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.35 | std=0.25 | range=[0.32, 2.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.53 | NEE=1.50 | PG=1.48  BOT: AMZN=1.28 | CAT=1.24 | NVDA=1.03
   🧭 Regime Start Dist (train resets): high_vol=79 (39.5%), low_vol=61 (30.5%), medium_vol=60 (30.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 160 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.006 (peak 0.041, dd 7.06% / trig 14.00%) | terminal=0.000 (peak 0.021) | TAPE=0.2551
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00306) | SPY bonus=0.007 (SPY ret=0.00184)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01583
[CYCLE] Update 161/348 | Step 168,336/500,000 | Episode 196 | Time: 22118.5s
   📊 Metrics: Return=+16.44% | Sharpe=0.420 | DD=21.88% | Turnover=28.38%
   🎚️ Intra-Step TAPE: potential=0.6533 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0318 | critic_loss=0.0079 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0039 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01346
[CYCLE] Update 162/348 | Step 169,848/500,000 | Episode 196 | Time: 22185.9s
   📊 Metrics: Return=+28.33% | Sharpe=0.395 | DD=21.88% | Turnover=28.73%
   🎚️ Intra-Step TAPE: potential=0.2791 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0346 | critic_loss=0.0116 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.32 | std=0.29 | range=[0.29, 2.24] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.60 | PG=1.56 | NEE=1.53  BOT: JPM=1.18 | AMZN=1.17 | NVDA=0.98
   🧭 Regime Start Dist (train resets): high_vol=79 (39.5%), low_vol=61 (30.5%), medium_vol=60 (30.0%)
   🔐 Lagrangian CVaR: λ=0.0006 | penalty=-0.0000 | rolling_cvar=-0.01686
      🧪 Deterministic validation: Sharpe=0.787 | Return=+82.72% | DD=26.49%
         Multi-horizon: score=0.799 | details=252:0.846/26.5%, 504:1.065/26.5%, 756:0.657/26.5%, 1008:0.787/26.5%
         SPY relative: spy_return=+53.67% | outperformance=+29.05%
[CYCLE] Update 163/348 | Step 171,360/500,000 | Episode 200 | Time: 22591.3s
   📊 Metrics: Return=+26.35% | Sharpe=0.398 | DD=15.66% | Turnover=29.27%
   🎚️ Intra-Step TAPE: potential=0.2375 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0464 | critic_loss=0.0097 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.37% / trig 14.00%) | terminal=0.000 (peak 0.002) | TAPE=0.2794
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02197
[CYCLE] Update 164/348 | Step 172,872/500,000 | Episode 200 | Time: 22656.0s
   📊 Metrics: Return=+26.58% | Sharpe=0.624 | DD=12.10% | Turnover=29.27%
   🎚️ Intra-Step TAPE: potential=0.4884 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0420 | critic_loss=0.0067 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.48 | std=0.35 | range=[0.29, 2.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.79 | PG=1.76 | NEE=1.71  BOT: CAT=1.35 | AMZN=1.30 | NVDA=1.09
   🧭 Regime Start Dist (train resets): high_vol=79 (38.7%), low_vol=62 (30.4%), medium_vol=63 (30.9%)
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.04032
[CYCLE] Update 165/348 | Step 174,384/500,000 | Episode 200 | Time: 22720.5s
   📊 Metrics: Return=+36.06% | Sharpe=0.529 | DD=12.10% | Turnover=28.60%
   🎚️ Intra-Step TAPE: potential=0.2237 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0417 | critic_loss=0.0045 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0014 | penalty=-0.0000 | rolling_cvar=-0.03437
[CYCLE] Update 166/348 | Step 175,896/500,000 | Episode 204 | Time: 22784.5s
   📊 Metrics: Return=+16.86% | Sharpe=0.198 | DD=38.23% | Turnover=27.66%
   🎚️ Intra-Step TAPE: potential=0.7338 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0409 | critic_loss=0.0151 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.58 | std=0.24 | range=[0.39, 2.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.76 | NEE=1.73 | PG=1.72  BOT: GLD=1.47 | AMZN=1.46 | NVDA=1.41
   🧭 Regime Start Dist (train resets): high_vol=79 (38.0%), low_vol=64 (30.8%), medium_vol=65 (31.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 166 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.61% / trig 14.00%) | terminal=1.422 (peak 2.461) | TAPE=0.2365
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01955
[CYCLE] Update 167/348 | Step 177,408/500,000 | Episode 204 | Time: 22849.9s
   📊 Metrics: Return=+16.83% | Sharpe=0.364 | DD=13.92% | Turnover=27.14%
   🎚️ Intra-Step TAPE: potential=0.2901 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0390 | critic_loss=0.0081 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0041 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
      🧪 Deterministic validation: Sharpe=0.794 | Return=+84.51% | DD=26.73%
         Multi-horizon: score=0.800 | details=252:0.844/26.7%, 504:1.068/26.7%, 756:0.662/26.7%, 1008:0.794/26.7%
         SPY relative: spy_return=+53.67% | outperformance=+30.84%
[CYCLE] Update 168/348 | Step 178,920/500,000 | Episode 208 | Time: 23241.2s
   📊 Metrics: Return=+66.68% | Sharpe=0.949 | DD=16.64% | Turnover=27.04%
   🎚️ Intra-Step TAPE: potential=0.2442 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0450 | critic_loss=0.0101 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.51 | std=0.32 | range=[0.29, 2.43] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.78 | PG=1.75 | NEE=1.73  BOT: CAT=1.47 | AMZN=1.38 | NVDA=1.13
   🧭 Regime Start Dist (train resets): high_vol=80 (37.7%), low_vol=67 (31.6%), medium_vol=65 (30.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.84% / trig 14.00%) | terminal=0.000 (peak 0.569) | TAPE=0.4780
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01739
[CYCLE] Update 169/348 | Step 180,432/500,000 | Episode 208 | Time: 23305.8s
   📊 Metrics: Return=-21.03% | Sharpe=-0.350 | DD=41.73% | Turnover=26.35%
   🎚️ Intra-Step TAPE: potential=0.6067 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0369 | critic_loss=0.0040 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0018 | penalty=-0.0000 | rolling_cvar=-0.01431
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 208 | Time: 23370.3s
   📊 Metrics: Return=+2.49% | Sharpe=0.067 | DD=41.73% | Turnover=27.59%
   🎚️ Intra-Step TAPE: potential=0.7429 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0426 | critic_loss=0.0035 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.28 | std=0.23 | range=[0.31, 1.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.47 | PG=1.43 | NEE=1.38  BOT: JPM=1.18 | CAT=1.13 | NVDA=0.97
   🧭 Regime Start Dist (train resets): high_vol=80 (37.7%), low_vol=67 (31.6%), medium_vol=65 (30.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 170 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0193 | penalty=-0.0004 | rolling_cvar=-0.01676
      🧪 Deterministic validation: Sharpe=0.805 | Return=+83.50% | DD=25.69%
         Multi-horizon: score=0.826 | details=252:0.880/25.7%, 504:1.092/25.7%, 756:0.673/25.7%, 1008:0.805/25.7%
         SPY relative: spy_return=+53.67% | outperformance=+29.83%
[CYCLE] Update 171/348 | Step 183,456/500,000 | Episode 212 | Time: 23762.6s
   📊 Metrics: Return=+33.16% | Sharpe=0.517 | DD=10.52% | Turnover=28.86%
   🎚️ Intra-Step TAPE: potential=0.6354 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0415 | critic_loss=0.0097 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0049 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.997 (peak 1.458, dd 0.18% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3148
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00021) | SPY bonus=0.005 (SPY ret=-0.00299)
   🔐 Lagrangian CVaR: λ=0.0264 | penalty=-0.0007 | rolling_cvar=-0.03068
[CYCLE] Update 172/348 | Step 184,968/500,000 | Episode 212 | Time: 23827.6s
   📊 Metrics: Return=+27.40% | Sharpe=0.497 | DD=20.80% | Turnover=30.58%
   🎚️ Intra-Step TAPE: potential=0.2864 | delta_reward=-0.0024
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0352 | critic_loss=0.0067 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.12 | std=0.22 | range=[0.63, 2.00] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.21 | PG=1.19 | NEE=1.16  BOT: AMZN=0.95 | CAT=0.95 | NVDA=0.83
   🧭 Regime Start Dist (train resets): high_vol=83 (38.4%), low_vol=67 (31.0%), medium_vol=66 (30.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 172 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0264 | penalty=-0.0005 | rolling_cvar=-0.02524
[CYCLE] Update 173/348 | Step 186,480/500,000 | Episode 212 | Time: 23891.8s
   📊 Metrics: Return=+35.18% | Sharpe=0.400 | DD=20.80% | Turnover=31.05%
   🎚️ Intra-Step TAPE: potential=0.7202 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0327 | critic_loss=0.0088 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0044 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0123 | penalty=-0.0001 | rolling_cvar=-0.02442
      🧪 Deterministic validation: Sharpe=0.812 | Return=+82.41% | DD=24.96%
         Multi-horizon: score=0.840 | details=252:0.897/25.0%, 504:1.103/25.0%, 756:0.679/25.0%, 1008:0.812/25.0%
         SPY relative: spy_return=+53.67% | outperformance=+28.73%
[CYCLE] Update 174/348 | Step 187,992/500,000 | Episode 216 | Time: 24278.8s
   📊 Metrics: Return=+44.76% | Sharpe=0.518 | DD=18.39% | Turnover=31.07%
   🎚️ Intra-Step TAPE: potential=0.2319 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0401 | critic_loss=0.0064 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0032 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.11 | std=0.29 | range=[0.33, 2.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.19 | PG=1.15 | XOM=1.12  BOT: JPM=0.99 | AMZN=0.91 | NVDA=0.84
   🧭 Regime Start Dist (train resets): high_vol=84 (38.2%), low_vol=67 (30.5%), medium_vol=69 (31.4%)
   🔒 Drawdown λ snapshot=1.769 (peak 1.769, dd 37.67% / trig 14.00%) | terminal=0.000 (peak 0.016) | TAPE=0.3090
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00263) | SPY bonus=0.007 (SPY ret=0.00042)
   🔐 Lagrangian CVaR: λ=0.0004 | penalty=-0.0000 | rolling_cvar=-0.01291
[CYCLE] Update 175/348 | Step 189,504/500,000 | Episode 216 | Time: 24343.2s
   📊 Metrics: Return=-19.01% | Sharpe=-0.242 | DD=43.86% | Turnover=31.73%
   🎚️ Intra-Step TAPE: potential=0.2393 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0325 | critic_loss=0.0049 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0201 | penalty=-0.0005 | rolling_cvar=-0.01378
      🧪 Deterministic validation: Sharpe=0.817 | Return=+79.85% | DD=23.85%
         Multi-horizon: score=0.860 | details=252:0.926/23.9%, 504:1.119/23.9%, 756:0.687/23.9%, 1008:0.817/23.9%
         SPY relative: spy_return=+53.67% | outperformance=+26.18%
[CYCLE] Update 176/348 | Step 191,016/500,000 | Episode 220 | Time: 24737.0s
   📊 Metrics: Return=+29.62% | Sharpe=0.478 | DD=12.80% | Turnover=31.85%
   🎚️ Intra-Step TAPE: potential=0.2158 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0417 | critic_loss=0.0080 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.09 | std=0.32 | range=[0.29, 2.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.13 | PG=1.13 | NEE=1.09  BOT: JPM=0.96 | AMZN=0.95 | NVDA=0.77
   🧭 Regime Start Dist (train resets): high_vol=86 (38.4%), low_vol=68 (30.4%), medium_vol=70 (31.2%)
   🔒 Drawdown λ snapshot=2.266 (peak 2.266, dd 19.63% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3007
   🔐 Lagrangian CVaR: λ=0.0301 | penalty=-0.0008 | rolling_cvar=-0.01333
[CYCLE] Update 177/348 | Step 192,528/500,000 | Episode 220 | Time: 24802.6s
   📊 Metrics: Return=+9.15% | Sharpe=0.241 | DD=32.65% | Turnover=31.41%
   🎚️ Intra-Step TAPE: potential=0.2300 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0397 | critic_loss=0.0068 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0688 | penalty=-0.0026 | rolling_cvar=-0.01303
[CYCLE] Update 178/348 | Step 194,040/500,000 | Episode 220 | Time: 24867.1s
   📊 Metrics: Return=+16.88% | Sharpe=0.231 | DD=32.65% | Turnover=31.66%
   🎚️ Intra-Step TAPE: potential=0.2412 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0374 | critic_loss=0.0056 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0028 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.08 | std=0.16 | range=[0.70, 1.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=1.14 | JNJ=1.13 | PG=1.13  BOT: CAT=0.99 | AMZN=0.98 | NVDA=0.89
   🧭 Regime Start Dist (train resets): high_vol=86 (38.4%), low_vol=68 (30.4%), medium_vol=70 (31.2%)
   [WARN]  WARNING: Alpha std < 0.25 after 178 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0729 | penalty=-0.0017 | rolling_cvar=-0.01389
[CYCLE] Update 179/348 | Step 195,552/500,000 | Episode 224 | Time: 24931.1s
   📊 Metrics: Return=+12.85% | Sharpe=0.149 | DD=16.16% | Turnover=32.16%
   🎚️ Intra-Step TAPE: potential=0.2263 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0410 | critic_loss=0.0066 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.221, dd 2.42% / trig 14.00%) | terminal=0.000 (peak 0.004) | TAPE=0.2523
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00082) | SPY bonus=0.009 (SPY ret=-0.00660)
   🔐 Lagrangian CVaR: λ=0.0646 | penalty=-0.0008 | rolling_cvar=-0.02491
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 224 | Time: 24994.7s
   📊 Metrics: Return=+18.48% | Sharpe=0.424 | DD=15.56% | Turnover=31.46%
   🎚️ Intra-Step TAPE: potential=0.2345 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0302 | critic_loss=0.0058 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.17 | std=0.24 | range=[0.26, 1.87] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.34 | PG=1.30 | GLD=1.29  BOT: JPM=1.04 | CAT=1.04 | NVDA=0.92
   🧭 Regime Start Dist (train resets): high_vol=89 (39.0%), low_vol=68 (29.8%), medium_vol=71 (31.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 180 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.1105 | penalty=-0.0045 | rolling_cvar=-0.04085
[CYCLE] Update 181/348 | Step 198,576/500,000 | Episode 224 | Time: 25058.2s
   📊 Metrics: Return=+32.18% | Sharpe=0.437 | DD=15.56% | Turnover=31.24%
   🎚️ Intra-Step TAPE: potential=0.5164 | delta_reward=+0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0377 | critic_loss=0.0056 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0028 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.1300 | penalty=-0.0037 | rolling_cvar=-0.03509
      🧪 Deterministic validation: Sharpe=0.823 | Return=+88.36% | DD=25.90%
         Multi-horizon: score=0.838 | details=252:0.887/25.9%, 504:1.110/25.9%, 756:0.677/25.9%, 1008:0.823/25.9%
         SPY relative: spy_return=+53.67% | outperformance=+34.68%

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.9

🎛️ EXECUTION BETA UPDATE at 200,088 steps:
   action_execution_beta: 0.550 (w_exec=(1-β)w_prev + βw_raw)
[CYCLE] Update 182/348 | Step 200,088/500,000 | Episode 228 | Time: 25436.0s
   📊 Metrics: Return=-2.25% | Sharpe=0.007 | DD=42.52% | Turnover=30.75%
   🎚️ Intra-Step TAPE: potential=0.2836 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0395 | critic_loss=0.0062 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.32 | std=0.18 | range=[0.76, 1.93] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.41 | NEE=1.41 | PG=1.39  BOT: CAT=1.23 | AMZN=1.21 | NVDA=1.06
   🧭 Regime Start Dist (train resets): high_vol=90 (38.8%), low_vol=70 (30.2%), medium_vol=72 (31.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 182 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.56% / trig 14.00%) | terminal=4.141 (peak 4.524) | TAPE=0.2229
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00578) | SPY bonus=0.000 (SPY ret=-0.00610)
   🔐 Lagrangian CVaR: λ=0.1038 | penalty=-0.0008 | rolling_cvar=-0.01558
[CYCLE] Update 183/348 | Step 201,600/500,000 | Episode 228 | Time: 25498.3s
   📊 Metrics: Return=+16.22% | Sharpe=0.376 | DD=11.19% | Turnover=33.66%
   🎚️ Intra-Step TAPE: potential=0.5324 | delta_reward=+0.0017
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0326 | critic_loss=0.0038 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0019 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0933 | penalty=-0.0018 | rolling_cvar=-0.01965
      🧪 Deterministic validation: Sharpe=0.825 | Return=+88.20% | DD=25.87%
         Multi-horizon: score=0.839 | details=252:0.888/25.9%, 504:1.111/25.9%, 756:0.679/25.9%, 1008:0.825/25.9%
         SPY relative: spy_return=+53.67% | outperformance=+34.53%
[CYCLE] Update 184/348 | Step 203,112/500,000 | Episode 232 | Time: 25876.3s
   📊 Metrics: Return=+18.44% | Sharpe=0.212 | DD=39.88% | Turnover=32.77%
   🎚️ Intra-Step TAPE: potential=0.5901 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0364 | critic_loss=0.0077 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0039 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.50 | std=0.29 | range=[0.29, 2.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.65 | NEE=1.61 | PG=1.60  BOT: JPM=1.45 | AMZN=1.37 | NVDA=1.23
   🧭 Regime Start Dist (train resets): high_vol=92 (39.0%), low_vol=72 (30.5%), medium_vol=72 (30.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.75% / trig 14.00%) | terminal=2.834 (peak 2.834) | TAPE=0.2391
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00039) | SPY bonus=0.006 (SPY ret=-0.00412)
   🔐 Lagrangian CVaR: λ=0.0843 | penalty=-0.0014 | rolling_cvar=-0.01923
[CYCLE] Update 185/348 | Step 204,624/500,000 | Episode 232 | Time: 25939.4s
   📊 Metrics: Return=-11.25% | Sharpe=-0.125 | DD=43.01% | Turnover=33.76%
   🎚️ Intra-Step TAPE: potential=0.7270 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0471 | critic_loss=0.0049 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0783 | penalty=-0.0018 | rolling_cvar=-0.02024
[CYCLE] Update 186/348 | Step 206,136/500,000 | Episode 232 | Time: 26002.3s
   📊 Metrics: Return=-6.79% | Sharpe=-0.045 | DD=43.01% | Turnover=34.29%
   🎚️ Intra-Step TAPE: potential=0.2271 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0460 | critic_loss=0.0070 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0035 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.65 | std=0.36 | range=[0.31, 2.53] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.91 | JNJ=1.89 | PG=1.86  BOT: AMZN=1.56 | JPM=1.47 | NVDA=1.25
   🧭 Regime Start Dist (train resets): high_vol=92 (39.0%), low_vol=72 (30.5%), medium_vol=72 (30.5%)
   🔐 Lagrangian CVaR: λ=0.1135 | penalty=-0.0036 | rolling_cvar=-0.03658
      🧪 Deterministic validation: Sharpe=0.826 | Return=+88.36% | DD=25.96%
         Multi-horizon: score=0.839 | details=252:0.887/26.0%, 504:1.112/26.0%, 756:0.679/26.0%, 1008:0.826/26.0%
         SPY relative: spy_return=+53.67% | outperformance=+34.69%
[CYCLE] Update 187/348 | Step 207,648/500,000 | Episode 236 | Time: 26393.0s
   📊 Metrics: Return=+4.47% | Sharpe=0.075 | DD=40.92% | Turnover=34.52%
   🎚️ Intra-Step TAPE: potential=0.2312 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0441 | critic_loss=0.0135 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0068 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=1.429 (peak 1.969, dd 7.26% / trig 14.00%) | terminal=3.869 (peak 3.870) | TAPE=0.2247
   🔐 Lagrangian CVaR: λ=0.1183 | penalty=-0.0033 | rolling_cvar=-0.01473
[CYCLE] Update 188/348 | Step 209,160/500,000 | Episode 236 | Time: 26458.2s
   📊 Metrics: Return=+12.51% | Sharpe=0.312 | DD=14.91% | Turnover=33.79%
   🎚️ Intra-Step TAPE: potential=0.2451 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0440 | critic_loss=0.0152 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0076 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.03 | std=0.24 | range=[1.25, 3.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.13 | NEE=2.11 | MSFT=2.11  BOT: AMZN=1.95 | CAT=1.91 | NVDA=1.77
   🧭 Regime Start Dist (train resets): high_vol=95 (39.6%), low_vol=73 (30.4%), medium_vol=72 (30.0%)
   [WARN]  WARNING: Alpha std < 0.25 after 188 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0762 | penalty=0.0000 | rolling_cvar=-0.01394
[CYCLE] Update 189/348 | Step 210,672/500,000 | Episode 236 | Time: 26522.5s
   📊 Metrics: Return=+43.75% | Sharpe=0.711 | DD=14.91% | Turnover=32.30%
   🎚️ Intra-Step TAPE: potential=0.2280 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0354 | critic_loss=0.0108 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0275 | penalty=0.0000 | rolling_cvar=-0.01544
      🧪 Deterministic validation: Sharpe=0.831 | Return=+88.37% | DD=25.83%
         Multi-horizon: score=0.847 | details=252:0.896/25.8%, 504:1.119/25.8%, 756:0.687/25.8%, 1008:0.831/25.8%
         SPY relative: spy_return=+53.67% | outperformance=+34.70%
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 240 | Time: 26913.3s
   📊 Metrics: Return=+57.08% | Sharpe=0.854 | DD=13.90% | Turnover=32.08%
   🎚️ Intra-Step TAPE: potential=0.2432 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0458 | critic_loss=0.0130 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0065 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.95 | std=0.36 | range=[0.43, 2.95] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=2.23 | JNJ=2.22 | PG=2.17  BOT: CAT=1.77 | JPM=1.74 | NVDA=1.56
   🧭 Regime Start Dist (train resets): high_vol=98 (40.2%), low_vol=74 (30.3%), medium_vol=72 (29.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 9.15% / trig 14.00%) | terminal=0.000 (peak 1.548) | TAPE=0.4708
   🔐 Lagrangian CVaR: λ=0.0763 | penalty=-0.0032 | rolling_cvar=-0.04912
[CYCLE] Update 191/348 | Step 213,696/500,000 | Episode 240 | Time: 26978.3s
   📊 Metrics: Return=+30.67% | Sharpe=0.696 | DD=11.72% | Turnover=31.94%
   🎚️ Intra-Step TAPE: potential=0.6677 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0402 | critic_loss=0.0035 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.1130 | penalty=-0.0042 | rolling_cvar=-0.03799
[CYCLE] Update 192/348 | Step 215,208/500,000 | Episode 244 | Time: 27043.4s
   📊 Metrics: Return=+4.63% | Sharpe=0.078 | DD=34.69% | Turnover=32.12%
   🎚️ Intra-Step TAPE: potential=0.6531 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0321 | critic_loss=0.0098 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0049 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.91 | std=0.30 | range=[0.97, 3.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=2.08 | JNJ=2.08 | GLD=2.06  BOT: CAT=1.81 | AMZN=1.81 | NVDA=1.54
   🧭 Regime Start Dist (train resets): high_vol=98 (39.5%), low_vol=75 (30.2%), medium_vol=75 (30.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.82% / trig 14.00%) | terminal=0.000 (peak 1.405) | TAPE=0.2282
   🔐 Lagrangian CVaR: λ=0.1183 | penalty=-0.0030 | rolling_cvar=-0.01097
[CYCLE] Update 193/348 | Step 216,720/500,000 | Episode 244 | Time: 27108.8s
   📊 Metrics: Return=+19.97% | Sharpe=0.759 | DD=8.22% | Turnover=31.14%
   🎚️ Intra-Step TAPE: potential=0.2309 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0397 | critic_loss=0.0048 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.1146 | penalty=-0.0040 | rolling_cvar=-0.01269
[CYCLE] Update 194/348 | Step 218,232/500,000 | Episode 244 | Time: 27173.4s
   📊 Metrics: Return=+58.62% | Sharpe=1.017 | DD=9.43% | Turnover=31.97%
   🎚️ Intra-Step TAPE: potential=0.6280 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0387 | critic_loss=0.0051 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.83 | std=0.28 | range=[0.56, 2.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=2.04 | PG=2.02 | GLD=2.01  BOT: CAT=1.72 | AMZN=1.67 | NVDA=1.42
   🧭 Regime Start Dist (train resets): high_vol=98 (39.5%), low_vol=75 (30.2%), medium_vol=75 (30.2%)
   🔐 Lagrangian CVaR: λ=0.1106 | penalty=-0.0027 | rolling_cvar=-0.01646
      🧪 Deterministic validation: Sharpe=0.826 | Return=+88.06% | DD=26.09%
         Multi-horizon: score=0.837 | details=252:0.882/26.1%, 504:1.110/26.1%, 756:0.685/26.1%, 1008:0.826/26.1%
         SPY relative: spy_return=+53.67% | outperformance=+34.38%
[CYCLE] Update 195/348 | Step 219,744/500,000 | Episode 248 | Time: 27571.1s
   📊 Metrics: Return=+24.92% | Sharpe=0.376 | DD=16.40% | Turnover=32.72%
   🎚️ Intra-Step TAPE: potential=0.2382 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0375 | critic_loss=0.0200 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0100 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.018, dd 7.50% / trig 14.00%) | terminal=0.000 (peak 0.004) | TAPE=0.2748
   🔐 Lagrangian CVaR: λ=0.1100 | penalty=-0.0026 | rolling_cvar=-0.02871
[CYCLE] Update 196/348 | Step 221,256/500,000 | Episode 248 | Time: 27637.7s
   📊 Metrics: Return=+0.03% | Sharpe=-0.069 | DD=15.50% | Turnover=33.97%
   🎚️ Intra-Step TAPE: potential=0.3047 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0400 | critic_loss=0.0047 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.57 | std=0.18 | range=[0.99, 2.20] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.68 | PG=1.66 | NEE=1.65  BOT: JPM=1.51 | CAT=1.42 | NVDA=1.35
   🧭 Regime Start Dist (train resets): high_vol=98 (38.9%), low_vol=77 (30.6%), medium_vol=77 (30.6%)
   [WARN]  WARNING: Alpha std < 0.25 after 196 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0835 | penalty=-0.0001 | rolling_cvar=-0.02107
[CYCLE] Update 197/348 | Step 222,768/500,000 | Episode 248 | Time: 27704.9s
   📊 Metrics: Return=+3.01% | Sharpe=-0.032 | DD=15.50% | Turnover=34.77%
   🎚️ Intra-Step TAPE: potential=0.2363 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0308 | critic_loss=0.0034 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0683 | penalty=-0.0009 | rolling_cvar=-0.01894
      🧪 Deterministic validation: Sharpe=0.830 | Return=+86.61% | DD=25.34%
         Multi-horizon: score=0.845 | details=252:0.893/25.3%, 504:1.116/25.3%, 756:0.683/25.3%, 1008:0.830/25.3%
         SPY relative: spy_return=+53.67% | outperformance=+32.94%
[CYCLE] Update 198/348 | Step 224,280/500,000 | Episode 252 | Time: 28097.6s
   📊 Metrics: Return=+1.76% | Sharpe=-0.059 | DD=17.05% | Turnover=34.59%
   🎚️ Intra-Step TAPE: potential=0.4595 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0379 | critic_loss=0.0031 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0016 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.31 | std=0.22 | range=[0.60, 2.31] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.39 | GLD=1.37 | PG=1.36  BOT: AMZN=1.19 | CAT=1.17 | NVDA=1.08
   🧭 Regime Start Dist (train resets): high_vol=101 (39.5%), low_vol=78 (30.5%), medium_vol=77 (30.1%)
   [WARN]  WARNING: Alpha std < 0.25 after 198 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 6.88% / trig 14.00%) | terminal=0.000 (peak 0.006) | TAPE=0.2347
   🔐 Lagrangian CVaR: λ=0.0555 | penalty=-0.0010 | rolling_cvar=-0.05065
[CYCLE] Update 199/348 | Step 225,792/500,000 | Episode 252 | Time: 28163.0s
   📊 Metrics: Return=+32.44% | Sharpe=0.756 | DD=13.20% | Turnover=37.17%
   🎚️ Intra-Step TAPE: potential=0.5289 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0364 | critic_loss=0.0033 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0654 | penalty=-0.0018 | rolling_cvar=-0.04022
      🧪 Deterministic validation: Sharpe=0.840 | Return=+89.34% | DD=25.49%
         Multi-horizon: score=0.855 | details=252:0.903/25.5%, 504:1.129/25.5%, 756:0.688/25.5%, 1008:0.840/25.5%
         SPY relative: spy_return=+53.67% | outperformance=+35.67%
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 256 | Time: 28557.3s
   📊 Metrics: Return=-17.65% | Sharpe=-0.171 | DD=44.28% | Turnover=37.59%
   🎚️ Intra-Step TAPE: potential=0.2392 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0435 | critic_loss=0.0067 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.32 | std=0.21 | range=[0.85, 2.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.33 | GLD=1.33 | PG=1.33  BOT: JPM=1.23 | CAT=1.20 | NVDA=1.14
   🧭 Regime Start Dist (train resets): high_vol=102 (39.2%), low_vol=79 (30.4%), medium_vol=79 (30.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 200 updates. TCN may not be learning asset discrimination.
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.06% / trig 14.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2134
   🔐 Lagrangian CVaR: λ=0.0643 | penalty=-0.0016 | rolling_cvar=-0.01585
[CYCLE] Update 201/348 | Step 228,816/500,000 | Episode 256 | Time: 28622.0s
   📊 Metrics: Return=+18.97% | Sharpe=0.648 | DD=12.24% | Turnover=38.09%
   🎚️ Intra-Step TAPE: potential=0.6974 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0343 | critic_loss=0.0025 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0012 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0206 | penalty=-0.0000 | rolling_cvar=-0.01444
[CYCLE] Update 202/348 | Step 230,328/500,000 | Episode 256 | Time: 28687.4s
   📊 Metrics: Return=+53.12% | Sharpe=0.993 | DD=12.24% | Turnover=37.31%
   🎚️ Intra-Step TAPE: potential=0.4105 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0377 | critic_loss=0.0023 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0012 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.43 | std=0.20 | range=[0.51, 2.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.47 | JNJ=1.46 | PG=1.42  BOT: CAT=1.37 | JPM=1.37 | NVDA=1.33
   🧭 Regime Start Dist (train resets): high_vol=102 (39.2%), low_vol=79 (30.4%), medium_vol=79 (30.4%)
   [WARN]  WARNING: Alpha std < 0.25 after 202 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0002 | rolling_cvar=-0.01468
      🧪 Deterministic validation: Sharpe=0.846 | Return=+91.70% | DD=25.73%
         Multi-horizon: score=0.860 | details=252:0.909/25.7%, 504:1.136/25.7%, 756:0.691/25.7%, 1008:0.846/25.7%
         SPY relative: spy_return=+53.67% | outperformance=+38.03%
[CYCLE] Update 203/348 | Step 231,840/500,000 | Episode 260 | Time: 29080.5s
   📊 Metrics: Return=+13.43% | Sharpe=0.160 | DD=10.15% | Turnover=37.52%
   🎚️ Intra-Step TAPE: potential=0.2424 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0392 | critic_loss=0.0137 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0068 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.57% / trig 14.00%) | terminal=0.000 (peak 2.000) | TAPE=0.2582
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00130) | SPY bonus=0.019 (SPY ret=-0.00415)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01402
[CYCLE] Update 204/348 | Step 233,352/500,000 | Episode 260 | Time: 29145.4s
   📊 Metrics: Return=+42.16% | Sharpe=1.131 | DD=11.90% | Turnover=35.41%
   🎚️ Intra-Step TAPE: potential=0.6464 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0454 | critic_loss=0.0088 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0044 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.47 | std=0.27 | range=[0.91, 2.72] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.46 | MSFT=1.45 | PG=1.44  BOT: CAT=1.37 | AMZN=1.37 | NVDA=1.31
   🧭 Regime Start Dist (train resets): high_vol=105 (39.8%), low_vol=80 (30.3%), medium_vol=79 (29.9%)
[CYCLE] Update 205/348 | Step 234,864/500,000 | Episode 260 | Time: 29210.4s
   📊 Metrics: Return=+41.44% | Sharpe=0.579 | DD=14.88% | Turnover=35.99%
   🎚️ Intra-Step TAPE: potential=0.2462 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0390 | critic_loss=0.0032 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0016 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
[CYCLE] Update 206/348 | Step 236,376/500,000 | Episode 264 | Time: 29275.0s
   📊 Metrics: Return=+26.96% | Sharpe=0.408 | DD=10.84% | Turnover=36.31%
   🎚️ Intra-Step TAPE: potential=0.3244 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0454 | critic_loss=0.0129 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0064 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.29 | std=0.26 | range=[0.58, 2.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.32 | PG=1.29 | GLD=1.29  BOT: CAT=1.20 | AMZN=1.19 | NVDA=1.10
   🧭 Regime Start Dist (train resets): high_vol=108 (40.3%), low_vol=80 (29.9%), medium_vol=80 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.078, dd 1.57% / trig 14.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2898
   🔐 Lagrangian CVaR: λ=0.0003 | penalty=-0.0000 | rolling_cvar=-0.02298
[CYCLE] Update 207/348 | Step 237,888/500,000 | Episode 264 | Time: 29339.3s
   📊 Metrics: Return=+7.01% | Sharpe=0.090 | DD=9.54% | Turnover=37.43%
   🎚️ Intra-Step TAPE: potential=0.2400 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0404 | critic_loss=0.0048 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0144 | penalty=-0.0003 | rolling_cvar=-0.03792
      🧪 Deterministic validation: Sharpe=0.842 | Return=+88.83% | DD=25.10%
         Multi-horizon: score=0.860 | details=252:0.913/25.1%, 504:1.133/25.1%, 756:0.688/25.1%, 1008:0.842/25.1%
         SPY relative: spy_return=+53.67% | outperformance=+35.16%
[CYCLE] Update 208/348 | Step 239,400/500,000 | Episode 268 | Time: 29730.5s
   📊 Metrics: Return=+3.54% | Sharpe=0.066 | DD=46.49% | Turnover=38.04%
   🎚️ Intra-Step TAPE: potential=0.2609 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0407 | critic_loss=0.0067 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.29 | std=0.27 | range=[0.54, 2.86] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.33 | JNJ=1.32 | PG=1.31  BOT: CAT=1.20 | JPM=1.18 | NVDA=1.07
   🧭 Regime Start Dist (train resets): high_vol=109 (40.1%), low_vol=81 (29.8%), medium_vol=82 (30.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.72% / trig 14.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2226
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00284) | SPY bonus=0.005 (SPY ret=-0.00015)
   🔐 Lagrangian CVaR: λ=0.0272 | penalty=-0.0006 | rolling_cvar=-0.01823

📚 EPISODE HORIZON UPDATE at 240,912 steps:
   Episode horizon: 1053 steps
[CYCLE] Update 209/348 | Step 240,912/500,000 | Episode 268 | Time: 29795.1s
   📊 Metrics: Return=+20.62% | Sharpe=0.709 | DD=11.25% | Turnover=37.74%
   🎚️ Intra-Step TAPE: potential=0.5589 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0321 | critic_loss=0.0040 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0442 | penalty=-0.0013 | rolling_cvar=-0.01782

📚 EPISODE HORIZON UPDATE at 242,424 steps:
   Episode horizon: 1127 steps
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 268 | Time: 29859.7s
   📊 Metrics: Return=+42.24% | Sharpe=0.798 | DD=11.25% | Turnover=36.99%
   🎚️ Intra-Step TAPE: potential=0.6016 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0300 | critic_loss=0.0044 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.40 | std=0.30 | range=[0.59, 3.01] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.44 | GLD=1.44 | PG=1.41  BOT: CAT=1.28 | JPM=1.25 | NVDA=1.12
   🧭 Regime Start Dist (train resets): high_vol=109 (40.1%), low_vol=81 (29.8%), medium_vol=82 (30.1%)
   🔐 Lagrangian CVaR: λ=0.0816 | penalty=-0.0027 | rolling_cvar=-0.03597
      🧪 Deterministic validation: Sharpe=0.842 | Return=+87.95% | DD=24.92%
         Multi-horizon: score=0.863 | details=252:0.916/24.9%, 504:1.134/24.9%, 756:0.690/24.9%, 1008:0.842/24.9%
         SPY relative: spy_return=+53.67% | outperformance=+34.27%

📚 EPISODE HORIZON UPDATE at 243,936 steps:
   Episode horizon: 1202 steps
[CYCLE] Update 211/348 | Step 243,936/500,000 | Episode 272 | Time: 30251.1s
   📊 Metrics: Return=-4.79% | Sharpe=-0.030 | DD=44.50% | Turnover=37.85%
   🎚️ Intra-Step TAPE: potential=0.3451 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0442 | critic_loss=0.0114 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0057 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.18% / trig 14.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2202
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00962) | SPY bonus=0.018 (SPY ret=-0.01484)
   🔐 Lagrangian CVaR: λ=0.1016 | penalty=-0.0029 | rolling_cvar=-0.01082

📚 EPISODE HORIZON UPDATE at 245,448 steps:
   Episode horizon: 1276 steps
[CYCLE] Update 212/348 | Step 245,448/500,000 | Episode 272 | Time: 30316.4s
   📊 Metrics: Return=+6.17% | Sharpe=0.158 | DD=11.24% | Turnover=35.16%
   🎚️ Intra-Step TAPE: potential=0.5197 | delta_reward=+0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0326 | critic_loss=0.0029 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0014 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.55 | std=0.25 | range=[0.41, 2.90] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.59 | GLD=1.58 | PG=1.57  BOT: CAT=1.47 | AMZN=1.46 | NVDA=1.34
   🧭 Regime Start Dist (train resets): high_vol=110 (39.9%), low_vol=81 (29.3%), medium_vol=85 (30.8%)
   [WARN]  WARNING: Alpha std < 0.25 after 212 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0770 | penalty=-0.0009 | rolling_cvar=-0.02077

📚 EPISODE HORIZON UPDATE at 246,960 steps:
   Episode horizon: 1350 steps
[CYCLE] Update 213/348 | Step 246,960/500,000 | Episode 272 | Time: 30381.7s
   📊 Metrics: Return=+2.59% | Sharpe=-0.048 | DD=11.24% | Turnover=35.43%
   🎚️ Intra-Step TAPE: potential=0.2336 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0421 | critic_loss=0.0029 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0014 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0905 | penalty=-0.0027 | rolling_cvar=-0.03807

📚 EPISODE HORIZON UPDATE at 248,472 steps:
   Episode horizon: 1425 steps
[CYCLE] Update 214/348 | Step 248,472/500,000 | Episode 272 | Time: 30446.4s
   📊 Metrics: Return=+7.93% | Sharpe=0.026 | DD=19.53% | Turnover=35.95%
   🎚️ Intra-Step TAPE: potential=0.7227 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0343 | critic_loss=0.0028 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0014 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.38 | std=0.29 | range=[0.40, 3.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.39 | JNJ=1.38 | NEE=1.36  BOT: CAT=1.27 | JPM=1.26 | NVDA=1.20
   🧭 Regime Start Dist (train resets): high_vol=110 (39.9%), low_vol=81 (29.3%), medium_vol=85 (30.8%)
   🔐 Lagrangian CVaR: λ=0.1139 | penalty=-0.0032 | rolling_cvar=-0.03370
      🧪 Deterministic validation: Sharpe=0.851 | Return=+88.69% | DD=24.51%
         Multi-horizon: score=0.879 | details=252:0.938/24.5%, 504:1.153/24.5%, 756:0.694/24.5%, 1008:0.851/24.5%
         SPY relative: spy_return=+53.67% | outperformance=+35.02%

📚 EPISODE HORIZON UPDATE at 249,984 steps:
   Episode horizon: 1499 steps
[CYCLE] Update 215/348 | Step 249,984/500,000 | Episode 276 | Time: 30841.0s
   📊 Metrics: Return=+22.85% | Sharpe=0.185 | DD=46.67% | Turnover=35.86%
   🎚️ Intra-Step TAPE: potential=0.6292 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0371 | critic_loss=0.0063 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 14.00%) | terminal=4.999 (peak 5.000) | TAPE=0.2327
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.00549) | SPY bonus=0.011 (SPY ret=0.00297)
   🔐 Lagrangian CVaR: λ=0.1043 | penalty=-0.0019 | rolling_cvar=-0.01634

📚 EPISODE HORIZON UPDATE at 251,496 steps:
   Episode horizon: 1500 steps
[CYCLE] Update 216/348 | Step 251,496/500,000 | Episode 276 | Time: 30906.0s
   📊 Metrics: Return=-15.67% | Sharpe=-0.223 | DD=41.13% | Turnover=38.06%
   🎚️ Intra-Step TAPE: potential=0.3029 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0379 | critic_loss=0.0027 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0014 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.28 | std=0.16 | range=[0.41, 2.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.33 | JNJ=1.32 | NEE=1.30  BOT: CAT=1.21 | JPM=1.20 | NVDA=1.14
   🧭 Regime Start Dist (train resets): high_vol=111 (39.6%), low_vol=83 (29.6%), medium_vol=86 (30.7%)
   [WARN]  WARNING: Alpha std < 0.25 after 216 updates. TCN may not be learning asset discrimination.
   🔐 Lagrangian CVaR: λ=0.0756 | penalty=-0.0004 | rolling_cvar=-0.02754

🎯 ENTROPY COEF UPDATE at 251,496 steps:
   entropy_coef: 0.0015
[CYCLE] Update 217/348 | Step 253,008/500,000 | Episode 276 | Time: 30971.6s
   📊 Metrics: Return=+0.46% | Sharpe=0.037 | DD=41.13% | Turnover=37.86%
   🎚️ Intra-Step TAPE: potential=0.7276 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0184 | critic_loss=0.0035 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.1162 | penalty=-0.0043 | rolling_cvar=-0.03534
[CYCLE] Update 218/348 | Step 254,520/500,000 | Episode 276 | Time: 31036.0s
   📊 Metrics: Return=+11.44% | Sharpe=0.112 | DD=41.13% | Turnover=37.69%
   🎚️ Intra-Step TAPE: potential=0.7412 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0322 | critic_loss=0.0054 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0027 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0020
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.51 | std=0.30 | range=[1.00, 2.94] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.50 | PG=1.47 | JNJ=1.47  BOT: MSFT=1.42 | JPM=1.36 | NVDA=1.26
   🧭 Regime Start Dist (train resets): high_vol=111 (39.6%), low_vol=83 (29.6%), medium_vol=86 (30.7%)
   🔐 Lagrangian CVaR: λ=0.1430 | penalty=-0.0042 | rolling_cvar=-0.03284
      🧪 Deterministic validation: Sharpe=0.851 | Return=+90.54% | DD=25.02%
         Multi-horizon: score=0.874 | details=252:0.929/25.0%, 504:1.151/25.0%, 756:0.694/25.0%, 1008:0.851/25.0%
         SPY relative: spy_return=+53.67% | outperformance=+36.87%
[CYCLE] Update 219/348 | Step 256,032/500,000 | Episode 280 | Time: 31429.9s
   📊 Metrics: Return=-0.64% | Sharpe=0.005 | DD=43.81% | Turnover=37.41%
   🎚️ Intra-Step TAPE: potential=0.2285 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0350 | critic_loss=0.0047 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.730 (peak 1.159, dd 7.73% / trig 14.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2224
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01100) | SPY bonus=0.001 (SPY ret=-0.00950)
   🔐 Lagrangian CVaR: λ=0.1692 | penalty=-0.0062 | rolling_cvar=-0.05694
[CYCLE] Update 220/348 | Step 257,544/500,000 | Episode 280 | Time: 31495.0s
   📊 Metrics: Return=+2.82% | Sharpe=-0.024 | DD=10.59% | Turnover=34.54%
   🎚️ Intra-Step TAPE: potential=0.2273 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0314 | critic_loss=0.0030 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0015 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.53 | std=0.39 | range=[0.47, 3.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.56 | PG=1.51 | GLD=1.51  BOT: JPM=1.39 | CAT=1.36 | NVDA=1.29
   🧭 Regime Start Dist (train resets): high_vol=113 (39.8%), low_vol=85 (29.9%), medium_vol=86 (30.3%)
   🔐 Lagrangian CVaR: λ=0.2313 | penalty=-0.0134 | rolling_cvar=-0.04193
[CYCLE] Update 221/348 | Step 259,056/500,000 | Episode 280 | Time: 31559.8s
   📊 Metrics: Return=+5.82% | Sharpe=0.010 | DD=13.10% | Turnover=34.85%
   🎚️ Intra-Step TAPE: potential=0.7470 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0242 | critic_loss=0.0026 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0013 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.2739 | penalty=-0.0123 | rolling_cvar=-0.03623
[CYCLE] Update 222/348 | Step 260,568/500,000 | Episode 280 | Time: 31623.8s
   📊 Metrics: Return=+32.47% | Sharpe=0.368 | DD=13.10% | Turnover=34.71%
   🎚️ Intra-Step TAPE: potential=0.5969 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0303 | critic_loss=0.0040 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.66 | std=0.42 | range=[1.13, 3.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.62 | JNJ=1.58 | PG=1.58  BOT: GLD=1.51 | CAT=1.45 | NVDA=1.44
   🧭 Regime Start Dist (train resets): high_vol=113 (39.8%), low_vol=85 (29.9%), medium_vol=86 (30.3%)
   🔐 Lagrangian CVaR: λ=0.2981 | penalty=-0.0093 | rolling_cvar=-0.03234
[CYCLE] Update 223/348 | Step 262,080/500,000 | Episode 284 | Time: 31688.2s
   📊 Metrics: Return=+9.92% | Sharpe=0.080 | DD=37.60% | Turnover=35.58%
   🎚️ Intra-Step TAPE: potential=0.7433 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0272 | critic_loss=0.0133 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.013, dd 0.17% / trig 14.00%) | terminal=2.346 (peak 4.225) | TAPE=0.2243
   🔐 Lagrangian CVaR: λ=0.2895 | penalty=-0.0036 | rolling_cvar=-0.01434
[CYCLE] Update 224/348 | Step 263,592/500,000 | Episode 284 | Time: 31753.4s
   📊 Metrics: Return=-1.11% | Sharpe=-0.075 | DD=16.77% | Turnover=34.37%
   🎚️ Intra-Step TAPE: potential=0.2402 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0254 | critic_loss=0.0038 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0019 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.83 | std=0.41 | range=[0.47, 3.99] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.83 | MSFT=1.78 | XOM=1.77  BOT: JPM=1.74 | CAT=1.70 | NVDA=1.67
   🧭 Regime Start Dist (train resets): high_vol=113 (39.2%), low_vol=87 (30.2%), medium_vol=88 (30.6%)
   🔐 Lagrangian CVaR: λ=0.2736 | penalty=-0.0035 | rolling_cvar=-0.01357
[CYCLE] Update 225/348 | Step 265,104/500,000 | Episode 284 | Time: 31818.6s
   📊 Metrics: Return=+9.98% | Sharpe=0.106 | DD=16.77% | Turnover=33.57%
   🎚️ Intra-Step TAPE: potential=0.2491 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0336 | critic_loss=0.0016 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0008 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.2781 | penalty=-0.0065 | rolling_cvar=-0.01606
[CYCLE] Update 226/348 | Step 266,616/500,000 | Episode 284 | Time: 31884.2s
   📊 Metrics: Return=+10.19% | Sharpe=0.052 | DD=16.77% | Turnover=33.86%
   🎚️ Intra-Step TAPE: potential=0.2432 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0277 | critic_loss=0.0018 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0009 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.61 | std=0.39 | range=[1.09, 3.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.58 | MSFT=1.55 | JNJ=1.52  BOT: JPM=1.47 | NVDA=1.46 | GLD=1.45
   🧭 Regime Start Dist (train resets): high_vol=113 (39.2%), low_vol=87 (30.2%), medium_vol=88 (30.6%)
   🔐 Lagrangian CVaR: λ=0.2828 | penalty=-0.0063 | rolling_cvar=-0.01508
      🧪 Deterministic validation: Sharpe=0.850 | Return=+90.89% | DD=24.87%
         Multi-horizon: score=0.873 | details=252:0.929/24.9%, 504:1.150/24.9%, 756:0.686/24.9%, 1008:0.850/24.9%
         SPY relative: spy_return=+53.67% | outperformance=+37.22%
[CYCLE] Update 227/348 | Step 268,128/500,000 | Episode 288 | Time: 32277.2s
   📊 Metrics: Return=+52.04% | Sharpe=0.521 | DD=12.06% | Turnover=33.26%
   🎚️ Intra-Step TAPE: potential=0.2421 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0362 | critic_loss=0.0108 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 10.18% / trig 14.00%) | terminal=0.000 (peak 0.938) | TAPE=0.3068
   🔐 Lagrangian CVaR: λ=0.2678 | penalty=-0.0036 | rolling_cvar=-0.01138
[CYCLE] Update 228/348 | Step 269,640/500,000 | Episode 288 | Time: 32342.6s
   📊 Metrics: Return=-1.26% | Sharpe=0.066 | DD=41.65% | Turnover=36.99%
   🎚️ Intra-Step TAPE: potential=0.6563 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0308 | critic_loss=0.0023 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0011 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.46 | std=0.28 | range=[0.41, 3.03] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.49 | MSFT=1.44 | JPM=1.42  BOT: PG=1.38 | GLD=1.38 | CAT=1.34
   🧭 Regime Start Dist (train resets): high_vol=114 (39.0%), low_vol=87 (29.8%), medium_vol=91 (31.2%)
   🔐 Lagrangian CVaR: λ=0.2520 | penalty=-0.0031 | rolling_cvar=-0.01647
[CYCLE] Update 229/348 | Step 271,152/500,000 | Episode 288 | Time: 32407.5s
   📊 Metrics: Return=+23.64% | Sharpe=0.265 | DD=41.65% | Turnover=36.20%
   🎚️ Intra-Step TAPE: potential=0.7494 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0285 | critic_loss=0.0014 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0007 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.2589 | penalty=-0.0067 | rolling_cvar=-0.01503
[CYCLE] Update 230/348 | Step 272,664/500,000 | Episode 288 | Time: 32472.7s
   📊 Metrics: Return=+5.79% | Sharpe=0.075 | DD=41.65% | Turnover=36.00%
   🎚️ Intra-Step TAPE: potential=0.2395 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0294 | critic_loss=0.0024 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0012 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.45 | std=0.37 | range=[1.06, 3.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.45 | MSFT=1.38 | NVDA=1.36  BOT: XOM=1.31 | PG=1.31 | NEE=1.31
   🧭 Regime Start Dist (train resets): high_vol=114 (39.0%), low_vol=87 (29.8%), medium_vol=91 (31.2%)
   🔐 Lagrangian CVaR: λ=0.2664 | penalty=-0.0066 | rolling_cvar=-0.01814
      🧪 Deterministic validation: Sharpe=0.852 | Return=+89.22% | DD=24.24%
         Multi-horizon: score=0.883 | details=252:0.944/24.2%, 504:1.159/24.2%, 756:0.689/24.2%, 1008:0.852/24.2%
         SPY relative: spy_return=+53.67% | outperformance=+35.54%
[CYCLE] Update 231/348 | Step 274,176/500,000 | Episode 292 | Time: 32865.4s
   📊 Metrics: Return=+67.86% | Sharpe=0.630 | DD=19.15% | Turnover=35.60%
   🎚️ Intra-Step TAPE: potential=0.2284 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0309 | critic_loss=0.0103 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0051 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.630 (peak 1.230, dd 17.01% / trig 14.00%) | terminal=0.000 (peak 0.020) | TAPE=0.3303
   🔐 Lagrangian CVaR: λ=0.2533 | penalty=-0.0024 | rolling_cvar=-0.01257
[CYCLE] Update 232/348 | Step 275,688/500,000 | Episode 292 | Time: 32930.0s
   📊 Metrics: Return=-6.28% | Sharpe=-0.224 | DD=17.84% | Turnover=37.51%
   🎚️ Intra-Step TAPE: potential=0.2403 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0281 | critic_loss=0.0092 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.41 | std=0.44 | range=[1.04, 3.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.34 | CAT=1.34 | GLD=1.32  BOT: MSFT=1.25 | JPM=1.25 | NVDA=1.24
   🧭 Regime Start Dist (train resets): high_vol=117 (39.5%), low_vol=87 (29.4%), medium_vol=92 (31.1%)
   🔐 Lagrangian CVaR: λ=0.2260 | penalty=-0.0000 | rolling_cvar=-0.01525
[CYCLE] Update 233/348 | Step 277,200/500,000 | Episode 292 | Time: 32994.8s
   📊 Metrics: Return=-0.31% | Sharpe=-0.081 | DD=17.84% | Turnover=36.99%
   🎚️ Intra-Step TAPE: potential=0.2226 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0296 | critic_loss=0.0034 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.2045 | penalty=-0.0000 | rolling_cvar=-0.01929
[CYCLE] Update 234/348 | Step 278,712/500,000 | Episode 292 | Time: 33059.5s
   📊 Metrics: Return=+4.91% | Sharpe=-0.023 | DD=17.84% | Turnover=35.81%
   🎚️ Intra-Step TAPE: potential=0.2365 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0291 | critic_loss=0.0021 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0010 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.00 | std=0.57 | range=[0.41, 4.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.04 | MSFT=1.96 | JPM=1.90  BOT: NEE=1.79 | XOM=1.78 | GLD=1.78
   🧭 Regime Start Dist (train resets): high_vol=117 (39.5%), low_vol=87 (29.4%), medium_vol=92 (31.1%)
   🔐 Lagrangian CVaR: λ=0.1939 | penalty=-0.0016 | rolling_cvar=-0.03181
      🧪 Deterministic validation: Sharpe=0.866 | Return=+95.01% | DD=25.01%
         Multi-horizon: score=0.883 | details=252:0.937/25.0%, 504:1.169/25.0%, 756:0.687/25.0%, 1008:0.866/25.0%
         SPY relative: spy_return=+53.67% | outperformance=+41.34%
[CYCLE] Update 235/348 | Step 280,224/500,000 | Episode 296 | Time: 33451.7s
   📊 Metrics: Return=+32.21% | Sharpe=0.235 | DD=43.09% | Turnover=35.37%
   🎚️ Intra-Step TAPE: potential=0.6013 | delta_reward=+0.0025
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0262 | critic_loss=0.0049 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.005, dd 8.21% / trig 14.00%) | terminal=3.044 (peak 3.222) | TAPE=0.2342
   📈 Outperformance: 1/N bonus=0.000 (EW ret=0.01839) | SPY bonus=0.004 (SPY ret=0.01112)
   🔐 Lagrangian CVaR: λ=0.1662 | penalty=-0.0009 | rolling_cvar=-0.01630
[CYCLE] Update 236/348 | Step 281,736/500,000 | Episode 296 | Time: 33516.2s
   📊 Metrics: Return=+9.04% | Sharpe=0.179 | DD=16.86% | Turnover=32.52%
   🎚️ Intra-Step TAPE: potential=0.2938 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0321 | critic_loss=0.0025 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0013 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.00 | std=0.37 | range=[0.47, 3.86] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.12 | JPM=2.00 | NVDA=1.98  BOT: CAT=1.87 | PG=1.85 | JNJ=1.83
   🧭 Regime Start Dist (train resets): high_vol=117 (39.0%), low_vol=87 (29.0%), medium_vol=96 (32.0%)
   🔐 Lagrangian CVaR: λ=0.1540 | penalty=-0.0010 | rolling_cvar=-0.02054
[CYCLE] Update 237/348 | Step 283,248/500,000 | Episode 296 | Time: 33580.7s
   📊 Metrics: Return=+21.07% | Sharpe=0.288 | DD=16.86% | Turnover=31.64%
   🎚️ Intra-Step TAPE: potential=0.2452 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0263 | critic_loss=0.0023 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0012 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.1673 | penalty=-0.0040 | rolling_cvar=-0.03701
[CYCLE] Update 238/348 | Step 284,760/500,000 | Episode 296 | Time: 33645.7s
   📊 Metrics: Return=+29.58% | Sharpe=0.279 | DD=16.86% | Turnover=31.90%
   🎚️ Intra-Step TAPE: potential=0.7513 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0347 | critic_loss=0.0024 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0012 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0019
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=2.01 | std=0.42 | range=[1.55, 4.28] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.11 | NVDA=1.99 | MSFT=1.93  BOT: JNJ=1.81 | NEE=1.80 | PG=1.78
   🧭 Regime Start Dist (train resets): high_vol=117 (39.0%), low_vol=87 (29.0%), medium_vol=96 (32.0%)
   🔐 Lagrangian CVaR: λ=0.1774 | penalty=-0.0040 | rolling_cvar=-0.03319
      🧪 Deterministic validation: Sharpe=0.856 | Return=+92.96% | DD=24.83%
         Multi-horizon: score=0.876 | details=252:0.930/24.8%, 504:1.162/24.8%, 756:0.678/24.8%, 1008:0.856/24.8%
         SPY relative: spy_return=+53.67% | outperformance=+39.29%
[CYCLE] Update 239/348 | Step 286,272/500,000 | Episode 300 | Time: 34039.6s
   📊 Metrics: Return=+15.51% | Sharpe=0.129 | DD=44.32% | Turnover=32.23%
   🎚️ Intra-Step TAPE: potential=0.7110 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0295 | critic_loss=0.0049 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.60% / trig 14.00%) | terminal=4.780 (peak 5.000) | TAPE=0.2263
   🔐 Lagrangian CVaR: λ=0.1814 | penalty=-0.0050 | rolling_cvar=-0.01618
[CYCLE] Update 240/348 | Step 287,784/500,000 | Episode 300 | Time: 34104.5s
   📊 Metrics: Return=-1.39% | Sharpe=0.016 | DD=37.91% | Turnover=32.54%
   🎚️ Intra-Step TAPE: potential=0.2242 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0323 | critic_loss=0.0035 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.78 | std=0.59 | range=[0.91, 4.87] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.80 | NVDA=1.73 | JPM=1.64  BOT: NEE=1.55 | PG=1.51 | JNJ=1.49
   🧭 Regime Start Dist (train resets): high_vol=120 (39.5%), low_vol=88 (28.9%), medium_vol=96 (31.6%)
   🔐 Lagrangian CVaR: λ=0.1936 | penalty=-0.0054 | rolling_cvar=-0.01816
[CYCLE] Update 241/348 | Step 289,296/500,000 | Episode 300 | Time: 34168.8s
   📊 Metrics: Return=+4.51% | Sharpe=0.082 | DD=41.88% | Turnover=32.98%
   🎚️ Intra-Step TAPE: potential=0.2255 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0339 | critic_loss=0.0017 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0009 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.2333 | penalty=-0.0082 | rolling_cvar=-0.03556
[CYCLE] Update 242/348 | Step 290,808/500,000 | Episode 300 | Time: 34233.4s
   📊 Metrics: Return=+26.78% | Sharpe=0.216 | DD=41.88% | Turnover=32.77%
   🎚️ Intra-Step TAPE: potential=0.5171 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0307 | critic_loss=0.0023 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0011 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.92 | std=0.61 | range=[1.41, 4.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.98 | NVDA=1.86 | CAT=1.80  BOT: JNJ=1.64 | PG=1.62 | NEE=1.61
   🧭 Regime Start Dist (train resets): high_vol=120 (39.5%), low_vol=88 (28.9%), medium_vol=96 (31.6%)
   🔐 Lagrangian CVaR: λ=0.2663 | penalty=-0.0083 | rolling_cvar=-0.03220
[CYCLE] Update 243/348 | Step 292,320/500,000 | Episode 304 | Time: 34298.1s
   📊 Metrics: Return=+46.70% | Sharpe=0.319 | DD=41.35% | Turnover=32.64%
   🎚️ Intra-Step TAPE: potential=0.7447 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0271 | critic_loss=0.0115 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.246 (peak 0.803, dd 0.00% / trig 14.00%) | terminal=2.142 (peak 2.930) | TAPE=0.2463
   🔐 Lagrangian CVaR: λ=0.2330 | penalty=-0.0020 | rolling_cvar=-0.01316
[CYCLE] Update 244/348 | Step 293,832/500,000 | Episode 304 | Time: 34363.7s
   📊 Metrics: Return=+2.08% | Sharpe=0.005 | DD=16.21% | Turnover=32.56%
   🎚️ Intra-Step TAPE: potential=0.2387 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0335 | critic_loss=0.0092 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.83 | std=0.44 | range=[1.32, 4.02] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.91 | NVDA=1.87 | CAT=1.73  BOT: NEE=1.61 | JNJ=1.59 | PG=1.59
   🧭 Regime Start Dist (train resets): high_vol=121 (39.3%), low_vol=89 (28.9%), medium_vol=98 (31.8%)
   🔐 Lagrangian CVaR: λ=0.1813 | penalty=-0.0000 | rolling_cvar=-0.01497
[CYCLE] Update 245/348 | Step 295,344/500,000 | Episode 304 | Time: 34428.7s
   📊 Metrics: Return=+15.81% | Sharpe=0.187 | DD=16.21% | Turnover=32.97%
   🎚️ Intra-Step TAPE: potential=0.7199 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0315 | critic_loss=0.0027 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0014 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.1522 | penalty=-0.0005 | rolling_cvar=-0.03126
[CYCLE] Update 246/348 | Step 296,856/500,000 | Episode 304 | Time: 34493.5s
   📊 Metrics: Return=+8.69% | Sharpe=0.028 | DD=16.21% | Turnover=33.59%
   🎚️ Intra-Step TAPE: potential=0.3725 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0209 | critic_loss=0.0028 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0014 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.69 | std=0.52 | range=[1.18, 4.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.69 | NVDA=1.67 | JPM=1.66  BOT: XOM=1.46 | PG=1.44 | GLD=1.43
   🧭 Regime Start Dist (train resets): high_vol=121 (39.3%), low_vol=89 (28.9%), medium_vol=98 (31.8%)
   🔐 Lagrangian CVaR: λ=0.1547 | penalty=-0.0029 | rolling_cvar=-0.03185
      🧪 Deterministic validation: Sharpe=0.844 | Return=+88.66% | DD=23.96%
         Multi-horizon: score=0.874 | details=252:0.933/24.0%, 504:1.157/24.0%, 756:0.669/24.0%, 1008:0.844/24.0%
         SPY relative: spy_return=+53.67% | outperformance=+34.98%
[CYCLE] Update 247/348 | Step 298,368/500,000 | Episode 308 | Time: 34884.0s
   📊 Metrics: Return=+36.17% | Sharpe=0.258 | DD=45.85% | Turnover=33.35%
   🎚️ Intra-Step TAPE: potential=0.5576 | delta_reward=+0.0026
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0333 | critic_loss=0.0041 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0021 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.44% / trig 14.00%) | terminal=4.993 (peak 5.000) | TAPE=0.2388
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00448) | SPY bonus=0.008 (SPY ret=-0.00718)
   🔐 Lagrangian CVaR: λ=0.1489 | penalty=-0.0033 | rolling_cvar=-0.02843
[CYCLE] Update 248/348 | Step 299,880/500,000 | Episode 308 | Time: 34948.5s
   📊 Metrics: Return=+17.54% | Sharpe=0.480 | DD=8.76% | Turnover=34.94%
   🎚️ Intra-Step TAPE: potential=0.5446 | delta_reward=+0.0027
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0308 | critic_loss=0.0033 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.65 | std=0.55 | range=[1.16, 4.35] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.60 | JPM=1.55 | MSFT=1.54  BOT: CAT=1.45 | XOM=1.45 | GLD=1.39
   🧭 Regime Start Dist (train resets): high_vol=122 (39.1%), low_vol=91 (29.2%), medium_vol=99 (31.7%)
   🔐 Lagrangian CVaR: λ=0.1502 | penalty=-0.0046 | rolling_cvar=-0.02272

📚 TURNOVER CURRICULUM UPDATE at 301,392 steps:
   Turnover penalty scalar: 1.0
[CYCLE] Update 249/348 | Step 301,392/500,000 | Episode 308 | Time: 35013.6s
   📊 Metrics: Return=+28.45% | Sharpe=0.428 | DD=14.86% | Turnover=34.94%
   🎚️ Intra-Step TAPE: potential=0.6106 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0307 | critic_loss=0.0083 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0042 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.1365 | penalty=-0.0026 | rolling_cvar=-0.01981

📚 PPO ROLLOUT UPDATE at 301,392 steps:
   Timesteps per update: 2016

📚 PPO BATCH SIZE UPDATE at 301,392 steps:
   Batch size: 504

🌡️ TEMPERATURE UPDATE at 301,392 steps:
   temperature: 0.9000
      🧪 Deterministic validation: Sharpe=0.829 | Return=+84.58% | DD=23.75%
         Multi-horizon: score=0.862 | details=252:0.921/23.7%, 504:1.134/23.7%, 756:0.670/23.7%, 1008:0.829/23.7%
         SPY relative: spy_return=+53.67% | outperformance=+30.91%
[CYCLE] Update 250/348 | Step 303,408/500,000 | Episode 312 | Time: 35429.2s
   📊 Metrics: Return=+20.40% | Sharpe=0.154 | DD=20.53% | Turnover=34.11%
   🎚️ Intra-Step TAPE: potential=0.2996 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0312 | critic_loss=0.0272 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0136 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.67 | std=0.66 | range=[0.96, 6.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.58 | MSFT=1.57 | JPM=1.52  BOT: XOM=1.43 | CAT=1.42 | GLD=1.38
   🧭 Regime Start Dist (train resets): high_vol=122 (38.6%), low_vol=93 (29.4%), medium_vol=101 (32.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.18% / trig 14.00%) | terminal=0.222 (peak 1.997) | TAPE=0.2393
   🔐 Lagrangian CVaR: λ=0.1064 | penalty=-0.0015 | rolling_cvar=-0.01147
[CYCLE] Update 251/348 | Step 305,424/500,000 | Episode 312 | Time: 35508.7s
   📊 Metrics: Return=-4.51% | Sharpe=-0.220 | DD=15.72% | Turnover=35.71%
   🎚️ Intra-Step TAPE: potential=0.5661 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0315 | critic_loss=0.0057 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0375 | penalty=-0.0000 | rolling_cvar=-0.01316
[CYCLE] Update 252/348 | Step 307,440/500,000 | Episode 312 | Time: 35587.1s
   📊 Metrics: Return=-2.68% | Sharpe=-0.155 | DD=15.72% | Turnover=34.88%
   🎚️ Intra-Step TAPE: potential=0.2417 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0277 | critic_loss=0.0049 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.69 | std=0.38 | range=[1.04, 3.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=1.72 | MSFT=1.64 | XOM=1.63  BOT: NVDA=1.59 | GLD=1.53 | CAT=1.52
   🧭 Regime Start Dist (train resets): high_vol=122 (38.6%), low_vol=93 (29.4%), medium_vol=101 (32.0%)
   🔐 Lagrangian CVaR: λ=0.0088 | penalty=-0.0002 | rolling_cvar=-0.02713
      🧪 Deterministic validation: Sharpe=0.817 | Return=+85.07% | DD=24.76%
         Multi-horizon: score=0.841 | details=252:0.895/24.8%, 504:1.112/24.8%, 756:0.666/24.8%, 1008:0.817/24.8%
         SPY relative: spy_return=+53.67% | outperformance=+31.40%
[CYCLE] Update 253/348 | Step 309,456/500,000 | Episode 316 | Time: 35990.4s
   📊 Metrics: Return=+11.93% | Sharpe=0.098 | DD=46.35% | Turnover=34.11%
   🎚️ Intra-Step TAPE: potential=0.7535 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0325 | critic_loss=0.0073 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0037 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.25% / trig 14.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2272
   🔐 Lagrangian CVaR: λ=0.0303 | penalty=-0.0005 | rolling_cvar=-0.02182
[CYCLE] Update 254/348 | Step 311,472/500,000 | Episode 316 | Time: 36070.0s
   📊 Metrics: Return=+41.24% | Sharpe=1.146 | DD=10.35% | Turnover=34.02%
   🎚️ Intra-Step TAPE: potential=0.3209 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0335 | critic_loss=0.0041 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.73 | std=0.34 | range=[0.72, 4.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.79 | XOM=1.77 | PG=1.76  BOT: AMZN=1.60 | CAT=1.55 | NVDA=1.40
   🧭 Regime Start Dist (train resets): high_vol=124 (38.8%), low_vol=93 (29.1%), medium_vol=103 (32.2%)
   🔐 Lagrangian CVaR: λ=0.0265 | penalty=-0.0008 | rolling_cvar=-0.04476
[CYCLE] Update 255/348 | Step 313,488/500,000 | Episode 316 | Time: 36149.4s
   📊 Metrics: Return=+20.60% | Sharpe=0.222 | DD=41.40% | Turnover=33.80%
   🎚️ Intra-Step TAPE: potential=0.2457 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0298 | critic_loss=0.0019 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0010 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0116 | penalty=-0.0004 | rolling_cvar=-0.03587
      🧪 Deterministic validation: Sharpe=0.808 | Return=+82.83% | DD=24.92%
         Multi-horizon: score=0.834 | details=252:0.887/24.9%, 504:1.101/24.9%, 756:0.670/24.9%, 1008:0.808/24.9%
         SPY relative: spy_return=+53.67% | outperformance=+29.16%
[CYCLE] Update 256/348 | Step 315,504/500,000 | Episode 320 | Time: 36560.6s
   📊 Metrics: Return=+15.38% | Sharpe=0.123 | DD=36.43% | Turnover=33.74%
   🎚️ Intra-Step TAPE: potential=0.7474 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0303 | critic_loss=0.0051 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.71 | std=0.40 | range=[0.89, 3.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.74 | MSFT=1.72 | PG=1.69  BOT: CAT=1.45 | GLD=1.45 | NVDA=1.41
   🧭 Regime Start Dist (train resets): high_vol=127 (39.2%), low_vol=94 (29.0%), medium_vol=103 (31.8%)
   🔒 Drawdown λ snapshot=1.548 (peak 1.754, dd 1.24% / trig 14.00%) | terminal=0.674 (peak 3.247) | TAPE=0.2284
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.00959) | SPY bonus=0.000 (SPY ret=-0.00878)
   🔐 Lagrangian CVaR: λ=0.0125 | penalty=-0.0002 | rolling_cvar=-0.01851
[CYCLE] Update 257/348 | Step 317,520/500,000 | Episode 320 | Time: 36642.2s
   📊 Metrics: Return=+5.84% | Sharpe=0.113 | DD=17.52% | Turnover=34.25%
   🎚️ Intra-Step TAPE: potential=0.2554 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0317 | critic_loss=0.0020 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0010 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01401
[CYCLE] Update 258/348 | Step 319,536/500,000 | Episode 320 | Time: 36722.6s
   📊 Metrics: Return=+19.35% | Sharpe=0.230 | DD=17.52% | Turnover=34.82%
   🎚️ Intra-Step TAPE: potential=0.7100 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0286 | critic_loss=0.0024 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0012 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.46 | std=0.35 | range=[0.71, 3.13] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.50 | NEE=1.46 | MSFT=1.44  BOT: CAT=1.26 | NVDA=1.24 | GLD=1.22
   🧭 Regime Start Dist (train resets): high_vol=127 (39.2%), low_vol=94 (29.0%), medium_vol=103 (31.8%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01577
[CYCLE] Update 259/348 | Step 321,552/500,000 | Episode 324 | Time: 36804.0s
   📊 Metrics: Return=+60.23% | Sharpe=0.615 | DD=13.70% | Turnover=35.43%
   🎚️ Intra-Step TAPE: potential=0.2367 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0313 | critic_loss=0.0059 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 8.25% / trig 14.00%) | terminal=0.000 (peak 0.270) | TAPE=0.3505
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02196
[CYCLE] Update 260/348 | Step 323,568/500,000 | Episode 324 | Time: 36884.4s
   📊 Metrics: Return=-5.72% | Sharpe=-0.248 | DD=13.38% | Turnover=38.23%
   🎚️ Intra-Step TAPE: potential=0.2258 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0261 | critic_loss=0.0042 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0021 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.24 | std=0.34 | range=[0.66, 3.23] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.24 | PG=1.22 | XOM=1.20  BOT: AMZN=1.12 | CAT=1.09 | NVDA=1.06
   🧭 Regime Start Dist (train resets): high_vol=128 (39.0%), low_vol=96 (29.3%), medium_vol=104 (31.7%)
   🔐 Lagrangian CVaR: λ=0.0110 | penalty=-0.0000 | rolling_cvar=-0.04395
[CYCLE] Update 261/348 | Step 325,584/500,000 | Episode 324 | Time: 36965.3s
   📊 Metrics: Return=-6.39% | Sharpe=-0.220 | DD=13.56% | Turnover=38.33%
   🎚️ Intra-Step TAPE: potential=0.2401 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0304 | critic_loss=0.0033 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0488 | penalty=-0.0011 | rolling_cvar=-0.03500
      🧪 Deterministic validation: Sharpe=0.812 | Return=+80.43% | DD=23.83%
         Multi-horizon: score=0.842 | details=252:0.900/23.8%, 504:1.106/23.8%, 756:0.666/23.8%, 1008:0.812/23.8%
         SPY relative: spy_return=+53.67% | outperformance=+26.75%
[CYCLE] Update 262/348 | Step 327,600/500,000 | Episode 328 | Time: 37378.7s
   📊 Metrics: Return=-13.78% | Sharpe=-0.115 | DD=49.30% | Turnover=38.13%
   🎚️ Intra-Step TAPE: potential=0.4727 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0325 | critic_loss=0.0145 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0072 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0015
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.17 | std=0.46 | range=[0.74, 3.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.10 | NEE=1.09 | MSFT=1.09  BOT: CAT=0.96 | NVDA=0.95 | GLD=0.94
   🧭 Regime Start Dist (train resets): high_vol=128 (38.6%), low_vol=100 (30.1%), medium_vol=104 (31.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.27% / trig 14.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2136
   🔐 Lagrangian CVaR: λ=0.0497 | penalty=-0.0010 | rolling_cvar=-0.01138
[CYCLE] Update 263/348 | Step 329,616/500,000 | Episode 328 | Time: 37459.5s
   📊 Metrics: Return=-13.50% | Sharpe=-0.143 | DD=41.75% | Turnover=39.66%
   🎚️ Intra-Step TAPE: potential=0.6387 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0288 | critic_loss=0.0025 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0013 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0043 | penalty=-0.0000 | rolling_cvar=-0.01984
[CYCLE] Update 264/348 | Step 331,632/500,000 | Episode 328 | Time: 37542.1s
   📊 Metrics: Return=+9.26% | Sharpe=0.116 | DD=41.75% | Turnover=39.28%
   🎚️ Intra-Step TAPE: potential=0.2410 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0280 | critic_loss=0.0016 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0008 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.26 | std=0.70 | range=[0.62, 4.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=1.11 | JNJ=1.09 | AMZN=1.09  BOT: NVDA=1.03 | CAT=1.02 | GLD=0.98
   🧭 Regime Start Dist (train resets): high_vol=128 (38.6%), low_vol=100 (30.1%), medium_vol=104 (31.3%)
   🔐 Lagrangian CVaR: λ=0.0141 | penalty=-0.0002 | rolling_cvar=-0.03481
      🧪 Deterministic validation: Sharpe=0.824 | Return=+77.70% | DD=22.08%
         Multi-horizon: score=0.872 | details=252:0.943/22.1%, 504:1.130/22.1%, 756:0.672/22.1%, 1008:0.824/22.1%
         SPY relative: spy_return=+53.67% | outperformance=+24.02%
[CYCLE] Update 265/348 | Step 333,648/500,000 | Episode 332 | Time: 37964.6s
   📊 Metrics: Return=-13.45% | Sharpe=-0.111 | DD=45.63% | Turnover=38.61%
   🎚️ Intra-Step TAPE: potential=0.7488 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0295 | critic_loss=0.0100 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.776 (peak 1.104, dd 0.54% / trig 14.00%) | terminal=5.000 (peak 5.000) | TAPE=0.2159
   📈 Outperformance: 1/N bonus=0.000 (EW ret=-0.01462) | SPY bonus=0.027 (SPY ret=-0.01902)
   🔐 Lagrangian CVaR: λ=0.0016 | penalty=-0.0002 | rolling_cvar=-0.01416
[CYCLE] Update 266/348 | Step 335,664/500,000 | Episode 332 | Time: 38047.7s
   📊 Metrics: Return=+4.81% | Sharpe=0.064 | DD=15.22% | Turnover=36.96%
   🎚️ Intra-Step TAPE: potential=0.6680 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0317 | critic_loss=0.0096 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.37 | std=0.81 | range=[0.87, 5.27] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.17 | JNJ=1.16 | NEE=1.16  BOT: NVDA=1.07 | CAT=1.07 | GLD=1.04
   🧭 Regime Start Dist (train resets): high_vol=129 (38.4%), low_vol=101 (30.1%), medium_vol=106 (31.5%)
[CYCLE] Update 267/348 | Step 337,680/500,000 | Episode 332 | Time: 38130.7s
   📊 Metrics: Return=+6.03% | Sharpe=-0.001 | DD=15.22% | Turnover=36.20%
   🎚️ Intra-Step TAPE: potential=0.2331 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0296 | critic_loss=0.0178 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0089 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0009
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
      🧪 Deterministic validation: Sharpe=0.825 | Return=+79.41% | DD=22.60%
         Multi-horizon: score=0.866 | details=252:0.933/22.6%, 504:1.126/22.6%, 756:0.670/22.6%, 1008:0.825/22.6%
         SPY relative: spy_return=+53.67% | outperformance=+25.73%
[CYCLE] Update 268/348 | Step 339,696/500,000 | Episode 336 | Time: 38543.9s
   📊 Metrics: Return=+27.30% | Sharpe=0.241 | DD=14.14% | Turnover=36.21%
   🎚️ Intra-Step TAPE: potential=0.2428 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0298 | critic_loss=0.0178 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0089 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.38 | std=0.57 | range=[0.81, 4.11] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.26 | NEE=1.26 | JNJ=1.26  BOT: NVDA=1.17 | CAT=1.11 | GLD=1.10
   🧭 Regime Start Dist (train resets): high_vol=131 (38.5%), low_vol=101 (29.7%), medium_vol=108 (31.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.001, dd 8.82% / trig 14.00%) | terminal=0.000 (peak 2.000) | TAPE=0.2589
[CYCLE] Update 269/348 | Step 341,712/500,000 | Episode 336 | Time: 38625.1s
   📊 Metrics: Return=-4.58% | Sharpe=-0.238 | DD=14.64% | Turnover=36.47%
   🎚️ Intra-Step TAPE: potential=0.2237 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0320 | critic_loss=0.0022 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0011 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0014
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.04136
[CYCLE] Update 270/348 | Step 343,728/500,000 | Episode 336 | Time: 38707.9s
   📊 Metrics: Return=-8.45% | Sharpe=-0.285 | DD=14.64% | Turnover=36.67%
   🎚️ Intra-Step TAPE: potential=0.2379 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0322 | critic_loss=0.0021 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0011 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.22 | std=0.62 | range=[0.67, 4.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.12 | PG=1.09 | NEE=1.08  BOT: CAT=0.99 | NVDA=0.98 | GLD=0.96
   🧭 Regime Start Dist (train resets): high_vol=131 (38.5%), low_vol=101 (29.7%), medium_vol=108 (31.8%)
   🔐 Lagrangian CVaR: λ=0.0015 | penalty=-0.0000 | rolling_cvar=-0.03408
      🧪 Deterministic validation: Sharpe=0.804 | Return=+75.79% | DD=23.04%
         Multi-horizon: score=0.833 | details=252:0.888/23.0%, 504:1.091/23.0%, 756:0.658/23.0%, 1008:0.804/23.0%
         SPY relative: spy_return=+53.67% | outperformance=+22.12%
[CYCLE] Update 271/348 | Step 345,744/500,000 | Episode 340 | Time: 39131.8s
   📊 Metrics: Return=-4.89% | Sharpe=-0.033 | DD=37.28% | Turnover=37.88%
   🎚️ Intra-Step TAPE: potential=0.6061 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0305 | critic_loss=0.0056 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0028 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0012 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.70% / trig 14.00%) | terminal=1.078 (peak 2.142) | TAPE=0.2240
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01459
[CYCLE] Update 272/348 | Step 347,760/500,000 | Episode 340 | Time: 39213.7s
   📊 Metrics: Return=-4.20% | Sharpe=0.005 | DD=44.37% | Turnover=39.61%
   🎚️ Intra-Step TAPE: potential=0.7012 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0283 | critic_loss=0.0017 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0008 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.28 | std=0.58 | range=[0.74, 4.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.20 | PG=1.17 | XOM=1.16  BOT: GLD=1.06 | CAT=1.04 | NVDA=1.01
   🧭 Regime Start Dist (train resets): high_vol=133 (38.7%), low_vol=102 (29.7%), medium_vol=109 (31.7%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01245
[CYCLE] Update 273/348 | Step 349,776/500,000 | Episode 340 | Time: 39295.5s
   📊 Metrics: Return=-7.96% | Sharpe=-0.055 | DD=44.37% | Turnover=38.21%
   🎚️ Intra-Step TAPE: potential=0.2470 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0309 | critic_loss=0.0023 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0012 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01402
   [TOOL] Actor learning rate adjusted to 0.000010 at step 350,000
[CYCLE] Update 274/348 | Step 351,792/500,000 | Episode 344 | Time: 39377.8s
   📊 Metrics: Return=+49.19% | Sharpe=0.523 | DD=19.12% | Turnover=37.30%
   🎚️ Intra-Step TAPE: potential=0.5310 | delta_reward=+0.0023
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0281 | critic_loss=0.0108 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   🔬 Alpha Diversity: mean=1.46 | std=0.50 | range=[0.89, 3.97] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.38 | JNJ=1.37 | NEE=1.37  BOT: CAT=1.26 | NVDA=1.23 | GLD=1.19
   🧭 Regime Start Dist (train resets): high_vol=134 (38.5%), low_vol=104 (29.9%), medium_vol=110 (31.6%)
   🔒 Drawdown λ snapshot=1.582 (peak 2.000, dd 1.23% / trig 14.00%) | terminal=0.000 (peak 0.431) | TAPE=0.3051
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02098

[DOWN] PPO GAMMA UPDATE at 351,792 steps:
   gamma: 0.9980

[DOWN] PPO GAE-λ UPDATE at 351,792 steps:
   gae_lambda: 0.9700
[CYCLE] Update 275/348 | Step 353,808/500,000 | Episode 344 | Time: 39459.8s
   📊 Metrics: Return=-10.07% | Sharpe=-0.081 | DD=46.45% | Turnover=36.05%
   🎚️ Intra-Step TAPE: potential=0.6927 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0300 | critic_loss=0.0128 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0064 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.02282
[CYCLE] Update 276/348 | Step 355,824/500,000 | Episode 344 | Time: 39541.3s
   📊 Metrics: Return=-2.73% | Sharpe=-0.003 | DD=46.45% | Turnover=35.79%
   🎚️ Intra-Step TAPE: potential=0.2257 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0335 | critic_loss=0.0033 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.56 | std=0.48 | range=[0.76, 4.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.52 | JPM=1.50 | PG=1.48  BOT: GLD=1.41 | CAT=1.35 | NVDA=1.35
   🧭 Regime Start Dist (train resets): high_vol=134 (38.5%), low_vol=104 (29.9%), medium_vol=110 (31.6%)
   🔐 Lagrangian CVaR: λ=0.0317 | penalty=-0.0004 | rolling_cvar=-0.01979
      🧪 Deterministic validation: Sharpe=0.819 | Return=+83.24% | DD=24.55%
         Multi-horizon: score=0.835 | details=252:0.883/24.6%, 504:1.104/24.6%, 756:0.665/24.6%, 1008:0.819/24.6%
         SPY relative: spy_return=+53.67% | outperformance=+29.57%
[CYCLE] Update 277/348 | Step 357,840/500,000 | Episode 348 | Time: 39952.3s
   📊 Metrics: Return=+39.59% | Sharpe=0.353 | DD=15.00% | Turnover=35.52%
   🎚️ Intra-Step TAPE: potential=0.3556 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0302 | critic_loss=0.0123 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0062 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔒 Drawdown λ snapshot=1.541 (peak 2.000, dd 1.30% / trig 14.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2705
   🔐 Lagrangian CVaR: λ=0.0333 | penalty=-0.0010 | rolling_cvar=-0.01343
[CYCLE] Update 278/348 | Step 359,856/500,000 | Episode 348 | Time: 40032.4s
   📊 Metrics: Return=+24.97% | Sharpe=0.618 | DD=9.00% | Turnover=34.97%
   🎚️ Intra-Step TAPE: potential=0.5610 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0323 | critic_loss=0.0055 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0028 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.51 | std=0.44 | range=[1.00, 3.85] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.46 | XOM=1.45 | NEE=1.44  BOT: GLD=1.32 | AMZN=1.30 | NVDA=1.25
   🧭 Regime Start Dist (train resets): high_vol=135 (38.4%), low_vol=104 (29.5%), medium_vol=113 (32.1%)
[CYCLE] Update 279/348 | Step 361,872/500,000 | Episode 348 | Time: 40112.3s
   📊 Metrics: Return=-6.41% | Sharpe=-0.050 | DD=50.51% | Turnover=35.75%
   🎚️ Intra-Step TAPE: potential=0.4105 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0289 | critic_loss=0.0059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0030 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0010 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01767
      🧪 Deterministic validation: Sharpe=0.808 | Return=+81.10% | DD=24.58%
         Multi-horizon: score=0.824 | details=252:0.871/24.6%, 504:1.091/24.6%, 756:0.660/24.6%, 1008:0.808/24.6%
         SPY relative: spy_return=+53.67% | outperformance=+27.43%
[CYCLE] Update 280/348 | Step 363,888/500,000 | Episode 352 | Time: 40521.2s
   📊 Metrics: Return=+38.11% | Sharpe=0.345 | DD=17.74% | Turnover=36.57%
   🎚️ Intra-Step TAPE: potential=0.2181 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0282 | critic_loss=0.0079 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0016
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.34 | std=0.49 | range=[0.73, 6.01] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=1.38 | JNJ=1.30 | PG=1.30  BOT: AMZN=1.15 | CAT=1.14 | NVDA=1.03
   🧭 Regime Start Dist (train resets): high_vol=136 (38.2%), low_vol=105 (29.5%), medium_vol=115 (32.3%)
   🔒 Drawdown λ snapshot=1.605 (peak 2.000, dd 10.77% / trig 14.00%) | terminal=0.000 (peak 0.014) | TAPE=0.2661
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.01560
[CYCLE] Update 281/348 | Step 365,904/500,000 | Episode 352 | Time: 40602.4s
   📊 Metrics: Return=+11.63% | Sharpe=0.247 | DD=12.54% | Turnover=36.71%
   🎚️ Intra-Step TAPE: potential=0.2625 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0314 | critic_loss=0.0047 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=-0.0000 | rolling_cvar=-0.02001
[CYCLE] Update 282/348 | Step 367,920/500,000 | Episode 352 | Time: 40682.1s
   📊 Metrics: Return=+10.82% | Sharpe=0.084 | DD=25.16% | Turnover=36.81%
   🎚️ Intra-Step TAPE: potential=0.2199 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0273 | critic_loss=0.0026 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0013 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0011 | dispersion_loss=0.0017
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000150 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   🔬 Alpha Diversity: mean=1.39 | std=0.42 | range=[0.73, 3.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=1.37 | PG=1.34 | NEE=1.33  BOT: AMZN=1.21 | CAT=1.21 | NVDA=1.15
   🧭 Regime Start Dist (train resets): high_vol=136 (38.2%), low_vol=105 (29.5%), medium_vol=115 (32.3%)
   🔐 Lagrangian CVaR: λ=0.0086 | penalty=-0.0001 | rolling_cvar=-0.01762