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
      260,000+ steps: B_ramp_2 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.60/t0.00/bm0.50/tt0.00
      320,000+ steps: C_ramp_1 | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t0.15/bm0.75/tt0.15
      380,000+ steps: C_ramp_2 | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t0.45/bm1.00/tt0.45
      440,000+ steps: C_full_tape | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t1.00/bm1.00/tt1.00
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
   [MOE] Objective expert mask initialized to [1.0, 0.0, 0.0]
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
   [DOWN] Distributional critic: enabled=False | num_quantiles=17
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
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260324_222948_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260324_222948_step_diagnostics.csv

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
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260324_222948_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260324_222948_metadata.json
[CYCLE] Update 1/348 | Step 1,008/500,000 | Episode 0 | Time: 156.3s
   📊 Metrics: Return=+4.78% | Sharpe=0.555 | DD=6.48% | Turnover=23.31%
   🎚️ Intra-Step TAPE: potential=0.6312 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1104 | critic_loss=2.1462 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.0731 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0283
   🧠 Objective Experts: aux_loss=-0.0049 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5551 | ema=0.5551 | best_ema=0.5551 | no_improve=0
[CYCLE] Update 2/348 | Step 2,016/500,000 | Episode 0 | Time: 294.5s
   📊 Metrics: Return=+18.22% | Sharpe=0.948 | DD=10.25% | Turnover=23.87%
   🎚️ Intra-Step TAPE: potential=0.7486 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0926 | critic_loss=1.9808 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.9904 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0293
   🧠 Objective Experts: aux_loss=-0.0024 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9478 | ema=0.5944 | best_ema=0.5944 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=1.45 | range=[1.25, 8.20] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.84 | NVDA=4.21 | MSFT=3.19  BOT: NEE=1.81 | GLD=1.69 | KO=1.68
   🧬 FiLM: seq(dg=0.0001, db=0.0001, sat=0.0%) | latent(dg=0.0004, db=0.0002, sat=0.0%) | asset(dg=0.0002, db=0.0001, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=1 (12.5%), low_vol=6 (75.0%), medium_vol=1 (12.5%)
[CYCLE] Update 3/348 | Step 3,024/500,000 | Episode 0 | Time: 433.0s
   📊 Metrics: Return=+34.10% | Sharpe=1.109 | DD=13.80% | Turnover=24.35%
   🎚️ Intra-Step TAPE: potential=0.7467 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0896 | critic_loss=1.5782 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.7891 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0286
   🧠 Objective Experts: aux_loss=0.0065 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1092 | ema=0.6458 | best_ema=0.6458 | no_improve=0
[CYCLE] Update 4/348 | Step 4,032/500,000 | Episode 0 | Time: 571.6s
   📊 Metrics: Return=+66.23% | Sharpe=1.469 | DD=13.80% | Turnover=24.31%
   🎚️ Intra-Step TAPE: potential=0.7433 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0669 | critic_loss=1.5951 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.7976 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.0108 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4685 | ema=0.7281 | best_ema=0.7281 | no_improve=0
   🔬 Alpha Diversity: mean=2.63 | std=1.92 | range=[1.25, 10.19] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.37 | AMZN=4.72 | CAT=3.52  BOT: BRK-B=1.61 | NEE=1.58 | KO=1.49
   🧬 FiLM: seq(dg=0.0002, db=0.0001, sat=0.0%) | latent(dg=0.0011, db=0.0006, sat=0.0%) | asset(dg=0.0004, db=0.0003, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=1 (12.5%), low_vol=6 (75.0%), medium_vol=1 (12.5%)
[CYCLE] Update 5/348 | Step 5,040/500,000 | Episode 0 | Time: 709.8s
   📊 Metrics: Return=+101.87% | Sharpe=1.685 | DD=13.80% | Turnover=24.34%
   🎚️ Intra-Step TAPE: potential=0.7551 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0736 | critic_loss=1.6531 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.8265 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0279
   🧠 Objective Experts: aux_loss=-0.0001 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6852 | ema=0.8238 | best_ema=0.8238 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p753_actor.weights.h5 (Sharpe=1.753, MDD=13.80%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00005_shp0p719_actor.weights.h5 (Sharpe=0.719, MDD=14.32%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp1p513_actor.weights.h5 (Sharpe=1.513, MDD=13.55%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp0p797_actor.weights.h5 (Sharpe=0.797, MDD=12.63%)
[CYCLE] Update 6/348 | Step 6,048/500,000 | Episode 8 | Time: 842.4s
   📊 Metrics: Return=+46.25% | Sharpe=0.797 | DD=12.63% | Turnover=24.73%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0230 | critic_loss=1.2653 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6327 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.0461 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7967 | ema=0.8211 | best_ema=0.8211 | no_improve=0
   🔬 Alpha Diversity: mean=2.60 | std=2.10 | range=[1.25, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.88 | AMZN=4.83 | MSFT=3.22  BOT: NEE=1.54 | BRK-B=1.51 | KO=1.45
   🧬 FiLM: seq(dg=0.0002, db=0.0001, sat=0.0%) | latent(dg=0.0017, db=0.0010, sat=0.0%) | asset(dg=0.0005, db=0.0004, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.500) | TAPE=0.4349
[CYCLE] Update 7/348 | Step 7,056/500,000 | Episode 8 | Time: 980.3s
   📊 Metrics: Return=+35.74% | Sharpe=4.190 | DD=3.31% | Turnover=24.33%
   🎚️ Intra-Step TAPE: potential=0.7474 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0525 | critic_loss=1.7832 | mean_adv=-0.0013
   🧮 Loss Detail: critic_scaled=0.8916 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.0187 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=4.1902 | ema=1.1580 | best_ema=1.1580 | no_improve=0
[CYCLE] Update 8/348 | Step 8,064/500,000 | Episode 8 | Time: 1118.3s
   📊 Metrics: Return=+12.30% | Sharpe=0.603 | DD=24.37% | Turnover=24.87%
   🎚️ Intra-Step TAPE: potential=0.2209 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0328 | critic_loss=1.3234 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6617 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0281
   🧠 Objective Experts: aux_loss=-0.0329 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6029 | ema=1.1025 | best_ema=1.1025 | no_improve=0
   🔬 Alpha Diversity: mean=2.61 | std=2.10 | range=[1.25, 10.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.38 | AMZN=2.92 | CAT=2.64  BOT: KO=1.57 | BRK-B=1.57 | GLD=1.55
   🧬 FiLM: seq(dg=0.0003, db=0.0002, sat=0.0%) | latent(dg=0.0023, db=0.0013, sat=0.0%) | asset(dg=0.0007, db=0.0005, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
[CYCLE] Update 9/348 | Step 9,072/500,000 | Episode 8 | Time: 1256.4s
   📊 Metrics: Return=+25.08% | Sharpe=0.674 | DD=26.31% | Turnover=24.34%
   🎚️ Intra-Step TAPE: potential=0.6079 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0343 | critic_loss=1.2220 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6110 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0283
   🧠 Objective Experts: aux_loss=-0.0349 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6424 | ema=1.0565 | best_ema=1.0565 | no_improve=0
[CYCLE] Update 10/348 | Step 10,080/500,000 | Episode 8 | Time: 1394.5s
   📊 Metrics: Return=+26.40% | Sharpe=0.571 | DD=26.31% | Turnover=24.89%
   🎚️ Intra-Step TAPE: potential=0.5786 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0828 | critic_loss=0.6795 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3398 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=0.0198 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5396 | ema=1.0048 | best_ema=1.0048 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.35 | range=[1.25, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.18 | CAT=1.88 | AMZN=1.87  BOT: KO=1.60 | XOM=1.59 | GLD=1.57
   🧬 FiLM: seq(dg=0.0003, db=0.0002, sat=0.0%) | latent(dg=0.0029, db=0.0016, sat=0.0%) | asset(dg=0.0008, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=4 (25.0%), low_vol=9 (56.2%), medium_vol=3 (18.8%)
[CYCLE] Update 11/348 | Step 11,088/500,000 | Episode 8 | Time: 1532.8s
   📊 Metrics: Return=+26.85% | Sharpe=0.493 | DD=26.31% | Turnover=25.08%
   🎚️ Intra-Step TAPE: potential=0.7268 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0721 | critic_loss=0.9740 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4870 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=0.0101 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4617 | ema=0.9505 | best_ema=0.9505 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p280_actor.weights.h5 (Sharpe=1.280, MDD=16.69%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p320_actor.weights.h5 (Sharpe=1.320, MDD=14.98%)
[CYCLE] Update 12/348 | Step 12,096/500,000 | Episode 16 | Time: 1664.3s
   📊 Metrics: Return=+54.67% | Sharpe=0.603 | DD=21.59% | Turnover=24.95%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0591 | critic_loss=0.8746 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4373 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=0.0011 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6032 | ema=0.9158 | best_ema=0.9158 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.33 | range=[1.25, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.66 | JPM=2.06 | CAT=1.98  BOT: XOM=1.72 | MSFT=1.57 | BRK-B=1.57
   🧬 FiLM: seq(dg=0.0003, db=0.0002, sat=0.0%) | latent(dg=0.0032, db=0.0018, sat=0.0%) | asset(dg=0.0009, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=11 (45.8%), medium_vol=6 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.119) | TAPE=0.3410
[CYCLE] Update 13/348 | Step 13,104/500,000 | Episode 16 | Time: 1801.7s
   📊 Metrics: Return=-6.18% | Sharpe=-0.500 | DD=17.55% | Turnover=26.32%
   🎚️ Intra-Step TAPE: potential=0.2398 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0462 | critic_loss=0.8078 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4039 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0283
   🧠 Objective Experts: aux_loss=-0.0185 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5005 | ema=0.7741 | best_ema=0.7741 | no_improve=0
[CYCLE] Update 14/348 | Step 14,112/500,000 | Episode 16 | Time: 1940.2s
   📊 Metrics: Return=-1.49% | Sharpe=-0.041 | DD=17.55% | Turnover=25.47%
   🎚️ Intra-Step TAPE: potential=0.3170 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0780 | critic_loss=0.9728 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4864 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0287
   🧠 Objective Experts: aux_loss=0.0130 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0406 | ema=0.6927 | best_ema=0.6927 | no_improve=0
   🔬 Alpha Diversity: mean=2.64 | std=1.76 | range=[1.24, 9.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.21 | NEE=3.09 | JPM=3.02  BOT: CAT=2.26 | XOM=2.22 | BRK-B=2.16
   🧬 FiLM: seq(dg=0.0004, db=0.0002, sat=0.0%) | latent(dg=0.0034, db=0.0019, sat=0.0%) | asset(dg=0.0010, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=11 (45.8%), medium_vol=6 (25.0%)
[CYCLE] Update 15/348 | Step 15,120/500,000 | Episode 16 | Time: 2077.9s
   📊 Metrics: Return=+0.50% | Sharpe=0.019 | DD=17.55% | Turnover=25.94%
   🎚️ Intra-Step TAPE: potential=0.7255 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0610 | critic_loss=0.5849 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2924 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   🧠 Objective Experts: aux_loss=-0.0003 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0188 | ema=0.6253 | best_ema=0.6253 | no_improve=0
[CYCLE] Update 16/348 | Step 16,128/500,000 | Episode 16 | Time: 2216.1s
   📊 Metrics: Return=+0.08% | Sharpe=-0.015 | DD=17.55% | Turnover=25.45%
   🎚️ Intra-Step TAPE: potential=0.2377 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0477 | critic_loss=0.6537 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3268 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0288
   🧠 Objective Experts: aux_loss=-0.0102 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0149 | ema=0.5613 | best_ema=0.5613 | no_improve=0
   🔬 Alpha Diversity: mean=2.65 | std=1.50 | range=[1.24, 8.83] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=4.36 | NEE=4.18 | GLD=3.36  BOT: CAT=1.85 | AMZN=1.77 | NVDA=1.70
   🧬 FiLM: seq(dg=0.0004, db=0.0003, sat=0.0%) | latent(dg=0.0038, db=0.0021, sat=0.0%) | asset(dg=0.0012, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=7 (29.2%), low_vol=11 (45.8%), medium_vol=6 (25.0%)
[CYCLE] Update 17/348 | Step 17,136/500,000 | Episode 16 | Time: 2353.9s
   📊 Metrics: Return=+4.65% | Sharpe=0.075 | DD=17.55% | Turnover=25.29%
   🎚️ Intra-Step TAPE: potential=0.2925 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0264 | critic_loss=0.5661 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2830 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0288
   🧠 Objective Experts: aux_loss=-0.0314 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0754 | ema=0.5127 | best_ema=0.5127 | no_improve=0
[CYCLE] Update 18/348 | Step 18,144/500,000 | Episode 24 | Time: 2484.3s
   📊 Metrics: Return=+16.26% | Sharpe=0.266 | DD=19.73% | Turnover=25.48%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0247 | critic_loss=0.6351 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3176 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   🧠 Objective Experts: aux_loss=-0.0310 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2664 | ema=0.4880 | best_ema=0.4880 | no_improve=0
   🔬 Alpha Diversity: mean=2.65 | std=1.42 | range=[1.24, 7.49] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=4.29 | NEE=4.08 | XOM=3.52  BOT: JPM=1.76 | AMZN=1.51 | NVDA=1.40
   🧬 FiLM: seq(dg=0.0005, db=0.0003, sat=0.0%) | latent(dg=0.0045, db=0.0026, sat=0.0%) | asset(dg=0.0013, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=12 (37.5%), medium_vol=10 (31.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.004) | TAPE=0.2604
[CYCLE] Update 19/348 | Step 19,152/500,000 | Episode 24 | Time: 2622.2s
   📊 Metrics: Return=+39.42% | Sharpe=1.754 | DD=20.25% | Turnover=24.43%
   🎚️ Intra-Step TAPE: potential=0.7249 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0949 | critic_loss=1.6914 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8457 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0289
   🧠 Objective Experts: aux_loss=0.0394 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7538 | ema=0.6146 | best_ema=0.6146 | no_improve=0
[CYCLE] Update 20/348 | Step 20,160/500,000 | Episode 24 | Time: 2760.1s
   📊 Metrics: Return=+64.94% | Sharpe=1.714 | DD=20.25% | Turnover=24.98%
   🎚️ Intra-Step TAPE: potential=0.5648 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0423 | critic_loss=0.4674 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2337 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0291
   🧠 Objective Experts: aux_loss=-0.0122 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7140 | ema=0.7246 | best_ema=0.7246 | no_improve=0
   🔬 Alpha Diversity: mean=2.67 | std=1.47 | range=[1.24, 7.80] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.29 | KO=3.63 | XOM=3.31  BOT: NVDA=1.91 | CAT=1.89 | AMZN=1.69
   🧬 FiLM: seq(dg=0.0005, db=0.0003, sat=0.0%) | latent(dg=0.0055, db=0.0031, sat=0.0%) | asset(dg=0.0015, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=12 (37.5%), medium_vol=10 (31.2%)
[CYCLE] Update 21/348 | Step 21,168/500,000 | Episode 24 | Time: 2897.8s
   📊 Metrics: Return=+49.32% | Sharpe=1.031 | DD=20.25% | Turnover=25.44%
   🎚️ Intra-Step TAPE: potential=0.2388 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0551 | critic_loss=0.7597 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3799 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   🧠 Objective Experts: aux_loss=-0.0034 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0313 | ema=0.7552 | best_ema=0.7552 | no_improve=0
[CYCLE] Update 22/348 | Step 22,176/500,000 | Episode 24 | Time: 3035.4s
   📊 Metrics: Return=+81.01% | Sharpe=1.233 | DD=20.25% | Turnover=25.04%
   🎚️ Intra-Step TAPE: potential=0.7509 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0438 | critic_loss=0.3716 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1858 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   🧠 Objective Experts: aux_loss=-0.0126 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2335 | ema=0.8031 | best_ema=0.8031 | no_improve=0
   🔬 Alpha Diversity: mean=2.64 | std=1.54 | range=[1.24, 9.21] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=3.16 | KO=3.04 | GLD=3.02  BOT: AMZN=2.25 | CAT=2.11 | NVDA=2.05
   🧬 FiLM: seq(dg=0.0005, db=0.0003, sat=0.0%) | latent(dg=0.0057, db=0.0032, sat=0.0%) | asset(dg=0.0013, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (31.2%), low_vol=12 (37.5%), medium_vol=10 (31.2%)
[CYCLE] Update 23/348 | Step 23,184/500,000 | Episode 24 | Time: 3173.1s
   📊 Metrics: Return=+81.87% | Sharpe=1.070 | DD=20.25% | Turnover=25.46%
   🎚️ Intra-Step TAPE: potential=0.2303 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0431 | critic_loss=0.4143 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2072 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0294
   🧠 Objective Experts: aux_loss=-0.0093 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0695 | ema=0.8297 | best_ema=0.8297 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp0p871_actor.weights.h5 (Sharpe=0.871, MDD=20.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00028_shp1p068_actor.weights.h5 (Sharpe=1.068, MDD=8.55%)
[CYCLE] Update 24/348 | Step 24,192/500,000 | Episode 32 | Time: 3304.4s
   📊 Metrics: Return=+22.90% | Sharpe=0.490 | DD=11.63% | Turnover=26.32%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0438 | critic_loss=0.5456 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2728 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   🧠 Objective Experts: aux_loss=-0.0087 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4898 | ema=0.7957 | best_ema=0.7957 | no_improve=0
   🔬 Alpha Diversity: mean=2.66 | std=1.51 | range=[1.24, 8.80] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.54 | KO=4.25 | GLD=4.17  BOT: JPM=1.78 | CAT=1.72 | NVDA=1.30
   🧬 FiLM: seq(dg=0.0005, db=0.0003, sat=0.0%) | latent(dg=0.0052, db=0.0029, sat=0.0%) | asset(dg=0.0016, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=11 (27.5%), low_vol=14 (35.0%), medium_vol=15 (37.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3102
[CYCLE] Update 25/348 | Step 25,200/500,000 | Episode 32 | Time: 3442.0s
   📊 Metrics: Return=+9.76% | Sharpe=3.005 | DD=1.66% | Turnover=25.37%
   🎚️ Intra-Step TAPE: potential=0.7541 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0091 | critic_loss=0.5136 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2568 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0296
   🧠 Objective Experts: aux_loss=-0.0429 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.0046 | ema=1.0166 | best_ema=1.0166 | no_improve=0
[CYCLE] Update 26/348 | Step 26,208/500,000 | Episode 32 | Time: 3579.7s
   📊 Metrics: Return=+17.71% | Sharpe=2.507 | DD=2.45% | Turnover=25.93%
   🎚️ Intra-Step TAPE: potential=0.6980 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0374 | critic_loss=0.3891 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1945 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0293
   🧠 Objective Experts: aux_loss=-0.0181 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.5072 | ema=1.1657 | best_ema=1.1657 | no_improve=0
   🔬 Alpha Diversity: mean=2.67 | std=1.39 | range=[1.24, 7.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.59 | KO=4.34 | XOM=3.37  BOT: AMZN=1.84 | CAT=1.57 | NVDA=1.29
   🧬 FiLM: seq(dg=0.0004, db=0.0003, sat=0.0%) | latent(dg=0.0056, db=0.0032, sat=0.0%) | asset(dg=0.0017, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=11 (27.5%), low_vol=14 (35.0%), medium_vol=15 (37.5%)
[CYCLE] Update 27/348 | Step 27,216/500,000 | Episode 32 | Time: 3717.3s
   📊 Metrics: Return=+23.31% | Sharpe=1.462 | DD=8.48% | Turnover=26.00%
   🎚️ Intra-Step TAPE: potential=0.2807 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0141 | critic_loss=0.3973 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1986 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   🧠 Objective Experts: aux_loss=-0.0371 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4616 | ema=1.1952 | best_ema=1.1952 | no_improve=0
[CYCLE] Update 28/348 | Step 28,224/500,000 | Episode 32 | Time: 3855.1s
   📊 Metrics: Return=+17.27% | Sharpe=0.678 | DD=9.89% | Turnover=25.80%
   🎚️ Intra-Step TAPE: potential=0.2400 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0247 | critic_loss=0.3986 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1993 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0293
   🧠 Objective Experts: aux_loss=-0.0222 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6782 | ema=1.1435 | best_ema=1.1435 | no_improve=0
   🔬 Alpha Diversity: mean=2.65 | std=1.35 | range=[1.24, 7.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.29 | KO=4.23 | GLD=3.32  BOT: CAT=1.99 | NVDA=1.54 | AMZN=1.51
   🧬 FiLM: seq(dg=0.0005, db=0.0003, sat=0.0%) | latent(dg=0.0059, db=0.0034, sat=0.0%) | asset(dg=0.0017, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=11 (27.5%), low_vol=14 (35.0%), medium_vol=15 (37.5%)
[CYCLE] Update 29/348 | Step 29,232/500,000 | Episode 32 | Time: 3993.0s
   📊 Metrics: Return=+21.29% | Sharpe=0.600 | DD=17.05% | Turnover=25.50%
   🎚️ Intra-Step TAPE: potential=0.2975 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0351 | critic_loss=0.4507 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2253 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0295
   🧠 Objective Experts: aux_loss=-0.0147 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6000 | ema=1.0892 | best_ema=1.0892 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00038_shp0p748_actor.weights.h5 (Sharpe=0.748, MDD=11.62%)
[CYCLE] Update 30/348 | Step 30,240/500,000 | Episode 40 | Time: 4123.6s
   📊 Metrics: Return=+12.69% | Sharpe=0.236 | DD=12.35% | Turnover=25.97%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0353 | critic_loss=0.7336 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3668 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0291
   🧠 Objective Experts: aux_loss=-0.0167 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2357 | ema=1.0038 | best_ema=1.0038 | no_improve=0
   🔬 Alpha Diversity: mean=2.64 | std=1.41 | range=[1.24, 8.36] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.16 | KO=3.76 | XOM=3.14  BOT: JPM=2.00 | CAT=1.89 | NVDA=1.73
   🧬 FiLM: seq(dg=0.0005, db=0.0003, sat=0.0%) | latent(dg=0.0063, db=0.0037, sat=0.0%) | asset(dg=0.0016, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=14 (29.2%), low_vol=15 (31.2%), medium_vol=19 (39.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2614
[CYCLE] Update 31/348 | Step 31,248/500,000 | Episode 40 | Time: 4261.0s
   📊 Metrics: Return=-0.13% | Sharpe=-0.022 | DD=13.08% | Turnover=25.07%
   🎚️ Intra-Step TAPE: potential=0.6818 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0248 | critic_loss=1.4062 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.7031 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0293
   🧠 Objective Experts: aux_loss=-0.0262 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0218 | ema=0.9013 | best_ema=0.9013 | no_improve=0
[CYCLE] Update 32/348 | Step 32,256/500,000 | Episode 40 | Time: 4398.7s
   📊 Metrics: Return=+14.05% | Sharpe=0.787 | DD=13.08% | Turnover=25.29%
   🎚️ Intra-Step TAPE: potential=0.3585 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0549 | critic_loss=0.5281 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2641 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   🧠 Objective Experts: aux_loss=0.0042 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7869 | ema=0.8898 | best_ema=0.8898 | no_improve=0
   🔬 Alpha Diversity: mean=2.65 | std=1.39 | range=[1.24, 7.15] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.60 | KO=4.36 | XOM=3.52  BOT: AMZN=1.92 | CAT=1.61 | NVDA=1.55
   🧬 FiLM: seq(dg=0.0005, db=0.0003, sat=0.0%) | latent(dg=0.0065, db=0.0039, sat=0.0%) | asset(dg=0.0018, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=14 (29.2%), low_vol=15 (31.2%), medium_vol=19 (39.6%)
[CYCLE] Update 33/348 | Step 33,264/500,000 | Episode 40 | Time: 4536.2s
   📊 Metrics: Return=+11.67% | Sharpe=0.382 | DD=13.52% | Turnover=25.87%
   🎚️ Intra-Step TAPE: potential=0.3580 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0152 | critic_loss=0.4594 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2297 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0291
   🧠 Objective Experts: aux_loss=-0.0374 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3825 | ema=0.8391 | best_ema=0.8391 | no_improve=0
[CYCLE] Update 34/348 | Step 34,272/500,000 | Episode 40 | Time: 4673.5s
   📊 Metrics: Return=+17.44% | Sharpe=0.432 | DD=13.52% | Turnover=25.63%
   🎚️ Intra-Step TAPE: potential=0.5977 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0144 | critic_loss=0.3652 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1826 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0291
   🧠 Objective Experts: aux_loss=-0.0317 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4321 | ema=0.7984 | best_ema=0.7984 | no_improve=0
   🔬 Alpha Diversity: mean=2.68 | std=1.45 | range=[1.24, 6.93] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.90 | KO=4.51 | MSFT=3.26  BOT: AMZN=1.60 | CAT=1.59 | NVDA=1.29
   🧬 FiLM: seq(dg=0.0004, db=0.0003, sat=0.0%) | latent(dg=0.0067, db=0.0040, sat=0.0%) | asset(dg=0.0019, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=14 (29.2%), low_vol=15 (31.2%), medium_vol=19 (39.6%)
[CYCLE] Update 35/348 | Step 35,280/500,000 | Episode 40 | Time: 4811.1s
   📊 Metrics: Return=+15.33% | Sharpe=0.308 | DD=13.52% | Turnover=25.68%
   🎚️ Intra-Step TAPE: potential=0.2669 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0012 | critic_loss=0.3783 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1891 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0292
   🧠 Objective Experts: aux_loss=-0.0478 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3078 | ema=0.7493 | best_ema=0.7493 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00042_shp0p969_actor.weights.h5 (Sharpe=0.969, MDD=9.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00043_shp0p818_actor.weights.h5 (Sharpe=0.818, MDD=7.14%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00046_shp0p834_actor.weights.h5 (Sharpe=0.834, MDD=9.96%)
[CYCLE] Update 36/348 | Step 36,288/500,000 | Episode 48 | Time: 4942.6s
   📊 Metrics: Return=+48.13% | Sharpe=0.623 | DD=19.12% | Turnover=25.34%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0142 | critic_loss=0.4981 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2491 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0293
   🧠 Objective Experts: aux_loss=-0.0337 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6226 | ema=0.7367 | best_ema=0.7367 | no_improve=0
   🔬 Alpha Diversity: mean=2.61 | std=1.33 | range=[1.24, 7.21] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.18 | KO=3.74 | XOM=3.13  BOT: JPM=2.03 | CAT=1.87 | NVDA=1.75
   🧬 FiLM: seq(dg=0.0006, db=0.0004, sat=0.0%) | latent(dg=0.0071, db=0.0041, sat=0.0%) | asset(dg=0.0018, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (28.6%), low_vol=19 (33.9%), medium_vol=21 (37.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.012) | TAPE=0.3481
[CYCLE] Update 37/348 | Step 37,296/500,000 | Episode 48 | Time: 5079.8s
   📊 Metrics: Return=+6.39% | Sharpe=0.983 | DD=5.69% | Turnover=26.88%
   🎚️ Intra-Step TAPE: potential=0.3202 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0080 | critic_loss=0.4519 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2260 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0298
   🧠 Objective Experts: aux_loss=-0.0420 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9834 | ema=0.7613 | best_ema=0.7613 | no_improve=0
[CYCLE] Update 38/348 | Step 38,304/500,000 | Episode 48 | Time: 5217.4s
   📊 Metrics: Return=-1.18% | Sharpe=-0.059 | DD=18.32% | Turnover=26.38%
   🎚️ Intra-Step TAPE: potential=0.4114 | delta_reward=-0.0020
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0192 | critic_loss=0.3323 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1662 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0288
   🧠 Objective Experts: aux_loss=-0.0627 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0595 | ema=0.6793 | best_ema=0.6793 | no_improve=0
   🔬 Alpha Diversity: mean=2.66 | std=1.45 | range=[1.24, 8.37] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.47 | KO=4.30 | XOM=3.58  BOT: JPM=2.12 | AMZN=1.91 | NVDA=1.41
   🧬 FiLM: seq(dg=0.0006, db=0.0004, sat=0.0%) | latent(dg=0.0074, db=0.0042, sat=0.0%) | asset(dg=0.0018, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (28.6%), low_vol=19 (33.9%), medium_vol=21 (37.5%)
[CYCLE] Update 39/348 | Step 39,312/500,000 | Episode 48 | Time: 5355.0s
   📊 Metrics: Return=+3.52% | Sharpe=0.107 | DD=18.32% | Turnover=26.16%
   🎚️ Intra-Step TAPE: potential=0.2858 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0093 | critic_loss=0.3292 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1646 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0290
   🧠 Objective Experts: aux_loss=-0.0581 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1074 | ema=0.6221 | best_ema=0.6221 | no_improve=0
[CYCLE] Update 40/348 | Step 40,320/500,000 | Episode 48 | Time: 5492.2s
   📊 Metrics: Return=+3.25% | Sharpe=0.059 | DD=18.32% | Turnover=26.28%
   🎚️ Intra-Step TAPE: potential=0.2401 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0275 | critic_loss=0.3352 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1676 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0288
   🧠 Objective Experts: aux_loss=-0.0717 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0595 | ema=0.5658 | best_ema=0.5658 | no_improve=0
   🔬 Alpha Diversity: mean=2.65 | std=1.57 | range=[1.23, 9.08] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=4.49 | NEE=4.03 | BRK-B=3.55  BOT: JPM=1.89 | AMZN=1.41 | NVDA=1.33
   🧬 FiLM: seq(dg=0.0008, db=0.0006, sat=0.0%) | latent(dg=0.0076, db=0.0043, sat=0.0%) | asset(dg=0.0019, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=16 (28.6%), low_vol=19 (33.9%), medium_vol=21 (37.5%)
[CYCLE] Update 41/348 | Step 41,328/500,000 | Episode 48 | Time: 5629.7s
   📊 Metrics: Return=+11.66% | Sharpe=0.234 | DD=18.32% | Turnover=25.72%
   🎚️ Intra-Step TAPE: potential=0.5490 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0008 | critic_loss=0.3214 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1607 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0287
   🧠 Objective Experts: aux_loss=-0.0476 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2345 | ema=0.5327 | best_ema=0.5327 | no_improve=0
[CYCLE] Update 42/348 | Step 42,336/500,000 | Episode 56 | Time: 5759.7s
   📊 Metrics: Return=+17.38% | Sharpe=0.304 | DD=16.74% | Turnover=25.62%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0115 | critic_loss=0.6779 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3389 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0286
   🧠 Objective Experts: aux_loss=-0.0587 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3037 | ema=0.5098 | best_ema=0.5098 | no_improve=0
   🔬 Alpha Diversity: mean=2.65 | std=1.60 | range=[1.23, 9.10] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=5.19 | NEE=4.60 | BRK-B=2.94  BOT: JPM=2.15 | NVDA=1.57 | AMZN=1.55
   🧬 FiLM: seq(dg=0.0009, db=0.0006, sat=0.0%) | latent(dg=0.0077, db=0.0044, sat=0.0%) | asset(dg=0.0020, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=23 (35.9%), medium_vol=23 (35.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2632
[CYCLE] Update 43/348 | Step 43,344/500,000 | Episode 56 | Time: 5896.8s
   📊 Metrics: Return=+5.70% | Sharpe=0.994 | DD=6.98% | Turnover=26.33%
   🎚️ Intra-Step TAPE: potential=0.2700 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0237 | critic_loss=0.9709 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4854 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0287
   🧠 Objective Experts: aux_loss=-0.0269 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9943 | ema=0.5582 | best_ema=0.5582 | no_improve=0
[CYCLE] Update 44/348 | Step 44,352/500,000 | Episode 56 | Time: 6034.1s
   📊 Metrics: Return=+9.76% | Sharpe=0.684 | DD=6.98% | Turnover=25.97%
   🎚️ Intra-Step TAPE: potential=0.4831 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0230 | critic_loss=0.4476 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2238 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0291
   🧠 Objective Experts: aux_loss=-0.0259 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6842 | ema=0.5708 | best_ema=0.5708 | no_improve=0
   🔬 Alpha Diversity: mean=2.63 | std=1.40 | range=[1.23, 7.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.38 | KO=4.16 | XOM=3.14  BOT: CAT=2.00 | JPM=1.98 | NVDA=1.86
   🧬 FiLM: seq(dg=0.0010, db=0.0007, sat=0.0%) | latent(dg=0.0077, db=0.0045, sat=0.0%) | asset(dg=0.0021, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=23 (35.9%), medium_vol=23 (35.9%)
[CYCLE] Update 45/348 | Step 45,360/500,000 | Episode 56 | Time: 6171.5s
   📊 Metrics: Return=+8.87% | Sharpe=0.346 | DD=11.22% | Turnover=25.51%
   🎚️ Intra-Step TAPE: potential=0.5873 | delta_reward=+0.0029
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0064 | critic_loss=0.4384 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2192 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0292
   🧠 Objective Experts: aux_loss=-0.0395 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3458 | ema=0.5483 | best_ema=0.5483 | no_improve=0
[CYCLE] Update 46/348 | Step 46,368/500,000 | Episode 56 | Time: 6308.8s
   📊 Metrics: Return=+18.96% | Sharpe=0.578 | DD=11.22% | Turnover=25.11%
   🎚️ Intra-Step TAPE: potential=0.7449 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0126 | critic_loss=0.4883 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2441 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   🧠 Objective Experts: aux_loss=-0.0323 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5779 | ema=0.5513 | best_ema=0.5513 | no_improve=0
   🔬 Alpha Diversity: mean=2.63 | std=1.84 | range=[1.23, 9.84] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=3.91 | KO=3.81 | BRK-B=2.65  BOT: JPM=1.81 | GLD=1.71 | NVDA=1.49
   🧬 FiLM: seq(dg=0.0012, db=0.0007, sat=0.0%) | latent(dg=0.0088, db=0.0049, sat=0.0%) | asset(dg=0.0020, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=18 (28.1%), low_vol=23 (35.9%), medium_vol=23 (35.9%)
[CYCLE] Update 47/348 | Step 47,376/500,000 | Episode 56 | Time: 6446.4s
   📊 Metrics: Return=+25.70% | Sharpe=0.650 | DD=11.22% | Turnover=25.17%
   🎚️ Intra-Step TAPE: potential=0.2420 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0181 | critic_loss=0.4194 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2097 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0267
   🧠 Objective Experts: aux_loss=-0.0302 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6500 | ema=0.5612 | best_ema=0.5612 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00057_shp0p742_actor.weights.h5 (Sharpe=0.742, MDD=11.22%)
[CYCLE] Update 48/348 | Step 48,384/500,000 | Episode 64 | Time: 6577.1s
   📊 Metrics: Return=+29.92% | Sharpe=0.691 | DD=6.59% | Turnover=25.97%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0507 | critic_loss=0.3805 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1903 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.0961 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6914 | ema=0.5742 | best_ema=0.5742 | no_improve=0
   🔬 Alpha Diversity: mean=2.65 | std=1.85 | range=[1.23, 9.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=4.27 | NEE=4.07 | GLD=2.57  BOT: AMZN=1.70 | JPM=1.62 | NVDA=1.38
   🧬 FiLM: seq(dg=0.0015, db=0.0008, sat=0.0%) | latent(dg=0.0095, db=0.0051, sat=0.0%) | asset(dg=0.0022, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=20 (27.8%), low_vol=29 (40.3%), medium_vol=23 (31.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3848
[CYCLE] Update 49/348 | Step 49,392/500,000 | Episode 64 | Time: 6714.7s
   📊 Metrics: Return=-2.38% | Sharpe=-0.546 | DD=6.18% | Turnover=25.85%
   🎚️ Intra-Step TAPE: potential=0.2682 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0110 | critic_loss=1.0009 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5004 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0292
   🧠 Objective Experts: aux_loss=-0.0364 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5459 | ema=0.4622 | best_ema=0.4622 | no_improve=0
[CYCLE] Update 50/348 | Step 50,400/500,000 | Episode 64 | Time: 6852.5s
   📊 Metrics: Return=+2.94% | Sharpe=0.136 | DD=6.19% | Turnover=26.03%
   🎚️ Intra-Step TAPE: potential=0.3150 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0024 | critic_loss=0.7221 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3610 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0294
   🧠 Objective Experts: aux_loss=-0.0415 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1361 | ema=0.4296 | best_ema=0.4296 | no_improve=0
   🔬 Alpha Diversity: mean=2.62 | std=1.51 | range=[1.23, 7.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=4.79 | NEE=4.39 | GLD=3.12  BOT: CAT=2.03 | JPM=1.92 | NVDA=1.89
   🧬 FiLM: seq(dg=0.0015, db=0.0008, sat=0.0%) | latent(dg=0.0097, db=0.0051, sat=0.0%) | asset(dg=0.0023, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=20 (27.8%), low_vol=29 (40.3%), medium_vol=23 (31.9%)
[CYCLE] Update 51/348 | Step 51,408/500,000 | Episode 64 | Time: 6989.8s
   📊 Metrics: Return=+1.42% | Sharpe=-0.012 | DD=8.35% | Turnover=25.83%
   🎚️ Intra-Step TAPE: potential=0.2490 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0523 | critic_loss=0.3131 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1566 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   🧠 Objective Experts: aux_loss=0.0018 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0118 | ema=0.3854 | best_ema=0.3854 | no_improve=0
[CYCLE] Update 52/348 | Step 52,416/500,000 | Episode 64 | Time: 7127.5s
   📊 Metrics: Return=+18.49% | Sharpe=0.573 | DD=8.35% | Turnover=25.55%
   🎚️ Intra-Step TAPE: potential=0.7038 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0041 | critic_loss=0.5102 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2551 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0286
   🧠 Objective Experts: aux_loss=-0.0489 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5733 | ema=0.4042 | best_ema=0.4042 | no_improve=0
   🔬 Alpha Diversity: mean=2.66 | std=1.73 | range=[1.23, 9.46] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=5.07 | NEE=4.90 | GLD=4.12  BOT: AMZN=1.60 | CAT=1.57 | NVDA=1.56
   🧬 FiLM: seq(dg=0.0018, db=0.0009, sat=0.0%) | latent(dg=0.0098, db=0.0051, sat=0.0%) | asset(dg=0.0026, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=20 (27.8%), low_vol=29 (40.3%), medium_vol=23 (31.9%)
[CYCLE] Update 53/348 | Step 53,424/500,000 | Episode 64 | Time: 7265.1s
   📊 Metrics: Return=+23.48% | Sharpe=0.586 | DD=8.35% | Turnover=25.48%
   🎚️ Intra-Step TAPE: potential=0.6403 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0123 | critic_loss=0.6380 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3190 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.0556 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5863 | ema=0.4224 | best_ema=0.4224 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00065_shp0p777_actor.weights.h5 (Sharpe=0.777, MDD=8.35%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00071_shp0p962_actor.weights.h5 (Sharpe=0.962, MDD=9.73%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00072_shp1p067_actor.weights.h5 (Sharpe=1.067, MDD=9.81%)
[CYCLE] Update 54/348 | Step 54,432/500,000 | Episode 72 | Time: 7396.6s
   📊 Metrics: Return=+49.40% | Sharpe=1.067 | DD=9.81% | Turnover=24.54%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0166 | critic_loss=0.9411 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4705 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0283
   🧠 Objective Experts: aux_loss=-0.0586 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0669 | ema=0.4869 | best_ema=0.4869 | no_improve=0
   🔬 Alpha Diversity: mean=2.63 | std=1.89 | range=[1.23, 9.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.33 | GLD=4.03 | NVDA=3.38  BOT: CAT=1.68 | JPM=1.67 | BRK-B=1.65
   🧬 FiLM: seq(dg=0.0016, db=0.0009, sat=0.0%) | latent(dg=0.0087, db=0.0046, sat=0.0%) | asset(dg=0.0022, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=32 (40.0%), medium_vol=24 (30.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5250
[CYCLE] Update 55/348 | Step 55,440/500,000 | Episode 72 | Time: 7533.6s
   📊 Metrics: Return=+24.86% | Sharpe=4.099 | DD=2.48% | Turnover=26.10%
   🎚️ Intra-Step TAPE: potential=0.7278 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0042 | critic_loss=0.4159 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2080 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0286
   🧠 Objective Experts: aux_loss=-0.0383 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=4.0986 | ema=0.8480 | best_ema=0.8480 | no_improve=0
[CYCLE] Update 56/348 | Step 56,448/500,000 | Episode 72 | Time: 7671.0s
   📊 Metrics: Return=+33.51% | Sharpe=2.748 | DD=3.24% | Turnover=25.69%
   🎚️ Intra-Step TAPE: potential=0.7404 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0400 | critic_loss=0.2517 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1259 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0285
   🧠 Objective Experts: aux_loss=-0.0891 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.7477 | ema=1.0380 | best_ema=1.0380 | no_improve=0
   🔬 Alpha Diversity: mean=2.64 | std=1.83 | range=[1.23, 8.88] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=4.78 | NEE=4.45 | BRK-B=2.32  BOT: NVDA=1.62 | JPM=1.53 | CAT=1.50
   🧬 FiLM: seq(dg=0.0017, db=0.0010, sat=0.0%) | latent(dg=0.0076, db=0.0043, sat=0.0%) | asset(dg=0.0023, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=32 (40.0%), medium_vol=24 (30.0%)
[CYCLE] Update 57/348 | Step 57,456/500,000 | Episode 72 | Time: 7808.8s
   📊 Metrics: Return=+43.70% | Sharpe=2.617 | DD=3.24% | Turnover=25.84%
   🎚️ Intra-Step TAPE: potential=0.7274 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0301 | critic_loss=0.2981 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1491 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   🧠 Objective Experts: aux_loss=-0.0750 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.6174 | ema=1.1959 | best_ema=1.1959 | no_improve=0
[CYCLE] Update 58/348 | Step 58,464/500,000 | Episode 72 | Time: 7946.4s
   📊 Metrics: Return=+48.75% | Sharpe=2.056 | DD=9.71% | Turnover=25.50%
   🎚️ Intra-Step TAPE: potential=0.2232 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0203 | critic_loss=0.6954 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3477 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.0253 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.0555 | ema=1.2819 | best_ema=1.2819 | no_improve=0
   🔬 Alpha Diversity: mean=2.64 | std=1.82 | range=[1.23, 9.69] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=4.86 | NEE=4.47 | KO=4.29  BOT: JPM=1.86 | AMZN=1.80 | NVDA=1.71
   🧬 FiLM: seq(dg=0.0026, db=0.0016, sat=0.0%) | latent(dg=0.0083, db=0.0042, sat=0.0%) | asset(dg=0.0024, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=24 (30.0%), low_vol=32 (40.0%), medium_vol=24 (30.0%)
[CYCLE] Update 59/348 | Step 59,472/500,000 | Episode 72 | Time: 8084.1s
   📊 Metrics: Return=+56.03% | Sharpe=1.755 | DD=9.71% | Turnover=25.59%
   🎚️ Intra-Step TAPE: potential=0.2826 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1031 | critic_loss=0.4347 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2173 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0286
   🧠 Objective Experts: aux_loss=-0.1460 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7553 | ema=1.3292 | best_ema=1.3292 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp1p064_actor.weights.h5 (Sharpe=1.064, MDD=16.80%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00075_shp1p073_actor.weights.h5 (Sharpe=1.073, MDD=7.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00079_shp0p835_actor.weights.h5 (Sharpe=0.835, MDD=8.84%)
[CYCLE] Update 60/348 | Step 60,480/500,000 | Episode 80 | Time: 8215.6s
   📊 Metrics: Return=+29.67% | Sharpe=0.617 | DD=22.17% | Turnover=25.31%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0627 | critic_loss=0.9849 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4924 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.1062 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6171 | ema=1.2580 | best_ema=1.2580 | no_improve=0
   🔬 Alpha Diversity: mean=2.61 | std=1.77 | range=[1.23, 8.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=5.23 | KO=4.62 | GLD=4.51  BOT: NVDA=1.69 | JPM=1.66 | CAT=1.55
   🧬 FiLM: seq(dg=0.0028, db=0.0016, sat=0.0%) | latent(dg=0.0079, db=0.0041, sat=0.0%) | asset(dg=0.0024, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=36 (40.9%), medium_vol=26 (29.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.013 (peak 0.023) | TAPE=0.3238
[CYCLE] Update 61/348 | Step 61,488/500,000 | Episode 80 | Time: 8352.9s
   📊 Metrics: Return=+0.31% | Sharpe=0.005 | DD=11.57% | Turnover=23.45%
   🎚️ Intra-Step TAPE: potential=0.6173 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0668 | critic_loss=0.3342 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1671 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0288
   🧠 Objective Experts: aux_loss=-0.1136 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0049 | ema=1.1327 | best_ema=1.1327 | no_improve=0
[CYCLE] Update 62/348 | Step 62,496/500,000 | Episode 80 | Time: 8490.7s
   📊 Metrics: Return=+15.46% | Sharpe=0.958 | DD=11.57% | Turnover=24.16%
   🎚️ Intra-Step TAPE: potential=0.6816 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0173 | critic_loss=0.2158 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1079 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   🧠 Objective Experts: aux_loss=-0.0272 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9579 | ema=1.1152 | best_ema=1.1152 | no_improve=0
   🔬 Alpha Diversity: mean=2.64 | std=1.83 | range=[1.23, 9.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.39 | KO=4.17 | GLD=2.82  BOT: JPM=1.63 | NVDA=1.45 | CAT=1.44
   🧬 FiLM: seq(dg=0.0024, db=0.0015, sat=0.0%) | latent(dg=0.0064, db=0.0036, sat=0.0%) | asset(dg=0.0025, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=36 (40.9%), medium_vol=26 (29.5%)
[CYCLE] Update 63/348 | Step 63,504/500,000 | Episode 80 | Time: 8628.1s
   📊 Metrics: Return=+5.76% | Sharpe=0.189 | DD=15.29% | Turnover=24.43%
   🎚️ Intra-Step TAPE: potential=0.2317 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0061 | critic_loss=0.3656 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1828 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   🧠 Objective Experts: aux_loss=-0.0469 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1889 | ema=1.0226 | best_ema=1.0226 | no_improve=0
[CYCLE] Update 64/348 | Step 64,512/500,000 | Episode 80 | Time: 8765.7s
   📊 Metrics: Return=+11.16% | Sharpe=0.283 | DD=15.85% | Turnover=24.40%
   🎚️ Intra-Step TAPE: potential=0.6682 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0589 | critic_loss=0.3976 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1988 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0283
   🧠 Objective Experts: aux_loss=-0.1012 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2831 | ema=0.9487 | best_ema=0.9487 | no_improve=0
   🔬 Alpha Diversity: mean=2.66 | std=1.73 | range=[1.22, 8.33] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=5.77 | NEE=4.90 | GLD=3.20  BOT: CAT=1.53 | AMZN=1.43 | NVDA=1.40
   🧬 FiLM: seq(dg=0.0037, db=0.0023, sat=0.0%) | latent(dg=0.0069, db=0.0036, sat=0.0%) | asset(dg=0.0027, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=26 (29.5%), low_vol=36 (40.9%), medium_vol=26 (29.5%)
[CYCLE] Update 65/348 | Step 65,520/500,000 | Episode 80 | Time: 8903.6s
   📊 Metrics: Return=+14.77% | Sharpe=0.304 | DD=15.85% | Turnover=24.44%
   🎚️ Intra-Step TAPE: potential=0.5670 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0769 | critic_loss=0.4592 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2296 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0281
   🧠 Objective Experts: aux_loss=-0.1215 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3040 | ema=0.8842 | best_ema=0.8842 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00082_shp0p788_actor.weights.h5 (Sharpe=0.788, MDD=8.61%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00083_shp0p841_actor.weights.h5 (Sharpe=0.841, MDD=7.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00085_shp0p811_actor.weights.h5 (Sharpe=0.811, MDD=7.01%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp0p733_actor.weights.h5 (Sharpe=0.733, MDD=8.68%)
[CYCLE] Update 66/348 | Step 66,528/500,000 | Episode 88 | Time: 9035.5s
   📊 Metrics: Return=+29.94% | Sharpe=0.733 | DD=8.68% | Turnover=25.23%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0497 | critic_loss=0.4479 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2239 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0266
   🧠 Objective Experts: aux_loss=0.0028 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7330 | ema=0.8691 | best_ema=0.8691 | no_improve=0
   🔬 Alpha Diversity: mean=2.57 | std=2.17 | range=[1.24, 10.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=3.73 | NEE=2.96 | GLD=2.43  BOT: MSFT=1.47 | JPM=1.42 | AMZN=1.36
   🧬 FiLM: seq(dg=0.0044, db=0.0031, sat=0.0%) | latent(dg=0.0069, db=0.0034, sat=0.0%) | asset(dg=0.0027, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (31.2%), low_vol=40 (41.7%), medium_vol=26 (27.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.010) | TAPE=0.4077
[CYCLE] Update 67/348 | Step 67,536/500,000 | Episode 88 | Time: 9172.9s
   📊 Metrics: Return=+8.42% | Sharpe=1.420 | DD=4.54% | Turnover=25.18%
   🎚️ Intra-Step TAPE: potential=0.2489 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0411 | critic_loss=0.6629 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3315 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0017 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4198 | ema=0.9241 | best_ema=0.9241 | no_improve=0
[CYCLE] Update 68/348 | Step 68,544/500,000 | Episode 88 | Time: 9310.8s
   📊 Metrics: Return=+8.76% | Sharpe=0.673 | DD=6.85% | Turnover=25.81%
   🎚️ Intra-Step TAPE: potential=0.2375 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0294 | critic_loss=0.4024 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2012 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0260
   🧠 Objective Experts: aux_loss=-0.0108 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6731 | ema=0.8990 | best_ema=0.8990 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=2.20 | range=[1.23, 10.31] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=2.52 | NEE=2.47 | NVDA=2.25  BOT: JPM=1.62 | XOM=1.56 | GLD=1.44
   🧬 FiLM: seq(dg=0.0046, db=0.0029, sat=0.0%) | latent(dg=0.0073, db=0.0036, sat=0.0%) | asset(dg=0.0024, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (31.2%), low_vol=40 (41.7%), medium_vol=26 (27.1%)
[CYCLE] Update 69/348 | Step 69,552/500,000 | Episode 88 | Time: 9448.1s
   📊 Metrics: Return=+13.60% | Sharpe=0.733 | DD=6.85% | Turnover=26.36%
   🎚️ Intra-Step TAPE: potential=0.3688 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0048 | critic_loss=0.5117 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2559 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.0417 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7327 | ema=0.8824 | best_ema=0.8824 | no_improve=0
[CYCLE] Update 70/348 | Step 70,560/500,000 | Episode 88 | Time: 9585.6s
   📊 Metrics: Return=+16.76% | Sharpe=0.674 | DD=6.85% | Turnover=26.36%
   🎚️ Intra-Step TAPE: potential=0.6683 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0649 | critic_loss=0.3162 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1581 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.1098 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6743 | ema=0.8616 | best_ema=0.8616 | no_improve=0
   🔬 Alpha Diversity: mean=2.63 | std=1.70 | range=[1.22, 9.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.35 | KO=4.23 | NVDA=2.44  BOT: XOM=1.93 | CAT=1.70 | AMZN=1.58
   🧬 FiLM: seq(dg=0.0034, db=0.0026, sat=0.0%) | latent(dg=0.0060, db=0.0033, sat=0.0%) | asset(dg=0.0023, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=30 (31.2%), low_vol=40 (41.7%), medium_vol=26 (27.1%)
[CYCLE] Update 71/348 | Step 71,568/500,000 | Episode 88 | Time: 9723.5s
   📊 Metrics: Return=+22.43% | Sharpe=0.705 | DD=6.85% | Turnover=26.13%
   🎚️ Intra-Step TAPE: potential=0.5351 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0699 | critic_loss=0.7326 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3663 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   🧠 Objective Experts: aux_loss=-0.1177 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7049 | ema=0.8459 | best_ema=0.8459 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp0p734_actor.weights.h5 (Sharpe=0.734, MDD=6.85%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00091_shp0p882_actor.weights.h5 (Sharpe=0.882, MDD=9.85%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00095_shp1p304_actor.weights.h5 (Sharpe=1.304, MDD=10.45%)
[CYCLE] Update 72/348 | Step 72,576/500,000 | Episode 96 | Time: 9854.6s
   📊 Metrics: Return=+28.59% | Sharpe=0.699 | DD=11.21% | Turnover=26.52%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0010 | critic_loss=0.4839 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2420 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   🧠 Objective Experts: aux_loss=-0.0470 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6993 | ema=0.8313 | best_ema=0.8313 | no_improve=0
   🔬 Alpha Diversity: mean=2.62 | std=1.78 | range=[1.22, 9.89] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=4.97 | NEE=3.83 | GLD=3.55  BOT: CAT=1.55 | NVDA=1.37 | AMZN=1.37
   🧬 FiLM: seq(dg=0.0033, db=0.0025, sat=0.0%) | latent(dg=0.0062, db=0.0033, sat=0.0%) | asset(dg=0.0028, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=32 (30.8%), low_vol=44 (42.3%), medium_vol=28 (26.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3849
[CYCLE] Update 73/348 | Step 73,584/500,000 | Episode 96 | Time: 9991.9s
   📊 Metrics: Return=+10.50% | Sharpe=3.406 | DD=1.82% | Turnover=24.59%
   🎚️ Intra-Step TAPE: potential=0.7402 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0424 | critic_loss=0.5640 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2820 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.0875 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.4058 | ema=1.0887 | best_ema=1.0887 | no_improve=0
[CYCLE] Update 74/348 | Step 74,592/500,000 | Episode 96 | Time: 10129.8s
   📊 Metrics: Return=+18.39% | Sharpe=2.713 | DD=2.75% | Turnover=24.79%
   🎚️ Intra-Step TAPE: potential=0.7319 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0406 | critic_loss=0.4768 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2384 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0283
   🧠 Objective Experts: aux_loss=-0.0048 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.7125 | ema=1.2511 | best_ema=1.2511 | no_improve=0
   🔬 Alpha Diversity: mean=2.66 | std=1.78 | range=[1.22, 9.27] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=4.23 | KO=4.20 | NEE=4.06  BOT: AMZN=1.67 | CAT=1.48 | NVDA=1.47
   🧬 FiLM: seq(dg=0.0046, db=0.0033, sat=0.0%) | latent(dg=0.0081, db=0.0042, sat=0.0%) | asset(dg=0.0029, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=32 (30.8%), low_vol=44 (42.3%), medium_vol=28 (26.9%)
[CYCLE] Update 75/348 | Step 75,600/500,000 | Episode 96 | Time: 10267.8s
   📊 Metrics: Return=+20.51% | Sharpe=1.355 | DD=8.41% | Turnover=24.85%
   🎚️ Intra-Step TAPE: potential=0.2517 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0387 | critic_loss=0.4834 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2417 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0284
   🧠 Objective Experts: aux_loss=-0.0816 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3554 | ema=1.2615 | best_ema=1.2615 | no_improve=0
[CYCLE] Update 76/348 | Step 76,608/500,000 | Episode 96 | Time: 10405.5s
   📊 Metrics: Return=+11.54% | Sharpe=0.435 | DD=12.38% | Turnover=25.04%
   🎚️ Intra-Step TAPE: potential=0.2277 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0704 | critic_loss=0.4191 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2096 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0279
   🧠 Objective Experts: aux_loss=-0.1159 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4350 | ema=1.1789 | best_ema=1.1789 | no_improve=0
   🔬 Alpha Diversity: mean=2.62 | std=1.91 | range=[1.22, 10.01] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=3.86 | KO=3.84 | GLD=3.25  BOT: NVDA=2.05 | CAT=1.89 | JPM=1.62
   🧬 FiLM: seq(dg=0.0038, db=0.0026, sat=0.0%) | latent(dg=0.0082, db=0.0040, sat=0.0%) | asset(dg=0.0026, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=32 (30.8%), low_vol=44 (42.3%), medium_vol=28 (26.9%)
[CYCLE] Update 77/348 | Step 77,616/500,000 | Episode 96 | Time: 10543.4s
   📊 Metrics: Return=+16.69% | Sharpe=0.440 | DD=21.20% | Turnover=25.17%
   🎚️ Intra-Step TAPE: potential=0.3103 | delta_reward=-0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0196 | critic_loss=0.4288 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2144 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=-0.0647 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4401 | ema=1.1050 | best_ema=1.1050 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00100_shp0p828_actor.weights.h5 (Sharpe=0.828, MDD=8.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00102_shp0p805_actor.weights.h5 (Sharpe=0.805, MDD=15.20%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00103_shp0p807_actor.weights.h5 (Sharpe=0.807, MDD=7.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00104_shp0p969_actor.weights.h5 (Sharpe=0.969, MDD=8.97%)
[CYCLE] Update 78/348 | Step 78,624/500,000 | Episode 104 | Time: 10675.6s
   📊 Metrics: Return=+44.19% | Sharpe=0.969 | DD=8.97% | Turnover=25.23%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0257 | critic_loss=0.5329 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2665 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0274
   🧠 Objective Experts: aux_loss=-0.0198 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9692 | ema=1.0914 | best_ema=1.0914 | no_improve=0
   🔬 Alpha Diversity: mean=2.63 | std=1.99 | range=[1.22, 10.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=6.05 | NEE=5.04 | KO=3.97  BOT: JPM=1.48 | CAT=1.45 | NVDA=1.41
   🧬 FiLM: seq(dg=0.0060, db=0.0043, sat=0.0%) | latent(dg=0.0091, db=0.0045, sat=0.0%) | asset(dg=0.0031, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (31.2%), low_vol=46 (41.1%), medium_vol=31 (27.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5202
[CYCLE] Update 79/348 | Step 79,632/500,000 | Episode 104 | Time: 10813.2s
   📊 Metrics: Return=-2.26% | Sharpe=-0.290 | DD=13.39% | Turnover=25.23%
   🎚️ Intra-Step TAPE: potential=0.5127 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0189 | critic_loss=0.5715 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2858 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0283
   🧠 Objective Experts: aux_loss=-0.0653 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2897 | ema=0.9533 | best_ema=0.9533 | no_improve=0
[CYCLE] Update 80/348 | Step 80,640/500,000 | Episode 104 | Time: 10951.1s
   📊 Metrics: Return=+12.12% | Sharpe=0.731 | DD=13.39% | Turnover=25.49%
   🎚️ Intra-Step TAPE: potential=0.6613 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1051 | critic_loss=0.4693 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2347 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0285
   🧠 Objective Experts: aux_loss=0.0586 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7306 | ema=0.9310 | best_ema=0.9310 | no_improve=0
   🔬 Alpha Diversity: mean=2.65 | std=1.80 | range=[1.22, 10.16] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.98 | KO=4.59 | BRK-B=3.32  BOT: NVDA=1.64 | JPM=1.64 | CAT=1.41
   🧬 FiLM: seq(dg=0.0047, db=0.0036, sat=0.0%) | latent(dg=0.0077, db=0.0038, sat=0.0%) | asset(dg=0.0032, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (31.2%), low_vol=46 (41.1%), medium_vol=31 (27.7%)
[CYCLE] Update 81/348 | Step 81,648/500,000 | Episode 104 | Time: 11088.5s
   📊 Metrics: Return=+6.07% | Sharpe=0.199 | DD=15.41% | Turnover=25.22%
   🎚️ Intra-Step TAPE: potential=0.2427 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0629 | critic_loss=0.5171 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2586 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0279
   🧠 Objective Experts: aux_loss=0.0173 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1993 | ema=0.8579 | best_ema=0.8579 | no_improve=0
[CYCLE] Update 82/348 | Step 82,656/500,000 | Episode 104 | Time: 11226.3s
   📊 Metrics: Return=+12.87% | Sharpe=0.306 | DD=18.13% | Turnover=24.94%
   🎚️ Intra-Step TAPE: potential=0.3381 | delta_reward=-0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0728 | critic_loss=0.4409 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2204 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.1187 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3062 | ema=0.8027 | best_ema=0.8027 | no_improve=0
   🔬 Alpha Diversity: mean=2.64 | std=1.91 | range=[1.22, 9.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.70 | GLD=3.46 | KO=3.42  BOT: BRK-B=1.89 | CAT=1.85 | XOM=1.76
   🧬 FiLM: seq(dg=0.0055, db=0.0041, sat=0.0%) | latent(dg=0.0084, db=0.0041, sat=0.0%) | asset(dg=0.0028, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (31.2%), low_vol=46 (41.1%), medium_vol=31 (27.7%)
[CYCLE] Update 83/348 | Step 83,664/500,000 | Episode 104 | Time: 11363.8s
   📊 Metrics: Return=+14.09% | Sharpe=0.271 | DD=18.13% | Turnover=24.72%
   🎚️ Intra-Step TAPE: potential=0.3521 | delta_reward=-0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1080 | critic_loss=0.3324 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1662 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.1532 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2706 | ema=0.7495 | best_ema=0.7495 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00108_shp1p047_actor.weights.h5 (Sharpe=1.047, MDD=9.12%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00109_shp0p774_actor.weights.h5 (Sharpe=0.774, MDD=7.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00111_shp1p513_actor.weights.h5 (Sharpe=1.513, MDD=9.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00112_shp1p183_actor.weights.h5 (Sharpe=1.183, MDD=9.71%)
[CYCLE] Update 84/348 | Step 84,672/500,000 | Episode 112 | Time: 11495.7s
   📊 Metrics: Return=+51.66% | Sharpe=1.183 | DD=9.71% | Turnover=24.52%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0038 | critic_loss=0.5833 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2916 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.0413 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1828 | ema=0.7928 | best_ema=0.7928 | no_improve=0
   🔬 Alpha Diversity: mean=2.60 | std=2.00 | range=[1.22, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=4.66 | KO=4.15 | AMZN=3.81  BOT: MSFT=1.57 | JPM=1.50 | CAT=1.38
   🧬 FiLM: seq(dg=0.0048, db=0.0039, sat=0.0%) | latent(dg=0.0079, db=0.0038, sat=0.0%) | asset(dg=0.0031, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=36 (30.0%), low_vol=51 (42.5%), medium_vol=33 (27.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5454
[CYCLE] Update 85/348 | Step 85,680/500,000 | Episode 112 | Time: 11633.1s
   📊 Metrics: Return=+2.08% | Sharpe=0.235 | DD=4.19% | Turnover=24.47%
   🎚️ Intra-Step TAPE: potential=0.2441 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1207 | critic_loss=0.4269 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2134 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.1669 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2353 | ema=0.7371 | best_ema=0.7371 | no_improve=0
[CYCLE] Update 86/348 | Step 86,688/500,000 | Episode 112 | Time: 11770.4s
   📊 Metrics: Return=+9.91% | Sharpe=0.695 | DD=5.66% | Turnover=25.45%
   🎚️ Intra-Step TAPE: potential=0.3344 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0290 | critic_loss=0.2584 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1292 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0276
   🧠 Objective Experts: aux_loss=-0.0160 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6952 | ema=0.7329 | best_ema=0.7329 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=2.01 | range=[1.22, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.05 | GLD=3.85 | KO=3.69  BOT: XOM=1.88 | JPM=1.75 | CAT=1.51
   🧬 FiLM: seq(dg=0.0060, db=0.0047, sat=0.0%) | latent(dg=0.0088, db=0.0042, sat=0.0%) | asset(dg=0.0029, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=36 (30.0%), low_vol=51 (42.5%), medium_vol=33 (27.5%)
[CYCLE] Update 87/348 | Step 87,696/500,000 | Episode 112 | Time: 11908.0s
   📊 Metrics: Return=+15.87% | Sharpe=0.778 | DD=5.66% | Turnover=24.99%
   🎚️ Intra-Step TAPE: potential=0.6371 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0648 | critic_loss=0.3084 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1542 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0278
   🧠 Objective Experts: aux_loss=0.0197 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7777 | ema=0.7374 | best_ema=0.7374 | no_improve=0
[CYCLE] Update 88/348 | Step 88,704/500,000 | Episode 112 | Time: 12045.2s
   📊 Metrics: Return=+23.65% | Sharpe=0.845 | DD=5.66% | Turnover=25.22%
   🎚️ Intra-Step TAPE: potential=0.5178 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0265 | critic_loss=0.4055 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2027 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.0716 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8452 | ema=0.7481 | best_ema=0.7481 | no_improve=0
   🔬 Alpha Diversity: mean=2.62 | std=2.05 | range=[1.22, 9.92] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=4.50 | NEE=3.59 | KO=2.75  BOT: CAT=1.56 | XOM=1.46 | JPM=1.44
   🧬 FiLM: seq(dg=0.0082, db=0.0063, sat=0.0%) | latent(dg=0.0108, db=0.0051, sat=0.0%) | asset(dg=0.0030, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=36 (30.0%), low_vol=51 (42.5%), medium_vol=33 (27.5%)
[CYCLE] Update 89/348 | Step 89,712/500,000 | Episode 112 | Time: 12182.7s
   📊 Metrics: Return=+27.41% | Sharpe=0.766 | DD=5.66% | Turnover=25.49%
   🎚️ Intra-Step TAPE: potential=0.2668 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0401 | critic_loss=0.3470 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1735 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0274
   🧠 Objective Experts: aux_loss=-0.0849 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7665 | ema=0.7500 | best_ema=0.7500 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00113_shp0p752_actor.weights.h5 (Sharpe=0.752, MDD=8.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00115_shp1p108_actor.weights.h5 (Sharpe=1.108, MDD=9.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00117_shp0p779_actor.weights.h5 (Sharpe=0.779, MDD=10.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00118_shp1p050_actor.weights.h5 (Sharpe=1.050, MDD=9.31%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00119_shp1p065_actor.weights.h5 (Sharpe=1.065, MDD=8.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00120_shp1p059_actor.weights.h5 (Sharpe=1.059, MDD=8.20%)
[CYCLE] Update 90/348 | Step 90,720/500,000 | Episode 120 | Time: 12315.4s
   📊 Metrics: Return=+46.77% | Sharpe=1.059 | DD=8.20% | Turnover=24.73%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0091 | critic_loss=0.7959 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3979 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0274
   🧠 Objective Experts: aux_loss=-0.0357 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0593 | ema=0.7809 | best_ema=0.7809 | no_improve=0
   🔬 Alpha Diversity: mean=2.61 | std=1.95 | range=[1.21, 10.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=5.17 | NEE=3.94 | KO=3.75  BOT: XOM=1.86 | JPM=1.74 | CAT=1.72
   🧬 FiLM: seq(dg=0.0084, db=0.0065, sat=0.0%) | latent(dg=0.0105, db=0.0049, sat=0.0%) | asset(dg=0.0034, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=39 (30.5%), low_vol=53 (41.4%), medium_vol=36 (28.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5472
[CYCLE] Update 91/348 | Step 91,728/500,000 | Episode 120 | Time: 12452.7s
   📊 Metrics: Return=+4.48% | Sharpe=0.520 | DD=8.79% | Turnover=24.02%
   🎚️ Intra-Step TAPE: potential=0.6188 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0373 | critic_loss=0.5878 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2939 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.0087 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5199 | ema=0.7548 | best_ema=0.7548 | no_improve=0
[CYCLE] Update 92/348 | Step 92,736/500,000 | Episode 120 | Time: 12590.3s
   📊 Metrics: Return=+20.21% | Sharpe=1.217 | DD=8.79% | Turnover=23.94%
   🎚️ Intra-Step TAPE: potential=0.7463 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0333 | critic_loss=0.6107 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3054 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0283
   🧠 Objective Experts: aux_loss=-0.0788 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2168 | ema=0.8010 | best_ema=0.8010 | no_improve=0
   🔬 Alpha Diversity: mean=2.62 | std=1.67 | range=[1.21, 10.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=3.99 | KO=3.54 | BRK-B=3.50  BOT: NVDA=2.16 | XOM=2.04 | CAT=1.54
   🧬 FiLM: seq(dg=0.0041, db=0.0040, sat=0.0%) | latent(dg=0.0065, db=0.0035, sat=0.0%) | asset(dg=0.0030, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=39 (30.5%), low_vol=53 (41.4%), medium_vol=36 (28.1%)
[CYCLE] Update 93/348 | Step 93,744/500,000 | Episode 120 | Time: 12727.7s
   📊 Metrics: Return=+27.38% | Sharpe=1.175 | DD=8.79% | Turnover=24.30%
   🎚️ Intra-Step TAPE: potential=0.2331 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1053 | critic_loss=0.4733 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2367 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.1502 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1755 | ema=0.8385 | best_ema=0.8385 | no_improve=0
[CYCLE] Update 94/348 | Step 94,752/500,000 | Episode 120 | Time: 12865.4s
   📊 Metrics: Return=+39.53% | Sharpe=1.306 | DD=8.79% | Turnover=24.31%
   🎚️ Intra-Step TAPE: potential=0.6969 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1412 | critic_loss=0.4105 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2052 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0278
   🧠 Objective Experts: aux_loss=-0.1862 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3062 | ema=0.8852 | best_ema=0.8852 | no_improve=0
   🔬 Alpha Diversity: mean=2.62 | std=1.96 | range=[1.22, 10.53] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=3.80 | KO=3.74 | GLD=3.24  BOT: JPM=1.64 | NVDA=1.56 | CAT=1.38
   🧬 FiLM: seq(dg=0.0073, db=0.0060, sat=0.0%) | latent(dg=0.0097, db=0.0047, sat=0.0%) | asset(dg=0.0033, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=39 (30.5%), low_vol=53 (41.4%), medium_vol=36 (28.1%)
[CYCLE] Update 95/348 | Step 95,760/500,000 | Episode 120 | Time: 13003.2s
   📊 Metrics: Return=+55.75% | Sharpe=1.512 | DD=8.79% | Turnover=24.12%
   🎚️ Intra-Step TAPE: potential=0.6618 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0260 | critic_loss=0.2574 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1287 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=-0.0185 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5124 | ema=0.9479 | best_ema=0.9479 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00121_shp1p324_actor.weights.h5 (Sharpe=1.324, MDD=9.44%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00122_shp0p729_actor.weights.h5 (Sharpe=0.729, MDD=8.73%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00123_shp0p855_actor.weights.h5 (Sharpe=0.855, MDD=7.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00127_shp0p737_actor.weights.h5 (Sharpe=0.737, MDD=8.43%)
[CYCLE] Update 96/348 | Step 96,768/500,000 | Episode 128 | Time: 13135.5s
   📊 Metrics: Return=+36.98% | Sharpe=0.659 | DD=15.50% | Turnover=24.81%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0400 | critic_loss=0.6034 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3017 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0274
   🧠 Objective Experts: aux_loss=-0.0044 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6587 | ema=0.9190 | best_ema=0.9190 | no_improve=0
   🔬 Alpha Diversity: mean=2.60 | std=1.99 | range=[1.21, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.41 | NEE=3.94 | GLD=3.85  BOT: NVDA=1.79 | JPM=1.71 | CAT=1.60
   🧬 FiLM: seq(dg=0.0083, db=0.0067, sat=0.0%) | latent(dg=0.0104, db=0.0050, sat=0.0%) | asset(dg=0.0034, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=54 (39.7%), medium_vol=38 (27.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3623
[CYCLE] Update 97/348 | Step 97,776/500,000 | Episode 128 | Time: 13272.9s
   📊 Metrics: Return=+14.40% | Sharpe=1.862 | DD=7.32% | Turnover=24.61%
   🎚️ Intra-Step TAPE: potential=0.4077 | delta_reward=-0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0392 | critic_loss=0.9666 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4833 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0291
   🧠 Objective Experts: aux_loss=-0.0864 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8618 | ema=1.0133 | best_ema=1.0133 | no_improve=0
[CYCLE] Update 98/348 | Step 98,784/500,000 | Episode 128 | Time: 13410.3s
   📊 Metrics: Return=+25.75% | Sharpe=1.813 | DD=7.32% | Turnover=24.36%
   🎚️ Intra-Step TAPE: potential=0.6348 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1181 | critic_loss=0.4339 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2169 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0281
   🧠 Objective Experts: aux_loss=-0.1632 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8131 | ema=1.0933 | best_ema=1.0933 | no_improve=0
   🔬 Alpha Diversity: mean=2.63 | std=1.80 | range=[1.21, 10.33] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=3.56 | KO=3.54 | GLD=3.48  BOT: JPM=1.96 | MSFT=1.72 | CAT=1.67
   🧬 FiLM: seq(dg=0.0077, db=0.0065, sat=0.0%) | latent(dg=0.0105, db=0.0051, sat=0.0%) | asset(dg=0.0035, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=54 (39.7%), medium_vol=38 (27.9%)
[CYCLE] Update 99/348 | Step 99,792/500,000 | Episode 128 | Time: 13547.6s
   📊 Metrics: Return=+46.85% | Sharpe=1.959 | DD=7.32% | Turnover=24.60%
   🎚️ Intra-Step TAPE: potential=0.7338 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1276 | critic_loss=0.2970 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1485 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.1727 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.9587 | ema=1.1798 | best_ema=1.1798 | no_improve=0
[CYCLE] Update 100/348 | Step 100,800/500,000 | Episode 128 | Time: 13685.0s
   📊 Metrics: Return=+64.29% | Sharpe=2.110 | DD=7.32% | Turnover=24.32%
   🎚️ Intra-Step TAPE: potential=0.7316 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0227 | critic_loss=0.2132 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1066 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0276
   🧠 Objective Experts: aux_loss=-0.0672 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1096 | ema=1.2728 | best_ema=1.2728 | no_improve=0
   🔬 Alpha Diversity: mean=2.61 | std=1.85 | range=[1.21, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.37 | KO=3.86 | GLD=3.48  BOT: NVDA=2.06 | MSFT=1.86 | CAT=1.53
   🧬 FiLM: seq(dg=0.0088, db=0.0074, sat=0.0%) | latent(dg=0.0114, db=0.0055, sat=0.0%) | asset(dg=0.0034, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=44 (32.4%), low_vol=54 (39.7%), medium_vol=38 (27.9%)
[CYCLE] Update 101/348 | Step 101,808/500,000 | Episode 128 | Time: 13822.6s
   📊 Metrics: Return=+78.32% | Sharpe=1.931 | DD=9.41% | Turnover=24.12%
   🎚️ Intra-Step TAPE: potential=0.3881 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0541 | critic_loss=0.2965 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1482 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.0991 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.9315 | ema=1.3387 | best_ema=1.3387 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00129_shp1p685_actor.weights.h5 (Sharpe=1.685, MDD=9.41%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00130_shp0p821_actor.weights.h5 (Sharpe=0.821, MDD=17.45%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00133_shp0p909_actor.weights.h5 (Sharpe=0.909, MDD=13.49%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00135_shp0p794_actor.weights.h5 (Sharpe=0.794, MDD=14.52%)
[CYCLE] Update 102/348 | Step 102,816/500,000 | Episode 136 | Time: 13954.4s
   📊 Metrics: Return=+25.32% | Sharpe=0.444 | DD=16.86% | Turnover=25.37%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0498 | critic_loss=0.6446 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3223 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0274
   🧠 Objective Experts: aux_loss=-0.0941 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4444 | ema=1.2492 | best_ema=1.2492 | no_improve=0
   🔬 Alpha Diversity: mean=2.58 | std=1.99 | range=[1.21, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.67 | NEE=3.25 | AMZN=2.91  BOT: XOM=2.06 | JPM=1.92 | CAT=1.53
   🧬 FiLM: seq(dg=0.0076, db=0.0058, sat=0.0%) | latent(dg=0.0117, db=0.0056, sat=0.0%) | asset(dg=0.0028, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=47 (32.6%), low_vol=57 (39.6%), medium_vol=40 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2900
[CYCLE] Update 103/348 | Step 103,824/500,000 | Episode 136 | Time: 14091.9s
   📊 Metrics: Return=+5.57% | Sharpe=1.060 | DD=3.69% | Turnover=24.92%
   🎚️ Intra-Step TAPE: potential=0.7456 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1015 | critic_loss=0.4403 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2201 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.1466 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0595 | ema=1.2303 | best_ema=1.2303 | no_improve=0
[CYCLE] Update 104/348 | Step 104,832/500,000 | Episode 136 | Time: 14229.7s
   📊 Metrics: Return=+14.86% | Sharpe=1.678 | DD=3.69% | Turnover=23.96%
   🎚️ Intra-Step TAPE: potential=0.7455 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1021 | critic_loss=0.3121 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1561 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0278
   🧠 Objective Experts: aux_loss=-0.1469 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6779 | ema=1.2750 | best_ema=1.2750 | no_improve=0
   🔬 Alpha Diversity: mean=2.61 | std=1.80 | range=[1.21, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=4.09 | KO=3.97 | BRK-B=3.48  BOT: MSFT=1.75 | NVDA=1.56 | CAT=1.55
   🧬 FiLM: seq(dg=0.0086, db=0.0068, sat=0.0%) | latent(dg=0.0120, db=0.0058, sat=0.0%) | asset(dg=0.0037, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=47 (32.6%), low_vol=57 (39.6%), medium_vol=40 (27.8%)
[CYCLE] Update 105/348 | Step 105,840/500,000 | Episode 136 | Time: 14367.7s
   📊 Metrics: Return=+21.83% | Sharpe=1.183 | DD=10.17% | Turnover=23.88%
   🎚️ Intra-Step TAPE: potential=0.2257 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0528 | critic_loss=0.4188 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2094 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0279
   🧠 Objective Experts: aux_loss=-0.0977 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1825 | ema=1.2658 | best_ema=1.2658 | no_improve=0
[CYCLE] Update 106/348 | Step 106,848/500,000 | Episode 136 | Time: 14505.8s
   📊 Metrics: Return=+29.05% | Sharpe=1.126 | DD=10.17% | Turnover=24.45%
   🎚️ Intra-Step TAPE: potential=0.7262 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1397 | critic_loss=0.2991 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1495 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.1846 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1265 | ema=1.2519 | best_ema=1.2519 | no_improve=0
   🔬 Alpha Diversity: mean=2.57 | std=1.78 | range=[1.21, 10.27] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=3.55 | NEE=3.07 | KO=2.87  BOT: BRK-B=2.46 | CAT=2.31 | XOM=2.07
   🧬 FiLM: seq(dg=0.0091, db=0.0077, sat=0.0%) | latent(dg=0.0106, db=0.0052, sat=0.0%) | asset(dg=0.0031, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=47 (32.6%), low_vol=57 (39.6%), medium_vol=40 (27.8%)
[CYCLE] Update 107/348 | Step 107,856/500,000 | Episode 136 | Time: 14643.5s
   📊 Metrics: Return=+23.24% | Sharpe=0.571 | DD=17.67% | Turnover=24.58%
   🎚️ Intra-Step TAPE: potential=0.6721 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0217 | critic_loss=0.5623 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2811 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=-0.0662 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5707 | ema=1.1837 | best_ema=1.1837 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00139_shp1p248_actor.weights.h5 (Sharpe=1.248, MDD=9.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00140_shp1p335_actor.weights.h5 (Sharpe=1.335, MDD=9.44%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00142_shp0p798_actor.weights.h5 (Sharpe=0.798, MDD=7.32%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00143_shp0p752_actor.weights.h5 (Sharpe=0.752, MDD=8.62%)
[CYCLE] Update 108/348 | Step 108,864/500,000 | Episode 144 | Time: 14775.6s
   📊 Metrics: Return=+34.35% | Sharpe=0.532 | DD=18.95% | Turnover=24.99%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0223 | critic_loss=0.4021 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2010 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.0665 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5321 | ema=1.1186 | best_ema=1.1186 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=2.09 | range=[1.21, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=3.43 | AMZN=3.24 | GLD=3.08  BOT: JPM=1.92 | NVDA=1.90 | CAT=1.64
   🧬 FiLM: seq(dg=0.0112, db=0.0091, sat=0.0%) | latent(dg=0.0123, db=0.0058, sat=0.0%) | asset(dg=0.0032, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=59 (38.8%), medium_vol=43 (28.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.002) | TAPE=0.3105
[CYCLE] Update 109/348 | Step 109,872/500,000 | Episode 144 | Time: 14913.4s
   📊 Metrics: Return=+8.74% | Sharpe=1.559 | DD=4.74% | Turnover=23.59%
   🎚️ Intra-Step TAPE: potential=0.2386 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1125 | critic_loss=0.6383 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3191 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=-0.1575 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5591 | ema=1.1626 | best_ema=1.1626 | no_improve=0
[CYCLE] Update 110/348 | Step 110,880/500,000 | Episode 144 | Time: 15051.3s
   📊 Metrics: Return=+17.27% | Sharpe=1.291 | DD=7.04% | Turnover=23.92%
   🎚️ Intra-Step TAPE: potential=0.3739 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0488 | critic_loss=0.2948 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1474 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=-0.0935 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2912 | ema=1.1755 | best_ema=1.1755 | no_improve=0
   🔬 Alpha Diversity: mean=2.62 | std=1.87 | range=[1.21, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: KO=4.32 | NEE=4.14 | GLD=3.37  BOT: XOM=2.02 | JPM=1.97 | CAT=1.41
   🧬 FiLM: seq(dg=0.0131, db=0.0107, sat=0.0%) | latent(dg=0.0159, db=0.0073, sat=0.0%) | asset(dg=0.0039, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=59 (38.8%), medium_vol=43 (28.3%)
[CYCLE] Update 111/348 | Step 111,888/500,000 | Episode 144 | Time: 15189.2s
   📊 Metrics: Return=+24.07% | Sharpe=1.169 | DD=7.04% | Turnover=24.30%
   🎚️ Intra-Step TAPE: potential=0.2546 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0718 | critic_loss=0.2178 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1089 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0267
   🧠 Objective Experts: aux_loss=-0.1158 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1693 | ema=1.1749 | best_ema=1.1749 | no_improve=0
[CYCLE] Update 112/348 | Step 112,896/500,000 | Episode 144 | Time: 15326.6s
   📊 Metrics: Return=+25.18% | Sharpe=0.801 | DD=7.92% | Turnover=24.51%
   🎚️ Intra-Step TAPE: potential=0.2460 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0366 | critic_loss=0.4371 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2185 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0271
   🧠 Objective Experts: aux_loss=-0.0075 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8008 | ema=1.1375 | best_ema=1.1375 | no_improve=0
   🔬 Alpha Diversity: mean=2.60 | std=2.05 | range=[1.21, 10.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=3.98 | KO=3.59 | NEE=3.26  BOT: CAT=1.64 | MSFT=1.59 | BRK-B=1.59
   🧬 FiLM: seq(dg=0.0125, db=0.0104, sat=0.0%) | latent(dg=0.0162, db=0.0076, sat=0.0%) | asset(dg=0.0036, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=50 (32.9%), low_vol=59 (38.8%), medium_vol=43 (28.3%)
[CYCLE] Update 113/348 | Step 113,904/500,000 | Episode 144 | Time: 15464.1s
   📊 Metrics: Return=+55.71% | Sharpe=1.351 | DD=8.60% | Turnover=24.91%
   🎚️ Intra-Step TAPE: potential=0.7243 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0209 | critic_loss=0.4119 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2060 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0271
   🧠 Objective Experts: aux_loss=-0.0649 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3507 | ema=1.1588 | best_ema=1.1588 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00145_shp1p531_actor.weights.h5 (Sharpe=1.531, MDD=8.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00146_shp0p730_actor.weights.h5 (Sharpe=0.730, MDD=8.15%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00147_shp1p525_actor.weights.h5 (Sharpe=1.525, MDD=9.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00151_shp0p842_actor.weights.h5 (Sharpe=0.842, MDD=21.78%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00152_shp0p972_actor.weights.h5 (Sharpe=0.972, MDD=10.62%)
[CYCLE] Update 114/348 | Step 114,912/500,000 | Episode 152 | Time: 15596.7s
   📊 Metrics: Return=+51.06% | Sharpe=0.972 | DD=10.62% | Turnover=24.32%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0633 | critic_loss=1.4284 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7142 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.1074 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9720 | ema=1.1401 | best_ema=1.1401 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=1.79 | range=[1.20, 10.35] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.38 | GLD=3.43 | CAT=3.01  BOT: NEE=2.20 | XOM=2.01 | BRK-B=1.98
   🧬 FiLM: seq(dg=0.0091, db=0.0082, sat=0.0%) | latent(dg=0.0112, db=0.0056, sat=0.0%) | asset(dg=0.0029, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=62 (38.8%), medium_vol=45 (28.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5033
[CYCLE] Update 115/348 | Step 115,920/500,000 | Episode 152 | Time: 15734.4s
   📊 Metrics: Return=+3.90% | Sharpe=0.548 | DD=4.70% | Turnover=27.84%
   🎚️ Intra-Step TAPE: potential=0.2479 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0093 | critic_loss=0.7419 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3709 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0272
   🧠 Objective Experts: aux_loss=-0.0355 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5484 | ema=1.0809 | best_ema=1.0809 | no_improve=0
[CYCLE] Update 116/348 | Step 116,928/500,000 | Episode 152 | Time: 15872.8s
   📊 Metrics: Return=+12.63% | Sharpe=0.879 | DD=6.10% | Turnover=26.48%
   🎚️ Intra-Step TAPE: potential=0.2907 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1238 | critic_loss=0.3813 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1906 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.1679 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8790 | ema=1.0607 | best_ema=1.0607 | no_improve=0
   🔬 Alpha Diversity: mean=2.56 | std=1.92 | range=[1.20, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.65 | KO=3.07 | NEE=2.96  BOT: JPM=2.15 | GLD=1.97 | CAT=1.71
   🧬 FiLM: seq(dg=0.0090, db=0.0083, sat=0.0%) | latent(dg=0.0110, db=0.0056, sat=0.0%) | asset(dg=0.0031, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=62 (38.8%), medium_vol=45 (28.1%)
[CYCLE] Update 117/348 | Step 117,936/500,000 | Episode 152 | Time: 16010.9s
   📊 Metrics: Return=+14.99% | Sharpe=0.709 | DD=6.10% | Turnover=25.88%
   🎚️ Intra-Step TAPE: potential=0.2372 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1249 | critic_loss=0.2766 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1383 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0264
   🧠 Objective Experts: aux_loss=-0.1686 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7092 | ema=1.0256 | best_ema=1.0256 | no_improve=0
[CYCLE] Update 118/348 | Step 118,944/500,000 | Episode 152 | Time: 16148.4s
   📊 Metrics: Return=+23.40% | Sharpe=0.778 | DD=6.90% | Turnover=25.84%
   🎚️ Intra-Step TAPE: potential=0.6831 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0575 | critic_loss=0.2194 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1097 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0271
   🧠 Objective Experts: aux_loss=-0.1019 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7777 | ema=1.0008 | best_ema=1.0008 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=1.87 | range=[1.20, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.94 | NEE=3.25 | KO=3.20  BOT: XOM=2.10 | BRK-B=2.09 | CAT=1.79
   🧬 FiLM: seq(dg=0.0104, db=0.0095, sat=0.0%) | latent(dg=0.0133, db=0.0064, sat=0.0%) | asset(dg=0.0033, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=53 (33.1%), low_vol=62 (38.8%), medium_vol=45 (28.1%)
[CYCLE] Update 119/348 | Step 119,952/500,000 | Episode 152 | Time: 16286.0s
   📊 Metrics: Return=+33.70% | Sharpe=0.800 | DD=9.94% | Turnover=25.94%
   🎚️ Intra-Step TAPE: potential=0.5646 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0293 | critic_loss=0.5003 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2501 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0263
   🧠 Objective Experts: aux_loss=-0.0728 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7999 | ema=0.9807 | best_ema=0.9807 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00153_shp0p795_actor.weights.h5 (Sharpe=0.795, MDD=13.24%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00154_shp1p559_actor.weights.h5 (Sharpe=1.559, MDD=11.90%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00157_shp1p464_actor.weights.h5 (Sharpe=1.464, MDD=12.78%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00160_shp0p932_actor.weights.h5 (Sharpe=0.932, MDD=24.02%)
[CYCLE] Update 120/348 | Step 120,960/500,000 | Episode 160 | Time: 16418.0s
   📊 Metrics: Return=+53.03% | Sharpe=0.932 | DD=24.02% | Turnover=24.48%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0314 | critic_loss=0.7342 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3671 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.0742 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9324 | ema=0.9759 | best_ema=0.9759 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.22 | range=[1.20, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.29 | MSFT=4.18 | AMZN=3.65  BOT: KO=1.64 | NEE=1.63 | GLD=1.60
   🧬 FiLM: seq(dg=0.0100, db=0.0083, sat=0.0%) | latent(dg=0.0137, db=0.0065, sat=0.0%) | asset(dg=0.0033, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (32.7%), low_vol=65 (38.7%), medium_vol=48 (28.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.051 (peak 0.094) | TAPE=0.4728
[CYCLE] Update 121/348 | Step 121,968/500,000 | Episode 160 | Time: 16555.5s
   📊 Metrics: Return=+6.92% | Sharpe=1.096 | DD=5.69% | Turnover=24.26%
   🎚️ Intra-Step TAPE: potential=0.6448 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0314 | critic_loss=0.3878 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1939 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0258
   🧠 Objective Experts: aux_loss=-0.0755 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0961 | ema=0.9879 | best_ema=0.9879 | no_improve=0
[CYCLE] Update 122/348 | Step 122,976/500,000 | Episode 160 | Time: 16693.1s
   📊 Metrics: Return=+2.98% | Sharpe=0.143 | DD=6.77% | Turnover=25.42%
   🎚️ Intra-Step TAPE: potential=0.2384 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0293 | critic_loss=0.4053 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2026 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0267
   🧠 Objective Experts: aux_loss=-0.0733 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1434 | ema=0.9034 | best_ema=0.9034 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.15 | range=[1.20, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.43 | AMZN=2.95 | JPM=2.67  BOT: KO=1.73 | NEE=1.71 | XOM=1.58
   🧬 FiLM: seq(dg=0.0100, db=0.0086, sat=0.0%) | latent(dg=0.0132, db=0.0064, sat=0.0%) | asset(dg=0.0029, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (32.7%), low_vol=65 (38.7%), medium_vol=48 (28.6%)
[CYCLE] Update 123/348 | Step 123,984/500,000 | Episode 160 | Time: 16831.0s
   📊 Metrics: Return=+15.02% | Sharpe=0.685 | DD=6.77% | Turnover=25.74%
   🎚️ Intra-Step TAPE: potential=0.2573 | delta_reward=-0.0035
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0322 | critic_loss=0.3778 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1889 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0263
   🧠 Objective Experts: aux_loss=-0.0756 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6852 | ema=0.8816 | best_ema=0.8816 | no_improve=0
[CYCLE] Update 124/348 | Step 124,992/500,000 | Episode 160 | Time: 16969.1s
   📊 Metrics: Return=+17.25% | Sharpe=0.493 | DD=10.89% | Turnover=25.40%
   🎚️ Intra-Step TAPE: potential=0.2353 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0123 | critic_loss=0.4092 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2046 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.0307 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4932 | ema=0.8428 | best_ema=0.8428 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=1.97 | range=[1.20, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.06 | NVDA=3.99 | MSFT=3.02  BOT: XOM=2.03 | GLD=1.98 | NEE=1.69
   🧬 FiLM: seq(dg=0.0099, db=0.0085, sat=0.0%) | latent(dg=0.0123, db=0.0061, sat=0.0%) | asset(dg=0.0030, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (32.7%), low_vol=65 (38.7%), medium_vol=48 (28.6%)
[CYCLE] Update 125/348 | Step 126,000/500,000 | Episode 160 | Time: 17108.0s
   📊 Metrics: Return=+50.68% | Sharpe=1.089 | DD=11.21% | Turnover=25.30%
   🎚️ Intra-Step TAPE: potential=0.7243 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0271 | critic_loss=0.5837 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2918 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.0714 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0892 | ema=0.8674 | best_ema=0.8674 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00161_shp1p317_actor.weights.h5 (Sharpe=1.317, MDD=11.21%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00163_shp0p796_actor.weights.h5 (Sharpe=0.796, MDD=19.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00165_shp0p797_actor.weights.h5 (Sharpe=0.797, MDD=11.30%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00166_shp0p707_actor.weights.h5 (Sharpe=0.707, MDD=20.16%)
[CYCLE] Update 126/348 | Step 127,008/500,000 | Episode 168 | Time: 17240.5s
   📊 Metrics: Return=+32.10% | Sharpe=0.658 | DD=8.44% | Turnover=25.94%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0371 | critic_loss=0.5363 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2681 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0265
   🧠 Objective Experts: aux_loss=-0.0808 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6583 | ema=0.8465 | best_ema=0.8465 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=1.74 | range=[1.20, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.36 | AMZN=3.93 | CAT=2.61  BOT: GLD=2.17 | XOM=2.03 | NEE=1.83
   🧬 FiLM: seq(dg=0.0087, db=0.0080, sat=0.0%) | latent(dg=0.0114, db=0.0059, sat=0.0%) | asset(dg=0.0027, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=58 (33.0%), low_vol=69 (39.2%), medium_vol=49 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.038) | TAPE=0.3706
[CYCLE] Update 127/348 | Step 128,016/500,000 | Episode 168 | Time: 17379.1s
   📊 Metrics: Return=+5.18% | Sharpe=0.599 | DD=6.79% | Turnover=25.43%
   🎚️ Intra-Step TAPE: potential=0.2552 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0089 | critic_loss=0.4714 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2357 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0267
   🧠 Objective Experts: aux_loss=-0.0529 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5995 | ema=0.8218 | best_ema=0.8218 | no_improve=0
[CYCLE] Update 128/348 | Step 129,024/500,000 | Episode 168 | Time: 17517.1s
   📊 Metrics: Return=+6.05% | Sharpe=0.335 | DD=8.59% | Turnover=25.40%
   🎚️ Intra-Step TAPE: potential=0.2419 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0581 | critic_loss=0.3481 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1740 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0264
   🧠 Objective Experts: aux_loss=-0.1016 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3350 | ema=0.7731 | best_ema=0.7731 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.08 | range=[1.20, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.22 | AMZN=3.98 | JPM=3.06  BOT: NEE=1.64 | XOM=1.57 | KO=1.57
   🧬 FiLM: seq(dg=0.0080, db=0.0078, sat=0.0%) | latent(dg=0.0099, db=0.0053, sat=0.0%) | asset(dg=0.0027, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=58 (33.0%), low_vol=69 (39.2%), medium_vol=49 (27.8%)
[CYCLE] Update 129/348 | Step 130,032/500,000 | Episode 168 | Time: 17655.3s
   📊 Metrics: Return=+16.25% | Sharpe=0.667 | DD=8.59% | Turnover=25.67%
   🎚️ Intra-Step TAPE: potential=0.6526 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0988 | critic_loss=0.4667 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2333 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0267
   🧠 Objective Experts: aux_loss=-0.1426 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6672 | ema=0.7625 | best_ema=0.7625 | no_improve=0
[CYCLE] Update 130/348 | Step 131,040/500,000 | Episode 168 | Time: 17792.7s
   📊 Metrics: Return=+17.23% | Sharpe=0.530 | DD=8.59% | Turnover=26.01%
   🎚️ Intra-Step TAPE: potential=0.5099 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0028 | critic_loss=0.2764 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1382 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0263
   🧠 Objective Experts: aux_loss=-0.0407 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5296 | ema=0.7392 | best_ema=0.7392 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=1.88 | range=[1.20, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.17 | AMZN=3.35 | GLD=2.97  BOT: MSFT=2.01 | KO=1.89 | NEE=1.76
   🧬 FiLM: seq(dg=0.0075, db=0.0078, sat=0.0%) | latent(dg=0.0094, db=0.0053, sat=0.0%) | asset(dg=0.0027, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=58 (33.0%), low_vol=69 (39.2%), medium_vol=49 (27.8%)
[CYCLE] Update 131/348 | Step 132,048/500,000 | Episode 168 | Time: 17930.2s
   📊 Metrics: Return=+19.33% | Sharpe=0.467 | DD=8.59% | Turnover=25.87%
   🎚️ Intra-Step TAPE: potential=0.2370 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0564 | critic_loss=0.4976 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2488 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0261
   🧠 Objective Experts: aux_loss=-0.0998 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4673 | ema=0.7121 | best_ema=0.7121 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00171_shp1p426_actor.weights.h5 (Sharpe=1.426, MDD=9.86%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00172_shp1p245_actor.weights.h5 (Sharpe=1.245, MDD=9.81%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00173_shp1p145_actor.weights.h5 (Sharpe=1.145, MDD=9.24%)
[CYCLE] Update 132/348 | Step 133,056/500,000 | Episode 176 | Time: 18061.8s
   📊 Metrics: Return=+26.59% | Sharpe=0.445 | DD=18.54% | Turnover=25.58%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0595 | critic_loss=0.6378 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3189 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0261
   🧠 Objective Experts: aux_loss=-0.1027 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4452 | ema=0.6854 | best_ema=0.6854 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.14 | range=[1.20, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.33 | AMZN=3.59 | GLD=2.98  BOT: CAT=1.79 | NEE=1.74 | BRK-B=1.67
   🧬 FiLM: seq(dg=0.0107, db=0.0100, sat=0.0%) | latent(dg=0.0134, db=0.0070, sat=0.0%) | asset(dg=0.0030, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=63 (34.2%), low_vol=71 (38.6%), medium_vol=50 (27.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.002) | TAPE=0.2912
[CYCLE] Update 133/348 | Step 134,064/500,000 | Episode 176 | Time: 18199.2s
   📊 Metrics: Return=+23.62% | Sharpe=3.400 | DD=3.86% | Turnover=25.59%
   🎚️ Intra-Step TAPE: potential=0.7486 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0466 | critic_loss=0.9394 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4697 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0260
   🧠 Objective Experts: aux_loss=-0.0911 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=3.4005 | ema=0.9569 | best_ema=0.9569 | no_improve=0
[CYCLE] Update 134/348 | Step 135,072/500,000 | Episode 176 | Time: 18337.0s
   📊 Metrics: Return=+21.03% | Sharpe=1.366 | DD=8.42% | Turnover=25.53%
   🎚️ Intra-Step TAPE: potential=0.2354 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1153 | critic_loss=0.3644 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1822 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0262
   🧠 Objective Experts: aux_loss=-0.1588 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3665 | ema=0.9978 | best_ema=0.9978 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=1.98 | range=[1.20, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.32 | AMZN=3.52 | JPM=2.96  BOT: KO=2.04 | NEE=2.01 | CAT=1.94
   🧬 FiLM: seq(dg=0.0137, db=0.0119, sat=0.0%) | latent(dg=0.0155, db=0.0078, sat=0.0%) | asset(dg=0.0035, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=63 (34.2%), low_vol=71 (38.6%), medium_vol=50 (27.2%)
[CYCLE] Update 135/348 | Step 136,080/500,000 | Episode 176 | Time: 18474.9s
   📊 Metrics: Return=+25.82% | Sharpe=0.761 | DD=19.53% | Turnover=25.39%
   🎚️ Intra-Step TAPE: potential=0.3504 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0594 | critic_loss=0.3270 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1635 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0260
   🧠 Objective Experts: aux_loss=-0.1028 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7608 | ema=0.9741 | best_ema=0.9741 | no_improve=0
[CYCLE] Update 136/348 | Step 137,088/500,000 | Episode 176 | Time: 18612.8s
   📊 Metrics: Return=+29.02% | Sharpe=0.673 | DD=19.53% | Turnover=25.37%
   🎚️ Intra-Step TAPE: potential=0.2448 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0712 | critic_loss=0.3861 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1930 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0262
   🧠 Objective Experts: aux_loss=-0.1147 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6735 | ema=0.9441 | best_ema=0.9441 | no_improve=0
   🔬 Alpha Diversity: mean=2.57 | std=1.74 | range=[1.20, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.14 | NVDA=2.89 | XOM=2.74  BOT: AMZN=2.43 | CAT=2.08 | NEE=1.91
   🧬 FiLM: seq(dg=0.0121, db=0.0110, sat=0.0%) | latent(dg=0.0138, db=0.0073, sat=0.0%) | asset(dg=0.0031, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=63 (34.2%), low_vol=71 (38.6%), medium_vol=50 (27.2%)
[CYCLE] Update 137/348 | Step 138,096/500,000 | Episode 176 | Time: 18750.4s
   📊 Metrics: Return=+29.73% | Sharpe=0.568 | DD=19.53% | Turnover=25.58%
   🎚️ Intra-Step TAPE: potential=0.2462 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0835 | critic_loss=0.3496 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1748 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0261
   🧠 Objective Experts: aux_loss=-0.1268 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5684 | ema=0.9065 | best_ema=0.9065 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00178_shp1p675_actor.weights.h5 (Sharpe=1.675, MDD=9.88%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00181_shp1p806_actor.weights.h5 (Sharpe=1.806, MDD=10.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00184_shp1p723_actor.weights.h5 (Sharpe=1.723, MDD=12.19%)
[CYCLE] Update 138/348 | Step 139,104/500,000 | Episode 184 | Time: 18883.2s
   📊 Metrics: Return=+103.01% | Sharpe=1.723 | DD=12.19% | Turnover=25.88%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1567 | critic_loss=0.5026 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2513 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0260
   🧠 Objective Experts: aux_loss=-0.2000 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7232 | ema=0.9882 | best_ema=0.9882 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=1.90 | range=[1.19, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=3.56 | NVDA=2.89 | MSFT=2.75  BOT: KO=2.06 | BRK-B=2.00 | NEE=1.60
   🧬 FiLM: seq(dg=0.0114, db=0.0106, sat=0.0%) | latent(dg=0.0117, db=0.0064, sat=0.0%) | asset(dg=0.0030, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=65 (33.9%), low_vol=75 (39.1%), medium_vol=52 (27.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6482
[CYCLE] Update 139/348 | Step 140,112/500,000 | Episode 184 | Time: 19021.0s
   📊 Metrics: Return=+4.94% | Sharpe=1.028 | DD=5.61% | Turnover=25.88%
   🎚️ Intra-Step TAPE: potential=0.2494 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1576 | critic_loss=0.6135 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3068 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0262
   🧠 Objective Experts: aux_loss=-0.2014 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0278 | ema=0.9921 | best_ema=0.9921 | no_improve=0
[CYCLE] Update 140/348 | Step 141,120/500,000 | Episode 184 | Time: 19159.1s
   📊 Metrics: Return=+7.48% | Sharpe=0.513 | DD=8.07% | Turnover=26.29%
   🎚️ Intra-Step TAPE: potential=0.2891 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0860 | critic_loss=0.4450 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2225 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.1295 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5130 | ema=0.9442 | best_ema=0.9442 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=1.97 | range=[1.19, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.37 | AMZN=3.33 | XOM=3.01  BOT: NEE=2.29 | GLD=2.11 | CAT=1.98
   🧬 FiLM: seq(dg=0.0167, db=0.0141, sat=0.0%) | latent(dg=0.0170, db=0.0087, sat=0.0%) | asset(dg=0.0038, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=65 (33.9%), low_vol=75 (39.1%), medium_vol=52 (27.1%)
[CYCLE] Update 141/348 | Step 142,128/500,000 | Episode 184 | Time: 19297.1s
   📊 Metrics: Return=+17.28% | Sharpe=0.728 | DD=9.25% | Turnover=26.30%
   🎚️ Intra-Step TAPE: potential=0.6550 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1220 | critic_loss=0.5377 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2688 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.1651 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7284 | ema=0.9226 | best_ema=0.9226 | no_improve=0
[CYCLE] Update 142/348 | Step 143,136/500,000 | Episode 184 | Time: 19435.1s
   📊 Metrics: Return=+26.57% | Sharpe=0.792 | DD=9.25% | Turnover=26.16%
   🎚️ Intra-Step TAPE: potential=0.7561 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0388 | critic_loss=0.4272 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2136 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.0813 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7920 | ema=0.9096 | best_ema=0.9096 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=2.14 | range=[1.19, 10.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.28 | GLD=2.67 | NEE=2.67  BOT: JPM=2.03 | NVDA=2.00 | CAT=1.57
   🧬 FiLM: seq(dg=0.0150, db=0.0130, sat=0.0%) | latent(dg=0.0166, db=0.0085, sat=0.0%) | asset(dg=0.0034, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=65 (33.9%), low_vol=75 (39.1%), medium_vol=52 (27.1%)
[CYCLE] Update 143/348 | Step 144,144/500,000 | Episode 184 | Time: 19572.8s
   📊 Metrics: Return=+53.43% | Sharpe=1.139 | DD=9.25% | Turnover=25.79%
   🎚️ Intra-Step TAPE: potential=0.7199 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1145 | critic_loss=0.4720 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2360 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0260
   🧠 Objective Experts: aux_loss=-0.1578 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1390 | ema=0.9325 | best_ema=0.9325 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00185_shp1p304_actor.weights.h5 (Sharpe=1.304, MDD=9.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00187_shp0p800_actor.weights.h5 (Sharpe=0.800, MDD=11.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00188_shp1p916_actor.weights.h5 (Sharpe=1.916, MDD=9.94%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00190_shp1p472_actor.weights.h5 (Sharpe=1.472, MDD=9.08%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00191_shp1p569_actor.weights.h5 (Sharpe=1.569, MDD=10.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00192_shp0p738_actor.weights.h5 (Sharpe=0.738, MDD=12.34%)
[CYCLE] Update 144/348 | Step 145,152/500,000 | Episode 192 | Time: 19706.0s
   📊 Metrics: Return=+37.29% | Sharpe=0.738 | DD=12.34% | Turnover=25.78%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0136 | critic_loss=0.7863 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3931 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.0296 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7379 | ema=0.9131 | best_ema=0.9131 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.11 | range=[1.19, 10.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.98 | NVDA=3.86 | JPM=2.92  BOT: MSFT=1.90 | BRK-B=1.89 | CAT=1.79
   🧬 FiLM: seq(dg=0.0134, db=0.0115, sat=0.0%) | latent(dg=0.0154, db=0.0080, sat=0.0%) | asset(dg=0.0039, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=68 (34.0%), low_vol=80 (40.0%), medium_vol=52 (26.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4037
[CYCLE] Update 145/348 | Step 146,160/500,000 | Episode 192 | Time: 19843.2s
   📊 Metrics: Return=+11.72% | Sharpe=1.107 | DD=12.59% | Turnover=24.43%
   🎚️ Intra-Step TAPE: potential=0.2406 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0547 | critic_loss=0.6813 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3406 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0260
   🧠 Objective Experts: aux_loss=-0.0985 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1066 | ema=0.9324 | best_ema=0.9324 | no_improve=0
[CYCLE] Update 146/348 | Step 147,168/500,000 | Episode 192 | Time: 19981.0s
   📊 Metrics: Return=+34.11% | Sharpe=1.726 | DD=12.59% | Turnover=24.88%
   🎚️ Intra-Step TAPE: potential=0.7222 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1010 | critic_loss=0.3015 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1508 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.1426 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7264 | ema=1.0118 | best_ema=1.0118 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.14 | range=[1.19, 10.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.60 | NVDA=3.52 | JPM=3.17  BOT: KO=2.03 | NEE=1.76 | CAT=1.71
   🧬 FiLM: seq(dg=0.0130, db=0.0107, sat=0.0%) | latent(dg=0.0160, db=0.0082, sat=0.0%) | asset(dg=0.0034, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=68 (34.0%), low_vol=80 (40.0%), medium_vol=52 (26.0%)
[CYCLE] Update 147/348 | Step 148,176/500,000 | Episode 192 | Time: 20118.5s
   📊 Metrics: Return=+55.85% | Sharpe=1.806 | DD=12.59% | Turnover=24.73%
   🎚️ Intra-Step TAPE: potential=0.7312 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0436 | critic_loss=0.3062 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1531 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.0846 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8064 | ema=1.0913 | best_ema=1.0913 | no_improve=0
[CYCLE] Update 148/348 | Step 149,184/500,000 | Episode 192 | Time: 20256.8s
   📊 Metrics: Return=+69.65% | Sharpe=1.775 | DD=12.59% | Turnover=25.33%
   🎚️ Intra-Step TAPE: potential=0.6234 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0874 | critic_loss=0.4291 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2145 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.1299 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7749 | ema=1.1596 | best_ema=1.1596 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=1.78 | range=[1.19, 10.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.43 | JPM=2.93 | BRK-B=2.85  BOT: NVDA=2.15 | NEE=2.00 | CAT=1.78
   🧬 FiLM: seq(dg=0.0136, db=0.0113, sat=0.0%) | latent(dg=0.0166, db=0.0086, sat=0.0%) | asset(dg=0.0032, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=68 (34.0%), low_vol=80 (40.0%), medium_vol=52 (26.0%)
   [TOOL] Actor learning rate adjusted to 0.000020 at step 150,000
   [TOOL] Critic learning rate adjusted to 0.000120 at step 150,000

🎛️ EXECUTION BETA UPDATE at 150,192 steps:
   action_execution_beta: 0.650 (w_exec=(1-β)w_prev + βw_raw)
[CYCLE] Update 149/348 | Step 150,192/500,000 | Episode 192 | Time: 20394.5s
   📊 Metrics: Return=+96.23% | Sharpe=1.861 | DD=12.59% | Turnover=25.79%
   🎚️ Intra-Step TAPE: potential=0.6358 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1142 | critic_loss=0.3375 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1688 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.1563 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8608 | ema=1.2297 | best_ema=1.2297 | no_improve=0

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
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00193_shp1p553_actor.weights.h5 (Sharpe=1.553, MDD=12.59%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00194_shp1p094_actor.weights.h5 (Sharpe=1.094, MDD=9.98%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00196_shp1p121_actor.weights.h5 (Sharpe=1.121, MDD=17.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00197_shp1p487_actor.weights.h5 (Sharpe=1.487, MDD=11.30%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00198_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=16.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00199_shp1p041_actor.weights.h5 (Sharpe=1.041, MDD=11.11%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00200_shp1p278_actor.weights.h5 (Sharpe=1.278, MDD=11.28%)
[CYCLE] Update 150/348 | Step 151,704/500,000 | Episode 200 | Time: 20592.7s
   📊 Metrics: Return=+74.29% | Sharpe=1.278 | DD=11.28% | Turnover=27.38%
   🎚️ Intra-Step TAPE: potential=0.5262 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1800 | critic_loss=1.5868 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7934 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.2181 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2779 | ema=1.2346 | best_ema=1.2346 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=1.70 | range=[1.19, 10.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.84 | AMZN=2.88 | BRK-B=2.84  BOT: CAT=2.16 | GLD=2.12 | NEE=1.98
   🧬 FiLM: seq(dg=0.0124, db=0.0109, sat=0.0%) | latent(dg=0.0148, db=0.0079, sat=0.0%) | asset(dg=0.0033, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (34.1%), low_vol=85 (40.9%), medium_vol=52 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.77% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5869
[CYCLE] Update 151/348 | Step 153,216/500,000 | Episode 200 | Time: 20779.6s
   📊 Metrics: Return=+8.82% | Sharpe=0.586 | DD=7.13% | Turnover=33.04%
   🎚️ Intra-Step TAPE: potential=0.6456 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1670 | critic_loss=0.4328 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2164 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.2039 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5855 | ema=1.1697 | best_ema=1.1697 | no_improve=0
[CYCLE] Update 152/348 | Step 154,728/500,000 | Episode 200 | Time: 20966.6s
   📊 Metrics: Return=+13.41% | Sharpe=0.425 | DD=12.13% | Turnover=32.86%
   🎚️ Intra-Step TAPE: potential=0.2487 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1143 | critic_loss=0.3859 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1930 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.1523 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4252 | ema=1.0952 | best_ema=1.0952 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.05 | range=[1.19, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.38 | JPM=2.92 | BRK-B=2.51  BOT: GLD=1.93 | KO=1.89 | CAT=1.69
   🧬 FiLM: seq(dg=0.0151, db=0.0126, sat=0.0%) | latent(dg=0.0182, db=0.0094, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (34.1%), low_vol=85 (40.9%), medium_vol=52 (25.0%)
[CYCLE] Update 153/348 | Step 156,240/500,000 | Episode 200 | Time: 21153.1s
   📊 Metrics: Return=+46.05% | Sharpe=0.977 | DD=12.13% | Turnover=32.58%
   🎚️ Intra-Step TAPE: potential=0.7530 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1728 | critic_loss=0.9304 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4652 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.2105 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9774 | ema=1.0834 | best_ema=1.0834 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00201_shp1p101_actor.weights.h5 (Sharpe=1.101, MDD=12.13%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00202_shp1p347_actor.weights.h5 (Sharpe=1.347, MDD=10.80%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00203_shp1p249_actor.weights.h5 (Sharpe=1.249, MDD=10.08%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00204_shp0p887_actor.weights.h5 (Sharpe=0.887, MDD=12.77%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00207_shp1p338_actor.weights.h5 (Sharpe=1.338, MDD=18.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00208_shp1p051_actor.weights.h5 (Sharpe=1.051, MDD=12.01%)
[CYCLE] Update 154/348 | Step 157,752/500,000 | Episode 208 | Time: 21342.4s
   📊 Metrics: Return=+57.78% | Sharpe=1.051 | DD=12.01% | Turnover=32.34%
   🎚️ Intra-Step TAPE: potential=0.2451 | delta_reward=-0.0027
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1551 | critic_loss=0.9680 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4840 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.1930 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0512 | ema=1.0802 | best_ema=1.0802 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=1.65 | range=[1.19, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.18 | AMZN=3.02 | GLD=2.69  BOT: XOM=2.32 | CAT=2.20 | NEE=2.18
   🧬 FiLM: seq(dg=0.0108, db=0.0097, sat=0.0%) | latent(dg=0.0140, db=0.0075, sat=0.0%) | asset(dg=0.0034, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=72 (33.3%), low_vol=88 (40.7%), medium_vol=56 (25.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.55% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5436
[CYCLE] Update 155/348 | Step 159,264/500,000 | Episode 208 | Time: 21528.9s
   📊 Metrics: Return=+2.66% | Sharpe=0.114 | DD=7.89% | Turnover=32.26%
   🎚️ Intra-Step TAPE: potential=0.2490 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0503 | critic_loss=0.5443 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2721 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0881 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1139 | ema=0.9836 | best_ema=0.9836 | no_improve=0
[CYCLE] Update 156/348 | Step 160,776/500,000 | Episode 208 | Time: 21715.5s
   📊 Metrics: Return=+13.64% | Sharpe=0.474 | DD=9.16% | Turnover=32.48%
   🎚️ Intra-Step TAPE: potential=0.2847 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0594 | critic_loss=0.4355 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2178 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.0962 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4737 | ema=0.9326 | best_ema=0.9326 | no_improve=0
   🔬 Alpha Diversity: mean=2.42 | std=2.04 | range=[1.19, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.25 | MSFT=2.60 | XOM=2.46  BOT: KO=2.15 | NEE=1.96 | CAT=1.83
   🧬 FiLM: seq(dg=0.0127, db=0.0114, sat=0.0%) | latent(dg=0.0144, db=0.0079, sat=0.0%) | asset(dg=0.0033, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=72 (33.3%), low_vol=88 (40.7%), medium_vol=56 (25.9%)
[CYCLE] Update 157/348 | Step 162,288/500,000 | Episode 208 | Time: 21901.3s
   📊 Metrics: Return=+35.95% | Sharpe=0.813 | DD=10.82% | Turnover=32.07%
   🎚️ Intra-Step TAPE: potential=0.6479 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0614 | critic_loss=0.5582 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2791 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.0994 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8126 | ema=0.9206 | best_ema=0.9206 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00209_shp0p956_actor.weights.h5 (Sharpe=0.956, MDD=10.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00211_shp0p850_actor.weights.h5 (Sharpe=0.850, MDD=10.08%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00213_shp0p884_actor.weights.h5 (Sharpe=0.884, MDD=10.35%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00214_shp0p805_actor.weights.h5 (Sharpe=0.805, MDD=19.87%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00215_shp1p599_actor.weights.h5 (Sharpe=1.599, MDD=9.85%)
[CYCLE] Update 158/348 | Step 163,800/500,000 | Episode 216 | Time: 22090.0s
   📊 Metrics: Return=+26.51% | Sharpe=0.579 | DD=7.88% | Turnover=32.23%
   🎚️ Intra-Step TAPE: potential=0.2486 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0107 | critic_loss=1.6140 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8070 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0484 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5787 | ema=0.8864 | best_ema=0.8864 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.42 | range=[1.19, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.20 | AMZN=2.50 | MSFT=2.04  BOT: BRK-B=1.81 | KO=1.75 | CAT=1.59
   🧬 FiLM: seq(dg=0.0101, db=0.0092, sat=0.0%) | latent(dg=0.0123, db=0.0067, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=72 (32.1%), low_vol=90 (40.2%), medium_vol=62 (27.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.54% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3364
[CYCLE] Update 159/348 | Step 165,312/500,000 | Episode 216 | Time: 22276.4s
   📊 Metrics: Return=+2.85% | Sharpe=0.142 | DD=5.68% | Turnover=31.00%
   🎚️ Intra-Step TAPE: potential=0.2465 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1550 | critic_loss=0.6902 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3451 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.1929 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1423 | ema=0.8120 | best_ema=0.8120 | no_improve=0
[CYCLE] Update 160/348 | Step 166,824/500,000 | Episode 216 | Time: 22462.9s
   📊 Metrics: Return=+12.29% | Sharpe=0.509 | DD=5.68% | Turnover=31.81%
   🎚️ Intra-Step TAPE: potential=0.2461 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1565 | critic_loss=0.5243 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2622 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.1942 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5090 | ema=0.7817 | best_ema=0.7817 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=2.27 | range=[1.18, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.41 | NVDA=2.54 | JPM=2.47  BOT: XOM=1.95 | CAT=1.74 | MSFT=1.73
   🧬 FiLM: seq(dg=0.0064, db=0.0077, sat=0.0%) | latent(dg=0.0083, db=0.0049, sat=0.0%) | asset(dg=0.0037, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=72 (32.1%), low_vol=90 (40.2%), medium_vol=62 (27.7%)
[CYCLE] Update 161/348 | Step 168,336/500,000 | Episode 216 | Time: 22648.9s
   📊 Metrics: Return=+29.06% | Sharpe=0.704 | DD=11.20% | Turnover=31.71%
   🎚️ Intra-Step TAPE: potential=0.7483 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1921 | critic_loss=0.9044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4522 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=0.1545 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7041 | ema=0.7739 | best_ema=0.7739 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00217_shp0p806_actor.weights.h5 (Sharpe=0.806, MDD=11.20%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00218_shp0p996_actor.weights.h5 (Sharpe=0.996, MDD=8.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00220_shp1p150_actor.weights.h5 (Sharpe=1.150, MDD=9.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00223_shp0p808_actor.weights.h5 (Sharpe=0.808, MDD=10.46%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00224_shp1p325_actor.weights.h5 (Sharpe=1.325, MDD=9.13%)
[CYCLE] Update 162/348 | Step 169,848/500,000 | Episode 224 | Time: 22837.7s
   📊 Metrics: Return=+61.53% | Sharpe=1.325 | DD=9.13% | Turnover=33.10%
   🎚️ Intra-Step TAPE: potential=0.2415 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0463 | critic_loss=1.6010 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8005 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.0844 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3250 | ema=0.8290 | best_ema=0.8290 | no_improve=0
   🔬 Alpha Diversity: mean=2.42 | std=1.48 | range=[1.18, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.27 | XOM=2.96 | JPM=2.85  BOT: MSFT=2.23 | NEE=2.00 | KO=1.98
   🧬 FiLM: seq(dg=0.0065, db=0.0082, sat=0.0%) | latent(dg=0.0077, db=0.0049, sat=0.0%) | asset(dg=0.0034, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=75 (32.3%), low_vol=92 (39.7%), medium_vol=65 (28.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.63% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5691
[CYCLE] Update 163/348 | Step 171,360/500,000 | Episode 224 | Time: 23024.0s
   📊 Metrics: Return=+3.42% | Sharpe=0.173 | DD=8.76% | Turnover=31.38%
   🎚️ Intra-Step TAPE: potential=0.2471 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0942 | critic_loss=0.5717 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2858 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=0.0568 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1730 | ema=0.7634 | best_ema=0.7634 | no_improve=0
[CYCLE] Update 164/348 | Step 172,872/500,000 | Episode 224 | Time: 23210.5s
   📊 Metrics: Return=+17.34% | Sharpe=0.568 | DD=10.27% | Turnover=32.06%
   🎚️ Intra-Step TAPE: potential=0.7483 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0108 | critic_loss=0.6534 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3267 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.0272 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5679 | ema=0.7439 | best_ema=0.7439 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=1.73 | range=[1.18, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.48 | BRK-B=3.19 | JPM=3.06  BOT: KO=2.12 | MSFT=2.10 | CAT=1.98
   🧬 FiLM: seq(dg=0.0067, db=0.0081, sat=0.0%) | latent(dg=0.0082, db=0.0051, sat=0.0%) | asset(dg=0.0037, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=75 (32.3%), low_vol=92 (39.7%), medium_vol=65 (28.0%)
[CYCLE] Update 165/348 | Step 174,384/500,000 | Episode 224 | Time: 23396.8s
   📊 Metrics: Return=+52.40% | Sharpe=1.178 | DD=10.27% | Turnover=31.65%
   🎚️ Intra-Step TAPE: potential=0.7502 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1292 | critic_loss=0.5427 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2713 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1664 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.1777 | ema=0.7873 | best_ema=0.7873 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00225_shp1p198_actor.weights.h5 (Sharpe=1.198, MDD=10.27%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00227_shp0p759_actor.weights.h5 (Sharpe=0.759, MDD=8.63%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00228_shp0p739_actor.weights.h5 (Sharpe=0.739, MDD=16.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00229_shp1p090_actor.weights.h5 (Sharpe=1.090, MDD=10.20%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00230_shp0p992_actor.weights.h5 (Sharpe=0.992, MDD=16.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00232_shp0p727_actor.weights.h5 (Sharpe=0.727, MDD=16.32%)
[CYCLE] Update 166/348 | Step 175,896/500,000 | Episode 232 | Time: 23586.3s
   📊 Metrics: Return=+50.01% | Sharpe=0.727 | DD=16.32% | Turnover=30.85%
   🎚️ Intra-Step TAPE: potential=0.7302 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1109 | critic_loss=0.6104 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3052 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1487 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7273 | ema=0.7813 | best_ema=0.7813 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=2.28 | range=[1.18, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.71 | NVDA=2.83 | JPM=2.45  BOT: KO=1.86 | GLD=1.68 | CAT=1.66
   🧬 FiLM: seq(dg=0.0058, db=0.0073, sat=0.0%) | latent(dg=0.0075, db=0.0048, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=77 (32.1%), low_vol=95 (39.6%), medium_vol=68 (28.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3867
[CYCLE] Update 167/348 | Step 177,408/500,000 | Episode 232 | Time: 23773.0s
   📊 Metrics: Return=+12.16% | Sharpe=0.638 | DD=14.76% | Turnover=32.15%
   🎚️ Intra-Step TAPE: potential=0.4207 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0335 | critic_loss=0.5639 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2820 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.0701 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6378 | ema=0.7669 | best_ema=0.7669 | no_improve=0
[CYCLE] Update 168/348 | Step 178,920/500,000 | Episode 232 | Time: 23960.0s
   📊 Metrics: Return=+36.07% | Sharpe=1.075 | DD=14.76% | Turnover=31.05%
   🎚️ Intra-Step TAPE: potential=0.2335 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0766 | critic_loss=0.5934 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2967 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.1142 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0755 | ema=0.7978 | best_ema=0.7978 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=1.87 | range=[1.18, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=3.41 | AMZN=3.32 | BRK-B=3.11  BOT: CAT=2.23 | KO=2.12 | GLD=1.80
   🧬 FiLM: seq(dg=0.0068, db=0.0080, sat=0.0%) | latent(dg=0.0081, db=0.0049, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=77 (32.1%), low_vol=95 (39.6%), medium_vol=68 (28.3%)
[CYCLE] Update 169/348 | Step 180,432/500,000 | Episode 232 | Time: 24147.4s
   📊 Metrics: Return=+41.10% | Sharpe=0.732 | DD=17.10% | Turnover=30.84%
   🎚️ Intra-Step TAPE: potential=0.5327 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1665 | critic_loss=0.7764 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3882 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.2038 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7319 | ema=0.7912 | best_ema=0.7912 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00234_shp0p973_actor.weights.h5 (Sharpe=0.973, MDD=18.49%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00235_shp1p200_actor.weights.h5 (Sharpe=1.200, MDD=9.82%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00237_shp1p300_actor.weights.h5 (Sharpe=1.300, MDD=17.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00238_shp1p397_actor.weights.h5 (Sharpe=1.397, MDD=10.66%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00239_shp1p213_actor.weights.h5 (Sharpe=1.213, MDD=10.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00240_shp1p204_actor.weights.h5 (Sharpe=1.204, MDD=14.57%)
[CYCLE] Update 170/348 | Step 181,944/500,000 | Episode 240 | Time: 24339.1s
   📊 Metrics: Return=+66.46% | Sharpe=1.204 | DD=14.57% | Turnover=31.28%
   🎚️ Intra-Step TAPE: potential=0.7218 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1725 | critic_loss=0.9812 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4906 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.2102 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2043 | ema=0.8325 | best_ema=0.8325 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=2.21 | range=[1.18, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.57 | AMZN=2.90 | JPM=2.79  BOT: MSFT=1.97 | XOM=1.96 | KO=1.91
   🧬 FiLM: seq(dg=0.0061, db=0.0071, sat=0.0%) | latent(dg=0.0082, db=0.0051, sat=0.0%) | asset(dg=0.0037, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=81 (32.7%), low_vol=98 (39.5%), medium_vol=69 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.49% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5546
[CYCLE] Update 171/348 | Step 183,456/500,000 | Episode 240 | Time: 24528.2s
   📊 Metrics: Return=+33.09% | Sharpe=2.210 | DD=4.37% | Turnover=31.54%
   🎚️ Intra-Step TAPE: potential=0.2574 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0582 | critic_loss=0.7848 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3924 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0952 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.2103 | ema=0.9703 | best_ema=0.9703 | no_improve=0
[CYCLE] Update 172/348 | Step 184,968/500,000 | Episode 240 | Time: 24717.6s
   📊 Metrics: Return=+66.54% | Sharpe=2.612 | DD=4.37% | Turnover=31.33%
   🎚️ Intra-Step TAPE: potential=0.7485 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1389 | critic_loss=0.5204 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2602 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.1770 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.6117 | ema=1.1344 | best_ema=1.1344 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=1.92 | range=[1.18, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=3.59 | BRK-B=3.48 | XOM=2.99  BOT: GLD=1.92 | KO=1.91 | CAT=1.84
   🧬 FiLM: seq(dg=0.0070, db=0.0076, sat=0.0%) | latent(dg=0.0092, db=0.0052, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=81 (32.7%), low_vol=98 (39.5%), medium_vol=69 (27.8%)
[CYCLE] Update 173/348 | Step 186,480/500,000 | Episode 240 | Time: 24906.5s
   📊 Metrics: Return=+64.93% | Sharpe=1.540 | DD=9.05% | Turnover=31.65%
   🎚️ Intra-Step TAPE: potential=0.2236 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1972 | critic_loss=0.6591 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3296 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.2348 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.5405 | ema=1.1750 | best_ema=1.1750 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00241_shp1p324_actor.weights.h5 (Sharpe=1.324, MDD=17.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00242_shp0p938_actor.weights.h5 (Sharpe=0.938, MDD=14.20%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00243_shp1p350_actor.weights.h5 (Sharpe=1.350, MDD=9.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00244_shp1p569_actor.weights.h5 (Sharpe=1.569, MDD=9.36%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00246_shp1p060_actor.weights.h5 (Sharpe=1.060, MDD=14.92%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00248_shp1p508_actor.weights.h5 (Sharpe=1.508, MDD=11.43%)
[CYCLE] Update 174/348 | Step 187,992/500,000 | Episode 248 | Time: 25098.0s
   📊 Metrics: Return=+85.25% | Sharpe=1.508 | DD=11.43% | Turnover=32.52%
   🎚️ Intra-Step TAPE: potential=0.2297 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1809 | critic_loss=0.6498 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3249 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.2182 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.5079 | ema=1.2083 | best_ema=1.2083 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=2.09 | range=[1.18, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: BRK-B=3.28 | JPM=2.97 | MSFT=2.78  BOT: KO=2.16 | GLD=1.74 | CAT=1.60
   🧬 FiLM: seq(dg=0.0079, db=0.0083, sat=0.0%) | latent(dg=0.0098, db=0.0057, sat=0.0%) | asset(dg=0.0037, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=85 (33.2%), low_vol=101 (39.5%), medium_vol=70 (27.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.27% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6248
[CYCLE] Update 175/348 | Step 189,504/500,000 | Episode 248 | Time: 25287.2s
   📊 Metrics: Return=+2.44% | Sharpe=0.094 | DD=7.91% | Turnover=31.00%
   🎚️ Intra-Step TAPE: potential=0.2881 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0107 | critic_loss=0.3824 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1912 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.0475 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0944 | ema=1.0969 | best_ema=1.0969 | no_improve=0

📚 EPISODE HORIZON UPDATE at 191,016 steps:
   Episode horizon: 782 steps
[CYCLE] Update 176/348 | Step 191,016/500,000 | Episode 248 | Time: 25475.7s
   📊 Metrics: Return=+9.23% | Sharpe=0.295 | DD=11.02% | Turnover=31.59%
   🎚️ Intra-Step TAPE: potential=0.2319 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1748 | critic_loss=0.5328 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2664 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0232
   🧠 Objective Experts: aux_loss=-0.2105 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2955 | ema=1.0168 | best_ema=1.0168 | no_improve=0
   🔬 Alpha Diversity: mean=2.39 | std=2.28 | range=[1.17, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.45 | MSFT=3.65 | JPM=2.52  BOT: NEE=1.72 | CAT=1.72 | KO=1.70
   🧬 FiLM: seq(dg=0.0070, db=0.0078, sat=0.0%) | latent(dg=0.0093, db=0.0056, sat=0.0%) | asset(dg=0.0034, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=85 (33.2%), low_vol=101 (39.5%), medium_vol=70 (27.3%)

📚 EPISODE HORIZON UPDATE at 192,528 steps:
   Episode horizon: 820 steps
[CYCLE] Update 177/348 | Step 192,528/500,000 | Episode 248 | Time: 25664.2s
   📊 Metrics: Return=+28.78% | Sharpe=0.648 | DD=11.57% | Turnover=31.60%
   🎚️ Intra-Step TAPE: potential=0.5965 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0208 | critic_loss=0.3183 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1591 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.0155 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6478 | ema=0.9799 | best_ema=0.9799 | no_improve=0

📚 EPISODE HORIZON UPDATE at 194,040 steps:
   Episode horizon: 858 steps
[CYCLE] Update 178/348 | Step 194,040/500,000 | Episode 248 | Time: 25852.7s
   📊 Metrics: Return=+52.30% | Sharpe=0.863 | DD=11.57% | Turnover=31.59%
   🎚️ Intra-Step TAPE: potential=0.4840 | delta_reward=+0.0025
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0936 | critic_loss=0.4038 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2019 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=0.0572 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8633 | ema=0.9682 | best_ema=0.9682 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.25 | range=[1.17, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.66 | NVDA=4.09 | MSFT=2.49  BOT: KO=1.87 | BRK-B=1.81 | CAT=1.46
   🧬 FiLM: seq(dg=0.0059, db=0.0076, sat=0.0%) | latent(dg=0.0075, db=0.0047, sat=0.0%) | asset(dg=0.0034, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=85 (33.2%), low_vol=101 (39.5%), medium_vol=70 (27.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00249_shp0p978_actor.weights.h5 (Sharpe=0.978, MDD=11.57%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00252_shp0p960_actor.weights.h5 (Sharpe=0.960, MDD=12.93%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00253_shp0p702_actor.weights.h5 (Sharpe=0.702, MDD=12.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00255_shp1p092_actor.weights.h5 (Sharpe=1.092, MDD=11.35%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00256_shp1p304_actor.weights.h5 (Sharpe=1.304, MDD=12.01%)

📚 EPISODE HORIZON UPDATE at 195,552 steps:
   Episode horizon: 896 steps
[CYCLE] Update 179/348 | Step 195,552/500,000 | Episode 256 | Time: 26043.8s
   📊 Metrics: Return=+94.22% | Sharpe=1.304 | DD=12.01% | Turnover=31.95%
   🎚️ Intra-Step TAPE: potential=0.2672 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0664 | critic_loss=0.9966 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4983 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.1039 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3043 | ema=1.0018 | best_ema=1.0018 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 8.09% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5811

📚 EPISODE HORIZON UPDATE at 197,064 steps:
   Episode horizon: 934 steps
[CYCLE] Update 180/348 | Step 197,064/500,000 | Episode 256 | Time: 26232.7s
   📊 Metrics: Return=+4.63% | Sharpe=0.167 | DD=11.98% | Turnover=33.14%
   🎚️ Intra-Step TAPE: potential=0.7150 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1803 | critic_loss=0.6994 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3497 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.2175 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1669 | ema=0.9183 | best_ema=0.9183 | no_improve=0
   🔬 Alpha Diversity: mean=2.43 | std=2.40 | range=[1.18, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.46 | JPM=3.05 | BRK-B=2.13  BOT: CAT=1.58 | KO=1.47 | XOM=1.44
   🧬 FiLM: seq(dg=0.0053, db=0.0071, sat=0.0%) | latent(dg=0.0069, db=0.0045, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=87 (33.0%), low_vol=103 (39.0%), medium_vol=74 (28.0%)

📚 EPISODE HORIZON UPDATE at 198,576 steps:
   Episode horizon: 972 steps
[CYCLE] Update 181/348 | Step 198,576/500,000 | Episode 256 | Time: 26419.4s
   📊 Metrics: Return=+6.28% | Sharpe=0.138 | DD=11.98% | Turnover=32.97%
   🎚️ Intra-Step TAPE: potential=0.2499 | delta_reward=-0.0031
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1005 | critic_loss=0.6817 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3408 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.1372 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1383 | ema=0.8403 | best_ema=0.8403 | no_improve=0

📚 TURNOVER CURRICULUM UPDATE at 200,088 steps:
   Turnover penalty scalar: 0.05

🧭 REWARD PHASE UPDATE at 200,088 steps:
   B_ramp_1 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.25/t0.00/bm0.20/tt0.00
   objective_expert_mask=[1.0, 1.0, 0.0]

📚 EPISODE HORIZON UPDATE at 200,088 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 182/348 | Step 200,088/500,000 | Episode 256 | Time: 26606.6s
   📊 Metrics: Return=+18.68% | Sharpe=0.341 | DD=11.98% | Turnover=32.71%
   🎚️ Intra-Step TAPE: potential=0.2991 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0430 | critic_loss=0.3062 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1531 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0925 | router_entropy=-0.0006 | diversity_loss=0.0132 | mask=[1, 1, 0] | router=return=0.974 | risk=0.026 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3414 | ema=0.7904 | best_ema=0.7904 | no_improve=0
   🔬 Alpha Diversity: mean=2.38 | std=1.97 | range=[1.17, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.02 | NVDA=4.00 | MSFT=3.12  BOT: CAT=1.80 | KO=1.79 | XOM=1.72
   🧬 FiLM: seq(dg=0.0049, db=0.0065, sat=0.0%) | latent(dg=0.0070, db=0.0047, sat=0.0%) | asset(dg=0.0034, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=87 (33.0%), low_vol=103 (39.0%), medium_vol=74 (28.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00257_shp0p859_actor.weights.h5 (Sharpe=0.859, MDD=23.55%)
[CYCLE] Update 183/348 | Step 201,600/500,000 | Episode 257 | Time: 26794.8s
   📊 Metrics: Return=+63.10% | Sharpe=0.859 | DD=23.55% | Turnover=32.95%
   🎚️ Intra-Step TAPE: potential=0.2406 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0056 | critic_loss=2.5220 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.2610 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.0427 | router_entropy=-0.0022 | diversity_loss=0.0130 | mask=[1, 1, 0] | router=return=0.783 | risk=0.217 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8594 | ema=0.7973 | best_ema=0.7973 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.32% / trig 16.50%) | terminal=0.000 (peak 0.049) | TAPE=0.4348
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=0.00352) | SPY shaping=0.000 (SPY ret=0.00243)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00258_shp1p039_actor.weights.h5 (Sharpe=1.039, MDD=23.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00260_shp0p818_actor.weights.h5 (Sharpe=0.818, MDD=9.93%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00263_shp1p236_actor.weights.h5 (Sharpe=1.236, MDD=12.21%)
[CYCLE] Update 184/348 | Step 203,112/500,000 | Episode 264 | Time: 26983.9s
   📊 Metrics: Return=+44.64% | Sharpe=0.655 | DD=11.62% | Turnover=32.83%
   🎚️ Intra-Step TAPE: potential=0.7349 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0093 | critic_loss=1.2508 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6254 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.0578 | router_entropy=-0.0030 | diversity_loss=0.0134 | mask=[1, 1, 0] | router=return=0.674 | risk=0.326 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6552 | ema=0.7831 | best_ema=0.7831 | no_improve=0
   🔬 Alpha Diversity: mean=2.41 | std=1.59 | range=[1.17, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.17 | AMZN=2.87 | BRK-B=2.87  BOT: XOM=2.22 | CAT=2.13 | GLD=1.96
   🧬 FiLM: seq(dg=0.0054, db=0.0071, sat=0.0%) | latent(dg=0.0072, db=0.0048, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=90 (33.1%), low_vol=106 (39.0%), medium_vol=76 (27.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.15% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3609
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=0.00269) | SPY shaping=-0.000 (SPY ret=0.00224)
[CYCLE] Update 185/348 | Step 204,624/500,000 | Episode 264 | Time: 27171.2s
   📊 Metrics: Return=+11.46% | Sharpe=0.534 | DD=17.47% | Turnover=32.64%
   🎚️ Intra-Step TAPE: potential=0.7195 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0266 | critic_loss=1.4110 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7055 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.0735 | router_entropy=-0.0028 | diversity_loss=0.0128 | mask=[1, 1, 0] | router=return=0.721 | risk=0.279 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5338 | ema=0.7582 | best_ema=0.7582 | no_improve=0
[CYCLE] Update 186/348 | Step 206,136/500,000 | Episode 264 | Time: 27359.1s
   📊 Metrics: Return=+24.14% | Sharpe=0.688 | DD=17.47% | Turnover=31.11%
   🎚️ Intra-Step TAPE: potential=0.2349 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1747 | critic_loss=1.2720 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6360 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.2216 | router_entropy=-0.0027 | diversity_loss=0.0124 | mask=[1, 1, 0] | router=return=0.746 | risk=0.254 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6876 | ema=0.7511 | best_ema=0.7511 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.04 | range=[1.17, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.13 | JPM=2.99 | XOM=2.49  BOT: GLD=2.13 | MSFT=1.97 | CAT=1.62
   🧬 FiLM: seq(dg=0.0054, db=0.0070, sat=0.0%) | latent(dg=0.0071, db=0.0048, sat=0.0%) | asset(dg=0.0040, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=90 (33.1%), low_vol=106 (39.0%), medium_vol=76 (27.9%)
[CYCLE] Update 187/348 | Step 207,648/500,000 | Episode 264 | Time: 27547.2s
   📊 Metrics: Return=+25.60% | Sharpe=0.472 | DD=17.47% | Turnover=31.65%
   🎚️ Intra-Step TAPE: potential=0.5527 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1496 | critic_loss=0.8916 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4458 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.1966 | router_entropy=-0.0029 | diversity_loss=0.0125 | mask=[1, 1, 0] | router=return=0.717 | risk=0.283 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4715 | ema=0.7232 | best_ema=0.7232 | no_improve=0
[CYCLE] Update 188/348 | Step 209,160/500,000 | Episode 264 | Time: 27737.1s
   📊 Metrics: Return=+35.91% | Sharpe=0.516 | DD=17.47% | Turnover=31.99%
   🎚️ Intra-Step TAPE: potential=0.2431 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0705 | critic_loss=0.8345 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4172 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1164 | router_entropy=-0.0031 | diversity_loss=0.0117 | mask=[1, 1, 0] | router=return=0.668 | risk=0.332 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5158 | ema=0.7024 | best_ema=0.7024 | no_improve=0
   🔬 Alpha Diversity: mean=2.48 | std=2.08 | range=[1.17, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.04 | AMZN=2.92 | JPM=2.73  BOT: BRK-B=2.23 | XOM=1.96 | CAT=1.47
   🧬 FiLM: seq(dg=0.0045, db=0.0057, sat=0.0%) | latent(dg=0.0070, db=0.0044, sat=0.0%) | asset(dg=0.0040, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=90 (33.1%), low_vol=106 (39.0%), medium_vol=76 (27.9%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00265_shp1p178_actor.weights.h5 (Sharpe=1.178, MDD=11.40%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00266_shp0p973_actor.weights.h5 (Sharpe=0.973, MDD=11.87%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00270_shp1p014_actor.weights.h5 (Sharpe=1.014, MDD=11.78%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00272_shp0p947_actor.weights.h5 (Sharpe=0.947, MDD=11.60%)
[CYCLE] Update 189/348 | Step 210,672/500,000 | Episode 272 | Time: 27928.7s
   📊 Metrics: Return=+66.63% | Sharpe=0.947 | DD=11.60% | Turnover=32.81%
   🎚️ Intra-Step TAPE: potential=0.7540 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0494 | critic_loss=1.1521 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5760 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=0.0034 | router_entropy=-0.0031 | diversity_loss=0.0117 | mask=[1, 1, 0] | router=return=0.678 | risk=0.322 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9471 | ema=0.7269 | best_ema=0.7269 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.46% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5158
   📈 Benchmark Relative: 1/N shaping=0.000 (EW ret=-0.00065) | SPY shaping=-0.000 (SPY ret=-0.00032)
[CYCLE] Update 190/348 | Step 212,184/500,000 | Episode 272 | Time: 28118.6s
   📊 Metrics: Return=+9.11% | Sharpe=0.693 | DD=8.23% | Turnover=31.78%
   🎚️ Intra-Step TAPE: potential=0.6566 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0567 | critic_loss=1.1121 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5561 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.1042 | router_entropy=-0.0030 | diversity_loss=0.0117 | mask=[1, 1, 0] | router=return=0.706 | risk=0.294 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6929 | ema=0.7235 | best_ema=0.7235 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=1.99 | range=[1.17, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: BRK-B=3.49 | AMZN=3.48 | NVDA=3.06  BOT: GLD=2.02 | CAT=1.92 | KO=1.88
   🧬 FiLM: seq(dg=0.0047, db=0.0060, sat=0.0%) | latent(dg=0.0074, db=0.0048, sat=0.0%) | asset(dg=0.0049, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=93 (33.2%), low_vol=110 (39.3%), medium_vol=77 (27.5%)
[CYCLE] Update 191/348 | Step 213,696/500,000 | Episode 272 | Time: 28308.5s
   📊 Metrics: Return=+22.30% | Sharpe=0.787 | DD=10.37% | Turnover=31.98%
   🎚️ Intra-Step TAPE: potential=0.2576 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1106 | critic_loss=0.7981 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3990 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.1577 | router_entropy=-0.0030 | diversity_loss=0.0119 | mask=[1, 1, 0] | router=return=0.709 | risk=0.291 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7865 | ema=0.7298 | best_ema=0.7298 | no_improve=0
[CYCLE] Update 192/348 | Step 215,208/500,000 | Episode 272 | Time: 28498.2s
   📊 Metrics: Return=+56.83% | Sharpe=1.241 | DD=10.37% | Turnover=31.61%
   🎚️ Intra-Step TAPE: potential=0.7293 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0382 | critic_loss=0.6438 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3219 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.0846 | router_entropy=-0.0030 | diversity_loss=0.0117 | mask=[1, 1, 0] | router=return=0.712 | risk=0.288 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2414 | ema=0.7810 | best_ema=0.7810 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=2.20 | range=[1.16, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.24 | NVDA=4.08 | JPM=3.28  BOT: KO=2.02 | CAT=1.68 | MSFT=1.67
   🧬 FiLM: seq(dg=0.0046, db=0.0058, sat=0.0%) | latent(dg=0.0076, db=0.0048, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=93 (33.2%), low_vol=110 (39.3%), medium_vol=77 (27.5%)
[CYCLE] Update 193/348 | Step 216,720/500,000 | Episode 272 | Time: 28686.4s
   📊 Metrics: Return=+74.41% | Sharpe=1.259 | DD=10.37% | Turnover=31.64%
   🎚️ Intra-Step TAPE: potential=0.2904 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0867 | critic_loss=0.4968 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2484 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=0.0412 | router_entropy=-0.0030 | diversity_loss=0.0114 | mask=[1, 1, 0] | router=return=0.699 | risk=0.301 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2591 | ema=0.8288 | best_ema=0.8288 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00273_shp1p242_actor.weights.h5 (Sharpe=1.242, MDD=10.07%)
[CYCLE] Update 194/348 | Step 218,232/500,000 | Episode 273 | Time: 28875.2s
   📊 Metrics: Return=+98.96% | Sharpe=1.242 | DD=10.07% | Turnover=31.29%
   🎚️ Intra-Step TAPE: potential=0.2221 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0018 | critic_loss=0.9394 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4697 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.0486 | router_entropy=-0.0030 | diversity_loss=0.0121 | mask=[1, 1, 0] | router=return=0.714 | risk=0.286 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2415 | ema=0.8700 | best_ema=0.8700 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=2.03 | range=[1.16, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.49 | GLD=3.28 | AMZN=2.97  BOT: XOM=1.74 | NEE=1.73 | KO=1.62
   🧬 FiLM: seq(dg=0.0051, db=0.0060, sat=0.0%) | latent(dg=0.0087, db=0.0054, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=94 (33.5%), low_vol=110 (39.1%), medium_vol=77 (27.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 5.45% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5804
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=0.00255) | SPY shaping=-0.000 (SPY ret=0.00333)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00275_shp1p172_actor.weights.h5 (Sharpe=1.172, MDD=10.37%)
[CYCLE] Update 195/348 | Step 219,744/500,000 | Episode 280 | Time: 29063.9s
   📊 Metrics: Return=+59.68% | Sharpe=0.681 | DD=17.31% | Turnover=30.96%
   🎚️ Intra-Step TAPE: potential=0.7430 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0598 | critic_loss=1.2424 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6212 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=0.0122 | router_entropy=-0.0029 | diversity_loss=0.0123 | mask=[1, 1, 0] | router=return=0.732 | risk=0.268 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6810 | ema=0.8511 | best_ema=0.8511 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.3671
   📈 Benchmark Relative: 1/N shaping=0.003 (EW ret=0.00367) | SPY shaping=0.001 (SPY ret=0.00305)
[CYCLE] Update 196/348 | Step 221,256/500,000 | Episode 280 | Time: 29253.7s
   📊 Metrics: Return=+7.85% | Sharpe=0.284 | DD=21.31% | Turnover=31.83%
   🎚️ Intra-Step TAPE: potential=0.2614 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0135 | critic_loss=0.9736 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4868 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0611 | router_entropy=-0.0028 | diversity_loss=0.0126 | mask=[1, 1, 0] | router=return=0.750 | risk=0.250 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2839 | ema=0.7944 | best_ema=0.7944 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=2.04 | range=[1.16, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.73 | GLD=2.90 | AMZN=2.67  BOT: KO=1.96 | XOM=1.94 | NEE=1.88
   🧬 FiLM: seq(dg=0.0050, db=0.0062, sat=0.0%) | latent(dg=0.0080, db=0.0051, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (33.7%), low_vol=111 (38.5%), medium_vol=80 (27.8%)
[CYCLE] Update 197/348 | Step 222,768/500,000 | Episode 280 | Time: 29441.9s
   📊 Metrics: Return=+14.76% | Sharpe=0.335 | DD=21.31% | Turnover=31.66%
   🎚️ Intra-Step TAPE: potential=0.2465 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0480 | critic_loss=0.7296 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3648 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=0.0001 | router_entropy=-0.0027 | diversity_loss=0.0129 | mask=[1, 1, 0] | router=return=0.765 | risk=0.235 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3350 | ema=0.7485 | best_ema=0.7485 | no_improve=0
[CYCLE] Update 198/348 | Step 224,280/500,000 | Episode 280 | Time: 29629.5s
   📊 Metrics: Return=+20.73% | Sharpe=0.351 | DD=21.31% | Turnover=31.83%
   🎚️ Intra-Step TAPE: potential=0.3266 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0162 | critic_loss=0.7672 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3836 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.0323 | router_entropy=-0.0026 | diversity_loss=0.0135 | mask=[1, 1, 0] | router=return=0.790 | risk=0.210 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3511 | ema=0.7087 | best_ema=0.7087 | no_improve=0
   🔬 Alpha Diversity: mean=2.42 | std=1.47 | range=[1.16, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.85 | GLD=2.94 | KO=2.57  BOT: XOM=2.19 | CAT=2.10 | JPM=2.04
   🧬 FiLM: seq(dg=0.0055, db=0.0067, sat=0.0%) | latent(dg=0.0079, db=0.0050, sat=0.0%) | asset(dg=0.0040, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (33.7%), low_vol=111 (38.5%), medium_vol=80 (27.8%)
[CYCLE] Update 199/348 | Step 225,792/500,000 | Episode 281 | Time: 29817.1s
   📊 Metrics: Return=+66.10% | Sharpe=0.682 | DD=20.84% | Turnover=31.56%
   🎚️ Intra-Step TAPE: potential=0.5320 | delta_reward=+0.0022
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0059 | critic_loss=0.7335 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3667 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0432 | router_entropy=-0.0023 | diversity_loss=0.0139 | mask=[1, 1, 0] | router=return=0.827 | risk=0.173 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6820 | ema=0.7061 | best_ema=0.7061 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.014, dd 1.16% / trig 16.50%) | terminal=0.000 (peak 0.008) | TAPE=0.3616
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.01135) | SPY shaping=0.001 (SPY ret=-0.01461)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00282_shp0p952_actor.weights.h5 (Sharpe=0.952, MDD=19.02%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00286_shp1p219_actor.weights.h5 (Sharpe=1.219, MDD=10.63%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00287_shp1p337_actor.weights.h5 (Sharpe=1.337, MDD=10.10%)
[CYCLE] Update 200/348 | Step 227,304/500,000 | Episode 288 | Time: 30005.9s
   📊 Metrics: Return=+44.23% | Sharpe=0.540 | DD=19.11% | Turnover=31.78%
   🎚️ Intra-Step TAPE: potential=0.7379 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0090 | critic_loss=1.5284 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7642 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.0405 | router_entropy=-0.0023 | diversity_loss=0.0136 | mask=[1, 1, 0] | router=return=0.820 | risk=0.180 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5398 | ema=0.6894 | best_ema=0.6894 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=2.05 | range=[1.16, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=2.92 | GLD=2.80 | NVDA=2.73  BOT: BRK-B=2.12 | JPM=1.84 | CAT=1.65
   🧬 FiLM: seq(dg=0.0070, db=0.0074, sat=0.0%) | latent(dg=0.0094, db=0.0056, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (34.1%), low_vol=112 (37.8%), medium_vol=83 (28.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.09% / trig 16.50%) | terminal=0.000 (peak 0.003) | TAPE=0.3151
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=-0.00425) | SPY shaping=-0.000 (SPY ret=-0.00430)
[CYCLE] Update 201/348 | Step 228,816/500,000 | Episode 288 | Time: 30193.4s
   📊 Metrics: Return=+7.86% | Sharpe=0.374 | DD=17.00% | Turnover=31.31%
   🎚️ Intra-Step TAPE: potential=0.2334 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0459 | critic_loss=1.0686 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5343 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0028 | router_entropy=-0.0025 | diversity_loss=0.0135 | mask=[1, 1, 0] | router=return=0.791 | risk=0.209 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3743 | ema=0.6579 | best_ema=0.6579 | no_improve=0
[CYCLE] Update 202/348 | Step 230,328/500,000 | Episode 288 | Time: 30381.0s
   📊 Metrics: Return=+46.62% | Sharpe=1.239 | DD=17.00% | Turnover=30.62%
   🎚️ Intra-Step TAPE: potential=0.7047 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0208 | critic_loss=0.6479 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3240 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.0696 | router_entropy=-0.0029 | diversity_loss=0.0138 | mask=[1, 1, 0] | router=return=0.738 | risk=0.262 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2394 | ema=0.7161 | best_ema=0.7161 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=1.62 | range=[1.16, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.50 | MSFT=2.93 | KO=2.76  BOT: XOM=2.37 | AMZN=2.01 | CAT=1.87
   🧬 FiLM: seq(dg=0.0054, db=0.0065, sat=0.0%) | latent(dg=0.0084, db=0.0054, sat=0.0%) | asset(dg=0.0042, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (34.1%), low_vol=112 (37.8%), medium_vol=83 (28.0%)
[CYCLE] Update 203/348 | Step 231,840/500,000 | Episode 288 | Time: 30567.9s
   📊 Metrics: Return=+35.21% | Sharpe=0.597 | DD=18.95% | Turnover=31.30%
   🎚️ Intra-Step TAPE: potential=0.5103 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0421 | critic_loss=0.6283 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3141 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0902 | router_entropy=-0.0027 | diversity_loss=0.0134 | mask=[1, 1, 0] | router=return=0.763 | risk=0.237 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5971 | ema=0.7042 | best_ema=0.7042 | no_improve=0
[CYCLE] Update 204/348 | Step 233,352/500,000 | Episode 288 | Time: 30754.9s
   📊 Metrics: Return=+44.83% | Sharpe=0.598 | DD=18.95% | Turnover=31.47%
   🎚️ Intra-Step TAPE: potential=0.5931 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0035 | critic_loss=0.6191 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.0441 | router_entropy=-0.0026 | diversity_loss=0.0130 | mask=[1, 1, 0] | router=return=0.783 | risk=0.217 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5979 | ema=0.6935 | best_ema=0.6935 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=2.03 | range=[1.16, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.15 | NVDA=3.42 | MSFT=3.18  BOT: XOM=1.89 | GLD=1.77 | CAT=1.71
   🧬 FiLM: seq(dg=0.0066, db=0.0072, sat=0.0%) | latent(dg=0.0096, db=0.0059, sat=0.0%) | asset(dg=0.0040, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (34.1%), low_vol=112 (37.8%), medium_vol=83 (28.0%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00293_shp1p012_actor.weights.h5 (Sharpe=1.012, MDD=14.78%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00294_shp0p891_actor.weights.h5 (Sharpe=0.891, MDD=21.20%)
[CYCLE] Update 205/348 | Step 234,864/500,000 | Episode 296 | Time: 30944.3s
   📊 Metrics: Return=+24.62% | Sharpe=0.316 | DD=15.60% | Turnover=31.69%
   🎚️ Intra-Step TAPE: potential=0.2338 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0145 | critic_loss=1.2080 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6040 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.0619 | router_entropy=-0.0027 | diversity_loss=0.0130 | mask=[1, 1, 0] | router=return=0.759 | risk=0.241 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3162 | ema=0.6558 | best_ema=0.6558 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.89% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2715
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.01032) | SPY shaping=0.003 (SPY ret=-0.01678)
[CYCLE] Update 206/348 | Step 236,376/500,000 | Episode 296 | Time: 31133.0s
   📊 Metrics: Return=+9.12% | Sharpe=0.861 | DD=5.76% | Turnover=31.46%
   🎚️ Intra-Step TAPE: potential=0.6046 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0043 | critic_loss=0.8748 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4374 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.0524 | router_entropy=-0.0029 | diversity_loss=0.0138 | mask=[1, 1, 0] | router=return=0.735 | risk=0.265 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8615 | ema=0.6764 | best_ema=0.6764 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=2.09 | range=[1.16, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.67 | BRK-B=3.48 | NVDA=3.47  BOT: NEE=1.79 | GLD=1.69 | CAT=1.60
   🧬 FiLM: seq(dg=0.0057, db=0.0071, sat=0.0%) | latent(dg=0.0084, db=0.0054, sat=0.0%) | asset(dg=0.0038, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (34.2%), low_vol=115 (37.8%), medium_vol=85 (28.0%)
[CYCLE] Update 207/348 | Step 237,888/500,000 | Episode 296 | Time: 31320.6s
   📊 Metrics: Return=+16.98% | Sharpe=0.750 | DD=7.13% | Turnover=32.21%
   🎚️ Intra-Step TAPE: potential=0.2446 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0078 | critic_loss=0.6029 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3014 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.0423 | router_entropy=-0.0030 | diversity_loss=0.0150 | mask=[1, 1, 0] | router=return=0.713 | risk=0.287 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7504 | ema=0.6838 | best_ema=0.6838 | no_improve=0
[CYCLE] Update 208/348 | Step 239,400/500,000 | Episode 296 | Time: 31508.7s
   📊 Metrics: Return=+29.70% | Sharpe=0.739 | DD=12.72% | Turnover=32.14%
   🎚️ Intra-Step TAPE: potential=0.7531 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0212 | critic_loss=0.8215 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4107 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0293 | router_entropy=-0.0029 | diversity_loss=0.0153 | mask=[1, 1, 0] | router=return=0.727 | risk=0.273 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7393 | ema=0.6893 | best_ema=0.6893 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=1.90 | range=[1.15, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.57 | NEE=3.01 | BRK-B=2.97  BOT: KO=2.20 | CAT=1.96 | GLD=1.83
   🧬 FiLM: seq(dg=0.0082, db=0.0083, sat=0.0%) | latent(dg=0.0110, db=0.0062, sat=0.0%) | asset(dg=0.0039, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (34.2%), low_vol=115 (37.8%), medium_vol=85 (28.0%)
[CYCLE] Update 209/348 | Step 240,912/500,000 | Episode 296 | Time: 31697.5s
   📊 Metrics: Return=+72.69% | Sharpe=1.205 | DD=12.72% | Turnover=31.91%
   🎚️ Intra-Step TAPE: potential=0.7445 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0013 | critic_loss=0.5491 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2745 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0504 | router_entropy=-0.0031 | diversity_loss=0.0151 | mask=[1, 1, 0] | router=return=0.691 | risk=0.309 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2048 | ema=0.7409 | best_ema=0.7409 | no_improve=0
[CYCLE] Update 210/348 | Step 242,424/500,000 | Episode 297 | Time: 31885.7s
   📊 Metrics: Return=+50.95% | Sharpe=0.574 | DD=19.73% | Turnover=31.43%
   🎚️ Intra-Step TAPE: potential=0.6504 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0215 | critic_loss=1.0274 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5137 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.0269 | router_entropy=-0.0031 | diversity_loss=0.0132 | mask=[1, 1, 0] | router=return=0.677 | risk=0.323 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5737 | ema=0.7242 | best_ema=0.7242 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=2.30 | range=[1.15, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.50 | AMZN=2.45 | JPM=1.85  BOT: BRK-B=1.63 | MSFT=1.57 | KO=1.48
   🧬 FiLM: seq(dg=0.0049, db=0.0063, sat=0.0%) | latent(dg=0.0079, db=0.0047, sat=0.0%) | asset(dg=0.0036, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (34.1%), low_vol=115 (37.7%), medium_vol=86 (28.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.13% / trig 16.50%) | terminal=0.000 (peak 0.007) | TAPE=0.3164
   📈 Benchmark Relative: 1/N shaping=0.006 (EW ret=0.00071) | SPY shaping=0.002 (SPY ret=0.00000)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00298_shp0p879_actor.weights.h5 (Sharpe=0.879, MDD=21.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00299_shp1p299_actor.weights.h5 (Sharpe=1.299, MDD=12.72%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00300_shp0p914_actor.weights.h5 (Sharpe=0.914, MDD=12.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00301_shp1p228_actor.weights.h5 (Sharpe=1.228, MDD=13.98%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00303_shp1p198_actor.weights.h5 (Sharpe=1.198, MDD=13.82%)
[CYCLE] Update 211/348 | Step 243,936/500,000 | Episode 304 | Time: 32075.9s
   📊 Metrics: Return=+13.13% | Sharpe=0.149 | DD=18.79% | Turnover=31.16%
   🎚️ Intra-Step TAPE: potential=0.2482 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0194 | critic_loss=1.3413 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6706 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0697 | router_entropy=-0.0030 | diversity_loss=0.0155 | mask=[1, 1, 0] | router=return=0.691 | risk=0.309 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1491 | ema=0.6666 | best_ema=0.6666 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.61% / trig 16.50%) | terminal=0.000 (peak 0.003) | TAPE=0.2435
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=0.00103) | SPY shaping=-0.000 (SPY ret=0.00254)
[CYCLE] Update 212/348 | Step 245,448/500,000 | Episode 304 | Time: 32264.3s
   📊 Metrics: Return=+21.36% | Sharpe=0.880 | DD=10.62% | Turnover=31.53%
   🎚️ Intra-Step TAPE: potential=0.7432 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0225 | critic_loss=0.6689 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3345 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.0271 | router_entropy=-0.0031 | diversity_loss=0.0149 | mask=[1, 1, 0] | router=return=0.686 | risk=0.314 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8798 | ema=0.6880 | best_ema=0.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.41 | std=1.79 | range=[1.15, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.74 | AMZN=3.60 | JPM=2.79  BOT: MSFT=2.25 | KO=1.77 | NEE=1.71
   🧬 FiLM: seq(dg=0.0056, db=0.0073, sat=0.0%) | latent(dg=0.0078, db=0.0049, sat=0.0%) | asset(dg=0.0036, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=106 (34.0%), low_vol=116 (37.2%), medium_vol=90 (28.8%)
[CYCLE] Update 213/348 | Step 246,960/500,000 | Episode 304 | Time: 32452.3s
   📊 Metrics: Return=+51.74% | Sharpe=1.340 | DD=10.62% | Turnover=31.74%
   🎚️ Intra-Step TAPE: potential=0.7506 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0009 | critic_loss=0.5818 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2909 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.0489 | router_entropy=-0.0031 | diversity_loss=0.0154 | mask=[1, 1, 0] | router=return=0.669 | risk=0.331 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3402 | ema=0.7532 | best_ema=0.7532 | no_improve=0
[CYCLE] Update 214/348 | Step 248,472/500,000 | Episode 304 | Time: 32640.0s
   📊 Metrics: Return=+85.61% | Sharpe=1.588 | DD=10.62% | Turnover=31.98%
   🎚️ Intra-Step TAPE: potential=0.7449 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0490 | critic_loss=0.6437 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3218 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=0.0005 | router_entropy=-0.0031 | diversity_loss=0.0142 | mask=[1, 1, 0] | router=return=0.669 | risk=0.331 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.5880 | ema=0.8367 | best_ema=0.8367 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=1.73 | range=[1.15, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.16 | JPM=2.94 | AMZN=2.70  BOT: XOM=2.29 | NEE=2.09 | KO=1.97
   🧬 FiLM: seq(dg=0.0046, db=0.0060, sat=0.0%) | latent(dg=0.0081, db=0.0046, sat=0.0%) | asset(dg=0.0038, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=106 (34.0%), low_vol=116 (37.2%), medium_vol=90 (28.8%)
[CYCLE] Update 215/348 | Step 249,984/500,000 | Episode 305 | Time: 32827.8s
   📊 Metrics: Return=+18.60% | Sharpe=0.218 | DD=20.75% | Turnover=30.94%
   🎚️ Intra-Step TAPE: potential=0.3338 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0157 | critic_loss=0.6263 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3132 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.0643 | router_entropy=-0.0031 | diversity_loss=0.0137 | mask=[1, 1, 0] | router=return=0.693 | risk=0.307 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2178 | ema=0.7748 | best_ema=0.7748 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.48% / trig 16.50%) | terminal=0.000 (peak 0.010) | TAPE=0.2484
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.01332) | SPY shaping=0.000 (SPY ret=-0.01330)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00307_shp0p879_actor.weights.h5 (Sharpe=0.879, MDD=17.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00308_shp0p978_actor.weights.h5 (Sharpe=0.978, MDD=23.31%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00309_shp1p263_actor.weights.h5 (Sharpe=1.263, MDD=10.89%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00310_shp1p068_actor.weights.h5 (Sharpe=1.068, MDD=20.41%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00311_shp0p910_actor.weights.h5 (Sharpe=0.910, MDD=11.91%)
[CYCLE] Update 216/348 | Step 251,496/500,000 | Episode 312 | Time: 33017.5s
   📊 Metrics: Return=+73.25% | Sharpe=0.656 | DD=21.47% | Turnover=31.74%
   🎚️ Intra-Step TAPE: potential=0.3554 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0125 | critic_loss=1.2404 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6202 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.0372 | router_entropy=-0.0030 | diversity_loss=0.0145 | mask=[1, 1, 0] | router=return=0.705 | risk=0.295 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6565 | ema=0.7629 | best_ema=0.7629 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=1.90 | range=[1.15, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.52 | AMZN=4.38 | CAT=2.63  BOT: XOM=1.87 | KO=1.82 | NEE=1.55
   🧬 FiLM: seq(dg=0.0055, db=0.0068, sat=0.0%) | latent(dg=0.0084, db=0.0049, sat=0.0%) | asset(dg=0.0037, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=108 (33.8%), low_vol=117 (36.6%), medium_vol=95 (29.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.001, dd 0.90% / trig 16.50%) | terminal=0.000 (peak 0.018) | TAPE=0.3592
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=0.00509) | SPY shaping=-0.002 (SPY ret=0.00685)
[CYCLE] Update 217/348 | Step 253,008/500,000 | Episode 312 | Time: 33205.5s
   📊 Metrics: Return=+12.36% | Sharpe=0.794 | DD=5.77% | Turnover=30.79%
   🎚️ Intra-Step TAPE: potential=0.4065 | delta_reward=+0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0341 | critic_loss=0.6987 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3493 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.0156 | router_entropy=-0.0031 | diversity_loss=0.0151 | mask=[1, 1, 0] | router=return=0.680 | risk=0.320 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7943 | ema=0.7661 | best_ema=0.7629 | no_improve=1
[CYCLE] Update 218/348 | Step 254,520/500,000 | Episode 312 | Time: 33392.9s
   📊 Metrics: Return=+16.64% | Sharpe=0.631 | DD=7.41% | Turnover=30.29%
   🎚️ Intra-Step TAPE: potential=0.2374 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0474 | critic_loss=0.5132 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2566 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0961 | router_entropy=-0.0032 | diversity_loss=0.0149 | mask=[1, 1, 0] | router=return=0.665 | risk=0.335 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6311 | ema=0.7526 | best_ema=0.7629 | no_improve=2
   🔬 Alpha Diversity: mean=2.47 | std=2.14 | range=[1.15, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.37 | MSFT=3.92 | GLD=3.04  BOT: BRK-B=1.87 | XOM=1.71 | KO=1.55
   🧬 FiLM: seq(dg=0.0049, db=0.0065, sat=0.0%) | latent(dg=0.0082, db=0.0049, sat=0.0%) | asset(dg=0.0039, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=108 (33.8%), low_vol=117 (36.6%), medium_vol=95 (29.7%)
[CYCLE] Update 219/348 | Step 256,032/500,000 | Episode 312 | Time: 33579.9s
   📊 Metrics: Return=+16.23% | Sharpe=0.362 | DD=10.50% | Turnover=30.53%
   🎚️ Intra-Step TAPE: potential=0.2461 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0107 | critic_loss=0.4923 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2462 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.0377 | router_entropy=-0.0032 | diversity_loss=0.0144 | mask=[1, 1, 0] | router=return=0.669 | risk=0.331 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3622 | ema=0.7135 | best_ema=0.7629 | no_improve=3
[CYCLE] Update 220/348 | Step 257,544/500,000 | Episode 312 | Time: 33768.2s
   📊 Metrics: Return=+41.99% | Sharpe=0.701 | DD=11.74% | Turnover=30.59%
   🎚️ Intra-Step TAPE: potential=0.7362 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0798 | critic_loss=0.7498 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3749 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.1289 | router_entropy=-0.0032 | diversity_loss=0.0153 | mask=[1, 1, 0] | router=return=0.668 | risk=0.332 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7009 | ema=0.7123 | best_ema=0.7629 | no_improve=4
   🔬 Alpha Diversity: mean=2.47 | std=2.20 | range=[1.15, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.04 | AMZN=3.87 | MSFT=3.12  BOT: BRK-B=1.92 | KO=1.46 | NEE=1.34
   🧬 FiLM: seq(dg=0.0046, db=0.0064, sat=0.0%) | latent(dg=0.0079, db=0.0047, sat=0.0%) | asset(dg=0.0039, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=108 (33.8%), low_vol=117 (36.6%), medium_vol=95 (29.7%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00313_shp0p793_actor.weights.h5 (Sharpe=0.793, MDD=11.96%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00314_shp1p084_actor.weights.h5 (Sharpe=1.084, MDD=18.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00315_shp1p050_actor.weights.h5 (Sharpe=1.050, MDD=11.74%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00316_shp1p186_actor.weights.h5 (Sharpe=1.186, MDD=19.37%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00320_shp0p817_actor.weights.h5 (Sharpe=0.817, MDD=10.78%)
[CYCLE] Update 221/348 | Step 259,056/500,000 | Episode 320 | Time: 33959.9s
   📊 Metrics: Return=+58.49% | Sharpe=0.817 | DD=10.78% | Turnover=31.26%
   🎚️ Intra-Step TAPE: potential=0.6406 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0803 | critic_loss=1.1888 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5944 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   🧠 Objective Experts: aux_loss=-0.1302 | router_entropy=-0.0032 | diversity_loss=0.0166 | mask=[1, 1, 0] | router=return=0.645 | risk=0.355 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8174 | ema=0.7228 | best_ema=0.7629 | no_improve=5
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.30% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4437
   📈 Benchmark Relative: 1/N shaping=-0.003 (EW ret=-0.00409) | SPY shaping=-0.001 (SPY ret=-0.00328)

🧭 REWARD PHASE UPDATE at 260,568 steps:
   B_ramp_2 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.60/t0.00/bm0.50/tt0.00
   objective_expert_mask=[1.0, 1.0, 0.0]
[CYCLE] Update 222/348 | Step 260,568/500,000 | Episode 320 | Time: 34149.2s
   📊 Metrics: Return=+1.23% | Sharpe=0.070 | DD=17.74% | Turnover=31.31%
   🎚️ Intra-Step TAPE: potential=0.7163 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0264 | critic_loss=0.7078 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3539 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0760 | router_entropy=-0.0033 | diversity_loss=0.0156 | mask=[1, 1, 0] | router=return=0.622 | risk=0.378 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0698 | ema=0.6575 | best_ema=0.7629 | no_improve=6
   🔬 Alpha Diversity: mean=2.44 | std=2.25 | range=[1.15, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.30 | MSFT=3.26 | JPM=3.21  BOT: KO=1.91 | CAT=1.87 | XOM=1.66
   🧬 FiLM: seq(dg=0.0052, db=0.0067, sat=0.0%) | latent(dg=0.0087, db=0.0050, sat=0.0%) | asset(dg=0.0039, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=111 (33.8%), low_vol=118 (36.0%), medium_vol=99 (30.2%)
[CYCLE] Update 223/348 | Step 262,080/500,000 | Episode 320 | Time: 34338.2s
   📊 Metrics: Return=+14.54% | Sharpe=0.476 | DD=17.74% | Turnover=31.27%
   🎚️ Intra-Step TAPE: potential=0.2330 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0431 | critic_loss=2.2019 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.1009 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.0910 | router_entropy=-0.0033 | diversity_loss=0.0136 | mask=[1, 1, 0] | router=return=0.616 | risk=0.384 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4758 | ema=0.6393 | best_ema=0.7629 | no_improve=7
[CYCLE] Update 224/348 | Step 263,592/500,000 | Episode 320 | Time: 34526.4s
   📊 Metrics: Return=+20.29% | Sharpe=0.403 | DD=20.20% | Turnover=31.58%
   🎚️ Intra-Step TAPE: potential=0.5391 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1120 | critic_loss=0.7797 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3899 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.1605 | router_entropy=-0.0033 | diversity_loss=0.0139 | mask=[1, 1, 0] | router=return=0.628 | risk=0.372 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4031 | ema=0.6157 | best_ema=0.7629 | no_improve=8
   🔬 Alpha Diversity: mean=2.45 | std=2.15 | range=[1.14, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.26 | AMZN=3.10 | MSFT=2.74  BOT: KO=1.84 | CAT=1.77 | NEE=1.69
   🧬 FiLM: seq(dg=0.0044, db=0.0061, sat=0.0%) | latent(dg=0.0082, db=0.0046, sat=0.0%) | asset(dg=0.0041, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=111 (33.8%), low_vol=118 (36.0%), medium_vol=99 (30.2%)
[CYCLE] Update 225/348 | Step 265,104/500,000 | Episode 320 | Time: 34714.9s
   📊 Metrics: Return=+22.30% | Sharpe=0.342 | DD=20.20% | Turnover=31.70%
   🎚️ Intra-Step TAPE: potential=0.5428 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0765 | critic_loss=0.6251 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3125 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.1252 | router_entropy=-0.0033 | diversity_loss=0.0151 | mask=[1, 1, 0] | router=return=0.624 | risk=0.376 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3419 | ema=0.5883 | best_ema=0.7629 | no_improve=9
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00321_shp1p031_actor.weights.h5 (Sharpe=1.031, MDD=16.07%)
[CYCLE] Update 226/348 | Step 266,616/500,000 | Episode 321 | Time: 34903.4s
   📊 Metrics: Return=+82.74% | Sharpe=1.031 | DD=16.07% | Turnover=32.16%
   🎚️ Intra-Step TAPE: potential=0.2500 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0684 | critic_loss=0.8074 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4037 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   🧠 Objective Experts: aux_loss=-0.1166 | router_entropy=-0.0032 | diversity_loss=0.0150 | mask=[1, 1, 0] | router=return=0.635 | risk=0.365 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0313 | ema=0.6326 | best_ema=0.7629 | no_improve=10
   🔬 Alpha Diversity: mean=2.40 | std=2.40 | range=[1.15, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.09 | NVDA=4.19 | JPM=1.98  BOT: XOM=1.70 | BRK-B=1.57 | CAT=1.41
   🧬 FiLM: seq(dg=0.0040, db=0.0052, sat=0.0%) | latent(dg=0.0094, db=0.0051, sat=0.0%) | asset(dg=0.0038, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=112 (34.0%), low_vol=118 (35.9%), medium_vol=99 (30.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.006, dd 0.93% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5244
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=-0.00183) | SPY shaping=0.001 (SPY ret=-0.00314)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00322_shp1p381_actor.weights.h5 (Sharpe=1.381, MDD=10.68%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00326_shp1p132_actor.weights.h5 (Sharpe=1.132, MDD=11.33%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00328_shp1p378_actor.weights.h5 (Sharpe=1.378, MDD=11.60%)
[CYCLE] Update 227/348 | Step 268,128/500,000 | Episode 328 | Time: 35092.3s
   📊 Metrics: Return=+105.06% | Sharpe=1.378 | DD=11.60% | Turnover=32.31%
   🎚️ Intra-Step TAPE: potential=0.6297 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0314 | critic_loss=1.9871 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.9935 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0824 | router_entropy=-0.0032 | diversity_loss=0.0166 | mask=[1, 1, 0] | router=return=0.648 | risk=0.352 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3783 | ema=0.7072 | best_ema=0.7629 | no_improve=11
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.29% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6011
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.00051) | SPY shaping=0.003 (SPY ret=-0.00373)
[CYCLE] Update 228/348 | Step 269,640/500,000 | Episode 328 | Time: 35279.8s
   📊 Metrics: Return=+0.84% | Sharpe=-0.036 | DD=13.56% | Turnover=32.24%
   🎚️ Intra-Step TAPE: potential=0.4184 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0917 | critic_loss=0.8163 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4082 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.1425 | router_entropy=-0.0032 | diversity_loss=0.0162 | mask=[1, 1, 0] | router=return=0.632 | risk=0.368 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0359 | ema=0.6329 | best_ema=0.7629 | no_improve=12
   🔬 Alpha Diversity: mean=2.46 | std=2.03 | range=[1.14, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.55 | BRK-B=3.47 | MSFT=2.70  BOT: NEE=2.14 | GLD=2.14 | CAT=1.66
   🧬 FiLM: seq(dg=0.0042, db=0.0061, sat=0.0%) | latent(dg=0.0083, db=0.0046, sat=0.0%) | asset(dg=0.0047, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=115 (34.2%), low_vol=120 (35.7%), medium_vol=101 (30.1%)
[CYCLE] Update 229/348 | Step 271,152/500,000 | Episode 328 | Time: 35467.4s
   📊 Metrics: Return=+9.32% | Sharpe=0.248 | DD=13.56% | Turnover=32.42%
   🎚️ Intra-Step TAPE: potential=0.4823 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1017 | critic_loss=0.8576 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4288 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.1520 | router_entropy=-0.0033 | diversity_loss=0.0155 | mask=[1, 1, 0] | router=return=0.618 | risk=0.382 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2476 | ema=0.5943 | best_ema=0.7629 | no_improve=13
[CYCLE] Update 230/348 | Step 272,664/500,000 | Episode 328 | Time: 35654.7s
   📊 Metrics: Return=+10.15% | Sharpe=0.181 | DD=13.56% | Turnover=31.89%
   🎚️ Intra-Step TAPE: potential=0.2484 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0949 | critic_loss=0.8176 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4088 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.1438 | router_entropy=-0.0032 | diversity_loss=0.0144 | mask=[1, 1, 0] | router=return=0.658 | risk=0.342 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1810 | ema=0.5530 | best_ema=0.7629 | no_improve=14
   🔬 Alpha Diversity: mean=2.48 | std=2.07 | range=[1.14, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.48 | MSFT=2.58 | GLD=2.31  BOT: XOM=1.98 | NEE=1.96 | CAT=1.61
   🧬 FiLM: seq(dg=0.0045, db=0.0063, sat=0.0%) | latent(dg=0.0089, db=0.0049, sat=0.0%) | asset(dg=0.0044, db=0.0026, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=115 (34.2%), low_vol=120 (35.7%), medium_vol=101 (30.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00329_shp0p788_actor.weights.h5 (Sharpe=0.788, MDD=14.63%)
[CYCLE] Update 231/348 | Step 274,176/500,000 | Episode 329 | Time: 35842.9s
   📊 Metrics: Return=+71.03% | Sharpe=0.788 | DD=14.63% | Turnover=31.25%
   🎚️ Intra-Step TAPE: potential=0.2394 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0681 | critic_loss=0.6693 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3347 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   🧠 Objective Experts: aux_loss=-0.1170 | router_entropy=-0.0033 | diversity_loss=0.0169 | mask=[1, 1, 0] | router=return=0.634 | risk=0.366 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7878 | ema=0.5765 | best_ema=0.7629 | no_improve=15
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 6.85% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4269
   📈 Benchmark Relative: 1/N shaping=0.003 (EW ret=0.00268) | SPY shaping=-0.002 (SPY ret=0.00698)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00335_shp1p133_actor.weights.h5 (Sharpe=1.133, MDD=11.09%)
[CYCLE] Update 232/348 | Step 275,688/500,000 | Episode 336 | Time: 36030.8s
   📊 Metrics: Return=+37.40% | Sharpe=0.479 | DD=16.05% | Turnover=32.03%
   🎚️ Intra-Step TAPE: potential=0.2516 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1515 | critic_loss=1.3364 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6682 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.2024 | router_entropy=-0.0033 | diversity_loss=0.0163 | mask=[1, 1, 0] | router=return=0.622 | risk=0.378 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4787 | ema=0.5667 | best_ema=0.7629 | no_improve=16
   🔬 Alpha Diversity: mean=2.46 | std=2.17 | range=[1.14, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.85 | NVDA=2.61 | BRK-B=2.44  BOT: NEE=1.88 | KO=1.82 | CAT=1.77
   🧬 FiLM: seq(dg=0.0036, db=0.0052, sat=0.0%) | latent(dg=0.0087, db=0.0046, sat=0.0%) | asset(dg=0.0047, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=119 (34.6%), low_vol=122 (35.5%), medium_vol=103 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.12% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2975
   📈 Benchmark Relative: 1/N shaping=-0.000 (EW ret=0.00314) | SPY shaping=-0.002 (SPY ret=0.00533)
[CYCLE] Update 233/348 | Step 277,200/500,000 | Episode 336 | Time: 36218.7s
   📊 Metrics: Return=+6.76% | Sharpe=0.436 | DD=4.64% | Turnover=33.18%
   🎚️ Intra-Step TAPE: potential=0.2771 | delta_reward=-0.0018
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1490 | critic_loss=0.7186 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3593 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.2008 | router_entropy=-0.0033 | diversity_loss=0.0165 | mask=[1, 1, 0] | router=return=0.593 | risk=0.407 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4365 | ema=0.5537 | best_ema=0.7629 | no_improve=17
[CYCLE] Update 234/348 | Step 278,712/500,000 | Episode 336 | Time: 36406.3s
   📊 Metrics: Return=+12.59% | Sharpe=0.490 | DD=4.67% | Turnover=31.87%
   🎚️ Intra-Step TAPE: potential=0.2313 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1251 | critic_loss=0.6266 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3133 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1752 | router_entropy=-0.0033 | diversity_loss=0.0160 | mask=[1, 1, 0] | router=return=0.611 | risk=0.389 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4901 | ema=0.5473 | best_ema=0.7629 | no_improve=18
   🔬 Alpha Diversity: mean=2.44 | std=2.06 | range=[1.14, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.85 | MSFT=3.37 | NVDA=3.14  BOT: XOM=1.81 | KO=1.80 | GLD=1.79
   🧬 FiLM: seq(dg=0.0033, db=0.0046, sat=0.0%) | latent(dg=0.0096, db=0.0051, sat=0.0%) | asset(dg=0.0048, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=119 (34.6%), low_vol=122 (35.5%), medium_vol=103 (29.9%)
[CYCLE] Update 235/348 | Step 280,224/500,000 | Episode 336 | Time: 36593.8s
   📊 Metrics: Return=+18.87% | Sharpe=0.474 | DD=9.20% | Turnover=32.27%
   🎚️ Intra-Step TAPE: potential=0.4737 | delta_reward=+0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0841 | critic_loss=0.3813 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1907 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.1333 | router_entropy=-0.0033 | diversity_loss=0.0162 | mask=[1, 1, 0] | router=return=0.624 | risk=0.376 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4743 | ema=0.5400 | best_ema=0.7629 | no_improve=19
[CYCLE] Update 236/348 | Step 281,736/500,000 | Episode 336 | Time: 36781.5s
   📊 Metrics: Return=+28.79% | Sharpe=0.490 | DD=12.89% | Turnover=32.14%
   🎚️ Intra-Step TAPE: potential=0.6676 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0183 | critic_loss=0.4149 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2075 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   🧠 Objective Experts: aux_loss=-0.0662 | router_entropy=-0.0032 | diversity_loss=0.0148 | mask=[1, 1, 0] | router=return=0.634 | risk=0.366 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4903 | ema=0.5350 | best_ema=0.7629 | no_improve=20
   🔬 Alpha Diversity: mean=2.39 | std=2.37 | range=[1.14, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.68 | NVDA=3.20 | JPM=2.28  BOT: KO=1.64 | BRK-B=1.62 | CAT=1.41
   🧬 FiLM: seq(dg=0.0039, db=0.0055, sat=0.0%) | latent(dg=0.0086, db=0.0047, sat=0.0%) | asset(dg=0.0041, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=119 (34.6%), low_vol=122 (35.5%), medium_vol=103 (29.9%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00337_shp1p107_actor.weights.h5 (Sharpe=1.107, MDD=11.61%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00339_shp0p773_actor.weights.h5 (Sharpe=0.773, MDD=12.89%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00340_shp0p831_actor.weights.h5 (Sharpe=0.831, MDD=12.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00341_shp0p815_actor.weights.h5 (Sharpe=0.815, MDD=17.20%)
[CYCLE] Update 237/348 | Step 283,248/500,000 | Episode 344 | Time: 36970.8s
   📊 Metrics: Return=+34.01% | Sharpe=0.485 | DD=11.13% | Turnover=32.20%
   🎚️ Intra-Step TAPE: potential=0.3635 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0632 | critic_loss=0.9387 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4694 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.1116 | router_entropy=-0.0032 | diversity_loss=0.0143 | mask=[1, 1, 0] | router=return=0.651 | risk=0.349 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4853 | ema=0.5301 | best_ema=0.7629 | no_improve=21
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3079
   📈 Benchmark Relative: 1/N shaping=-0.003 (EW ret=0.00237) | SPY shaping=-0.000 (SPY ret=0.00133)
[CYCLE] Update 238/348 | Step 284,760/500,000 | Episode 344 | Time: 37158.3s
   📊 Metrics: Return=+5.83% | Sharpe=0.437 | DD=9.68% | Turnover=32.01%
   🎚️ Intra-Step TAPE: potential=0.2613 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1046 | critic_loss=0.7200 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3600 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.1538 | router_entropy=-0.0032 | diversity_loss=0.0156 | mask=[1, 1, 0] | router=return=0.643 | risk=0.357 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4375 | ema=0.5208 | best_ema=0.7629 | no_improve=22
   🔬 Alpha Diversity: mean=2.43 | std=2.10 | range=[1.14, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.32 | MSFT=3.15 | JPM=3.06  BOT: NEE=2.08 | GLD=2.06 | CAT=1.81
   🧬 FiLM: seq(dg=0.0056, db=0.0059, sat=0.0%) | latent(dg=0.0110, db=0.0057, sat=0.0%) | asset(dg=0.0043, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=122 (34.7%), low_vol=125 (35.5%), medium_vol=105 (29.8%)
[CYCLE] Update 239/348 | Step 286,272/500,000 | Episode 344 | Time: 37345.9s
   📊 Metrics: Return=+7.20% | Sharpe=0.266 | DD=9.68% | Turnover=31.90%
   🎚️ Intra-Step TAPE: potential=0.2645 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0216 | critic_loss=0.5691 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2846 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.0264 | router_entropy=-0.0032 | diversity_loss=0.0144 | mask=[1, 1, 0] | router=return=0.643 | risk=0.357 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2665 | ema=0.4954 | best_ema=0.7629 | no_improve=23
[CYCLE] Update 240/348 | Step 287,784/500,000 | Episode 344 | Time: 37533.4s
   📊 Metrics: Return=+15.17% | Sharpe=0.429 | DD=9.68% | Turnover=31.43%
   🎚️ Intra-Step TAPE: potential=0.4309 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1424 | critic_loss=0.5594 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2797 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.1935 | router_entropy=-0.0033 | diversity_loss=0.0165 | mask=[1, 1, 0] | router=return=0.605 | risk=0.395 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4285 | ema=0.4887 | best_ema=0.7629 | no_improve=24
   🔬 Alpha Diversity: mean=2.45 | std=2.20 | range=[1.14, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.15 | MSFT=3.11 | AMZN=3.11  BOT: NEE=1.88 | GLD=1.79 | KO=1.78
   🧬 FiLM: seq(dg=0.0044, db=0.0037, sat=0.0%) | latent(dg=0.0118, db=0.0059, sat=0.0%) | asset(dg=0.0050, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=122 (34.7%), low_vol=125 (35.5%), medium_vol=105 (29.8%)
[CYCLE] Update 241/348 | Step 289,296/500,000 | Episode 344 | Time: 37720.6s
   📊 Metrics: Return=+20.36% | Sharpe=0.415 | DD=9.68% | Turnover=31.91%
   🎚️ Intra-Step TAPE: potential=0.2487 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1750 | critic_loss=0.6903 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3452 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.2253 | router_entropy=-0.0033 | diversity_loss=0.0168 | mask=[1, 1, 0] | router=return=0.616 | risk=0.384 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4149 | ema=0.4813 | best_ema=0.7629 | no_improve=25
[CYCLE] Update 242/348 | Step 290,808/500,000 | Episode 345 | Time: 37908.0s
   📊 Metrics: Return=+23.41% | Sharpe=0.319 | DD=10.12% | Turnover=32.70%
   🎚️ Intra-Step TAPE: potential=0.7489 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0412 | critic_loss=0.6463 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3231 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.0912 | router_entropy=-0.0033 | diversity_loss=0.0169 | mask=[1, 1, 0] | router=return=0.618 | risk=0.382 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3193 | ema=0.4651 | best_ema=0.7629 | no_improve=26
   🔬 Alpha Diversity: mean=2.41 | std=2.19 | range=[1.13, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.21 | AMZN=3.38 | GLD=2.79  BOT: CAT=1.92 | BRK-B=1.84 | XOM=1.79
   🧬 FiLM: seq(dg=0.0046, db=0.0043, sat=0.0%) | latent(dg=0.0120, db=0.0061, sat=0.0%) | asset(dg=0.0046, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=123 (34.8%), low_vol=125 (35.4%), medium_vol=105 (29.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.76% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2792
   📈 Benchmark Relative: 1/N shaping=-0.003 (EW ret=0.00439) | SPY shaping=0.001 (SPY ret=0.00162)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00346_shp0p884_actor.weights.h5 (Sharpe=0.884, MDD=15.14%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00348_shp0p985_actor.weights.h5 (Sharpe=0.985, MDD=11.69%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00349_shp1p104_actor.weights.h5 (Sharpe=1.104, MDD=11.95%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00351_shp1p032_actor.weights.h5 (Sharpe=1.032, MDD=12.32%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00352_shp1p192_actor.weights.h5 (Sharpe=1.192, MDD=12.47%)
[CYCLE] Update 243/348 | Step 292,320/500,000 | Episode 352 | Time: 38098.0s
   📊 Metrics: Return=+94.28% | Sharpe=1.192 | DD=12.47% | Turnover=32.16%
   🎚️ Intra-Step TAPE: potential=0.3404 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0827 | critic_loss=1.3187 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6594 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0262
   🧠 Objective Experts: aux_loss=-0.1346 | router_entropy=-0.0033 | diversity_loss=0.0159 | mask=[1, 1, 0] | router=return=0.611 | risk=0.389 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.1915 | ema=0.5377 | best_ema=0.7629 | no_improve=27
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.28% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5669
   📈 Benchmark Relative: 1/N shaping=0.000 (EW ret=0.00268) | SPY shaping=-0.004 (SPY ret=0.00850)
[CYCLE] Update 244/348 | Step 293,832/500,000 | Episode 352 | Time: 38285.4s
   📊 Metrics: Return=+11.64% | Sharpe=0.596 | DD=6.59% | Turnover=32.48%
   🎚️ Intra-Step TAPE: potential=0.2657 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1309 | critic_loss=0.5291 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2646 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.1800 | router_entropy=-0.0032 | diversity_loss=0.0145 | mask=[1, 1, 0] | router=return=0.637 | risk=0.363 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5958 | ema=0.5436 | best_ema=0.7629 | no_improve=28
   🔬 Alpha Diversity: mean=2.44 | std=2.20 | range=[1.13, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=3.08 | BRK-B=2.57 | AMZN=2.52  BOT: KO=1.91 | GLD=1.75 | CAT=1.68
   🧬 FiLM: seq(dg=0.0075, db=0.0070, sat=0.0%) | latent(dg=0.0128, db=0.0065, sat=0.0%) | asset(dg=0.0049, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=126 (35.0%), low_vol=129 (35.8%), medium_vol=105 (29.2%)
[CYCLE] Update 245/348 | Step 295,344/500,000 | Episode 352 | Time: 38473.0s
   📊 Metrics: Return=+13.34% | Sharpe=0.387 | DD=10.06% | Turnover=32.73%
   🎚️ Intra-Step TAPE: potential=0.5879 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1131 | critic_loss=0.5362 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2681 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.1629 | router_entropy=-0.0033 | diversity_loss=0.0149 | mask=[1, 1, 0] | router=return=0.613 | risk=0.387 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3871 | ema=0.5279 | best_ema=0.7629 | no_improve=29
[CYCLE] Update 246/348 | Step 296,856/500,000 | Episode 352 | Time: 38660.8s
   📊 Metrics: Return=+44.89% | Sharpe=0.945 | DD=10.06% | Turnover=32.65%
   🎚️ Intra-Step TAPE: potential=0.7455 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0337 | critic_loss=0.5575 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2788 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0820 | router_entropy=-0.0033 | diversity_loss=0.0142 | mask=[1, 1, 0] | router=return=0.620 | risk=0.380 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9451 | ema=0.5696 | best_ema=0.7629 | no_improve=30
   🔬 Alpha Diversity: mean=2.41 | std=2.30 | range=[1.13, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.02 | NVDA=2.45 | GLD=2.44  BOT: BRK-B=1.80 | JPM=1.79 | MSFT=1.76
   🧬 FiLM: seq(dg=0.0078, db=0.0074, sat=0.0%) | latent(dg=0.0128, db=0.0066, sat=0.0%) | asset(dg=0.0046, db=0.0026, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=126 (35.0%), low_vol=129 (35.8%), medium_vol=105 (29.2%)
[CYCLE] Update 247/348 | Step 298,368/500,000 | Episode 353 | Time: 38848.3s
   📊 Metrics: Return=+40.16% | Sharpe=0.610 | DD=11.40% | Turnover=32.18%
   🎚️ Intra-Step TAPE: potential=0.7541 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0072 | critic_loss=0.7146 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3573 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0570 | router_entropy=-0.0032 | diversity_loss=0.0157 | mask=[1, 1, 0] | router=return=0.631 | risk=0.369 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6096 | ema=0.5736 | best_ema=0.7629 | no_improve=31
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3475
   📈 Benchmark Relative: 1/N shaping=0.012 (EW ret=-0.00095) | SPY shaping=0.003 (SPY ret=-0.00062)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00355_shp1p104_actor.weights.h5 (Sharpe=1.104, MDD=10.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00359_shp0p908_actor.weights.h5 (Sharpe=0.908, MDD=10.77%)
[CYCLE] Update 248/348 | Step 299,880/500,000 | Episode 360 | Time: 39037.1s
   📊 Metrics: Return=+21.11% | Sharpe=0.286 | DD=13.86% | Turnover=32.15%
   🎚️ Intra-Step TAPE: potential=0.2449 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0588 | critic_loss=1.1412 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5706 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.1092 | router_entropy=-0.0032 | diversity_loss=0.0162 | mask=[1, 1, 0] | router=return=0.629 | risk=0.371 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2860 | ema=0.5449 | best_ema=0.7629 | no_improve=32
   🔬 Alpha Diversity: mean=2.43 | std=1.85 | range=[1.13, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.84 | GLD=2.87 | NVDA=2.59  BOT: XOM=2.25 | JPM=2.18 | MSFT=2.18
   🧬 FiLM: seq(dg=0.0097, db=0.0086, sat=0.0%) | latent(dg=0.0149, db=0.0076, sat=0.0%) | asset(dg=0.0049, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=129 (35.1%), low_vol=131 (35.6%), medium_vol=108 (29.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.43% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2687
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=0.01890) | SPY shaping=0.001 (SPY ret=0.01749)

🎛️ EXECUTION BETA UPDATE at 301,392 steps:
   action_execution_beta: 0.800 (w_exec=(1-β)w_prev + βw_raw)
[CYCLE] Update 249/348 | Step 301,392/500,000 | Episode 360 | Time: 39224.6s
   📊 Metrics: Return=+5.62% | Sharpe=0.278 | DD=11.52% | Turnover=32.96%
   🎚️ Intra-Step TAPE: potential=0.7177 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0852 | critic_loss=0.5959 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2980 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=0.0359 | router_entropy=-0.0032 | diversity_loss=0.0150 | mask=[1, 1, 0] | router=return=0.651 | risk=0.349 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2785 | ema=0.5182 | best_ema=0.7629 | no_improve=33

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
[CYCLE] Update 250/348 | Step 303,408/500,000 | Episode 360 | Time: 39437.6s
   📊 Metrics: Return=+37.24% | Sharpe=1.053 | DD=11.52% | Turnover=36.14%
   🎚️ Intra-Step TAPE: potential=0.6523 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0038 | critic_loss=0.5605 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2803 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.0511 | router_entropy=-0.0032 | diversity_loss=0.0166 | mask=[1, 1, 0] | router=return=0.641 | risk=0.359 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0429 | ema=0.5707 | best_ema=0.7629 | no_improve=34
   🔬 Alpha Diversity: mean=2.45 | std=1.77 | range=[1.13, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.34 | KO=2.82 | GLD=2.81  BOT: CAT=2.30 | XOM=2.28 | AMZN=2.16
   🧬 FiLM: seq(dg=0.0106, db=0.0089, sat=0.0%) | latent(dg=0.0156, db=0.0078, sat=0.0%) | asset(dg=0.0057, db=0.0033, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=129 (35.1%), low_vol=131 (35.6%), medium_vol=108 (29.3%)
[CYCLE] Update 251/348 | Step 305,424/500,000 | Episode 360 | Time: 39641.9s
   📊 Metrics: Return=+53.66% | Sharpe=0.985 | DD=11.52% | Turnover=37.31%
   🎚️ Intra-Step TAPE: potential=0.2204 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0119 | critic_loss=0.6867 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3434 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0339 | router_entropy=-0.0032 | diversity_loss=0.0160 | mask=[1, 1, 0] | router=return=0.656 | risk=0.344 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9648 | ema=0.6101 | best_ema=0.7629 | no_improve=35
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00361_shp1p109_actor.weights.h5 (Sharpe=1.109, MDD=15.85%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00365_shp0p785_actor.weights.h5 (Sharpe=0.785, MDD=11.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00367_shp0p883_actor.weights.h5 (Sharpe=0.883, MDD=9.95%)
[CYCLE] Update 252/348 | Step 307,440/500,000 | Episode 368 | Time: 39847.7s
   📊 Metrics: Return=+19.29% | Sharpe=0.228 | DD=20.63% | Turnover=38.55%
   🎚️ Intra-Step TAPE: potential=0.2397 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0473 | critic_loss=1.0297 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5148 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.0918 | router_entropy=-0.0032 | diversity_loss=0.0145 | mask=[1, 1, 0] | router=return=0.653 | risk=0.347 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1979 | ema=0.5689 | best_ema=0.7629 | no_improve=36
   🔬 Alpha Diversity: mean=2.47 | std=1.78 | range=[1.13, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=3.37 | NVDA=3.26 | CAT=2.64  BOT: JPM=2.21 | MSFT=2.20 | NEE=2.07
   🧬 FiLM: seq(dg=0.0080, db=0.0076, sat=0.0%) | latent(dg=0.0124, db=0.0063, sat=0.0%) | asset(dg=0.0044, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=134 (35.6%), low_vol=134 (35.6%), medium_vol=108 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 12.23% / trig 16.50%) | terminal=0.000 (peak 0.011) | TAPE=0.2455
   📈 Benchmark Relative: 1/N shaping=-0.003 (EW ret=0.00411) | SPY shaping=-0.002 (SPY ret=0.00644)
[CYCLE] Update 253/348 | Step 309,456/500,000 | Episode 368 | Time: 40052.0s
   📊 Metrics: Return=+5.67% | Sharpe=0.264 | DD=15.34% | Turnover=41.59%
   🎚️ Intra-Step TAPE: potential=0.2296 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0185 | critic_loss=0.8059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.0652 | router_entropy=-0.0032 | diversity_loss=0.0164 | mask=[1, 1, 0] | router=return=0.647 | risk=0.353 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2074 | ema=0.5327 | best_ema=0.7629 | no_improve=37
[CYCLE] Update 254/348 | Step 311,472/500,000 | Episode 368 | Time: 40256.7s
   📊 Metrics: Return=+1.70% | Sharpe=0.042 | DD=19.25% | Turnover=40.12%
   🎚️ Intra-Step TAPE: potential=0.2400 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0233 | critic_loss=0.7589 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3794 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.0681 | router_entropy=-0.0031 | diversity_loss=0.0141 | mask=[1, 1, 0] | router=return=0.686 | risk=0.314 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0019 | ema=0.4793 | best_ema=0.7629 | no_improve=38
   🔬 Alpha Diversity: mean=2.46 | std=2.11 | range=[1.13, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.84 | GLD=2.52 | NEE=2.37  BOT: KO=1.93 | CAT=1.91 | MSFT=1.82
   🧬 FiLM: seq(dg=0.0102, db=0.0094, sat=0.0%) | latent(dg=0.0143, db=0.0073, sat=0.0%) | asset(dg=0.0052, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=134 (35.6%), low_vol=134 (35.6%), medium_vol=108 (28.7%)
[CYCLE] Update 255/348 | Step 313,488/500,000 | Episode 368 | Time: 40460.4s
   📊 Metrics: Return=+3.19% | Sharpe=0.030 | DD=19.25% | Turnover=41.45%
   🎚️ Intra-Step TAPE: potential=0.5134 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0216 | critic_loss=0.8473 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4236 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0637 | router_entropy=-0.0029 | diversity_loss=0.0116 | mask=[1, 1, 0] | router=return=0.723 | risk=0.277 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0255 | ema=0.4288 | best_ema=0.7629 | no_improve=39
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp0p964_actor.weights.h5 (Sharpe=0.964, MDD=21.79%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00375_shp0p720_actor.weights.h5 (Sharpe=0.720, MDD=11.33%)
[CYCLE] Update 256/348 | Step 315,504/500,000 | Episode 376 | Time: 40665.5s
   📊 Metrics: Return=+53.85% | Sharpe=0.611 | DD=18.38% | Turnover=41.49%
   🎚️ Intra-Step TAPE: potential=0.7435 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0088 | critic_loss=1.1612 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5806 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.0333 | router_entropy=-0.0029 | diversity_loss=0.0121 | mask=[1, 1, 0] | router=return=0.727 | risk=0.273 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5550 | ema=0.4414 | best_ema=0.7629 | no_improve=40
   🔬 Alpha Diversity: mean=2.42 | std=1.59 | range=[1.12, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=3.64 | NVDA=2.66 | AMZN=2.36  BOT: CAT=2.29 | KO=2.27 | JPM=2.16
   🧬 FiLM: seq(dg=0.0088, db=0.0092, sat=0.0%) | latent(dg=0.0112, db=0.0061, sat=0.0%) | asset(dg=0.0038, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=140 (36.5%), low_vol=134 (34.9%), medium_vol=110 (28.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.25% / trig 16.50%) | terminal=0.000 (peak 0.002) | TAPE=0.3350
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=0.00098) | SPY shaping=0.001 (SPY ret=0.00036)
[CYCLE] Update 257/348 | Step 317,520/500,000 | Episode 376 | Time: 40869.8s
   📊 Metrics: Return=+12.60% | Sharpe=0.784 | DD=8.82% | Turnover=42.44%
   🎚️ Intra-Step TAPE: potential=0.5140 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0808 | critic_loss=1.0316 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5158 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.1254 | router_entropy=-0.0030 | diversity_loss=0.0138 | mask=[1, 1, 0] | router=return=0.697 | risk=0.303 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7199 | ema=0.4693 | best_ema=0.7629 | no_improve=41
[CYCLE] Update 258/348 | Step 319,536/500,000 | Episode 376 | Time: 41073.8s
   📊 Metrics: Return=+12.26% | Sharpe=0.366 | DD=8.82% | Turnover=41.84%
   🎚️ Intra-Step TAPE: potential=0.2390 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0176 | critic_loss=0.4803 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2401 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0260 | router_entropy=-0.0030 | diversity_loss=0.0133 | mask=[1, 1, 0] | router=return=0.695 | risk=0.305 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3072 | ema=0.4531 | best_ema=0.7629 | no_improve=42
   🔬 Alpha Diversity: mean=2.44 | std=1.97 | range=[1.12, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=3.65 | NVDA=2.51 | MSFT=2.44  BOT: CAT=1.89 | XOM=1.85 | AMZN=1.77
   🧬 FiLM: seq(dg=0.0097, db=0.0094, sat=0.0%) | latent(dg=0.0119, db=0.0064, sat=0.0%) | asset(dg=0.0048, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=140 (36.5%), low_vol=134 (34.9%), medium_vol=110 (28.6%)

🧭 REWARD PHASE UPDATE at 321,552 steps:
   C_ramp_1 | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t0.15/bm0.75/tt0.15
   objective_expert_mask=[1.0, 1.0, 1.0]
[CYCLE] Update 259/348 | Step 321,552/500,000 | Episode 376 | Time: 41277.9s
   📊 Metrics: Return=+12.95% | Sharpe=0.234 | DD=8.87% | Turnover=42.36%
   🎚️ Intra-Step TAPE: potential=0.2434 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0801 | critic_loss=0.3900 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1950 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1231 | router_entropy=-0.0048 | diversity_loss=0.0149 | mask=[1, 1, 1] | router=return=0.568 | risk=0.255 | discipline=0.177
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1706 | ema=0.4248 | best_ema=0.7629 | no_improve=43
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00383_shp0p731_actor.weights.h5 (Sharpe=0.731, MDD=10.45%)
[CYCLE] Update 260/348 | Step 323,568/500,000 | Episode 384 | Time: 41482.6s
   📊 Metrics: Return=+20.89% | Sharpe=0.282 | DD=10.33% | Turnover=42.13%
   🎚️ Intra-Step TAPE: potential=0.2288 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0348 | critic_loss=1.0937 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5468 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.0085 | router_entropy=-0.0049 | diversity_loss=0.0151 | mask=[1, 1, 1] | router=return=0.553 | risk=0.235 | discipline=0.212
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2207 | ema=0.4044 | best_ema=0.7629 | no_improve=44
   🔬 Alpha Diversity: mean=2.45 | std=1.87 | range=[1.12, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=3.94 | AMZN=3.67 | BRK-B=2.75  BOT: JPM=1.76 | XOM=1.76 | CAT=1.75
   🧬 FiLM: seq(dg=0.0116, db=0.0112, sat=0.0%) | latent(dg=0.0135, db=0.0074, sat=0.0%) | asset(dg=0.0046, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=141 (36.0%), low_vol=137 (34.9%), medium_vol=114 (29.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.51% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2719
   📈 Benchmark Relative: 1/N shaping=-0.018 (EW ret=0.01499) | SPY shaping=-0.005 (SPY ret=0.01521)

📚 TURNOVER CURRICULUM UPDATE at 325,584 steps:
   Turnover penalty scalar: 0.1
[CYCLE] Update 261/348 | Step 325,584/500,000 | Episode 384 | Time: 41687.2s
   📊 Metrics: Return=+7.62% | Sharpe=0.484 | DD=6.61% | Turnover=39.62%
   🎚️ Intra-Step TAPE: potential=0.6640 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0383 | critic_loss=0.5169 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2584 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.0826 | router_entropy=-0.0049 | diversity_loss=0.0153 | mask=[1, 1, 1] | router=return=0.541 | risk=0.252 | discipline=0.207
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4445 | ema=0.4084 | best_ema=0.7629 | no_improve=45
[CYCLE] Update 262/348 | Step 327,600/500,000 | Episode 384 | Time: 41891.1s
   📊 Metrics: Return=+25.54% | Sharpe=0.756 | DD=9.14% | Turnover=38.61%
   🎚️ Intra-Step TAPE: potential=0.7376 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0916 | critic_loss=0.4320 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2160 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.1361 | router_entropy=-0.0050 | diversity_loss=0.0157 | mask=[1, 1, 1] | router=return=0.520 | risk=0.243 | discipline=0.237
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7251 | ema=0.4401 | best_ema=0.7629 | no_improve=46
   🔬 Alpha Diversity: mean=2.49 | std=1.90 | range=[1.12, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: GLD=4.07 | KO=3.04 | AMZN=3.03  BOT: NVDA=2.01 | JPM=1.97 | CAT=1.86
   🧬 FiLM: seq(dg=0.0129, db=0.0117, sat=0.0%) | latent(dg=0.0151, db=0.0081, sat=0.0%) | asset(dg=0.0053, db=0.0031, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=141 (36.0%), low_vol=137 (34.9%), medium_vol=114 (29.1%)
[CYCLE] Update 263/348 | Step 329,616/500,000 | Episode 384 | Time: 42095.0s
   📊 Metrics: Return=+45.08% | Sharpe=0.918 | DD=9.14% | Turnover=38.38%
   🎚️ Intra-Step TAPE: potential=0.7451 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1089 | critic_loss=0.5091 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2546 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.1525 | router_entropy=-0.0050 | diversity_loss=0.0150 | mask=[1, 1, 1] | router=return=0.530 | risk=0.225 | discipline=0.245
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8892 | ema=0.4850 | best_ema=0.7629 | no_improve=47
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00385_shp0p775_actor.weights.h5 (Sharpe=0.775, MDD=8.69%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00387_shp0p987_actor.weights.h5 (Sharpe=0.987, MDD=9.87%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00388_shp0p779_actor.weights.h5 (Sharpe=0.779, MDD=9.20%)
