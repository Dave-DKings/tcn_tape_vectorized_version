[START] Starting training
Architecture: TCN_FUSION
max_total_timesteps: 500000
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
[OK] Features: Enhanced (includes 10 covariance eigenvalues)
   Eigenvalues: ['Covariance_Eigenvalue_0', 'Covariance_Eigenvalue_1', 'Covariance_ExplainedVarRatio_0', 'Covariance_ExplainedVarRatio_1', 'Covariance_Trace', 'Covariance_EffectiveRank', 'Covariance_MeanPairwiseCorr', 'Covariance_CorrDispersion', 'Covariance_PC1_Loading', 'Covariance_PC2_Loading']
   Train shape: (27680, 75)
   Test shape: (14230, 75)
   ℹ️ Actuarial features disabled by config.

🏗️ Creating THREE-COMPONENT TAPE v3 environments (with curriculum)...
   🎯 Reward System: TAPE (Three-Component v3)
   📊 Profile: BalancedGrowth
   ⚙️  Component 1: Base Reward (Net Return)
   ⚙️  Component 2: DSR/PBRS (window=60, scalar=2.00, gamma=0.99)
   ⚙️  Component 3: Turnover Proximity (target=0.35, band=±0.20, scalar=0.00 -> 0.05 => 0.10 => 0.20 => 0.30)
      ↳ Schedule: 0.00@0 => 0.05@200,000 => 0.10@325,000 => 0.20@400,000 => 0.30@475,000
   ⚙️  Component 4: Execution Inertia (beta=0.55 -> 0.65 => 0.80 => 0.95 => 1.00, w_exec=(1-β)w_prev + βw_raw)
      ↳ Schedule: 0.55@0 => 0.65@150,000 => 0.80@300,000 => 0.95@425,000 => 1.00@475,000
   🧭 Reward Component Curriculum:
      0+ steps: A_return_only | base=True dsr=False turnover=False benchmark=False terminal=False | weights=b1.00/d0.00/t0.00/bm0.00/tt0.00
      200,000+ steps: B_ramp_1 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.25/t0.00/bm0.20/tt0.00
      240,000+ steps: B_ramp_2 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.55/t0.00/bm0.45/tt0.00
      280,000+ steps: B_full | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d1.00/t0.00/bm0.75/tt0.00
      375,000+ steps: C_ramp_1 | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t0.20/bm0.90/tt0.20
      410,000+ steps: C_ramp_2 | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t0.50/bm1.00/tt0.50
      445,000+ steps: C_full_tape | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t1.00/bm1.00/tt1.00
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
   🔐 Lagrangian CVaR: disabled
   Tail-Aware Advantage: ENABLED | weight=0.1 | bottom_k=4
   Alpha Regularization: hhi_coef=0.0 | dispersion_coef=0.2 | target_std=0.2
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
   [TOOL] Actor LR schedule: 0.000030@0 => 0.000020@150,000 => 0.000010@350,000
   [TOOL] Critic LR schedule: 0.000150@0 => 0.000120@150,000 => 0.000100@350,000
   State dim: 273
   Action dim: 10
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
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0007
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@150,000 => 0.9980@350,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@150,000 => 0.9700@350,000
   🎯 Entropy coef schedule: 0.0007@0 => 0.0005@150,000 => 0.0003@300,000 => 0.0001@425,000
   🧪 Aux-return coef schedule: 0.3500@0 => 0.3000@150,000 => 0.2500@300,000
   🌡️ Temperature schedule: 1.0000@0 => 0.9000@150,000 => 0.8000@300,000
   📐 PPO rollout schedule: 1008@0 => 1512@150,000 => 2016@300,000
   🧺 PPO batch-size schedule: 252@0 => 336@150,000 => 504@300,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260320_160032_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260320_160032_step_diagnostics.csv

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
      200,000+ steps: limit=1008
      350,000+ steps: limit=1500
      475,000+ steps: limit=full
      ↳ smooth ramp: enabled (overlap=10,000 steps)
   📚 Turnover Scalar Curriculum:
      0+ steps: scalar=0.00
      200,000+ steps: scalar=0.05
      325,000+ steps: scalar=0.10
      400,000+ steps: scalar=0.20
      475,000+ steps: scalar=0.30
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.55
      150,000+ steps: beta=0.65
      300,000+ steps: beta=0.80
      425,000+ steps: beta=0.95
      475,000+ steps: beta=1.00
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.70, MDD <= 25.0%, skip_on_det_validation=True)
   ⏹️ Training early-stop: enabled (warmup=250,000 steps, patience=50 updates, min_delta=0.005, hard_dd=45.0% x 8)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260320_160032_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260320_160032_metadata.json
[CYCLE] Update 1/348 | Step 1,008/500,000 | Episode 0 | Time: 120.6s
   📊 Metrics: Return=-2.50% | Sharpe=-0.525 | DD=7.14% | Turnover=29.73%
   🎚️ Intra-Step TAPE: potential=0.2534 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.2169 | critic_loss=0.2844 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1422 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0294
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5248 | ema=-0.5248 | best_ema=-0.5248 | no_improve=0
[CYCLE] Update 2/348 | Step 2,016/500,000 | Episode 0 | Time: 217.6s
   📊 Metrics: Return=-3.44% | Sharpe=-0.341 | DD=14.15% | Turnover=29.29%
   🎚️ Intra-Step TAPE: potential=0.6193 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1314 | critic_loss=0.3048 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1524 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0292
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3412 | ema=-0.5064 | best_ema=-0.5064 | no_improve=0
   🔬 Alpha Diversity: mean=2.18 | std=1.08 | range=[0.95, 6.22] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=3.25 | XOM=2.90 | MSFT=2.53  BOT: NVDA=1.23 | GLD=1.22 | AMZN=1.09
   🧬 FiLM: seq(dg=0.0001, db=0.0000, sat=0.0%) | latent(dg=0.0003, db=0.0002, sat=0.0%) | asset(dg=0.0002, db=0.0001, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=1 (12.5%), low_vol=6 (75.0%), medium_vol=1 (12.5%)
[CYCLE] Update 3/348 | Step 3,024/500,000 | Episode 0 | Time: 314.8s
   📊 Metrics: Return=+1.62% | Sharpe=-0.001 | DD=14.15% | Turnover=29.18%
   🎚️ Intra-Step TAPE: potential=0.3057 | delta_reward=-0.0026
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1130 | critic_loss=0.2494 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1247 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0293
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0014 | ema=-0.4559 | best_ema=-0.4559 | no_improve=0
[CYCLE] Update 4/348 | Step 4,032/500,000 | Episode 0 | Time: 411.8s
   📊 Metrics: Return=+10.45% | Sharpe=0.300 | DD=14.15% | Turnover=29.05%
   🎚️ Intra-Step TAPE: potential=0.7420 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0981 | critic_loss=0.2449 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1224 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0292
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2995 | ema=-0.3804 | best_ema=-0.3804 | no_improve=0
   🔬 Alpha Diversity: mean=2.19 | std=1.09 | range=[0.95, 5.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=3.07 | MSFT=3.02 | KO=2.83  BOT: NVDA=1.47 | AMZN=1.41 | GLD=1.02
   🧬 FiLM: seq(dg=0.0001, db=0.0001, sat=0.0%) | latent(dg=0.0012, db=0.0006, sat=0.0%) | asset(dg=0.0004, db=0.0002, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=1 (12.5%), low_vol=6 (75.0%), medium_vol=1 (12.5%)
[CYCLE] Update 5/348 | Step 5,040/500,000 | Episode 0 | Time: 509.1s
   📊 Metrics: Return=+21.37% | Sharpe=0.551 | DD=14.15% | Turnover=28.88%
   🎚️ Intra-Step TAPE: potential=0.7247 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0903 | critic_loss=0.2606 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1303 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0292
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5510 | ema=-0.2872 | best_ema=-0.2872 | no_improve=0
[CYCLE] Update 6/348 | Step 6,048/500,000 | Episode 8 | Time: 605.2s
   📊 Metrics: Return=+13.22% | Sharpe=0.235 | DD=12.52% | Turnover=28.40%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0779 | critic_loss=0.2456 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1228 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0293
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2355 | ema=-0.2350 | best_ema=-0.2350 | no_improve=0
   🔬 Alpha Diversity: mean=2.17 | std=1.14 | range=[0.95, 6.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.90 | KO=2.55 | XOM=2.55  BOT: CAT=1.74 | NVDA=1.61 | GLD=1.03
   🧬 FiLM: seq(dg=0.0001, db=0.0001, sat=0.0%) | latent(dg=0.0030, db=0.0017, sat=0.0%) | asset(dg=0.0005, db=0.0004, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.500) | TAPE=0.2618
[CYCLE] Update 7/348 | Step 7,056/500,000 | Episode 8 | Time: 702.5s
   📊 Metrics: Return=+23.80% | Sharpe=3.447 | DD=2.71% | Turnover=29.02%
   🎚️ Intra-Step TAPE: potential=0.7335 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0729 | critic_loss=0.2646 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1323 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0293
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.4465 | ema=0.1332 | best_ema=0.1332 | no_improve=0
[CYCLE] Update 8/348 | Step 8,064/500,000 | Episode 8 | Time: 799.6s
   📊 Metrics: Return=+13.63% | Sharpe=0.751 | DD=14.21% | Turnover=29.50%
   🎚️ Intra-Step TAPE: potential=0.2294 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0672 | critic_loss=0.2484 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1242 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0294
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7514 | ema=0.1950 | best_ema=0.1950 | no_improve=0
   🔬 Alpha Diversity: mean=2.17 | std=1.08 | range=[0.95, 6.35] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.74 | XOM=2.82 | KO=2.79  BOT: CAT=1.73 | NVDA=1.43 | GLD=1.34
   🧬 FiLM: seq(dg=0.0001, db=0.0001, sat=0.0%) | latent(dg=0.0049, db=0.0028, sat=0.0%) | asset(dg=0.0007, db=0.0005, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
[CYCLE] Update 9/348 | Step 9,072/500,000 | Episode 8 | Time: 896.6s
   📊 Metrics: Return=+19.71% | Sharpe=0.674 | DD=14.69% | Turnover=29.55%
   🎚️ Intra-Step TAPE: potential=0.6966 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0657 | critic_loss=0.2239 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1119 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0294
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6737 | ema=0.2429 | best_ema=0.2429 | no_improve=0
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 8 | Time: 993.7s
   📊 Metrics: Return=+18.74% | Sharpe=0.492 | DD=14.69% | Turnover=28.97%
   🎚️ Intra-Step TAPE: potential=0.5809 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0605 | critic_loss=0.2337 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1169 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0294
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4917 | ema=0.2678 | best_ema=0.2678 | no_improve=0
   🔬 Alpha Diversity: mean=2.17 | std=1.10 | range=[0.95, 6.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.99 | KO=2.93 | XOM=2.86  BOT: CAT=1.62 | NVDA=1.25 | GLD=1.13
   🧬 FiLM: seq(dg=0.0001, db=0.0001, sat=0.0%) | latent(dg=0.0063, db=0.0037, sat=0.0%) | asset(dg=0.0007, db=0.0005, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
[CYCLE] Update 11/348 | Step 11,088/500,000 | Episode 8 | Time: 1091.0s
   📊 Metrics: Return=+19.35% | Sharpe=0.415 | DD=14.69% | Turnover=28.85%
   🎚️ Intra-Step TAPE: potential=0.7039 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0585 | critic_loss=0.1870 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0935 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0292
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4146 | ema=0.2824 | best_ema=0.2824 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p053_actor.weights.h5 (Sharpe=1.053, MDD=18.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp0p753_actor.weights.h5 (Sharpe=0.753, MDD=19.57%)
[CYCLE] Update 12/348 | Step 12,096/500,000 | Episode 16 | Time: 1187.8s
   📊 Metrics: Return=+11.49% | Sharpe=0.182 | DD=22.27% | Turnover=28.76%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0572 | critic_loss=0.2130 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1065 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0289
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1817 | ema=0.2724 | best_ema=0.2724 | no_improve=0
   🔬 Alpha Diversity: mean=2.17 | std=1.26 | range=[0.95, 7.22] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.08 | KO=2.83 | XOM=2.57  BOT: NVDA=1.21 | GLD=1.20 | CAT=1.14
   🧬 FiLM: seq(dg=0.0002, db=0.0001, sat=0.0%) | latent(dg=0.0076, db=0.0045, sat=0.0%) | asset(dg=0.0008, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=11 (45.8%), medium_vol=6 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.039) | TAPE=0.2381
[CYCLE] Update 13/348 | Step 13,104/500,000 | Episode 16 | Time: 1285.0s
   📊 Metrics: Return=-5.93% | Sharpe=-0.652 | DD=12.61% | Turnover=29.47%
   🎚️ Intra-Step TAPE: potential=0.2391 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0564 | critic_loss=0.1675 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0837 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.6517 | ema=0.1800 | best_ema=0.1800 | no_improve=0
[CYCLE] Update 14/348 | Step 14,112/500,000 | Episode 16 | Time: 1382.3s
   📊 Metrics: Return=+0.27% | Sharpe=-0.024 | DD=12.61% | Turnover=29.66%
   🎚️ Intra-Step TAPE: potential=0.5485 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0539 | critic_loss=0.1184 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0592 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0289
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0245 | ema=0.1595 | best_ema=0.1595 | no_improve=0
   🔬 Alpha Diversity: mean=2.14 | std=1.27 | range=[0.94, 7.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=2.65 | KO=2.52 | XOM=2.46  BOT: CAT=1.47 | NVDA=1.34 | GLD=1.08
   🧬 FiLM: seq(dg=0.0002, db=0.0002, sat=0.0%) | latent(dg=0.0087, db=0.0051, sat=0.0%) | asset(dg=0.0009, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=11 (45.8%), medium_vol=6 (25.0%)
[CYCLE] Update 15/348 | Step 15,120/500,000 | Episode 16 | Time: 1479.5s
   📊 Metrics: Return=+0.24% | Sharpe=-0.053 | DD=12.61% | Turnover=29.97%
   🎚️ Intra-Step TAPE: potential=0.5909 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0557 | critic_loss=0.1423 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0712 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0292
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0526 | ema=0.1383 | best_ema=0.1383 | no_improve=0
[CYCLE] Update 16/348 | Step 16,128/500,000 | Episode 16 | Time: 1576.6s
   📊 Metrics: Return=+1.79% | Sharpe=-0.014 | DD=12.61% | Turnover=29.64%
   🎚️ Intra-Step TAPE: potential=0.4428 | delta_reward=+0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0524 | critic_loss=0.1034 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0517 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0288
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0136 | ema=0.1231 | best_ema=0.1231 | no_improve=0
   🔬 Alpha Diversity: mean=2.16 | std=1.27 | range=[0.94, 7.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=2.99 | KO=2.53 | XOM=2.32  BOT: NVDA=1.45 | AMZN=1.41 | GLD=1.07
   🧬 FiLM: seq(dg=0.0002, db=0.0002, sat=0.0%) | latent(dg=0.0095, db=0.0056, sat=0.0%) | asset(dg=0.0009, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=11 (45.8%), medium_vol=6 (25.0%)
[CYCLE] Update 17/348 | Step 17,136/500,000 | Episode 16 | Time: 1673.9s
   📊 Metrics: Return=+7.03% | Sharpe=0.122 | DD=12.61% | Turnover=29.82%
   🎚️ Intra-Step TAPE: potential=0.2611 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0521 | critic_loss=0.0826 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0413 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1215 | ema=0.1230 | best_ema=0.1230 | no_improve=0
[CYCLE] Update 18/348 | Step 18,144/500,000 | Episode 24 | Time: 1769.9s
   📊 Metrics: Return=+15.85% | Sharpe=0.297 | DD=12.75% | Turnover=29.50%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0526 | critic_loss=0.0734 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0367 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0285
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2972 | ema=0.1404 | best_ema=0.1404 | no_improve=0
   🔬 Alpha Diversity: mean=2.15 | std=1.35 | range=[0.94, 7.88] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=2.46 | MSFT=2.27 | XOM=2.21  BOT: NVDA=1.41 | AMZN=1.21 | GLD=1.07
   🧬 FiLM: seq(dg=0.0002, db=0.0002, sat=0.0%) | latent(dg=0.0102, db=0.0062, sat=0.0%) | asset(dg=0.0010, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=12 (37.5%), medium_vol=10 (31.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2696
[CYCLE] Update 19/348 | Step 19,152/500,000 | Episode 24 | Time: 1866.8s
   📊 Metrics: Return=+10.71% | Sharpe=0.914 | DD=13.10% | Turnover=30.87%
   🎚️ Intra-Step TAPE: potential=0.6820 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0472 | critic_loss=0.1032 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0516 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0289
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9139 | ema=0.2177 | best_ema=0.2177 | no_improve=0
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 1964.1s
   📊 Metrics: Return=+20.92% | Sharpe=1.040 | DD=13.10% | Turnover=30.43%
   🎚️ Intra-Step TAPE: potential=0.5675 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0502 | critic_loss=0.0395 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0197 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0291
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0399 | ema=0.3000 | best_ema=0.3000 | no_improve=0
   🔬 Alpha Diversity: mean=2.13 | std=1.25 | range=[0.94, 7.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=2.49 | MSFT=2.48 | XOM=2.41  BOT: GLD=1.27 | AMZN=1.15 | NVDA=1.10
   🧬 FiLM: seq(dg=0.0002, db=0.0002, sat=0.0%) | latent(dg=0.0109, db=0.0067, sat=0.0%) | asset(dg=0.0010, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=12 (37.5%), medium_vol=10 (31.2%)
[CYCLE] Update 21/348 | Step 21,168/500,000 | Episode 24 | Time: 2061.4s
   📊 Metrics: Return=+13.33% | Sharpe=0.461 | DD=13.10% | Turnover=30.21%
   🎚️ Intra-Step TAPE: potential=0.2413 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0486 | critic_loss=0.0393 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0197 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0288
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4612 | ema=0.3161 | best_ema=0.3161 | no_improve=0
[CYCLE] Update 22/348 | Step 22,176/500,000 | Episode 24 | Time: 2158.7s
   📊 Metrics: Return=+28.74% | Sharpe=0.769 | DD=13.10% | Turnover=30.07%
   🎚️ Intra-Step TAPE: potential=0.7481 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0503 | critic_loss=0.0213 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0106 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0286
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7687 | ema=0.3613 | best_ema=0.3613 | no_improve=0
   🔬 Alpha Diversity: mean=2.15 | std=1.35 | range=[0.94, 7.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=2.63 | KO=2.37 | XOM=2.34  BOT: AMZN=1.30 | NVDA=1.18 | GLD=1.09
   🧬 FiLM: seq(dg=0.0002, db=0.0002, sat=0.0%) | latent(dg=0.0115, db=0.0071, sat=0.0%) | asset(dg=0.0010, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=12 (37.5%), medium_vol=10 (31.2%)
[CYCLE] Update 23/348 | Step 23,184/500,000 | Episode 24 | Time: 2256.1s
   📊 Metrics: Return=+25.20% | Sharpe=0.553 | DD=13.10% | Turnover=30.21%
   🎚️ Intra-Step TAPE: potential=0.2303 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0486 | critic_loss=0.0274 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0137 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5529 | ema=0.3805 | best_ema=0.3805 | no_improve=0
[CYCLE] Update 24/348 | Step 24,192/500,000 | Episode 32 | Time: 2352.3s
   📊 Metrics: Return=+4.89% | Sharpe=0.016 | DD=14.03% | Turnover=30.31%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0483 | critic_loss=0.0308 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0154 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0276
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0160 | ema=0.3440 | best_ema=0.3440 | no_improve=0
   🔬 Alpha Diversity: mean=2.12 | std=1.61 | range=[0.94, 8.00] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=2.31 | XOM=2.12 | MSFT=2.10  BOT: CAT=1.19 | AMZN=1.16 | GLD=1.09
   🧬 FiLM: seq(dg=0.0002, db=0.0002, sat=0.0%) | latent(dg=0.0121, db=0.0074, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=11 (27.5%), low_vol=14 (35.0%), medium_vol=15 (37.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2467
[CYCLE] Update 25/348 | Step 25,200/500,000 | Episode 32 | Time: 2449.9s
   📊 Metrics: Return=+5.62% | Sharpe=1.610 | DD=1.98% | Turnover=31.32%
   🎚️ Intra-Step TAPE: potential=0.7289 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0460 | critic_loss=0.0273 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0136 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6097 | ema=0.4706 | best_ema=0.4706 | no_improve=0
[CYCLE] Update 26/348 | Step 26,208/500,000 | Episode 32 | Time: 2547.8s
   📊 Metrics: Return=+9.36% | Sharpe=1.229 | DD=2.11% | Turnover=30.53%
   🎚️ Intra-Step TAPE: potential=0.6659 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0437 | critic_loss=0.0195 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0097 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2285 | ema=0.5464 | best_ema=0.5464 | no_improve=0
   🔬 Alpha Diversity: mean=2.06 | std=1.91 | range=[0.94, 8.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.79 | MSFT=1.76 | KO=1.70  BOT: CAT=1.20 | NVDA=1.18 | GLD=1.11
   🧬 FiLM: seq(dg=0.0003, db=0.0003, sat=0.0%) | latent(dg=0.0129, db=0.0080, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=11 (27.5%), low_vol=14 (35.0%), medium_vol=15 (37.5%)
[CYCLE] Update 27/348 | Step 27,216/500,000 | Episode 32 | Time: 2645.4s
   📊 Metrics: Return=+12.83% | Sharpe=0.839 | DD=6.11% | Turnover=29.74%
   🎚️ Intra-Step TAPE: potential=0.2641 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0447 | critic_loss=0.0211 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0105 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8387 | ema=0.5756 | best_ema=0.5756 | no_improve=0
[CYCLE] Update 28/348 | Step 28,224/500,000 | Episode 32 | Time: 2743.3s
   📊 Metrics: Return=+7.63% | Sharpe=0.247 | DD=7.74% | Turnover=29.70%
   🎚️ Intra-Step TAPE: potential=0.2303 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0479 | critic_loss=0.0295 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0148 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2475 | ema=0.5428 | best_ema=0.5428 | no_improve=0
   🔬 Alpha Diversity: mean=2.04 | std=2.02 | range=[0.97, 8.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=1.70 | XOM=1.62 | MSFT=1.59  BOT: GLD=1.21 | NVDA=1.21 | AMZN=1.10
   🧬 FiLM: seq(dg=0.0003, db=0.0003, sat=0.0%) | latent(dg=0.0133, db=0.0084, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=11 (27.5%), low_vol=14 (35.0%), medium_vol=15 (37.5%)
[CYCLE] Update 29/348 | Step 29,232/500,000 | Episode 32 | Time: 2841.4s
   📊 Metrics: Return=+8.03% | Sharpe=0.172 | DD=14.16% | Turnover=29.54%
   🎚️ Intra-Step TAPE: potential=0.2524 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0338 | critic_loss=0.0324 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0162 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1722 | ema=0.5058 | best_ema=0.5058 | no_improve=0
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 2938.3s
   📊 Metrics: Return=+2.14% | Sharpe=-0.117 | DD=10.55% | Turnover=29.66%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0442 | critic_loss=0.0371 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0186 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1174 | ema=0.4434 | best_ema=0.4434 | no_improve=0
   🔬 Alpha Diversity: mean=2.04 | std=1.99 | range=[0.95, 8.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.70 | KO=1.69 | MSFT=1.53  BOT: AMZN=1.24 | NVDA=1.20 | GLD=1.19
   🧬 FiLM: seq(dg=0.0003, db=0.0004, sat=0.0%) | latent(dg=0.0134, db=0.0086, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=14 (29.2%), low_vol=15 (31.2%), medium_vol=19 (39.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2451
[CYCLE] Update 31/348 | Step 31,248/500,000 | Episode 40 | Time: 3036.2s
   📊 Metrics: Return=-0.91% | Sharpe=-0.224 | DD=11.25% | Turnover=29.62%
   🎚️ Intra-Step TAPE: potential=0.5962 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0465 | critic_loss=0.0566 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0283 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2240 | ema=0.3767 | best_ema=0.3767 | no_improve=0
[CYCLE] Update 32/348 | Step 32,256/500,000 | Episode 40 | Time: 3134.4s
   📊 Metrics: Return=+9.61% | Sharpe=0.704 | DD=11.25% | Turnover=29.24%
   🎚️ Intra-Step TAPE: potential=0.2639 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0424 | critic_loss=0.0221 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0110 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0237
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7041 | ema=0.4094 | best_ema=0.4094 | no_improve=0
   🔬 Alpha Diversity: mean=2.03 | std=2.02 | range=[0.95, 8.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=1.68 | XOM=1.66 | MSFT=1.61  BOT: AMZN=1.19 | CAT=1.17 | NVDA=1.06
   🧬 FiLM: seq(dg=0.0003, db=0.0004, sat=0.0%) | latent(dg=0.0136, db=0.0085, sat=0.0%) | asset(dg=0.0011, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=14 (29.2%), low_vol=15 (31.2%), medium_vol=19 (39.6%)
[CYCLE] Update 33/348 | Step 33,264/500,000 | Episode 40 | Time: 3231.8s
   📊 Metrics: Return=+3.39% | Sharpe=0.083 | DD=13.64% | Turnover=29.47%
   🎚️ Intra-Step TAPE: potential=0.2473 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0451 | critic_loss=0.0166 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0235
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0832 | ema=0.3768 | best_ema=0.3768 | no_improve=0
[CYCLE] Update 34/348 | Step 34,272/500,000 | Episode 40 | Time: 3329.3s
   📊 Metrics: Return=+3.15% | Sharpe=0.027 | DD=13.64% | Turnover=29.44%
   🎚️ Intra-Step TAPE: potential=0.2570 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0458 | critic_loss=0.0121 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0230
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0269 | ema=0.3418 | best_ema=0.3418 | no_improve=0
   🔬 Alpha Diversity: mean=2.02 | std=2.07 | range=[0.96, 8.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.61 | KO=1.56 | XOM=1.53  BOT: GLD=1.23 | CAT=1.21 | NVDA=1.10
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0140, db=0.0087, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=14 (29.2%), low_vol=15 (31.2%), medium_vol=19 (39.6%)
[CYCLE] Update 35/348 | Step 35,280/500,000 | Episode 40 | Time: 3426.5s
   📊 Metrics: Return=-0.57% | Sharpe=-0.131 | DD=13.64% | Turnover=29.17%
   🎚️ Intra-Step TAPE: potential=0.2462 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0430 | critic_loss=0.0116 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1307 | ema=0.2946 | best_ema=0.2946 | no_improve=0
[CYCLE] Update 36/348 | Step 36,288/500,000 | Episode 48 | Time: 3522.3s
   📊 Metrics: Return=+14.72% | Sharpe=0.260 | DD=13.52% | Turnover=29.13%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0429 | critic_loss=0.0280 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0140 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2601 | ema=0.2911 | best_ema=0.2911 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=2.12 | range=[1.01, 8.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.49 | MSFT=1.48 | KO=1.48  BOT: GLD=1.23 | AMZN=1.21 | CAT=1.19
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0143, db=0.0090, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (28.6%), low_vol=19 (33.9%), medium_vol=21 (37.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2652
[CYCLE] Update 37/348 | Step 37,296/500,000 | Episode 48 | Time: 3619.3s
   📊 Metrics: Return=+7.65% | Sharpe=1.550 | DD=4.87% | Turnover=29.12%
   🎚️ Intra-Step TAPE: potential=0.2318 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0379 | critic_loss=0.0219 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0110 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5500 | ema=0.4170 | best_ema=0.4170 | no_improve=0
[CYCLE] Update 38/348 | Step 38,304/500,000 | Episode 48 | Time: 3716.5s
   📊 Metrics: Return=+5.53% | Sharpe=0.324 | DD=10.20% | Turnover=29.15%
   🎚️ Intra-Step TAPE: potential=0.5422 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0442 | critic_loss=0.0190 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3239 | ema=0.4077 | best_ema=0.4077 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.13 | range=[1.04, 8.80] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.47 | KO=1.45 | BRK-B=1.42  BOT: CAT=1.22 | AMZN=1.21 | GLD=1.20
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0144, db=0.0091, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (28.6%), low_vol=19 (33.9%), medium_vol=21 (37.5%)
[CYCLE] Update 39/348 | Step 39,312/500,000 | Episode 48 | Time: 3813.7s
   📊 Metrics: Return=+8.04% | Sharpe=0.323 | DD=10.20% | Turnover=29.16%
   🎚️ Intra-Step TAPE: potential=0.2509 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0448 | critic_loss=0.0151 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0076 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0221
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3226 | ema=0.3992 | best_ema=0.3992 | no_improve=0
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 48 | Time: 3910.7s
   📊 Metrics: Return=+3.83% | Sharpe=0.048 | DD=10.20% | Turnover=29.08%
   🎚️ Intra-Step TAPE: potential=0.2296 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0368 | critic_loss=0.0189 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0479 | ema=0.3641 | best_ema=0.3641 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.15 | range=[1.08, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.41 | KO=1.40 | MSFT=1.38  BOT: NVDA=1.25 | GLD=1.24 | AMZN=1.22
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0149, db=0.0095, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (28.6%), low_vol=19 (33.9%), medium_vol=21 (37.5%)
[CYCLE] Update 41/348 | Step 41,328/500,000 | Episode 48 | Time: 4007.9s
   📊 Metrics: Return=+8.46% | Sharpe=0.173 | DD=10.20% | Turnover=28.83%
   🎚️ Intra-Step TAPE: potential=0.4945 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0399 | critic_loss=0.0230 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0115 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1725 | ema=0.3449 | best_ema=0.3449 | no_improve=0
[CYCLE] Update 42/348 | Step 42,336/500,000 | Episode 56 | Time: 4103.6s
   📊 Metrics: Return=-0.17% | Sharpe=-0.152 | DD=13.73% | Turnover=29.76%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0405 | critic_loss=0.0426 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0213 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1523 | ema=0.2952 | best_ema=0.2952 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.15 | range=[1.08, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=1.40 | XOM=1.38 | MSFT=1.38  BOT: CAT=1.27 | NVDA=1.25 | GLD=1.21
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0153, db=0.0097, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=23 (35.9%), medium_vol=23 (35.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2388
[CYCLE] Update 43/348 | Step 43,344/500,000 | Episode 56 | Time: 4200.9s
   📊 Metrics: Return=+1.32% | Sharpe=0.128 | DD=4.94% | Turnover=29.58%
   🎚️ Intra-Step TAPE: potential=0.2459 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0368 | critic_loss=0.0366 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0183 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1281 | ema=0.2785 | best_ema=0.2785 | no_improve=0
[CYCLE] Update 44/348 | Step 44,352/500,000 | Episode 56 | Time: 4298.4s
   📊 Metrics: Return=+0.07% | Sharpe=-0.219 | DD=6.81% | Turnover=29.29%
   🎚️ Intra-Step TAPE: potential=0.2772 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0432 | critic_loss=0.0130 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0065 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2185 | ema=0.2288 | best_ema=0.2288 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.14 | range=[1.01, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.42 | KO=1.40 | BRK-B=1.37  BOT: NVDA=1.24 | AMZN=1.23 | GLD=1.22
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0153, db=0.0096, sat=0.0%) | asset(dg=0.0012, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=23 (35.9%), medium_vol=23 (35.9%)
[CYCLE] Update 45/348 | Step 45,360/500,000 | Episode 56 | Time: 4395.4s
   📊 Metrics: Return=-1.51% | Sharpe=-0.318 | DD=11.69% | Turnover=29.30%
   🎚️ Intra-Step TAPE: potential=0.6221 | delta_reward=+0.0025
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0397 | critic_loss=0.0129 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0064 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3176 | ema=0.1741 | best_ema=0.1741 | no_improve=0
[CYCLE] Update 46/348 | Step 46,368/500,000 | Episode 56 | Time: 4492.3s
   📊 Metrics: Return=-0.32% | Sharpe=-0.202 | DD=11.69% | Turnover=29.19%
   🎚️ Intra-Step TAPE: potential=0.6627 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0375 | critic_loss=0.0137 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0069 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2024 | ema=0.1365 | best_ema=0.1365 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.15 | range=[1.08, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: XOM=1.39 | KO=1.39 | MSFT=1.38  BOT: CAT=1.25 | AMZN=1.24 | GLD=1.22
   🧬 FiLM: seq(dg=0.0004, db=0.0004, sat=0.0%) | latent(dg=0.0150, db=0.0094, sat=0.0%) | asset(dg=0.0013, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=23 (35.9%), medium_vol=23 (35.9%)
[CYCLE] Update 47/348 | Step 47,376/500,000 | Episode 56 | Time: 4589.1s
   📊 Metrics: Return=+4.58% | Sharpe=0.019 | DD=11.69% | Turnover=29.07%
   🎚️ Intra-Step TAPE: potential=0.3068 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0387 | critic_loss=0.0130 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0065 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0193 | ema=0.1248 | best_ema=0.1248 | no_improve=0
[CYCLE] Update 48/348 | Step 48,384/500,000 | Episode 64 | Time: 4685.2s
   📊 Metrics: Return=+1.28% | Sharpe=-0.149 | DD=11.42% | Turnover=29.38%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0373 | critic_loss=0.0279 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0140 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1488 | ema=0.0974 | best_ema=0.0974 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.16 | range=[1.14, 8.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.39 | KO=1.36 | XOM=1.34  BOT: CAT=1.25 | GLD=1.25 | NVDA=1.24
   🧬 FiLM: seq(dg=0.0005, db=0.0004, sat=0.0%) | latent(dg=0.0156, db=0.0098, sat=0.0%) | asset(dg=0.0013, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=20 (27.8%), low_vol=29 (40.3%), medium_vol=23 (31.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2416
[CYCLE] Update 49/348 | Step 49,392/500,000 | Episode 64 | Time: 4782.3s
   📊 Metrics: Return=-7.30% | Sharpe=-2.190 | DD=7.41% | Turnover=30.00%
   🎚️ Intra-Step TAPE: potential=0.2439 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0385 | critic_loss=0.0206 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0103 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-2.1899 | ema=-0.1313 | best_ema=-0.1313 | no_improve=0
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 4880.1s
   📊 Metrics: Return=-5.49% | Sharpe=-0.989 | DD=8.01% | Turnover=29.35%
   🎚️ Intra-Step TAPE: potential=0.2987 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0377 | critic_loss=0.0170 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0085 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.9888 | ema=-0.2171 | best_ema=-0.2171 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.16 | range=[1.17, 8.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.36 | AMZN=1.36 | KO=1.31  BOT: CAT=1.28 | NEE=1.28 | GLD=1.26
   🧬 FiLM: seq(dg=0.0005, db=0.0004, sat=0.0%) | latent(dg=0.0165, db=0.0104, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=20 (27.8%), low_vol=29 (40.3%), medium_vol=23 (31.9%)
[CYCLE] Update 51/348 | Step 51,408/500,000 | Episode 64 | Time: 4977.3s
   📊 Metrics: Return=-8.74% | Sharpe=-0.848 | DD=11.10% | Turnover=29.40%
   🎚️ Intra-Step TAPE: potential=0.2421 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0365 | critic_loss=0.0156 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0078 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.8479 | ema=-0.2802 | best_ema=-0.2802 | no_improve=0
[CYCLE] Update 52/348 | Step 52,416/500,000 | Episode 64 | Time: 5074.3s
   📊 Metrics: Return=-1.48% | Sharpe=-0.259 | DD=11.10% | Turnover=29.42%
   🎚️ Intra-Step TAPE: potential=0.5269 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0399 | critic_loss=0.0176 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0088 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2593 | ema=-0.2781 | best_ema=-0.2781 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.16 | range=[1.14, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.38 | AMZN=1.36 | JPM=1.32  BOT: BRK-B=1.29 | NEE=1.27 | GLD=1.24
   🧬 FiLM: seq(dg=0.0005, db=0.0004, sat=0.0%) | latent(dg=0.0161, db=0.0102, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=20 (27.8%), low_vol=29 (40.3%), medium_vol=23 (31.9%)
[CYCLE] Update 53/348 | Step 53,424/500,000 | Episode 64 | Time: 5171.6s
   📊 Metrics: Return=+2.73% | Sharpe=-0.063 | DD=11.10% | Turnover=29.56%
   🎚️ Intra-Step TAPE: potential=0.7187 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0306 | critic_loss=0.0215 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0627 | ema=-0.2565 | best_ema=-0.2565 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00072_shp0p924_actor.weights.h5 (Sharpe=0.924, MDD=7.06%)
[CYCLE] Update 54/348 | Step 54,432/500,000 | Episode 72 | Time: 5268.1s
   📊 Metrics: Return=+32.96% | Sharpe=0.924 | DD=7.06% | Turnover=29.24%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0383 | critic_loss=0.0307 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0153 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9245 | ema=-0.1384 | best_ema=-0.1384 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.05, 8.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.45 | AMZN=1.37 | KO=1.33  BOT: BRK-B=1.28 | CAT=1.26 | GLD=1.25
   🧬 FiLM: seq(dg=0.0005, db=0.0004, sat=0.0%) | latent(dg=0.0155, db=0.0097, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=32 (40.0%), medium_vol=24 (30.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5038
[CYCLE] Update 55/348 | Step 55,440/500,000 | Episode 72 | Time: 5365.3s
   📊 Metrics: Return=+13.02% | Sharpe=3.467 | DD=1.58% | Turnover=29.73%
   🎚️ Intra-Step TAPE: potential=0.7330 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0407 | critic_loss=0.0182 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0091 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.4668 | ema=0.2221 | best_ema=0.2221 | no_improve=0
[CYCLE] Update 56/348 | Step 56,448/500,000 | Episode 72 | Time: 5463.1s
   📊 Metrics: Return=+17.71% | Sharpe=2.150 | DD=2.14% | Turnover=29.09%
   🎚️ Intra-Step TAPE: potential=0.6536 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0332 | critic_loss=0.0102 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0051 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1504 | ema=0.4149 | best_ema=0.4149 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.07, 8.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.39 | JPM=1.38 | AMZN=1.37  BOT: CAT=1.29 | NEE=1.27 | GLD=1.17
   🧬 FiLM: seq(dg=0.0005, db=0.0004, sat=0.0%) | latent(dg=0.0158, db=0.0099, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=32 (40.0%), medium_vol=24 (30.0%)
[CYCLE] Update 57/348 | Step 57,456/500,000 | Episode 72 | Time: 5561.5s
   📊 Metrics: Return=+25.40% | Sharpe=2.127 | DD=2.14% | Turnover=29.30%
   🎚️ Intra-Step TAPE: potential=0.6599 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0405 | critic_loss=0.0120 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1269 | ema=0.5861 | best_ema=0.5861 | no_improve=0
[CYCLE] Update 58/348 | Step 58,464/500,000 | Episode 72 | Time: 5659.3s
   📊 Metrics: Return=+31.69% | Sharpe=1.790 | DD=6.41% | Turnover=29.10%
   🎚️ Intra-Step TAPE: potential=0.2302 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0419 | critic_loss=0.0227 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0113 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7903 | ema=0.7065 | best_ema=0.7065 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.08, 8.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=1.46 | AMZN=1.38 | NVDA=1.33  BOT: XOM=1.29 | BRK-B=1.27 | GLD=1.18
   🧬 FiLM: seq(dg=0.0005, db=0.0005, sat=0.0%) | latent(dg=0.0162, db=0.0100, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=32 (40.0%), medium_vol=24 (30.0%)
[CYCLE] Update 59/348 | Step 59,472/500,000 | Episode 72 | Time: 5757.2s
   📊 Metrics: Return=+34.76% | Sharpe=1.415 | DD=6.67% | Turnover=29.11%
   🎚️ Intra-Step TAPE: potential=0.5433 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0454 | critic_loss=0.0116 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4152 | ema=0.7774 | best_ema=0.7774 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp0p816_actor.weights.h5 (Sharpe=0.816, MDD=12.79%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 5853.8s
   📊 Metrics: Return=+19.20% | Sharpe=0.500 | DD=14.81% | Turnover=28.89%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0352 | critic_loss=0.0247 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0124 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5002 | ema=0.7497 | best_ema=0.7497 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.14, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.45 | AMZN=1.42 | MSFT=1.39  BOT: CAT=1.25 | NEE=1.24 | GLD=1.22
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0170, db=0.0104, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=36 (40.9%), medium_vol=26 (29.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2918
[CYCLE] Update 61/348 | Step 61,488/500,000 | Episode 80 | Time: 5951.8s
   📊 Metrics: Return=-3.20% | Sharpe=-0.593 | DD=10.84% | Turnover=29.67%
   🎚️ Intra-Step TAPE: potential=0.2849 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0381 | critic_loss=0.0148 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0074 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5926 | ema=0.6155 | best_ema=0.6155 | no_improve=0
[CYCLE] Update 62/348 | Step 62,496/500,000 | Episode 80 | Time: 6049.2s
   📊 Metrics: Return=+7.11% | Sharpe=0.503 | DD=10.84% | Turnover=29.01%
   🎚️ Intra-Step TAPE: potential=0.6999 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0384 | critic_loss=0.0159 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0079 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5026 | ema=0.6042 | best_ema=0.6042 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.13, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.43 | NVDA=1.39 | MSFT=1.38  BOT: KO=1.25 | NEE=1.24 | GLD=1.21
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0178, db=0.0110, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=36 (40.9%), medium_vol=26 (29.5%)
[CYCLE] Update 63/348 | Step 63,504/500,000 | Episode 80 | Time: 6146.9s
   📊 Metrics: Return=+3.53% | Sharpe=0.088 | DD=10.85% | Turnover=29.57%
   🎚️ Intra-Step TAPE: potential=0.2702 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0406 | critic_loss=0.0114 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0057 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0876 | ema=0.5525 | best_ema=0.5525 | no_improve=0
[CYCLE] Update 64/348 | Step 64,512/500,000 | Episode 80 | Time: 6244.3s
   📊 Metrics: Return=+4.46% | Sharpe=0.079 | DD=13.13% | Turnover=29.70%
   🎚️ Intra-Step TAPE: potential=0.4945 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0402 | critic_loss=0.0088 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0044 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0787 | ema=0.5051 | best_ema=0.5051 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.16 | range=[1.19, 8.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.38 | NVDA=1.36 | MSFT=1.35  BOT: KO=1.26 | GLD=1.25 | NEE=1.24
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0180, db=0.0111, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=36 (40.9%), medium_vol=26 (29.5%)
[CYCLE] Update 65/348 | Step 65,520/500,000 | Episode 80 | Time: 6341.6s
   📊 Metrics: Return=+4.77% | Sharpe=0.049 | DD=13.13% | Turnover=29.47%
   🎚️ Intra-Step TAPE: potential=0.5646 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0366 | critic_loss=0.0073 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0036 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0494 | ema=0.4596 | best_ema=0.4596 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00082_shp0p852_actor.weights.h5 (Sharpe=0.852, MDD=8.12%)
[CYCLE] Update 66/348 | Step 66,528/500,000 | Episode 88 | Time: 6437.9s
   📊 Metrics: Return=+12.84% | Sharpe=0.303 | DD=13.13% | Turnover=29.60%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0421 | critic_loss=0.0141 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0070 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3028 | ema=0.4439 | best_ema=0.4439 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.18, 8.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.45 | AMZN=1.41 | MSFT=1.33  BOT: XOM=1.26 | KO=1.25 | NEE=1.24
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0183, db=0.0112, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (31.2%), low_vol=40 (41.7%), medium_vol=26 (27.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2732
[CYCLE] Update 67/348 | Step 67,536/500,000 | Episode 88 | Time: 6535.3s
   📊 Metrics: Return=+4.27% | Sharpe=0.669 | DD=4.88% | Turnover=29.12%
   🎚️ Intra-Step TAPE: potential=0.2548 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0386 | critic_loss=0.0143 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0072 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6695 | ema=0.4664 | best_ema=0.4664 | no_improve=0
[CYCLE] Update 68/348 | Step 68,544/500,000 | Episode 88 | Time: 6633.0s
   📊 Metrics: Return=+4.60% | Sharpe=0.305 | DD=6.62% | Turnover=29.42%
   🎚️ Intra-Step TAPE: potential=0.2372 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0341 | critic_loss=0.0074 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0037 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3049 | ema=0.4503 | best_ema=0.4503 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.16, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.45 | JPM=1.39 | AMZN=1.36  BOT: BRK-B=1.26 | KO=1.23 | NEE=1.21
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0181, db=0.0113, sat=0.0%) | asset(dg=0.0015, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (31.2%), low_vol=40 (41.7%), medium_vol=26 (27.1%)
[CYCLE] Update 69/348 | Step 69,552/500,000 | Episode 88 | Time: 6730.7s
   📊 Metrics: Return=+9.36% | Sharpe=0.486 | DD=6.62% | Turnover=29.59%
   🎚️ Intra-Step TAPE: potential=0.5862 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0393 | critic_loss=0.0098 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0049 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4864 | ema=0.4539 | best_ema=0.4539 | no_improve=0
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 88 | Time: 6828.2s
   📊 Metrics: Return=+7.99% | Sharpe=0.261 | DD=6.62% | Turnover=29.68%
   🎚️ Intra-Step TAPE: potential=0.3127 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0413 | critic_loss=0.0081 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2606 | ema=0.4346 | best_ema=0.4346 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.17, 8.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.50 | AMZN=1.41 | MSFT=1.36  BOT: XOM=1.24 | KO=1.23 | NEE=1.22
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0172, db=0.0109, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (31.2%), low_vol=40 (41.7%), medium_vol=26 (27.1%)
[CYCLE] Update 71/348 | Step 71,568/500,000 | Episode 88 | Time: 6926.0s
   📊 Metrics: Return=+9.12% | Sharpe=0.225 | DD=6.62% | Turnover=29.75%
   🎚️ Intra-Step TAPE: potential=0.2320 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0365 | critic_loss=0.0116 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2253 | ema=0.4136 | best_ema=0.4136 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00091_shp0p906_actor.weights.h5 (Sharpe=0.906, MDD=7.24%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00095_shp0p970_actor.weights.h5 (Sharpe=0.970, MDD=6.71%)
[CYCLE] Update 72/348 | Step 72,576/500,000 | Episode 96 | Time: 7023.4s
   📊 Metrics: Return=+3.31% | Sharpe=-0.071 | DD=12.59% | Turnover=29.35%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0331 | critic_loss=0.0498 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0249 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0709 | ema=0.3652 | best_ema=0.3652 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.15 | range=[1.18, 8.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.47 | AMZN=1.40 | MSFT=1.36  BOT: KO=1.25 | GLD=1.23 | NEE=1.22
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0168, db=0.0109, sat=0.0%) | asset(dg=0.0014, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=32 (30.8%), low_vol=44 (42.3%), medium_vol=28 (26.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2406
[CYCLE] Update 73/348 | Step 73,584/500,000 | Episode 96 | Time: 7121.0s
   📊 Metrics: Return=+8.12% | Sharpe=2.489 | DD=1.82% | Turnover=28.71%
   🎚️ Intra-Step TAPE: potential=0.7473 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0349 | critic_loss=0.0194 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0097 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4889 | ema=0.5776 | best_ema=0.5776 | no_improve=0
[CYCLE] Update 74/348 | Step 74,592/500,000 | Episode 96 | Time: 7219.0s
   📊 Metrics: Return=+16.06% | Sharpe=2.321 | DD=1.82% | Turnover=28.75%
   🎚️ Intra-Step TAPE: potential=0.7560 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0351 | critic_loss=0.0133 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3209 | ema=0.7519 | best_ema=0.7519 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.14 | range=[1.15, 8.80] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.56 | AMZN=1.43 | MSFT=1.36  BOT: XOM=1.24 | KO=1.22 | NEE=1.21
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0173, db=0.0111, sat=0.0%) | asset(dg=0.0015, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=32 (30.8%), low_vol=44 (42.3%), medium_vol=28 (26.9%)
[CYCLE] Update 75/348 | Step 75,600/500,000 | Episode 96 | Time: 7316.8s
   📊 Metrics: Return=+22.00% | Sharpe=1.456 | DD=6.24% | Turnover=29.22%
   🎚️ Intra-Step TAPE: potential=0.2353 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0411 | critic_loss=0.0128 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0064 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4558 | ema=0.8223 | best_ema=0.8223 | no_improve=0
[CYCLE] Update 76/348 | Step 76,608/500,000 | Episode 96 | Time: 7414.4s
   📊 Metrics: Return=+14.72% | Sharpe=0.601 | DD=9.38% | Turnover=29.19%
   🎚️ Intra-Step TAPE: potential=0.2328 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0364 | critic_loss=0.0109 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6006 | ema=0.8001 | best_ema=0.8001 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.12 | range=[1.10, 8.78] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.64 | AMZN=1.55 | CAT=1.39  BOT: XOM=1.20 | KO=1.17 | NEE=1.16
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0172, db=0.0111, sat=0.0%) | asset(dg=0.0015, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=32 (30.8%), low_vol=44 (42.3%), medium_vol=28 (26.9%)
[CYCLE] Update 77/348 | Step 77,616/500,000 | Episode 96 | Time: 7512.1s
   📊 Metrics: Return=+19.52% | Sharpe=0.603 | DD=14.16% | Turnover=29.11%
   🎚️ Intra-Step TAPE: potential=0.3974 | delta_reward=-0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0350 | critic_loss=0.0147 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0074 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6032 | ema=0.7804 | best_ema=0.7804 | no_improve=0
[CYCLE] Update 78/348 | Step 78,624/500,000 | Episode 104 | Time: 7608.3s
   📊 Metrics: Return=+8.42% | Sharpe=0.128 | DD=11.55% | Turnover=29.19%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0398 | critic_loss=0.0202 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0101 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1277 | ema=0.7152 | best_ema=0.7152 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.13 | range=[1.11, 8.78] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.67 | AMZN=1.50 | CAT=1.35  BOT: XOM=1.21 | KO=1.19 | NEE=1.18
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0172, db=0.0110, sat=0.0%) | asset(dg=0.0015, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (31.2%), low_vol=46 (41.1%), medium_vol=31 (27.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2535
[CYCLE] Update 79/348 | Step 79,632/500,000 | Episode 104 | Time: 7705.8s
   📊 Metrics: Return=-3.92% | Sharpe=-0.705 | DD=10.88% | Turnover=30.85%
   🎚️ Intra-Step TAPE: potential=0.2488 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0381 | critic_loss=0.0127 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0063 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.7050 | ema=0.5731 | best_ema=0.5731 | no_improve=0
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 7803.8s
   📊 Metrics: Return=+9.29% | Sharpe=0.674 | DD=10.88% | Turnover=29.98%
   🎚️ Intra-Step TAPE: potential=0.7060 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0420 | critic_loss=0.0062 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6744 | ema=0.5833 | best_ema=0.5833 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.13 | range=[1.10, 8.78] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.55 | AMZN=1.52 | CAT=1.38  BOT: XOM=1.21 | KO=1.18 | NEE=1.16
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0178, db=0.0114, sat=0.0%) | asset(dg=0.0015, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (31.2%), low_vol=46 (41.1%), medium_vol=31 (27.7%)
[CYCLE] Update 81/348 | Step 81,648/500,000 | Episode 104 | Time: 7901.4s
   📊 Metrics: Return=-2.18% | Sharpe=-0.221 | DD=15.36% | Turnover=29.65%
   🎚️ Intra-Step TAPE: potential=0.2274 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0389 | critic_loss=0.0115 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2206 | ema=0.5029 | best_ema=0.5029 | no_improve=0
[CYCLE] Update 82/348 | Step 82,656/500,000 | Episode 104 | Time: 7999.3s
   📊 Metrics: Return=+1.93% | Sharpe=-0.016 | DD=15.81% | Turnover=29.97%
   🎚️ Intra-Step TAPE: potential=0.2525 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0410 | critic_loss=0.0064 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0032 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0163 | ema=0.4510 | best_ema=0.4510 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.11 | range=[1.08, 8.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.77 | AMZN=1.43 | CAT=1.35  BOT: XOM=1.19 | NEE=1.17 | KO=1.17
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0183, db=0.0117, sat=0.0%) | asset(dg=0.0015, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (31.2%), low_vol=46 (41.1%), medium_vol=31 (27.7%)
[CYCLE] Update 83/348 | Step 83,664/500,000 | Episode 104 | Time: 8097.3s
   📊 Metrics: Return=-0.93% | Sharpe=-0.133 | DD=15.81% | Turnover=29.77%
   🎚️ Intra-Step TAPE: potential=0.2743 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0406 | critic_loss=0.0059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0030 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1332 | ema=0.3925 | best_ema=0.3925 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00108_shp1p282_actor.weights.h5 (Sharpe=1.282, MDD=6.49%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00111_shp1p245_actor.weights.h5 (Sharpe=1.245, MDD=6.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00112_shp0p878_actor.weights.h5 (Sharpe=0.878, MDD=7.29%)
[CYCLE] Update 84/348 | Step 84,672/500,000 | Episode 112 | Time: 8194.7s
   📊 Metrics: Return=+32.43% | Sharpe=0.878 | DD=7.29% | Turnover=29.19%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0342 | critic_loss=0.0362 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0181 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8781 | ema=0.4411 | best_ema=0.4411 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.11 | range=[1.09, 8.77] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.72 | NVDA=1.64 | MSFT=1.36  BOT: XOM=1.18 | KO=1.18 | NEE=1.16
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0178, db=0.0115, sat=0.0%) | asset(dg=0.0015, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=36 (30.0%), low_vol=51 (42.5%), medium_vol=33 (27.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4633
[CYCLE] Update 85/348 | Step 85,680/500,000 | Episode 112 | Time: 8292.1s
   📊 Metrics: Return=-0.60% | Sharpe=-0.385 | DD=3.31% | Turnover=30.31%
   🎚️ Intra-Step TAPE: potential=0.2331 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0368 | critic_loss=0.0080 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3848 | ema=0.3585 | best_ema=0.3585 | no_improve=0
[CYCLE] Update 86/348 | Step 86,688/500,000 | Episode 112 | Time: 8389.9s
   📊 Metrics: Return=+3.37% | Sharpe=0.215 | DD=3.70% | Turnover=29.89%
   🎚️ Intra-Step TAPE: potential=0.2786 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0362 | critic_loss=0.0074 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0037 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2146 | ema=0.3441 | best_ema=0.3441 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.13 | range=[1.12, 8.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.56 | AMZN=1.50 | MSFT=1.35  BOT: XOM=1.21 | KO=1.19 | NEE=1.19
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0177, db=0.0114, sat=0.0%) | asset(dg=0.0016, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=36 (30.0%), low_vol=51 (42.5%), medium_vol=33 (27.5%)
[CYCLE] Update 87/348 | Step 87,696/500,000 | Episode 112 | Time: 8487.8s
   📊 Metrics: Return=+4.76% | Sharpe=0.191 | DD=4.29% | Turnover=30.22%
   🎚️ Intra-Step TAPE: potential=0.4053 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0388 | critic_loss=0.0083 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0042 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1913 | ema=0.3288 | best_ema=0.3288 | no_improve=0
[CYCLE] Update 88/348 | Step 88,704/500,000 | Episode 112 | Time: 8585.6s
   📊 Metrics: Return=+3.52% | Sharpe=0.004 | DD=6.90% | Turnover=29.95%
   🎚️ Intra-Step TAPE: potential=0.2425 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0372 | critic_loss=0.0117 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0059 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0036 | ema=0.2963 | best_ema=0.2963 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.13 | range=[1.14, 8.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.59 | AMZN=1.48 | MSFT=1.39  BOT: XOM=1.22 | NEE=1.21 | KO=1.21
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0163, db=0.0108, sat=0.0%) | asset(dg=0.0016, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=36 (30.0%), low_vol=51 (42.5%), medium_vol=33 (27.5%)
[CYCLE] Update 89/348 | Step 89,712/500,000 | Episode 112 | Time: 8683.4s
   📊 Metrics: Return=+2.38% | Sharpe=-0.105 | DD=6.90% | Turnover=29.95%
   🎚️ Intra-Step TAPE: potential=0.2493 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0370 | critic_loss=0.0068 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1049 | ema=0.2562 | best_ema=0.2562 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00115_shp0p730_actor.weights.h5 (Sharpe=0.730, MDD=9.93%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00118_shp1p216_actor.weights.h5 (Sharpe=1.216, MDD=6.43%)
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 8780.6s
   📊 Metrics: Return=+16.52% | Sharpe=0.408 | DD=11.21% | Turnover=29.29%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0374 | critic_loss=0.0204 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0102 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4080 | ema=0.2714 | best_ema=0.2714 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.12 | range=[1.09, 8.78] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.70 | AMZN=1.51 | MSFT=1.41  BOT: KO=1.21 | NEE=1.21 | GLD=1.17
   🧬 FiLM: seq(dg=0.0006, db=0.0004, sat=0.0%) | latent(dg=0.0164, db=0.0108, sat=0.0%) | asset(dg=0.0016, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=39 (30.5%), low_vol=53 (41.4%), medium_vol=36 (28.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2929
[CYCLE] Update 91/348 | Step 91,728/500,000 | Episode 120 | Time: 8877.9s
   📊 Metrics: Return=-3.22% | Sharpe=-0.818 | DD=9.47% | Turnover=30.43%
   🎚️ Intra-Step TAPE: potential=0.2359 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0373 | critic_loss=0.0107 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.8181 | ema=0.1624 | best_ema=0.1624 | no_improve=0
[CYCLE] Update 92/348 | Step 92,736/500,000 | Episode 120 | Time: 8975.9s
   📊 Metrics: Return=+5.35% | Sharpe=0.369 | DD=9.47% | Turnover=30.02%
   🎚️ Intra-Step TAPE: potential=0.7402 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0395 | critic_loss=0.0093 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3686 | ema=0.1830 | best_ema=0.1830 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.14 | range=[1.03, 8.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.48 | MSFT=1.40 | NVDA=1.37  BOT: NEE=1.23 | KO=1.22 | GLD=1.17
   🧬 FiLM: seq(dg=0.0005, db=0.0004, sat=0.0%) | latent(dg=0.0164, db=0.0109, sat=0.0%) | asset(dg=0.0016, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=39 (30.5%), low_vol=53 (41.4%), medium_vol=36 (28.1%)
[CYCLE] Update 93/348 | Step 93,744/500,000 | Episode 120 | Time: 9074.0s
   📊 Metrics: Return=+8.10% | Sharpe=0.393 | DD=9.47% | Turnover=29.70%
   🎚️ Intra-Step TAPE: potential=0.2325 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0422 | critic_loss=0.0081 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3928 | ema=0.2040 | best_ema=0.2040 | no_improve=0
[CYCLE] Update 94/348 | Step 94,752/500,000 | Episode 120 | Time: 9171.5s
   📊 Metrics: Return=+15.82% | Sharpe=0.668 | DD=9.47% | Turnover=29.75%
   🎚️ Intra-Step TAPE: potential=0.2448 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0407 | critic_loss=0.0061 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6684 | ema=0.2504 | best_ema=0.2504 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.14 | range=[1.04, 8.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=1.43 | MSFT=1.40 | NVDA=1.40  BOT: NEE=1.24 | KO=1.23 | GLD=1.17
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0183, db=0.0119, sat=0.0%) | asset(dg=0.0017, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=39 (30.5%), low_vol=53 (41.4%), medium_vol=36 (28.1%)
[CYCLE] Update 95/348 | Step 95,760/500,000 | Episode 120 | Time: 9269.1s
   📊 Metrics: Return=+24.55% | Sharpe=0.878 | DD=9.47% | Turnover=29.56%
   🎚️ Intra-Step TAPE: potential=0.5907 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0364 | critic_loss=0.0072 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0036 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8783 | ema=0.3132 | best_ema=0.3132 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00121_shp0p917_actor.weights.h5 (Sharpe=0.917, MDD=9.47%)
[CYCLE] Update 96/348 | Step 96,768/500,000 | Episode 128 | Time: 9365.8s
   📊 Metrics: Return=+8.50% | Sharpe=0.124 | DD=13.80% | Turnover=29.45%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0375 | critic_loss=0.0295 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0148 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1237 | ema=0.2943 | best_ema=0.2943 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.12 | range=[1.04, 8.76] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.66 | NVDA=1.45 | MSFT=1.45  BOT: NEE=1.21 | KO=1.20 | GLD=1.13
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0186, db=0.0123, sat=0.0%) | asset(dg=0.0016, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=54 (39.7%), medium_vol=38 (27.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2521
[CYCLE] Update 97/348 | Step 97,776/500,000 | Episode 128 | Time: 9463.2s
   📊 Metrics: Return=+7.77% | Sharpe=1.265 | DD=6.70% | Turnover=30.57%
   🎚️ Intra-Step TAPE: potential=0.2442 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0355 | critic_loss=0.0291 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0145 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2649 | ema=0.3913 | best_ema=0.3913 | no_improve=0
[CYCLE] Update 98/348 | Step 98,784/500,000 | Episode 128 | Time: 9560.6s
   📊 Metrics: Return=+16.81% | Sharpe=1.546 | DD=6.70% | Turnover=29.46%
   🎚️ Intra-Step TAPE: potential=0.5409 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0411 | critic_loss=0.0101 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5460 | ema=0.5068 | best_ema=0.5068 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.10 | range=[1.08, 8.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.78 | CAT=1.48 | JPM=1.46  BOT: GLD=1.16 | NEE=1.16 | KO=1.15
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0190, db=0.0125, sat=0.0%) | asset(dg=0.0016, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=54 (39.7%), medium_vol=38 (27.9%)
[CYCLE] Update 99/348 | Step 99,792/500,000 | Episode 128 | Time: 9657.6s
   📊 Metrics: Return=+27.59% | Sharpe=1.755 | DD=6.70% | Turnover=29.24%
   🎚️ Intra-Step TAPE: potential=0.4283 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0397 | critic_loss=0.0054 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0027 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7548 | ema=0.6316 | best_ema=0.6316 | no_improve=0
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 9754.6s
   📊 Metrics: Return=+37.19% | Sharpe=1.779 | DD=6.70% | Turnover=29.37%
   🎚️ Intra-Step TAPE: potential=0.4987 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0424 | critic_loss=0.0046 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7791 | ema=0.7464 | best_ema=0.7464 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.10 | range=[1.07, 8.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.90 | AMZN=1.48 | JPM=1.41  BOT: XOM=1.18 | NEE=1.16 | KO=1.16
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0192, db=0.0126, sat=0.0%) | asset(dg=0.0017, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=54 (39.7%), medium_vol=38 (27.9%)
[CYCLE] Update 101/348 | Step 101,808/500,000 | Episode 128 | Time: 9851.6s
   📊 Metrics: Return=+49.77% | Sharpe=1.779 | DD=6.70% | Turnover=29.38%
   🎚️ Intra-Step TAPE: potential=0.5960 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0342 | critic_loss=0.0101 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7795 | ema=0.8497 | best_ema=0.8497 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00129_shp1p440_actor.weights.h5 (Sharpe=1.440, MDD=6.70%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00133_shp0p888_actor.weights.h5 (Sharpe=0.888, MDD=8.40%)
[CYCLE] Update 102/348 | Step 102,816/500,000 | Episode 136 | Time: 9948.2s
   📊 Metrics: Return=-1.38% | Sharpe=-0.186 | DD=14.19% | Turnover=29.77%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0399 | critic_loss=0.0407 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0203 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1863 | ema=0.7461 | best_ema=0.7461 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.10 | range=[1.07, 8.75] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.67 | AMZN=1.61 | MSFT=1.45  BOT: XOM=1.17 | NEE=1.16 | KO=1.14
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0183, db=0.0120, sat=0.0%) | asset(dg=0.0016, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=47 (32.6%), low_vol=57 (39.6%), medium_vol=40 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2390
[CYCLE] Update 103/348 | Step 103,824/500,000 | Episode 136 | Time: 10044.7s
   📊 Metrics: Return=+7.06% | Sharpe=1.525 | DD=2.14% | Turnover=29.59%
   🎚️ Intra-Step TAPE: potential=0.5310 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0405 | critic_loss=0.0210 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0105 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5248 | ema=0.8239 | best_ema=0.8239 | no_improve=0
[CYCLE] Update 104/348 | Step 104,832/500,000 | Episode 136 | Time: 10141.8s
   📊 Metrics: Return=+16.54% | Sharpe=1.829 | DD=2.14% | Turnover=29.55%
   🎚️ Intra-Step TAPE: potential=0.5726 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0383 | critic_loss=0.0067 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8286 | ema=0.9244 | best_ema=0.9244 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.12 | range=[1.07, 8.77] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.59 | AMZN=1.44 | JPM=1.42  BOT: GLD=1.19 | NEE=1.18 | KO=1.17
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0186, db=0.0123, sat=0.0%) | asset(dg=0.0016, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=47 (32.6%), low_vol=57 (39.6%), medium_vol=40 (27.8%)
[CYCLE] Update 105/348 | Step 105,840/500,000 | Episode 136 | Time: 10238.9s
   📊 Metrics: Return=+21.74% | Sharpe=1.354 | DD=5.45% | Turnover=29.33%
   🎚️ Intra-Step TAPE: potential=0.2285 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0365 | critic_loss=0.0074 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0037 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0210
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3543 | ema=0.9674 | best_ema=0.9674 | no_improve=0
[CYCLE] Update 106/348 | Step 106,848/500,000 | Episode 136 | Time: 10335.6s
   📊 Metrics: Return=+27.60% | Sharpe=1.296 | DD=5.45% | Turnover=29.22%
   🎚️ Intra-Step TAPE: potential=0.7130 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0355 | critic_loss=0.0068 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2963 | ema=1.0003 | best_ema=1.0003 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.12 | range=[1.09, 8.74] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.71 | AMZN=1.52 | MSFT=1.41  BOT: XOM=1.19 | GLD=1.18 | KO=1.17
   🧬 FiLM: seq(dg=0.0006, db=0.0004, sat=0.0%) | latent(dg=0.0179, db=0.0119, sat=0.0%) | asset(dg=0.0017, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=47 (32.6%), low_vol=57 (39.6%), medium_vol=40 (27.8%)
[CYCLE] Update 107/348 | Step 107,856/500,000 | Episode 136 | Time: 10432.7s
   📊 Metrics: Return=+24.10% | Sharpe=0.746 | DD=13.23% | Turnover=29.28%
   🎚️ Intra-Step TAPE: potential=0.7246 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0341 | critic_loss=0.0067 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7460 | ema=0.9749 | best_ema=0.9749 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00139_shp1p016_actor.weights.h5 (Sharpe=1.016, MDD=6.73%)
[CYCLE] Update 108/348 | Step 108,864/500,000 | Episode 144 | Time: 10528.8s
   📊 Metrics: Return=+23.26% | Sharpe=0.467 | DD=12.07% | Turnover=29.61%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0377 | critic_loss=0.0307 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0153 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4668 | ema=0.9241 | best_ema=0.9241 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.12 | range=[1.09, 8.75] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.60 | AMZN=1.49 | MSFT=1.38  BOT: NEE=1.17 | KO=1.16 | GLD=1.16
   🧬 FiLM: seq(dg=0.0006, db=0.0004, sat=0.0%) | latent(dg=0.0174, db=0.0117, sat=0.0%) | asset(dg=0.0016, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=59 (38.8%), medium_vol=43 (28.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3038
[CYCLE] Update 109/348 | Step 109,872/500,000 | Episode 144 | Time: 10625.5s
   📊 Metrics: Return=-1.37% | Sharpe=-0.707 | DD=5.26% | Turnover=29.84%
   🎚️ Intra-Step TAPE: potential=0.2253 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0389 | critic_loss=0.0093 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.7072 | ema=0.7609 | best_ema=0.7609 | no_improve=0
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 144 | Time: 10722.5s
   📊 Metrics: Return=-1.34% | Sharpe=-0.435 | DD=7.30% | Turnover=29.25%
   🎚️ Intra-Step TAPE: potential=0.2419 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0372 | critic_loss=0.0093 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0210
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4347 | ema=0.6414 | best_ema=0.6414 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.13 | range=[1.08, 8.75] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.62 | AMZN=1.47 | MSFT=1.36  BOT: NEE=1.19 | KO=1.18 | GLD=1.16
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0185, db=0.0125, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=59 (38.8%), medium_vol=43 (28.3%)
[CYCLE] Update 111/348 | Step 111,888/500,000 | Episode 144 | Time: 10819.7s
   📊 Metrics: Return=-2.51% | Sharpe=-0.496 | DD=7.41% | Turnover=29.56%
   🎚️ Intra-Step TAPE: potential=0.2437 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0417 | critic_loss=0.0063 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4960 | ema=0.5276 | best_ema=0.5276 | no_improve=0
[CYCLE] Update 112/348 | Step 112,896/500,000 | Episode 144 | Time: 10917.1s
   📊 Metrics: Return=-7.02% | Sharpe=-0.590 | DD=12.29% | Turnover=29.67%
   🎚️ Intra-Step TAPE: potential=0.2403 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0352 | critic_loss=0.0092 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5896 | ema=0.4159 | best_ema=0.4159 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.10 | range=[1.05, 8.72] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.91 | AMZN=1.52 | MSFT=1.41  BOT: XOM=1.17 | KO=1.16 | GLD=1.15
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0188, db=0.0126, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=59 (38.8%), medium_vol=43 (28.3%)
[CYCLE] Update 113/348 | Step 113,904/500,000 | Episode 144 | Time: 11014.1s
   📊 Metrics: Return=+9.03% | Sharpe=0.215 | DD=12.29% | Turnover=29.57%
   🎚️ Intra-Step TAPE: potential=0.7239 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0461 | critic_loss=0.0066 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2146 | ema=0.3958 | best_ema=0.3958 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00147_shp1p091_actor.weights.h5 (Sharpe=1.091, MDD=7.81%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00152_shp0p948_actor.weights.h5 (Sharpe=0.948, MDD=7.11%)
[CYCLE] Update 114/348 | Step 114,912/500,000 | Episode 152 | Time: 11110.4s
   📊 Metrics: Return=+35.64% | Sharpe=0.948 | DD=7.11% | Turnover=28.63%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0359 | critic_loss=0.0275 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0137 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9479 | ema=0.4510 | best_ema=0.4510 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=2.05 | range=[1.02, 8.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.20 | AMZN=1.71 | MSFT=1.57  BOT: NEE=1.13 | KO=1.12 | GLD=1.11
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0191, db=0.0127, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=62 (38.8%), medium_vol=45 (28.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4988
[CYCLE] Update 115/348 | Step 115,920/500,000 | Episode 152 | Time: 11207.4s
   📊 Metrics: Return=-0.43% | Sharpe=-0.317 | DD=3.17% | Turnover=29.16%
   🎚️ Intra-Step TAPE: potential=0.2426 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0392 | critic_loss=0.0148 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0074 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3169 | ema=0.3742 | best_ema=0.3742 | no_improve=0
[CYCLE] Update 116/348 | Step 116,928/500,000 | Episode 152 | Time: 11304.3s
   📊 Metrics: Return=+2.03% | Sharpe=0.042 | DD=4.31% | Turnover=29.49%
   🎚️ Intra-Step TAPE: potential=0.2353 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0385 | critic_loss=0.0059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0416 | ema=0.3409 | best_ema=0.3409 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=2.05 | range=[1.01, 8.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.93 | JPM=1.57 | AMZN=1.56  BOT: GLD=1.13 | NEE=1.12 | KO=1.09
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0203, db=0.0134, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=62 (38.8%), medium_vol=45 (28.1%)
[CYCLE] Update 117/348 | Step 117,936/500,000 | Episode 152 | Time: 11401.0s
   📊 Metrics: Return=+0.01% | Sharpe=-0.235 | DD=4.31% | Turnover=29.51%
   🎚️ Intra-Step TAPE: potential=0.2419 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0401 | critic_loss=0.0052 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0221
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2348 | ema=0.2833 | best_ema=0.2833 | no_improve=0
[CYCLE] Update 118/348 | Step 118,944/500,000 | Episode 152 | Time: 11497.5s
   📊 Metrics: Return=-1.82% | Sharpe=-0.330 | DD=7.21% | Turnover=29.27%
   🎚️ Intra-Step TAPE: potential=0.2314 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0411 | critic_loss=0.0086 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0043 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0226
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3298 | ema=0.2220 | best_ema=0.2220 | no_improve=0
   🔬 Alpha Diversity: mean=2.03 | std=1.99 | range=[0.99, 8.46] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.40 | AMZN=1.91 | JPM=1.51  BOT: NEE=1.11 | KO=1.10 | GLD=1.08
   🧬 FiLM: seq(dg=0.0005, db=0.0004, sat=0.0%) | latent(dg=0.0201, db=0.0133, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=62 (38.8%), medium_vol=45 (28.1%)
[CYCLE] Update 119/348 | Step 119,952/500,000 | Episode 152 | Time: 11593.8s
   📊 Metrics: Return=+3.51% | Sharpe=-0.023 | DD=7.21% | Turnover=29.13%
   🎚️ Intra-Step TAPE: potential=0.3910 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0402 | critic_loss=0.0116 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0235 | ema=0.1975 | best_ema=0.1975 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00154_shp1p381_actor.weights.h5 (Sharpe=1.381, MDD=8.15%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00157_shp1p110_actor.weights.h5 (Sharpe=1.110, MDD=7.73%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00160_shp0p791_actor.weights.h5 (Sharpe=0.791, MDD=19.63%)
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 160 | Time: 11690.0s
   📊 Metrics: Return=+33.43% | Sharpe=0.791 | DD=19.63% | Turnover=29.11%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0389 | critic_loss=0.0419 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0209 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0228
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7910 | ema=0.2568 | best_ema=0.2568 | no_improve=0
   🔬 Alpha Diversity: mean=2.03 | std=1.97 | range=[0.96, 8.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.08 | AMZN=1.99 | MSFT=1.84  BOT: NEE=1.11 | GLD=1.06 | KO=1.06
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0195, db=0.0130, sat=0.0%) | asset(dg=0.0017, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (32.7%), low_vol=65 (38.7%), medium_vol=48 (28.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.009) | TAPE=0.3954
[CYCLE] Update 121/348 | Step 121,968/500,000 | Episode 160 | Time: 11786.5s
   📊 Metrics: Return=+0.29% | Sharpe=-0.160 | DD=3.31% | Turnover=29.92%
   🎚️ Intra-Step TAPE: potential=0.2423 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0398 | critic_loss=0.0089 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0226
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1600 | ema=0.2151 | best_ema=0.2151 | no_improve=0
[CYCLE] Update 122/348 | Step 122,976/500,000 | Episode 160 | Time: 11883.1s
   📊 Metrics: Return=-5.01% | Sharpe=-0.844 | DD=6.38% | Turnover=30.11%
   🎚️ Intra-Step TAPE: potential=0.2402 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0412 | critic_loss=0.0072 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0036 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0228
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.8438 | ema=0.1093 | best_ema=0.1093 | no_improve=0
   🔬 Alpha Diversity: mean=2.04 | std=1.97 | range=[0.96, 8.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.23 | AMZN=1.99 | JPM=1.52  BOT: GLD=1.10 | XOM=1.10 | KO=1.08
   🧬 FiLM: seq(dg=0.0006, db=0.0004, sat=0.0%) | latent(dg=0.0203, db=0.0135, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (32.7%), low_vol=65 (38.7%), medium_vol=48 (28.6%)
[CYCLE] Update 123/348 | Step 123,984/500,000 | Episode 160 | Time: 11980.0s
   📊 Metrics: Return=+1.87% | Sharpe=-0.040 | DD=6.65% | Turnover=30.02%
   🎚️ Intra-Step TAPE: potential=0.2459 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0374 | critic_loss=0.0073 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0037 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0403 | ema=0.0943 | best_ema=0.0943 | no_improve=0
[CYCLE] Update 124/348 | Step 124,992/500,000 | Episode 160 | Time: 12077.2s
   📊 Metrics: Return=+3.52% | Sharpe=0.028 | DD=7.72% | Turnover=30.01%
   🎚️ Intra-Step TAPE: potential=0.2418 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0378 | critic_loss=0.0123 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0062 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0234
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0279 | ema=0.0877 | best_ema=0.0877 | no_improve=0
   🔬 Alpha Diversity: mean=2.05 | std=1.92 | range=[0.95, 8.33] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.35 | NVDA=2.24 | MSFT=1.81  BOT: NEE=1.09 | GLD=1.05 | KO=1.05
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0203, db=0.0135, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (32.7%), low_vol=65 (38.7%), medium_vol=48 (28.6%)
[CYCLE] Update 125/348 | Step 126,000/500,000 | Episode 160 | Time: 12174.2s
   📊 Metrics: Return=+17.49% | Sharpe=0.481 | DD=9.22% | Turnover=29.96%
   🎚️ Intra-Step TAPE: potential=0.7077 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0420 | critic_loss=0.0073 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0037 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0230
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4809 | ema=0.1270 | best_ema=0.1270 | no_improve=0
[CYCLE] Update 126/348 | Step 127,008/500,000 | Episode 168 | Time: 12269.8s
   📊 Metrics: Return=+10.90% | Sharpe=0.216 | DD=6.87% | Turnover=28.97%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0380 | critic_loss=0.0154 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0077 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2161 | ema=0.1359 | best_ema=0.1359 | no_improve=0
   🔬 Alpha Diversity: mean=2.03 | std=1.97 | range=[0.96, 8.43] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.26 | AMZN=2.01 | MSFT=1.69  BOT: NEE=1.10 | GLD=1.08 | KO=1.07
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0207, db=0.0137, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=58 (33.0%), low_vol=69 (39.2%), medium_vol=49 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2625
[CYCLE] Update 127/348 | Step 128,016/500,000 | Episode 168 | Time: 12366.5s
   📊 Metrics: Return=-0.55% | Sharpe=-0.199 | DD=8.25% | Turnover=29.30%
   🎚️ Intra-Step TAPE: potential=0.2446 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0377 | critic_loss=0.0100 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0224
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1989 | ema=0.1024 | best_ema=0.1024 | no_improve=0
[CYCLE] Update 128/348 | Step 129,024/500,000 | Episode 168 | Time: 12463.6s
   📊 Metrics: Return=-1.06% | Sharpe=-0.226 | DD=9.83% | Turnover=29.06%
   🎚️ Intra-Step TAPE: potential=0.2397 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0406 | critic_loss=0.0086 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0043 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2257 | ema=0.0696 | best_ema=0.0696 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=2.03 | range=[1.02, 8.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.09 | NVDA=1.68 | JPM=1.54  BOT: NEE=1.12 | GLD=1.11 | KO=1.10
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0207, db=0.0138, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=58 (33.0%), low_vol=69 (39.2%), medium_vol=49 (27.8%)
[CYCLE] Update 129/348 | Step 130,032/500,000 | Episode 168 | Time: 12560.5s
   📊 Metrics: Return=+3.20% | Sharpe=0.061 | DD=9.83% | Turnover=29.34%
   🎚️ Intra-Step TAPE: potential=0.2399 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0385 | critic_loss=0.0066 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0224
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0611 | ema=0.0687 | best_ema=0.0687 | no_improve=0
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 168 | Time: 12657.4s
   📊 Metrics: Return=+3.73% | Sharpe=0.031 | DD=9.83% | Turnover=29.29%
   🎚️ Intra-Step TAPE: potential=0.6282 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0357 | critic_loss=0.0053 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0230
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0310 | ema=0.0650 | best_ema=0.0650 | no_improve=0
   🔬 Alpha Diversity: mean=2.04 | std=1.94 | range=[0.96, 8.45] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.15 | MSFT=2.01 | NVDA=1.93  BOT: NEE=1.11 | GLD=1.09 | KO=1.05
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0214, db=0.0142, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=58 (33.0%), low_vol=69 (39.2%), medium_vol=49 (27.8%)
[CYCLE] Update 131/348 | Step 132,048/500,000 | Episode 168 | Time: 12754.3s
   📊 Metrics: Return=+4.48% | Sharpe=0.021 | DD=9.83% | Turnover=29.06%
   🎚️ Intra-Step TAPE: potential=0.2363 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0408 | critic_loss=0.0051 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0205 | ema=0.0605 | best_ema=0.0605 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00171_shp1p289_actor.weights.h5 (Sharpe=1.289, MDD=8.13%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00173_shp0p926_actor.weights.h5 (Sharpe=0.926, MDD=7.01%)
[CYCLE] Update 132/348 | Step 133,056/500,000 | Episode 176 | Time: 12850.8s
   📊 Metrics: Return=+10.64% | Sharpe=0.178 | DD=16.56% | Turnover=28.86%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0385 | critic_loss=0.0153 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0076 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1784 | ema=0.0723 | best_ema=0.0723 | no_improve=0
   🔬 Alpha Diversity: mean=2.04 | std=1.93 | range=[0.93, 8.16] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.39 | AMZN=2.26 | MSFT=1.67  BOT: NEE=1.11 | KO=1.08 | GLD=1.02
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0206, db=0.0137, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=63 (34.2%), low_vol=71 (38.6%), medium_vol=50 (27.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2552
[CYCLE] Update 133/348 | Step 134,064/500,000 | Episode 176 | Time: 12947.5s
   📊 Metrics: Return=+22.26% | Sharpe=3.632 | DD=3.76% | Turnover=29.82%
   🎚️ Intra-Step TAPE: potential=0.7527 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0398 | critic_loss=0.0115 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.6323 | ema=0.4283 | best_ema=0.4283 | no_improve=0
[CYCLE] Update 134/348 | Step 135,072/500,000 | Episode 176 | Time: 13044.5s
   📊 Metrics: Return=+14.70% | Sharpe=1.096 | DD=9.93% | Turnover=29.53%
   🎚️ Intra-Step TAPE: potential=0.2355 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0388 | critic_loss=0.0040 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0961 | ema=0.4951 | best_ema=0.4951 | no_improve=0
   🔬 Alpha Diversity: mean=2.05 | std=1.88 | range=[0.93, 8.26] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.30 | AMZN=2.01 | JPM=1.90  BOT: KO=1.04 | NEE=1.03 | GLD=1.01
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0206, db=0.0138, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=63 (34.2%), low_vol=71 (38.6%), medium_vol=50 (27.2%)
[CYCLE] Update 135/348 | Step 136,080/500,000 | Episode 176 | Time: 13141.7s
   📊 Metrics: Return=+14.27% | Sharpe=0.534 | DD=16.60% | Turnover=29.31%
   🎚️ Intra-Step TAPE: potential=0.2830 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0388 | critic_loss=0.0041 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5339 | ema=0.4990 | best_ema=0.4990 | no_improve=0
[CYCLE] Update 136/348 | Step 137,088/500,000 | Episode 176 | Time: 13238.5s
   📊 Metrics: Return=+9.21% | Sharpe=0.243 | DD=17.12% | Turnover=29.48%
   🎚️ Intra-Step TAPE: potential=0.2436 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0388 | critic_loss=0.0034 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2426 | ema=0.4733 | best_ema=0.4733 | no_improve=0
   🔬 Alpha Diversity: mean=2.04 | std=1.95 | range=[0.95, 8.29] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.41 | AMZN=1.80 | JPM=1.67  BOT: XOM=1.10 | GLD=1.07 | KO=1.07
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0206, db=0.0139, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=63 (34.2%), low_vol=71 (38.6%), medium_vol=50 (27.2%)
[CYCLE] Update 137/348 | Step 138,096/500,000 | Episode 176 | Time: 13335.5s
   📊 Metrics: Return=+10.81% | Sharpe=0.227 | DD=17.48% | Turnover=29.44%
   🎚️ Intra-Step TAPE: potential=0.6271 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0377 | critic_loss=0.0046 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2274 | ema=0.4487 | best_ema=0.4487 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00178_shp1p352_actor.weights.h5 (Sharpe=1.352, MDD=9.73%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00181_shp1p594_actor.weights.h5 (Sharpe=1.594, MDD=10.09%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00184_shp1p701_actor.weights.h5 (Sharpe=1.701, MDD=9.03%)
[CYCLE] Update 138/348 | Step 139,104/500,000 | Episode 184 | Time: 13432.7s
   📊 Metrics: Return=+78.96% | Sharpe=1.701 | DD=9.03% | Turnover=29.16%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0388 | critic_loss=0.0414 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0207 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7005 | ema=0.5739 | best_ema=0.5739 | no_improve=0
   🔬 Alpha Diversity: mean=2.04 | std=1.94 | range=[0.95, 8.34] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.32 | NVDA=2.29 | MSFT=1.68  BOT: NEE=1.07 | KO=1.06 | GLD=1.03
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0212, db=0.0143, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=65 (33.9%), low_vol=75 (39.1%), medium_vol=52 (27.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6394
[CYCLE] Update 139/348 | Step 140,112/500,000 | Episode 184 | Time: 13530.3s
   📊 Metrics: Return=-0.77% | Sharpe=-0.425 | DD=8.28% | Turnover=29.14%
   🎚️ Intra-Step TAPE: potential=0.2389 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0358 | critic_loss=0.0144 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0072 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4253 | ema=0.4740 | best_ema=0.4740 | no_improve=0
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 184 | Time: 13627.3s
   📊 Metrics: Return=-2.24% | Sharpe=-0.469 | DD=8.28% | Turnover=29.14%
   🎚️ Intra-Step TAPE: potential=0.2410 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0415 | critic_loss=0.0065 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0032 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4695 | ema=0.3796 | best_ema=0.3796 | no_improve=0
   🔬 Alpha Diversity: mean=2.02 | std=1.99 | range=[0.97, 8.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.05 | AMZN=2.03 | CAT=1.50  BOT: NEE=1.10 | KO=1.06 | GLD=1.03
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0218, db=0.0146, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=65 (33.9%), low_vol=75 (39.1%), medium_vol=52 (27.1%)
[CYCLE] Update 141/348 | Step 142,128/500,000 | Episode 184 | Time: 13724.3s
   📊 Metrics: Return=+2.28% | Sharpe=0.000 | DD=11.42% | Turnover=29.13%
   🎚️ Intra-Step TAPE: potential=0.7255 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0377 | critic_loss=0.0061 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0030 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0004 | ema=0.3417 | best_ema=0.3417 | no_improve=0
[CYCLE] Update 142/348 | Step 143,136/500,000 | Episode 184 | Time: 13821.4s
   📊 Metrics: Return=+5.23% | Sharpe=0.107 | DD=11.42% | Turnover=29.40%
   🎚️ Intra-Step TAPE: potential=0.7501 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0342 | critic_loss=0.0050 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1066 | ema=0.3182 | best_ema=0.3182 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.05 | range=[0.99, 8.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.01 | AMZN=1.59 | CAT=1.43  BOT: NEE=1.12 | KO=1.09 | GLD=1.08
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0215, db=0.0145, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=65 (33.9%), low_vol=75 (39.1%), medium_vol=52 (27.1%)
[CYCLE] Update 143/348 | Step 144,144/500,000 | Episode 184 | Time: 13918.2s
   📊 Metrics: Return=+14.58% | Sharpe=0.399 | DD=11.42% | Turnover=29.34%
   🎚️ Intra-Step TAPE: potential=0.6507 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0376 | critic_loss=0.0057 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3993 | ema=0.3263 | best_ema=0.3263 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00188_shp1p326_actor.weights.h5 (Sharpe=1.326, MDD=9.49%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00190_shp0p911_actor.weights.h5 (Sharpe=0.911, MDD=9.66%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00191_shp1p229_actor.weights.h5 (Sharpe=1.229, MDD=10.21%)
[CYCLE] Update 144/348 | Step 145,152/500,000 | Episode 192 | Time: 14014.9s
   📊 Metrics: Return=+12.18% | Sharpe=0.252 | DD=10.43% | Turnover=29.40%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0401 | critic_loss=0.0145 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0072 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2525 | ema=0.3189 | best_ema=0.3189 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.08 | range=[0.99, 8.73] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.90 | AMZN=1.56 | JPM=1.39  BOT: NEE=1.12 | KO=1.11 | GLD=1.10
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0208, db=0.0142, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=68 (34.0%), low_vol=80 (40.0%), medium_vol=52 (26.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2622
[CYCLE] Update 145/348 | Step 146,160/500,000 | Episode 192 | Time: 14111.6s
   📊 Metrics: Return=+7.60% | Sharpe=1.035 | DD=8.10% | Turnover=30.33%
   🎚️ Intra-Step TAPE: potential=0.2348 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0330 | critic_loss=0.0079 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0039 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0348 | ema=0.3905 | best_ema=0.3905 | no_improve=0
[CYCLE] Update 146/348 | Step 147,168/500,000 | Episode 192 | Time: 14208.6s
   📊 Metrics: Return=+19.82% | Sharpe=1.590 | DD=8.10% | Turnover=29.50%
   🎚️ Intra-Step TAPE: potential=0.7157 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0384 | critic_loss=0.0048 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5900 | ema=0.5105 | best_ema=0.5105 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.07 | range=[0.99, 8.73] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.80 | AMZN=1.66 | JPM=1.42  BOT: NEE=1.14 | KO=1.12 | GLD=1.08
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0212, db=0.0144, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=68 (34.0%), low_vol=80 (40.0%), medium_vol=52 (26.0%)
[CYCLE] Update 147/348 | Step 148,176/500,000 | Episode 192 | Time: 14305.7s
   📊 Metrics: Return=+31.15% | Sharpe=1.704 | DD=8.10% | Turnover=29.71%
   🎚️ Intra-Step TAPE: potential=0.6374 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0361 | critic_loss=0.0087 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0044 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7042 | ema=0.6298 | best_ema=0.6298 | no_improve=0
[CYCLE] Update 148/348 | Step 149,184/500,000 | Episode 192 | Time: 14402.6s
   📊 Metrics: Return=+41.81% | Sharpe=1.703 | DD=8.10% | Turnover=29.59%
   🎚️ Intra-Step TAPE: potential=0.3487 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0396 | critic_loss=0.0065 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7027 | ema=0.7371 | best_ema=0.7371 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.03 | range=[0.98, 8.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.19 | AMZN=1.76 | MSFT=1.55  BOT: NEE=1.15 | KO=1.10 | GLD=1.09
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0215, db=0.0145, sat=0.0%) | asset(dg=0.0019, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=68 (34.0%), low_vol=80 (40.0%), medium_vol=52 (26.0%)
   [TOOL] Actor learning rate adjusted to 0.000020 at step 150,000
   [TOOL] Critic learning rate adjusted to 0.000120 at step 150,000

🎛️ EXECUTION BETA UPDATE at 150,192 steps:
   action_execution_beta: 0.650 (w_exec=(1-β)w_prev + βw_raw)
[CYCLE] Update 149/348 | Step 150,192/500,000 | Episode 192 | Time: 14499.4s
   📊 Metrics: Return=+61.61% | Sharpe=1.866 | DD=8.10% | Turnover=29.72%
   🎚️ Intra-Step TAPE: potential=0.5870 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0376 | critic_loss=0.0086 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0043 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8661 | ema=0.8500 | best_ema=0.8500 | no_improve=0

📚 PPO ROLLOUT UPDATE at 150,192 steps:
   Timesteps per update: 1512

📚 PPO BATCH SIZE UPDATE at 150,192 steps:
   Batch size: 336

[DOWN] PPO GAMMA UPDATE at 150,192 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 150,192 steps:
   gae_lambda: 0.9500

🎯 ENTROPY COEF UPDATE at 150,192 steps:
   entropy_coef: 0.0005

🧪 AUX-RETURN COEF UPDATE at 150,192 steps:
   aux_return_pred_coef: 0.3000

🌡️ TEMPERATURE UPDATE at 150,192 steps:
   temperature: 0.9000
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00193_shp1p355_actor.weights.h5 (Sharpe=1.355, MDD=8.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00197_shp1p153_actor.weights.h5 (Sharpe=1.153, MDD=8.10%)
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 200 | Time: 14652.1s
   📊 Metrics: Return=+24.48% | Sharpe=0.633 | DD=9.88% | Turnover=30.34%
   🎚️ Intra-Step TAPE: potential=0.2950 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0396 | critic_loss=0.0214 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0107 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6332 | ema=0.8283 | best_ema=0.8283 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=2.01 | range=[0.98, 8.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.19 | AMZN=1.86 | MSFT=1.50  BOT: KO=1.09 | NEE=1.09 | GLD=1.06
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0217, db=0.0145, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (34.1%), low_vol=85 (40.9%), medium_vol=52 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.11% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3581
[CYCLE] Update 151/348 | Step 153,216/500,000 | Episode 200 | Time: 14788.7s
   📊 Metrics: Return=-1.47% | Sharpe=-0.373 | DD=7.79% | Turnover=35.36%
   🎚️ Intra-Step TAPE: potential=0.4303 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0338 | critic_loss=0.0078 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0039 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3759 | ema=0.7079 | best_ema=0.7079 | no_improve=0
[CYCLE] Update 152/348 | Step 154,728/500,000 | Episode 200 | Time: 14924.9s
   📊 Metrics: Return=-2.04% | Sharpe=-0.264 | DD=9.75% | Turnover=35.38%
   🎚️ Intra-Step TAPE: potential=0.2255 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0358 | critic_loss=0.0082 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0041 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0221
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2673 | ema=0.6104 | best_ema=0.6104 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=2.01 | range=[0.97, 8.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.33 | AMZN=1.75 | MSFT=1.43  BOT: NEE=1.11 | KO=1.09 | GLD=1.07
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0228, db=0.0153, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (34.1%), low_vol=85 (40.9%), medium_vol=52 (25.0%)
[CYCLE] Update 153/348 | Step 156,240/500,000 | Episode 200 | Time: 15060.8s
   📊 Metrics: Return=+14.87% | Sharpe=0.414 | DD=9.75% | Turnover=35.58%
   🎚️ Intra-Step TAPE: potential=0.7489 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0296 | critic_loss=0.0065 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4086 | ema=0.5902 | best_ema=0.5902 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00202_shp1p064_actor.weights.h5 (Sharpe=1.064, MDD=8.96%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00203_shp0p718_actor.weights.h5 (Sharpe=0.718, MDD=9.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00204_shp0p707_actor.weights.h5 (Sharpe=0.707, MDD=11.67%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00208_shp0p831_actor.weights.h5 (Sharpe=0.831, MDD=9.73%)
[CYCLE] Update 154/348 | Step 157,752/500,000 | Episode 208 | Time: 15198.9s
   📊 Metrics: Return=+33.36% | Sharpe=0.831 | DD=9.73% | Turnover=35.37%
   🎚️ Intra-Step TAPE: potential=0.2255 | delta_reward=-0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0356 | critic_loss=0.0215 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8277 | ema=0.6140 | best_ema=0.6140 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=2.01 | range=[0.95, 8.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.14 | AMZN=1.75 | JPM=1.47  BOT: XOM=1.11 | GLD=1.09 | KO=1.08
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0220, db=0.0147, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=72 (33.3%), low_vol=88 (40.7%), medium_vol=56 (25.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.22% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4620
[CYCLE] Update 155/348 | Step 159,264/500,000 | Episode 208 | Time: 15335.6s
   📊 Metrics: Return=-2.03% | Sharpe=-0.473 | DD=6.33% | Turnover=35.98%
   🎚️ Intra-Step TAPE: potential=0.3430 | delta_reward=-0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0256 | critic_loss=0.0076 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0038 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4812 | ema=0.5045 | best_ema=0.5045 | no_improve=0
[CYCLE] Update 156/348 | Step 160,776/500,000 | Episode 208 | Time: 15472.0s
   📊 Metrics: Return=-0.32% | Sharpe=-0.196 | DD=7.24% | Turnover=35.58%
   🎚️ Intra-Step TAPE: potential=0.2406 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0359 | critic_loss=0.0100 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0050 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2014 | ema=0.4339 | best_ema=0.4339 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.03 | range=[0.98, 8.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.93 | NVDA=1.78 | MSFT=1.58  BOT: XOM=1.14 | KO=1.09 | GLD=1.06
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0226, db=0.0152, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=72 (33.3%), low_vol=88 (40.7%), medium_vol=56 (25.9%)
[CYCLE] Update 157/348 | Step 162,288/500,000 | Episode 208 | Time: 15608.2s
   📊 Metrics: Return=+9.82% | Sharpe=0.231 | DD=9.27% | Turnover=35.58%
   🎚️ Intra-Step TAPE: potential=0.6091 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0296 | critic_loss=0.0056 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0028 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2265 | ema=0.4131 | best_ema=0.4131 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00215_shp1p142_actor.weights.h5 (Sharpe=1.142, MDD=9.01%)
[CYCLE] Update 158/348 | Step 163,800/500,000 | Episode 216 | Time: 15744.9s
   📊 Metrics: Return=+5.00% | Sharpe=0.001 | DD=8.63% | Turnover=35.85%
   🎚️ Intra-Step TAPE: potential=0.2414 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0430 | critic_loss=0.0165 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0083 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0060 | ema=0.3712 | best_ema=0.3712 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=1.99 | range=[0.98, 8.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.15 | AMZN=1.89 | MSFT=1.52  BOT: NEE=1.12 | KO=1.07 | GLD=1.06
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0229, db=0.0154, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=72 (32.1%), low_vol=90 (40.2%), medium_vol=62 (27.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.48% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2500
[CYCLE] Update 159/348 | Step 165,312/500,000 | Episode 216 | Time: 15881.3s
   📊 Metrics: Return=-1.37% | Sharpe=-0.398 | DD=6.70% | Turnover=35.33%
   🎚️ Intra-Step TAPE: potential=0.2330 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0472 | critic_loss=0.0039 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4007 | ema=0.2940 | best_ema=0.2940 | no_improve=0
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 216 | Time: 16017.6s
   📊 Metrics: Return=-1.84% | Sharpe=-0.336 | DD=7.90% | Turnover=35.39%
   🎚️ Intra-Step TAPE: potential=0.2440 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0322 | critic_loss=0.0032 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0016 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3389 | ema=0.2307 | best_ema=0.2307 | no_improve=0
   🔬 Alpha Diversity: mean=2.00 | std=2.02 | range=[0.98, 8.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.07 | AMZN=1.75 | JPM=1.55  BOT: NEE=1.12 | KO=1.08 | GLD=1.06
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0226, db=0.0152, sat=0.0%) | asset(dg=0.0019, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=72 (32.1%), low_vol=90 (40.2%), medium_vol=62 (27.7%)
[CYCLE] Update 161/348 | Step 168,336/500,000 | Episode 216 | Time: 16153.7s
   📊 Metrics: Return=+5.73% | Sharpe=0.074 | DD=10.45% | Turnover=35.22%
   🎚️ Intra-Step TAPE: potential=0.7506 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0404 | critic_loss=0.0047 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0718 | ema=0.2148 | best_ema=0.2148 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00218_shp0p942_actor.weights.h5 (Sharpe=0.942, MDD=9.62%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00220_shp1p021_actor.weights.h5 (Sharpe=1.021, MDD=7.86%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00224_shp0p841_actor.weights.h5 (Sharpe=0.841, MDD=9.25%)
[CYCLE] Update 162/348 | Step 169,848/500,000 | Episode 224 | Time: 16290.7s
   📊 Metrics: Return=+36.39% | Sharpe=0.841 | DD=9.25% | Turnover=35.69%
   🎚️ Intra-Step TAPE: potential=0.2346 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0309 | critic_loss=0.0201 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0100 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8350 | ema=0.2769 | best_ema=0.2769 | no_improve=0
   🔬 Alpha Diversity: mean=2.02 | std=1.96 | range=[0.95, 8.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.23 | AMZN=1.98 | MSFT=1.62  BOT: NEE=1.11 | KO=1.05 | GLD=1.04
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0223, db=0.0151, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=75 (32.3%), low_vol=92 (39.7%), medium_vol=65 (28.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.08% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4617
[CYCLE] Update 163/348 | Step 171,360/500,000 | Episode 224 | Time: 16426.9s
   📊 Metrics: Return=+0.03% | Sharpe=-0.189 | DD=6.53% | Turnover=36.62%
   🎚️ Intra-Step TAPE: potential=0.2432 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0346 | critic_loss=0.0057 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0028 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2031 | ema=0.2289 | best_ema=0.2289 | no_improve=0
[CYCLE] Update 164/348 | Step 172,872/500,000 | Episode 224 | Time: 16563.4s
   📊 Metrics: Return=+4.94% | Sharpe=0.126 | DD=10.62% | Turnover=36.32%
   🎚️ Intra-Step TAPE: potential=0.7430 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0416 | critic_loss=0.0050 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0226
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1147 | ema=0.2174 | best_ema=0.2174 | no_improve=0
   🔬 Alpha Diversity: mean=2.02 | std=1.95 | range=[0.93, 8.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.19 | AMZN=1.94 | MSFT=1.56  BOT: NEE=1.09 | KO=1.07 | GLD=1.06
   🧬 FiLM: seq(dg=0.0006, db=0.0005, sat=0.0%) | latent(dg=0.0230, db=0.0155, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=75 (32.3%), low_vol=92 (39.7%), medium_vol=65 (28.0%)
[CYCLE] Update 165/348 | Step 174,384/500,000 | Episode 224 | Time: 16700.0s
   📊 Metrics: Return=+25.00% | Sharpe=0.734 | DD=10.62% | Turnover=36.09%
   🎚️ Intra-Step TAPE: potential=0.7518 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0259 | critic_loss=0.0042 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0021 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7246 | ema=0.2682 | best_ema=0.2682 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00225_shp0p819_actor.weights.h5 (Sharpe=0.819, MDD=10.62%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00229_shp0p894_actor.weights.h5 (Sharpe=0.894, MDD=11.47%)
[CYCLE] Update 166/348 | Step 175,896/500,000 | Episode 232 | Time: 16837.2s
   📊 Metrics: Return=+7.63% | Sharpe=0.103 | DD=17.77% | Turnover=35.49%
   🎚️ Intra-Step TAPE: potential=0.7070 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0350 | critic_loss=0.0122 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0061 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0986 | ema=0.2512 | best_ema=0.2512 | no_improve=0
   🔬 Alpha Diversity: mean=2.02 | std=1.95 | range=[0.93, 8.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.30 | AMZN=1.81 | JPM=1.62  BOT: KO=1.09 | GLD=1.07 | NEE=1.07
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0231, db=0.0156, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=77 (32.1%), low_vol=95 (39.6%), medium_vol=68 (28.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.002 (peak 0.002) | TAPE=0.2420
[CYCLE] Update 167/348 | Step 177,408/500,000 | Episode 232 | Time: 16974.2s
   📊 Metrics: Return=-0.82% | Sharpe=-0.142 | DD=14.61% | Turnover=35.74%
   🎚️ Intra-Step TAPE: potential=0.2670 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0276 | critic_loss=0.0049 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1485 | ema=0.2112 | best_ema=0.2112 | no_improve=0
[CYCLE] Update 168/348 | Step 178,920/500,000 | Episode 232 | Time: 17111.2s
   📊 Metrics: Return=+8.93% | Sharpe=0.295 | DD=14.61% | Turnover=35.75%
   🎚️ Intra-Step TAPE: potential=0.2311 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0469 | critic_loss=0.0034 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2881 | ema=0.2189 | best_ema=0.2189 | no_improve=0
   🔬 Alpha Diversity: mean=2.03 | std=1.91 | range=[0.92, 8.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.73 | AMZN=1.90 | CAT=1.56  BOT: NEE=1.08 | KO=1.05 | GLD=1.04
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0238, db=0.0160, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=77 (32.1%), low_vol=95 (39.6%), medium_vol=68 (28.3%)
[CYCLE] Update 169/348 | Step 180,432/500,000 | Episode 232 | Time: 17247.2s
   📊 Metrics: Return=+6.51% | Sharpe=0.109 | DD=19.93% | Turnover=35.90%
   🎚️ Intra-Step TAPE: potential=0.3788 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0356 | critic_loss=0.0048 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0024 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1013 | ema=0.2072 | best_ema=0.2072 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00235_shp0p962_actor.weights.h5 (Sharpe=0.962, MDD=7.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00237_shp0p740_actor.weights.h5 (Sharpe=0.740, MDD=17.69%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00238_shp1p322_actor.weights.h5 (Sharpe=1.322, MDD=7.80%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00239_shp0p821_actor.weights.h5 (Sharpe=0.821, MDD=13.18%)
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 240 | Time: 17384.9s
   📊 Metrics: Return=+25.50% | Sharpe=0.565 | DD=18.93% | Turnover=35.45%
   🎚️ Intra-Step TAPE: potential=0.7015 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0295 | critic_loss=0.0177 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0089 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5612 | ema=0.2426 | best_ema=0.2426 | no_improve=0
   🔬 Alpha Diversity: mean=2.01 | std=1.97 | range=[0.91, 8.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.23 | AMZN=1.79 | MSFT=1.57  BOT: NEE=1.10 | GLD=1.09 | XOM=1.07
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0224, db=0.0150, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=81 (32.7%), low_vol=98 (39.5%), medium_vol=69 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.045, dd 0.30% / trig 16.50%) | terminal=0.000 (peak 0.004) | TAPE=0.3016
[CYCLE] Update 171/348 | Step 183,456/500,000 | Episode 240 | Time: 17521.3s
   📊 Metrics: Return=+18.76% | Sharpe=1.566 | DD=3.31% | Turnover=35.52%
   🎚️ Intra-Step TAPE: potential=0.2243 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0359 | critic_loss=0.0049 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0226
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.5617 | ema=0.3745 | best_ema=0.3745 | no_improve=0
[CYCLE] Update 172/348 | Step 184,968/500,000 | Episode 240 | Time: 17657.7s
   📊 Metrics: Return=+41.64% | Sharpe=2.026 | DD=3.31% | Turnover=35.99%
   🎚️ Intra-Step TAPE: potential=0.7321 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0340 | critic_loss=0.0040 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.0172 | ema=0.5388 | best_ema=0.5388 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.01 | range=[0.95, 8.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.20 | AMZN=1.65 | CAT=1.59  BOT: NEE=1.10 | KO=1.10 | GLD=1.08
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0241, db=0.0163, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=81 (32.7%), low_vol=98 (39.5%), medium_vol=69 (27.8%)
[CYCLE] Update 173/348 | Step 186,480/500,000 | Episode 240 | Time: 17793.9s
   📊 Metrics: Return=+36.31% | Sharpe=1.098 | DD=6.53% | Turnover=36.17%
   🎚️ Intra-Step TAPE: potential=0.2211 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0339 | critic_loss=0.0046 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0879 | ema=0.5937 | best_ema=0.5937 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00241_shp0p729_actor.weights.h5 (Sharpe=0.729, MDD=16.93%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00244_shp1p033_actor.weights.h5 (Sharpe=1.033, MDD=9.54%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00248_shp0p782_actor.weights.h5 (Sharpe=0.782, MDD=9.62%)
[CYCLE] Update 174/348 | Step 187,992/500,000 | Episode 248 | Time: 17931.6s
   📊 Metrics: Return=+30.66% | Sharpe=0.782 | DD=9.62% | Turnover=36.18%
   🎚️ Intra-Step TAPE: potential=0.2385 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0358 | critic_loss=0.0216 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7721 | ema=0.6115 | best_ema=0.6115 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.03 | range=[0.96, 8.72] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.83 | AMZN=1.64 | CAT=1.55  BOT: NEE=1.12 | XOM=1.12 | KO=1.09
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0233, db=0.0158, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=85 (33.2%), low_vol=101 (39.5%), medium_vol=70 (27.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.63% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4169
[CYCLE] Update 175/348 | Step 189,504/500,000 | Episode 248 | Time: 18068.7s
   📊 Metrics: Return=-1.61% | Sharpe=-0.421 | DD=5.60% | Turnover=34.84%
   🎚️ Intra-Step TAPE: potential=0.2892 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0288 | critic_loss=0.0065 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4215 | ema=0.5082 | best_ema=0.5082 | no_improve=0

📚 EPISODE HORIZON UPDATE at 191,016 steps:
   Episode horizon: 782 steps
[CYCLE] Update 176/348 | Step 191,016/500,000 | Episode 248 | Time: 18205.8s
   📊 Metrics: Return=-0.24% | Sharpe=-0.176 | DD=9.51% | Turnover=35.95%
   🎚️ Intra-Step TAPE: potential=0.2507 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0356 | critic_loss=0.0054 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0027 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1841 | ema=0.4390 | best_ema=0.4390 | no_improve=0
   🔬 Alpha Diversity: mean=1.97 | std=2.06 | range=[0.97, 8.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.78 | NVDA=1.61 | MSFT=1.49  BOT: XOM=1.14 | KO=1.12 | GLD=1.07
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0236, db=0.0161, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=85 (33.2%), low_vol=101 (39.5%), medium_vol=70 (27.3%)

📚 EPISODE HORIZON UPDATE at 192,528 steps:
   Episode horizon: 820 steps
[CYCLE] Update 177/348 | Step 192,528/500,000 | Episode 248 | Time: 18342.7s
   📊 Metrics: Return=+6.69% | Sharpe=0.111 | DD=10.79% | Turnover=36.06%
   🎚️ Intra-Step TAPE: potential=0.6749 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0335 | critic_loss=0.0050 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1022 | ema=0.4053 | best_ema=0.4053 | no_improve=0

📚 EPISODE HORIZON UPDATE at 194,040 steps:
   Episode horizon: 858 steps
[CYCLE] Update 178/348 | Step 194,040/500,000 | Episode 248 | Time: 18479.7s
   📊 Metrics: Return=+16.25% | Sharpe=0.336 | DD=10.79% | Turnover=36.20%
   🎚️ Intra-Step TAPE: potential=0.2396 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0218 | critic_loss=0.0045 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3253 | ema=0.3973 | best_ema=0.3973 | no_improve=0
   🔬 Alpha Diversity: mean=1.97 | std=2.05 | range=[0.96, 8.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.91 | AMZN=1.66 | MSFT=1.50  BOT: XOM=1.13 | KO=1.10 | GLD=1.06
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0231, db=0.0157, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=85 (33.2%), low_vol=101 (39.5%), medium_vol=70 (27.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00256_shp0p953_actor.weights.h5 (Sharpe=0.953, MDD=9.88%)

📚 EPISODE HORIZON UPDATE at 195,552 steps:
   Episode horizon: 896 steps
[CYCLE] Update 179/348 | Step 195,552/500,000 | Episode 256 | Time: 18616.9s
   📊 Metrics: Return=+44.57% | Sharpe=0.953 | DD=9.88% | Turnover=35.99%
   🎚️ Intra-Step TAPE: potential=0.2422 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0310 | critic_loss=0.0150 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0075 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9447 | ema=0.4520 | best_ema=0.4520 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 11.59% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5054

📚 EPISODE HORIZON UPDATE at 197,064 steps:
   Episode horizon: 934 steps
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 256 | Time: 18754.0s
   📊 Metrics: Return=-10.01% | Sharpe=-0.687 | DD=13.47% | Turnover=36.38%
   🎚️ Intra-Step TAPE: potential=0.4331 | delta_reward=+0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0372 | critic_loss=0.0040 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0020 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.6991 | ema=0.3369 | best_ema=0.3369 | no_improve=0
   🔬 Alpha Diversity: mean=1.96 | std=2.08 | range=[0.98, 8.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.64 | AMZN=1.52 | JPM=1.43  BOT: NEE=1.14 | KO=1.13 | GLD=1.10
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0225, db=0.0155, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=87 (33.0%), low_vol=103 (39.0%), medium_vol=74 (28.0%)

📚 EPISODE HORIZON UPDATE at 198,576 steps:
   Episode horizon: 972 steps
[CYCLE] Update 181/348 | Step 198,576/500,000 | Episode 256 | Time: 18890.7s
   📊 Metrics: Return=-9.78% | Sharpe=-0.542 | DD=15.05% | Turnover=36.09%
   🎚️ Intra-Step TAPE: potential=0.3917 | delta_reward=-0.0024
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0361 | critic_loss=0.0043 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0021 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.5510 | ema=0.2481 | best_ema=0.2481 | no_improve=0

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.05

🧭 REWARD PHASE UPDATE at 200,088 steps:
   B_ramp_1 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.25/t0.00/bm0.20/tt0.00

📚 EPISODE HORIZON UPDATE at 200,088 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 182/348 | Step 200,088/500,000 | Episode 256 | Time: 19027.2s
   📊 Metrics: Return=-5.85% | Sharpe=-0.336 | DD=15.05% | Turnover=36.16%
   🎚️ Intra-Step TAPE: potential=0.3398 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0292 | critic_loss=0.0044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3462 | ema=0.1887 | best_ema=0.1887 | no_improve=0
   🔬 Alpha Diversity: mean=1.97 | std=2.04 | range=[0.95, 8.72] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.72 | NVDA=1.71 | MSFT=1.55  BOT: NEE=1.12 | KO=1.09 | GLD=1.05
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0220, db=0.0152, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=87 (33.0%), low_vol=103 (39.0%), medium_vol=74 (28.0%)
[CYCLE] Update 183/348 | Step 201,600/500,000 | Episode 257 | Time: 19164.1s
   📊 Metrics: Return=+23.30% | Sharpe=0.455 | DD=17.75% | Turnover=35.72%
   🎚️ Intra-Step TAPE: potential=0.2381 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0313 | critic_loss=0.0084 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0042 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4483 | ema=0.2147 | best_ema=0.2147 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 9.26% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.2791
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=0.00352) | SPY shaping=-0.000 (SPY ret=0.00243)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00258_shp0p811_actor.weights.h5 (Sharpe=0.811, MDD=15.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00263_shp0p788_actor.weights.h5 (Sharpe=0.788, MDD=8.14%)
[CYCLE] Update 184/348 | Step 203,112/500,000 | Episode 264 | Time: 19301.5s
   📊 Metrics: Return=+15.49% | Sharpe=0.232 | DD=8.70% | Turnover=35.69%
   🎚️ Intra-Step TAPE: potential=0.2873 | delta_reward=-0.0017
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0298 | critic_loss=0.0134 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0067 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2259 | ema=0.2158 | best_ema=0.2158 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.02 | range=[0.94, 8.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.86 | NVDA=1.80 | MSFT=1.54  BOT: NEE=1.11 | KO=1.08 | GLD=1.05
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0232, db=0.0158, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=90 (33.1%), low_vol=106 (39.0%), medium_vol=76 (27.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.04% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2633
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=0.00269) | SPY shaping=-0.000 (SPY ret=0.00224)
[CYCLE] Update 185/348 | Step 204,624/500,000 | Episode 264 | Time: 19438.3s
   📊 Metrics: Return=-2.03% | Sharpe=-0.251 | DD=12.84% | Turnover=36.33%
   🎚️ Intra-Step TAPE: potential=0.6654 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0341 | critic_loss=0.0068 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2626 | ema=0.1680 | best_ema=0.1680 | no_improve=0
[CYCLE] Update 186/348 | Step 206,136/500,000 | Episode 264 | Time: 19574.9s
   📊 Metrics: Return=+2.87% | Sharpe=0.017 | DD=12.84% | Turnover=36.48%
   🎚️ Intra-Step TAPE: potential=0.2308 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0339 | critic_loss=0.0037 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0018 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0045 | ema=0.1516 | best_ema=0.1516 | no_improve=0
   🔬 Alpha Diversity: mean=1.97 | std=2.04 | range=[0.94, 8.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.78 | AMZN=1.73 | MSFT=1.40  BOT: NEE=1.12 | KO=1.11 | GLD=1.08
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0238, db=0.0164, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=90 (33.1%), low_vol=106 (39.0%), medium_vol=76 (27.9%)
[CYCLE] Update 187/348 | Step 207,648/500,000 | Episode 264 | Time: 19711.4s
   📊 Metrics: Return=+1.12% | Sharpe=-0.063 | DD=14.61% | Turnover=36.12%
   🎚️ Intra-Step TAPE: potential=0.2464 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0316 | critic_loss=0.0031 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0016 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0730 | ema=0.1292 | best_ema=0.1292 | no_improve=0
[CYCLE] Update 188/348 | Step 209,160/500,000 | Episode 264 | Time: 19848.1s
   📊 Metrics: Return=-4.05% | Sharpe=-0.215 | DD=15.71% | Turnover=35.98%
   🎚️ Intra-Step TAPE: potential=0.2354 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0392 | critic_loss=0.0036 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0018 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2236 | ema=0.0939 | best_ema=0.0939 | no_improve=0
   🔬 Alpha Diversity: mean=1.98 | std=2.03 | range=[0.95, 8.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.08 | AMZN=1.66 | JPM=1.45  BOT: NEE=1.10 | KO=1.07 | GLD=1.05
   🧬 FiLM: seq(dg=0.0007, db=0.0005, sat=0.0%) | latent(dg=0.0239, db=0.0163, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=90 (33.1%), low_vol=106 (39.0%), medium_vol=76 (27.9%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00265_shp0p916_actor.weights.h5 (Sharpe=0.916, MDD=8.61%)
[CYCLE] Update 189/348 | Step 210,672/500,000 | Episode 272 | Time: 19985.2s
   📊 Metrics: Return=+27.52% | Sharpe=0.508 | DD=10.51% | Turnover=36.12%
   🎚️ Intra-Step TAPE: potential=0.7397 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0384 | critic_loss=0.0283 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0142 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4987 | ema=0.1344 | best_ema=0.1344 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.39% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3139
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=-0.00065) | SPY shaping=-0.000 (SPY ret=-0.00032)
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 272 | Time: 20121.8s
   📊 Metrics: Return=-1.55% | Sharpe=-0.413 | DD=7.23% | Turnover=36.10%
   🎚️ Intra-Step TAPE: potential=0.5564 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0330 | critic_loss=0.0091 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4224 | ema=0.0787 | best_ema=0.0787 | no_improve=0
   🔬 Alpha Diversity: mean=1.99 | std=2.00 | range=[0.94, 8.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.83 | NVDA=1.81 | CAT=1.72  BOT: NEE=1.10 | KO=1.07 | GLD=1.06
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0244, db=0.0165, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=93 (33.2%), low_vol=110 (39.3%), medium_vol=77 (27.5%)
[CYCLE] Update 191/348 | Step 213,696/500,000 | Episode 272 | Time: 20258.9s
   📊 Metrics: Return=+3.68% | Sharpe=0.080 | DD=9.09% | Turnover=36.32%
   🎚️ Intra-Step TAPE: potential=0.2341 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0321 | critic_loss=0.0044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0685 | ema=0.0777 | best_ema=0.0777 | no_improve=0
[CYCLE] Update 192/348 | Step 215,208/500,000 | Episode 272 | Time: 20395.4s
   📊 Metrics: Return=+18.75% | Sharpe=0.583 | DD=9.09% | Turnover=36.02%
   🎚️ Intra-Step TAPE: potential=0.7223 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0338 | critic_loss=0.0034 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5744 | ema=0.1273 | best_ema=0.1273 | no_improve=0
   🔬 Alpha Diversity: mean=1.97 | std=2.03 | range=[0.93, 8.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.71 | NVDA=1.63 | JPM=1.60  BOT: NEE=1.12 | KO=1.10 | GLD=1.06
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0244, db=0.0165, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=93 (33.2%), low_vol=110 (39.3%), medium_vol=77 (27.5%)
[CYCLE] Update 193/348 | Step 216,720/500,000 | Episode 272 | Time: 20532.0s
   📊 Metrics: Return=+30.49% | Sharpe=0.734 | DD=9.09% | Turnover=35.94%
   🎚️ Intra-Step TAPE: potential=0.4377 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0263 | critic_loss=0.0039 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0019 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7260 | ema=0.1872 | best_ema=0.1872 | no_improve=0
[CYCLE] Update 194/348 | Step 218,232/500,000 | Episode 273 | Time: 20668.9s
   📊 Metrics: Return=+16.37% | Sharpe=0.246 | DD=10.62% | Turnover=36.05%
   🎚️ Intra-Step TAPE: potential=0.2666 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0318 | critic_loss=0.0108 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2365 | ema=0.1921 | best_ema=0.1921 | no_improve=0
   🔬 Alpha Diversity: mean=1.97 | std=2.03 | range=[0.93, 8.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.78 | NVDA=1.73 | MSFT=1.65  BOT: XOM=1.09 | KO=1.08 | GLD=1.04
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0234, db=0.0159, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=94 (33.5%), low_vol=110 (39.1%), medium_vol=77 (27.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.80% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2609
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=0.00255) | SPY shaping=-0.001 (SPY ret=0.00333)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00275_shp0p846_actor.weights.h5 (Sharpe=0.846, MDD=9.09%)
[CYCLE] Update 195/348 | Step 219,744/500,000 | Episode 280 | Time: 20806.3s
   📊 Metrics: Return=+10.60% | Sharpe=0.104 | DD=13.61% | Turnover=36.26%
   🎚️ Intra-Step TAPE: potential=0.7508 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0370 | critic_loss=0.0316 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0158 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0931 | ema=0.1822 | best_ema=0.1822 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.41% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2508
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=0.00367) | SPY shaping=-0.000 (SPY ret=0.00305)
[CYCLE] Update 196/348 | Step 221,256/500,000 | Episode 280 | Time: 20943.3s
   📊 Metrics: Return=+3.40% | Sharpe=0.103 | DD=15.95% | Turnover=36.60%
   🎚️ Intra-Step TAPE: potential=0.2311 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0328 | critic_loss=0.0072 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0036 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0890 | ema=0.1729 | best_ema=0.1729 | no_improve=0
   🔬 Alpha Diversity: mean=1.97 | std=2.04 | range=[0.95, 8.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.74 | NVDA=1.72 | MSFT=1.44  BOT: NEE=1.13 | KO=1.11 | GLD=1.04
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0238, db=0.0163, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (33.7%), low_vol=111 (38.5%), medium_vol=80 (27.8%)
[CYCLE] Update 197/348 | Step 222,768/500,000 | Episode 280 | Time: 21081.9s
   📊 Metrics: Return=-0.31% | Sharpe=-0.114 | DD=17.13% | Turnover=36.48%
   🎚️ Intra-Step TAPE: potential=0.2440 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0358 | critic_loss=0.0043 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1270 | ema=0.1429 | best_ema=0.1429 | no_improve=0
[CYCLE] Update 198/348 | Step 224,280/500,000 | Episode 280 | Time: 21218.9s
   📊 Metrics: Return=-0.15% | Sharpe=-0.124 | DD=18.20% | Turnover=36.22%
   🎚️ Intra-Step TAPE: potential=0.2288 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0338 | critic_loss=0.0055 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0027 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1344 | ema=0.1152 | best_ema=0.1152 | no_improve=0
   🔬 Alpha Diversity: mean=1.97 | std=2.04 | range=[0.93, 8.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.80 | AMZN=1.72 | JPM=1.48  BOT: NEE=1.11 | KO=1.09 | GLD=1.01
   🧬 FiLM: seq(dg=0.0007, db=0.0006, sat=0.0%) | latent(dg=0.0243, db=0.0165, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (33.7%), low_vol=111 (38.5%), medium_vol=80 (27.8%)
[CYCLE] Update 199/348 | Step 225,792/500,000 | Episode 281 | Time: 21355.6s
   📊 Metrics: Return=+12.92% | Sharpe=0.148 | DD=16.90% | Turnover=36.46%
   🎚️ Intra-Step TAPE: potential=0.2431 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0295 | critic_loss=0.0066 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1351 | ema=0.1172 | best_ema=0.1172 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.009, dd 14.20% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2465
   📈 Benchmark Relative: 1/N shaping=0.007 (EW ret=-0.01135) | SPY shaping=0.003 (SPY ret=-0.01461)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00286_shp0p894_actor.weights.h5 (Sharpe=0.894, MDD=9.59%)
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 288 | Time: 21493.4s
   📊 Metrics: Return=+15.52% | Sharpe=0.208 | DD=11.28% | Turnover=36.21%
   🎚️ Intra-Step TAPE: potential=0.7115 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0384 | critic_loss=0.0145 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0072 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1979 | ema=0.1253 | best_ema=0.1253 | no_improve=0
   🔬 Alpha Diversity: mean=1.95 | std=2.07 | range=[0.92, 8.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.63 | AMZN=1.49 | JPM=1.45  BOT: NEE=1.16 | KO=1.14 | GLD=1.03
   🧬 FiLM: seq(dg=0.0008, db=0.0006, sat=0.0%) | latent(dg=0.0241, db=0.0164, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (34.1%), low_vol=112 (37.8%), medium_vol=83 (28.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.66% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2639
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.00425) | SPY shaping=0.001 (SPY ret=-0.00430)
[CYCLE] Update 201/348 | Step 228,816/500,000 | Episode 288 | Time: 21632.0s
   📊 Metrics: Return=-2.08% | Sharpe=-0.238 | DD=14.72% | Turnover=36.26%
   🎚️ Intra-Step TAPE: potential=0.2336 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0301 | critic_loss=0.0069 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0034 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0209
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2487 | ema=0.0879 | best_ema=0.0879 | no_improve=0
[CYCLE] Update 202/348 | Step 230,328/500,000 | Episode 288 | Time: 21772.8s
   📊 Metrics: Return=+14.75% | Sharpe=0.519 | DD=14.72% | Turnover=36.46%
   🎚️ Intra-Step TAPE: potential=0.5507 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0404 | critic_loss=0.0047 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0209
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5068 | ema=0.1298 | best_ema=0.1298 | no_improve=0
   🔬 Alpha Diversity: mean=1.95 | std=2.09 | range=[0.97, 8.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.56 | AMZN=1.55 | JPM=1.40  BOT: XOM=1.15 | KO=1.12 | GLD=1.06
   🧬 FiLM: seq(dg=0.0008, db=0.0006, sat=0.0%) | latent(dg=0.0245, db=0.0167, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (34.1%), low_vol=112 (37.8%), medium_vol=83 (28.0%)
[CYCLE] Update 203/348 | Step 231,840/500,000 | Episode 288 | Time: 21914.0s
   📊 Metrics: Return=+1.36% | Sharpe=-0.044 | DD=15.92% | Turnover=36.58%
   🎚️ Intra-Step TAPE: potential=0.2482 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0260 | critic_loss=0.0096 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0579 | ema=0.1110 | best_ema=0.1110 | no_improve=0
[CYCLE] Update 204/348 | Step 233,352/500,000 | Episode 288 | Time: 22054.9s
   📊 Metrics: Return=+6.62% | Sharpe=0.057 | DD=15.92% | Turnover=36.53%
   🎚️ Intra-Step TAPE: potential=0.5321 | delta_reward=+0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0344 | critic_loss=0.0050 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0440 | ema=0.1043 | best_ema=0.1043 | no_improve=0
   🔬 Alpha Diversity: mean=1.96 | std=2.06 | range=[0.93, 8.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.72 | NVDA=1.60 | MSFT=1.51  BOT: NEE=1.14 | KO=1.08 | GLD=1.02
   🧬 FiLM: seq(dg=0.0008, db=0.0006, sat=0.0%) | latent(dg=0.0248, db=0.0168, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (34.1%), low_vol=112 (37.8%), medium_vol=83 (28.0%)
[CYCLE] Update 205/348 | Step 234,864/500,000 | Episode 296 | Time: 22196.2s
   📊 Metrics: Return=-6.58% | Sharpe=-0.321 | DD=10.53% | Turnover=36.52%
   🎚️ Intra-Step TAPE: potential=0.2356 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0393 | critic_loss=0.0186 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0093 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3345 | ema=0.0604 | best_ema=0.0604 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.58% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2418
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.01032) | SPY shaping=0.002 (SPY ret=-0.01678)
[CYCLE] Update 206/348 | Step 236,376/500,000 | Episode 296 | Time: 22334.0s
   📊 Metrics: Return=-4.13% | Sharpe=-0.871 | DD=7.74% | Turnover=37.69%
   🎚️ Intra-Step TAPE: potential=0.2362 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0318 | critic_loss=0.0067 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.8937 | ema=-0.0350 | best_ema=-0.0350 | no_improve=0
   🔬 Alpha Diversity: mean=1.96 | std=2.04 | range=[0.93, 8.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.73 | NVDA=1.64 | CAT=1.49  BOT: NEE=1.11 | KO=1.06 | GLD=1.04
   🧬 FiLM: seq(dg=0.0008, db=0.0006, sat=0.0%) | latent(dg=0.0250, db=0.0170, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (34.2%), low_vol=115 (37.8%), medium_vol=85 (28.0%)
[CYCLE] Update 207/348 | Step 237,888/500,000 | Episode 296 | Time: 22471.2s
   📊 Metrics: Return=-4.11% | Sharpe=-0.543 | DD=8.27% | Turnover=36.19%
   🎚️ Intra-Step TAPE: potential=0.2448 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0340 | critic_loss=0.0043 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.5531 | ema=-0.0868 | best_ema=-0.0868 | no_improve=0
[CYCLE] Update 208/348 | Step 239,400/500,000 | Episode 296 | Time: 22608.8s
   📊 Metrics: Return=-3.28% | Sharpe=-0.301 | DD=12.35% | Turnover=35.88%
   🎚️ Intra-Step TAPE: potential=0.7382 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0319 | critic_loss=0.0032 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0016 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3089 | ema=-0.1090 | best_ema=-0.1090 | no_improve=0
   🔬 Alpha Diversity: mean=1.96 | std=2.05 | range=[0.93, 8.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.84 | AMZN=1.65 | MSFT=1.43  BOT: NEE=1.10 | KO=1.07 | GLD=1.03
   🧬 FiLM: seq(dg=0.0008, db=0.0006, sat=0.0%) | latent(dg=0.0260, db=0.0177, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (34.2%), low_vol=115 (37.8%), medium_vol=85 (28.0%)

🧭 REWARD PHASE UPDATE at 240,912 steps:
   B_ramp_2 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.55/t0.00/bm0.45/tt0.00
[CYCLE] Update 209/348 | Step 240,912/500,000 | Episode 296 | Time: 22746.0s
   📊 Metrics: Return=+14.19% | Sharpe=0.284 | DD=12.35% | Turnover=35.87%
   🎚️ Intra-Step TAPE: potential=0.7503 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0423 | critic_loss=0.0031 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0016 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2765 | ema=-0.0705 | best_ema=-0.0705 | no_improve=0
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 297 | Time: 22883.6s
   📊 Metrics: Return=+12.25% | Sharpe=0.135 | DD=16.14% | Turnover=35.83%
   🎚️ Intra-Step TAPE: potential=0.7319 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0260 | critic_loss=0.0097 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1281 | ema=-0.0506 | best_ema=-0.0506 | no_improve=0
   🔬 Alpha Diversity: mean=1.96 | std=2.04 | range=[0.93, 8.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.12 | AMZN=1.59 | MSFT=1.41  BOT: NEE=1.09 | KO=1.07 | GLD=1.05
   🧬 FiLM: seq(dg=0.0008, db=0.0006, sat=0.0%) | latent(dg=0.0257, db=0.0175, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (34.1%), low_vol=115 (37.7%), medium_vol=86 (28.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.11% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2465
   📈 Benchmark Relative: 1/N shaping=-0.005 (EW ret=0.00071) | SPY shaping=-0.001 (SPY ret=0.00000)
[CYCLE] Update 211/348 | Step 243,936/500,000 | Episode 304 | Time: 23021.1s
   📊 Metrics: Return=+0.72% | Sharpe=-0.103 | DD=16.43% | Turnover=36.51%
   🎚️ Intra-Step TAPE: potential=0.2413 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0357 | critic_loss=0.0193 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0096 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1154 | ema=-0.0571 | best_ema=-0.0571 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.68% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2290
   📈 Benchmark Relative: 1/N shaping=-0.000 (EW ret=0.00103) | SPY shaping=-0.001 (SPY ret=0.00254)
[CYCLE] Update 212/348 | Step 245,448/500,000 | Episode 304 | Time: 23158.8s
   📊 Metrics: Return=+0.18% | Sharpe=-0.132 | DD=8.64% | Turnover=35.43%
   🎚️ Intra-Step TAPE: potential=0.7031 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0314 | critic_loss=0.0060 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0030 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1357 | ema=-0.0650 | best_ema=-0.0650 | no_improve=0
   🔬 Alpha Diversity: mean=1.96 | std=2.04 | range=[0.95, 8.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.81 | NVDA=1.79 | MSFT=1.46  BOT: NEE=1.09 | GLD=1.07 | KO=1.05
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0263, db=0.0178, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=106 (34.0%), low_vol=116 (37.2%), medium_vol=90 (28.8%)
[CYCLE] Update 213/348 | Step 246,960/500,000 | Episode 304 | Time: 23296.4s
   📊 Metrics: Return=+18.04% | Sharpe=0.662 | DD=8.64% | Turnover=35.56%
   🎚️ Intra-Step TAPE: potential=0.7519 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0399 | critic_loss=0.0033 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6576 | ema=0.0073 | best_ema=0.0073 | no_improve=0
[CYCLE] Update 214/348 | Step 248,472/500,000 | Episode 304 | Time: 23433.8s
   📊 Metrics: Return=+32.33% | Sharpe=0.891 | DD=8.64% | Turnover=35.66%
   🎚️ Intra-Step TAPE: potential=0.5799 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0388 | critic_loss=0.0051 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8858 | ema=0.0952 | best_ema=0.0952 | no_improve=0
   🔬 Alpha Diversity: mean=1.95 | std=2.06 | range=[0.98, 8.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.15 | AMZN=1.57 | MSFT=1.33  BOT: XOM=1.10 | GLD=1.08 | KO=1.07
   🧬 FiLM: seq(dg=0.0008, db=0.0007, sat=0.0%) | latent(dg=0.0265, db=0.0181, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=106 (34.0%), low_vol=116 (37.2%), medium_vol=90 (28.8%)
[CYCLE] Update 215/348 | Step 249,984/500,000 | Episode 305 | Time: 23571.5s
   📊 Metrics: Return=-2.54% | Sharpe=-0.179 | DD=18.59% | Turnover=36.08%
   🎚️ Intra-Step TAPE: potential=0.5156 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0306 | critic_loss=0.0089 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0045 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1879 | ema=0.0669 | best_ema=0.0669 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.98% / trig 16.50%) | terminal=0.000 (peak 0.017) | TAPE=0.2339
   📈 Benchmark Relative: 1/N shaping=0.012 (EW ret=-0.01332) | SPY shaping=0.003 (SPY ret=-0.01330)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00309_shp0p856_actor.weights.h5 (Sharpe=0.856, MDD=8.53%)
[CYCLE] Update 216/348 | Step 251,496/500,000 | Episode 312 | Time: 23709.6s
   📊 Metrics: Return=+22.35% | Sharpe=0.299 | DD=18.76% | Turnover=35.93%
   🎚️ Intra-Step TAPE: potential=0.2339 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0298 | critic_loss=0.0151 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0076 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2911 | ema=0.0893 | best_ema=0.0893 | no_improve=0
   🔬 Alpha Diversity: mean=1.95 | std=2.06 | range=[0.94, 8.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.75 | AMZN=1.69 | JPM=1.39  BOT: GLD=1.07 | KO=1.06 | NEE=1.06
   🧬 FiLM: seq(dg=0.0008, db=0.0007, sat=0.0%) | latent(dg=0.0266, db=0.0181, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=108 (33.8%), low_vol=117 (36.6%), medium_vol=95 (29.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.05% / trig 16.50%) | terminal=0.005 (peak 0.023) | TAPE=0.2655
   📈 Benchmark Relative: 1/N shaping=-0.006 (EW ret=0.00509) | SPY shaping=-0.003 (SPY ret=0.00685)
[CYCLE] Update 217/348 | Step 253,008/500,000 | Episode 312 | Time: 23847.1s
   📊 Metrics: Return=-1.01% | Sharpe=-0.351 | DD=5.99% | Turnover=37.01%
   🎚️ Intra-Step TAPE: potential=0.2247 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0321 | critic_loss=0.0058 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3681 | ema=0.0435 | best_ema=0.0893 | no_improve=1
[CYCLE] Update 218/348 | Step 254,520/500,000 | Episode 312 | Time: 23984.7s
   📊 Metrics: Return=-0.07% | Sharpe=-0.244 | DD=6.67% | Turnover=36.59%
   🎚️ Intra-Step TAPE: potential=0.2409 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0257 | critic_loss=0.0059 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0209
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2577 | ema=0.0134 | best_ema=0.0893 | no_improve=2
   🔬 Alpha Diversity: mean=1.94 | std=2.09 | range=[1.00, 8.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.71 | AMZN=1.57 | JPM=1.35  BOT: XOM=1.10 | KO=1.10 | GLD=1.07
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0270, db=0.0184, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=108 (33.8%), low_vol=117 (36.6%), medium_vol=95 (29.7%)
[CYCLE] Update 219/348 | Step 256,032/500,000 | Episode 312 | Time: 24122.2s
   📊 Metrics: Return=-3.73% | Sharpe=-0.383 | DD=8.29% | Turnover=36.54%
   🎚️ Intra-Step TAPE: potential=0.2359 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0313 | critic_loss=0.0116 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0058 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0210
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3958 | ema=-0.0275 | best_ema=0.0893 | no_improve=3
[CYCLE] Update 220/348 | Step 257,544/500,000 | Episode 312 | Time: 24259.4s
   📊 Metrics: Return=+3.68% | Sharpe=-0.062 | DD=9.83% | Turnover=36.38%
   🎚️ Intra-Step TAPE: potential=0.6268 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0277 | critic_loss=0.0060 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0030 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0208
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0741 | ema=-0.0322 | best_ema=0.0893 | no_improve=4
   🔬 Alpha Diversity: mean=1.93 | std=2.10 | range=[0.99, 8.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.64 | AMZN=1.64 | MSFT=1.39  BOT: NEE=1.11 | KO=1.09 | GLD=1.06
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0271, db=0.0185, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=108 (33.8%), low_vol=117 (36.6%), medium_vol=95 (29.7%)
[CYCLE] Update 221/348 | Step 259,056/500,000 | Episode 320 | Time: 24397.2s
   📊 Metrics: Return=+9.64% | Sharpe=0.080 | DD=10.00% | Turnover=35.79%
   🎚️ Intra-Step TAPE: potential=0.2402 | delta_reward=-0.0020
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0329 | critic_loss=0.0113 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0056 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0208
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0737 | ema=-0.0216 | best_ema=0.0893 | no_improve=5
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.75% / trig 16.50%) | terminal=0.000 (peak 0.004) | TAPE=0.2469
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.00409) | SPY shaping=0.000 (SPY ret=-0.00328)
[CYCLE] Update 222/348 | Step 260,568/500,000 | Episode 320 | Time: 24534.7s
   📊 Metrics: Return=-4.83% | Sharpe=-0.607 | DD=11.06% | Turnover=35.82%
   🎚️ Intra-Step TAPE: potential=0.3130 | delta_reward=-0.0023
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0300 | critic_loss=0.0108 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0207
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.6144 | ema=-0.0809 | best_ema=0.0893 | no_improve=6
   🔬 Alpha Diversity: mean=1.93 | std=2.10 | range=[1.00, 8.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.55 | AMZN=1.55 | JPM=1.39  BOT: XOM=1.11 | KO=1.10 | GLD=1.10
   🧬 FiLM: seq(dg=0.0010, db=0.0008, sat=0.0%) | latent(dg=0.0268, db=0.0182, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=111 (33.8%), low_vol=118 (36.0%), medium_vol=99 (30.2%)
[CYCLE] Update 223/348 | Step 262,080/500,000 | Episode 320 | Time: 24672.3s
   📊 Metrics: Return=+0.90% | Sharpe=-0.075 | DD=11.06% | Turnover=36.61%
   🎚️ Intra-Step TAPE: potential=0.2289 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0389 | critic_loss=0.0065 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0206
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0892 | ema=-0.0817 | best_ema=0.0893 | no_improve=7
[CYCLE] Update 224/348 | Step 263,592/500,000 | Episode 320 | Time: 24809.8s
   📊 Metrics: Return=+2.30% | Sharpe=-0.020 | DD=14.10% | Turnover=36.32%
   🎚️ Intra-Step TAPE: potential=0.2518 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0439 | critic_loss=0.0039 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0019 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0209
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0318 | ema=-0.0767 | best_ema=0.0893 | no_improve=8
   🔬 Alpha Diversity: mean=1.93 | std=2.09 | range=[0.98, 8.68] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.70 | AMZN=1.62 | MSFT=1.41  BOT: NEE=1.10 | GLD=1.08 | KO=1.06
   🧬 FiLM: seq(dg=0.0009, db=0.0008, sat=0.0%) | latent(dg=0.0272, db=0.0186, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=111 (33.8%), low_vol=118 (36.0%), medium_vol=99 (30.2%)
[CYCLE] Update 225/348 | Step 265,104/500,000 | Episode 320 | Time: 24947.0s
   📊 Metrics: Return=-0.45% | Sharpe=-0.125 | DD=14.10% | Turnover=36.26%
   🎚️ Intra-Step TAPE: potential=0.2524 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0332 | critic_loss=0.0063 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0208
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1358 | ema=-0.0826 | best_ema=0.0893 | no_improve=9
[CYCLE] Update 226/348 | Step 266,616/500,000 | Episode 321 | Time: 25084.6s
   📊 Metrics: Return=+30.79% | Sharpe=0.552 | DD=13.22% | Turnover=36.10%
   🎚️ Intra-Step TAPE: potential=0.2443 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0381 | critic_loss=0.0075 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0037 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0209
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5422 | ema=-0.0201 | best_ema=0.0893 | no_improve=10
   🔬 Alpha Diversity: mean=1.94 | std=2.08 | range=[0.94, 8.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.86 | AMZN=1.56 | JPM=1.32  BOT: XOM=1.09 | KO=1.08 | GLD=1.08
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0269, db=0.0185, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=112 (34.0%), low_vol=118 (35.9%), medium_vol=99 (30.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 9.94% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3174
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=-0.00183) | SPY shaping=0.001 (SPY ret=-0.00314)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00326_shp0p791_actor.weights.h5 (Sharpe=0.791, MDD=9.30%)
[CYCLE] Update 227/348 | Step 268,128/500,000 | Episode 328 | Time: 25222.2s
   📊 Metrics: Return=+25.11% | Sharpe=0.469 | DD=12.74% | Turnover=35.52%
   🎚️ Intra-Step TAPE: potential=0.2711 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0278 | critic_loss=0.0344 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0172 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0209
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4648 | ema=0.0284 | best_ema=0.0893 | no_improve=11
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.29% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2988
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=-0.00051) | SPY shaping=0.002 (SPY ret=-0.00373)
[CYCLE] Update 228/348 | Step 269,640/500,000 | Episode 328 | Time: 25359.9s
   📊 Metrics: Return=-2.81% | Sharpe=-0.453 | DD=8.58% | Turnover=35.90%
   🎚️ Intra-Step TAPE: potential=0.3031 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0406 | critic_loss=0.0113 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0057 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0205
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4610 | ema=-0.0206 | best_ema=0.0893 | no_improve=12
   🔬 Alpha Diversity: mean=1.92 | std=2.11 | range=[1.00, 8.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.50 | NVDA=1.48 | CAT=1.40  BOT: NEE=1.11 | KO=1.09 | GLD=1.08
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0274, db=0.0188, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=115 (34.2%), low_vol=120 (35.7%), medium_vol=101 (30.1%)
[CYCLE] Update 229/348 | Step 271,152/500,000 | Episode 328 | Time: 25497.2s
   📊 Metrics: Return=+0.26% | Sharpe=-0.198 | DD=8.58% | Turnover=36.13%
   🎚️ Intra-Step TAPE: potential=0.2509 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0350 | critic_loss=0.0098 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0049 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0205
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2076 | ema=-0.0393 | best_ema=0.0893 | no_improve=13
[CYCLE] Update 230/348 | Step 272,664/500,000 | Episode 328 | Time: 25634.5s
   📊 Metrics: Return=-1.26% | Sharpe=-0.279 | DD=8.58% | Turnover=36.25%
   🎚️ Intra-Step TAPE: potential=0.3892 | delta_reward=-0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0299 | critic_loss=0.0096 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0204
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2900 | ema=-0.0644 | best_ema=0.0893 | no_improve=14
   🔬 Alpha Diversity: mean=1.92 | std=2.12 | range=[0.97, 8.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.47 | NVDA=1.43 | JPM=1.38  BOT: NEE=1.12 | KO=1.10 | GLD=1.08
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0278, db=0.0190, sat=0.0%) | asset(dg=0.0017, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=115 (34.2%), low_vol=120 (35.7%), medium_vol=101 (30.1%)
[CYCLE] Update 231/348 | Step 274,176/500,000 | Episode 329 | Time: 25771.9s
   📊 Metrics: Return=+3.15% | Sharpe=-0.033 | DD=16.32% | Turnover=36.34%
   🎚️ Intra-Step TAPE: potential=0.2354 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0292 | critic_loss=0.0111 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0055 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0204
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0442 | ema=-0.0623 | best_ema=0.0893 | no_improve=15
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 8.06% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2435
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=0.00268) | SPY shaping=-0.004 (SPY ret=0.00699)
[CYCLE] Update 232/348 | Step 275,688/500,000 | Episode 336 | Time: 25909.3s
   📊 Metrics: Return=-4.38% | Sharpe=-0.226 | DD=17.75% | Turnover=36.31%
   🎚️ Intra-Step TAPE: potential=0.2336 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0263 | critic_loss=0.0258 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0129 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0204
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2376 | ema=-0.0799 | best_ema=0.0893 | no_improve=16
   🔬 Alpha Diversity: mean=1.92 | std=2.12 | range=[0.97, 8.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.50 | NVDA=1.46 | MSFT=1.32  BOT: XOM=1.12 | KO=1.11 | GLD=1.09
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0270, db=0.0186, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=119 (34.6%), low_vol=122 (35.5%), medium_vol=103 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.61% / trig 16.50%) | terminal=0.000 (peak 0.005) | TAPE=0.2250
   📈 Benchmark Relative: 1/N shaping=-0.003 (EW ret=0.00314) | SPY shaping=-0.002 (SPY ret=0.00533)
[CYCLE] Update 233/348 | Step 277,200/500,000 | Episode 336 | Time: 26046.5s
   📊 Metrics: Return=+3.36% | Sharpe=0.184 | DD=4.25% | Turnover=36.82%
   🎚️ Intra-Step TAPE: potential=0.5311 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0317 | critic_loss=0.0094 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0047 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0204
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1685 | ema=-0.0550 | best_ema=0.0893 | no_improve=17
[CYCLE] Update 234/348 | Step 278,712/500,000 | Episode 336 | Time: 26184.2s
   📊 Metrics: Return=-3.15% | Sharpe=-0.498 | DD=7.85% | Turnover=36.15%
   🎚️ Intra-Step TAPE: potential=0.2323 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0308 | critic_loss=0.0079 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0205
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.5082 | ema=-0.1003 | best_ema=0.0893 | no_improve=18
   🔬 Alpha Diversity: mean=1.92 | std=2.12 | range=[1.00, 8.70] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.54 | AMZN=1.52 | MSFT=1.30  BOT: XOM=1.12 | KO=1.10 | GLD=1.08
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0274, db=0.0187, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=119 (34.6%), low_vol=122 (35.5%), medium_vol=103 (29.9%)

🧭 REWARD PHASE UPDATE at 280,224 steps:
   B_full | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d1.00/t0.00/bm0.75/tt0.00
[CYCLE] Update 235/348 | Step 280,224/500,000 | Episode 336 | Time: 26321.5s
   📊 Metrics: Return=-1.10% | Sharpe=-0.293 | DD=9.39% | Turnover=36.02%
   🎚️ Intra-Step TAPE: potential=0.2772 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0342 | critic_loss=0.0050 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0207
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3020 | ema=-0.1205 | best_ema=0.0893 | no_improve=19
[CYCLE] Update 236/348 | Step 281,736/500,000 | Episode 336 | Time: 26458.6s
   📊 Metrics: Return=+8.08% | Sharpe=0.083 | DD=9.41% | Turnover=35.89%
   🎚️ Intra-Step TAPE: potential=0.7241 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0300 | critic_loss=0.0161 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0081 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0209
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0751 | ema=-0.1009 | best_ema=0.0893 | no_improve=20
   🔬 Alpha Diversity: mean=1.93 | std=2.08 | range=[0.95, 8.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.73 | AMZN=1.65 | MSFT=1.35  BOT: NEE=1.10 | KO=1.08 | GLD=1.05
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0275, db=0.0186, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=119 (34.6%), low_vol=122 (35.5%), medium_vol=103 (29.9%)
[CYCLE] Update 237/348 | Step 283,248/500,000 | Episode 344 | Time: 26596.0s
   📊 Metrics: Return=-6.07% | Sharpe=-0.378 | DD=11.40% | Turnover=36.08%
   🎚️ Intra-Step TAPE: potential=0.3770 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0288 | critic_loss=0.0271 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0135 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3870 | ema=-0.1296 | best_ema=0.0893 | no_improve=21
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2422
   📈 Benchmark Relative: 1/N shaping=-0.006 (EW ret=0.00237) | SPY shaping=-0.000 (SPY ret=0.00133)
[CYCLE] Update 238/348 | Step 284,760/500,000 | Episode 344 | Time: 26733.2s
   📊 Metrics: Return=+3.13% | Sharpe=0.245 | DD=4.65% | Turnover=35.49%
   🎚️ Intra-Step TAPE: potential=0.4110 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0271 | critic_loss=0.0122 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0061 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0207
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2409 | ema=-0.0925 | best_ema=0.0893 | no_improve=22
   🔬 Alpha Diversity: mean=1.92 | std=2.09 | range=[0.92, 8.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.59 | NVDA=1.54 | JPM=1.42  BOT: NEE=1.10 | KO=1.08 | GLD=1.04
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0276, db=0.0187, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=122 (34.7%), low_vol=125 (35.5%), medium_vol=105 (29.8%)
[CYCLE] Update 239/348 | Step 286,272/500,000 | Episode 344 | Time: 26870.3s
   📊 Metrics: Return=+4.00% | Sharpe=0.101 | DD=5.30% | Turnover=35.75%
   🎚️ Intra-Step TAPE: potential=0.2413 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0332 | critic_loss=0.0111 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0056 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0209
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0942 | ema=-0.0738 | best_ema=0.0893 | no_improve=23
[CYCLE] Update 240/348 | Step 287,784/500,000 | Episode 344 | Time: 27007.9s
   📊 Metrics: Return=+3.17% | Sharpe=-0.052 | DD=7.27% | Turnover=36.15%
   🎚️ Intra-Step TAPE: potential=0.2385 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0254 | critic_loss=0.0072 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0036 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0210
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0615 | ema=-0.0726 | best_ema=0.0893 | no_improve=24
   🔬 Alpha Diversity: mean=1.93 | std=2.07 | range=[0.93, 8.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.81 | AMZN=1.69 | MSFT=1.39  BOT: NEE=1.10 | KO=1.06 | GLD=1.03
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0279, db=0.0189, sat=0.0%) | asset(dg=0.0019, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=122 (34.7%), low_vol=125 (35.5%), medium_vol=105 (29.8%)
[CYCLE] Update 241/348 | Step 289,296/500,000 | Episode 344 | Time: 27144.9s
   📊 Metrics: Return=+4.39% | Sharpe=-0.040 | DD=7.27% | Turnover=35.82%
   🎚️ Intra-Step TAPE: potential=0.2486 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0355 | critic_loss=0.0083 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0041 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0473 | ema=-0.0701 | best_ema=0.0893 | no_improve=25
[CYCLE] Update 242/348 | Step 290,808/500,000 | Episode 345 | Time: 27282.3s
   📊 Metrics: Return=-8.18% | Sharpe=-0.366 | DD=13.47% | Turnover=36.52%
   🎚️ Intra-Step TAPE: potential=0.7327 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0405 | critic_loss=0.0092 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3791 | ema=-0.1010 | best_ema=0.0893 | no_improve=26
   🔬 Alpha Diversity: mean=1.93 | std=2.06 | range=[0.92, 8.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.06 | AMZN=1.56 | MSFT=1.30  BOT: NEE=1.09 | KO=1.07 | GLD=1.03
   🧬 FiLM: seq(dg=0.0008, db=0.0007, sat=0.0%) | latent(dg=0.0274, db=0.0187, sat=0.0%) | asset(dg=0.0020, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=123 (34.8%), low_vol=125 (35.4%), medium_vol=105 (29.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.52% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2344
   📈 Benchmark Relative: 1/N shaping=-0.014 (EW ret=0.00439) | SPY shaping=-0.000 (SPY ret=0.00162)
[CYCLE] Update 243/348 | Step 292,320/500,000 | Episode 352 | Time: 27420.2s
   📊 Metrics: Return=+24.33% | Sharpe=0.439 | DD=11.50% | Turnover=36.06%
   🎚️ Intra-Step TAPE: potential=0.2353 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0337 | critic_loss=0.0212 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0106 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0208
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4303 | ema=-0.0478 | best_ema=0.0893 | no_improve=27
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.31% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2929
   📈 Benchmark Relative: 1/N shaping=-0.000 (EW ret=0.00268) | SPY shaping=-0.007 (SPY ret=0.00850)
[CYCLE] Update 244/348 | Step 293,832/500,000 | Episode 352 | Time: 27557.7s
   📊 Metrics: Return=-2.45% | Sharpe=-0.476 | DD=8.98% | Turnover=35.64%
   🎚️ Intra-Step TAPE: potential=0.2425 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0213 | critic_loss=0.0079 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0205
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.4819 | ema=-0.0913 | best_ema=0.0893 | no_improve=28
   🔬 Alpha Diversity: mean=1.91 | std=2.11 | range=[0.95, 8.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.50 | NVDA=1.48 | JPM=1.31  BOT: NEE=1.12 | KO=1.09 | GLD=1.06
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0277, db=0.0191, sat=0.0%) | asset(dg=0.0018, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=126 (35.0%), low_vol=129 (35.8%), medium_vol=105 (29.2%)
[CYCLE] Update 245/348 | Step 295,344/500,000 | Episode 352 | Time: 27695.1s
   📊 Metrics: Return=-0.80% | Sharpe=-0.211 | DD=13.63% | Turnover=36.10%
   🎚️ Intra-Step TAPE: potential=0.7055 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0322 | critic_loss=0.0063 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0202
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2204 | ema=-0.1042 | best_ema=0.0893 | no_improve=29
[CYCLE] Update 246/348 | Step 296,856/500,000 | Episode 352 | Time: 27832.4s
   📊 Metrics: Return=+8.77% | Sharpe=0.155 | DD=13.63% | Turnover=36.08%
   🎚️ Intra-Step TAPE: potential=0.5562 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0269 | critic_loss=0.0065 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0032 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0203
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1459 | ema=-0.0792 | best_ema=0.0893 | no_improve=30
   🔬 Alpha Diversity: mean=1.90 | std=2.13 | range=[0.96, 8.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.47 | AMZN=1.44 | MSFT=1.31  BOT: XOM=1.13 | KO=1.12 | GLD=1.06
   🧬 FiLM: seq(dg=0.0008, db=0.0007, sat=0.0%) | latent(dg=0.0278, db=0.0194, sat=0.0%) | asset(dg=0.0019, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=126 (35.0%), low_vol=129 (35.8%), medium_vol=105 (29.2%)
[CYCLE] Update 247/348 | Step 298,368/500,000 | Episode 353 | Time: 27969.8s
   📊 Metrics: Return=-2.52% | Sharpe=-0.273 | DD=14.53% | Turnover=35.97%
   🎚️ Intra-Step TAPE: potential=0.7535 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0346 | critic_loss=0.0075 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0038 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0202
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2818 | ema=-0.0994 | best_ema=0.0893 | no_improve=31
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2314
   📈 Benchmark Relative: 1/N shaping=0.009 (EW ret=-0.00095) | SPY shaping=0.002 (SPY ret=-0.00062)
[CYCLE] Update 248/348 | Step 299,880/500,000 | Episode 360 | Time: 28107.2s
   📊 Metrics: Return=-8.24% | Sharpe=-0.376 | DD=21.36% | Turnover=36.04%
   🎚️ Intra-Step TAPE: potential=0.2440 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0335 | critic_loss=0.0233 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0117 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0203
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3852 | ema=-0.1280 | best_ema=0.0893 | no_improve=32
   🔬 Alpha Diversity: mean=1.90 | std=2.12 | range=[0.99, 8.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.50 | NVDA=1.46 | JPM=1.29  BOT: XOM=1.13 | KO=1.12 | GLD=1.06
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0274, db=0.0192, sat=0.0%) | asset(dg=0.0019, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=129 (35.1%), low_vol=131 (35.6%), medium_vol=108 (29.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.37% / trig 16.50%) | terminal=0.680 (peak 0.680) | TAPE=0.2218
   📈 Benchmark Relative: 1/N shaping=-0.033 (EW ret=0.01890) | SPY shaping=-0.007 (SPY ret=0.01749)

🎛️ EXECUTION BETA UPDATE at 301,392 steps:
   action_execution_beta: 0.800 (w_exec=(1-β)w_prev + βw_raw)
[CYCLE] Update 249/348 | Step 301,392/500,000 | Episode 360 | Time: 28244.6s
   📊 Metrics: Return=+4.31% | Sharpe=0.239 | DD=7.38% | Turnover=36.29%
   🎚️ Intra-Step TAPE: potential=0.7269 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0348 | critic_loss=0.0096 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0048 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0202
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2281 | ema=-0.0924 | best_ema=0.0893 | no_improve=33

📚 PPO ROLLOUT UPDATE at 301,392 steps:
   Timesteps per update: 2016

📚 PPO BATCH SIZE UPDATE at 301,392 steps:
   Batch size: 504

🎯 ENTROPY COEF UPDATE at 301,392 steps:
   entropy_coef: 0.0003

🧪 AUX-RETURN COEF UPDATE at 301,392 steps:
   aux_return_pred_coef: 0.2500

🌡️ TEMPERATURE UPDATE at 301,392 steps:
   temperature: 0.8000
[CYCLE] Update 250/348 | Step 303,408/500,000 | Episode 360 | Time: 28413.5s
   📊 Metrics: Return=+9.53% | Sharpe=0.312 | DD=7.38% | Turnover=41.49%
   🎚️ Intra-Step TAPE: potential=0.2249 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0265 | critic_loss=0.0085 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0042 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0201
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2566 | ema=-0.0575 | best_ema=0.0893 | no_improve=34
   🔬 Alpha Diversity: mean=1.90 | std=2.14 | range=[0.98, 8.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=1.49 | AMZN=1.35 | JPM=1.27  BOT: NEE=1.15 | KO=1.13 | GLD=1.07
   🧬 FiLM: seq(dg=0.0009, db=0.0007, sat=0.0%) | latent(dg=0.0280, db=0.0195, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=129 (35.1%), low_vol=131 (35.6%), medium_vol=108 (29.3%)
[CYCLE] Update 251/348 | Step 305,424/500,000 | Episode 360 | Time: 28571.2s
   📊 Metrics: Return=+16.13% | Sharpe=0.368 | DD=8.32% | Turnover=43.19%
   🎚️ Intra-Step TAPE: potential=0.2251 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0244 | critic_loss=0.0112 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0056 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0201
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2980 | ema=-0.0219 | best_ema=0.0893 | no_improve=35
[CYCLE] Update 252/348 | Step 307,440/500,000 | Episode 368 | Time: 28729.4s
   📊 Metrics: Return=-17.28% | Sharpe=-0.566 | DD=28.55% | Turnover=44.16%
   🎚️ Intra-Step TAPE: potential=0.2357 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0266 | critic_loss=0.0215 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0202
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.7296 | ema=-0.0927 | best_ema=0.0893 | no_improve=36
   🔬 Alpha Diversity: mean=1.90 | std=2.14 | range=[0.97, 8.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=1.41 | NVDA=1.40 | MSFT=1.32  BOT: NEE=1.14 | KO=1.13 | GLD=1.06
   🧬 FiLM: seq(dg=0.0009, db=0.0008, sat=0.0%) | latent(dg=0.0280, db=0.0195, sat=0.0%) | asset(dg=0.0018, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=134 (35.6%), low_vol=134 (35.6%), medium_vol=108 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.021, dd 6.19% / trig 16.50%) | terminal=2.217 (peak 2.217) | TAPE=0.2087
   📈 Benchmark Relative: 1/N shaping=-0.015 (EW ret=0.00411) | SPY shaping=-0.006 (SPY ret=0.00644)