[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 100000
num_parallel_envs: 8

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
   Train shape: (13840, 67)
   Test shape: (7115, 67)
   ℹ️ Actuarial features disabled by config.

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.35, band=±0.20, scalar=0.05 -> 0.10 => 0.20 => 0.30 => 0.40)
      ↳ Schedule: 0.05@0 => 0.10@20,000 => 0.20@40,000 => 0.30@60,000 => 0.40@80,000
   ⚙️  Component 4: Execution Inertia (beta=0.55 -> 0.70 => 0.85 => 1.00, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.55@0 => 0.70@20,000 => 0.85@40,000 => 1.00@60,000
   🧭 Reward Component Curriculum:
      0+ steps: A_return_only | base=True dsr=False turnover=False benchmark=False terminal=False
      30,000+ steps: B_add_risk | base=True dsr=True turnover=False benchmark=True terminal=False
      60,000+ steps: C_full_tape | base=True dsr=True turnover=True benchmark=True terminal=True
   ⚡ Parallel rollout envs: 8
      ↳ Vectorized rollout collection enabled
   🎁 Terminal: mode=signed, baseline=0.20, scalar=10.0 (clipped ±10.0)
   🟰 Neutral Band: enabled (±0.020 around baseline)
   🚦 Gate A: enabled (Sharpe <= 0.00, MDD >= 25.0%)
   [BRAIN] Credit Assignment: step reward is computed at each environment step
   [RCPT] Episode-End Handling: terminal TAPE bonus is added at episode completion only
   [OK] Retroactive episode-wide reward rescaling: disabled in notebook helper path
   🌊 DSR Regime Scaling: ENABLED | low=+0.80/-0.90 (vol<0.12) | mid=+1.00/-1.00 | high=+1.25/-1.25 (vol>0.25)
   📈 Benchmark Shaping (1/N): ENABLED | scalar=6.0 | mode=signed_clipped | clip=0.0200
   📈 Benchmark Shaping (SPY): ENABLED | scalar=1.5 | mode=signed_clipped | clip=0.0100
   🔐 Lagrangian CVaR: ENABLED | threshold=-0.025 | lr=0.004 | lambda_max=5.0 | penalty_scale=0.0
   Tail-Aware Advantage: ENABLED | weight=0.1 | bottom_k=4
   Alpha Regularization: hhi_coef=0.002 | dispersion_coef=0.1 | target_std=0.15
   Risk Aux: sharpe_coef=0.0 | mvo_coef=0.0 | cvar_coef=0.0
   🧪 Aux Per-Asset Return Head: ENABLED | coef=0.35
   🔒 Dirichlet Alpha Cap: 50.0
   🔒 Drawdown dual controller (requested): target=18.00%, tolerance=-1.50% (trigger boundary ≈ 16.50%), lr=0.100, λ_init=0.50, λ_floor=0.00, λ_max=5.00, penalty_coef=1.50
   📐 Position constraints: max_single_asset=25%, min_cash=5%
   [DEBUG] Regime-balanced sampling: use_curriculum_learning=True, volatility_regime pre-existing=False
   🎲 Volatility regimes ready for sampling (computed):
      high_vol: 909 dates (32.8%)
      low_vol: 909 dates (32.8%)
      medium_vol: 950 dates (34.3%)
   🧭 Regime start buckets (train env):
      high_vol: 909 dates (32.8%)
      low_vol: 909 dates (32.8%)
      medium_vol: 950 dates (34.3%)
   [OK] Drawdown controller armed in env: target=18.00%, trigger=16.50%, λ_init=0.500, λ_floor=0.000, λ_max=5.00, penalty_coef=1.50
[OK] THREE-COMPONENT TAPE v3 Environments created:
   Training: 2768 days
   Parallel train env instances: 8
   Testing: 1423 days

🤖 Creating TCN_FUSION agent with Dirichlet distribution for Exp 6...
[OK] Agent created: PPOAgentTF
   [RAND] Dirichlet Distribution: ENABLED
   [TOOL] Actor LR schedule: 0.000030@0 => 0.000020@30,000 => 0.000010@70,000
   [TOOL] Critic LR schedule: 0.000150@0 => 0.000120@30,000 => 0.000100@70,000
   State dim: 232
   Action dim: 5
   Actor LR (configured): 3e-05
   Actor LR (active): 0.000030
   Critic LR (active): 0.000150
   🧱 TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Cross-Asset Mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DNA] State augmentation: enabled=False
   [DOWN] Distributional critic: enabled=True | num_quantiles=17
   🎛️ Dirichlet controls: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Dual-head consistency coef: 0.0
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0015
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@30,000 => 0.9980@70,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@30,000 => 0.9700@70,000
   🎯 Entropy coef schedule: 0.0015@0 => 0.0015@20,000 => 0.0010@50,000 => 0.0005@80,000
   🧪 Aux-return coef schedule: 0.3500@0 => 0.3000@30,000 => 0.2500@60,000
   🌡️ Temperature schedule: 1.0000@0 => 0.9000@30,000 => 0.8000@60,000
   📐 PPO rollout schedule: 1008@0 => 1512@30,000 => 2016@60,000
   🧺 PPO batch-size schedule: 252@0 => 336@30,000 => 504@60,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_152902_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_152902_step_diagnostics.csv

🎯 Starting THREE-COMPONENT TAPE v3 training (with curriculum)...
   Total timesteps: 100,000
   Timesteps per update: scheduled
      0+ steps: timesteps_per_update=1008
      30,000+ steps: timesteps_per_update=1512
      60,000+ steps: timesteps_per_update=2016
   Number of updates: 70
   PPO batch_size: scheduled
      0+ steps: batch_size=252
      30,000+ steps: batch_size=336
      60,000+ steps: batch_size=504
   PPO gamma schedule: 0.9900@0 => 0.9950@30,000 => 0.9980@70,000
   PPO GAE-λ schedule: 0.9200@0 => 0.9500@30,000 => 0.9700@70,000
   📚 Episode Length Curriculum:
      0+ steps: limit=756
      20,000+ steps: limit=1008
      50,000+ steps: limit=1500
      80,000+ steps: limit=full
      ↳ smooth ramp: enabled (overlap=2,000 steps)
   📚 Turnover Scalar Curriculum:
      0+ steps: scalar=0.05
      20,000+ steps: scalar=0.10
      40,000+ steps: scalar=0.20
      60,000+ steps: scalar=0.30
      80,000+ steps: scalar=0.40
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.55
      20,000+ steps: beta=0.70
      40,000+ steps: beta=0.85
      60,000+ steps: beta=1.00
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.70, MDD <= 25.0%, skip_on_det_validation=True)
   ⏹️ Training early-stop: enabled (warmup=100,000 steps, patience=40 updates, min_delta=0.005, hard_dd=45.0% x 8)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_152902_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_152902_metadata.json
[CYCLE] Update 1/70 | Step 1,008/100,000 | Episode 0 | Time: 116.8s
   📊 Metrics: Return=-2.12% | Sharpe=-0.478 | DD=7.02% | Turnover=23.58%
   🎚️ Intra-Step TAPE: potential=0.2486 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0724 | critic_loss=0.2645 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1323 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0053
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4781 | ema=-0.4781 | best_ema=-0.4781 | no_improve=0
[CYCLE] Update 2/70 | Step 2,016/100,000 | Episode 0 | Time: 212.4s
   📊 Metrics: Return=-3.98% | Sharpe=-0.402 | DD=10.68% | Turnover=20.18%
   🎚️ Intra-Step TAPE: potential=0.2539 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0544 | critic_loss=0.3109 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1554 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0051
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4017 | ema=-0.4704 | best_ema=-0.4704 | no_improve=0
   🔬 Alpha Diversity: mean=1.77 | std=1.04 | range=[0.71, 4.93] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.06 | JPM=1.90 | XOM=1.66  BOT: XOM=1.66 | GLD=1.63 | MSFT=1.31
   🧬 FiLM: seq(dg=0.0001, db=0.0000, sat=0.0%) | latent(dg=0.0002, db=0.0001, sat=0.0%) | asset(dg=0.0002, db=0.0001, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=1 (12.5%), low_vol=6 (75.0%), medium_vol=1 (12.5%)
[CYCLE] Update 3/70 | Step 3,024/100,000 | Episode 0 | Time: 307.8s
   📊 Metrics: Return=+5.19% | Sharpe=0.167 | DD=12.10% | Turnover=19.46%
   🎚️ Intra-Step TAPE: potential=0.2450 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0461 | critic_loss=0.2821 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1410 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0054
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1669 | ema=-0.4067 | best_ema=-0.4067 | no_improve=0
[CYCLE] Update 4/70 | Step 4,032/100,000 | Episode 0 | Time: 403.3s
   📊 Metrics: Return=+32.69% | Sharpe=0.896 | DD=12.10% | Turnover=19.47%
   🎚️ Intra-Step TAPE: potential=0.7124 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0424 | critic_loss=0.2226 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1113 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0059
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8961 | ema=-0.2764 | best_ema=-0.2764 | no_improve=0
   🔬 Alpha Diversity: mean=1.75 | std=0.81 | range=[0.70, 4.80] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.04 | JPM=2.07 | XOM=1.86  BOT: XOM=1.86 | MSFT=1.52 | GLD=1.29
   🧬 FiLM: seq(dg=0.0001, db=0.0001, sat=0.0%) | latent(dg=0.0008, db=0.0005, sat=0.0%) | asset(dg=0.0004, db=0.0002, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=1 (12.5%), low_vol=6 (75.0%), medium_vol=1 (12.5%)
[CYCLE] Update 5/70 | Step 5,040/100,000 | Episode 0 | Time: 498.6s
   📊 Metrics: Return=+58.54% | Sharpe=1.181 | DD=12.10% | Turnover=19.21%
   🎚️ Intra-Step TAPE: potential=0.5945 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0396 | critic_loss=0.2433 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1217 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0053
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1805 | ema=-0.1307 | best_ema=-0.1307 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5 (Sharpe=1.251, MDD=12.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5 (Sharpe=0.992, MDD=15.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5 (Sharpe=0.893, MDD=23.59%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5 (Sharpe=1.099, MDD=12.93%)
[CYCLE] Update 6/70 | Step 6,048/100,000 | Episode 8 | Time: 595.1s
   📊 Metrics: Return=+64.82% | Sharpe=1.099 | DD=12.93% | Turnover=20.71%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0338 | critic_loss=0.2292 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1146 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0048
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0993 | ema=-0.0077 | best_ema=-0.0077 | no_improve=0
   🔬 Alpha Diversity: mean=1.76 | std=1.21 | range=[0.71, 5.11] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.06 | JPM=1.81 | XOM=1.71  BOT: XOM=1.71 | MSFT=1.03 | GLD=1.00
   🧬 FiLM: seq(dg=0.0001, db=0.0001, sat=0.0%) | latent(dg=0.0015, db=0.0010, sat=0.0%) | asset(dg=0.0005, db=0.0003, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=5 (31.2%), low_vol=9 (56.2%), medium_vol=2 (12.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.500) | TAPE=0.5588
[CYCLE] Update 7/70 | Step 7,056/100,000 | Episode 8 | Time: 691.2s
   📊 Metrics: Return=+34.32% | Sharpe=3.645 | DD=3.79% | Turnover=20.90%
   🎚️ Intra-Step TAPE: potential=0.7563 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0376 | critic_loss=0.2250 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1125 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0050
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.6449 | ema=0.3575 | best_ema=0.3575 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=0.0000 | rolling_cvar=-0.04455
[CYCLE] Update 8/70 | Step 8,064/100,000 | Episode 8 | Time: 787.1s
   📊 Metrics: Return=+11.35% | Sharpe=0.603 | DD=18.98% | Turnover=20.59%
   🎚️ Intra-Step TAPE: potential=0.2225 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0298 | critic_loss=0.2387 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1193 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0051
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6031 | ema=0.3821 | best_ema=0.3821 | no_improve=0
   🔬 Alpha Diversity: mean=1.75 | std=1.01 | range=[0.70, 4.89] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.25 | JPM=2.12 | XOM=1.86  BOT: XOM=1.86 | MSFT=1.28 | GLD=1.27
   🧬 FiLM: seq(dg=0.0002, db=0.0001, sat=0.0%) | latent(dg=0.0023, db=0.0015, sat=0.0%) | asset(dg=0.0006, db=0.0004, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=5 (31.2%), low_vol=9 (56.2%), medium_vol=2 (12.5%)
   🔐 Lagrangian CVaR: λ=0.0001 | penalty=0.0000 | rolling_cvar=-0.03929
[CYCLE] Update 9/70 | Step 9,072/100,000 | Episode 8 | Time: 882.5s
   📊 Metrics: Return=+19.33% | Sharpe=0.559 | DD=27.97% | Turnover=20.35%
   🎚️ Intra-Step TAPE: potential=0.3724 | delta_reward=-0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0278 | critic_loss=0.2376 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1188 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0058
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4880 | ema=0.3927 | best_ema=0.3927 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.03736
[CYCLE] Update 10/70 | Step 10,080/100,000 | Episode 8 | Time: 977.7s
   📊 Metrics: Return=+14.59% | Sharpe=0.339 | DD=27.97% | Turnover=20.39%
   🎚️ Intra-Step TAPE: potential=0.3294 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0321 | critic_loss=0.2119 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0066
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2673 | ema=0.3801 | best_ema=0.3801 | no_improve=0
   🔬 Alpha Diversity: mean=1.73 | std=0.63 | range=[0.69, 3.38] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.44 | JPM=2.09 | XOM=1.99  BOT: XOM=1.99 | MSFT=1.73 | GLD=1.42
   🧬 FiLM: seq(dg=0.0002, db=0.0001, sat=0.0%) | latent(dg=0.0035, db=0.0022, sat=0.0%) | asset(dg=0.0007, db=0.0005, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=5 (31.2%), low_vol=9 (56.2%), medium_vol=2 (12.5%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.03423
[CYCLE] Update 11/70 | Step 11,088/100,000 | Episode 8 | Time: 1073.0s
   📊 Metrics: Return=+15.26% | Sharpe=0.289 | DD=27.97% | Turnover=20.21%
   🎚️ Intra-Step TAPE: potential=0.3623 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0251 | critic_loss=0.1768 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0884 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0072
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2178 | ema=0.3639 | best_ema=0.3639 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.03309
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5 (Sharpe=1.264, MDD=24.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5 (Sharpe=0.871, MDD=12.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5 (Sharpe=1.094, MDD=22.98%)
[CYCLE] Update 12/70 | Step 12,096/100,000 | Episode 16 | Time: 1168.3s
   📊 Metrics: Return=+40.86% | Sharpe=0.518 | DD=25.98% | Turnover=20.47%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0230 | critic_loss=0.1609 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0804 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0072
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4944 | ema=0.3770 | best_ema=0.3770 | no_improve=0
   🔬 Alpha Diversity: mean=1.72 | std=0.60 | range=[0.69, 3.34] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=2.47 | JPM=2.01 | MSFT=1.87  BOT: MSFT=1.87 | NVDA=1.65 | GLD=1.63
   🧬 FiLM: seq(dg=0.0002, db=0.0001, sat=0.0%) | latent(dg=0.0046, db=0.0030, sat=0.0%) | asset(dg=0.0008, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=8 (33.3%), low_vol=10 (41.7%), medium_vol=6 (25.0%)
   🔒 Drawdown λ snapshot=0.407 (peak 0.407, dd 0.00% / trig 16.50%) | terminal=0.260 (peak 0.356) | TAPE=0.3004
   🔐 Lagrangian CVaR: λ=0.0014 | penalty=0.0000 | rolling_cvar=-0.03425
[CYCLE] Update 13/70 | Step 13,104/100,000 | Episode 16 | Time: 1264.0s
   📊 Metrics: Return=-6.59% | Sharpe=-0.689 | DD=16.00% | Turnover=20.48%
   🎚️ Intra-Step TAPE: potential=0.2634 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0279 | critic_loss=0.1203 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0601 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0061
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.6886 | ema=0.2704 | best_ema=0.2704 | no_improve=0
[CYCLE] Update 14/70 | Step 14,112/100,000 | Episode 16 | Time: 1360.6s
   📊 Metrics: Return=+1.61% | Sharpe=0.089 | DD=19.64% | Turnover=20.06%
   🎚️ Intra-Step TAPE: potential=0.7517 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0228 | critic_loss=0.0939 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0469 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0056
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0893 | ema=0.2523 | best_ema=0.2523 | no_improve=0
   🔬 Alpha Diversity: mean=1.74 | std=0.78 | range=[0.68, 4.07] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=2.68 | JPM=2.07 | MSFT=1.89  BOT: MSFT=1.89 | GLD=1.67 | NVDA=1.40
   🧬 FiLM: seq(dg=0.0002, db=0.0002, sat=0.0%) | latent(dg=0.0053, db=0.0035, sat=0.0%) | asset(dg=0.0008, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=8 (33.3%), low_vol=10 (41.7%), medium_vol=6 (25.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.03280
[CYCLE] Update 15/70 | Step 15,120/100,000 | Episode 16 | Time: 1456.6s
   📊 Metrics: Return=+0.81% | Sharpe=0.024 | DD=19.64% | Turnover=19.41%
   🎚️ Intra-Step TAPE: potential=0.7332 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0238 | critic_loss=0.0625 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0313 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0052
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0241 | ema=0.2295 | best_ema=0.2295 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.02954
[CYCLE] Update 16/70 | Step 16,128/100,000 | Episode 16 | Time: 1553.0s
   📊 Metrics: Return=-5.19% | Sharpe=-0.169 | DD=19.64% | Turnover=19.01%
   🎚️ Intra-Step TAPE: potential=0.4450 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0218 | critic_loss=0.0345 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0173 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0050
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1687 | ema=0.1896 | best_ema=0.1896 | no_improve=0
   🔬 Alpha Diversity: mean=1.75 | std=1.11 | range=[0.68, 4.91] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=3.08 | JPM=1.75 | MSFT=1.58  BOT: MSFT=1.58 | GLD=1.38 | NVDA=1.24
   🧬 FiLM: seq(dg=0.0002, db=0.0002, sat=0.0%) | latent(dg=0.0059, db=0.0039, sat=0.0%) | asset(dg=0.0009, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=8 (33.3%), low_vol=10 (41.7%), medium_vol=6 (25.0%)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.02737
[CYCLE] Update 17/70 | Step 17,136/100,000 | Episode 16 | Time: 1649.0s
   📊 Metrics: Return=-5.43% | Sharpe=-0.163 | DD=19.64% | Turnover=19.13%
   🎚️ Intra-Step TAPE: potential=0.2638 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0217 | critic_loss=0.0337 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0168 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0049
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1631 | ema=0.1544 | best_ema=0.1544 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.02630
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5 (Sharpe=0.932, MDD=20.95%)

📚 EPISODE HORIZON UPDATE at 18,144 steps:
   Episode horizon: 774 steps
[CYCLE] Update 18/70 | Step 18,144/100,000 | Episode 24 | Time: 1744.2s
   📊 Metrics: Return=+7.26% | Sharpe=0.104 | DD=23.95% | Turnover=18.71%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0214 | critic_loss=0.0576 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0288 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0054
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1042 | ema=0.1494 | best_ema=0.1494 | no_improve=0
   🔬 Alpha Diversity: mean=1.73 | std=0.83 | range=[0.68, 4.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=2.84 | JPM=1.86 | GLD=1.77  BOT: GLD=1.77 | MSFT=1.61 | NVDA=1.60
   🧬 FiLM: seq(dg=0.0003, db=0.0002, sat=0.0%) | latent(dg=0.0065, db=0.0043, sat=0.0%) | asset(dg=0.0009, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=11 (34.4%), medium_vol=11 (34.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.195) | TAPE=0.2382

📚 EPISODE HORIZON UPDATE at 19,152 steps:
   Episode horizon: 901 steps
[CYCLE] Update 19/70 | Step 19,152/100,000 | Episode 24 | Time: 1839.8s
   📊 Metrics: Return=+28.84% | Sharpe=1.378 | DD=20.28% | Turnover=18.74%
   🎚️ Intra-Step TAPE: potential=0.6660 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0182 | critic_loss=0.0626 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0313 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0055
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3783 | ema=0.2723 | best_ema=0.2723 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0025 | penalty=0.0000 | rolling_cvar=-0.01614

📚 TURNOVER CURRICULUM UPDATE at 20,160 steps:
   Turnover penalty scalar: 0.1

🎛️ EXECUTION BETA UPDATE at 20,160 steps:
   action_execution_beta: 0.700 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 20,160 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 20/70 | Step 20,160/100,000 | Episode 24 | Time: 1935.4s
   📊 Metrics: Return=+54.13% | Sharpe=1.461 | DD=20.28% | Turnover=19.49%
   🎚️ Intra-Step TAPE: potential=0.7080 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0212 | critic_loss=0.0247 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0124 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0060
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4611 | ema=0.3911 | best_ema=0.3911 | no_improve=0
   🔬 Alpha Diversity: mean=1.71 | std=0.73 | range=[0.67, 3.85] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=2.47 | JPM=2.13 | MSFT=1.80  BOT: MSFT=1.80 | GLD=1.64 | NVDA=1.57
   🧬 FiLM: seq(dg=0.0003, db=0.0002, sat=0.0%) | latent(dg=0.0071, db=0.0049, sat=0.0%) | asset(dg=0.0009, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=11 (34.4%), medium_vol=11 (34.4%)
   🔐 Lagrangian CVaR: λ=0.0040 | penalty=0.0000 | rolling_cvar=-0.01507
[CYCLE] Update 21/70 | Step 21,168/100,000 | Episode 24 | Time: 2030.8s
   📊 Metrics: Return=+32.40% | Sharpe=0.731 | DD=20.28% | Turnover=21.36%
   🎚️ Intra-Step TAPE: potential=0.2357 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0242 | critic_loss=0.0230 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0115 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0060
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7314 | ema=0.4252 | best_ema=0.4252 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0059 | penalty=0.0000 | rolling_cvar=-0.01564
[CYCLE] Update 22/70 | Step 22,176/100,000 | Episode 24 | Time: 2126.4s
   📊 Metrics: Return=+60.16% | Sharpe=0.972 | DD=20.28% | Turnover=22.43%
   🎚️ Intra-Step TAPE: potential=0.7537 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0235 | critic_loss=0.0130 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0065 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0062
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9718 | ema=0.4798 | best_ema=0.4798 | no_improve=0
   🔬 Alpha Diversity: mean=1.71 | std=0.70 | range=[0.67, 3.33] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=2.61 | MSFT=2.01 | JPM=1.90  BOT: JPM=1.90 | NVDA=1.54 | GLD=1.53
   🧬 FiLM: seq(dg=0.0003, db=0.0002, sat=0.0%) | latent(dg=0.0077, db=0.0052, sat=0.0%) | asset(dg=0.0010, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=11 (34.4%), medium_vol=11 (34.4%)
   🔐 Lagrangian CVaR: λ=0.0075 | penalty=0.0000 | rolling_cvar=-0.01767
[CYCLE] Update 23/70 | Step 23,184/100,000 | Episode 24 | Time: 2222.2s
   📊 Metrics: Return=+51.02% | Sharpe=0.732 | DD=20.28% | Turnover=22.91%
   🎚️ Intra-Step TAPE: potential=0.2323 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0209 | critic_loss=0.0156 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0078 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0004 | dispersion_loss=0.0058
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7318 | ema=0.5050 | best_ema=0.5050 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0063 | penalty=0.0000 | rolling_cvar=-0.01909
[CYCLE] Update 24/70 | Step 24,192/100,000 | Episode 24 | Time: 2318.8s
   📊 Metrics: Return=+48.99% | Sharpe=0.584 | DD=20.28% | Turnover=23.22%
   🎚️ Intra-Step TAPE: potential=0.2606 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0213 | critic_loss=0.0267 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0134 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0051
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5842 | ema=0.5129 | best_ema=0.5129 | no_improve=0
   🔬 Alpha Diversity: mean=1.73 | std=1.02 | range=[0.67, 4.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=3.40 | JPM=1.93 | MSFT=1.89  BOT: MSFT=1.89 | NVDA=1.24 | GLD=1.21
   🧬 FiLM: seq(dg=0.0003, db=0.0002, sat=0.0%) | latent(dg=0.0080, db=0.0053, sat=0.0%) | asset(dg=0.0010, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=11 (34.4%), medium_vol=11 (34.4%)
   🔐 Lagrangian CVaR: λ=0.0042 | penalty=0.0000 | rolling_cvar=-0.01903
[CYCLE] Update 25/70 | Step 25,200/100,000 | Episode 24 | Time: 2414.5s
   📊 Metrics: Return=+47.44% | Sharpe=0.507 | DD=20.28% | Turnover=23.11%
   🎚️ Intra-Step TAPE: potential=0.2479 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0202 | critic_loss=0.0202 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0101 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0048
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5072 | ema=0.5124 | best_ema=0.5124 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.01852
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5 (Sharpe=1.287, MDD=19.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5 (Sharpe=0.810, MDD=13.92%)
[CYCLE] Update 26/70 | Step 26,208/100,000 | Episode 32 | Time: 2510.1s
   📊 Metrics: Return=+59.79% | Sharpe=0.810 | DD=13.92% | Turnover=23.29%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0192 | critic_loss=0.0310 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0155 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0049
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8102 | ema=0.5422 | best_ema=0.5422 | no_improve=0
   🔬 Alpha Diversity: mean=1.74 | std=1.04 | range=[0.66, 4.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=3.02 | JPM=2.13 | MSFT=1.79  BOT: MSFT=1.79 | NVDA=1.15 | GLD=0.84
   🧬 FiLM: seq(dg=0.0003, db=0.0003, sat=0.0%) | latent(dg=0.0083, db=0.0054, sat=0.0%) | asset(dg=0.0010, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=12 (30.0%), low_vol=13 (32.5%), medium_vol=15 (37.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4473
[CYCLE] Update 27/70 | Step 27,216/100,000 | Episode 32 | Time: 2605.5s
   📊 Metrics: Return=-7.41% | Sharpe=-1.283 | DD=11.64% | Turnover=36.24%
   🎚️ Intra-Step TAPE: potential=0.2530 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0200 | critic_loss=0.0246 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0123 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0050
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-1.2937 | ema=0.3586 | best_ema=0.3586 | no_improve=0
[CYCLE] Update 28/70 | Step 28,224/100,000 | Episode 32 | Time: 2702.1s
   📊 Metrics: Return=+0.44% | Sharpe=-0.085 | DD=11.64% | Turnover=35.69%
   🎚️ Intra-Step TAPE: potential=0.2366 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0237 | critic_loss=0.0184 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0092 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0044
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0913 | ema=0.3136 | best_ema=0.3136 | no_improve=0
   🔬 Alpha Diversity: mean=1.72 | std=1.24 | range=[0.68, 4.84] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=2.07 | JPM=1.19 | MSFT=1.11  BOT: MSFT=1.11 | GLD=0.95 | NVDA=0.82
   🧬 FiLM: seq(dg=0.0003, db=0.0003, sat=0.0%) | latent(dg=0.0087, db=0.0057, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=12 (30.0%), low_vol=13 (32.5%), medium_vol=15 (37.5%)
[CYCLE] Update 29/70 | Step 29,232/100,000 | Episode 32 | Time: 2797.7s
   📊 Metrics: Return=-8.85% | Sharpe=-0.560 | DD=18.25% | Turnover=35.98%
   🎚️ Intra-Step TAPE: potential=0.2282 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0195 | critic_loss=0.0151 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0040
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5683 | ema=0.2254 | best_ema=0.2254 | no_improve=0
   [TOOL] Actor learning rate adjusted to 0.000020 at step 30,000
   [TOOL] Critic learning rate adjusted to 0.000120 at step 30,000

🧭 REWARD PHASE UPDATE at 30,240 steps:
   B_add_risk | base=True dsr=True turnover=False benchmark=True terminal=False
[CYCLE] Update 30/70 | Step 30,240/100,000 | Episode 32 | Time: 2893.5s
   📊 Metrics: Return=-9.88% | Sharpe=-0.491 | DD=19.16% | Turnover=36.18%
   🎚️ Intra-Step TAPE: potential=0.2413 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0234 | critic_loss=0.0111 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0055 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0044
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5014 | ema=0.1527 | best_ema=0.1527 | no_improve=0
   🔬 Alpha Diversity: mean=1.73 | std=1.20 | range=[0.66, 5.10] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=2.08 | JPM=1.39 | MSFT=1.18  BOT: MSFT=1.18 | GLD=0.88 | NVDA=0.80
   🧬 FiLM: seq(dg=0.0004, db=0.0003, sat=0.0%) | latent(dg=0.0088, db=0.0057, sat=0.0%) | asset(dg=0.0010, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=12 (30.0%), low_vol=13 (32.5%), medium_vol=15 (37.5%)

📚 PPO ROLLOUT UPDATE at 30,240 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 30,240 steps:
   Batch size: 336

[DOWN] PPO GAMMA UPDATE at 30,240 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 30,240 steps:
   gae_lambda: 0.9500

🧪 AUX-RETURN COEF UPDATE at 30,240 steps:
   aux_return_pred_coef: 0.3000

🌡️ TEMPERATURE UPDATE at 30,240 steps:
   temperature: 0.9000
[CYCLE] Update 31/70 | Step 31,752/100,000 | Episode 32 | Time: 3039.4s
   📊 Metrics: Return=-15.33% | Sharpe=-0.613 | DD=22.28% | Turnover=36.21%
   🎚️ Intra-Step TAPE: potential=0.2453 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0211 | critic_loss=0.0727 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0364 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0046
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.6236 | ema=0.0751 | best_ema=0.0751 | no_improve=0
[CYCLE] Update 32/70 | Step 33,264/100,000 | Episode 32 | Time: 3175.8s
   📊 Metrics: Return=-15.57% | Sharpe=-0.557 | DD=22.28% | Turnover=35.92%
   🎚️ Intra-Step TAPE: potential=0.2425 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0200 | critic_loss=0.0339 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0170 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0046
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.5647 | ema=0.0111 | best_ema=0.0111 | no_improve=0
   🔬 Alpha Diversity: mean=1.72 | std=1.15 | range=[0.65, 4.99] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=2.17 | JPM=1.44 | MSFT=1.15  BOT: MSFT=1.15 | GLD=0.84 | NVDA=0.81
   🧬 FiLM: seq(dg=0.0004, db=0.0003, sat=0.0%) | latent(dg=0.0090, db=0.0058, sat=0.0%) | asset(dg=0.0011, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=12 (30.0%), low_vol=13 (32.5%), medium_vol=15 (37.5%)
[CYCLE] Update 33/70 | Step 34,776/100,000 | Episode 40 | Time: 3311.0s
   📊 Metrics: Return=-2.23% | Sharpe=-0.214 | DD=15.75% | Turnover=34.92%
   🎚️ Intra-Step TAPE: potential=0.2885 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0131 | critic_loss=0.0371 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0185 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0038
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2141 | ema=-0.0114 | best_ema=-0.0114 | no_improve=0
   🔒 Drawdown λ snapshot=0.787 (peak 1.025, dd 1.07% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2375
   📈 Benchmark Relative: 1/N shaping=-0.000 (EW ret=0.00096) | SPY shaping=0.001 (SPY ret=-0.00005)
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=0.0000 | rolling_cvar=-0.03491
[CYCLE] Update 34/70 | Step 36,288/100,000 | Episode 40 | Time: 3445.1s
   📊 Metrics: Return=-3.11% | Sharpe=-0.801 | DD=5.92% | Turnover=36.83%
   🎚️ Intra-Step TAPE: potential=0.2374 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0143 | critic_loss=0.0304 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0152 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0026
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.8170 | ema=-0.0920 | best_ema=-0.0920 | no_improve=0
   🔬 Alpha Diversity: mean=1.68 | std=1.42 | range=[0.69, 5.10] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.48 | MSFT=1.01 | JPM=1.01  BOT: JPM=1.01 | GLD=0.98 | NVDA=0.82
   🧬 FiLM: seq(dg=0.0004, db=0.0003, sat=0.0%) | latent(dg=0.0092, db=0.0059, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=15 (31.2%), low_vol=15 (31.2%), medium_vol=18 (37.5%)
[CYCLE] Update 35/70 | Step 37,800/100,000 | Episode 40 | Time: 3579.8s
   📊 Metrics: Return=-8.51% | Sharpe=-0.972 | DD=10.23% | Turnover=37.05%
   🎚️ Intra-Step TAPE: potential=0.2453 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0222 | critic_loss=0.0278 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0139 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0025
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.9900 | ema=-0.1818 | best_ema=-0.1818 | no_improve=0
[CYCLE] Update 36/70 | Step 39,312/100,000 | Episode 40 | Time: 3716.3s
   📊 Metrics: Return=-13.89% | Sharpe=-0.927 | DD=18.71% | Turnover=37.32%
   🎚️ Intra-Step TAPE: potential=0.2463 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0173 | critic_loss=0.0199 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0099 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0024
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.9473 | ema=-0.2583 | best_ema=-0.2583 | no_improve=0
   🔬 Alpha Diversity: mean=1.67 | std=1.43 | range=[0.68, 5.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.42 | MSFT=1.05 | JPM=1.02  BOT: JPM=1.02 | GLD=0.91 | NVDA=0.83
   🧬 FiLM: seq(dg=0.0004, db=0.0003, sat=0.0%) | latent(dg=0.0093, db=0.0060, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=15 (31.2%), low_vol=15 (31.2%), medium_vol=18 (37.5%)

📚 TURNOVER CURRICULUM UPDATE at 40,824 steps:
   Turnover penalty scalar: 0.2

🎛️ EXECUTION BETA UPDATE at 40,824 steps:
   action_execution_beta: 0.850 (w_exec=(1-β)w_prev + βw_raw)
[CYCLE] Update 37/70 | Step 40,824/100,000 | Episode 40 | Time: 3851.8s
   📊 Metrics: Return=-5.54% | Sharpe=-0.419 | DD=18.71% | Turnover=37.02%
   🎚️ Intra-Step TAPE: potential=0.7466 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0135 | critic_loss=0.0274 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0137 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0031
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4365 | ema=-0.2761 | best_ema=-0.2761 | no_improve=0
[CYCLE] Update 38/70 | Step 42,336/100,000 | Episode 48 | Time: 3986.8s
   📊 Metrics: Return=+4.50% | Sharpe=-0.012 | DD=13.77% | Turnover=39.64%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0181 | critic_loss=0.0407 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0203 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0027
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0516 | ema=-0.2537 | best_ema=-0.2537 | no_improve=0
   🔬 Alpha Diversity: mean=1.67 | std=1.40 | range=[0.65, 5.08] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.48 | JPM=1.06 | MSFT=0.99  BOT: MSFT=0.99 | GLD=0.96 | NVDA=0.79
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0094, db=0.0061, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (30.4%), low_vol=20 (35.7%), medium_vol=19 (33.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2474
   📈 Benchmark Relative: 1/N shaping=0.000 (EW ret=-0.00031) | SPY shaping=0.001 (SPY ret=-0.00068)
[CYCLE] Update 39/70 | Step 43,848/100,000 | Episode 48 | Time: 4121.2s
   📊 Metrics: Return=-4.34% | Sharpe=-1.188 | DD=5.93% | Turnover=46.59%
   🎚️ Intra-Step TAPE: potential=0.2414 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0157 | critic_loss=0.0382 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0191 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0018
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.2874 | ema=-0.3571 | best_ema=-0.3571 | no_improve=0
[CYCLE] Update 40/70 | Step 45,360/100,000 | Episode 48 | Time: 4256.5s
   📊 Metrics: Return=-11.21% | Sharpe=-1.284 | DD=16.06% | Turnover=47.48%
   🎚️ Intra-Step TAPE: potential=0.2410 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0136 | critic_loss=0.0389 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0195 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.3908 | ema=-0.4604 | best_ema=-0.4604 | no_improve=0
   🔬 Alpha Diversity: mean=1.65 | std=1.49 | range=[0.71, 5.08] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.22 | GLD=0.97 | JPM=0.94  BOT: JPM=0.94 | MSFT=0.94 | NVDA=0.86
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0097, db=0.0062, sat=0.0%) | asset(dg=0.0012, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (30.4%), low_vol=20 (35.7%), medium_vol=19 (33.9%)
[CYCLE] Update 41/70 | Step 46,872/100,000 | Episode 48 | Time: 4391.0s
   📊 Metrics: Return=-10.23% | Sharpe=-0.794 | DD=16.27% | Turnover=48.04%
   🎚️ Intra-Step TAPE: potential=0.2235 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0095 | critic_loss=0.0278 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0139 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.9061 | ema=-0.5050 | best_ema=-0.5050 | no_improve=0

📚 EPISODE HORIZON UPDATE at 48,384 steps:
   Episode horizon: 1102 steps
[CYCLE] Update 42/70 | Step 48,384/100,000 | Episode 48 | Time: 4525.6s
   📊 Metrics: Return=-12.76% | Sharpe=-0.801 | DD=16.27% | Turnover=47.93%
   🎚️ Intra-Step TAPE: potential=0.2412 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0116 | critic_loss=0.0322 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0161 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0011
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.9122 | ema=-0.5457 | best_ema=-0.5457 | no_improve=0
   🔬 Alpha Diversity: mean=1.65 | std=1.48 | range=[0.69, 5.07] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.27 | JPM=0.98 | MSFT=0.98  BOT: MSFT=0.98 | GLD=0.90 | NVDA=0.83
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0098, db=0.0063, sat=0.0%) | asset(dg=0.0012, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (30.4%), low_vol=20 (35.7%), medium_vol=19 (33.9%)

📚 EPISODE HORIZON UPDATE at 49,896 steps:
   Episode horizon: 1474 steps
[CYCLE] Update 43/70 | Step 49,896/100,000 | Episode 48 | Time: 4660.2s
   📊 Metrics: Return=+0.20% | Sharpe=-0.217 | DD=16.27% | Turnover=47.76%
   🎚️ Intra-Step TAPE: potential=0.7454 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0235 | critic_loss=0.0575 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0287 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0012
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3258 | ema=-0.5237 | best_ema=-0.5237 | no_improve=0

📚 EPISODE HORIZON UPDATE at 51,408 steps:
   Episode horizon: 1500 steps
[CYCLE] Update 44/70 | Step 51,408/100,000 | Episode 48 | Time: 4794.2s
   📊 Metrics: Return=-5.10% | Sharpe=-0.358 | DD=16.27% | Turnover=47.32%
   🎚️ Intra-Step TAPE: potential=0.2227 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0197 | critic_loss=0.0860 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0430 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4639 | ema=-0.5177 | best_ema=-0.5177 | no_improve=0
   🔬 Alpha Diversity: mean=1.64 | std=1.48 | range=[0.68, 5.07] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.17 | JPM=1.04 | MSFT=1.01  BOT: MSFT=1.01 | GLD=0.86 | NVDA=0.82
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0102, db=0.0066, sat=0.0%) | asset(dg=0.0012, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (30.4%), low_vol=20 (35.7%), medium_vol=19 (33.9%)

🎯 ENTROPY COEF UPDATE at 51,408 steps:
   entropy_coef: 0.0010
[CYCLE] Update 45/70 | Step 52,920/100,000 | Episode 48 | Time: 4928.1s
   📊 Metrics: Return=-3.97% | Sharpe=-0.308 | DD=16.27% | Turnover=46.98%
   🎚️ Intra-Step TAPE: potential=0.2299 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0096 | critic_loss=0.0646 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0323 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0013
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4107 | ema=-0.5070 | best_ema=-0.5070 | no_improve=0
[CYCLE] Update 46/70 | Step 54,432/100,000 | Episode 56 | Time: 5062.2s
   📊 Metrics: Return=-21.70% | Sharpe=-0.748 | DD=32.89% | Turnover=48.00%
   🎚️ Intra-Step TAPE: potential=0.2245 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0172 | critic_loss=0.0683 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0341 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0010
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.0491 | ema=-0.5612 | best_ema=-0.5612 | no_improve=0
   🔬 Alpha Diversity: mean=1.63 | std=1.48 | range=[0.69, 5.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.22 | MSFT=1.03 | JPM=0.99  BOT: JPM=0.99 | GLD=0.84 | NVDA=0.82
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0103, db=0.0067, sat=0.0%) | asset(dg=0.0012, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=25 (39.1%), medium_vol=21 (32.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 11.99% / trig 16.50%) | terminal=5.000 (peak 5.000) | TAPE=0.1938
   📈 Benchmark Relative: 1/N shaping=-0.061 (EW ret=0.01914) | SPY shaping=-0.007 (SPY ret=0.01350)
[CYCLE] Update 47/70 | Step 55,944/100,000 | Episode 56 | Time: 5195.3s
   📊 Metrics: Return=-12.62% | Sharpe=-1.816 | DD=14.97% | Turnover=46.90%
   🎚️ Intra-Step TAPE: potential=0.2632 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0067 | critic_loss=0.0733 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0367 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0006
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.9176 | ema=-0.6969 | best_ema=-0.6969 | no_improve=0
[CYCLE] Update 48/70 | Step 57,456/100,000 | Episode 56 | Time: 5328.7s
   📊 Metrics: Return=-10.63% | Sharpe=-1.097 | DD=15.19% | Turnover=46.64%
   🎚️ Intra-Step TAPE: potential=0.3562 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0114 | critic_loss=0.0642 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0321 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0004
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.1965 | ema=-0.7468 | best_ema=-0.7468 | no_improve=0
   🔬 Alpha Diversity: mean=1.62 | std=1.53 | range=[0.75, 5.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.06 | JPM=0.94 | MSFT=0.93  BOT: MSFT=0.93 | NVDA=0.92 | GLD=0.85
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0103, db=0.0067, sat=0.0%) | asset(dg=0.0012, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=25 (39.1%), medium_vol=21 (32.8%)
[CYCLE] Update 49/70 | Step 58,968/100,000 | Episode 56 | Time: 5461.9s
   📊 Metrics: Return=-11.09% | Sharpe=-0.901 | DD=15.19% | Turnover=46.91%
   🎚️ Intra-Step TAPE: potential=0.4532 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0125 | critic_loss=0.0594 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0297 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0003
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.0030 | ema=-0.7725 | best_ema=-0.7725 | no_improve=0

📚 TURNOVER CURRICULUM UPDATE at 60,480 steps:
   Turnover penalty scalar: 0.3

🎛️ EXECUTION BETA UPDATE at 60,480 steps:
   action_execution_beta: 1.000 (w_exec=(1-β)w_prev + βw_raw)

🧭 REWARD PHASE UPDATE at 60,480 steps:
   C_full_tape | base=True dsr=True turnover=True benchmark=True terminal=True
[CYCLE] Update 50/70 | Step 60,480/100,000 | Episode 56 | Time: 5595.1s
   📊 Metrics: Return=-19.45% | Sharpe=-1.163 | DD=20.64% | Turnover=47.00%
   🎚️ Intra-Step TAPE: potential=0.2444 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0100 | critic_loss=0.0472 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0236 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0003
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.2663 | ema=-0.8218 | best_ema=-0.8218 | no_improve=0
   🔬 Alpha Diversity: mean=1.61 | std=1.53 | range=[0.76, 5.06] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.03 | JPM=0.95 | MSFT=0.94  BOT: MSFT=0.94 | NVDA=0.92 | GLD=0.82
   🧬 FiLM: seq(dg=0.0005, db=0.0004, sat=0.0%) | latent(dg=0.0106, db=0.0069, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=25 (39.1%), medium_vol=21 (32.8%)

📚 PPO ROLLOUT UPDATE at 60,480 steps:
   Timesteps per update: 2016

📚 PPO BATCH SIZE UPDATE at 60,480 steps:
   Batch size: 504

🧪 AUX-RETURN COEF UPDATE at 60,480 steps:
   aux_return_pred_coef: 0.2500

🌡️ TEMPERATURE UPDATE at 60,480 steps:
   temperature: 0.8000
[CYCLE] Update 51/70 | Step 62,496/100,000 | Episode 56 | Time: 5753.6s
   📊 Metrics: Return=-23.96% | Sharpe=-1.013 | DD=28.88% | Turnover=50.59%
   🎚️ Intra-Step TAPE: potential=0.5632 | delta_reward=+0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0117 | critic_loss=0.1199 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0600 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0003
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.2394 | ema=-0.8636 | best_ema=-0.8636 | no_improve=0
[CYCLE] Update 52/70 | Step 64,512/100,000 | Episode 56 | Time: 5906.7s
   📊 Metrics: Return=-18.42% | Sharpe=-0.653 | DD=28.88% | Turnover=52.18%
   🎚️ Intra-Step TAPE: potential=0.2745 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0125 | critic_loss=0.0797 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0399 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0002
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.8938 | ema=-0.8666 | best_ema=-0.8666 | no_improve=0
   🔬 Alpha Diversity: mean=1.61 | std=1.52 | range=[0.75, 5.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.03 | MSFT=0.98 | JPM=0.94  BOT: JPM=0.94 | GLD=0.86 | NVDA=0.82
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0107, db=0.0071, sat=0.0%) | asset(dg=0.0012, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=25 (39.1%), medium_vol=21 (32.8%)
[CYCLE] Update 53/70 | Step 66,528/100,000 | Episode 64 | Time: 6061.6s
   📊 Metrics: Return=-35.97% | Sharpe=-1.167 | DD=39.08% | Turnover=54.32%
   🎚️ Intra-Step TAPE: potential=0.2127 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0106 | critic_loss=0.1025 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0513 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0002
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.6710 | ema=-0.9471 | best_ema=-0.9471 | no_improve=0
   🔒 Drawdown λ snapshot=2.823 (peak 3.043, dd 11.20% / trig 16.50%) | terminal=5.000 (peak 5.000) | TAPE=0.1976
   📈 Benchmark Relative: 1/N shaping=-0.039 (EW ret=0.02228) | SPY shaping=-0.011 (SPY ret=0.02303)
[CYCLE] Update 54/70 | Step 68,544/100,000 | Episode 64 | Time: 6214.4s
   📊 Metrics: Return=-22.84% | Sharpe=-1.780 | DD=25.30% | Turnover=58.38%
   🎚️ Intra-Step TAPE: potential=0.2406 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0101 | critic_loss=0.1090 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0545 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0002
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.9872 | ema=-1.0511 | best_ema=-1.0511 | no_improve=0
   🔬 Alpha Diversity: mean=1.60 | std=1.53 | range=[0.73, 5.04] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.02 | MSFT=0.91 | GLD=0.88  BOT: GLD=0.88 | JPM=0.88 | NVDA=0.87
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0105, db=0.0070, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=21 (29.2%), low_vol=29 (40.3%), medium_vol=22 (30.6%)
   [TOOL] Actor learning rate adjusted to 0.000010 at step 70,000
   [TOOL] Critic learning rate adjusted to 0.000100 at step 70,000
[CYCLE] Update 55/70 | Step 70,560/100,000 | Episode 64 | Time: 6367.4s
   📊 Metrics: Return=-28.82% | Sharpe=-1.537 | DD=30.41% | Turnover=59.31%
   🎚️ Intra-Step TAPE: potential=0.2145 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0101 | critic_loss=0.0849 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0424 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.8753 | ema=-1.1335 | best_ema=-1.1335 | no_improve=0

[DOWN] PPO GAMMA UPDATE at 70,560 steps:
   gamma: 0.9980

[DOWN] PPO GAE-λ UPDATE at 70,560 steps:
   gae_lambda: 0.9700
[CYCLE] Update 56/70 | Step 72,576/100,000 | Episode 64 | Time: 6520.3s
   📊 Metrics: Return=-32.25% | Sharpe=-1.411 | DD=34.31% | Turnover=59.00%
   🎚️ Intra-Step TAPE: potential=0.2445 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0118 | critic_loss=0.1244 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0622 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0002
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.8400 | ema=-1.2041 | best_ema=-1.2041 | no_improve=0
   🔬 Alpha Diversity: mean=1.59 | std=1.53 | range=[0.73, 5.03] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.00 | MSFT=0.93 | JPM=0.90  BOT: JPM=0.90 | NVDA=0.86 | GLD=0.85
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0107, db=0.0071, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=21 (29.2%), low_vol=29 (40.3%), medium_vol=22 (30.6%)
[CYCLE] Update 57/70 | Step 74,592/100,000 | Episode 64 | Time: 6673.3s
   📊 Metrics: Return=-40.49% | Sharpe=-1.516 | DD=41.30% | Turnover=59.08%
   🎚️ Intra-Step TAPE: potential=0.2352 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0115 | critic_loss=0.0891 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0446 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0002
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-2.1140 | ema=-1.2951 | best_ema=-1.2951 | no_improve=0
[CYCLE] Update 58/70 | Step 76,608/100,000 | Episode 64 | Time: 6826.4s
   📊 Metrics: Return=-46.22% | Sharpe=-1.462 | DD=50.02% | Turnover=59.54%
   🎚️ Intra-Step TAPE: potential=0.6769 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0100 | critic_loss=0.0497 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0249 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-2.2729 | ema=-1.3929 | best_ema=-1.3929 | no_improve=0
   🔬 Alpha Diversity: mean=1.58 | std=1.53 | range=[0.72, 5.03] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.98 | MSFT=0.93 | JPM=0.91  BOT: JPM=0.91 | GLD=0.85 | NVDA=0.82
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0107, db=0.0072, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=21 (29.2%), low_vol=29 (40.3%), medium_vol=22 (30.6%)

📚 EPISODE HORIZON UPDATE at 78,624 steps:
   Episode horizon: 1896 steps
[CYCLE] Update 59/70 | Step 78,624/100,000 | Episode 72 | Time: 6979.7s
   📊 Metrics: Return=-33.43% | Sharpe=-1.060 | DD=38.04% | Turnover=60.18%
   🎚️ Intra-Step TAPE: potential=0.2143 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0086 | critic_loss=0.0876 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0438 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.5887 | ema=-1.4125 | best_ema=-1.4125 | no_improve=0
   🔒 Drawdown λ snapshot=3.412 (peak 3.750, dd 4.87% / trig 16.50%) | terminal=5.000 (peak 5.000) | TAPE=0.1992
   📈 Benchmark Relative: 1/N shaping=-0.007 (EW ret=0.00745) | SPY shaping=0.009 (SPY ret=0.00025)

📚 TURNOVER CURRICULUM UPDATE at 80,640 steps:
   Turnover penalty scalar: 0.4

📚 EPISODE HORIZON UPDATE at 80,640 steps:
   Episode horizon set to full dataset
[CYCLE] Update 60/70 | Step 80,640/100,000 | Episode 72 | Time: 7132.0s
   📊 Metrics: Return=-6.51% | Sharpe=-1.123 | DD=9.55% | Turnover=58.44%
   🎚️ Intra-Step TAPE: potential=0.2171 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0090 | critic_loss=0.6115 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.3235 | ema=-1.4036 | best_ema=-1.4036 | no_improve=0
   🔬 Alpha Diversity: mean=1.57 | std=1.53 | range=[0.72, 5.02] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.97 | MSFT=0.89 | JPM=0.87  BOT: JPM=0.87 | GLD=0.86 | NVDA=0.84
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0105, db=0.0070, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=34 (42.5%), medium_vol=22 (27.5%)

🎯 ENTROPY COEF UPDATE at 80,640 steps:
   entropy_coef: 0.0005

📚 EPISODE HORIZON UPDATE at 82,656 steps:
   Episode horizon set to full dataset
[CYCLE] Update 61/70 | Step 82,656/100,000 | Episode 72 | Time: 7284.8s
   📊 Metrics: Return=-16.75% | Sharpe=-1.460 | DD=19.17% | Turnover=59.79%
   🎚️ Intra-Step TAPE: potential=0.2214 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0060 | critic_loss=0.2191 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.6725 | ema=-1.4305 | best_ema=-1.4305 | no_improve=0

📚 EPISODE HORIZON UPDATE at 84,672 steps:
   Episode horizon set to full dataset
[CYCLE] Update 62/70 | Step 84,672/100,000 | Episode 72 | Time: 7440.3s
   📊 Metrics: Return=-12.35% | Sharpe=-0.755 | DD=22.92% | Turnover=59.15%
   🎚️ Intra-Step TAPE: potential=0.5689 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0068 | critic_loss=0.2000 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1000 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.9617 | ema=-1.3836 | best_ema=-1.3836 | no_improve=0
   🔬 Alpha Diversity: mean=1.56 | std=1.54 | range=[0.76, 5.01] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.95 | JPM=0.89 | MSFT=0.88  BOT: MSFT=0.88 | NVDA=0.85 | GLD=0.82
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0107, db=0.0072, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=34 (42.5%), medium_vol=22 (27.5%)

📚 EPISODE HORIZON UPDATE at 86,688 steps:
   Episode horizon set to full dataset
[CYCLE] Update 63/70 | Step 86,688/100,000 | Episode 72 | Time: 7594.0s
   📊 Metrics: Return=-7.59% | Sharpe=-0.429 | DD=22.92% | Turnover=58.87%
   🎚️ Intra-Step TAPE: potential=0.2395 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0097 | critic_loss=0.0870 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0435 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.6341 | ema=-1.3086 | best_ema=-1.3086 | no_improve=0

📚 EPISODE HORIZON UPDATE at 88,704 steps:
   Episode horizon set to full dataset
[CYCLE] Update 64/70 | Step 88,704/100,000 | Episode 72 | Time: 7749.2s
   📊 Metrics: Return=-6.98% | Sharpe=-0.379 | DD=22.92% | Turnover=59.33%
   🎚️ Intra-Step TAPE: potential=0.2314 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0093 | critic_loss=0.0945 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0472 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.5878 | ema=-1.2366 | best_ema=-1.2366 | no_improve=0
   🔬 Alpha Diversity: mean=1.56 | std=1.52 | range=[0.69, 5.00] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.96 | MSFT=0.95 | JPM=0.90  BOT: JPM=0.90 | GLD=0.82 | NVDA=0.77
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0108, db=0.0073, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=34 (42.5%), medium_vol=22 (27.5%)

📚 EPISODE HORIZON UPDATE at 90,720 steps:
   Episode horizon set to full dataset
[CYCLE] Update 65/70 | Step 90,720/100,000 | Episode 72 | Time: 7906.1s
   📊 Metrics: Return=-21.26% | Sharpe=-0.669 | DD=24.65% | Turnover=59.55%
   🎚️ Intra-Step TAPE: potential=0.2096 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0084 | critic_loss=0.1188 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0594 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.8793 | ema=-1.2008 | best_ema=-1.2008 | no_improve=0

📚 EPISODE HORIZON UPDATE at 92,736 steps:
   Episode horizon set to full dataset
[CYCLE] Update 66/70 | Step 92,736/100,000 | Episode 76 | Time: 8064.7s
   📊 Metrics: Return=-37.57% | Sharpe=-1.114 | DD=39.53% | Turnover=59.97%
   🎚️ Intra-Step TAPE: potential=0.2345 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0069 | critic_loss=0.1326 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0663 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.6764 | ema=-1.2484 | best_ema=-1.2484 | no_improve=0
   🔬 Alpha Diversity: mean=1.56 | std=1.51 | range=[0.66, 5.00] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.01 | MSFT=0.95 | JPM=0.88  BOT: JPM=0.88 | GLD=0.82 | NVDA=0.74
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0109, db=0.0073, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (31.0%), low_vol=35 (41.7%), medium_vol=23 (27.4%)
   🔒 Drawdown λ snapshot=2.159 (peak 2.543, dd 12.33% / trig 16.50%) | terminal=5.000 (peak 5.000) | TAPE=0.1900
   📈 Benchmark Relative: 1/N shaping=-0.019 (EW ret=0.00506) | SPY shaping=-0.001 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 94,752 steps:
   Episode horizon set to full dataset
[CYCLE] Update 67/70 | Step 94,752/100,000 | Episode 80 | Time: 8222.7s
   📊 Metrics: Return=-14.14% | Sharpe=-1.247 | DD=16.18% | Turnover=60.76%
   🎚️ Intra-Step TAPE: potential=0.2458 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0047 | critic_loss=0.2446 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1223 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.4680 | ema=-1.2703 | best_ema=-1.2703 | no_improve=0
   🔒 Drawdown λ snapshot=1.397 (peak 1.481, dd 0.13% / trig 16.50%) | terminal=1.975 (peak 2.543) | TAPE=0.2118
   📈 Benchmark Relative: 1/N shaping=-0.029 (EW ret=0.00506) | SPY shaping=-0.003 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 96,768 steps:
   Episode horizon set to full dataset
[CYCLE] Update 68/70 | Step 96,768/100,000 | Episode 81 | Time: 8381.5s
   📊 Metrics: Return=-15.84% | Sharpe=-1.079 | DD=23.16% | Turnover=62.02%
   🎚️ Intra-Step TAPE: potential=0.6266 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0055 | critic_loss=0.2391 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1195 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.3104 | ema=-1.2743 | best_ema=-1.2743 | no_improve=0
   🔬 Alpha Diversity: mean=1.56 | std=1.52 | range=[0.67, 5.00] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.98 | MSFT=0.89 | JPM=0.89  BOT: JPM=0.89 | GLD=0.85 | NVDA=0.77
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0109, db=0.0073, sat=0.0%) | asset(dg=0.0013, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=27 (30.3%), low_vol=38 (42.7%), medium_vol=24 (27.0%)
   🔒 Drawdown λ snapshot=0.599 (peak 1.481, dd 5.28% / trig 16.50%) | terminal=3.927 (peak 3.927) | TAPE=0.1922
   📈 Benchmark Relative: 1/N shaping=-0.021 (EW ret=0.00506) | SPY shaping=-0.001 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 98,784 steps:
   Episode horizon set to full dataset
[CYCLE] Update 69/70 | Step 98,784/100,000 | Episode 84 | Time: 8540.1s
   📊 Metrics: Return=-20.16% | Sharpe=-1.340 | DD=22.90% | Turnover=61.17%
   🎚️ Intra-Step TAPE: potential=0.6648 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0065 | critic_loss=0.0968 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0484 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.5638 | ema=-1.3033 | best_ema=-1.3033 | no_improve=0
   🔒 Drawdown λ snapshot=0.455 (peak 1.481, dd 14.11% / trig 16.50%) | terminal=4.035 (peak 4.035) | TAPE=0.1897
   📈 Benchmark Relative: 1/N shaping=-0.009 (EW ret=0.00506) | SPY shaping=0.002 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 100,000 steps:
   Episode horizon set to full dataset
[CYCLE] Update 70/70 | Step 100,000/100,000 | Episode 85 | Time: 8645.0s
   📊 Metrics: Return=-7.05% | Sharpe=-1.052 | DD=11.13% | Turnover=61.67%
   🎚️ Intra-Step TAPE: potential=0.2317 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0084 | critic_loss=0.0845 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0422 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0006 | dispersion_loss=0.0001
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-1.2810 | ema=-1.3011 | best_ema=-1.3011 | no_improve=0
   🔬 Alpha Diversity: mean=1.56 | std=1.52 | range=[0.64, 5.00] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=0.97 | MSFT=0.94 | JPM=0.88  BOT: JPM=0.88 | GLD=0.85 | NVDA=0.75
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0109, db=0.0073, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=29 (31.2%), low_vol=39 (41.9%), medium_vol=25 (26.9%)
   🔒 Drawdown λ snapshot=0.815 (peak 1.481, dd 21.02% / trig 16.50%) | terminal=2.984 (peak 3.750) | TAPE=0.2224
   📈 Benchmark Relative: 1/N shaping=-0.022 (EW ret=0.00506) | SPY shaping=-0.001 (SPY ret=0.00243)

[OK] THREE-COMPONENT TAPE v3 training completed!
   Total episodes: 85
   Total timesteps: 100,000
   Training time: 8645.03s (144.08min)
📊 Training summary saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260319_152902_summary.csv
💾 Final models saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00085_shm1p052_actor.weights.h5, /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00085_shm1p052_critic.weights.h5
🎯 Default selected checkpoint: final high-watermark-style checkpoint
[OK] Training complete
checkpoint_prefix: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00085_shm1p052