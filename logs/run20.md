Streaming output truncated to the last 5000 lines.
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
      285,000+ steps: scalar=0.05
      345,000+ steps: scalar=0.10
      405,000+ steps: scalar=0.20
      470,000+ steps: scalar=0.30
   🎛️ Action Execution Beta Curriculum:
      0+ steps: beta=0.55
      235,000+ steps: beta=0.65
      365,000+ steps: beta=0.75
      430,000+ steps: beta=0.90
      480,000+ steps: beta=1.00
   🏆 Deterministic-validation checkpoints: disabled
   🧷 Legacy checkpoint routes: configurable
   [WARN] Checkpoint selector default: legacy high-watermark path
   💾 High-watermark checkpoints: enabled (Sharpe >= 0.70, MDD <= 25.0%, skip_on_det_validation=True)
   ⏹️ Training early-stop: enabled (warmup=250,000 steps, patience=75 updates, min_delta=0.005, hard_dd=45.0% x 8)
      ↳ phase-aware resets: grace=15,000 steps | reset_ema_on_transition=True | reward_phase=True | turnover=True | beta=True | rollout_batch=True | temperature=True
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260326_065026_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260326_065026_metadata.json
[CYCLE] Update 1/401 | Step 1,008/500,000 | Episode 0 | Time: 119.6s
   📊 Metrics: Return=-2.35% | Sharpe=-1.148 | DD=3.77% | Turnover=26.81%
   🎚️ Intra-Step TAPE: potential=0.2476 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.3052 | critic_loss=1.3156 | mean_adv=-0.0003
   🧮 Loss Detail: critic_scaled=0.6578 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=0.0225 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-1.1485 | ema=-1.1485 | best_ema=-1.1485 | no_improve=0
[CYCLE] Update 2/401 | Step 2,016/500,000 | Episode 0 | Time: 220.3s
   📊 Metrics: Return=-0.33% | Sharpe=-0.268 | DD=4.34% | Turnover=27.08%
   🎚️ Intra-Step TAPE: potential=0.3099 | delta_reward=-0.0027
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0867 | critic_loss=1.4956 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7478 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0272
   🧠 Objective Experts: aux_loss=-0.0160 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2684 | ema=-1.0605 | best_ema=-1.0605 | no_improve=0
   🔬 Alpha Diversity: mean=2.57 | std=2.24 | range=[1.26, 10.37] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.28 | AMZN=2.57 | GLD=2.20  BOT: KO=1.52 | BRK-B=1.51 | XOM=1.32
   🧬 FiLM: seq(dg=0.0001, db=0.0001, sat=0.0%) | latent(dg=0.0006, db=0.0004, sat=0.0%) | asset(dg=0.0003, db=0.0002, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=3 (18.8%), low_vol=9 (56.2%), medium_vol=4 (25.0%)
[CYCLE] Update 3/401 | Step 3,024/500,000 | Episode 0 | Time: 321.3s
   📊 Metrics: Return=-1.03% | Sharpe=-0.227 | DD=8.20% | Turnover=26.64%
   🎚️ Intra-Step TAPE: potential=0.2516 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1057 | critic_loss=2.0962 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=1.0481 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=0.0182 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2266 | ema=-0.9771 | best_ema=-0.9771 | no_improve=0
[CYCLE] Update 4/401 | Step 4,032/500,000 | Episode 0 | Time: 422.1s
   📊 Metrics: Return=+9.53% | Sharpe=0.652 | DD=8.20% | Turnover=26.11%
   🎚️ Intra-Step TAPE: potential=0.7457 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0719 | critic_loss=2.5124 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=1.2562 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0282
   🧠 Objective Experts: aux_loss=-0.0126 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6519 | ema=-0.8142 | best_ema=-0.8142 | no_improve=0
   🔬 Alpha Diversity: mean=2.64 | std=1.99 | range=[1.25, 9.38] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.93 | AMZN=2.99 | CAT=2.75  BOT: BRK-B=1.54 | XOM=1.37 | KO=1.35
   🧬 FiLM: seq(dg=0.0002, db=0.0001, sat=0.0%) | latent(dg=0.0006, db=0.0004, sat=0.0%) | asset(dg=0.0003, db=0.0002, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=3 (18.8%), low_vol=9 (56.2%), medium_vol=4 (25.0%)
[CYCLE] Update 5/401 | Step 5,040/500,000 | Episode 0 | Time: 522.9s
   📊 Metrics: Return=+9.35% | Sharpe=0.462 | DD=10.89% | Turnover=26.10%
   🎚️ Intra-Step TAPE: potential=0.2413 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0702 | critic_loss=1.9705 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.9852 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0279
   🧠 Objective Experts: aux_loss=-0.0103 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4615 | ema=-0.6866 | best_ema=-0.6866 | no_improve=0
[CYCLE] Update 6/401 | Step 6,048/500,000 | Episode 0 | Time: 623.8s
   📊 Metrics: Return=+22.09% | Sharpe=0.957 | DD=10.89% | Turnover=25.95%
   🎚️ Intra-Step TAPE: potential=0.7480 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0669 | critic_loss=1.8994 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.9497 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.0087 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9573 | ema=-0.5222 | best_ema=-0.5222 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=2.20 | range=[1.25, 10.33] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.82 | AMZN=4.25 | GLD=2.30  BOT: KO=1.58 | BRK-B=1.51 | XOM=1.39
   🧬 FiLM: seq(dg=0.0002, db=0.0001, sat=0.0%) | latent(dg=0.0008, db=0.0004, sat=0.0%) | asset(dg=0.0004, db=0.0003, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=3 (18.8%), low_vol=9 (56.2%), medium_vol=4 (25.0%)
[CYCLE] Update 7/401 | Step 7,056/500,000 | Episode 0 | Time: 724.7s
   📊 Metrics: Return=+29.41% | Sharpe=1.071 | DD=10.89% | Turnover=25.39%
   🎚️ Intra-Step TAPE: potential=0.5957 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0240 | critic_loss=2.1507 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=1.0754 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0279
   🧠 Objective Experts: aux_loss=-0.0468 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0707 | ema=-0.3629 | best_ema=-0.3629 | no_improve=0
[CYCLE] Update 8/401 | Step 8,064/500,000 | Episode 0 | Time: 825.8s
   📊 Metrics: Return=+43.62% | Sharpe=1.357 | DD=10.89% | Turnover=25.16%
   🎚️ Intra-Step TAPE: potential=0.7532 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0440 | critic_loss=1.1739 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5869 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0285
   🧠 Objective Experts: aux_loss=-0.0244 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3570 | ema=-0.1909 | best_ema=-0.1909 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=1.82 | range=[1.25, 10.20] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.75 | AMZN=3.70 | CAT=2.89  BOT: MSFT=2.21 | BRK-B=1.82 | XOM=1.80
   🧬 FiLM: seq(dg=0.0004, db=0.0002, sat=0.0%) | latent(dg=0.0012, db=0.0007, sat=0.0%) | asset(dg=0.0005, db=0.0003, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=3 (18.8%), low_vol=9 (56.2%), medium_vol=4 (25.0%)
[CYCLE] Update 9/401 | Step 9,072/500,000 | Episode 0 | Time: 926.9s
   📊 Metrics: Return=+46.58% | Sharpe=1.302 | DD=10.89% | Turnover=25.19%
   🎚️ Intra-Step TAPE: potential=0.4755 | delta_reward=+0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0515 | critic_loss=1.5394 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7697 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.0186 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3025 | ema=-0.0416 | best_ema=-0.0416 | no_improve=0
[CYCLE] Update 10/401 | Step 10,080/500,000 | Episode 0 | Time: 1028.0s
   📊 Metrics: Return=+57.98% | Sharpe=1.427 | DD=10.89% | Turnover=25.10%
   🎚️ Intra-Step TAPE: potential=0.7239 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0257 | critic_loss=1.2653 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6326 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.0425 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4266 | ema=0.1052 | best_ema=0.1052 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=1.96 | range=[1.25, 10.49] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=4.30 | NVDA=3.48 | AMZN=3.40  BOT: KO=1.77 | NEE=1.73 | XOM=1.72
   🧬 FiLM: seq(dg=0.0004, db=0.0002, sat=0.0%) | latent(dg=0.0016, db=0.0009, sat=0.0%) | asset(dg=0.0006, db=0.0003, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=3 (18.8%), low_vol=9 (56.2%), medium_vol=4 (25.0%)
[CYCLE] Update 11/401 | Step 11,088/500,000 | Episode 0 | Time: 1129.2s
   📊 Metrics: Return=+65.43% | Sharpe=1.457 | DD=10.89% | Turnover=25.05%
   🎚️ Intra-Step TAPE: potential=0.6850 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0474 | critic_loss=0.9177 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4588 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0279
   🧠 Objective Experts: aux_loss=-0.0238 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4567 | ema=0.2404 | best_ema=0.2404 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00001_shp1p629_actor.weights.h5 (Sharpe=1.629, MDD=10.89%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00006_shp1p207_actor.weights.h5 (Sharpe=1.207, MDD=9.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00010_shp1p651_actor.weights.h5 (Sharpe=1.651, MDD=10.96%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00011_shp0p989_actor.weights.h5 (Sharpe=0.989, MDD=11.92%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00013_shp1p179_actor.weights.h5 (Sharpe=1.179, MDD=11.18%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00014_shp0p962_actor.weights.h5 (Sharpe=0.962, MDD=17.52%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00016_shp1p181_actor.weights.h5 (Sharpe=1.181, MDD=10.22%)
[CYCLE] Update 12/401 | Step 12,096/500,000 | Episode 16 | Time: 1218.4s
   📊 Metrics: Return=+58.88% | Sharpe=1.181 | DD=10.22% | Turnover=25.44%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0666 | critic_loss=1.3865 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6933 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.0042 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1811 | ema=0.3344 | best_ema=0.3344 | no_improve=0
   🔬 Alpha Diversity: mean=2.61 | std=1.95 | range=[1.25, 9.71] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.09 | CAT=3.76 | JPM=3.06  BOT: BRK-B=1.75 | XOM=1.59 | GLD=1.31
   🧬 FiLM: seq(dg=0.0004, db=0.0002, sat=0.0%) | latent(dg=0.0025, db=0.0012, sat=0.0%) | asset(dg=0.0007, db=0.0004, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=6 (18.8%), low_vol=18 (56.2%), medium_vol=8 (25.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.500) | TAPE=0.5600
[CYCLE] Update 13/401 | Step 13,104/500,000 | Episode 16 | Time: 1319.1s
   📊 Metrics: Return=+12.90% | Sharpe=4.080 | DD=1.95% | Turnover=27.13%
   🎚️ Intra-Step TAPE: potential=0.7513 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0482 | critic_loss=1.7663 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.8831 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0280
   🧠 Objective Experts: aux_loss=-0.0231 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=4.0797 | ema=0.7090 | best_ema=0.7090 | no_improve=0
[CYCLE] Update 14/401 | Step 14,112/500,000 | Episode 16 | Time: 1420.2s
   📊 Metrics: Return=+37.83% | Sharpe=4.144 | DD=3.02% | Turnover=26.10%
   🎚️ Intra-Step TAPE: potential=0.7528 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0355 | critic_loss=1.4711 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.7356 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0278
   🧠 Objective Experts: aux_loss=-0.0335 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=4.1445 | ema=1.0525 | best_ema=1.0525 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=1.99 | range=[1.24, 10.29] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.72 | AMZN=3.82 | MSFT=2.83  BOT: KO=1.78 | XOM=1.68 | GLD=1.63
   🧬 FiLM: seq(dg=0.0005, db=0.0002, sat=0.0%) | latent(dg=0.0030, db=0.0015, sat=0.0%) | asset(dg=0.0007, db=0.0004, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=6 (18.8%), low_vol=18 (56.2%), medium_vol=8 (25.0%)
[CYCLE] Update 15/401 | Step 15,120/500,000 | Episode 16 | Time: 1521.2s
   📊 Metrics: Return=+24.93% | Sharpe=1.857 | DD=12.94% | Turnover=26.21%
   🎚️ Intra-Step TAPE: potential=0.2221 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0716 | critic_loss=1.3185 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.6592 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=0.0035 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8566 | ema=1.1329 | best_ema=1.1329 | no_improve=0
[CYCLE] Update 16/401 | Step 16,128/500,000 | Episode 16 | Time: 1622.1s
   📊 Metrics: Return=+15.44% | Sharpe=0.828 | DD=21.84% | Turnover=26.29%
   🎚️ Intra-Step TAPE: potential=0.2337 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0195 | critic_loss=1.1788 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5894 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=-0.0472 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8284 | ema=1.1025 | best_ema=1.1025 | no_improve=0
   🔬 Alpha Diversity: mean=2.62 | std=1.97 | range=[1.24, 10.30] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.16 | AMZN=3.95 | CAT=3.41  BOT: BRK-B=1.68 | KO=1.53 | GLD=1.36
   🧬 FiLM: seq(dg=0.0005, db=0.0002, sat=0.0%) | latent(dg=0.0032, db=0.0016, sat=0.0%) | asset(dg=0.0008, db=0.0005, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=6 (18.8%), low_vol=18 (56.2%), medium_vol=8 (25.0%)
[CYCLE] Update 17/401 | Step 17,136/500,000 | Episode 16 | Time: 1723.3s
   📊 Metrics: Return=+18.97% | Sharpe=0.704 | DD=24.13% | Turnover=26.08%
   🎚️ Intra-Step TAPE: potential=0.5612 | delta_reward=+0.0028
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0196 | critic_loss=1.0443 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5222 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=-0.0419 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7041 | ema=1.0626 | best_ema=1.0626 | no_improve=0
[CYCLE] Update 18/401 | Step 18,144/500,000 | Episode 16 | Time: 1824.3s
   📊 Metrics: Return=+23.41% | Sharpe=0.706 | DD=24.13% | Turnover=25.76%
   🎚️ Intra-Step TAPE: potential=0.5830 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0637 | critic_loss=1.2970 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.6485 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0272
   🧠 Objective Experts: aux_loss=0.0105 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7062 | ema=1.0270 | best_ema=1.0270 | no_improve=0
   🔬 Alpha Diversity: mean=2.57 | std=2.12 | range=[1.24, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.50 | CAT=4.26 | AMZN=4.03  BOT: XOM=1.68 | KO=1.50 | GLD=1.48
   🧬 FiLM: seq(dg=0.0005, db=0.0002, sat=0.0%) | latent(dg=0.0039, db=0.0020, sat=0.0%) | asset(dg=0.0009, db=0.0005, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=6 (18.8%), low_vol=18 (56.2%), medium_vol=8 (25.0%)
[CYCLE] Update 19/401 | Step 19,152/500,000 | Episode 16 | Time: 1925.5s
   📊 Metrics: Return=+22.07% | Sharpe=0.585 | DD=24.13% | Turnover=25.53%
   🎚️ Intra-Step TAPE: potential=0.2616 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0203 | critic_loss=1.0017 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5008 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0267
   🧠 Objective Experts: aux_loss=-0.0444 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5845 | ema=0.9827 | best_ema=0.9827 | no_improve=0
[CYCLE] Update 20/401 | Step 20,160/500,000 | Episode 16 | Time: 2026.5s
   📊 Metrics: Return=+26.64% | Sharpe=0.617 | DD=24.13% | Turnover=25.73%
   🎚️ Intra-Step TAPE: potential=0.6783 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0637 | critic_loss=1.2669 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6334 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=0.0027 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6169 | ema=0.9462 | best_ema=0.9462 | no_improve=0
   🔬 Alpha Diversity: mean=2.58 | std=2.17 | range=[1.24, 10.25] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.79 | AMZN=4.09 | CAT=3.46  BOT: NEE=1.51 | KO=1.38 | GLD=1.37
   🧬 FiLM: seq(dg=0.0005, db=0.0002, sat=0.0%) | latent(dg=0.0045, db=0.0023, sat=0.0%) | asset(dg=0.0010, db=0.0005, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=6 (18.8%), low_vol=18 (56.2%), medium_vol=8 (25.0%)
[CYCLE] Update 21/401 | Step 21,168/500,000 | Episode 16 | Time: 2127.7s
   📊 Metrics: Return=+18.73% | Sharpe=0.400 | DD=24.13% | Turnover=25.65%
   🎚️ Intra-Step TAPE: potential=0.2410 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0175 | critic_loss=1.1718 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5859 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0274
   🧠 Objective Experts: aux_loss=-0.0404 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3996 | ema=0.8915 | best_ema=0.8915 | no_improve=0
[CYCLE] Update 22/401 | Step 22,176/500,000 | Episode 16 | Time: 2228.9s
   📊 Metrics: Return=+27.18% | Sharpe=0.520 | DD=24.13% | Turnover=25.49%
   🎚️ Intra-Step TAPE: potential=0.7205 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0432 | critic_loss=0.8900 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4450 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=-0.0144 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5205 | ema=0.8544 | best_ema=0.8544 | no_improve=0
   🔬 Alpha Diversity: mean=2.60 | std=2.09 | range=[1.24, 10.19] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.46 | NVDA=4.39 | CAT=4.11  BOT: NEE=1.47 | KO=1.42 | GLD=1.36
   🧬 FiLM: seq(dg=0.0006, db=0.0003, sat=0.0%) | latent(dg=0.0049, db=0.0025, sat=0.0%) | asset(dg=0.0010, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=6 (18.8%), low_vol=18 (56.2%), medium_vol=8 (25.0%)
[CYCLE] Update 23/401 | Step 23,184/500,000 | Episode 16 | Time: 2330.0s
   📊 Metrics: Return=+34.96% | Sharpe=0.603 | DD=24.13% | Turnover=25.28%
   🎚️ Intra-Step TAPE: potential=0.7033 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0248 | critic_loss=1.7814 | mean_adv=-0.0008
   🧮 Loss Detail: critic_scaled=0.8907 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=-0.0315 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6035 | ema=0.8293 | best_ema=0.8293 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00018_shp1p287_actor.weights.h5 (Sharpe=1.287, MDD=21.05%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00019_shp0p913_actor.weights.h5 (Sharpe=0.913, MDD=12.90%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00021_shp1p146_actor.weights.h5 (Sharpe=1.146, MDD=18.34%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00025_shp1p312_actor.weights.h5 (Sharpe=1.312, MDD=13.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00026_shp1p543_actor.weights.h5 (Sharpe=1.543, MDD=10.50%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00028_shp0p973_actor.weights.h5 (Sharpe=0.973, MDD=12.98%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00029_shp1p373_actor.weights.h5 (Sharpe=1.373, MDD=20.07%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00030_shp1p195_actor.weights.h5 (Sharpe=1.195, MDD=11.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00031_shp0p970_actor.weights.h5 (Sharpe=0.970, MDD=13.64%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00032_shp1p665_actor.weights.h5 (Sharpe=1.665, MDD=11.75%)
[CYCLE] Update 24/401 | Step 24,192/500,000 | Episode 32 | Time: 2420.9s
   📊 Metrics: Return=+101.47% | Sharpe=1.665 | DD=11.75% | Turnover=24.81%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0661 | critic_loss=1.7869 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8935 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0272
   🧠 Objective Experts: aux_loss=0.0123 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6649 | ema=0.9129 | best_ema=0.9129 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=2.09 | range=[1.24, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=4.71 | NVDA=4.59 | AMZN=3.71  BOT: GLD=1.73 | KO=1.65 | NEE=1.46
   🧬 FiLM: seq(dg=0.0005, db=0.0002, sat=0.0%) | latent(dg=0.0053, db=0.0028, sat=0.0%) | asset(dg=0.0011, db=0.0006, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (20.8%), low_vol=25 (52.1%), medium_vol=13 (27.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6203
[CYCLE] Update 25/401 | Step 25,200/500,000 | Episode 32 | Time: 2521.4s
   📊 Metrics: Return=-5.17% | Sharpe=-1.316 | DD=10.88% | Turnover=25.63%
   🎚️ Intra-Step TAPE: potential=0.2268 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0043 | critic_loss=1.2800 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6400 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0271
   🧠 Objective Experts: aux_loss=-0.0609 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-1.3157 | ema=0.6900 | best_ema=0.6900 | no_improve=0
[CYCLE] Update 26/401 | Step 26,208/500,000 | Episode 32 | Time: 2622.4s
   📊 Metrics: Return=-9.36% | Sharpe=-0.632 | DD=21.71% | Turnover=25.31%
   🎚️ Intra-Step TAPE: potential=0.2416 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1129 | critic_loss=1.1132 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5566 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=0.0556 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.6318 | ema=0.5578 | best_ema=0.5578 | no_improve=0
   🔬 Alpha Diversity: mean=2.56 | std=2.17 | range=[1.24, 10.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.13 | AMZN=4.31 | CAT=3.24  BOT: KO=1.59 | BRK-B=1.53 | XOM=1.50
   🧬 FiLM: seq(dg=0.0006, db=0.0003, sat=0.0%) | latent(dg=0.0052, db=0.0027, sat=0.0%) | asset(dg=0.0012, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (20.8%), low_vol=25 (52.1%), medium_vol=13 (27.1%)
[CYCLE] Update 27/401 | Step 27,216/500,000 | Episode 32 | Time: 2723.5s
   📊 Metrics: Return=-10.42% | Sharpe=-0.472 | DD=21.71% | Turnover=24.57%
   🎚️ Intra-Step TAPE: potential=0.2465 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0233 | critic_loss=0.8718 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4359 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0271
   🧠 Objective Experts: aux_loss=-0.0291 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4723 | ema=0.4548 | best_ema=0.4548 | no_improve=0
[CYCLE] Update 28/401 | Step 28,224/500,000 | Episode 32 | Time: 2824.5s
   📊 Metrics: Return=-8.58% | Sharpe=-0.324 | DD=21.71% | Turnover=25.00%
   🎚️ Intra-Step TAPE: potential=0.2674 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0241 | critic_loss=0.8673 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4337 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0274
   🧠 Objective Experts: aux_loss=-0.0758 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3239 | ema=0.3769 | best_ema=0.3769 | no_improve=0
   🔬 Alpha Diversity: mean=2.58 | std=2.15 | range=[1.24, 10.44] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.77 | CAT=3.48 | AMZN=3.34  BOT: XOM=1.57 | KO=1.52 | BRK-B=1.50
   🧬 FiLM: seq(dg=0.0005, db=0.0003, sat=0.0%) | latent(dg=0.0056, db=0.0030, sat=0.0%) | asset(dg=0.0012, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (20.8%), low_vol=25 (52.1%), medium_vol=13 (27.1%)
[CYCLE] Update 29/401 | Step 29,232/500,000 | Episode 32 | Time: 2925.6s
   📊 Metrics: Return=-8.67% | Sharpe=-0.283 | DD=21.71% | Turnover=25.27%
   🎚️ Intra-Step TAPE: potential=0.2564 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0261 | critic_loss=1.0758 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5379 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0270
   🧠 Objective Experts: aux_loss=-0.0303 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2829 | ema=0.3110 | best_ema=0.3110 | no_improve=0
[CYCLE] Update 30/401 | Step 30,240/500,000 | Episode 32 | Time: 3026.6s
   📊 Metrics: Return=-5.01% | Sharpe=-0.138 | DD=21.71% | Turnover=25.24%
   🎚️ Intra-Step TAPE: potential=0.6243 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0376 | critic_loss=1.0220 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5110 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0271
   🧠 Objective Experts: aux_loss=-0.0172 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1381 | ema=0.2661 | best_ema=0.2661 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.22 | range=[1.24, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.73 | NVDA=4.66 | CAT=2.53  BOT: KO=1.77 | XOM=1.72 | BRK-B=1.62
   🧬 FiLM: seq(dg=0.0006, db=0.0003, sat=0.0%) | latent(dg=0.0050, db=0.0027, sat=0.0%) | asset(dg=0.0013, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (20.8%), low_vol=25 (52.1%), medium_vol=13 (27.1%)
[CYCLE] Update 31/401 | Step 31,248/500,000 | Episode 32 | Time: 3127.6s
   📊 Metrics: Return=-4.86% | Sharpe=-0.126 | DD=21.71% | Turnover=25.09%
   🎚️ Intra-Step TAPE: potential=0.5417 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0690 | critic_loss=0.8526 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4263 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=0.0186 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1255 | ema=0.2269 | best_ema=0.2269 | no_improve=0
[CYCLE] Update 32/401 | Step 32,256/500,000 | Episode 32 | Time: 3228.7s
   📊 Metrics: Return=-2.26% | Sharpe=-0.055 | DD=21.71% | Turnover=25.29%
   🎚️ Intra-Step TAPE: potential=0.2739 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0061 | critic_loss=1.1257 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5628 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=-0.0457 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0552 | ema=0.1987 | best_ema=0.1987 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=2.23 | range=[1.24, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.63 | AMZN=4.53 | CAT=3.25  BOT: NEE=1.66 | KO=1.58 | GLD=1.46
   🧬 FiLM: seq(dg=0.0007, db=0.0003, sat=0.0%) | latent(dg=0.0063, db=0.0033, sat=0.0%) | asset(dg=0.0013, db=0.0007, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (20.8%), low_vol=25 (52.1%), medium_vol=13 (27.1%)
[CYCLE] Update 33/401 | Step 33,264/500,000 | Episode 32 | Time: 3329.9s
   📊 Metrics: Return=-0.62% | Sharpe=-0.020 | DD=21.71% | Turnover=25.18%
   🎚️ Intra-Step TAPE: potential=0.2536 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0604 | critic_loss=1.1955 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5978 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0272
   🧠 Objective Experts: aux_loss=-0.1093 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0198 | ema=0.1768 | best_ema=0.1768 | no_improve=0
[CYCLE] Update 34/401 | Step 34,272/500,000 | Episode 32 | Time: 3430.9s
   📊 Metrics: Return=+1.51% | Sharpe=0.019 | DD=21.71% | Turnover=25.15%
   🎚️ Intra-Step TAPE: potential=0.4428 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0486 | critic_loss=0.8568 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4284 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.0061 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0189 | ema=0.1610 | best_ema=0.1610 | no_improve=0
   🔬 Alpha Diversity: mean=2.60 | std=2.15 | range=[1.24, 9.99] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.40 | AMZN=4.90 | CAT=1.99  BOT: KO=1.57 | XOM=1.35 | BRK-B=1.32
   🧬 FiLM: seq(dg=0.0007, db=0.0004, sat=0.0%) | latent(dg=0.0062, db=0.0032, sat=0.0%) | asset(dg=0.0014, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=10 (20.8%), low_vol=25 (52.1%), medium_vol=13 (27.1%)
[CYCLE] Update 35/401 | Step 35,280/500,000 | Episode 32 | Time: 3532.1s
   📊 Metrics: Return=+4.56% | Sharpe=0.070 | DD=21.71% | Turnover=25.30%
   🎚️ Intra-Step TAPE: potential=0.4933 | delta_reward=-0.0018
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0288 | critic_loss=0.7718 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.3859 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.0238 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0698 | ema=0.1519 | best_ema=0.1519 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00034_shp0p871_actor.weights.h5 (Sharpe=0.871, MDD=24.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00043_shp0p935_actor.weights.h5 (Sharpe=0.935, MDD=11.89%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00044_shp0p857_actor.weights.h5 (Sharpe=0.857, MDD=23.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00045_shp0p984_actor.weights.h5 (Sharpe=0.984, MDD=24.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00047_shp1p107_actor.weights.h5 (Sharpe=1.107, MDD=12.94%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00048_shp0p801_actor.weights.h5 (Sharpe=0.801, MDD=13.12%)
[CYCLE] Update 36/401 | Step 36,288/500,000 | Episode 48 | Time: 3620.7s
   📊 Metrics: Return=+44.83% | Sharpe=0.801 | DD=13.12% | Turnover=25.22%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0232 | critic_loss=2.2410 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.1205 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=-0.0277 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8005 | ema=0.2168 | best_ema=0.2168 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=2.15 | range=[1.24, 10.07] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.59 | AMZN=2.78 | MSFT=2.02  BOT: GLD=1.48 | XOM=1.38 | BRK-B=1.36
   🧬 FiLM: seq(dg=0.0007, db=0.0003, sat=0.0%) | latent(dg=0.0075, db=0.0038, sat=0.0%) | asset(dg=0.0013, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (26.6%), low_vol=29 (45.3%), medium_vol=18 (28.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4296
[CYCLE] Update 37/401 | Step 37,296/500,000 | Episode 48 | Time: 3721.2s
   📊 Metrics: Return=+16.39% | Sharpe=1.797 | DD=15.40% | Turnover=26.13%
   🎚️ Intra-Step TAPE: potential=0.6913 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0363 | critic_loss=2.0724 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=1.0362 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.0216 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7973 | ema=0.3748 | best_ema=0.3748 | no_improve=0
[CYCLE] Update 38/401 | Step 38,304/500,000 | Episode 48 | Time: 3822.2s
   📊 Metrics: Return=+23.27% | Sharpe=1.466 | DD=15.40% | Turnover=26.12%
   🎚️ Intra-Step TAPE: potential=0.5902 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0106 | critic_loss=1.1342 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5671 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0276
   🧠 Objective Experts: aux_loss=-0.0384 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4660 | ema=0.4840 | best_ema=0.4840 | no_improve=0
   🔬 Alpha Diversity: mean=2.58 | std=2.13 | range=[1.24, 10.34] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.40 | AMZN=4.14 | NEE=2.01  BOT: CAT=1.61 | XOM=1.47 | BRK-B=1.40
   🧬 FiLM: seq(dg=0.0008, db=0.0004, sat=0.0%) | latent(dg=0.0077, db=0.0039, sat=0.0%) | asset(dg=0.0015, db=0.0008, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (26.6%), low_vol=29 (45.3%), medium_vol=18 (28.1%)
[CYCLE] Update 39/401 | Step 39,312/500,000 | Episode 48 | Time: 3923.3s
   📊 Metrics: Return=+38.85% | Sharpe=1.727 | DD=15.40% | Turnover=26.22%
   🎚️ Intra-Step TAPE: potential=0.7268 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0063 | critic_loss=1.4550 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7275 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0276
   🧠 Objective Experts: aux_loss=-0.0465 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7266 | ema=0.6082 | best_ema=0.6082 | no_improve=0
[CYCLE] Update 40/401 | Step 40,320/500,000 | Episode 48 | Time: 4024.7s
   📊 Metrics: Return=+49.83% | Sharpe=1.758 | DD=15.40% | Turnover=26.49%
   🎚️ Intra-Step TAPE: potential=0.7312 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0195 | critic_loss=1.2985 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6492 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0278
   🧠 Objective Experts: aux_loss=-0.0653 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7584 | ema=0.7232 | best_ema=0.7232 | no_improve=0
   🔬 Alpha Diversity: mean=2.60 | std=2.06 | range=[1.23, 10.17] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.15 | NVDA=3.89 | GLD=2.50  BOT: JPM=1.58 | BRK-B=1.49 | XOM=1.48
   🧬 FiLM: seq(dg=0.0010, db=0.0005, sat=0.0%) | latent(dg=0.0080, db=0.0041, sat=0.0%) | asset(dg=0.0015, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (26.6%), low_vol=29 (45.3%), medium_vol=18 (28.1%)
[CYCLE] Update 41/401 | Step 41,328/500,000 | Episode 48 | Time: 4125.8s
   📊 Metrics: Return=+55.38% | Sharpe=1.631 | DD=15.40% | Turnover=26.42%
   🎚️ Intra-Step TAPE: potential=0.6080 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0113 | critic_loss=1.1568 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5784 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=-0.0610 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6312 | ema=0.8140 | best_ema=0.8140 | no_improve=0
[CYCLE] Update 42/401 | Step 42,336/500,000 | Episode 48 | Time: 4226.6s
   📊 Metrics: Return=+33.43% | Sharpe=0.864 | DD=19.85% | Turnover=26.18%
   🎚️ Intra-Step TAPE: potential=0.2310 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0002 | critic_loss=0.7718 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3859 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0274
   🧠 Objective Experts: aux_loss=-0.0479 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8641 | ema=0.8191 | best_ema=0.8191 | no_improve=0
   🔬 Alpha Diversity: mean=2.57 | std=2.11 | range=[1.23, 10.37] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.46 | AMZN=2.74 | CAT=2.49  BOT: KO=1.83 | XOM=1.74 | BRK-B=1.68
   🧬 FiLM: seq(dg=0.0009, db=0.0005, sat=0.0%) | latent(dg=0.0091, db=0.0048, sat=0.0%) | asset(dg=0.0016, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (26.6%), low_vol=29 (45.3%), medium_vol=18 (28.1%)
[CYCLE] Update 43/401 | Step 43,344/500,000 | Episode 48 | Time: 4327.5s
   📊 Metrics: Return=+44.22% | Sharpe=0.965 | DD=19.85% | Turnover=26.05%
   🎚️ Intra-Step TAPE: potential=0.6389 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0093 | critic_loss=0.8795 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4398 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=-0.0556 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9653 | ema=0.8337 | best_ema=0.8337 | no_improve=0
[CYCLE] Update 44/401 | Step 44,352/500,000 | Episode 48 | Time: 4428.6s
   📊 Metrics: Return=+67.85% | Sharpe=1.239 | DD=19.85% | Turnover=26.11%
   🎚️ Intra-Step TAPE: potential=0.7558 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0438 | critic_loss=0.8847 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4424 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=-0.0897 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2389 | ema=0.8742 | best_ema=0.8742 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=2.10 | range=[1.23, 10.34] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.78 | NVDA=3.60 | GLD=2.16  BOT: MSFT=1.82 | XOM=1.61 | BRK-B=1.52
   🧬 FiLM: seq(dg=0.0011, db=0.0006, sat=0.0%) | latent(dg=0.0104, db=0.0054, sat=0.0%) | asset(dg=0.0016, db=0.0009, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (26.6%), low_vol=29 (45.3%), medium_vol=18 (28.1%)
[CYCLE] Update 45/401 | Step 45,360/500,000 | Episode 48 | Time: 4529.5s
   📊 Metrics: Return=+63.17% | Sharpe=1.064 | DD=19.85% | Turnover=26.37%
   🎚️ Intra-Step TAPE: potential=0.2327 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0005 | critic_loss=0.9851 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4925 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0275
   🧠 Objective Experts: aux_loss=-0.0506 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0643 | ema=0.8932 | best_ema=0.8932 | no_improve=0
[CYCLE] Update 46/401 | Step 46,368/500,000 | Episode 48 | Time: 4630.7s
   📊 Metrics: Return=+52.16% | Sharpe=0.835 | DD=19.85% | Turnover=26.21%
   🎚️ Intra-Step TAPE: potential=0.2247 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0111 | critic_loss=0.9306 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4653 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0277
   🧠 Objective Experts: aux_loss=-0.0379 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8351 | ema=0.8874 | best_ema=0.8874 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=1.92 | range=[1.23, 10.45] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.85 | AMZN=3.47 | NEE=2.61  BOT: XOM=1.81 | MSFT=1.72 | BRK-B=1.67
   🧬 FiLM: seq(dg=0.0012, db=0.0007, sat=0.0%) | latent(dg=0.0116, db=0.0062, sat=0.0%) | asset(dg=0.0016, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=17 (26.6%), low_vol=29 (45.3%), medium_vol=18 (28.1%)
[CYCLE] Update 47/401 | Step 47,376/500,000 | Episode 48 | Time: 4731.7s
   📊 Metrics: Return=+52.38% | Sharpe=0.721 | DD=23.28% | Turnover=26.20%
   🎚️ Intra-Step TAPE: potential=0.2402 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0041 | critic_loss=0.9160 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.4580 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0276
   🧠 Objective Experts: aux_loss=-0.0433 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7211 | ema=0.8708 | best_ema=0.8708 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00050_shp0p730_actor.weights.h5 (Sharpe=0.730, MDD=19.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00052_shp1p615_actor.weights.h5 (Sharpe=1.615, MDD=12.18%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00057_shp1p633_actor.weights.h5 (Sharpe=1.633, MDD=18.92%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00059_shp1p202_actor.weights.h5 (Sharpe=1.202, MDD=11.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00060_shp0p706_actor.weights.h5 (Sharpe=0.706, MDD=21.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00061_shp0p821_actor.weights.h5 (Sharpe=0.821, MDD=9.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00062_shp0p807_actor.weights.h5 (Sharpe=0.807, MDD=10.70%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00063_shp1p330_actor.weights.h5 (Sharpe=1.330, MDD=9.39%)
[CYCLE] Update 48/401 | Step 48,384/500,000 | Episode 64 | Time: 4821.3s
   📊 Metrics: Return=+12.66% | Sharpe=0.207 | DD=15.66% | Turnover=25.89%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0334 | critic_loss=2.7839 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.3919 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0273
   🧠 Objective Experts: aux_loss=-0.0798 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2069 | ema=0.8044 | best_ema=0.8044 | no_improve=0
   🔬 Alpha Diversity: mean=2.60 | std=2.17 | range=[1.24, 10.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.88 | AMZN=3.80 | CAT=2.60  BOT: BRK-B=1.44 | XOM=1.41 | KO=1.40
   🧬 FiLM: seq(dg=0.0014, db=0.0007, sat=0.0%) | latent(dg=0.0148, db=0.0076, sat=0.0%) | asset(dg=0.0017, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (23.8%), low_vol=37 (46.2%), medium_vol=24 (30.0%)
   🔒 Drawdown λ snapshot=0.054 (peak 0.054, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2608
[CYCLE] Update 49/401 | Step 49,392/500,000 | Episode 64 | Time: 4921.7s
   📊 Metrics: Return=+3.98% | Sharpe=1.216 | DD=3.74% | Turnover=26.18%
   🎚️ Intra-Step TAPE: potential=0.4851 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0186 | critic_loss=1.1501 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5750 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0271
   🧠 Objective Experts: aux_loss=-0.0318 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2158 | ema=0.8455 | best_ema=0.8455 | no_improve=0
[CYCLE] Update 50/401 | Step 50,400/500,000 | Episode 64 | Time: 5022.7s
   📊 Metrics: Return=+17.60% | Sharpe=2.312 | DD=5.14% | Turnover=24.83%
   🎚️ Intra-Step TAPE: potential=0.7549 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0120 | critic_loss=1.1063 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5532 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=-0.0529 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3123 | ema=0.9922 | best_ema=0.9922 | no_improve=0
   🔬 Alpha Diversity: mean=2.59 | std=2.21 | range=[1.26, 10.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.96 | AMZN=4.03 | MSFT=2.24  BOT: XOM=1.38 | BRK-B=1.38 | KO=1.36
   🧬 FiLM: seq(dg=0.0016, db=0.0008, sat=0.0%) | latent(dg=0.0171, db=0.0086, sat=0.0%) | asset(dg=0.0018, db=0.0010, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (23.8%), low_vol=37 (46.2%), medium_vol=24 (30.0%)
[CYCLE] Update 51/401 | Step 51,408/500,000 | Episode 64 | Time: 5123.7s
   📊 Metrics: Return=+24.77% | Sharpe=2.166 | DD=5.14% | Turnover=24.54%
   🎚️ Intra-Step TAPE: potential=0.6610 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0510 | critic_loss=1.1499 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.5750 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=-0.0967 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1664 | ema=1.1096 | best_ema=1.1096 | no_improve=0
[CYCLE] Update 52/401 | Step 52,416/500,000 | Episode 64 | Time: 5224.5s
   📊 Metrics: Return=+36.37% | Sharpe=2.364 | DD=5.14% | Turnover=24.54%
   🎚️ Intra-Step TAPE: potential=0.7160 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0577 | critic_loss=0.9351 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4675 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0272
   🧠 Objective Experts: aux_loss=-0.1038 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3642 | ema=1.2351 | best_ema=1.2351 | no_improve=0
   🔬 Alpha Diversity: mean=2.56 | std=2.15 | range=[1.23, 10.46] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.87 | AMZN=4.44 | NEE=2.22  BOT: GLD=1.79 | BRK-B=1.60 | XOM=1.55
   🧬 FiLM: seq(dg=0.0018, db=0.0010, sat=0.0%) | latent(dg=0.0184, db=0.0096, sat=0.0%) | asset(dg=0.0019, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (23.8%), low_vol=37 (46.2%), medium_vol=24 (30.0%)
[CYCLE] Update 53/401 | Step 53,424/500,000 | Episode 64 | Time: 5325.5s
   📊 Metrics: Return=+51.86% | Sharpe=2.441 | DD=8.01% | Turnover=24.72%
   🎚️ Intra-Step TAPE: potential=0.7102 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0616 | critic_loss=0.7237 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3618 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0272
   🧠 Objective Experts: aux_loss=-0.1025 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4408 | ema=1.3557 | best_ema=1.3557 | no_improve=0
[CYCLE] Update 54/401 | Step 54,432/500,000 | Episode 64 | Time: 5426.6s
   📊 Metrics: Return=+49.73% | Sharpe=1.966 | DD=8.01% | Turnover=25.41%
   🎚️ Intra-Step TAPE: potential=0.2372 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0127 | critic_loss=0.8837 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4419 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=-0.0594 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.9656 | ema=1.4166 | best_ema=1.4166 | no_improve=0
   🔬 Alpha Diversity: mean=2.58 | std=2.25 | range=[1.25, 10.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.50 | AMZN=3.02 | JPM=1.95  BOT: KO=1.46 | XOM=1.38 | BRK-B=1.37
   🧬 FiLM: seq(dg=0.0020, db=0.0011, sat=0.0%) | latent(dg=0.0201, db=0.0106, sat=0.0%) | asset(dg=0.0019, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (23.8%), low_vol=37 (46.2%), medium_vol=24 (30.0%)
[CYCLE] Update 55/401 | Step 55,440/500,000 | Episode 64 | Time: 5527.7s
   📊 Metrics: Return=+50.12% | Sharpe=1.779 | DD=8.01% | Turnover=25.68%
   🎚️ Intra-Step TAPE: potential=0.2605 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0505 | critic_loss=0.7886 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3943 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0265
   🧠 Objective Experts: aux_loss=-0.0971 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7786 | ema=1.4528 | best_ema=1.4528 | no_improve=0
[CYCLE] Update 56/401 | Step 56,448/500,000 | Episode 64 | Time: 5628.8s
   📊 Metrics: Return=+34.84% | Sharpe=0.979 | DD=13.89% | Turnover=25.78%
   🎚️ Intra-Step TAPE: potential=0.2255 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0350 | critic_loss=1.1766 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5883 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0270
   🧠 Objective Experts: aux_loss=-0.0817 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9787 | ema=1.4054 | best_ema=1.4054 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.04 | range=[1.23, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.70 | AMZN=4.49 | CAT=3.01  BOT: NEE=1.71 | XOM=1.70 | BRK-B=1.67
   🧬 FiLM: seq(dg=0.0022, db=0.0011, sat=0.0%) | latent(dg=0.0235, db=0.0123, sat=0.0%) | asset(dg=0.0019, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (23.8%), low_vol=37 (46.2%), medium_vol=24 (30.0%)
[CYCLE] Update 57/401 | Step 57,456/500,000 | Episode 64 | Time: 5729.9s
   📊 Metrics: Return=+40.98% | Sharpe=0.909 | DD=22.05% | Turnover=25.50%
   🎚️ Intra-Step TAPE: potential=0.5847 | delta_reward=+0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0175 | critic_loss=0.8014 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4007 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0264
   🧠 Objective Experts: aux_loss=-0.0285 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9094 | ema=1.3558 | best_ema=1.3558 | no_improve=0
[CYCLE] Update 58/401 | Step 58,464/500,000 | Episode 64 | Time: 5831.1s
   📊 Metrics: Return=+39.85% | Sharpe=0.802 | DD=22.05% | Turnover=25.25%
   🎚️ Intra-Step TAPE: potential=0.2359 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0641 | critic_loss=0.9493 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4746 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.1103 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8017 | ema=1.3004 | best_ema=1.3004 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=2.12 | range=[1.23, 10.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.19 | AMZN=4.46 | CAT=2.49  BOT: MSFT=1.86 | BRK-B=1.65 | GLD=1.51
   🧬 FiLM: seq(dg=0.0026, db=0.0014, sat=0.0%) | latent(dg=0.0262, db=0.0138, sat=0.0%) | asset(dg=0.0019, db=0.0011, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=19 (23.8%), low_vol=37 (46.2%), medium_vol=24 (30.0%)
[CYCLE] Update 59/401 | Step 59,472/500,000 | Episode 64 | Time: 5932.3s
   📊 Metrics: Return=+47.74% | Sharpe=0.870 | DD=22.05% | Turnover=25.32%
   🎚️ Intra-Step TAPE: potential=0.5642 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0392 | critic_loss=1.0903 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5451 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0272
   🧠 Objective Experts: aux_loss=-0.0857 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8699 | ema=1.2574 | best_ema=1.2574 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00065_shp0p916_actor.weights.h5 (Sharpe=0.916, MDD=22.05%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00067_shp0p877_actor.weights.h5 (Sharpe=0.877, MDD=12.74%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00070_shp1p189_actor.weights.h5 (Sharpe=1.189, MDD=11.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00073_shp1p986_actor.weights.h5 (Sharpe=1.986, MDD=12.05%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00074_shp0p836_actor.weights.h5 (Sharpe=0.836, MDD=10.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00075_shp1p934_actor.weights.h5 (Sharpe=1.934, MDD=11.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00076_shp0p820_actor.weights.h5 (Sharpe=0.820, MDD=11.69%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00077_shp1p674_actor.weights.h5 (Sharpe=1.674, MDD=10.39%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00078_shp1p924_actor.weights.h5 (Sharpe=1.924, MDD=11.44%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00080_shp1p816_actor.weights.h5 (Sharpe=1.816, MDD=10.93%)
[CYCLE] Update 60/401 | Step 60,480/500,000 | Episode 80 | Time: 6023.1s
   📊 Metrics: Return=+114.62% | Sharpe=1.816 | DD=10.93% | Turnover=25.60%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0622 | critic_loss=2.9748 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.4874 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=-0.1082 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.8160 | ema=1.3132 | best_ema=1.3132 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.02 | range=[1.23, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.57 | CAT=3.49 | AMZN=2.98  BOT: XOM=2.00 | GLD=1.94 | BRK-B=1.63
   🧬 FiLM: seq(dg=0.0029, db=0.0016, sat=0.0%) | latent(dg=0.0289, db=0.0155, sat=0.0%) | asset(dg=0.0020, db=0.0012, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=27 (28.1%), low_vol=40 (41.7%), medium_vol=29 (30.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6577
[CYCLE] Update 61/401 | Step 61,488/500,000 | Episode 80 | Time: 6123.5s
   📊 Metrics: Return=-13.13% | Sharpe=-1.855 | DD=16.16% | Turnover=24.39%
   🎚️ Intra-Step TAPE: potential=0.2401 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0549 | critic_loss=1.7878 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8939 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=0.0077 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-1.8548 | ema=0.9964 | best_ema=0.9964 | no_improve=0
[CYCLE] Update 62/401 | Step 62,496/500,000 | Episode 80 | Time: 6224.8s
   📊 Metrics: Return=-2.88% | Sharpe=-0.212 | DD=16.16% | Turnover=25.24%
   🎚️ Intra-Step TAPE: potential=0.7075 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0203 | critic_loss=0.9980 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4990 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0265
   🧠 Objective Experts: aux_loss=-0.0255 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2124 | ema=0.8755 | best_ema=0.8755 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=2.27 | range=[1.23, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.57 | AMZN=4.79 | JPM=2.29  BOT: KO=1.51 | BRK-B=1.45 | XOM=1.44
   🧬 FiLM: seq(dg=0.0029, db=0.0016, sat=0.0%) | latent(dg=0.0268, db=0.0144, sat=0.0%) | asset(dg=0.0022, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=27 (28.1%), low_vol=40 (41.7%), medium_vol=29 (30.2%)
[CYCLE] Update 63/401 | Step 63,504/500,000 | Episode 80 | Time: 6325.8s
   📊 Metrics: Return=+19.04% | Sharpe=1.079 | DD=16.16% | Turnover=25.48%
   🎚️ Intra-Step TAPE: potential=0.7542 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1023 | critic_loss=1.0591 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5296 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0266
   🧠 Objective Experts: aux_loss=-0.1480 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0786 | ema=0.8958 | best_ema=0.8958 | no_improve=0
[CYCLE] Update 64/401 | Step 64,512/500,000 | Episode 80 | Time: 6427.3s
   📊 Metrics: Return=+19.02% | Sharpe=0.845 | DD=16.16% | Turnover=25.84%
   🎚️ Intra-Step TAPE: potential=0.2315 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0534 | critic_loss=0.8921 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4461 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0268
   🧠 Objective Experts: aux_loss=-0.0992 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8449 | ema=0.8908 | best_ema=0.8908 | no_improve=0
   🔬 Alpha Diversity: mean=2.57 | std=2.11 | range=[1.22, 10.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.47 | NEE=2.55 | AMZN=2.50  BOT: JPM=1.67 | BRK-B=1.63 | MSFT=1.58
   🧬 FiLM: seq(dg=0.0029, db=0.0017, sat=0.0%) | latent(dg=0.0304, db=0.0164, sat=0.0%) | asset(dg=0.0023, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=27 (28.1%), low_vol=40 (41.7%), medium_vol=29 (30.2%)
[CYCLE] Update 65/401 | Step 65,520/500,000 | Episode 80 | Time: 6528.3s
   📊 Metrics: Return=+6.18% | Sharpe=0.241 | DD=16.16% | Turnover=26.16%
   🎚️ Intra-Step TAPE: potential=0.2298 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0234 | critic_loss=1.0620 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5310 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0266
   🧠 Objective Experts: aux_loss=-0.0689 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2407 | ema=0.8258 | best_ema=0.8258 | no_improve=0
[CYCLE] Update 66/401 | Step 66,528/500,000 | Episode 80 | Time: 6629.8s
   📊 Metrics: Return=+11.88% | Sharpe=0.351 | DD=23.66% | Turnover=26.24%
   🎚️ Intra-Step TAPE: potential=0.3454 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0707 | critic_loss=0.9162 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4581 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0258
   🧠 Objective Experts: aux_loss=-0.1157 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3508 | ema=0.7783 | best_ema=0.7783 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.28 | range=[1.23, 10.53] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=8.06 | AMZN=3.18 | CAT=2.47  BOT: BRK-B=1.47 | KO=1.44 | XOM=1.41
   🧬 FiLM: seq(dg=0.0034, db=0.0018, sat=0.0%) | latent(dg=0.0346, db=0.0183, sat=0.0%) | asset(dg=0.0023, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=27 (28.1%), low_vol=40 (41.7%), medium_vol=29 (30.2%)
[CYCLE] Update 67/401 | Step 67,536/500,000 | Episode 80 | Time: 6730.7s
   📊 Metrics: Return=+12.66% | Sharpe=0.322 | DD=23.66% | Turnover=26.18%
   🎚️ Intra-Step TAPE: potential=0.5525 | delta_reward=+0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0097 | critic_loss=0.8646 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4323 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0549 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3221 | ema=0.7326 | best_ema=0.7326 | no_improve=0
[CYCLE] Update 68/401 | Step 68,544/500,000 | Episode 80 | Time: 6831.5s
   📊 Metrics: Return=+18.85% | Sharpe=0.407 | DD=23.66% | Turnover=26.27%
   🎚️ Intra-Step TAPE: potential=0.6646 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0141 | critic_loss=0.8304 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4152 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0258
   🧠 Objective Experts: aux_loss=-0.0590 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4068 | ema=0.7001 | best_ema=0.7001 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.33 | range=[1.24, 10.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.47 | AMZN=3.83 | CAT=2.11  BOT: KO=1.40 | MSFT=1.39 | XOM=1.38
   🧬 FiLM: seq(dg=0.0040, db=0.0021, sat=0.0%) | latent(dg=0.0387, db=0.0205, sat=0.0%) | asset(dg=0.0024, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=27 (28.1%), low_vol=40 (41.7%), medium_vol=29 (30.2%)
[CYCLE] Update 69/401 | Step 69,552/500,000 | Episode 80 | Time: 6932.3s
   📊 Metrics: Return=+18.07% | Sharpe=0.355 | DD=23.66% | Turnover=26.06%
   🎚️ Intra-Step TAPE: potential=0.2617 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0714 | critic_loss=0.6191 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3095 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0267
   🧠 Objective Experts: aux_loss=-0.1170 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3555 | ema=0.6656 | best_ema=0.6656 | no_improve=0
[CYCLE] Update 70/401 | Step 70,560/500,000 | Episode 80 | Time: 7033.4s
   📊 Metrics: Return=+12.75% | Sharpe=0.239 | DD=23.66% | Turnover=26.21%
   🎚️ Intra-Step TAPE: potential=0.2417 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0139 | critic_loss=0.6833 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3416 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0270
   🧠 Objective Experts: aux_loss=-0.0595 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2389 | ema=0.6229 | best_ema=0.6229 | no_improve=0
   🔬 Alpha Diversity: mean=2.58 | std=1.98 | range=[1.22, 10.39] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.19 | NEE=2.90 | AMZN=2.65  BOT: BRK-B=1.80 | MSFT=1.79 | CAT=1.54
   🧬 FiLM: seq(dg=0.0036, db=0.0021, sat=0.0%) | latent(dg=0.0410, db=0.0224, sat=0.0%) | asset(dg=0.0024, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=27 (28.1%), low_vol=40 (41.7%), medium_vol=29 (30.2%)
[CYCLE] Update 71/401 | Step 71,568/500,000 | Episode 80 | Time: 7134.8s
   📊 Metrics: Return=+14.55% | Sharpe=0.247 | DD=23.66% | Turnover=26.26%
   🎚️ Intra-Step TAPE: potential=0.2542 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0101 | critic_loss=0.4697 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2349 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.0354 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2470 | ema=0.5853 | best_ema=0.5853 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00082_shp1p752_actor.weights.h5 (Sharpe=1.752, MDD=12.27%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00086_shp1p648_actor.weights.h5 (Sharpe=1.648, MDD=12.67%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00089_shp0p801_actor.weights.h5 (Sharpe=0.801, MDD=12.72%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00090_shp1p801_actor.weights.h5 (Sharpe=1.801, MDD=11.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00096_shp1p161_actor.weights.h5 (Sharpe=1.161, MDD=20.32%)
[CYCLE] Update 72/401 | Step 72,576/500,000 | Episode 96 | Time: 7222.7s
   📊 Metrics: Return=+72.00% | Sharpe=1.161 | DD=20.32% | Turnover=25.33%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0960 | critic_loss=1.6762 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8381 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.1415 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1615 | ema=0.6430 | best_ema=0.6430 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=2.17 | range=[1.22, 10.45] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.86 | AMZN=2.74 | NEE=2.20  BOT: BRK-B=1.56 | CAT=1.51 | GLD=1.48
   🧬 FiLM: seq(dg=0.0034, db=0.0020, sat=0.0%) | latent(dg=0.0395, db=0.0215, sat=0.0%) | asset(dg=0.0023, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=31 (27.7%), low_vol=47 (42.0%), medium_vol=34 (30.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.009) | TAPE=0.5255
[CYCLE] Update 73/401 | Step 73,584/500,000 | Episode 96 | Time: 7323.2s
   📊 Metrics: Return=+20.92% | Sharpe=4.366 | DD=2.34% | Turnover=25.86%
   🎚️ Intra-Step TAPE: potential=0.7557 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0342 | critic_loss=1.3806 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6903 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0263
   🧠 Objective Experts: aux_loss=-0.0798 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=4.3662 | ema=1.0153 | best_ema=1.0153 | no_improve=0
[CYCLE] Update 74/401 | Step 74,592/500,000 | Episode 96 | Time: 7423.7s
   📊 Metrics: Return=+16.08% | Sharpe=1.658 | DD=12.99% | Turnover=25.32%
   🎚️ Intra-Step TAPE: potential=0.2295 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0298 | critic_loss=0.8477 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4238 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0264
   🧠 Objective Experts: aux_loss=-0.0749 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6584 | ema=1.0796 | best_ema=1.0796 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=1.96 | range=[1.22, 10.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.03 | AMZN=4.24 | JPM=2.25  BOT: KO=1.96 | XOM=1.95 | GLD=1.83
   🧬 FiLM: seq(dg=0.0041, db=0.0023, sat=0.0%) | latent(dg=0.0455, db=0.0246, sat=0.0%) | asset(dg=0.0025, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=31 (27.7%), low_vol=47 (42.0%), medium_vol=34 (30.4%)
[CYCLE] Update 75/401 | Step 75,600/500,000 | Episode 96 | Time: 7524.6s
   📊 Metrics: Return=-4.57% | Sharpe=-0.335 | DD=22.91% | Turnover=25.52%
   🎚️ Intra-Step TAPE: potential=0.2120 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0450 | critic_loss=0.6465 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3233 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0269
   🧠 Objective Experts: aux_loss=-0.0902 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3352 | ema=0.9381 | best_ema=0.9381 | no_improve=0
[CYCLE] Update 76/401 | Step 76,608/500,000 | Episode 96 | Time: 7625.8s
   📊 Metrics: Return=+4.64% | Sharpe=0.226 | DD=24.86% | Turnover=25.73%
   🎚️ Intra-Step TAPE: potential=0.3545 | delta_reward=-0.0021
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1295 | critic_loss=0.5207 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2603 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0266
   🧠 Objective Experts: aux_loss=-0.1744 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2260 | ema=0.8669 | best_ema=0.8669 | no_improve=0
   🔬 Alpha Diversity: mean=2.56 | std=2.10 | range=[1.22, 10.28] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.58 | AMZN=3.01 | CAT=2.47  BOT: BRK-B=1.81 | KO=1.64 | XOM=1.49
   🧬 FiLM: seq(dg=0.0038, db=0.0024, sat=0.0%) | latent(dg=0.0441, db=0.0245, sat=0.0%) | asset(dg=0.0022, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=31 (27.7%), low_vol=47 (42.0%), medium_vol=34 (30.4%)
[CYCLE] Update 77/401 | Step 77,616/500,000 | Episode 96 | Time: 7726.8s
   📊 Metrics: Return=+4.75% | Sharpe=0.191 | DD=24.86% | Turnover=25.81%
   🎚️ Intra-Step TAPE: potential=0.3370 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0478 | critic_loss=0.6641 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3321 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0264
   🧠 Objective Experts: aux_loss=-0.0928 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1906 | ema=0.7993 | best_ema=0.7993 | no_improve=0
[CYCLE] Update 78/401 | Step 78,624/500,000 | Episode 96 | Time: 7827.7s
   📊 Metrics: Return=+6.29% | Sharpe=0.204 | DD=24.86% | Turnover=25.75%
   🎚️ Intra-Step TAPE: potential=0.3275 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0125 | critic_loss=0.7270 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3635 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.0564 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2044 | ema=0.7398 | best_ema=0.7398 | no_improve=0
   🔬 Alpha Diversity: mean=2.53 | std=2.33 | range=[1.26, 10.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.15 | AMZN=5.16 | CAT=2.10  BOT: NEE=1.40 | XOM=1.39 | KO=1.34
   🧬 FiLM: seq(dg=0.0049, db=0.0026, sat=0.0%) | latent(dg=0.0479, db=0.0260, sat=0.0%) | asset(dg=0.0024, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=31 (27.7%), low_vol=47 (42.0%), medium_vol=34 (30.4%)
[CYCLE] Update 79/401 | Step 79,632/500,000 | Episode 96 | Time: 7928.5s
   📊 Metrics: Return=+6.64% | Sharpe=0.186 | DD=24.86% | Turnover=25.66%
   🎚️ Intra-Step TAPE: potential=0.2627 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0226 | critic_loss=0.8059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4029 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.0658 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1857 | ema=0.6844 | best_ema=0.6844 | no_improve=0
[CYCLE] Update 80/401 | Step 80,640/500,000 | Episode 96 | Time: 8029.7s
   📊 Metrics: Return=+2.35% | Sharpe=0.062 | DD=24.86% | Turnover=25.81%
   🎚️ Intra-Step TAPE: potential=0.2382 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0454 | critic_loss=0.6781 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3391 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0263
   🧠 Objective Experts: aux_loss=-0.0897 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0615 | ema=0.6221 | best_ema=0.6221 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=1.96 | range=[1.22, 10.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.14 | AMZN=3.32 | NEE=2.41  BOT: JPM=1.88 | BRK-B=1.87 | MSFT=1.78
   🧬 FiLM: seq(dg=0.0051, db=0.0029, sat=0.0%) | latent(dg=0.0533, db=0.0293, sat=0.0%) | asset(dg=0.0024, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=31 (27.7%), low_vol=47 (42.0%), medium_vol=34 (30.4%)
[CYCLE] Update 81/401 | Step 81,648/500,000 | Episode 96 | Time: 8130.6s
   📊 Metrics: Return=+4.70% | Sharpe=0.101 | DD=24.86% | Turnover=25.91%
   🎚️ Intra-Step TAPE: potential=0.6543 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1637 | critic_loss=0.9481 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4740 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0265
   🧠 Objective Experts: aux_loss=-0.2082 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1006 | ema=0.5699 | best_ema=0.5699 | no_improve=0
[CYCLE] Update 82/401 | Step 82,656/500,000 | Episode 96 | Time: 8231.3s
   📊 Metrics: Return=+7.61% | Sharpe=0.144 | DD=24.86% | Turnover=26.06%
   🎚️ Intra-Step TAPE: potential=0.5702 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0711 | critic_loss=1.1859 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5929 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0264
   🧠 Objective Experts: aux_loss=-0.1156 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1442 | ema=0.5274 | best_ema=0.5274 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=2.12 | range=[1.22, 10.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.99 | NVDA=2.84 | CAT=2.29  BOT: JPM=1.79 | XOM=1.73 | MSFT=1.53
   🧬 FiLM: seq(dg=0.0041, db=0.0027, sat=0.0%) | latent(dg=0.0494, db=0.0278, sat=0.0%) | asset(dg=0.0023, db=0.0013, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=31 (27.7%), low_vol=47 (42.0%), medium_vol=34 (30.4%)
[CYCLE] Update 83/401 | Step 83,664/500,000 | Episode 96 | Time: 8331.9s
   📊 Metrics: Return=+8.01% | Sharpe=0.135 | DD=24.86% | Turnover=26.04%
   🎚️ Intra-Step TAPE: potential=0.2311 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1344 | critic_loss=0.6342 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3171 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0264
   🧠 Objective Experts: aux_loss=-0.1787 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1354 | ema=0.4882 | best_ema=0.4882 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00099_shp0p876_actor.weights.h5 (Sharpe=0.876, MDD=12.51%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00100_shp0p921_actor.weights.h5 (Sharpe=0.921, MDD=12.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00105_shp1p063_actor.weights.h5 (Sharpe=1.063, MDD=11.92%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00106_shp1p572_actor.weights.h5 (Sharpe=1.572, MDD=11.16%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00108_shp0p933_actor.weights.h5 (Sharpe=0.933, MDD=20.29%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00109_shp1p396_actor.weights.h5 (Sharpe=1.396, MDD=19.73%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00111_shp0p753_actor.weights.h5 (Sharpe=0.753, MDD=12.68%)
[CYCLE] Update 84/401 | Step 84,672/500,000 | Episode 112 | Time: 8421.2s
   📊 Metrics: Return=+84.09% | Sharpe=0.909 | DD=26.44% | Turnover=25.52%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0113 | critic_loss=2.2403 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.1202 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.0321 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8749 | ema=0.5268 | best_ema=0.5268 | no_improve=0
   🔬 Alpha Diversity: mean=2.50 | std=2.10 | range=[1.22, 10.46] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.77 | CAT=3.05 | AMZN=2.75  BOT: GLD=1.75 | KO=1.75 | MSFT=1.65
   🧬 FiLM: seq(dg=0.0057, db=0.0031, sat=0.0%) | latent(dg=0.0554, db=0.0305, sat=0.0%) | asset(dg=0.0025, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (27.3%), low_vol=53 (41.4%), medium_vol=40 (31.2%)
   🔒 Drawdown λ snapshot=0.126 (peak 0.126, dd 0.00% / trig 16.50%) | terminal=0.257 (peak 0.273) | TAPE=0.4753
[CYCLE] Update 85/401 | Step 85,680/500,000 | Episode 112 | Time: 8521.8s
   📊 Metrics: Return=+4.64% | Sharpe=1.408 | DD=6.64% | Turnover=27.80%
   🎚️ Intra-Step TAPE: potential=0.5516 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0004 | critic_loss=1.1175 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5587 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.0443 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4079 | ema=0.6149 | best_ema=0.6149 | no_improve=0
[CYCLE] Update 86/401 | Step 86,688/500,000 | Episode 112 | Time: 8622.7s
   📊 Metrics: Return=+3.57% | Sharpe=0.485 | DD=8.97% | Turnover=27.11%
   🎚️ Intra-Step TAPE: potential=0.2376 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0315 | critic_loss=0.5031 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2516 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.0752 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4850 | ema=0.6019 | best_ema=0.6019 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=2.22 | range=[1.22, 10.38] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.01 | AMZN=3.85 | XOM=2.00  BOT: JPM=1.65 | KO=1.63 | BRK-B=1.57
   🧬 FiLM: seq(dg=0.0056, db=0.0031, sat=0.0%) | latent(dg=0.0537, db=0.0297, sat=0.0%) | asset(dg=0.0027, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (27.3%), low_vol=53 (41.4%), medium_vol=40 (31.2%)
[CYCLE] Update 87/401 | Step 87,696/500,000 | Episode 112 | Time: 8723.9s
   📊 Metrics: Return=+0.63% | Sharpe=-0.031 | DD=8.97% | Turnover=26.29%
   🎚️ Intra-Step TAPE: potential=0.2363 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1331 | critic_loss=0.5442 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2721 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0261
   🧠 Objective Experts: aux_loss=-0.1771 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0311 | ema=0.5386 | best_ema=0.5386 | no_improve=0
[CYCLE] Update 88/401 | Step 88,704/500,000 | Episode 112 | Time: 8824.9s
   📊 Metrics: Return=+1.71% | Sharpe=0.036 | DD=9.90% | Turnover=26.55%
   🎚️ Intra-Step TAPE: potential=0.3005 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0884 | critic_loss=0.3944 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1972 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0263
   🧠 Objective Experts: aux_loss=-0.1325 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0364 | ema=0.4884 | best_ema=0.4884 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=1.83 | range=[1.21, 10.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.05 | AMZN=3.72 | NEE=2.38  BOT: JPM=2.07 | MSFT=1.93 | GLD=1.45
   🧬 FiLM: seq(dg=0.0054, db=0.0033, sat=0.0%) | latent(dg=0.0590, db=0.0331, sat=0.0%) | asset(dg=0.0025, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (27.3%), low_vol=53 (41.4%), medium_vol=40 (31.2%)
[CYCLE] Update 89/401 | Step 89,712/500,000 | Episode 112 | Time: 8926.1s
   📊 Metrics: Return=+2.98% | Sharpe=0.090 | DD=9.90% | Turnover=26.50%
   🎚️ Intra-Step TAPE: potential=0.3483 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1206 | critic_loss=0.4167 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2083 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0260
   🧠 Objective Experts: aux_loss=-0.1643 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0903 | ema=0.4486 | best_ema=0.4486 | no_improve=0
[CYCLE] Update 90/401 | Step 90,720/500,000 | Episode 112 | Time: 9026.9s
   📊 Metrics: Return=+10.75% | Sharpe=0.440 | DD=10.45% | Turnover=26.60%
   🎚️ Intra-Step TAPE: potential=0.7379 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1028 | critic_loss=0.5098 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2549 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0258
   🧠 Objective Experts: aux_loss=-0.1465 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4397 | ema=0.4477 | best_ema=0.4477 | no_improve=0
   🔬 Alpha Diversity: mean=2.50 | std=2.40 | range=[1.23, 10.67] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.54 | AMZN=2.99 | CAT=1.67  BOT: NEE=1.45 | BRK-B=1.43 | KO=1.42
   🧬 FiLM: seq(dg=0.0060, db=0.0035, sat=0.0%) | latent(dg=0.0578, db=0.0323, sat=0.0%) | asset(dg=0.0026, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (27.3%), low_vol=53 (41.4%), medium_vol=40 (31.2%)
[CYCLE] Update 91/401 | Step 91,728/500,000 | Episode 112 | Time: 9128.0s
   📊 Metrics: Return=+8.22% | Sharpe=0.255 | DD=11.67% | Turnover=26.50%
   🎚️ Intra-Step TAPE: potential=0.2392 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1323 | critic_loss=0.5929 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2964 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0260
   🧠 Objective Experts: aux_loss=-0.1761 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2547 | ema=0.4284 | best_ema=0.4284 | no_improve=0
[CYCLE] Update 92/401 | Step 92,736/500,000 | Episode 112 | Time: 9228.9s
   📊 Metrics: Return=+24.83% | Sharpe=0.744 | DD=11.67% | Turnover=26.38%
   🎚️ Intra-Step TAPE: potential=0.7530 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0158 | critic_loss=0.6847 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3424 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.0593 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7443 | ema=0.4600 | best_ema=0.4600 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=1.98 | range=[1.21, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.03 | AMZN=4.78 | CAT=2.49  BOT: NEE=1.79 | XOM=1.76 | BRK-B=1.76
   🧬 FiLM: seq(dg=0.0064, db=0.0039, sat=0.0%) | latent(dg=0.0624, db=0.0350, sat=0.0%) | asset(dg=0.0026, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (27.3%), low_vol=53 (41.4%), medium_vol=40 (31.2%)
[CYCLE] Update 93/401 | Step 93,744/500,000 | Episode 112 | Time: 9330.0s
   📊 Metrics: Return=+33.61% | Sharpe=0.894 | DD=11.67% | Turnover=26.50%
   🎚️ Intra-Step TAPE: potential=0.7019 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0374 | critic_loss=0.5032 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2516 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.0810 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8943 | ema=0.5034 | best_ema=0.5034 | no_improve=0
[CYCLE] Update 94/401 | Step 94,752/500,000 | Episode 112 | Time: 9431.1s
   📊 Metrics: Return=+35.26% | Sharpe=0.842 | DD=11.67% | Turnover=26.37%
   🎚️ Intra-Step TAPE: potential=0.3037 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1130 | critic_loss=0.5955 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2978 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0262
   🧠 Objective Experts: aux_loss=-0.1569 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8419 | ema=0.5373 | best_ema=0.5373 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=2.15 | range=[1.21, 10.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.10 | AMZN=4.03 | CAT=2.06  BOT: MSFT=1.70 | BRK-B=1.67 | JPM=1.60
   🧬 FiLM: seq(dg=0.0056, db=0.0035, sat=0.0%) | latent(dg=0.0630, db=0.0357, sat=0.0%) | asset(dg=0.0026, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=35 (27.3%), low_vol=53 (41.4%), medium_vol=40 (31.2%)
[CYCLE] Update 95/401 | Step 95,760/500,000 | Episode 112 | Time: 9532.1s
   📊 Metrics: Return=+41.52% | Sharpe=0.910 | DD=11.67% | Turnover=26.56%
   🎚️ Intra-Step TAPE: potential=0.7144 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0891 | critic_loss=0.5399 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2700 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0258
   🧠 Objective Experts: aux_loss=-0.1327 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9097 | ema=0.5745 | best_ema=0.5745 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00113_shp0p949_actor.weights.h5 (Sharpe=0.949, MDD=11.67%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00119_shp1p088_actor.weights.h5 (Sharpe=1.088, MDD=13.50%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00120_shp0p866_actor.weights.h5 (Sharpe=0.866, MDD=10.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00121_shp1p764_actor.weights.h5 (Sharpe=1.764, MDD=10.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00122_shp0p879_actor.weights.h5 (Sharpe=0.879, MDD=16.13%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00123_shp0p765_actor.weights.h5 (Sharpe=0.765, MDD=12.37%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00128_shp1p104_actor.weights.h5 (Sharpe=1.104, MDD=12.90%)
[CYCLE] Update 96/401 | Step 96,768/500,000 | Episode 128 | Time: 9621.2s
   📊 Metrics: Return=+60.94% | Sharpe=1.104 | DD=12.90% | Turnover=26.25%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0509 | critic_loss=2.3587 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.1793 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.0945 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1037 | ema=0.6274 | best_ema=0.6274 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=2.14 | range=[1.21, 10.24] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.13 | CAT=2.42 | AMZN=2.38  BOT: MSFT=1.69 | BRK-B=1.68 | XOM=1.62
   🧬 FiLM: seq(dg=0.0070, db=0.0042, sat=0.0%) | latent(dg=0.0679, db=0.0384, sat=0.0%) | asset(dg=0.0026, db=0.0014, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=40 (27.8%), low_vol=61 (42.4%), medium_vol=43 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.193) | TAPE=0.5316
[CYCLE] Update 97/401 | Step 97,776/500,000 | Episode 128 | Time: 9721.9s
   📊 Metrics: Return=-5.95% | Sharpe=-2.251 | DD=7.08% | Turnover=25.89%
   🎚️ Intra-Step TAPE: potential=0.2333 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1142 | critic_loss=1.8417 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.9208 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0264
   🧠 Objective Experts: aux_loss=-0.1587 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-2.2514 | ema=0.3396 | best_ema=0.3396 | no_improve=0
[CYCLE] Update 98/401 | Step 98,784/500,000 | Episode 128 | Time: 9822.6s
   📊 Metrics: Return=-2.49% | Sharpe=-0.538 | DD=7.23% | Turnover=27.21%
   🎚️ Intra-Step TAPE: potential=0.3559 | delta_reward=-0.0019
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1124 | critic_loss=0.6086 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3043 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.1554 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.5384 | ema=0.2518 | best_ema=0.2518 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=2.06 | range=[1.21, 10.44] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.92 | AMZN=3.37 | CAT=2.87  BOT: BRK-B=1.67 | XOM=1.66 | KO=1.62
   🧬 FiLM: seq(dg=0.0071, db=0.0042, sat=0.0%) | latent(dg=0.0653, db=0.0369, sat=0.0%) | asset(dg=0.0027, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=40 (27.8%), low_vol=61 (42.4%), medium_vol=43 (29.9%)
[CYCLE] Update 99/401 | Step 99,792/500,000 | Episode 128 | Time: 9923.6s
   📊 Metrics: Return=-1.86% | Sharpe=-0.308 | DD=7.23% | Turnover=27.49%
   🎚️ Intra-Step TAPE: potential=0.2315 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0023 | critic_loss=0.6878 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3439 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0452 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.3084 | ema=0.1957 | best_ema=0.1957 | no_improve=0
[CYCLE] Update 100/401 | Step 100,800/500,000 | Episode 128 | Time: 10024.8s
   📊 Metrics: Return=+0.06% | Sharpe=-0.107 | DD=7.23% | Turnover=27.68%
   🎚️ Intra-Step TAPE: potential=0.2757 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0235 | critic_loss=0.4557 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2278 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0191 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.1068 | ema=0.1655 | best_ema=0.1655 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.24 | range=[1.21, 10.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=8.07 | AMZN=2.83 | CAT=2.46  BOT: BRK-B=1.52 | XOM=1.44 | KO=1.36
   🧬 FiLM: seq(dg=0.0085, db=0.0049, sat=0.0%) | latent(dg=0.0732, db=0.0414, sat=0.0%) | asset(dg=0.0029, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=40 (27.8%), low_vol=61 (42.4%), medium_vol=43 (29.9%)
[CYCLE] Update 101/401 | Step 101,808/500,000 | Episode 128 | Time: 10125.8s
   📊 Metrics: Return=+3.53% | Sharpe=0.126 | DD=10.36% | Turnover=27.33%
   🎚️ Intra-Step TAPE: potential=0.5685 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0860 | critic_loss=0.5191 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2595 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.1290 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1258 | ema=0.1615 | best_ema=0.1615 | no_improve=0
[CYCLE] Update 102/401 | Step 102,816/500,000 | Episode 128 | Time: 10226.5s
   📊 Metrics: Return=+1.97% | Sharpe=0.020 | DD=10.36% | Turnover=27.00%
   🎚️ Intra-Step TAPE: potential=0.2490 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0828 | critic_loss=0.6512 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3256 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.1260 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0205 | ema=0.1474 | best_ema=0.1474 | no_improve=0
   🔬 Alpha Diversity: mean=2.50 | std=2.04 | range=[1.21, 10.46] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.48 | AMZN=3.16 | CAT=2.27  BOT: XOM=1.83 | GLD=1.79 | KO=1.78
   🧬 FiLM: seq(dg=0.0079, db=0.0046, sat=0.0%) | latent(dg=0.0718, db=0.0407, sat=0.0%) | asset(dg=0.0027, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=40 (27.8%), low_vol=61 (42.4%), medium_vol=43 (29.9%)
[CYCLE] Update 103/401 | Step 103,824/500,000 | Episode 128 | Time: 10327.2s
   📊 Metrics: Return=+20.82% | Sharpe=0.693 | DD=10.94% | Turnover=26.66%
   🎚️ Intra-Step TAPE: potential=0.7364 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1451 | critic_loss=0.5196 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2598 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.1881 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6932 | ema=0.2020 | best_ema=0.2020 | no_improve=0
[CYCLE] Update 104/401 | Step 104,832/500,000 | Episode 128 | Time: 10427.8s
   📊 Metrics: Return=+34.49% | Sharpe=0.970 | DD=10.94% | Turnover=26.50%
   🎚️ Intra-Step TAPE: potential=0.7248 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0340 | critic_loss=0.5768 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2884 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.0770 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9698 | ema=0.2788 | best_ema=0.2788 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.06 | range=[1.21, 10.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.41 | AMZN=4.21 | CAT=2.61  BOT: XOM=1.53 | KO=1.52 | GLD=1.38
   🧬 FiLM: seq(dg=0.0071, db=0.0045, sat=0.0%) | latent(dg=0.0715, db=0.0409, sat=0.0%) | asset(dg=0.0027, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=40 (27.8%), low_vol=61 (42.4%), medium_vol=43 (29.9%)
[CYCLE] Update 105/401 | Step 105,840/500,000 | Episode 128 | Time: 10528.9s
   📊 Metrics: Return=+40.62% | Sharpe=1.014 | DD=10.94% | Turnover=26.50%
   🎚️ Intra-Step TAPE: potential=0.5809 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1251 | critic_loss=0.6706 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3353 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.1682 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0135 | ema=0.3522 | best_ema=0.3522 | no_improve=0
[CYCLE] Update 106/401 | Step 106,848/500,000 | Episode 128 | Time: 10630.0s
   📊 Metrics: Return=+47.38% | Sharpe=1.058 | DD=10.94% | Turnover=26.57%
   🎚️ Intra-Step TAPE: potential=0.6204 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0520 | critic_loss=0.4859 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2430 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0259
   🧠 Objective Experts: aux_loss=-0.0953 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0580 | ema=0.4228 | best_ema=0.4228 | no_improve=0
   🔬 Alpha Diversity: mean=2.56 | std=1.83 | range=[1.21, 10.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.76 | AMZN=3.02 | NEE=2.54  BOT: XOM=2.13 | CAT=2.09 | GLD=1.69
   🧬 FiLM: seq(dg=0.0071, db=0.0045, sat=0.0%) | latent(dg=0.0724, db=0.0416, sat=0.0%) | asset(dg=0.0028, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=40 (27.8%), low_vol=61 (42.4%), medium_vol=43 (29.9%)
[CYCLE] Update 107/401 | Step 107,856/500,000 | Episode 128 | Time: 10730.9s
   📊 Metrics: Return=+48.17% | Sharpe=0.983 | DD=10.94% | Turnover=26.57%
   🎚️ Intra-Step TAPE: potential=0.2352 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0987 | critic_loss=0.6553 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3277 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0258
   🧠 Objective Experts: aux_loss=-0.1420 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9830 | ema=0.4788 | best_ema=0.4788 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00129_shp1p305_actor.weights.h5 (Sharpe=1.305, MDD=10.94%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00131_shp1p307_actor.weights.h5 (Sharpe=1.307, MDD=18.64%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00132_shp1p086_actor.weights.h5 (Sharpe=1.086, MDD=18.37%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00133_shp1p599_actor.weights.h5 (Sharpe=1.599, MDD=17.16%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00135_shp1p576_actor.weights.h5 (Sharpe=1.576, MDD=13.07%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00136_shp1p614_actor.weights.h5 (Sharpe=1.614, MDD=11.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00138_shp1p527_actor.weights.h5 (Sharpe=1.527, MDD=16.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00142_shp1p575_actor.weights.h5 (Sharpe=1.575, MDD=11.67%)
[CYCLE] Update 108/401 | Step 108,864/500,000 | Episode 144 | Time: 10820.4s
   📊 Metrics: Return=+47.01% | Sharpe=0.774 | DD=25.58% | Turnover=26.87%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0855 | critic_loss=2.1633 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.0817 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0262
   🧠 Objective Experts: aux_loss=-0.1292 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7599 | ema=0.5070 | best_ema=0.5070 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=2.03 | range=[1.21, 10.38] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.67 | AMZN=3.93 | CAT=2.81  BOT: NEE=1.71 | GLD=1.60 | XOM=1.58
   🧬 FiLM: seq(dg=0.0073, db=0.0046, sat=0.0%) | latent(dg=0.0741, db=0.0427, sat=0.0%) | asset(dg=0.0029, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=45 (28.1%), low_vol=68 (42.5%), medium_vol=47 (29.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.075) | TAPE=0.3796
[CYCLE] Update 109/401 | Step 109,872/500,000 | Episode 144 | Time: 10921.2s
   📊 Metrics: Return=+17.99% | Sharpe=4.946 | DD=2.89% | Turnover=26.14%
   🎚️ Intra-Step TAPE: potential=0.7529 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0306 | critic_loss=0.8506 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4253 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.0741 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=4.9460 | ema=0.9509 | best_ema=0.9509 | no_improve=0
[CYCLE] Update 110/401 | Step 110,880/500,000 | Episode 144 | Time: 11022.4s
   📊 Metrics: Return=+29.14% | Sharpe=4.148 | DD=3.72% | Turnover=25.73%
   🎚️ Intra-Step TAPE: potential=0.6905 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1642 | critic_loss=0.7916 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3958 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.2071 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=4.1479 | ema=1.2706 | best_ema=1.2706 | no_improve=0
   🔬 Alpha Diversity: mean=2.55 | std=2.08 | range=[1.21, 10.38] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.61 | NVDA=3.62 | NEE=2.13  BOT: JPM=1.87 | MSFT=1.71 | GLD=1.62
   🧬 FiLM: seq(dg=0.0086, db=0.0052, sat=0.0%) | latent(dg=0.0787, db=0.0453, sat=0.0%) | asset(dg=0.0030, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=45 (28.1%), low_vol=68 (42.5%), medium_vol=47 (29.4%)
[CYCLE] Update 111/401 | Step 111,888/500,000 | Episode 144 | Time: 11123.4s
   📊 Metrics: Return=+28.76% | Sharpe=2.761 | DD=3.72% | Turnover=26.20%
   🎚️ Intra-Step TAPE: potential=0.2370 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0759 | critic_loss=0.3950 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1975 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.1186 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.7614 | ema=1.4196 | best_ema=1.4196 | no_improve=0
[CYCLE] Update 112/401 | Step 112,896/500,000 | Episode 144 | Time: 11224.5s
   📊 Metrics: Return=+41.58% | Sharpe=2.974 | DD=3.72% | Turnover=27.28%
   🎚️ Intra-Step TAPE: potential=0.7361 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1107 | critic_loss=0.4011 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2006 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.1537 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.9741 | ema=1.5751 | best_ema=1.5751 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=2.24 | range=[1.21, 10.41] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.83 | AMZN=2.59 | CAT=2.25  BOT: GLD=1.54 | XOM=1.51 | KO=1.49
   🧬 FiLM: seq(dg=0.0081, db=0.0051, sat=0.0%) | latent(dg=0.0765, db=0.0442, sat=0.0%) | asset(dg=0.0028, db=0.0015, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=45 (28.1%), low_vol=68 (42.5%), medium_vol=47 (29.4%)
[CYCLE] Update 113/401 | Step 113,904/500,000 | Episode 144 | Time: 11325.7s
   📊 Metrics: Return=+48.52% | Sharpe=2.548 | DD=4.82% | Turnover=26.94%
   🎚️ Intra-Step TAPE: potential=0.6378 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1639 | critic_loss=0.6249 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3124 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.2067 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.5478 | ema=1.6724 | best_ema=1.6724 | no_improve=0
[CYCLE] Update 114/401 | Step 114,912/500,000 | Episode 144 | Time: 11426.8s
   📊 Metrics: Return=+65.78% | Sharpe=2.735 | DD=4.82% | Turnover=26.38%
   🎚️ Intra-Step TAPE: potential=0.7378 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0838 | critic_loss=0.6401 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3201 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.1267 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.7352 | ema=1.7786 | best_ema=1.7786 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=2.27 | range=[1.23, 10.27] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.71 | CAT=2.52 | MSFT=2.24  BOT: XOM=1.39 | NEE=1.37 | KO=1.31
   🧬 FiLM: seq(dg=0.0083, db=0.0052, sat=0.0%) | latent(dg=0.0791, db=0.0458, sat=0.0%) | asset(dg=0.0030, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=45 (28.1%), low_vol=68 (42.5%), medium_vol=47 (29.4%)
[CYCLE] Update 115/401 | Step 115,920/500,000 | Episode 144 | Time: 11528.0s
   📊 Metrics: Return=+85.55% | Sharpe=2.889 | DD=4.82% | Turnover=26.27%
   🎚️ Intra-Step TAPE: potential=0.7465 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0837 | critic_loss=0.5620 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2810 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.1259 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.8888 | ema=1.8897 | best_ema=1.8897 | no_improve=0
[CYCLE] Update 116/401 | Step 116,928/500,000 | Episode 144 | Time: 11629.1s
   📊 Metrics: Return=+94.39% | Sharpe=2.646 | DD=7.46% | Turnover=26.26%
   🎚️ Intra-Step TAPE: potential=0.5225 | delta_reward=+0.0014
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0244 | critic_loss=0.5319 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2659 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.0672 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.6461 | ema=1.9653 | best_ema=1.9653 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=1.95 | range=[1.20, 10.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.24 | AMZN=3.75 | JPM=2.18  BOT: NEE=1.79 | GLD=1.73 | KO=1.71
   🧬 FiLM: seq(dg=0.0089, db=0.0054, sat=0.0%) | latent(dg=0.0813, db=0.0471, sat=0.0%) | asset(dg=0.0029, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=45 (28.1%), low_vol=68 (42.5%), medium_vol=47 (29.4%)
[CYCLE] Update 117/401 | Step 117,936/500,000 | Episode 144 | Time: 11730.3s
   📊 Metrics: Return=+104.34% | Sharpe=2.448 | DD=7.46% | Turnover=26.29%
   🎚️ Intra-Step TAPE: potential=0.2758 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0418 | critic_loss=0.6067 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3033 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.0843 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4481 | ema=2.0136 | best_ema=2.0136 | no_improve=0
[CYCLE] Update 118/401 | Step 118,944/500,000 | Episode 144 | Time: 11831.3s
   📊 Metrics: Return=+108.07% | Sharpe=2.323 | DD=7.46% | Turnover=26.38%
   🎚️ Intra-Step TAPE: potential=0.6291 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1081 | critic_loss=0.5683 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2842 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.1509 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3231 | ema=2.0445 | best_ema=2.0445 | no_improve=0
   🔬 Alpha Diversity: mean=2.56 | std=1.84 | range=[1.20, 10.26] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.09 | NVDA=3.29 | NEE=2.73  BOT: MSFT=1.85 | JPM=1.83 | CAT=1.65
   🧬 FiLM: seq(dg=0.0075, db=0.0048, sat=0.0%) | latent(dg=0.0760, db=0.0441, sat=0.0%) | asset(dg=0.0029, db=0.0016, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=45 (28.1%), low_vol=68 (42.5%), medium_vol=47 (29.4%)
[CYCLE] Update 119/401 | Step 119,952/500,000 | Episode 144 | Time: 11932.3s
   📊 Metrics: Return=+109.88% | Sharpe=2.118 | DD=9.51% | Turnover=26.41%
   🎚️ Intra-Step TAPE: potential=0.2725 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0279 | critic_loss=0.5404 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2702 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0258
   🧠 Objective Experts: aux_loss=-0.0710 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.1182 | ema=2.0519 | best_ema=2.0519 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00145_shp1p472_actor.weights.h5 (Sharpe=1.472, MDD=21.97%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00147_shp0p934_actor.weights.h5 (Sharpe=0.934, MDD=12.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00151_shp0p842_actor.weights.h5 (Sharpe=0.842, MDD=11.70%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00152_shp1p215_actor.weights.h5 (Sharpe=1.215, MDD=20.70%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00153_shp1p169_actor.weights.h5 (Sharpe=1.169, MDD=17.38%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00154_shp0p834_actor.weights.h5 (Sharpe=0.834, MDD=12.46%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00155_shp1p294_actor.weights.h5 (Sharpe=1.294, MDD=13.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00157_shp1p039_actor.weights.h5 (Sharpe=1.039, MDD=10.80%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00158_shp0p983_actor.weights.h5 (Sharpe=0.983, MDD=12.40%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00160_shp1p376_actor.weights.h5 (Sharpe=1.376, MDD=17.59%)
[CYCLE] Update 120/401 | Step 120,960/500,000 | Episode 160 | Time: 12022.8s
   📊 Metrics: Return=+85.20% | Sharpe=1.376 | DD=17.59% | Turnover=26.71%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1247 | critic_loss=2.9506 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.4753 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=0.0818 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3758 | ema=1.9843 | best_ema=1.9843 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=2.14 | range=[1.20, 10.31] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.79 | AMZN=4.11 | CAT=2.43  BOT: NEE=1.59 | KO=1.52 | XOM=1.45
   🧬 FiLM: seq(dg=0.0078, db=0.0050, sat=0.0%) | latent(dg=0.0790, db=0.0459, sat=0.0%) | asset(dg=0.0030, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=49 (27.8%), low_vol=76 (43.2%), medium_vol=51 (29.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.5704
[CYCLE] Update 121/401 | Step 121,968/500,000 | Episode 160 | Time: 12123.1s
   📊 Metrics: Return=-12.82% | Sharpe=-2.737 | DD=15.09% | Turnover=28.79%
   🎚️ Intra-Step TAPE: potential=0.2374 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1306 | critic_loss=0.6935 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3468 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.1736 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-2.7367 | ema=1.5122 | best_ema=1.5122 | no_improve=0
[CYCLE] Update 122/401 | Step 122,976/500,000 | Episode 160 | Time: 12224.3s
   📊 Metrics: Return=-8.06% | Sharpe=-0.780 | DD=17.07% | Turnover=27.47%
   🎚️ Intra-Step TAPE: potential=0.3144 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0166 | critic_loss=0.5071 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2536 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.0593 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.7800 | ema=1.2830 | best_ema=1.2830 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.28 | range=[1.21, 10.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.02 | AMZN=4.39 | MSFT=2.14  BOT: BRK-B=1.44 | XOM=1.42 | KO=1.36
   🧬 FiLM: seq(dg=0.0078, db=0.0049, sat=0.0%) | latent(dg=0.0799, db=0.0465, sat=0.0%) | asset(dg=0.0031, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=49 (27.8%), low_vol=76 (43.2%), medium_vol=51 (29.0%)
[CYCLE] Update 123/401 | Step 123,984/500,000 | Episode 160 | Time: 12325.2s
   📊 Metrics: Return=+7.33% | Sharpe=0.481 | DD=17.07% | Turnover=27.78%
   🎚️ Intra-Step TAPE: potential=0.7481 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0089 | critic_loss=0.6943 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3471 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.0335 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4808 | ema=1.2027 | best_ema=1.2027 | no_improve=0
[CYCLE] Update 124/401 | Step 124,992/500,000 | Episode 160 | Time: 12426.1s
   📊 Metrics: Return=+18.69% | Sharpe=0.881 | DD=17.07% | Turnover=26.85%
   🎚️ Intra-Step TAPE: potential=0.7030 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0082 | critic_loss=0.6409 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3205 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.0506 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8809 | ema=1.1706 | best_ema=1.1706 | no_improve=0
   🔬 Alpha Diversity: mean=2.50 | std=2.22 | range=[1.20, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.90 | AMZN=4.92 | MSFT=2.40  BOT: GLD=1.46 | KO=1.44 | XOM=1.44
   🧬 FiLM: seq(dg=0.0079, db=0.0049, sat=0.0%) | latent(dg=0.0768, db=0.0445, sat=0.0%) | asset(dg=0.0033, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=49 (27.8%), low_vol=76 (43.2%), medium_vol=51 (29.0%)
[CYCLE] Update 125/401 | Step 126,000/500,000 | Episode 160 | Time: 12527.1s
   📊 Metrics: Return=+11.66% | Sharpe=0.456 | DD=17.07% | Turnover=27.29%
   🎚️ Intra-Step TAPE: potential=0.2283 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0238 | critic_loss=0.5107 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2553 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0660 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4561 | ema=1.0991 | best_ema=1.0991 | no_improve=0
[CYCLE] Update 126/401 | Step 127,008/500,000 | Episode 160 | Time: 12628.2s
   📊 Metrics: Return=+6.65% | Sharpe=0.215 | DD=24.53% | Turnover=26.94%
   🎚️ Intra-Step TAPE: potential=0.2415 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0641 | critic_loss=0.4705 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2353 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.1059 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2148 | ema=1.0107 | best_ema=1.0107 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.17 | range=[1.20, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.21 | AMZN=3.90 | CAT=2.65  BOT: NEE=1.64 | GLD=1.62 | KO=1.57
   🧬 FiLM: seq(dg=0.0087, db=0.0053, sat=0.0%) | latent(dg=0.0812, db=0.0472, sat=0.0%) | asset(dg=0.0033, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=49 (27.8%), low_vol=76 (43.2%), medium_vol=51 (29.0%)
[CYCLE] Update 127/401 | Step 128,016/500,000 | Episode 160 | Time: 12729.3s
   📊 Metrics: Return=+5.17% | Sharpe=0.154 | DD=26.13% | Turnover=26.49%
   🎚️ Intra-Step TAPE: potential=0.2609 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0378 | critic_loss=0.6270 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3135 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.0791 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1270 | ema=0.9223 | best_ema=0.9223 | no_improve=0
[CYCLE] Update 128/401 | Step 129,024/500,000 | Episode 160 | Time: 12830.4s
   📊 Metrics: Return=+8.85% | Sharpe=0.213 | DD=26.13% | Turnover=26.25%
   🎚️ Intra-Step TAPE: potential=0.5160 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1512 | critic_loss=0.5622 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2811 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.1934 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1855 | ema=0.8486 | best_ema=0.8486 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=2.05 | range=[1.20, 10.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.75 | AMZN=3.46 | NEE=2.23  BOT: XOM=1.92 | JPM=1.82 | MSFT=1.72
   🧬 FiLM: seq(dg=0.0084, db=0.0052, sat=0.0%) | latent(dg=0.0801, db=0.0464, sat=0.0%) | asset(dg=0.0032, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=49 (27.8%), low_vol=76 (43.2%), medium_vol=51 (29.0%)
[CYCLE] Update 129/401 | Step 130,032/500,000 | Episode 160 | Time: 12931.5s
   📊 Metrics: Return=+5.54% | Sharpe=0.127 | DD=26.13% | Turnover=26.11%
   🎚️ Intra-Step TAPE: potential=0.2465 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1008 | critic_loss=0.5495 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2748 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.1433 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0995 | ema=0.7737 | best_ema=0.7737 | no_improve=0
[CYCLE] Update 130/401 | Step 131,040/500,000 | Episode 160 | Time: 13032.3s
   📊 Metrics: Return=+11.80% | Sharpe=0.223 | DD=26.13% | Turnover=25.96%
   🎚️ Intra-Step TAPE: potential=0.6348 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0325 | critic_loss=0.4947 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2473 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.0751 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1958 | ema=0.7159 | best_ema=0.7159 | no_improve=0
   🔬 Alpha Diversity: mean=2.52 | std=2.09 | range=[1.20, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.16 | AMZN=4.14 | CAT=2.13  BOT: KO=1.74 | GLD=1.71 | JPM=1.70
   🧬 FiLM: seq(dg=0.0075, db=0.0048, sat=0.0%) | latent(dg=0.0806, db=0.0468, sat=0.0%) | asset(dg=0.0030, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=49 (27.8%), low_vol=76 (43.2%), medium_vol=51 (29.0%)
[CYCLE] Update 131/401 | Step 132,048/500,000 | Episode 160 | Time: 13133.1s
   📊 Metrics: Return=+6.10% | Sharpe=0.110 | DD=26.13% | Turnover=26.02%
   🎚️ Intra-Step TAPE: potential=0.2295 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0149 | critic_loss=0.5676 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2838 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0275 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0825 | ema=0.6526 | best_ema=0.6526 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00162_shp2p040_actor.weights.h5 (Sharpe=2.040, MDD=11.43%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00163_shp1p296_actor.weights.h5 (Sharpe=1.296, MDD=10.35%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00165_shp1p206_actor.weights.h5 (Sharpe=1.206, MDD=10.52%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00168_shp1p348_actor.weights.h5 (Sharpe=1.348, MDD=11.18%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00171_shp0p832_actor.weights.h5 (Sharpe=0.832, MDD=13.54%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00172_shp1p365_actor.weights.h5 (Sharpe=1.365, MDD=12.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00173_shp2p217_actor.weights.h5 (Sharpe=2.217, MDD=11.93%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00174_shp1p534_actor.weights.h5 (Sharpe=1.534, MDD=13.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00176_shp1p992_actor.weights.h5 (Sharpe=1.992, MDD=12.62%)
[CYCLE] Update 132/401 | Step 133,056/500,000 | Episode 176 | Time: 13222.9s
   📊 Metrics: Return=+148.26% | Sharpe=1.992 | DD=12.62% | Turnover=25.26%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0225 | critic_loss=2.9563 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.4782 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.0652 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.9915 | ema=0.7865 | best_ema=0.7865 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=1.66 | range=[1.20, 10.49] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.56 | AMZN=2.95 | CAT=2.59  BOT: XOM=2.01 | KO=1.93 | GLD=1.82
   🧬 FiLM: seq(dg=0.0066, db=0.0044, sat=0.0%) | latent(dg=0.0766, db=0.0444, sat=0.0%) | asset(dg=0.0030, db=0.0017, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (28.6%), low_vol=83 (43.2%), medium_vol=54 (28.1%)
   🔒 Drawdown λ snapshot=0.231 (peak 0.231, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6715
[CYCLE] Update 133/401 | Step 134,064/500,000 | Episode 176 | Time: 13323.1s
   📊 Metrics: Return=+10.38% | Sharpe=2.719 | DD=3.95% | Turnover=26.99%
   🎚️ Intra-Step TAPE: potential=0.7246 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0143 | critic_loss=1.2365 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6183 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0257
   🧠 Objective Experts: aux_loss=-0.0287 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.7187 | ema=0.9797 | best_ema=0.9797 | no_improve=0
[CYCLE] Update 134/401 | Step 135,072/500,000 | Episode 176 | Time: 13423.8s
   📊 Metrics: Return=+4.66% | Sharpe=0.607 | DD=9.45% | Turnover=27.02%
   🎚️ Intra-Step TAPE: potential=0.2434 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0614 | critic_loss=0.5489 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2744 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.1042 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6067 | ema=0.9424 | best_ema=0.9424 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=1.85 | range=[1.20, 10.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.08 | AMZN=4.51 | CAT=2.22  BOT: NEE=1.83 | XOM=1.77 | KO=1.73
   🧬 FiLM: seq(dg=0.0079, db=0.0052, sat=0.0%) | latent(dg=0.0820, db=0.0478, sat=0.0%) | asset(dg=0.0032, db=0.0018, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (28.6%), low_vol=83 (43.2%), medium_vol=54 (28.1%)
[CYCLE] Update 135/401 | Step 136,080/500,000 | Episode 176 | Time: 13524.8s
   📊 Metrics: Return=+12.12% | Sharpe=1.035 | DD=10.66% | Turnover=27.47%
   🎚️ Intra-Step TAPE: potential=0.7016 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1529 | critic_loss=0.5906 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2953 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0254
   🧠 Objective Experts: aux_loss=-0.1955 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0346 | ema=0.9516 | best_ema=0.9516 | no_improve=0
[CYCLE] Update 136/401 | Step 137,088/500,000 | Episode 176 | Time: 13625.7s
   📊 Metrics: Return=+6.88% | Sharpe=0.405 | DD=10.66% | Turnover=27.36%
   🎚️ Intra-Step TAPE: potential=0.2372 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0057 | critic_loss=0.5552 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2776 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.0480 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4046 | ema=0.8969 | best_ema=0.8969 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=2.34 | range=[1.21, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.55 | AMZN=3.86 | CAT=2.04  BOT: XOM=1.38 | NEE=1.36 | KO=1.34
   🧬 FiLM: seq(dg=0.0099, db=0.0062, sat=0.0%) | latent(dg=0.0853, db=0.0500, sat=0.0%) | asset(dg=0.0035, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (28.6%), low_vol=83 (43.2%), medium_vol=54 (28.1%)
[CYCLE] Update 137/401 | Step 138,096/500,000 | Episode 176 | Time: 13726.5s
   📊 Metrics: Return=+10.83% | Sharpe=0.535 | DD=10.66% | Turnover=27.46%
   🎚️ Intra-Step TAPE: potential=0.6077 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0397 | critic_loss=0.5248 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2624 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.0822 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5349 | ema=0.8607 | best_ema=0.8607 | no_improve=0
[CYCLE] Update 138/401 | Step 139,104/500,000 | Episode 176 | Time: 13827.3s
   📊 Metrics: Return=+14.72% | Sharpe=0.623 | DD=10.66% | Turnover=27.30%
   🎚️ Intra-Step TAPE: potential=0.4756 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1413 | critic_loss=0.5567 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2784 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0253
   🧠 Objective Experts: aux_loss=-0.1838 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6231 | ema=0.8370 | best_ema=0.8370 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=2.22 | range=[1.20, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.18 | AMZN=4.13 | CAT=2.96  BOT: XOM=1.47 | NEE=1.46 | KO=1.39
   🧬 FiLM: seq(dg=0.0073, db=0.0049, sat=0.0%) | latent(dg=0.0786, db=0.0460, sat=0.0%) | asset(dg=0.0034, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (28.6%), low_vol=83 (43.2%), medium_vol=54 (28.1%)
[CYCLE] Update 139/401 | Step 140,112/500,000 | Episode 176 | Time: 13928.2s
   📊 Metrics: Return=+14.03% | Sharpe=0.499 | DD=10.66% | Turnover=27.29%
   🎚️ Intra-Step TAPE: potential=0.2397 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0602 | critic_loss=0.4577 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2289 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1022 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4995 | ema=0.8032 | best_ema=0.8032 | no_improve=0
[CYCLE] Update 140/401 | Step 141,120/500,000 | Episode 176 | Time: 14028.9s
   📊 Metrics: Return=+21.32% | Sharpe=0.678 | DD=10.66% | Turnover=27.50%
   🎚️ Intra-Step TAPE: potential=0.7188 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0512 | critic_loss=0.5317 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2659 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0255
   🧠 Objective Experts: aux_loss=-0.0938 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6780 | ema=0.7907 | best_ema=0.7907 | no_improve=0
   🔬 Alpha Diversity: mean=2.43 | std=1.60 | range=[1.19, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.12 | AMZN=3.99 | MSFT=2.30  BOT: GLD=2.08 | JPM=2.07 | XOM=2.06
   🧬 FiLM: seq(dg=0.0064, db=0.0044, sat=0.0%) | latent(dg=0.0769, db=0.0448, sat=0.0%) | asset(dg=0.0033, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (28.6%), low_vol=83 (43.2%), medium_vol=54 (28.1%)
[CYCLE] Update 141/401 | Step 142,128/500,000 | Episode 176 | Time: 14129.7s
   📊 Metrics: Return=+27.26% | Sharpe=0.765 | DD=10.66% | Turnover=27.30%
   🎚️ Intra-Step TAPE: potential=0.6021 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1600 | critic_loss=0.4158 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2079 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.2020 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7651 | ema=0.7881 | best_ema=0.7881 | no_improve=0
[CYCLE] Update 142/401 | Step 143,136/500,000 | Episode 176 | Time: 14230.5s
   📊 Metrics: Return=+24.33% | Sharpe=0.602 | DD=10.66% | Turnover=27.12%
   🎚️ Intra-Step TAPE: potential=0.2288 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1678 | critic_loss=0.5886 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2943 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.2095 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6024 | ema=0.7696 | best_ema=0.7696 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=2.32 | range=[1.19, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.44 | NVDA=4.28 | CAT=3.03  BOT: GLD=1.46 | NEE=1.41 | KO=1.39
   🧬 FiLM: seq(dg=0.0104, db=0.0065, sat=0.0%) | latent(dg=0.0885, db=0.0520, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=55 (28.6%), low_vol=83 (43.2%), medium_vol=54 (28.1%)
[CYCLE] Update 143/401 | Step 144,144/500,000 | Episode 176 | Time: 14331.5s
   📊 Metrics: Return=+29.80% | Sharpe=0.667 | DD=10.66% | Turnover=27.24%
   🎚️ Intra-Step TAPE: potential=0.6131 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0570 | critic_loss=0.5365 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2682 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.0988 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6673 | ema=0.7593 | best_ema=0.7593 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00179_shp1p826_actor.weights.h5 (Sharpe=1.826, MDD=11.41%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00181_shp1p063_actor.weights.h5 (Sharpe=1.063, MDD=15.65%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00183_shp1p740_actor.weights.h5 (Sharpe=1.740, MDD=13.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00184_shp0p979_actor.weights.h5 (Sharpe=0.979, MDD=12.24%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00188_shp0p720_actor.weights.h5 (Sharpe=0.720, MDD=12.55%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00189_shp1p644_actor.weights.h5 (Sharpe=1.644, MDD=16.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00190_shp1p433_actor.weights.h5 (Sharpe=1.433, MDD=11.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00192_shp1p795_actor.weights.h5 (Sharpe=1.795, MDD=10.17%)
[CYCLE] Update 144/401 | Step 145,152/500,000 | Episode 192 | Time: 14420.7s
   📊 Metrics: Return=+113.49% | Sharpe=1.795 | DD=10.17% | Turnover=25.86%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0527 | critic_loss=2.2934 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.1467 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0947 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7952 | ema=0.8629 | best_ema=0.8629 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=1.82 | range=[1.19, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.41 | NVDA=4.13 | NEE=2.50  BOT: JPM=2.04 | CAT=2.03 | MSFT=1.76
   🧬 FiLM: seq(dg=0.0078, db=0.0053, sat=0.0%) | latent(dg=0.0845, db=0.0495, sat=0.0%) | asset(dg=0.0034, db=0.0019, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=60 (28.8%), low_vol=88 (42.3%), medium_vol=60 (28.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6563
[CYCLE] Update 145/401 | Step 146,160/500,000 | Episode 192 | Time: 14520.9s
   📊 Metrics: Return=+4.05% | Sharpe=1.221 | DD=3.94% | Turnover=27.11%
   🎚️ Intra-Step TAPE: potential=0.6011 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0851 | critic_loss=1.0521 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5261 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1267 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2209 | ema=0.8987 | best_ema=0.8987 | no_improve=0
[CYCLE] Update 146/401 | Step 147,168/500,000 | Episode 192 | Time: 14621.8s
   📊 Metrics: Return=+17.28% | Sharpe=2.326 | DD=4.95% | Turnover=26.23%
   🎚️ Intra-Step TAPE: potential=0.7545 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1378 | critic_loss=0.4281 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2140 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.1794 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3257 | ema=1.0414 | best_ema=1.0414 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=2.27 | range=[1.19, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.43 | AMZN=3.04 | CAT=2.09  BOT: KO=1.62 | NEE=1.61 | JPM=1.53
   🧬 FiLM: seq(dg=0.0084, db=0.0054, sat=0.0%) | latent(dg=0.0804, db=0.0471, sat=0.0%) | asset(dg=0.0037, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=60 (28.8%), low_vol=88 (42.3%), medium_vol=60 (28.8%)
[CYCLE] Update 147/401 | Step 148,176/500,000 | Episode 192 | Time: 14722.5s
   📊 Metrics: Return=+21.38% | Sharpe=1.940 | DD=4.95% | Turnover=26.09%
   🎚️ Intra-Step TAPE: potential=0.5679 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1494 | critic_loss=0.5412 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2706 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.1914 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.9400 | ema=1.1313 | best_ema=1.1313 | no_improve=0
[CYCLE] Update 148/401 | Step 149,184/500,000 | Episode 192 | Time: 14823.4s
   📊 Metrics: Return=+33.66% | Sharpe=2.320 | DD=4.95% | Turnover=25.88%
   🎚️ Intra-Step TAPE: potential=0.7476 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1457 | critic_loss=0.3852 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1926 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.1872 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.3199 | ema=1.2501 | best_ema=1.2501 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=2.38 | range=[1.20, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.26 | AMZN=4.49 | CAT=1.91  BOT: JPM=1.58 | KO=1.54 | XOM=1.51
   🧬 FiLM: seq(dg=0.0108, db=0.0068, sat=0.0%) | latent(dg=0.0858, db=0.0503, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=60 (28.8%), low_vol=88 (42.3%), medium_vol=60 (28.8%)
   [TOOL] Actor learning rate adjusted to 0.000020 at step 150,000
   [TOOL] Critic learning rate adjusted to 0.000120 at step 150,000
[CYCLE] Update 149/401 | Step 150,192/500,000 | Episode 192 | Time: 14924.2s
   📊 Metrics: Return=+49.46% | Sharpe=2.431 | DD=7.97% | Turnover=25.80%
   🎚️ Intra-Step TAPE: potential=0.7121 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0802 | critic_loss=0.5358 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2679 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.1214 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4311 | ema=1.3682 | best_ema=1.3682 | no_improve=0

[DOWN] PPO GAMMA UPDATE at 150,192 steps:
   gamma: 0.9950

[DOWN] PPO GAE-λ UPDATE at 150,192 steps:
   gae_lambda: 0.9500
[CYCLE] Update 150/401 | Step 151,200/500,000 | Episode 192 | Time: 15024.9s
   📊 Metrics: Return=+47.76% | Sharpe=1.932 | DD=7.97% | Turnover=26.00%
   🎚️ Intra-Step TAPE: potential=0.2441 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0383 | critic_loss=0.4926 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2463 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.0035 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.9319 | ema=1.4246 | best_ema=1.4246 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=1.85 | range=[1.19, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.26 | AMZN=3.54 | GLD=2.42  BOT: BRK-B=1.90 | XOM=1.88 | JPM=1.75
   🧬 FiLM: seq(dg=0.0089, db=0.0059, sat=0.0%) | latent(dg=0.0848, db=0.0498, sat=0.0%) | asset(dg=0.0035, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=60 (28.8%), low_vol=88 (42.3%), medium_vol=60 (28.8%)
[CYCLE] Update 151/401 | Step 152,208/500,000 | Episode 192 | Time: 15125.6s
   📊 Metrics: Return=+53.15% | Sharpe=1.860 | DD=7.97% | Turnover=26.10%
   🎚️ Intra-Step TAPE: potential=0.5313 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1316 | critic_loss=0.4563 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2282 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.1732 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.8603 | ema=1.4682 | best_ema=1.4682 | no_improve=0
[CYCLE] Update 152/401 | Step 153,216/500,000 | Episode 192 | Time: 15226.7s
   📊 Metrics: Return=+37.15% | Sharpe=1.063 | DD=13.62% | Turnover=26.22%
   🎚️ Intra-Step TAPE: potential=0.2309 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0727 | critic_loss=1.2669 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6334 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1146 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0628 | ema=1.4276 | best_ema=1.4276 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=2.11 | range=[1.19, 10.66] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.46 | NVDA=4.73 | CAT=2.46  BOT: JPM=1.63 | KO=1.63 | XOM=1.60
   🧬 FiLM: seq(dg=0.0077, db=0.0052, sat=0.0%) | latent(dg=0.0807, db=0.0474, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=60 (28.8%), low_vol=88 (42.3%), medium_vol=60 (28.8%)
[CYCLE] Update 153/401 | Step 154,224/500,000 | Episode 192 | Time: 15327.7s
   📊 Metrics: Return=+43.41% | Sharpe=1.019 | DD=20.22% | Turnover=26.30%
   🎚️ Intra-Step TAPE: potential=0.4726 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0142 | critic_loss=0.6032 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3016 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.0278 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0193 | ema=1.3868 | best_ema=1.3868 | no_improve=0
[CYCLE] Update 154/401 | Step 155,232/500,000 | Episode 192 | Time: 15428.4s
   📊 Metrics: Return=+42.67% | Sharpe=0.900 | DD=20.22% | Turnover=26.03%
   🎚️ Intra-Step TAPE: potential=0.2343 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.2000 | critic_loss=1.0462 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5231 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.2420 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8998 | ema=1.3381 | best_ema=1.3381 | no_improve=0
   🔬 Alpha Diversity: mean=2.51 | std=2.29 | range=[1.20, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.58 | AMZN=5.03 | CAT=2.79  BOT: XOM=1.40 | NEE=1.33 | KO=1.31
   🧬 FiLM: seq(dg=0.0107, db=0.0068, sat=0.0%) | latent(dg=0.0855, db=0.0503, sat=0.0%) | asset(dg=0.0039, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=60 (28.8%), low_vol=88 (42.3%), medium_vol=60 (28.8%)
[CYCLE] Update 155/401 | Step 156,240/500,000 | Episode 192 | Time: 15529.3s
   📊 Metrics: Return=+52.66% | Sharpe=0.980 | DD=20.22% | Turnover=26.04%
   🎚️ Intra-Step TAPE: potential=0.6352 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1293 | critic_loss=0.7440 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3720 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=0.0880 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9796 | ema=1.3023 | best_ema=1.3023 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00193_shp1p023_actor.weights.h5 (Sharpe=1.023, MDD=20.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00197_shp0p971_actor.weights.h5 (Sharpe=0.971, MDD=20.87%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00198_shp1p058_actor.weights.h5 (Sharpe=1.058, MDD=19.51%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00199_shp1p485_actor.weights.h5 (Sharpe=1.485, MDD=10.35%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00200_shp0p930_actor.weights.h5 (Sharpe=0.930, MDD=12.89%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00201_shp0p985_actor.weights.h5 (Sharpe=0.985, MDD=19.50%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00202_shp1p105_actor.weights.h5 (Sharpe=1.105, MDD=11.04%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00203_shp1p589_actor.weights.h5 (Sharpe=1.589, MDD=12.23%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00204_shp2p016_actor.weights.h5 (Sharpe=2.016, MDD=10.37%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00207_shp0p787_actor.weights.h5 (Sharpe=0.787, MDD=12.99%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00208_shp2p016_actor.weights.h5 (Sharpe=2.016, MDD=11.75%)
[CYCLE] Update 156/401 | Step 157,248/500,000 | Episode 208 | Time: 15620.1s
   📊 Metrics: Return=+133.52% | Sharpe=2.016 | DD=11.75% | Turnover=25.69%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0055 | critic_loss=3.8211 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.9105 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0366 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.0158 | ema=1.3736 | best_ema=1.3736 | no_improve=0
   🔬 Alpha Diversity: mean=2.54 | std=2.24 | range=[1.20, 10.44] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.41 | AMZN=4.00 | CAT=3.33  BOT: XOM=1.39 | KO=1.30 | NEE=1.30
   🧬 FiLM: seq(dg=0.0093, db=0.0060, sat=0.0%) | latent(dg=0.0848, db=0.0500, sat=0.0%) | asset(dg=0.0037, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=67 (29.9%), low_vol=92 (41.1%), medium_vol=65 (29.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6828
[CYCLE] Update 157/401 | Step 158,256/500,000 | Episode 208 | Time: 15720.2s
   📊 Metrics: Return=-10.73% | Sharpe=-1.918 | DD=16.17% | Turnover=28.42%
   🎚️ Intra-Step TAPE: potential=0.2336 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0398 | critic_loss=1.4699 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7349 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.0820 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-1.9183 | ema=1.0444 | best_ema=1.0444 | no_improve=0
[CYCLE] Update 158/401 | Step 159,264/500,000 | Episode 208 | Time: 15820.9s
   📊 Metrics: Return=-7.58% | Sharpe=-0.649 | DD=18.64% | Turnover=26.36%
   🎚️ Intra-Step TAPE: potential=0.2564 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0490 | critic_loss=0.4977 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2489 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.0907 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.6495 | ema=0.8750 | best_ema=0.8750 | no_improve=0
   🔬 Alpha Diversity: mean=2.48 | std=2.32 | range=[1.19, 10.37] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.08 | AMZN=3.60 | CAT=2.03  BOT: NEE=1.39 | BRK-B=1.38 | KO=1.35
   🧬 FiLM: seq(dg=0.0124, db=0.0076, sat=0.0%) | latent(dg=0.0919, db=0.0542, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=67 (29.9%), low_vol=92 (41.1%), medium_vol=65 (29.0%)
[CYCLE] Update 159/401 | Step 160,272/500,000 | Episode 208 | Time: 15921.7s
   📊 Metrics: Return=+9.42% | Sharpe=0.584 | DD=18.64% | Turnover=26.02%
   🎚️ Intra-Step TAPE: potential=0.7490 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0863 | critic_loss=0.6468 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3234 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.1279 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5836 | ema=0.8459 | best_ema=0.8459 | no_improve=0
[CYCLE] Update 160/401 | Step 161,280/500,000 | Episode 208 | Time: 16022.5s
   📊 Metrics: Return=+21.55% | Sharpe=0.962 | DD=18.64% | Turnover=26.36%
   🎚️ Intra-Step TAPE: potential=0.7087 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0425 | critic_loss=0.5695 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2847 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.0839 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9617 | ema=0.8575 | best_ema=0.8575 | no_improve=0
   🔬 Alpha Diversity: mean=2.43 | std=2.01 | range=[1.19, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.54 | AMZN=4.37 | CAT=1.95  BOT: NEE=1.81 | MSFT=1.74 | JPM=1.73
   🧬 FiLM: seq(dg=0.0112, db=0.0072, sat=0.0%) | latent(dg=0.0926, db=0.0546, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=67 (29.9%), low_vol=92 (41.1%), medium_vol=65 (29.0%)
[CYCLE] Update 161/401 | Step 162,288/500,000 | Episode 208 | Time: 16123.4s
   📊 Metrics: Return=+15.47% | Sharpe=0.579 | DD=18.64% | Turnover=26.50%
   🎚️ Intra-Step TAPE: potential=0.2305 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0311 | critic_loss=0.6082 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3041 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.0725 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5789 | ema=0.8296 | best_ema=0.8296 | no_improve=0
[CYCLE] Update 162/401 | Step 163,296/500,000 | Episode 208 | Time: 16224.0s
   📊 Metrics: Return=+6.67% | Sharpe=0.215 | DD=23.67% | Turnover=26.31%
   🎚️ Intra-Step TAPE: potential=0.2407 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0664 | critic_loss=0.7467 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3733 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.1080 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2153 | ema=0.7682 | best_ema=0.7682 | no_improve=0
   🔬 Alpha Diversity: mean=2.41 | std=1.82 | range=[1.18, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.85 | AMZN=3.41 | CAT=2.37  BOT: BRK-B=1.85 | KO=1.83 | XOM=1.81
   🧬 FiLM: seq(dg=0.0092, db=0.0061, sat=0.0%) | latent(dg=0.0876, db=0.0516, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=67 (29.9%), low_vol=92 (41.1%), medium_vol=65 (29.0%)
[CYCLE] Update 163/401 | Step 164,304/500,000 | Episode 208 | Time: 16324.6s
   📊 Metrics: Return=+9.61% | Sharpe=0.256 | DD=25.61% | Turnover=26.20%
   🎚️ Intra-Step TAPE: potential=0.2659 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0910 | critic_loss=0.4692 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2346 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=-0.1320 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2415 | ema=0.7155 | best_ema=0.7155 | no_improve=0
[CYCLE] Update 164/401 | Step 165,312/500,000 | Episode 208 | Time: 16425.1s
   📊 Metrics: Return=+9.13% | Sharpe=0.218 | DD=25.61% | Turnover=25.87%
   🎚️ Intra-Step TAPE: potential=0.2536 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1134 | critic_loss=0.5309 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2655 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.1545 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2037 | ema=0.6643 | best_ema=0.6643 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=2.34 | range=[1.19, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.42 | AMZN=4.70 | CAT=2.09  BOT: KO=1.54 | NEE=1.47 | XOM=1.47
   🧬 FiLM: seq(dg=0.0109, db=0.0070, sat=0.0%) | latent(dg=0.0899, db=0.0530, sat=0.0%) | asset(dg=0.0039, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=67 (29.9%), low_vol=92 (41.1%), medium_vol=65 (29.0%)
[CYCLE] Update 165/401 | Step 166,320/500,000 | Episode 208 | Time: 16526.0s
   📊 Metrics: Return=+8.49% | Sharpe=0.184 | DD=25.61% | Turnover=25.86%
   🎚️ Intra-Step TAPE: potential=0.2544 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0827 | critic_loss=0.8759 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4379 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1240 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1695 | ema=0.6149 | best_ema=0.6149 | no_improve=0
[CYCLE] Update 166/401 | Step 167,328/500,000 | Episode 208 | Time: 16626.8s
   📊 Metrics: Return=+16.00% | Sharpe=0.292 | DD=25.61% | Turnover=25.92%
   🎚️ Intra-Step TAPE: potential=0.5799 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1442 | critic_loss=0.7223 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3611 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1855 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2775 | ema=0.5811 | best_ema=0.5811 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.35 | range=[1.18, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.42 | AMZN=5.05 | CAT=2.01  BOT: JPM=1.58 | NEE=1.53 | GLD=1.51
   🧬 FiLM: seq(dg=0.0094, db=0.0062, sat=0.0%) | latent(dg=0.0874, db=0.0516, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=67 (29.9%), low_vol=92 (41.1%), medium_vol=65 (29.0%)
[CYCLE] Update 167/401 | Step 168,336/500,000 | Episode 208 | Time: 16727.5s
   📊 Metrics: Return=+12.49% | Sharpe=0.214 | DD=25.61% | Turnover=25.82%
   🎚️ Intra-Step TAPE: potential=0.2361 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0364 | critic_loss=0.5966 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2983 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.0779 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1997 | ema=0.5430 | best_ema=0.5430 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00212_shp2p044_actor.weights.h5 (Sharpe=2.044, MDD=11.28%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00215_shp1p974_actor.weights.h5 (Sharpe=1.974, MDD=11.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00216_shp1p796_actor.weights.h5 (Sharpe=1.796, MDD=10.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00219_shp1p452_actor.weights.h5 (Sharpe=1.452, MDD=17.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00220_shp0p846_actor.weights.h5 (Sharpe=0.846, MDD=13.34%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00223_shp1p240_actor.weights.h5 (Sharpe=1.240, MDD=11.77%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00224_shp2p118_actor.weights.h5 (Sharpe=2.118, MDD=11.98%)
[CYCLE] Update 168/401 | Step 169,344/500,000 | Episode 224 | Time: 16816.3s
   📊 Metrics: Return=+143.06% | Sharpe=2.118 | DD=11.98% | Turnover=26.38%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0719 | critic_loss=3.9926 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.9963 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.1134 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.1179 | ema=0.7005 | best_ema=0.7005 | no_improve=0
   🔬 Alpha Diversity: mean=2.48 | std=1.79 | range=[1.18, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.29 | AMZN=4.19 | NEE=2.60  BOT: XOM=2.01 | CAT=1.89 | MSFT=1.79
   🧬 FiLM: seq(dg=0.0092, db=0.0062, sat=0.0%) | latent(dg=0.0902, db=0.0533, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (29.6%), low_vol=100 (41.7%), medium_vol=69 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6925
[CYCLE] Update 169/401 | Step 170,352/500,000 | Episode 224 | Time: 16916.4s
   📊 Metrics: Return=+5.35% | Sharpe=1.752 | DD=3.45% | Turnover=26.75%
   🎚️ Intra-Step TAPE: potential=0.6812 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1377 | critic_loss=1.7795 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8898 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.1792 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.7524 | ema=0.8057 | best_ema=0.8057 | no_improve=0
[CYCLE] Update 170/401 | Step 171,360/500,000 | Episode 224 | Time: 17017.5s
   📊 Metrics: Return=+4.98% | Sharpe=0.763 | DD=4.07% | Turnover=26.03%
   🎚️ Intra-Step TAPE: potential=0.2461 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1889 | critic_loss=0.6776 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3388 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.2306 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7627 | ema=0.8014 | best_ema=0.8014 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=1.87 | range=[1.18, 10.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.53 | AMZN=3.59 | XOM=2.56  BOT: JPM=1.80 | GLD=1.69 | MSFT=1.69
   🧬 FiLM: seq(dg=0.0101, db=0.0066, sat=0.0%) | latent(dg=0.0891, db=0.0526, sat=0.0%) | asset(dg=0.0037, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (29.6%), low_vol=100 (41.7%), medium_vol=69 (28.7%)
[CYCLE] Update 171/401 | Step 172,368/500,000 | Episode 224 | Time: 17118.0s
   📊 Metrics: Return=+9.83% | Sharpe=1.012 | DD=4.18% | Turnover=26.50%
   🎚️ Intra-Step TAPE: potential=0.6861 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1170 | critic_loss=1.0800 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5400 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1588 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0118 | ema=0.8224 | best_ema=0.8224 | no_improve=0
[CYCLE] Update 172/401 | Step 173,376/500,000 | Episode 224 | Time: 17218.7s
   📊 Metrics: Return=+10.80% | Sharpe=0.857 | DD=4.18% | Turnover=26.91%
   🎚️ Intra-Step TAPE: potential=0.3038 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0771 | critic_loss=0.6735 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3368 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.1187 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8573 | ema=0.8259 | best_ema=0.8259 | no_improve=0
   🔬 Alpha Diversity: mean=2.48 | std=2.10 | range=[1.18, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.27 | NVDA=4.04 | CAT=2.11  BOT: NEE=1.69 | JPM=1.65 | MSFT=1.63
   🧬 FiLM: seq(dg=0.0108, db=0.0071, sat=0.0%) | latent(dg=0.0944, db=0.0559, sat=0.0%) | asset(dg=0.0037, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (29.6%), low_vol=100 (41.7%), medium_vol=69 (28.7%)
[CYCLE] Update 173/401 | Step 174,384/500,000 | Episode 224 | Time: 17319.4s
   📊 Metrics: Return=+6.50% | Sharpe=0.336 | DD=6.32% | Turnover=27.10%
   🎚️ Intra-Step TAPE: potential=0.2248 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0571 | critic_loss=0.7084 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3542 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=-0.0980 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3364 | ema=0.7769 | best_ema=0.7769 | no_improve=0
[CYCLE] Update 174/401 | Step 175,392/500,000 | Episode 224 | Time: 17420.1s
   📊 Metrics: Return=+11.05% | Sharpe=0.508 | DD=6.79% | Turnover=27.09%
   🎚️ Intra-Step TAPE: potential=0.5329 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1031 | critic_loss=0.6383 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3192 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.1440 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5083 | ema=0.7501 | best_ema=0.7501 | no_improve=0
   🔬 Alpha Diversity: mean=2.41 | std=1.97 | range=[1.18, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.74 | AMZN=4.00 | CAT=2.37  BOT: GLD=1.77 | KO=1.76 | BRK-B=1.73
   🧬 FiLM: seq(dg=0.0108, db=0.0070, sat=0.0%) | latent(dg=0.0891, db=0.0526, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (29.6%), low_vol=100 (41.7%), medium_vol=69 (28.7%)
[CYCLE] Update 175/401 | Step 176,400/500,000 | Episode 224 | Time: 17520.8s
   📊 Metrics: Return=+11.96% | Sharpe=0.457 | DD=8.33% | Turnover=26.78%
   🎚️ Intra-Step TAPE: potential=0.2567 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0371 | critic_loss=0.9676 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4838 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0237
   🧠 Objective Experts: aux_loss=-0.0778 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4573 | ema=0.7208 | best_ema=0.7208 | no_improve=0
[CYCLE] Update 176/401 | Step 177,408/500,000 | Episode 224 | Time: 17621.4s
   📊 Metrics: Return=+11.68% | Sharpe=0.360 | DD=8.44% | Turnover=26.75%
   🎚️ Intra-Step TAPE: potential=0.2484 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0682 | critic_loss=0.9841 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4921 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.1095 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3597 | ema=0.6847 | best_ema=0.6847 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=2.33 | range=[1.18, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.24 | AMZN=4.95 | CAT=2.14  BOT: XOM=1.45 | NEE=1.39 | KO=1.38
   🧬 FiLM: seq(dg=0.0107, db=0.0070, sat=0.0%) | latent(dg=0.0923, db=0.0546, sat=0.0%) | asset(dg=0.0039, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (29.6%), low_vol=100 (41.7%), medium_vol=69 (28.7%)
[CYCLE] Update 177/401 | Step 178,416/500,000 | Episode 224 | Time: 17722.1s
   📊 Metrics: Return=+12.59% | Sharpe=0.343 | DD=8.44% | Turnover=26.79%
   🎚️ Intra-Step TAPE: potential=0.2828 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0030 | critic_loss=0.7632 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3816 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.0446 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3434 | ema=0.6506 | best_ema=0.6506 | no_improve=0
[CYCLE] Update 178/401 | Step 179,424/500,000 | Episode 224 | Time: 17822.8s
   📊 Metrics: Return=+14.72% | Sharpe=0.370 | DD=8.44% | Turnover=26.87%
   🎚️ Intra-Step TAPE: potential=0.4895 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1147 | critic_loss=0.8942 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4471 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.1563 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3704 | ema=0.6225 | best_ema=0.6225 | no_improve=0
   🔬 Alpha Diversity: mean=2.49 | std=2.06 | range=[1.18, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.48 | AMZN=3.33 | CAT=2.17  BOT: XOM=1.80 | BRK-B=1.77 | MSFT=1.73
   🧬 FiLM: seq(dg=0.0089, db=0.0060, sat=0.0%) | latent(dg=0.0888, db=0.0525, sat=0.0%) | asset(dg=0.0036, db=0.0020, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=71 (29.6%), low_vol=100 (41.7%), medium_vol=69 (28.7%)
[CYCLE] Update 179/401 | Step 180,432/500,000 | Episode 224 | Time: 17923.4s
   📊 Metrics: Return=+23.76% | Sharpe=0.531 | DD=8.80% | Turnover=26.96%
   🎚️ Intra-Step TAPE: potential=0.7279 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0228 | critic_loss=0.9281 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4640 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.0180 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5313 | ema=0.6134 | best_ema=0.6134 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00227_shp1p634_actor.weights.h5 (Sharpe=1.634, MDD=12.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00230_shp1p923_actor.weights.h5 (Sharpe=1.923, MDD=12.77%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00231_shp1p065_actor.weights.h5 (Sharpe=1.065, MDD=13.18%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00232_shp1p291_actor.weights.h5 (Sharpe=1.291, MDD=13.22%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00234_shp0p858_actor.weights.h5 (Sharpe=0.858, MDD=11.61%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00236_shp1p491_actor.weights.h5 (Sharpe=1.491, MDD=21.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00238_shp1p259_actor.weights.h5 (Sharpe=1.259, MDD=12.13%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00240_shp2p028_actor.weights.h5 (Sharpe=2.028, MDD=12.40%)
[CYCLE] Update 180/401 | Step 181,440/500,000 | Episode 240 | Time: 18012.6s
   📊 Metrics: Return=+139.93% | Sharpe=2.028 | DD=12.40% | Turnover=26.34%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0644 | critic_loss=6.2881 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=3.1440 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=0.0233 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.0276 | ema=0.7548 | best_ema=0.7548 | no_improve=0
   🔬 Alpha Diversity: mean=2.42 | std=1.98 | range=[1.18, 10.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.22 | AMZN=4.19 | CAT=2.35  BOT: BRK-B=1.87 | NEE=1.82 | MSFT=1.66
   🧬 FiLM: seq(dg=0.0096, db=0.0064, sat=0.0%) | latent(dg=0.0884, db=0.0523, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=78 (30.5%), low_vol=102 (39.8%), medium_vol=76 (29.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6791
[CYCLE] Update 181/401 | Step 182,448/500,000 | Episode 240 | Time: 18112.6s
   📊 Metrics: Return=-1.63% | Sharpe=-0.873 | DD=5.04% | Turnover=27.65%
   🎚️ Intra-Step TAPE: potential=0.2448 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0499 | critic_loss=1.9564 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.9782 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   🧠 Objective Experts: aux_loss=-0.0904 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.8730 | ema=0.5921 | best_ema=0.5921 | no_improve=0
[CYCLE] Update 182/401 | Step 183,456/500,000 | Episode 240 | Time: 18213.2s
   📊 Metrics: Return=+4.17% | Sharpe=0.471 | DD=10.64% | Turnover=27.55%
   🎚️ Intra-Step TAPE: potential=0.6066 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1313 | critic_loss=0.6045 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3023 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=-0.1722 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4712 | ema=0.5800 | best_ema=0.5800 | no_improve=0
   🔬 Alpha Diversity: mean=2.41 | std=2.13 | range=[1.18, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.09 | AMZN=4.38 | NEE=1.94  BOT: BRK-B=1.69 | MSFT=1.66 | JPM=1.66
   🧬 FiLM: seq(dg=0.0113, db=0.0074, sat=0.0%) | latent(dg=0.0932, db=0.0552, sat=0.0%) | asset(dg=0.0039, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=78 (30.5%), low_vol=102 (39.8%), medium_vol=76 (29.7%)
[CYCLE] Update 183/401 | Step 184,464/500,000 | Episode 240 | Time: 18313.8s
   📊 Metrics: Return=+1.75% | Sharpe=0.102 | DD=10.64% | Turnover=27.06%
   🎚️ Intra-Step TAPE: potential=0.2452 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1878 | critic_loss=0.5757 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2878 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.2286 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1016 | ema=0.5321 | best_ema=0.5321 | no_improve=0
[CYCLE] Update 184/401 | Step 185,472/500,000 | Episode 240 | Time: 18414.3s
   📊 Metrics: Return=+19.04% | Sharpe=1.028 | DD=12.00% | Turnover=26.62%
   🎚️ Intra-Step TAPE: potential=0.7380 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1370 | critic_loss=0.6020 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3010 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.1781 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0276 | ema=0.5817 | best_ema=0.5817 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.36 | range=[1.18, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.69 | AMZN=2.98 | KO=1.61  BOT: CAT=1.53 | BRK-B=1.52 | MSFT=1.51
   🧬 FiLM: seq(dg=0.0120, db=0.0079, sat=0.0%) | latent(dg=0.0987, db=0.0586, sat=0.0%) | asset(dg=0.0039, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=78 (30.5%), low_vol=102 (39.8%), medium_vol=76 (29.7%)
[CYCLE] Update 185/401 | Step 186,480/500,000 | Episode 240 | Time: 18515.0s
   📊 Metrics: Return=+32.05% | Sharpe=1.362 | DD=12.00% | Turnover=26.59%
   🎚️ Intra-Step TAPE: potential=0.7327 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1496 | critic_loss=0.4789 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2395 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1909 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3618 | ema=0.6597 | best_ema=0.6597 | no_improve=0
[CYCLE] Update 186/401 | Step 187,488/500,000 | Episode 240 | Time: 18615.6s
   📊 Metrics: Return=+37.98% | Sharpe=1.372 | DD=12.00% | Turnover=26.60%
   🎚️ Intra-Step TAPE: potential=0.5519 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0307 | critic_loss=0.5124 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2562 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.0717 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3724 | ema=0.7310 | best_ema=0.7310 | no_improve=0
   🔬 Alpha Diversity: mean=2.40 | std=1.98 | range=[1.18, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.56 | AMZN=4.24 | CAT=1.94  BOT: JPM=1.86 | GLD=1.79 | BRK-B=1.75
   🧬 FiLM: seq(dg=0.0112, db=0.0074, sat=0.0%) | latent(dg=0.0951, db=0.0564, sat=0.0%) | asset(dg=0.0039, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=78 (30.5%), low_vol=102 (39.8%), medium_vol=76 (29.7%)
[CYCLE] Update 187/401 | Step 188,496/500,000 | Episode 240 | Time: 18716.3s
   📊 Metrics: Return=+53.74% | Sharpe=1.633 | DD=12.00% | Turnover=26.54%
   🎚️ Intra-Step TAPE: potential=0.7513 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1905 | critic_loss=0.4474 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2237 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.2315 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.6328 | ema=0.8211 | best_ema=0.8211 | no_improve=0
[CYCLE] Update 188/401 | Step 189,504/500,000 | Episode 240 | Time: 18817.0s
   📊 Metrics: Return=+56.15% | Sharpe=1.507 | DD=12.00% | Turnover=26.44%
   🎚️ Intra-Step TAPE: potential=0.2351 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0565 | critic_loss=0.4885 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2443 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=0.0153 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.5071 | ema=0.8897 | best_ema=0.8897 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=1.99 | range=[1.17, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.66 | AMZN=4.54 | JPM=2.32  BOT: BRK-B=1.83 | MSFT=1.82 | KO=1.79
   🧬 FiLM: seq(dg=0.0102, db=0.0069, sat=0.0%) | latent(dg=0.0935, db=0.0554, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=78 (30.5%), low_vol=102 (39.8%), medium_vol=76 (29.7%)

📚 EPISODE HORIZON UPDATE at 190,512 steps:
   Episode horizon: 769 steps
[CYCLE] Update 189/401 | Step 190,512/500,000 | Episode 240 | Time: 18917.8s
   📊 Metrics: Return=+76.06% | Sharpe=1.727 | DD=12.00% | Turnover=26.47%
   🎚️ Intra-Step TAPE: potential=0.7549 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0241 | critic_loss=0.5090 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2545 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.0652 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.7269 | ema=0.9735 | best_ema=0.9735 | no_improve=0

📚 EPISODE HORIZON UPDATE at 191,520 steps:
   Episode horizon: 794 steps
[CYCLE] Update 190/401 | Step 191,520/500,000 | Episode 240 | Time: 19018.4s
   📊 Metrics: Return=+91.36% | Sharpe=1.818 | DD=12.00% | Turnover=26.11%
   🎚️ Intra-Step TAPE: potential=0.7273 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1076 | critic_loss=0.9315 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4658 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   🧠 Objective Experts: aux_loss=-0.1483 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.8176 | ema=1.0579 | best_ema=1.0579 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.33 | range=[1.17, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.65 | AMZN=3.37 | CAT=2.37  BOT: GLD=1.52 | KO=1.49 | BRK-B=1.48
   🧬 FiLM: seq(dg=0.0121, db=0.0080, sat=0.0%) | latent(dg=0.0964, db=0.0572, sat=0.0%) | asset(dg=0.0039, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=78 (30.5%), low_vol=102 (39.8%), medium_vol=76 (29.7%)

📚 EPISODE HORIZON UPDATE at 192,528 steps:
   Episode horizon: 820 steps
[CYCLE] Update 191/401 | Step 192,528/500,000 | Episode 240 | Time: 19119.1s
   📊 Metrics: Return=+118.33% | Sharpe=2.048 | DD=12.00% | Turnover=26.13%
   🎚️ Intra-Step TAPE: potential=0.7472 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0577 | critic_loss=0.7356 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3678 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0991 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.0477 | ema=1.1569 | best_ema=1.1569 | no_improve=0

📚 EPISODE HORIZON UPDATE at 193,536 steps:
   Episode horizon: 845 steps
[CYCLE] Update 192/401 | Step 193,536/500,000 | Episode 240 | Time: 19219.7s
   📊 Metrics: Return=+117.85% | Sharpe=1.791 | DD=12.00% | Turnover=26.17%
   🎚️ Intra-Step TAPE: potential=0.2279 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0274 | critic_loss=1.2430 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6215 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.0684 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.7913 | ema=1.2203 | best_ema=1.2203 | no_improve=0
   🔬 Alpha Diversity: mean=2.43 | std=2.25 | range=[1.17, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.34 | AMZN=3.26 | GLD=2.80  BOT: NEE=1.60 | BRK-B=1.58 | KO=1.51
   🧬 FiLM: seq(dg=0.0102, db=0.0069, sat=0.0%) | latent(dg=0.0930, db=0.0552, sat=0.0%) | asset(dg=0.0039, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=78 (30.5%), low_vol=102 (39.8%), medium_vol=76 (29.7%)

📚 EPISODE HORIZON UPDATE at 194,544 steps:
   Episode horizon: 871 steps
[CYCLE] Update 193/401 | Step 194,544/500,000 | Episode 240 | Time: 19320.5s
   📊 Metrics: Return=+117.58% | Sharpe=1.669 | DD=12.00% | Turnover=26.17%
   🎚️ Intra-Step TAPE: potential=0.2768 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0973 | critic_loss=1.0384 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5192 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.1387 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.6693 | ema=1.2652 | best_ema=1.2652 | no_improve=0
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00241_shp1p705_actor.weights.h5 (Sharpe=1.705, MDD=12.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00243_shp0p743_actor.weights.h5 (Sharpe=0.743, MDD=13.03%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00249_shp1p648_actor.weights.h5 (Sharpe=1.648, MDD=12.24%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00253_shp1p285_actor.weights.h5 (Sharpe=1.285, MDD=14.58%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00254_shp1p329_actor.weights.h5 (Sharpe=1.329, MDD=20.24%)

📚 EPISODE HORIZON UPDATE at 195,552 steps:
   Episode horizon: 896 steps
[CYCLE] Update 194/401 | Step 195,552/500,000 | Episode 256 | Time: 19423.9s
   📊 Metrics: Return=+21.66% | Sharpe=0.342 | DD=11.37% | Turnover=26.90%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0680 | critic_loss=7.1762 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=3.5881 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.1094 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3423 | ema=1.1729 | best_ema=1.1729 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=2.23 | range=[1.17, 10.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.03 | AMZN=4.60 | JPM=2.36  BOT: NEE=1.58 | MSFT=1.44 | KO=1.42
   🧬 FiLM: seq(dg=0.0098, db=0.0067, sat=0.0%) | latent(dg=0.0918, db=0.0544, sat=0.0%) | asset(dg=0.0039, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=84 (30.9%), low_vol=105 (38.6%), medium_vol=83 (30.5%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.80% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2811

📚 EPISODE HORIZON UPDATE at 196,560 steps:
   Episode horizon: 921 steps
[CYCLE] Update 195/401 | Step 196,560/500,000 | Episode 256 | Time: 19524.2s
   📊 Metrics: Return=+19.36% | Sharpe=3.695 | DD=3.78% | Turnover=26.21%
   🎚️ Intra-Step TAPE: potential=0.7496 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0777 | critic_loss=1.4585 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7293 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.1187 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=3.6954 | ema=1.4252 | best_ema=1.4252 | no_improve=0

📚 EPISODE HORIZON UPDATE at 197,568 steps:
   Episode horizon: 947 steps
[CYCLE] Update 196/401 | Step 197,568/500,000 | Episode 256 | Time: 19625.3s
   📊 Metrics: Return=+24.12% | Sharpe=2.316 | DD=10.45% | Turnover=26.18%
   🎚️ Intra-Step TAPE: potential=0.6095 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1924 | critic_loss=1.1296 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5648 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.2339 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.3156 | ema=1.5142 | best_ema=1.5142 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=2.21 | range=[1.17, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.13 | AMZN=3.36 | CAT=2.58  BOT: NEE=1.69 | KO=1.63 | MSFT=1.55
   🧬 FiLM: seq(dg=0.0118, db=0.0077, sat=0.0%) | latent(dg=0.0959, db=0.0569, sat=0.0%) | asset(dg=0.0040, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=84 (30.9%), low_vol=105 (38.6%), medium_vol=83 (30.5%)

📚 EPISODE HORIZON UPDATE at 198,576 steps:
   Episode horizon: 972 steps
[CYCLE] Update 197/401 | Step 198,576/500,000 | Episode 256 | Time: 19726.3s
   📊 Metrics: Return=+35.31% | Sharpe=2.382 | DD=10.45% | Turnover=25.48%
   🎚️ Intra-Step TAPE: potential=0.7409 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0440 | critic_loss=1.2712 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6356 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=0.0026 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.3819 | ema=1.6010 | best_ema=1.6010 | no_improve=0

📚 EPISODE HORIZON UPDATE at 199,584 steps:
   Episode horizon: 998 steps
[CYCLE] Update 198/401 | Step 199,584/500,000 | Episode 256 | Time: 19827.0s
   📊 Metrics: Return=+47.77% | Sharpe=2.471 | DD=10.45% | Turnover=25.16%
   🎚️ Intra-Step TAPE: potential=0.7198 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0657 | critic_loss=0.7536 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3768 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.1065 | router_entropy=-0.0000 | diversity_loss=0.0000 | mask=[1, 0, 0] | router=return=1.000 | risk=0.000 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.4715 | ema=1.6880 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.42 | std=2.07 | range=[1.17, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.32 | AMZN=3.23 | CAT=2.28  BOT: XOM=1.80 | MSFT=1.76 | KO=1.68
   🧬 FiLM: seq(dg=0.0114, db=0.0075, sat=0.0%) | latent(dg=0.0960, db=0.0569, sat=0.0%) | asset(dg=0.0039, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=84 (30.9%), low_vol=105 (38.6%), medium_vol=83 (30.5%)

🧭 REWARD PHASE UPDATE at 200,592 steps:
   B_ramp_1 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.25/t0.00/bm0.20/tt0.00
   objective_expert_mask=[1.0, 1.0, 0.0]
   ⏹️ Early-stop transition reset: reason=reward_phase:B_ramp_1 | grace_until=215,592 | best_ema_reset=yes

📚 EPISODE HORIZON UPDATE at 200,592 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 199/401 | Step 200,592/500,000 | Episode 256 | Time: 19927.6s
   📊 Metrics: Return=+66.35% | Sharpe=2.702 | DD=10.45% | Turnover=25.36%
   🎚️ Intra-Step TAPE: potential=0.7514 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0370 | critic_loss=0.4369 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2185 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.0906 | router_entropy=-0.0029 | diversity_loss=0.0145 | mask=[1, 1, 0] | router=return=0.708 | risk=0.292 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.7019 | ema=1.7894 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
[CYCLE] Update 200/401 | Step 201,600/500,000 | Episode 256 | Time: 20028.5s
   📊 Metrics: Return=+70.79% | Sharpe=2.454 | DD=10.45% | Turnover=25.30%
   🎚️ Intra-Step TAPE: potential=0.5917 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0584 | critic_loss=3.0512 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.5256 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0237
   🧠 Objective Experts: aux_loss=-0.1100 | router_entropy=-0.0025 | diversity_loss=0.0136 | mask=[1, 1, 0] | router=return=0.785 | risk=0.215 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.4541 | ema=1.8559 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
   🔬 Alpha Diversity: mean=2.41 | std=2.26 | range=[1.17, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.80 | AMZN=3.25 | CAT=2.65  BOT: MSFT=1.67 | NEE=1.55 | KO=1.49
   🧬 FiLM: seq(dg=0.0123, db=0.0079, sat=0.0%) | latent(dg=0.0950, db=0.0563, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=84 (30.9%), low_vol=105 (38.6%), medium_vol=83 (30.5%)
[CYCLE] Update 201/401 | Step 202,608/500,000 | Episode 256 | Time: 20129.4s
   📊 Metrics: Return=+74.70% | Sharpe=2.275 | DD=10.45% | Turnover=25.44%
   🎚️ Intra-Step TAPE: potential=0.6524 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1032 | critic_loss=1.4733 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7367 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1550 | router_entropy=-0.0025 | diversity_loss=0.0133 | mask=[1, 1, 0] | router=return=0.793 | risk=0.207 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.2751 | ema=1.8978 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
[CYCLE] Update 202/401 | Step 203,616/500,000 | Episode 256 | Time: 20230.4s
   📊 Metrics: Return=+83.74% | Sharpe=2.236 | DD=10.45% | Turnover=25.83%
   🎚️ Intra-Step TAPE: potential=0.6595 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0161 | critic_loss=1.0705 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5352 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0685 | router_entropy=-0.0027 | diversity_loss=0.0133 | mask=[1, 1, 0] | router=return=0.762 | risk=0.238 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.2356 | ema=1.9316 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
   🔬 Alpha Diversity: mean=2.45 | std=1.87 | range=[1.17, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.59 | AMZN=3.38 | GLD=3.06  BOT: JPM=1.97 | KO=1.95 | MSFT=1.61
   🧬 FiLM: seq(dg=0.0095, db=0.0066, sat=0.0%) | latent(dg=0.0928, db=0.0551, sat=0.0%) | asset(dg=0.0040, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=84 (30.9%), low_vol=105 (38.6%), medium_vol=83 (30.5%)
[CYCLE] Update 203/401 | Step 204,624/500,000 | Episode 256 | Time: 20331.1s
   📊 Metrics: Return=+96.24% | Sharpe=2.308 | DD=10.45% | Turnover=26.29%
   🎚️ Intra-Step TAPE: potential=0.7551 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1543 | critic_loss=1.2263 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6132 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.2058 | router_entropy=-0.0028 | diversity_loss=0.0129 | mask=[1, 1, 0] | router=return=0.750 | risk=0.250 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.3078 | ema=1.9692 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
[CYCLE] Update 204/401 | Step 205,632/500,000 | Episode 256 | Time: 20432.0s
   📊 Metrics: Return=+103.71% | Sharpe=2.091 | DD=10.45% | Turnover=26.31%
   🎚️ Intra-Step TAPE: potential=0.3608 | delta_reward=-0.0018
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0706 | critic_loss=0.9638 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4819 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.1220 | router_entropy=-0.0028 | diversity_loss=0.0126 | mask=[1, 1, 0] | router=return=0.752 | risk=0.248 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.0909 | ema=1.9814 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
   🔬 Alpha Diversity: mean=2.47 | std=2.18 | range=[1.17, 10.63] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.82 | NVDA=3.61 | GLD=3.03  BOT: KO=1.69 | JPM=1.61 | MSFT=1.38
   🧬 FiLM: seq(dg=0.0103, db=0.0071, sat=0.0%) | latent(dg=0.0950, db=0.0566, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=84 (30.9%), low_vol=105 (38.6%), medium_vol=83 (30.5%)
[CYCLE] Update 205/401 | Step 206,640/500,000 | Episode 256 | Time: 20533.0s
   📊 Metrics: Return=+107.37% | Sharpe=1.961 | DD=10.45% | Turnover=26.34%
   🎚️ Intra-Step TAPE: potential=0.2405 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0316 | critic_loss=1.1289 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5644 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0837 | router_entropy=-0.0028 | diversity_loss=0.0131 | mask=[1, 1, 0] | router=return=0.751 | risk=0.249 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.9610 | ema=1.9793 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
[CYCLE] Update 206/401 | Step 207,648/500,000 | Episode 256 | Time: 20634.0s
   📊 Metrics: Return=+122.80% | Sharpe=2.012 | DD=10.45% | Turnover=26.40%
   🎚️ Intra-Step TAPE: potential=0.7315 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0123 | critic_loss=1.0638 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5319 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.0647 | router_entropy=-0.0028 | diversity_loss=0.0135 | mask=[1, 1, 0] | router=return=0.744 | risk=0.256 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.0119 | ema=1.9826 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
   🔬 Alpha Diversity: mean=2.47 | std=2.26 | range=[1.17, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.64 | AMZN=4.22 | CAT=4.16  BOT: XOM=1.58 | KO=1.40 | NEE=1.35
   🧬 FiLM: seq(dg=0.0106, db=0.0073, sat=0.0%) | latent(dg=0.0944, db=0.0562, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=84 (30.9%), low_vol=105 (38.6%), medium_vol=83 (30.5%)
[CYCLE] Update 207/401 | Step 208,656/500,000 | Episode 256 | Time: 20735.0s
   📊 Metrics: Return=+78.00% | Sharpe=1.124 | DD=25.95% | Turnover=26.34%
   🎚️ Intra-Step TAPE: potential=0.2191 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0694 | critic_loss=1.3654 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6827 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.1220 | router_entropy=-0.0029 | diversity_loss=0.0136 | mask=[1, 1, 0] | router=return=0.733 | risk=0.267 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.1010 | ema=1.8944 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00257_shp1p406_actor.weights.h5 (Sharpe=1.406, MDD=15.58%)
[CYCLE] Update 208/401 | Step 209,664/500,000 | Episode 257 | Time: 20836.7s
   📊 Metrics: Return=+107.60% | Sharpe=1.406 | DD=15.58% | Turnover=26.05%
   🎚️ Intra-Step TAPE: potential=0.7182 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0580 | critic_loss=1.3043 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6521 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0250
   🧠 Objective Experts: aux_loss=-0.1107 | router_entropy=-0.0029 | diversity_loss=0.0135 | mask=[1, 1, 0] | router=return=0.730 | risk=0.270 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.4056 | ema=1.8456 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
   🔬 Alpha Diversity: mean=2.46 | std=2.16 | range=[1.17, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.55 | AMZN=5.20 | GLD=2.98  BOT: KO=1.53 | NEE=1.49 | XOM=1.45
   🧬 FiLM: seq(dg=0.0094, db=0.0066, sat=0.0%) | latent(dg=0.0907, db=0.0538, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=84 (30.8%), low_vol=105 (38.5%), medium_vol=84 (30.8%)
   🔒 Drawdown λ snapshot=0.045 (peak 0.078, dd 8.15% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5807
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=0.00352) | SPY shaping=0.001 (SPY ret=0.00243)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00258_shp1p355_actor.weights.h5 (Sharpe=1.355, MDD=17.16%)
[CYCLE] Update 209/401 | Step 210,672/500,000 | Episode 258 | Time: 20938.3s
   📊 Metrics: Return=+115.81% | Sharpe=1.355 | DD=17.16% | Turnover=26.08%
   🎚️ Intra-Step TAPE: potential=0.2538 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0230 | critic_loss=1.1847 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5923 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0748 | router_entropy=-0.0029 | diversity_loss=0.0127 | mask=[1, 1, 0] | router=return=0.718 | risk=0.282 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3550 | ema=1.7965 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
   🔒 Drawdown λ snapshot=0.000 (peak 0.078, dd 6.58% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.5690
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=0.00352) | SPY shaping=0.000 (SPY ret=0.00243)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00259_shp1p289_actor.weights.h5 (Sharpe=1.289, MDD=18.13%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00263_shp1p041_actor.weights.h5 (Sharpe=1.041, MDD=22.18%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00267_shp1p246_actor.weights.h5 (Sharpe=1.246, MDD=14.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00269_shp0p852_actor.weights.h5 (Sharpe=0.852, MDD=12.16%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00270_shp1p028_actor.weights.h5 (Sharpe=1.028, MDD=23.38%)
[CYCLE] Update 210/401 | Step 211,680/500,000 | Episode 272 | Time: 21041.8s
   📊 Metrics: Return=+16.48% | Sharpe=0.192 | DD=25.68% | Turnover=25.79%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1020 | critic_loss=3.1602 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.5801 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.1552 | router_entropy=-0.0029 | diversity_loss=0.0137 | mask=[1, 1, 0] | router=return=0.714 | risk=0.286 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1759 | ema=1.6344 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
   🔬 Alpha Diversity: mean=2.51 | std=2.15 | range=[1.17, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.64 | AMZN=3.25 | CAT=3.05  BOT: NEE=1.47 | XOM=1.40 | KO=1.38
   🧬 FiLM: seq(dg=0.0109, db=0.0074, sat=0.0%) | latent(dg=0.0915, db=0.0544, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=92 (31.9%), low_vol=109 (37.8%), medium_vol=87 (30.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.217) | TAPE=0.2394
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=-0.00133) | SPY shaping=-0.001 (SPY ret=-0.00016)
[CYCLE] Update 211/401 | Step 212,688/500,000 | Episode 272 | Time: 21142.6s
   📊 Metrics: Return=-0.59% | Sharpe=-0.285 | DD=5.98% | Turnover=26.04%
   🎚️ Intra-Step TAPE: potential=0.2493 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0842 | critic_loss=1.6515 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8258 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.1387 | router_entropy=-0.0031 | diversity_loss=0.0150 | mask=[1, 1, 0] | router=return=0.672 | risk=0.328 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.2848 | ema=1.4425 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
[CYCLE] Update 212/401 | Step 213,696/500,000 | Episode 272 | Time: 21243.5s
   📊 Metrics: Return=+8.17% | Sharpe=0.962 | DD=9.05% | Turnover=26.75%
   🎚️ Intra-Step TAPE: potential=0.6722 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0911 | critic_loss=1.4907 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7453 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1439 | router_entropy=-0.0031 | diversity_loss=0.0145 | mask=[1, 1, 0] | router=return=0.665 | risk=0.335 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9624 | ema=1.3945 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
   🔬 Alpha Diversity: mean=2.46 | std=2.33 | range=[1.17, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.50 | NVDA=5.44 | CAT=2.29  BOT: NEE=1.38 | BRK-B=1.34 | KO=1.31
   🧬 FiLM: seq(dg=0.0145, db=0.0093, sat=0.0%) | latent(dg=0.0963, db=0.0573, sat=0.0%) | asset(dg=0.0045, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=92 (31.9%), low_vol=109 (37.8%), medium_vol=87 (30.2%)
[CYCLE] Update 213/401 | Step 214,704/500,000 | Episode 272 | Time: 21344.5s
   📊 Metrics: Return=+4.10% | Sharpe=0.278 | DD=10.85% | Turnover=26.94%
   🎚️ Intra-Step TAPE: potential=0.2454 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0470 | critic_loss=1.0588 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5294 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0989 | router_entropy=-0.0031 | diversity_loss=0.0136 | mask=[1, 1, 0] | router=return=0.665 | risk=0.335 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2779 | ema=1.2828 | best_ema=1.6880 | no_improve=0 | grace_until=215,592
[CYCLE] Update 214/401 | Step 215,712/500,000 | Episode 272 | Time: 21445.4s
   📊 Metrics: Return=+20.84% | Sharpe=1.110 | DD=11.91% | Turnover=26.27%
   🎚️ Intra-Step TAPE: potential=0.7396 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0398 | critic_loss=0.9603 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4801 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.0922 | router_entropy=-0.0030 | diversity_loss=0.0143 | mask=[1, 1, 0] | router=return=0.684 | risk=0.316 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.1100 | ema=1.2656 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.46 | std=2.17 | range=[1.16, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.07 | AMZN=4.00 | CAT=2.68  BOT: XOM=1.60 | KO=1.60 | NEE=1.55
   🧬 FiLM: seq(dg=0.0158, db=0.0103, sat=0.0%) | latent(dg=0.1083, db=0.0647, sat=0.0%) | asset(dg=0.0045, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=92 (31.9%), low_vol=109 (37.8%), medium_vol=87 (30.2%)
[CYCLE] Update 215/401 | Step 216,720/500,000 | Episode 272 | Time: 21546.4s
   📊 Metrics: Return=+31.64% | Sharpe=1.345 | DD=11.91% | Turnover=26.04%
   🎚️ Intra-Step TAPE: potential=0.7259 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0261 | critic_loss=0.9618 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4809 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   🧠 Objective Experts: aux_loss=-0.0785 | router_entropy=-0.0030 | diversity_loss=0.0148 | mask=[1, 1, 0] | router=return=0.686 | risk=0.314 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3447 | ema=1.2735 | best_ema=1.6880 | no_improve=0
[CYCLE] Update 216/401 | Step 217,728/500,000 | Episode 272 | Time: 21647.3s
   📊 Metrics: Return=+34.52% | Sharpe=1.254 | DD=11.91% | Turnover=26.16%
   🎚️ Intra-Step TAPE: potential=0.3649 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0966 | critic_loss=1.0891 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5445 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.1484 | router_entropy=-0.0030 | diversity_loss=0.0141 | mask=[1, 1, 0] | router=return=0.681 | risk=0.319 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2543 | ema=1.2715 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.24 | range=[1.16, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.81 | GLD=3.24 | AMZN=2.93  BOT: XOM=1.59 | BRK-B=1.56 | JPM=1.55
   🧬 FiLM: seq(dg=0.0141, db=0.0091, sat=0.0%) | latent(dg=0.0984, db=0.0586, sat=0.0%) | asset(dg=0.0042, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=92 (31.9%), low_vol=109 (37.8%), medium_vol=87 (30.2%)
[CYCLE] Update 217/401 | Step 218,736/500,000 | Episode 272 | Time: 21748.1s
   📊 Metrics: Return=+48.82% | Sharpe=1.500 | DD=11.91% | Turnover=26.64%
   🎚️ Intra-Step TAPE: potential=0.7540 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1647 | critic_loss=1.0268 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5134 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.2162 | router_entropy=-0.0030 | diversity_loss=0.0138 | mask=[1, 1, 0] | router=return=0.686 | risk=0.314 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.5000 | ema=1.2944 | best_ema=1.6880 | no_improve=0
[CYCLE] Update 218/401 | Step 219,744/500,000 | Episode 272 | Time: 21848.7s
   📊 Metrics: Return=+52.50% | Sharpe=1.421 | DD=11.91% | Turnover=26.46%
   🎚️ Intra-Step TAPE: potential=0.2480 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1186 | critic_loss=1.2158 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6079 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.1708 | router_entropy=-0.0029 | diversity_loss=0.0144 | mask=[1, 1, 0] | router=return=0.723 | risk=0.277 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.4208 | ema=1.3070 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.42 | std=2.36 | range=[1.16, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.53 | AMZN=2.81 | GLD=2.41  BOT: KO=1.52 | XOM=1.49 | NEE=1.48
   🧬 FiLM: seq(dg=0.0130, db=0.0084, sat=0.0%) | latent(dg=0.0948, db=0.0564, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=92 (31.9%), low_vol=109 (37.8%), medium_vol=87 (30.2%)
[CYCLE] Update 219/401 | Step 220,752/500,000 | Episode 272 | Time: 21949.6s
   📊 Metrics: Return=+70.47% | Sharpe=1.623 | DD=11.91% | Turnover=26.64%
   🎚️ Intra-Step TAPE: potential=0.7546 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0352 | critic_loss=0.9020 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4510 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.0888 | router_entropy=-0.0029 | diversity_loss=0.0156 | mask=[1, 1, 0] | router=return=0.721 | risk=0.279 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.6229 | ema=1.3386 | best_ema=1.6880 | no_improve=0
[CYCLE] Update 220/401 | Step 221,760/500,000 | Episode 272 | Time: 22050.5s
   📊 Metrics: Return=+82.84% | Sharpe=1.697 | DD=11.91% | Turnover=26.58%
   🎚️ Intra-Step TAPE: potential=0.7482 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1187 | critic_loss=0.8467 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4234 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1724 | router_entropy=-0.0029 | diversity_loss=0.0154 | mask=[1, 1, 0] | router=return=0.710 | risk=0.290 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.6968 | ema=1.3744 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.43 | std=1.96 | range=[1.16, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.27 | NVDA=4.60 | JPM=2.12  BOT: XOM=1.87 | MSFT=1.84 | BRK-B=1.82
   🧬 FiLM: seq(dg=0.0120, db=0.0080, sat=0.0%) | latent(dg=0.0974, db=0.0579, sat=0.0%) | asset(dg=0.0044, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=92 (31.9%), low_vol=109 (37.8%), medium_vol=87 (30.2%)
[CYCLE] Update 221/401 | Step 222,768/500,000 | Episode 272 | Time: 22151.3s
   📊 Metrics: Return=+107.53% | Sharpe=1.925 | DD=11.91% | Turnover=26.65%
   🎚️ Intra-Step TAPE: potential=0.7559 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0041 | critic_loss=0.9804 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4902 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.0488 | router_entropy=-0.0029 | diversity_loss=0.0148 | mask=[1, 1, 0] | router=return=0.705 | risk=0.295 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.9250 | ema=1.4295 | best_ema=1.6880 | no_improve=0
[CYCLE] Update 222/401 | Step 223,776/500,000 | Episode 272 | Time: 22252.2s
   📊 Metrics: Return=+107.03% | Sharpe=1.685 | DD=11.91% | Turnover=26.51%
   🎚️ Intra-Step TAPE: potential=0.2326 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1193 | critic_loss=0.8164 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4082 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.1721 | router_entropy=-0.0030 | diversity_loss=0.0143 | mask=[1, 1, 0] | router=return=0.685 | risk=0.315 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.6851 | ema=1.4551 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.48 | std=2.28 | range=[1.17, 10.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.79 | NVDA=4.77 | CAT=3.18  BOT: XOM=1.53 | NEE=1.38 | KO=1.35
   🧬 FiLM: seq(dg=0.0119, db=0.0080, sat=0.0%) | latent(dg=0.1008, db=0.0600, sat=0.0%) | asset(dg=0.0045, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=92 (31.9%), low_vol=109 (37.8%), medium_vol=87 (30.2%)
[CYCLE] Update 223/401 | Step 224,784/500,000 | Episode 272 | Time: 22353.4s
   📊 Metrics: Return=+114.60% | Sharpe=1.664 | DD=11.91% | Turnover=26.58%
   🎚️ Intra-Step TAPE: potential=0.6116 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0045 | critic_loss=0.9096 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4548 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0249
   🧠 Objective Experts: aux_loss=-0.0473 | router_entropy=-0.0029 | diversity_loss=0.0130 | mask=[1, 1, 0] | router=return=0.720 | risk=0.280 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.6637 | ema=1.4759 | best_ema=1.6880 | no_improve=0
[CYCLE] Update 224/401 | Step 225,792/500,000 | Episode 273 | Time: 22454.2s
   📊 Metrics: Return=+3.38% | Sharpe=0.013 | DD=21.87% | Turnover=25.64%
   🎚️ Intra-Step TAPE: potential=0.2253 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0376 | critic_loss=1.0564 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5282 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.0901 | router_entropy=-0.0030 | diversity_loss=0.0138 | mask=[1, 1, 0] | router=return=0.686 | risk=0.314 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0128 | ema=1.3296 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.47 | std=2.33 | range=[1.17, 10.36] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.50 | CAT=2.90 | AMZN=2.57  BOT: BRK-B=1.41 | NEE=1.33 | KO=1.31
   🧬 FiLM: seq(dg=0.0117, db=0.0079, sat=0.0%) | latent(dg=0.0982, db=0.0585, sat=0.0%) | asset(dg=0.0045, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=92 (31.8%), low_vol=110 (38.1%), medium_vol=87 (30.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 6.97% / trig 16.50%) | terminal=0.000 (peak 0.013) | TAPE=0.2365
   📈 Benchmark Relative: 1/N shaping=0.003 (EW ret=0.00534) | SPY shaping=0.001 (SPY ret=0.00318)
[CYCLE] Update 225/401 | Step 226,800/500,000 | Episode 274 | Time: 22555.2s
   📊 Metrics: Return=+63.37% | Sharpe=0.594 | DD=26.32% | Turnover=25.29%
   🎚️ Intra-Step TAPE: potential=0.2338 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0205 | critic_loss=0.9834 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4917 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0735 | router_entropy=-0.0030 | diversity_loss=0.0146 | mask=[1, 1, 0] | router=return=0.682 | risk=0.318 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5619 | ema=1.2528 | best_ema=1.6880 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.011, dd 9.74% / trig 16.50%) | terminal=0.240 (peak 0.323) | TAPE=0.3191
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=0.00687) | SPY shaping=0.001 (SPY ret=0.00405)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00275_shp1p015_actor.weights.h5 (Sharpe=1.015, MDD=21.00%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00276_shp1p218_actor.weights.h5 (Sharpe=1.218, MDD=21.03%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00278_shp1p259_actor.weights.h5 (Sharpe=1.259, MDD=20.01%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00287_shp1p597_actor.weights.h5 (Sharpe=1.597, MDD=10.25%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00288_shp1p320_actor.weights.h5 (Sharpe=1.320, MDD=11.71%)
[CYCLE] Update 226/401 | Step 227,808/500,000 | Episode 288 | Time: 22658.7s
   📊 Metrics: Return=+110.65% | Sharpe=1.320 | DD=11.71% | Turnover=26.58%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0074 | critic_loss=3.4889 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.7445 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.0447 | router_entropy=-0.0030 | diversity_loss=0.0138 | mask=[1, 1, 0] | router=return=0.684 | risk=0.316 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3199 | ema=1.2595 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=2.35 | range=[1.16, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.62 | AMZN=4.74 | GLD=2.49  BOT: BRK-B=1.43 | KO=1.41 | NEE=1.36
   🧬 FiLM: seq(dg=0.0130, db=0.0086, sat=0.0%) | latent(dg=0.0992, db=0.0592, sat=0.0%) | asset(dg=0.0044, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (31.9%), low_vol=116 (38.2%), medium_vol=91 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.31% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5803
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=0.01622) | SPY shaping=-0.001 (SPY ret=0.01594)
[CYCLE] Update 227/401 | Step 228,816/500,000 | Episode 288 | Time: 22759.4s
   📊 Metrics: Return=+2.49% | Sharpe=0.513 | DD=5.31% | Turnover=26.15%
   🎚️ Intra-Step TAPE: potential=0.2634 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0609 | critic_loss=1.8498 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.9249 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=0.0086 | router_entropy=-0.0030 | diversity_loss=0.0140 | mask=[1, 1, 0] | router=return=0.686 | risk=0.314 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5132 | ema=1.1849 | best_ema=1.6880 | no_improve=0
[CYCLE] Update 228/401 | Step 229,824/500,000 | Episode 288 | Time: 22860.2s
   📊 Metrics: Return=+6.31% | Sharpe=0.670 | DD=8.59% | Turnover=26.90%
   🎚️ Intra-Step TAPE: potential=0.5723 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1121 | critic_loss=1.3306 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6653 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=-0.1629 | router_entropy=-0.0029 | diversity_loss=0.0128 | mask=[1, 1, 0] | router=return=0.722 | risk=0.278 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6697 | ema=1.1334 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.42 | std=2.41 | range=[1.17, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.73 | NVDA=4.43 | GLD=2.14  BOT: XOM=1.42 | KO=1.41 | NEE=1.41
   🧬 FiLM: seq(dg=0.0134, db=0.0087, sat=0.0%) | latent(dg=0.1002, db=0.0597, sat=0.0%) | asset(dg=0.0044, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (31.9%), low_vol=116 (38.2%), medium_vol=91 (29.9%)
[CYCLE] Update 229/401 | Step 230,832/500,000 | Episode 288 | Time: 22961.0s
   📊 Metrics: Return=+1.80% | Sharpe=0.094 | DD=8.59% | Turnover=26.35%
   🎚️ Intra-Step TAPE: potential=0.2401 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0385 | critic_loss=0.8290 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4145 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.0135 | router_entropy=-0.0029 | diversity_loss=0.0137 | mask=[1, 1, 0] | router=return=0.731 | risk=0.269 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0936 | ema=1.0294 | best_ema=1.6880 | no_improve=0
[CYCLE] Update 230/401 | Step 231,840/500,000 | Episode 288 | Time: 23061.8s
   📊 Metrics: Return=+6.05% | Sharpe=0.322 | DD=10.29% | Turnover=26.33%
   🎚️ Intra-Step TAPE: potential=0.7410 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1375 | critic_loss=0.7783 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3891 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=0.0846 | router_entropy=-0.0030 | diversity_loss=0.0151 | mask=[1, 1, 0] | router=return=0.698 | risk=0.302 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3225 | ema=0.9587 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.45 | std=2.27 | range=[1.16, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.07 | AMZN=3.72 | JPM=1.97  BOT: BRK-B=1.65 | GLD=1.53 | XOM=1.48
   🧬 FiLM: seq(dg=0.0149, db=0.0095, sat=0.0%) | latent(dg=0.1026, db=0.0613, sat=0.0%) | asset(dg=0.0045, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (31.9%), low_vol=116 (38.2%), medium_vol=91 (29.9%)
[CYCLE] Update 231/401 | Step 232,848/500,000 | Episode 288 | Time: 23162.8s
   📊 Metrics: Return=+12.43% | Sharpe=0.579 | DD=10.29% | Turnover=26.31%
   🎚️ Intra-Step TAPE: potential=0.6714 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0851 | critic_loss=0.8587 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4294 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   🧠 Objective Experts: aux_loss=0.0325 | router_entropy=-0.0029 | diversity_loss=0.0153 | mask=[1, 1, 0] | router=return=0.695 | risk=0.305 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5791 | ema=0.9208 | best_ema=1.6880 | no_improve=0
[CYCLE] Update 232/401 | Step 233,856/500,000 | Episode 288 | Time: 23263.8s
   📊 Metrics: Return=+9.67% | Sharpe=0.365 | DD=10.29% | Turnover=26.16%
   🎚️ Intra-Step TAPE: potential=0.2251 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0437 | critic_loss=1.1372 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5686 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=-0.0954 | router_entropy=-0.0030 | diversity_loss=0.0139 | mask=[1, 1, 0] | router=return=0.688 | risk=0.312 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3649 | ema=0.8652 | best_ema=1.6880 | no_improve=0
   🔬 Alpha Diversity: mean=2.44 | std=2.20 | range=[1.16, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.10 | AMZN=4.42 | GLD=2.64  BOT: NEE=1.81 | JPM=1.80 | BRK-B=1.74
   🧬 FiLM: seq(dg=0.0136, db=0.0088, sat=0.0%) | latent(dg=0.0994, db=0.0593, sat=0.0%) | asset(dg=0.0044, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (31.9%), low_vol=116 (38.2%), medium_vol=91 (29.9%)
[CYCLE] Update 233/401 | Step 234,864/500,000 | Episode 288 | Time: 23364.7s
   📊 Metrics: Return=+15.40% | Sharpe=0.525 | DD=10.29% | Turnover=26.59%
   🎚️ Intra-Step TAPE: potential=0.6979 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0522 | critic_loss=0.9179 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4590 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=0.0009 | router_entropy=-0.0029 | diversity_loss=0.0130 | mask=[1, 1, 0] | router=return=0.720 | risk=0.280 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5249 | ema=0.8311 | best_ema=1.6880 | no_improve=0

🎛️ EXECUTION BETA UPDATE at 235,872 steps:
   action_execution_beta: 0.650 (w_exec=(1-β)w_prev + βw_raw)
   ⏹️ Early-stop transition reset: reason=action_execution_beta_update | grace_until=250,872 | best_ema_reset=yes
[CYCLE] Update 234/401 | Step 235,872/500,000 | Episode 288 | Time: 23465.6s
   📊 Metrics: Return=+16.78% | Sharpe=0.502 | DD=10.29% | Turnover=26.83%
   🎚️ Intra-Step TAPE: potential=0.2498 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0855 | critic_loss=1.0972 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5486 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.1375 | router_entropy=-0.0028 | diversity_loss=0.0136 | mask=[1, 1, 0] | router=return=0.740 | risk=0.260 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5020 | ema=0.7982 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔬 Alpha Diversity: mean=2.48 | std=1.92 | range=[1.16, 10.44] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.69 | AMZN=2.45 | KO=2.31  BOT: NEE=2.05 | GLD=1.88 | CAT=1.87
   🧬 FiLM: seq(dg=0.0119, db=0.0079, sat=0.0%) | latent(dg=0.0991, db=0.0590, sat=0.0%) | asset(dg=0.0040, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (31.9%), low_vol=116 (38.2%), medium_vol=91 (29.9%)
[CYCLE] Update 235/401 | Step 236,880/500,000 | Episode 288 | Time: 23566.5s
   📊 Metrics: Return=+16.39% | Sharpe=0.426 | DD=10.29% | Turnover=27.30%
   🎚️ Intra-Step TAPE: potential=0.2280 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0129 | critic_loss=0.9582 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4791 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.0388 | router_entropy=-0.0029 | diversity_loss=0.0136 | mask=[1, 1, 0] | router=return=0.726 | risk=0.274 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4260 | ema=0.7610 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
[CYCLE] Update 236/401 | Step 237,888/500,000 | Episode 288 | Time: 23667.6s
   📊 Metrics: Return=+21.29% | Sharpe=0.504 | DD=10.29% | Turnover=27.76%
   🎚️ Intra-Step TAPE: potential=0.6212 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0052 | critic_loss=0.8936 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4468 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.0465 | router_entropy=-0.0029 | diversity_loss=0.0137 | mask=[1, 1, 0] | router=return=0.722 | risk=0.278 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5044 | ema=0.7353 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔬 Alpha Diversity: mean=2.42 | std=1.94 | range=[1.15, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.06 | AMZN=3.94 | GLD=2.38  BOT: BRK-B=1.92 | NEE=1.91 | MSFT=1.87
   🧬 FiLM: seq(dg=0.0114, db=0.0076, sat=0.0%) | latent(dg=0.0969, db=0.0576, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (31.9%), low_vol=116 (38.2%), medium_vol=91 (29.9%)
[CYCLE] Update 237/401 | Step 238,896/500,000 | Episode 288 | Time: 23768.5s
   📊 Metrics: Return=+21.78% | Sharpe=0.464 | DD=10.29% | Turnover=28.03%
   🎚️ Intra-Step TAPE: potential=0.2425 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0984 | critic_loss=1.1778 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5889 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=0.0474 | router_entropy=-0.0028 | diversity_loss=0.0126 | mask=[1, 1, 0] | router=return=0.742 | risk=0.258 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4644 | ema=0.7083 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
[CYCLE] Update 238/401 | Step 239,904/500,000 | Episode 288 | Time: 23869.6s
   📊 Metrics: Return=+19.99% | Sharpe=0.374 | DD=10.29% | Turnover=28.48%
   🎚️ Intra-Step TAPE: potential=0.2283 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0082 | critic_loss=0.9284 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4642 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.0434 | router_entropy=-0.0029 | diversity_loss=0.0131 | mask=[1, 1, 0] | router=return=0.731 | risk=0.269 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3738 | ema=0.6748 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔬 Alpha Diversity: mean=2.46 | std=2.09 | range=[1.15, 10.50] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.98 | AMZN=3.23 | CAT=3.13  BOT: GLD=1.63 | KO=1.61 | NEE=1.51
   🧬 FiLM: seq(dg=0.0109, db=0.0073, sat=0.0%) | latent(dg=0.0946, db=0.0562, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (31.9%), low_vol=116 (38.2%), medium_vol=91 (29.9%)
[CYCLE] Update 239/401 | Step 240,912/500,000 | Episode 288 | Time: 23970.6s
   📊 Metrics: Return=+23.91% | Sharpe=0.413 | DD=10.29% | Turnover=28.54%
   🎚️ Intra-Step TAPE: potential=0.5234 | delta_reward=+0.0021
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1010 | critic_loss=1.1708 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5854 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.1527 | router_entropy=-0.0028 | diversity_loss=0.0129 | mask=[1, 1, 0] | router=return=0.751 | risk=0.249 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4134 | ema=0.6487 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00289_shp1p431_actor.weights.h5 (Sharpe=1.431, MDD=11.69%)
[CYCLE] Update 240/401 | Step 241,920/500,000 | Episode 289 | Time: 24072.0s
   📊 Metrics: Return=+120.79% | Sharpe=1.431 | DD=11.69% | Turnover=27.68%
   🎚️ Intra-Step TAPE: potential=0.3551 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0639 | critic_loss=1.1373 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5687 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=0.0129 | router_entropy=-0.0027 | diversity_loss=0.0122 | mask=[1, 1, 0] | router=return=0.770 | risk=0.230 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.4315 | ema=0.7270 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔬 Alpha Diversity: mean=2.45 | std=2.27 | range=[1.15, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.85 | AMZN=4.51 | CAT=2.69  BOT: NEE=1.43 | KO=1.43 | GLD=1.35
   🧬 FiLM: seq(dg=0.0091, db=0.0065, sat=0.0%) | latent(dg=0.0973, db=0.0578, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=97 (31.8%), low_vol=116 (38.0%), medium_vol=92 (30.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.27% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.6010
   📈 Benchmark Relative: 1/N shaping=-0.000 (EW ret=0.00335) | SPY shaping=0.001 (SPY ret=0.00042)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00290_shp1p402_actor.weights.h5 (Sharpe=1.402, MDD=12.71%)
[CYCLE] Update 241/401 | Step 242,928/500,000 | Episode 290 | Time: 24173.3s
   📊 Metrics: Return=+122.56% | Sharpe=1.402 | DD=12.71% | Turnover=28.50%
   🎚️ Intra-Step TAPE: potential=0.6905 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0668 | critic_loss=1.1263 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5632 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0251
   🧠 Objective Experts: aux_loss=-0.1180 | router_entropy=-0.0026 | diversity_loss=0.0118 | mask=[1, 1, 0] | router=return=0.784 | risk=0.216 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.4022 | ema=0.7945 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.93% / trig 16.50%) | terminal=0.000 (peak 0.180) | TAPE=0.5931
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=0.01021) | SPY shaping=-0.000 (SPY ret=0.00935)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00291_shp1p105_actor.weights.h5 (Sharpe=1.105, MDD=20.75%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00294_shp1p126_actor.weights.h5 (Sharpe=1.126, MDD=23.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00295_shp1p416_actor.weights.h5 (Sharpe=1.416, MDD=10.31%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00299_shp1p284_actor.weights.h5 (Sharpe=1.284, MDD=12.64%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00301_shp1p464_actor.weights.h5 (Sharpe=1.464, MDD=10.64%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00302_shp1p449_actor.weights.h5 (Sharpe=1.449, MDD=11.47%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00303_shp1p041_actor.weights.h5 (Sharpe=1.041, MDD=11.56%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00304_shp0p909_actor.weights.h5 (Sharpe=0.909, MDD=13.69%)
[CYCLE] Update 242/401 | Step 243,936/500,000 | Episode 304 | Time: 24278.2s
   📊 Metrics: Return=+69.55% | Sharpe=0.909 | DD=13.69% | Turnover=28.56%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0761 | critic_loss=4.2724 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.1362 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=0.0253 | router_entropy=-0.0027 | diversity_loss=0.0119 | mask=[1, 1, 0] | router=return=0.766 | risk=0.234 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9089 | ema=0.8059 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔬 Alpha Diversity: mean=2.45 | std=2.31 | range=[1.15, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.63 | AMZN=3.37 | CAT=2.44  BOT: GLD=1.51 | BRK-B=1.44 | NEE=1.44
   🧬 FiLM: seq(dg=0.0118, db=0.0080, sat=0.0%) | latent(dg=0.1003, db=0.0597, sat=0.0%) | asset(dg=0.0040, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (31.6%), low_vol=123 (38.4%), medium_vol=96 (30.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.11% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4868
   📈 Benchmark Relative: 1/N shaping=0.000 (EW ret=0.00147) | SPY shaping=0.000 (SPY ret=0.00127)
[CYCLE] Update 243/401 | Step 244,944/500,000 | Episode 304 | Time: 24378.7s
   📊 Metrics: Return=+5.40% | Sharpe=1.272 | DD=4.95% | Turnover=28.88%
   🎚️ Intra-Step TAPE: potential=0.5432 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0250 | critic_loss=1.6853 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8427 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.0770 | router_entropy=-0.0028 | diversity_loss=0.0134 | mask=[1, 1, 0] | router=return=0.720 | risk=0.280 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.2723 | ema=0.8526 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
[CYCLE] Update 244/401 | Step 245,952/500,000 | Episode 304 | Time: 24479.5s
   📊 Metrics: Return=+6.79% | Sharpe=0.974 | DD=4.95% | Turnover=31.58%
   🎚️ Intra-Step TAPE: potential=0.3085 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0384 | critic_loss=0.9987 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4994 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0240
   🧠 Objective Experts: aux_loss=-0.0902 | router_entropy=-0.0029 | diversity_loss=0.0136 | mask=[1, 1, 0] | router=return=0.716 | risk=0.284 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9741 | ema=0.8647 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔬 Alpha Diversity: mean=2.46 | std=2.16 | range=[1.15, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.01 | AMZN=4.05 | GLD=2.16  BOT: BRK-B=1.68 | XOM=1.67 | KO=1.55
   🧬 FiLM: seq(dg=0.0144, db=0.0094, sat=0.0%) | latent(dg=0.1065, db=0.0635, sat=0.0%) | asset(dg=0.0042, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (31.6%), low_vol=123 (38.4%), medium_vol=96 (30.0%)
[CYCLE] Update 245/401 | Step 246,960/500,000 | Episode 304 | Time: 24580.3s
   📊 Metrics: Return=+8.06% | Sharpe=0.793 | DD=4.95% | Turnover=32.11%
   🎚️ Intra-Step TAPE: potential=0.2734 | delta_reward=-0.0032
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0642 | critic_loss=0.6099 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3049 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1167 | router_entropy=-0.0029 | diversity_loss=0.0143 | mask=[1, 1, 0] | router=return=0.718 | risk=0.282 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7931 | ema=0.8576 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
[CYCLE] Update 246/401 | Step 247,968/500,000 | Episode 304 | Time: 24681.1s
   📊 Metrics: Return=+10.70% | Sharpe=0.758 | DD=5.74% | Turnover=31.68%
   🎚️ Intra-Step TAPE: potential=0.4655 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0829 | critic_loss=0.6283 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3141 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   🧠 Objective Experts: aux_loss=-0.1359 | router_entropy=-0.0030 | diversity_loss=0.0156 | mask=[1, 1, 0] | router=return=0.700 | risk=0.300 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7581 | ema=0.8476 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔬 Alpha Diversity: mean=2.43 | std=2.24 | range=[1.15, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=6.17 | NVDA=4.54 | JPM=2.01  BOT: XOM=1.64 | KO=1.61 | GLD=1.46
   🧬 FiLM: seq(dg=0.0151, db=0.0096, sat=0.0%) | latent(dg=0.1051, db=0.0627, sat=0.0%) | asset(dg=0.0045, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (31.6%), low_vol=123 (38.4%), medium_vol=96 (30.0%)
[CYCLE] Update 247/401 | Step 248,976/500,000 | Episode 304 | Time: 24782.0s
   📊 Metrics: Return=+13.33% | Sharpe=0.754 | DD=6.48% | Turnover=31.81%
   🎚️ Intra-Step TAPE: potential=0.6855 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0484 | critic_loss=0.9022 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4511 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   🧠 Objective Experts: aux_loss=-0.0041 | router_entropy=-0.0030 | diversity_loss=0.0158 | mask=[1, 1, 0] | router=return=0.677 | risk=0.323 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7544 | ema=0.8383 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
[CYCLE] Update 248/401 | Step 249,984/500,000 | Episode 304 | Time: 24882.9s
   📊 Metrics: Return=+6.90% | Sharpe=0.260 | DD=8.82% | Turnover=32.03%
   🎚️ Intra-Step TAPE: potential=0.2350 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0974 | critic_loss=0.7147 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3574 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=0.0451 | router_entropy=-0.0030 | diversity_loss=0.0142 | mask=[1, 1, 0] | router=return=0.697 | risk=0.303 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2604 | ema=0.7805 | best_ema=0.8311 | no_improve=0 | grace_until=250,872
   🔬 Alpha Diversity: mean=2.42 | std=2.08 | range=[1.15, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.03 | AMZN=4.45 | CAT=2.49  BOT: NEE=1.69 | KO=1.55 | BRK-B=1.48
   🧬 FiLM: seq(dg=0.0126, db=0.0083, sat=0.0%) | latent(dg=0.1002, db=0.0597, sat=0.0%) | asset(dg=0.0044, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (31.6%), low_vol=123 (38.4%), medium_vol=96 (30.0%)
[CYCLE] Update 249/401 | Step 250,992/500,000 | Episode 304 | Time: 24984.1s
   📊 Metrics: Return=+8.58% | Sharpe=0.280 | DD=8.82% | Turnover=32.00%
   🎚️ Intra-Step TAPE: potential=0.2629 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0436 | critic_loss=0.6286 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3143 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.0078 | router_entropy=-0.0029 | diversity_loss=0.0129 | mask=[1, 1, 0] | router=return=0.732 | risk=0.268 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2801 | ema=0.7305 | best_ema=0.8311 | no_improve=1

📚 PPO ROLLOUT UPDATE at 250,992 steps:
   Timesteps per update: 1512
   ⏹️ Early-stop transition reset: reason=rollout_update | grace_until=265,992 | best_ema_reset=yes
[CYCLE] Update 250/401 | Step 252,504/500,000 | Episode 304 | Time: 25140.6s
   📊 Metrics: Return=+13.09% | Sharpe=0.363 | DD=9.33% | Turnover=31.69%
   🎚️ Intra-Step TAPE: potential=0.6969 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1236 | critic_loss=0.7794 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3897 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.1746 | router_entropy=-0.0028 | diversity_loss=0.0121 | mask=[1, 1, 0] | router=return=0.758 | risk=0.242 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3629 | ema=0.6937 | best_ema=0.7305 | no_improve=0 | grace_until=265,992
   🔬 Alpha Diversity: mean=2.46 | std=2.03 | range=[1.15, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.25 | MSFT=2.91 | AMZN=2.62  BOT: KO=2.11 | JPM=1.94 | BRK-B=1.87
   🧬 FiLM: seq(dg=0.0092, db=0.0066, sat=0.0%) | latent(dg=0.0974, db=0.0581, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (31.6%), low_vol=123 (38.4%), medium_vol=96 (30.0%)
[CYCLE] Update 251/401 | Step 254,016/500,000 | Episode 304 | Time: 25292.3s
   📊 Metrics: Return=+20.13% | Sharpe=0.468 | DD=9.49% | Turnover=31.80%
   🎚️ Intra-Step TAPE: potential=0.6804 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0001 | critic_loss=1.0044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.0511 | router_entropy=-0.0028 | diversity_loss=0.0127 | mask=[1, 1, 0] | router=return=0.735 | risk=0.265 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4683 | ema=0.6712 | best_ema=0.7305 | no_improve=0 | grace_until=265,992
[CYCLE] Update 252/401 | Step 255,528/500,000 | Episode 304 | Time: 25444.1s
   📊 Metrics: Return=+23.29% | Sharpe=0.439 | DD=12.92% | Turnover=31.61%
   🎚️ Intra-Step TAPE: potential=0.2845 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0112 | critic_loss=0.9089 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4544 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0232
   🧠 Objective Experts: aux_loss=-0.0397 | router_entropy=-0.0030 | diversity_loss=0.0138 | mask=[1, 1, 0] | router=return=0.704 | risk=0.296 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4393 | ema=0.6480 | best_ema=0.7305 | no_improve=0 | grace_until=265,992
   🔬 Alpha Diversity: mean=2.41 | std=2.28 | range=[1.15, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.72 | AMZN=4.63 | CAT=2.57  BOT: KO=1.56 | BRK-B=1.52 | GLD=1.50
   🧬 FiLM: seq(dg=0.0145, db=0.0093, sat=0.0%) | latent(dg=0.1080, db=0.0645, sat=0.0%) | asset(dg=0.0045, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (31.6%), low_vol=123 (38.4%), medium_vol=96 (30.0%)
[CYCLE] Update 253/401 | Step 257,040/500,000 | Episode 304 | Time: 25595.9s
   📊 Metrics: Return=+40.08% | Sharpe=0.664 | DD=12.92% | Turnover=31.54%
   🎚️ Intra-Step TAPE: potential=0.6219 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0147 | critic_loss=0.8350 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4175 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.0660 | router_entropy=-0.0028 | diversity_loss=0.0129 | mask=[1, 1, 0] | router=return=0.736 | risk=0.264 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6643 | ema=0.6496 | best_ema=0.7305 | no_improve=0 | grace_until=265,992
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00305_shp1p119_actor.weights.h5 (Sharpe=1.119, MDD=12.28%)
[CYCLE] Update 254/401 | Step 258,552/500,000 | Episode 305 | Time: 25748.1s
   📊 Metrics: Return=+87.82% | Sharpe=1.119 | DD=12.28% | Turnover=32.07%
   🎚️ Intra-Step TAPE: potential=0.7211 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0158 | critic_loss=0.8895 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4448 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0248
   🧠 Objective Experts: aux_loss=-0.0668 | router_entropy=-0.0029 | diversity_loss=0.0123 | mask=[1, 1, 0] | router=return=0.733 | risk=0.267 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.1186 | ema=0.6965 | best_ema=0.7305 | no_improve=0 | grace_until=265,992
   🔬 Alpha Diversity: mean=2.45 | std=2.14 | range=[1.15, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.76 | AMZN=4.17 | CAT=3.72  BOT: KO=1.66 | BRK-B=1.49 | GLD=1.40
   🧬 FiLM: seq(dg=0.0089, db=0.0065, sat=0.0%) | latent(dg=0.0965, db=0.0576, sat=0.0%) | asset(dg=0.0044, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=101 (31.5%), low_vol=124 (38.6%), medium_vol=96 (29.9%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.33% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5475
   📈 Benchmark Relative: 1/N shaping=0.003 (EW ret=0.00834) | SPY shaping=0.003 (SPY ret=0.00176)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00309_shp1p097_actor.weights.h5 (Sharpe=1.097, MDD=21.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00311_shp0p816_actor.weights.h5 (Sharpe=0.816, MDD=13.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00314_shp0p824_actor.weights.h5 (Sharpe=0.824, MDD=12.32%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00315_shp0p778_actor.weights.h5 (Sharpe=0.778, MDD=12.69%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00316_shp1p244_actor.weights.h5 (Sharpe=1.244, MDD=12.55%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00317_shp0p838_actor.weights.h5 (Sharpe=0.838, MDD=12.17%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00318_shp1p131_actor.weights.h5 (Sharpe=1.131, MDD=13.07%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00319_shp1p134_actor.weights.h5 (Sharpe=1.134, MDD=21.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00320_shp0p750_actor.weights.h5 (Sharpe=0.750, MDD=13.66%)

🧭 REWARD PHASE UPDATE at 260,064 steps:
   B_ramp_2 | base=True dsr=True turnover=False benchmark=True terminal=False | weights=b1.00/d0.60/t0.00/bm0.50/tt0.00
   objective_expert_mask=[1.0, 1.0, 0.0]
   ⏹️ Early-stop transition reset: reason=reward_phase:B_ramp_2 | grace_until=275,064 | best_ema_reset=yes
[CYCLE] Update 255/401 | Step 260,064/500,000 | Episode 320 | Time: 25904.6s
   📊 Metrics: Return=+55.82% | Sharpe=0.750 | DD=13.66% | Turnover=31.70%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0025 | critic_loss=3.4738 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.7369 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.0527 | router_entropy=-0.0030 | diversity_loss=0.0119 | mask=[1, 1, 0] | router=return=0.711 | risk=0.289 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7497 | ema=0.7018 | best_ema=0.7018 | no_improve=0 | grace_until=275,064
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.17% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4032
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=-0.00201) | SPY shaping=-0.001 (SPY ret=-0.00107)
[CYCLE] Update 256/401 | Step 261,576/500,000 | Episode 320 | Time: 26056.2s
   📊 Metrics: Return=+2.87% | Sharpe=0.425 | DD=5.28% | Turnover=31.66%
   🎚️ Intra-Step TAPE: potential=0.2402 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0877 | critic_loss=2.4716 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.2358 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0232
   🧠 Objective Experts: aux_loss=0.0366 | router_entropy=-0.0031 | diversity_loss=0.0139 | mask=[1, 1, 0] | router=return=0.658 | risk=0.342 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4249 | ema=0.6741 | best_ema=0.7018 | no_improve=0 | grace_until=275,064
   🔬 Alpha Diversity: mean=2.40 | std=2.30 | range=[1.15, 10.62] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.13 | AMZN=4.84 | GLD=2.12  BOT: CAT=1.60 | KO=1.59 | BRK-B=1.42
   🧬 FiLM: seq(dg=0.0161, db=0.0101, sat=0.0%) | latent(dg=0.1067, db=0.0636, sat=0.0%) | asset(dg=0.0045, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (31.0%), low_vol=131 (39.0%), medium_vol=101 (30.1%)
[CYCLE] Update 257/401 | Step 263,088/500,000 | Episode 320 | Time: 26208.1s
   📊 Metrics: Return=+4.19% | Sharpe=0.305 | DD=9.48% | Turnover=31.49%
   🎚️ Intra-Step TAPE: potential=0.3382 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0068 | critic_loss=0.7804 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3902 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.0432 | router_entropy=-0.0029 | diversity_loss=0.0117 | mask=[1, 1, 0] | router=return=0.715 | risk=0.285 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3045 | ema=0.6372 | best_ema=0.7018 | no_improve=0 | grace_until=275,064
[CYCLE] Update 258/401 | Step 264,600/500,000 | Episode 320 | Time: 26359.9s
   📊 Metrics: Return=-1.17% | Sharpe=-0.170 | DD=9.48% | Turnover=31.96%
   🎚️ Intra-Step TAPE: potential=0.2418 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0578 | critic_loss=0.8086 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4043 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=0.0080 | router_entropy=-0.0028 | diversity_loss=0.0116 | mask=[1, 1, 0] | router=return=0.746 | risk=0.254 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.1696 | ema=0.5565 | best_ema=0.7018 | no_improve=0 | grace_until=275,064
   🔬 Alpha Diversity: mean=2.46 | std=1.94 | range=[1.14, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.70 | AMZN=3.62 | NEE=2.70  BOT: CAT=1.76 | BRK-B=1.74 | GLD=1.53
   🧬 FiLM: seq(dg=0.0141, db=0.0093, sat=0.0%) | latent(dg=0.1072, db=0.0640, sat=0.0%) | asset(dg=0.0043, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (31.0%), low_vol=131 (39.0%), medium_vol=101 (30.1%)
[CYCLE] Update 259/401 | Step 266,112/500,000 | Episode 320 | Time: 26511.8s
   📊 Metrics: Return=+1.69% | Sharpe=-0.014 | DD=9.48% | Turnover=32.30%
   🎚️ Intra-Step TAPE: potential=0.2542 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0174 | critic_loss=0.8392 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4196 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.0661 | router_entropy=-0.0027 | diversity_loss=0.0101 | mask=[1, 1, 0] | router=return=0.778 | risk=0.222 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0138 | ema=0.4995 | best_ema=0.7018 | no_improve=0 | grace_until=275,064
[CYCLE] Update 260/401 | Step 267,624/500,000 | Episode 320 | Time: 26663.9s
   📊 Metrics: Return=+13.69% | Sharpe=0.401 | DD=12.76% | Turnover=32.32%
   🎚️ Intra-Step TAPE: potential=0.7486 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0147 | critic_loss=0.8231 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4116 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.0343 | router_entropy=-0.0026 | diversity_loss=0.0106 | mask=[1, 1, 0] | router=return=0.786 | risk=0.214 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4014 | ema=0.4897 | best_ema=0.7018 | no_improve=0 | grace_until=275,064
   🔬 Alpha Diversity: mean=2.42 | std=2.32 | range=[1.14, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.79 | AMZN=3.26 | NEE=1.76  BOT: XOM=1.54 | KO=1.42 | BRK-B=1.36
   🧬 FiLM: seq(dg=0.0146, db=0.0094, sat=0.0%) | latent(dg=0.1070, db=0.0639, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (31.0%), low_vol=131 (39.0%), medium_vol=101 (30.1%)
[CYCLE] Update 261/401 | Step 269,136/500,000 | Episode 320 | Time: 26815.8s
   📊 Metrics: Return=+22.33% | Sharpe=0.537 | DD=12.76% | Turnover=32.17%
   🎚️ Intra-Step TAPE: potential=0.7502 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0774 | critic_loss=0.7601 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3801 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=-0.1263 | router_entropy=-0.0027 | diversity_loss=0.0107 | mask=[1, 1, 0] | router=return=0.769 | risk=0.231 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5370 | ema=0.4944 | best_ema=0.7018 | no_improve=0 | grace_until=275,064
[CYCLE] Update 262/401 | Step 270,648/500,000 | Episode 320 | Time: 26967.7s
   📊 Metrics: Return=+31.70% | Sharpe=0.665 | DD=12.76% | Turnover=32.24%
   🎚️ Intra-Step TAPE: potential=0.6911 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0537 | critic_loss=0.7232 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3616 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.1029 | router_entropy=-0.0028 | diversity_loss=0.0104 | mask=[1, 1, 0] | router=return=0.759 | risk=0.241 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6652 | ema=0.5115 | best_ema=0.7018 | no_improve=0 | grace_until=275,064
   🔬 Alpha Diversity: mean=2.44 | std=2.22 | range=[1.14, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.29 | AMZN=3.55 | GLD=2.39  BOT: KO=1.58 | CAT=1.46 | BRK-B=1.41
   🧬 FiLM: seq(dg=0.0113, db=0.0077, sat=0.0%) | latent(dg=0.1016, db=0.0606, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (31.0%), low_vol=131 (39.0%), medium_vol=101 (30.1%)

📚 PPO BATCH SIZE UPDATE at 270,648 steps:
   Batch size: 504
   ⏹️ Early-stop transition reset: reason=batch_size_update | grace_until=285,648 | best_ema_reset=yes
[CYCLE] Update 263/401 | Step 272,160/500,000 | Episode 320 | Time: 27093.2s
   📊 Metrics: Return=+35.74% | Sharpe=0.668 | DD=12.76% | Turnover=32.40%
   🎚️ Intra-Step TAPE: potential=0.5808 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0613 | critic_loss=1.0591 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5295 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0247
   🧠 Objective Experts: aux_loss=-0.1104 | router_entropy=-0.0027 | diversity_loss=0.0102 | mask=[1, 1, 0] | router=return=0.767 | risk=0.233 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6681 | ema=0.5271 | best_ema=0.5271 | no_improve=0 | grace_until=285,648
[CYCLE] Update 264/401 | Step 273,672/500,000 | Episode 320 | Time: 27212.4s
   📊 Metrics: Return=+38.96% | Sharpe=0.658 | DD=12.76% | Turnover=32.67%
   🎚️ Intra-Step TAPE: potential=0.5771 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0562 | critic_loss=1.0391 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5195 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0244
   🧠 Objective Experts: aux_loss=-0.1046 | router_entropy=-0.0028 | diversity_loss=0.0100 | mask=[1, 1, 0] | router=return=0.759 | risk=0.241 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6580 | ema=0.5402 | best_ema=0.5402 | no_improve=0 | grace_until=285,648
   🔬 Alpha Diversity: mean=2.40 | std=2.43 | range=[1.16, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.20 | AMZN=3.84 | MSFT=1.79  BOT: GLD=1.36 | KO=1.35 | BRK-B=1.31
   🧬 FiLM: seq(dg=0.0130, db=0.0085, sat=0.0%) | latent(dg=0.1050, db=0.0625, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=104 (31.0%), low_vol=131 (39.0%), medium_vol=101 (30.1%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00321_shp0p981_actor.weights.h5 (Sharpe=0.981, MDD=11.55%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00322_shp0p952_actor.weights.h5 (Sharpe=0.952, MDD=11.91%)
[CYCLE] Update 265/401 | Step 275,184/500,000 | Episode 322 | Time: 27332.8s
   📊 Metrics: Return=+68.22% | Sharpe=0.952 | DD=11.91% | Turnover=32.93%
   🎚️ Intra-Step TAPE: potential=0.7530 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1382 | critic_loss=1.0692 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5346 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0245
   🧠 Objective Experts: aux_loss=-0.1868 | router_entropy=-0.0029 | diversity_loss=0.0101 | mask=[1, 1, 0] | router=return=0.717 | risk=0.283 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9515 | ema=0.5814 | best_ema=0.5814 | no_improve=0 | grace_until=285,648
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.28% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5080
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=0.00167) | SPY shaping=-0.001 (SPY ret=0.00182)

🎯 ENTROPY COEF UPDATE at 275,184 steps:
   entropy_coef: 0.0005
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00324_shp0p840_actor.weights.h5 (Sharpe=0.840, MDD=12.76%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00326_shp0p704_actor.weights.h5 (Sharpe=0.704, MDD=11.91%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00327_shp0p843_actor.weights.h5 (Sharpe=0.843, MDD=11.63%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00332_shp0p771_actor.weights.h5 (Sharpe=0.771, MDD=18.53%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00333_shp0p704_actor.weights.h5 (Sharpe=0.704, MDD=17.65%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00335_shp0p757_actor.weights.h5 (Sharpe=0.757, MDD=12.35%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00336_shp0p986_actor.weights.h5 (Sharpe=0.986, MDD=10.43%)
[CYCLE] Update 266/401 | Step 276,696/500,000 | Episode 336 | Time: 27455.5s
   📊 Metrics: Return=+68.30% | Sharpe=0.986 | DD=10.43% | Turnover=33.30%
   🎚️ Intra-Step TAPE: potential=0.5577 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0100 | critic_loss=2.6124 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.3062 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.0550 | router_entropy=-0.0030 | diversity_loss=0.0105 | mask=[1, 1, 0] | router=return=0.671 | risk=0.329 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9863 | ema=0.6218 | best_ema=0.6218 | no_improve=0 | grace_until=285,648
   🔬 Alpha Diversity: mean=2.41 | std=2.36 | range=[1.14, 10.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.85 | AMZN=3.32 | CAT=2.06  BOT: NEE=1.54 | KO=1.44 | BRK-B=1.37
   🧬 FiLM: seq(dg=0.0149, db=0.0094, sat=0.0%) | latent(dg=0.1059, db=0.0628, sat=0.0%) | asset(dg=0.0040, db=0.0022, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=110 (31.2%), low_vol=141 (40.1%), medium_vol=101 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.04% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5213
   📈 Benchmark Relative: 1/N shaping=-0.016 (EW ret=0.00764) | SPY shaping=0.001 (SPY ret=0.00170)
[CYCLE] Update 267/401 | Step 278,208/500,000 | Episode 336 | Time: 27574.8s
   📊 Metrics: Return=+4.57% | Sharpe=0.409 | DD=9.80% | Turnover=30.99%
   🎚️ Intra-Step TAPE: potential=0.2498 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0014 | critic_loss=1.1784 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5892 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   🧠 Objective Experts: aux_loss=-0.0430 | router_entropy=-0.0029 | diversity_loss=0.0105 | mask=[1, 1, 0] | router=return=0.701 | risk=0.299 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4092 | ema=0.6006 | best_ema=0.6218 | no_improve=0 | grace_until=285,648
[CYCLE] Update 268/401 | Step 279,720/500,000 | Episode 336 | Time: 27693.9s
   📊 Metrics: Return=+6.59% | Sharpe=0.362 | DD=9.80% | Turnover=30.88%
   🎚️ Intra-Step TAPE: potential=0.2424 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0405 | critic_loss=0.7520 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3760 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   🧠 Objective Experts: aux_loss=-0.0842 | router_entropy=-0.0029 | diversity_loss=0.0102 | mask=[1, 1, 0] | router=return=0.658 | risk=0.342 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3619 | ema=0.5767 | best_ema=0.6218 | no_improve=0 | grace_until=285,648
   🔬 Alpha Diversity: mean=2.37 | std=2.45 | range=[1.14, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.75 | NVDA=4.16 | CAT=1.83  BOT: GLD=1.44 | KO=1.44 | BRK-B=1.34
   🧬 FiLM: seq(dg=0.0158, db=0.0099, sat=0.0%) | latent(dg=0.1086, db=0.0644, sat=0.0%) | asset(dg=0.0042, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=110 (31.2%), low_vol=141 (40.1%), medium_vol=101 (28.7%)
[CYCLE] Update 269/401 | Step 281,232/500,000 | Episode 336 | Time: 27813.0s
   📊 Metrics: Return=+4.81% | Sharpe=0.176 | DD=10.27% | Turnover=31.76%
   🎚️ Intra-Step TAPE: potential=0.3102 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0237 | critic_loss=0.8999 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4500 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   🧠 Objective Experts: aux_loss=-0.0202 | router_entropy=-0.0029 | diversity_loss=0.0102 | mask=[1, 1, 0] | router=return=0.589 | risk=0.411 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1764 | ema=0.5367 | best_ema=0.6218 | no_improve=0 | grace_until=285,648
[CYCLE] Update 270/401 | Step 282,744/500,000 | Episode 336 | Time: 27932.0s
   📊 Metrics: Return=+5.40% | Sharpe=0.147 | DD=10.27% | Turnover=31.81%
   🎚️ Intra-Step TAPE: potential=0.2247 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0844 | critic_loss=0.9514 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4757 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.1296 | router_entropy=-0.0029 | diversity_loss=0.0108 | mask=[1, 1, 0] | router=return=0.566 | risk=0.434 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1474 | ema=0.4978 | best_ema=0.6218 | no_improve=0 | grace_until=285,648
   🔬 Alpha Diversity: mean=2.39 | std=2.37 | range=[1.14, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.35 | AMZN=2.24 | GLD=2.01  BOT: NEE=1.46 | KO=1.39 | BRK-B=1.35
   🧬 FiLM: seq(dg=0.0137, db=0.0089, sat=0.0%) | latent(dg=0.1078, db=0.0640, sat=0.0%) | asset(dg=0.0041, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=110 (31.2%), low_vol=141 (40.1%), medium_vol=101 (28.7%)
[CYCLE] Update 271/401 | Step 284,256/500,000 | Episode 336 | Time: 28051.1s
   📊 Metrics: Return=+9.36% | Sharpe=0.238 | DD=10.27% | Turnover=31.79%
   🎚️ Intra-Step TAPE: potential=0.7018 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0725 | critic_loss=0.7452 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3726 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0239
   🧠 Objective Experts: aux_loss=-0.1174 | router_entropy=-0.0029 | diversity_loss=0.0108 | mask=[1, 1, 0] | router=return=0.555 | risk=0.445 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2377 | ema=0.4717 | best_ema=0.6218 | no_improve=0 | grace_until=285,648

📚 TURNOVER CURRICULUM UPDATE at 285,768 steps:
   Turnover penalty scalar: 0.05
   ⏹️ Early-stop transition reset: reason=turnover_scalar_update | grace_until=300,768 | best_ema_reset=yes
[CYCLE] Update 272/401 | Step 285,768/500,000 | Episode 336 | Time: 28170.1s
   📊 Metrics: Return=+10.82% | Sharpe=0.231 | DD=10.27% | Turnover=31.72%
   🎚️ Intra-Step TAPE: potential=0.2299 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0087 | critic_loss=0.7983 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3991 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0230
   🧠 Objective Experts: aux_loss=-0.0530 | router_entropy=-0.0029 | diversity_loss=0.0110 | mask=[1, 1, 0] | router=return=0.593 | risk=0.407 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2306 | ema=0.4476 | best_ema=0.4717 | no_improve=0 | grace_until=300,768
   🔬 Alpha Diversity: mean=2.38 | std=2.43 | range=[1.14, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.67 | AMZN=2.99 | CAT=1.72  BOT: GLD=1.42 | BRK-B=1.37 | KO=1.36
   🧬 FiLM: seq(dg=0.0133, db=0.0086, sat=0.0%) | latent(dg=0.1068, db=0.0634, sat=0.0%) | asset(dg=0.0043, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=110 (31.2%), low_vol=141 (40.1%), medium_vol=101 (28.7%)
[CYCLE] Update 273/401 | Step 287,280/500,000 | Episode 336 | Time: 28289.4s
   📊 Metrics: Return=+10.83% | Sharpe=0.191 | DD=10.27% | Turnover=31.87%
   🎚️ Intra-Step TAPE: potential=0.2245 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1352 | critic_loss=0.7644 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3822 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0230
   🧠 Objective Experts: aux_loss=-0.1801 | router_entropy=-0.0029 | diversity_loss=0.0116 | mask=[1, 1, 0] | router=return=0.603 | risk=0.397 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1908 | ema=0.4220 | best_ema=0.4717 | no_improve=0 | grace_until=300,768
[CYCLE] Update 274/401 | Step 288,792/500,000 | Episode 336 | Time: 28408.6s
   📊 Metrics: Return=+9.75% | Sharpe=0.135 | DD=10.27% | Turnover=31.81%
   🎚️ Intra-Step TAPE: potential=0.2389 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0172 | critic_loss=1.0760 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5380 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.0636 | router_entropy=-0.0031 | diversity_loss=0.0125 | mask=[1, 1, 0] | router=return=0.438 | risk=0.562 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1349 | ema=0.3933 | best_ema=0.4717 | no_improve=0 | grace_until=300,768
   🔬 Alpha Diversity: mean=2.40 | std=2.41 | range=[1.14, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.90 | AMZN=2.52 | CAT=2.30  BOT: NEE=1.39 | KO=1.34 | BRK-B=1.32
   🧬 FiLM: seq(dg=0.0093, db=0.0068, sat=0.0%) | latent(dg=0.0951, db=0.0568, sat=0.0%) | asset(dg=0.0042, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=110 (31.2%), low_vol=141 (40.1%), medium_vol=101 (28.7%)
[CYCLE] Update 275/401 | Step 290,304/500,000 | Episode 337 | Time: 28527.8s
   📊 Metrics: Return=+44.59% | Sharpe=0.674 | DD=12.23% | Turnover=33.34%
   🎚️ Intra-Step TAPE: potential=0.2664 | delta_reward=-0.0017
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0880 | critic_loss=0.7934 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3967 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0256
   🧠 Objective Experts: aux_loss=-0.1360 | router_entropy=-0.0032 | diversity_loss=0.0127 | mask=[1, 1, 0] | router=return=0.461 | risk=0.539 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6745 | ema=0.4214 | best_ema=0.4717 | no_improve=0 | grace_until=300,768
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 8.37% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3767
   📈 Benchmark Relative: 1/N shaping=-0.006 (EW ret=0.00298) | SPY shaping=-0.001 (SPY ret=0.00221)

🧪 AUX-RETURN COEF UPDATE at 290,304 steps:
   aux_return_pred_coef: 0.3000
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00339_shp1p048_actor.weights.h5 (Sharpe=1.048, MDD=12.46%)
[CYCLE] Update 276/401 | Step 291,816/500,000 | Episode 339 | Time: 28647.5s
   📊 Metrics: Return=+67.37% | Sharpe=1.048 | DD=12.46% | Turnover=32.73%
   🎚️ Intra-Step TAPE: potential=0.5665 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0105 | critic_loss=1.3007 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6503 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0252
   🧠 Objective Experts: aux_loss=-0.0571 | router_entropy=-0.0032 | diversity_loss=0.0120 | mask=[1, 1, 0] | router=return=0.556 | risk=0.444 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0483 | ema=0.4841 | best_ema=0.4841 | no_improve=0 | grace_until=300,768
   🔬 Alpha Diversity: mean=2.45 | std=2.20 | range=[1.13, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.13 | CAT=2.95 | AMZN=2.87  BOT: GLD=1.47 | KO=1.46 | BRK-B=1.41
   🧬 FiLM: seq(dg=0.0109, db=0.0076, sat=0.0%) | latent(dg=0.0996, db=0.0593, sat=0.0%) | asset(dg=0.0042, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=111 (31.3%), low_vol=142 (40.0%), medium_vol=102 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.60% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.5349
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=0.00078) | SPY shaping=0.001 (SPY ret=-0.00153)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00342_shp0p827_actor.weights.h5 (Sharpe=0.827, MDD=14.01%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00343_shp1p155_actor.weights.h5 (Sharpe=1.155, MDD=13.30%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00344_shp0p905_actor.weights.h5 (Sharpe=0.905, MDD=10.48%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00345_shp0p999_actor.weights.h5 (Sharpe=0.999, MDD=12.35%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00346_shp0p747_actor.weights.h5 (Sharpe=0.747, MDD=20.86%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00347_shp1p011_actor.weights.h5 (Sharpe=1.011, MDD=13.37%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00350_shp1p068_actor.weights.h5 (Sharpe=1.068, MDD=11.63%)
[CYCLE] Update 277/401 | Step 293,328/500,000 | Episode 352 | Time: 28769.9s
   📊 Metrics: Return=+17.22% | Sharpe=0.200 | DD=25.14% | Turnover=31.39%
   🎚️ Intra-Step TAPE: potential=0.7475 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0799 | critic_loss=2.4017 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.2008 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   🧠 Objective Experts: aux_loss=0.0336 | router_entropy=-0.0029 | diversity_loss=0.0132 | mask=[1, 1, 0] | router=return=0.706 | risk=0.294 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.1965 | ema=0.4553 | best_ema=0.4841 | no_improve=0 | grace_until=300,768
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.242) | TAPE=0.2403
   📈 Benchmark Relative: 1/N shaping=-0.012 (EW ret=-0.00958) | SPY shaping=-0.001 (SPY ret=-0.01182)
[CYCLE] Update 278/401 | Step 294,840/500,000 | Episode 352 | Time: 28888.9s
   📊 Metrics: Return=+31.12% | Sharpe=2.082 | DD=13.49% | Turnover=31.95%
   🎚️ Intra-Step TAPE: potential=0.2243 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0441 | critic_loss=0.9976 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4988 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0230
   🧠 Objective Experts: aux_loss=-0.0004 | router_entropy=-0.0029 | diversity_loss=0.0117 | mask=[1, 1, 0] | router=return=0.723 | risk=0.277 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.0824 | ema=0.6180 | best_ema=0.6180 | no_improve=0 | grace_until=300,768
   🔬 Alpha Diversity: mean=2.39 | std=2.33 | range=[1.13, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.25 | AMZN=4.65 | MSFT=1.94  BOT: KO=1.44 | GLD=1.42 | BRK-B=1.42
   🧬 FiLM: seq(dg=0.0169, db=0.0103, sat=0.0%) | latent(dg=0.1135, db=0.0671, sat=0.0%) | asset(dg=0.0047, db=0.0025, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=117 (31.8%), low_vol=147 (39.9%), medium_vol=104 (28.3%)
[CYCLE] Update 279/401 | Step 296,352/500,000 | Episode 352 | Time: 29008.1s
   📊 Metrics: Return=+15.00% | Sharpe=0.605 | DD=25.60% | Turnover=32.12%
   🎚️ Intra-Step TAPE: potential=0.2351 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0218 | critic_loss=0.6252 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3126 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   🧠 Objective Experts: aux_loss=-0.0215 | router_entropy=-0.0029 | diversity_loss=0.0111 | mask=[1, 1, 0] | router=return=0.726 | risk=0.274 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5903 | ema=0.6153 | best_ema=0.6180 | no_improve=0 | grace_until=300,768
[CYCLE] Update 280/401 | Step 297,864/500,000 | Episode 352 | Time: 29127.3s
   📊 Metrics: Return=+23.18% | Sharpe=0.625 | DD=26.63% | Turnover=31.41%
   🎚️ Intra-Step TAPE: potential=0.2499 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0167 | critic_loss=0.6212 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3106 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0234
   🧠 Objective Experts: aux_loss=-0.0273 | router_entropy=-0.0030 | diversity_loss=0.0108 | mask=[1, 1, 0] | router=return=0.716 | risk=0.284 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5864 | ema=0.6124 | best_ema=0.6180 | no_improve=0 | grace_until=300,768
   🔬 Alpha Diversity: mean=2.39 | std=2.28 | range=[1.13, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=8.09 | AMZN=3.23 | MSFT=2.07  BOT: KO=1.54 | XOM=1.48 | BRK-B=1.48
   🧬 FiLM: seq(dg=0.0153, db=0.0096, sat=0.0%) | latent(dg=0.1095, db=0.0648, sat=0.0%) | asset(dg=0.0045, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=117 (31.8%), low_vol=147 (39.9%), medium_vol=104 (28.3%)
[CYCLE] Update 281/401 | Step 299,376/500,000 | Episode 352 | Time: 29246.5s
   📊 Metrics: Return=+20.41% | Sharpe=0.470 | DD=26.63% | Turnover=31.21%
   🎚️ Intra-Step TAPE: potential=0.2476 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0326 | critic_loss=0.5455 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2728 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0234
   🧠 Objective Experts: aux_loss=-0.0759 | router_entropy=-0.0029 | diversity_loss=0.0101 | mask=[1, 1, 0] | router=return=0.722 | risk=0.278 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4311 | ema=0.5942 | best_ema=0.6180 | no_improve=0 | grace_until=300,768
[CYCLE] Update 282/401 | Step 300,888/500,000 | Episode 352 | Time: 29365.8s
   📊 Metrics: Return=+25.32% | Sharpe=0.487 | DD=26.63% | Turnover=31.14%
   🎚️ Intra-Step TAPE: potential=0.2650 | delta_reward=-0.0033
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0673 | critic_loss=0.5402 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2701 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0234
   🧠 Objective Experts: aux_loss=-0.1098 | router_entropy=-0.0030 | diversity_loss=0.0095 | mask=[1, 1, 0] | router=return=0.713 | risk=0.287 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4475 | ema=0.5796 | best_ema=0.6180 | no_improve=1
   🔬 Alpha Diversity: mean=2.39 | std=2.41 | range=[1.13, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.21 | AMZN=5.14 | JPM=1.65  BOT: KO=1.41 | XOM=1.40 | BRK-B=1.33
   🧬 FiLM: seq(dg=0.0145, db=0.0093, sat=0.0%) | latent(dg=0.1073, db=0.0635, sat=0.0%) | asset(dg=0.0043, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=117 (31.8%), low_vol=147 (39.9%), medium_vol=104 (28.3%)

🌡️ TEMPERATURE UPDATE at 300,888 steps:
   temperature: 0.9000
   ⏹️ Early-stop transition reset: reason=temperature_update | grace_until=315,888 | best_ema_reset=yes
[CYCLE] Update 283/401 | Step 302,400/500,000 | Episode 352 | Time: 29485.1s
   📊 Metrics: Return=+30.04% | Sharpe=0.499 | DD=26.63% | Turnover=31.59%
   🎚️ Intra-Step TAPE: potential=0.6064 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1201 | critic_loss=0.5386 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2693 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0232
   🧠 Objective Experts: aux_loss=-0.1621 | router_entropy=-0.0030 | diversity_loss=0.0094 | mask=[1, 1, 0] | router=return=0.688 | risk=0.312 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4600 | ema=0.5676 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
[CYCLE] Update 284/401 | Step 303,912/500,000 | Episode 352 | Time: 29604.5s
   📊 Metrics: Return=+29.28% | Sharpe=0.440 | DD=26.63% | Turnover=31.98%
   🎚️ Intra-Step TAPE: potential=0.2538 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1851 | critic_loss=0.5728 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2864 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0236
   🧠 Objective Experts: aux_loss=-0.2274 | router_entropy=-0.0032 | diversity_loss=0.0095 | mask=[1, 1, 0] | router=return=0.592 | risk=0.408 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4012 | ema=0.5510 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
   🔬 Alpha Diversity: mean=2.34 | std=2.53 | range=[1.14, 10.61] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.45 | AMZN=2.84 | MSFT=1.55  BOT: GLD=1.40 | CAT=1.38 | BRK-B=1.38
   🧬 FiLM: seq(dg=0.0131, db=0.0088, sat=0.0%) | latent(dg=0.1051, db=0.0624, sat=0.0%) | asset(dg=0.0038, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=117 (31.8%), low_vol=147 (39.9%), medium_vol=104 (28.3%)
[CYCLE] Update 285/401 | Step 305,424/500,000 | Episode 352 | Time: 29723.7s
   📊 Metrics: Return=+29.17% | Sharpe=0.400 | DD=26.63% | Turnover=32.06%
   🎚️ Intra-Step TAPE: potential=0.4944 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0504 | critic_loss=0.8326 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4163 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   🧠 Objective Experts: aux_loss=-0.0926 | router_entropy=-0.0031 | diversity_loss=0.0099 | mask=[1, 1, 0] | router=return=0.466 | risk=0.534 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3607 | ema=0.5319 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
[CYCLE] Update 286/401 | Step 306,936/500,000 | Episode 353 | Time: 29842.8s
   📊 Metrics: Return=+6.27% | Sharpe=0.059 | DD=27.05% | Turnover=31.33%
   🎚️ Intra-Step TAPE: potential=0.2251 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0038 | critic_loss=1.1309 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5655 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0230
   🧠 Objective Experts: aux_loss=-0.0461 | router_entropy=-0.0030 | diversity_loss=0.0099 | mask=[1, 1, 0] | router=return=0.413 | risk=0.587 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0094 | ema=0.4797 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
   🔬 Alpha Diversity: mean=2.34 | std=2.51 | range=[1.13, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.04 | AMZN=2.23 | MSFT=1.70  BOT: KO=1.40 | JPM=1.39 | BRK-B=1.37
   🧬 FiLM: seq(dg=0.0116, db=0.0082, sat=0.0%) | latent(dg=0.1027, db=0.0611, sat=0.0%) | asset(dg=0.0039, db=0.0021, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=117 (31.7%), low_vol=148 (40.1%), medium_vol=104 (28.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.312, dd 12.64% / trig 16.50%) | terminal=0.000 (peak 0.433) | TAPE=0.2277
   📈 Benchmark Relative: 1/N shaping=-0.005 (EW ret=0.00336) | SPY shaping=-0.003 (SPY ret=0.00507)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00355_shp0p819_actor.weights.h5 (Sharpe=0.819, MDD=12.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00357_shp1p138_actor.weights.h5 (Sharpe=1.138, MDD=14.97%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00359_shp0p734_actor.weights.h5 (Sharpe=0.734, MDD=18.78%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00361_shp0p750_actor.weights.h5 (Sharpe=0.750, MDD=13.66%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00362_shp0p744_actor.weights.h5 (Sharpe=0.744, MDD=11.53%)
[CYCLE] Update 287/401 | Step 308,448/500,000 | Episode 362 | Time: 29964.6s
   📊 Metrics: Return=+51.74% | Sharpe=0.744 | DD=11.53% | Turnover=31.96%
   🎚️ Intra-Step TAPE: potential=0.5335 | delta_reward=-0.0017
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0414 | critic_loss=1.7252 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8626 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   🧠 Objective Experts: aux_loss=-0.0841 | router_entropy=-0.0029 | diversity_loss=0.0100 | mask=[1, 1, 0] | router=return=0.488 | risk=0.512 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7435 | ema=0.5061 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.56% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4110
   📈 Benchmark Relative: 1/N shaping=-0.003 (EW ret=0.00028) | SPY shaping=-0.000 (SPY ret=-0.00024)
[CYCLE] Update 288/401 | Step 309,960/500,000 | Episode 368 | Time: 30083.4s
   📊 Metrics: Return=+7.44% | Sharpe=0.083 | DD=25.52% | Turnover=31.55%
   🎚️ Intra-Step TAPE: potential=0.2364 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0159 | critic_loss=1.9894 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.9947 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   🧠 Objective Experts: aux_loss=-0.0265 | router_entropy=-0.0030 | diversity_loss=0.0101 | mask=[1, 1, 0] | router=return=0.582 | risk=0.418 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0709 | ema=0.4626 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
   🔬 Alpha Diversity: mean=2.36 | std=2.47 | range=[1.13, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.59 | AMZN=3.69 | CAT=1.94  BOT: KO=1.40 | BRK-B=1.36 | GLD=1.36
   🧬 FiLM: seq(dg=0.0169, db=0.0106, sat=0.0%) | latent(dg=0.1127, db=0.0668, sat=0.0%) | asset(dg=0.0044, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=121 (31.5%), low_vol=154 (40.1%), medium_vol=109 (28.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.48% / trig 16.50%) | terminal=0.000 (peak 0.216) | TAPE=0.2319
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=0.00210) | SPY shaping=-0.003 (SPY ret=0.00454)
[CYCLE] Update 289/401 | Step 311,472/500,000 | Episode 368 | Time: 30202.5s
   📊 Metrics: Return=-1.83% | Sharpe=-0.394 | DD=7.27% | Turnover=32.66%
   🎚️ Intra-Step TAPE: potential=0.2477 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0435 | critic_loss=0.9013 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4506 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=0.0014 | router_entropy=-0.0029 | diversity_loss=0.0101 | mask=[1, 1, 0] | router=return=0.565 | risk=0.435 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.3940 | ema=0.3769 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
[CYCLE] Update 290/401 | Step 312,984/500,000 | Episode 368 | Time: 30321.7s
   📊 Metrics: Return=-6.27% | Sharpe=-0.777 | DD=10.04% | Turnover=32.96%
   🎚️ Intra-Step TAPE: potential=0.2224 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0583 | critic_loss=1.0044 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5022 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=-0.1004 | router_entropy=-0.0028 | diversity_loss=0.0100 | mask=[1, 1, 0] | router=return=0.592 | risk=0.408 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.7768 | ema=0.2615 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
   🔬 Alpha Diversity: mean=2.35 | std=2.48 | range=[1.13, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.09 | AMZN=2.17 | MSFT=1.58  BOT: KO=1.43 | GLD=1.40 | BRK-B=1.37
   🧬 FiLM: seq(dg=0.0169, db=0.0107, sat=0.0%) | latent(dg=0.1135, db=0.0672, sat=0.0%) | asset(dg=0.0042, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=121 (31.5%), low_vol=154 (40.1%), medium_vol=109 (28.4%)
[CYCLE] Update 291/401 | Step 314,496/500,000 | Episode 368 | Time: 30440.9s
   📊 Metrics: Return=+3.34% | Sharpe=0.060 | DD=11.03% | Turnover=33.12%
   🎚️ Intra-Step TAPE: potential=0.2678 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0697 | critic_loss=0.9810 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4905 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0221
   🧠 Objective Experts: aux_loss=-0.1115 | router_entropy=-0.0027 | diversity_loss=0.0099 | mask=[1, 1, 0] | router=return=0.608 | risk=0.392 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0597 | ema=0.2413 | best_ema=0.5796 | no_improve=0 | grace_until=315,888
[CYCLE] Update 292/401 | Step 316,008/500,000 | Episode 368 | Time: 30560.4s
   📊 Metrics: Return=+19.17% | Sharpe=0.611 | DD=13.08% | Turnover=33.12%
   🎚️ Intra-Step TAPE: potential=0.7455 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1254 | critic_loss=0.7608 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3804 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   🧠 Objective Experts: aux_loss=-0.1686 | router_entropy=-0.0027 | diversity_loss=0.0101 | mask=[1, 1, 0] | router=return=0.590 | risk=0.410 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6108 | ema=0.2783 | best_ema=0.5796 | no_improve=1
   🔬 Alpha Diversity: mean=2.39 | std=2.30 | range=[1.12, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.87 | AMZN=3.48 | JPM=2.01  BOT: BRK-B=1.51 | KO=1.47 | GLD=1.45
   🧬 FiLM: seq(dg=0.0167, db=0.0106, sat=0.0%) | latent(dg=0.1143, db=0.0677, sat=0.0%) | asset(dg=0.0045, db=0.0024, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=121 (31.5%), low_vol=154 (40.1%), medium_vol=109 (28.4%)
[CYCLE] Update 293/401 | Step 317,520/500,000 | Episode 368 | Time: 30679.5s
   📊 Metrics: Return=+22.02% | Sharpe=0.606 | DD=13.08% | Turnover=33.18%
   🎚️ Intra-Step TAPE: potential=0.2322 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1689 | critic_loss=0.9133 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4566 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0233
   🧠 Objective Experts: aux_loss=-0.2117 | router_entropy=-0.0029 | diversity_loss=0.0098 | mask=[1, 1, 0] | router=return=0.537 | risk=0.463 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6064 | ema=0.3111 | best_ema=0.5796 | no_improve=2
[CYCLE] Update 294/401 | Step 319,032/500,000 | Episode 368 | Time: 30798.7s
   📊 Metrics: Return=+25.57% | Sharpe=0.626 | DD=13.08% | Turnover=33.41%
   🎚️ Intra-Step TAPE: potential=0.6666 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0825 | critic_loss=0.7958 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3979 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0228
   🧠 Objective Experts: aux_loss=-0.1243 | router_entropy=-0.0030 | diversity_loss=0.0094 | mask=[1, 1, 0] | router=return=0.530 | risk=0.470 | discipline=0.000
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6260 | ema=0.3426 | best_ema=0.5796 | no_improve=3
   🔬 Alpha Diversity: mean=2.35 | std=2.41 | range=[1.12, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.11 | NVDA=3.06 | JPM=1.67  BOT: GLD=1.49 | XOM=1.47 | BRK-B=1.43
   🧬 FiLM: seq(dg=0.0132, db=0.0090, sat=0.0%) | latent(dg=0.1066, db=0.0632, sat=0.0%) | asset(dg=0.0043, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=121 (31.5%), low_vol=154 (40.1%), medium_vol=109 (28.4%)

🧭 REWARD PHASE UPDATE at 320,544 steps:
   C_disc_intro | base=True dsr=True turnover=True benchmark=True terminal=False | weights=b1.00/d1.00/t0.10/bm0.65/tt0.00
   objective_expert_mask=[1.0, 1.0, 1.0]
   ⏹️ Early-stop transition reset: reason=reward_phase:C_disc_intro | grace_until=335,544 | best_ema_reset=yes
[CYCLE] Update 295/401 | Step 320,544/500,000 | Episode 368 | Time: 30917.9s
   📊 Metrics: Return=+29.68% | Sharpe=0.655 | DD=13.08% | Turnover=33.41%
   🎚️ Intra-Step TAPE: potential=0.7028 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0975 | critic_loss=0.5575 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2787 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=-0.1407 | router_entropy=-0.0039 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.511 | risk=0.420 | discipline=0.069
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6551 | ema=0.3738 | best_ema=0.3738 | no_improve=0 | grace_until=335,544
[CYCLE] Update 296/401 | Step 322,056/500,000 | Episode 368 | Time: 31037.0s
   📊 Metrics: Return=+37.14% | Sharpe=0.751 | DD=13.08% | Turnover=33.36%
   🎚️ Intra-Step TAPE: potential=0.7538 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0966 | critic_loss=1.0955 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5478 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   🧠 Objective Experts: aux_loss=-0.1400 | router_entropy=-0.0039 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.464 | risk=0.483 | discipline=0.053
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7515 | ema=0.4116 | best_ema=0.4116 | no_improve=0 | grace_until=335,544
   🔬 Alpha Diversity: mean=2.33 | std=2.50 | range=[1.13, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.05 | AMZN=1.75 | MSFT=1.66  BOT: KO=1.47 | XOM=1.47 | BRK-B=1.41
   🧬 FiLM: seq(dg=0.0112, db=0.0080, sat=0.0%) | latent(dg=0.1020, db=0.0606, sat=0.0%) | asset(dg=0.0043, db=0.0023, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=121 (31.5%), low_vol=154 (40.1%), medium_vol=109 (28.4%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00370_shp0p779_actor.weights.h5 (Sharpe=0.779, MDD=21.99%)
[CYCLE] Update 297/401 | Step 323,568/500,000 | Episode 370 | Time: 31156.8s
   📊 Metrics: Return=+51.82% | Sharpe=0.779 | DD=21.99% | Turnover=33.52%
   🎚️ Intra-Step TAPE: potential=0.2280 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0072 | critic_loss=0.6788 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3394 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0228
   🧠 Objective Experts: aux_loss=-0.0363 | router_entropy=-0.0040 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.410 | risk=0.531 | discipline=0.058
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7791 | ema=0.4484 | best_ema=0.4484 | no_improve=0 | grace_until=335,544
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.27% / trig 16.50%) | terminal=0.000 (peak 0.015) | TAPE=0.4083
   📈 Benchmark Relative: 1/N shaping=0.013 (EW ret=-0.00886) | SPY shaping=0.006 (SPY ret=-0.01189)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00371_shp0p732_actor.weights.h5 (Sharpe=0.732, MDD=20.11%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00372_shp0p767_actor.weights.h5 (Sharpe=0.767, MDD=13.08%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00376_shp0p872_actor.weights.h5 (Sharpe=0.872, MDD=13.19%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00377_shp0p823_actor.weights.h5 (Sharpe=0.823, MDD=12.60%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00378_shp0p951_actor.weights.h5 (Sharpe=0.951, MDD=11.10%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00379_shp0p961_actor.weights.h5 (Sharpe=0.961, MDD=17.32%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00381_shp0p758_actor.weights.h5 (Sharpe=0.758, MDD=20.51%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00382_shp0p833_actor.weights.h5 (Sharpe=0.833, MDD=13.16%)
[CYCLE] Update 298/401 | Step 325,080/500,000 | Episode 384 | Time: 31279.7s
   📊 Metrics: Return=+22.53% | Sharpe=0.260 | DD=26.17% | Turnover=32.10%
   🎚️ Intra-Step TAPE: potential=0.7485 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1061 | critic_loss=1.3987 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6994 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   🧠 Objective Experts: aux_loss=-0.1505 | router_entropy=-0.0044 | diversity_loss=0.0128 | mask=[1, 1, 1] | router=return=0.453 | risk=0.376 | discipline=0.171
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2319 | ema=0.4267 | best_ema=0.4484 | no_improve=0 | grace_until=335,544
   🔬 Alpha Diversity: mean=2.39 | std=2.38 | range=[1.12, 10.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.83 | AMZN=3.62 | MSFT=1.87  BOT: GLD=1.40 | BRK-B=1.37 | KO=1.36
   🧬 FiLM: seq(dg=0.0158, db=0.0100, sat=0.0%) | latent(dg=0.1089, db=0.0646, sat=0.0%) | asset(dg=0.0048, db=0.0026, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=127 (31.8%), low_vol=162 (40.5%), medium_vol=111 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.69% / trig 16.50%) | terminal=0.000 (peak 0.304) | TAPE=0.2459
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=0.00429) | SPY shaping=-0.006 (SPY ret=0.00904)
[CYCLE] Update 299/401 | Step 326,592/500,000 | Episode 384 | Time: 31398.8s
   📊 Metrics: Return=+29.07% | Sharpe=2.102 | DD=13.02% | Turnover=30.77%
   🎚️ Intra-Step TAPE: potential=0.7383 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0970 | critic_loss=0.8378 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4189 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0226
   🧠 Objective Experts: aux_loss=-0.1408 | router_entropy=-0.0048 | diversity_loss=0.0129 | mask=[1, 1, 1] | router=return=0.444 | risk=0.284 | discipline=0.272
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.1017 | ema=0.5942 | best_ema=0.5942 | no_improve=0 | grace_until=335,544
[CYCLE] Update 300/401 | Step 328,104/500,000 | Episode 384 | Time: 31518.0s
   📊 Metrics: Return=+37.33% | Sharpe=1.913 | DD=13.02% | Turnover=32.22%
   🎚️ Intra-Step TAPE: potential=0.5134 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1074 | critic_loss=0.5338 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2669 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   🧠 Objective Experts: aux_loss=-0.1502 | router_entropy=-0.0048 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.380 | risk=0.312 | discipline=0.308
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.9128 | ema=0.7261 | best_ema=0.7261 | no_improve=0 | grace_until=335,544
   🔬 Alpha Diversity: mean=2.38 | std=2.43 | range=[1.15, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.86 | AMZN=4.42 | CAT=2.10  BOT: XOM=1.35 | KO=1.33 | BRK-B=1.31
   🧬 FiLM: seq(dg=0.0175, db=0.0108, sat=0.0%) | latent(dg=0.1130, db=0.0670, sat=0.0%) | asset(dg=0.0051, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=127 (31.8%), low_vol=162 (40.5%), medium_vol=111 (27.8%)
[CYCLE] Update 301/401 | Step 329,616/500,000 | Episode 384 | Time: 31636.8s
   📊 Metrics: Return=+44.04% | Sharpe=1.785 | DD=13.02% | Turnover=32.35%
   🎚️ Intra-Step TAPE: potential=0.7527 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0562 | critic_loss=0.5123 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2562 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.0983 | router_entropy=-0.0046 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.340 | risk=0.440 | discipline=0.219
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.7849 | ema=0.8319 | best_ema=0.8319 | no_improve=0 | grace_until=335,544
[CYCLE] Update 302/401 | Step 331,128/500,000 | Episode 384 | Time: 31755.6s
   📊 Metrics: Return=+52.65% | Sharpe=1.786 | DD=13.02% | Turnover=32.85%
   🎚️ Intra-Step TAPE: potential=0.7531 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1391 | critic_loss=0.5452 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2726 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   🧠 Objective Experts: aux_loss=-0.1807 | router_entropy=-0.0046 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.325 | risk=0.455 | discipline=0.220
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.7856 | ema=0.9273 | best_ema=0.9273 | no_improve=0 | grace_until=335,544
   🔬 Alpha Diversity: mean=2.34 | std=2.51 | range=[1.16, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.44 | AMZN=2.54 | MSFT=1.74  BOT: GLD=1.40 | KO=1.36 | BRK-B=1.33
   🧬 FiLM: seq(dg=0.0135, db=0.0089, sat=0.0%) | latent(dg=0.1067, db=0.0633, sat=0.0%) | asset(dg=0.0048, db=0.0026, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=127 (31.8%), low_vol=162 (40.5%), medium_vol=111 (27.8%)
[CYCLE] Update 303/401 | Step 332,640/500,000 | Episode 384 | Time: 31874.4s
   📊 Metrics: Return=+56.03% | Sharpe=1.658 | DD=13.02% | Turnover=32.98%
   🎚️ Intra-Step TAPE: potential=0.5217 | delta_reward=-0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0848 | critic_loss=0.6409 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3204 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.1270 | router_entropy=-0.0046 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.343 | risk=0.427 | discipline=0.231
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.6579 | ema=1.0004 | best_ema=1.0004 | no_improve=0 | grace_until=335,544
[CYCLE] Update 304/401 | Step 334,152/500,000 | Episode 384 | Time: 31993.4s
   📊 Metrics: Return=+59.18% | Sharpe=1.515 | DD=13.02% | Turnover=33.06%
   🎚️ Intra-Step TAPE: potential=0.2627 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.2041 | critic_loss=0.3931 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1965 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0224
   🧠 Objective Experts: aux_loss=-0.2470 | router_entropy=-0.0047 | diversity_loss=0.0125 | mask=[1, 1, 1] | router=return=0.369 | risk=0.395 | discipline=0.236
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.5145 | ema=1.0518 | best_ema=1.0518 | no_improve=0 | grace_until=335,544
   🔬 Alpha Diversity: mean=2.37 | std=2.42 | range=[1.13, 10.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.44 | AMZN=3.05 | JPM=1.83  BOT: GLD=1.37 | NEE=1.37 | KO=1.32
   🧬 FiLM: seq(dg=0.0150, db=0.0096, sat=0.0%) | latent(dg=0.1116, db=0.0662, sat=0.0%) | asset(dg=0.0050, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=127 (31.8%), low_vol=162 (40.5%), medium_vol=111 (27.8%)
[CYCLE] Update 305/401 | Step 335,664/500,000 | Episode 384 | Time: 32112.5s
   📊 Metrics: Return=+61.58% | Sharpe=1.378 | DD=13.02% | Turnover=33.07%
   🎚️ Intra-Step TAPE: potential=0.5506 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1335 | critic_loss=0.4050 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2025 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   🧠 Objective Experts: aux_loss=-0.1759 | router_entropy=-0.0046 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.320 | risk=0.464 | discipline=0.216
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.3779 | ema=1.0844 | best_ema=1.0844 | no_improve=0
[CYCLE] Update 306/401 | Step 337,176/500,000 | Episode 384 | Time: 32231.4s
   📊 Metrics: Return=+61.32% | Sharpe=1.184 | DD=13.02% | Turnover=32.91%
   🎚️ Intra-Step TAPE: potential=0.2378 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0925 | critic_loss=0.3913 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1957 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.1344 | router_entropy=-0.0045 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.293 | risk=0.532 | discipline=0.175
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.1837 | ema=1.0943 | best_ema=1.0943 | no_improve=0
   🔬 Alpha Diversity: mean=2.33 | std=2.52 | range=[1.15, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=2.88 | NVDA=2.63 | CAT=1.67  BOT: XOM=1.38 | KO=1.38 | BRK-B=1.36
   🧬 FiLM: seq(dg=0.0114, db=0.0079, sat=0.0%) | latent(dg=0.1031, db=0.0612, sat=0.0%) | asset(dg=0.0049, db=0.0026, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=127 (31.8%), low_vol=162 (40.5%), medium_vol=111 (27.8%)
[CYCLE] Update 307/401 | Step 338,688/500,000 | Episode 384 | Time: 32350.5s
   📊 Metrics: Return=+75.64% | Sharpe=1.114 | DD=15.42% | Turnover=32.58%
   🎚️ Intra-Step TAPE: potential=0.7463 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0641 | critic_loss=0.5395 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2698 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   🧠 Objective Experts: aux_loss=-0.1063 | router_entropy=-0.0045 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.292 | risk=0.527 | discipline=0.181
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.1142 | ema=1.0963 | best_ema=1.0943 | no_improve=1
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00386_shp0p789_actor.weights.h5 (Sharpe=0.789, MDD=20.08%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00388_shp0p974_actor.weights.h5 (Sharpe=0.974, MDD=15.42%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00389_shp0p828_actor.weights.h5 (Sharpe=0.828, MDD=12.71%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00391_shp0p920_actor.weights.h5 (Sharpe=0.920, MDD=16.06%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00392_shp0p979_actor.weights.h5 (Sharpe=0.979, MDD=12.77%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00393_shp0p752_actor.weights.h5 (Sharpe=0.752, MDD=12.08%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00394_shp0p867_actor.weights.h5 (Sharpe=0.867, MDD=13.24%)

📚 EPISODE HORIZON UPDATE at 340,200 steps:
   Episode horizon: 1018 steps
[CYCLE] Update 308/401 | Step 340,200/500,000 | Episode 394 | Time: 32473.2s
   📊 Metrics: Return=+52.37% | Sharpe=0.867 | DD=13.24% | Turnover=33.05%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0604 | critic_loss=1.0805 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5402 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0221
   🧠 Objective Experts: aux_loss=-0.1028 | router_entropy=-0.0045 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.314 | risk=0.500 | discipline=0.186
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8667 | ema=1.0734 | best_ema=1.0943 | no_improve=2
   🔬 Alpha Diversity: mean=2.35 | std=2.47 | range=[1.12, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.35 | AMZN=2.60 | CAT=1.97  BOT: BRK-B=1.40 | NEE=1.40 | KO=1.38
   🧬 FiLM: seq(dg=0.0123, db=0.0083, sat=0.0%) | latent(dg=0.1046, db=0.0620, sat=0.0%) | asset(dg=0.0049, db=0.0026, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=131 (32.0%), low_vol=165 (40.2%), medium_vol=114 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.06% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.4791
   📈 Benchmark Relative: 1/N shaping=-0.013 (EW ret=0.00405) | SPY shaping=-0.000 (SPY ret=0.00107)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00395_shp0p968_actor.weights.h5 (Sharpe=0.968, MDD=11.72%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00397_shp0p869_actor.weights.h5 (Sharpe=0.869, MDD=13.86%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00400_shp0p724_actor.weights.h5 (Sharpe=0.724, MDD=20.21%)

📚 EPISODE HORIZON UPDATE at 341,712 steps:
   Episode horizon: 1092 steps
[CYCLE] Update 309/401 | Step 341,712/500,000 | Episode 400 | Time: 32593.4s
   📊 Metrics: Return=+52.37% | Sharpe=0.724 | DD=20.21% | Turnover=32.59%
   🎚️ Intra-Step TAPE: potential=0.2368 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0383 | critic_loss=0.9971 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4985 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   🧠 Objective Experts: aux_loss=-0.0046 | router_entropy=-0.0047 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.341 | risk=0.415 | discipline=0.244
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7239 | ema=1.0384 | best_ema=1.0943 | no_improve=3
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 5.72% / trig 16.50%) | terminal=0.000 (peak 0.005) | TAPE=0.3795
   📈 Benchmark Relative: 1/N shaping=-0.010 (EW ret=-0.00951) | SPY shaping=-0.003 (SPY ret=-0.00871)

📚 EPISODE HORIZON UPDATE at 343,224 steps:
   Episode horizon: 1167 steps
[CYCLE] Update 310/401 | Step 343,224/500,000 | Episode 400 | Time: 32712.4s
   📊 Metrics: Return=-5.65% | Sharpe=-0.855 | DD=8.93% | Turnover=31.85%
   🎚️ Intra-Step TAPE: potential=0.2468 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0504 | critic_loss=0.6706 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3353 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   🧠 Objective Experts: aux_loss=-0.0933 | router_entropy=-0.0047 | diversity_loss=0.0124 | mask=[1, 1, 1] | router=return=0.363 | risk=0.400 | discipline=0.237
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.8551 | ema=0.8491 | best_ema=1.0943 | no_improve=4
   🔬 Alpha Diversity: mean=2.38 | std=2.40 | range=[1.14, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.37 | AMZN=3.81 | JPM=2.11  BOT: GLD=1.35 | NEE=1.32 | KO=1.29
   🧬 FiLM: seq(dg=0.0160, db=0.0099, sat=0.0%) | latent(dg=0.1118, db=0.0662, sat=0.0%) | asset(dg=0.0052, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=134 (32.2%), low_vol=166 (39.9%), medium_vol=116 (27.9%)

📚 EPISODE HORIZON UPDATE at 344,736 steps:
   Episode horizon: 1241 steps
[CYCLE] Update 311/401 | Step 344,736/500,000 | Episode 400 | Time: 32831.4s
   📊 Metrics: Return=-4.03% | Sharpe=-0.553 | DD=9.98% | Turnover=32.06%
   🎚️ Intra-Step TAPE: potential=0.2488 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1467 | critic_loss=0.5370 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2685 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0224
   🧠 Objective Experts: aux_loss=-0.1896 | router_entropy=-0.0047 | diversity_loss=0.0124 | mask=[1, 1, 1] | router=return=0.332 | risk=0.428 | discipline=0.240
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.5527 | ema=0.7089 | best_ema=1.0943 | no_improve=5

📚 TURNOVER CURRICULUM UPDATE at 346,248 steps:
   Turnover penalty scalar: 0.1
   ⏹️ Early-stop transition reset: reason=turnover_scalar_update | grace_until=361,248 | best_ema_reset=yes

📚 EPISODE HORIZON UPDATE at 346,248 steps:
   Episode horizon: 1315 steps
[CYCLE] Update 312/401 | Step 346,248/500,000 | Episode 400 | Time: 32950.4s
   📊 Metrics: Return=+7.54% | Sharpe=0.283 | DD=13.47% | Turnover=31.89%
   🎚️ Intra-Step TAPE: potential=0.7456 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1748 | critic_loss=0.3727 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1863 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   🧠 Objective Experts: aux_loss=-0.2167 | router_entropy=-0.0048 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.357 | risk=0.361 | discipline=0.282
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2833 | ema=0.6663 | best_ema=0.7089 | no_improve=0 | grace_until=361,248
   🔬 Alpha Diversity: mean=2.34 | std=2.50 | range=[1.15, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.00 | AMZN=3.81 | MSFT=1.62  BOT: GLD=1.36 | KO=1.33 | BRK-B=1.31
   🧬 FiLM: seq(dg=0.0164, db=0.0101, sat=0.0%) | latent(dg=0.1122, db=0.0665, sat=0.0%) | asset(dg=0.0051, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=134 (32.2%), low_vol=166 (39.9%), medium_vol=116 (27.9%)

📚 EPISODE HORIZON UPDATE at 347,760 steps:
   Episode horizon: 1390 steps
[CYCLE] Update 313/401 | Step 347,760/500,000 | Episode 400 | Time: 33069.3s
   📊 Metrics: Return=+14.69% | Sharpe=0.452 | DD=13.47% | Turnover=31.31%
   🎚️ Intra-Step TAPE: potential=0.7520 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0508 | critic_loss=0.5758 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2879 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   🧠 Objective Experts: aux_loss=-0.0923 | router_entropy=-0.0048 | diversity_loss=0.0124 | mask=[1, 1, 1] | router=return=0.345 | risk=0.372 | discipline=0.283
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.4521 | ema=0.6449 | best_ema=0.7089 | no_improve=0 | grace_until=361,248

📚 EPISODE HORIZON UPDATE at 349,272 steps:
   Episode horizon: 1464 steps
[CYCLE] Update 314/401 | Step 349,272/500,000 | Episode 400 | Time: 33188.2s
   📊 Metrics: Return=+22.25% | Sharpe=0.599 | DD=13.47% | Turnover=31.84%
   🎚️ Intra-Step TAPE: potential=0.3434 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0487 | critic_loss=0.3494 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1747 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   🧠 Objective Experts: aux_loss=0.0073 | router_entropy=-0.0046 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.276 | risk=0.527 | discipline=0.197
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5995 | ema=0.6404 | best_ema=0.7089 | no_improve=0 | grace_until=361,248
   🔬 Alpha Diversity: mean=2.31 | std=2.55 | range=[1.14, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.73 | AMZN=1.83 | MSFT=1.61  BOT: BRK-B=1.40 | GLD=1.38 | KO=1.37
   🧬 FiLM: seq(dg=0.0114, db=0.0078, sat=0.0%) | latent(dg=0.1023, db=0.0607, sat=0.0%) | asset(dg=0.0050, db=0.0026, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=134 (32.2%), low_vol=166 (39.9%), medium_vol=116 (27.9%)
   [TOOL] Actor learning rate adjusted to 0.000010 at step 350,000
   [TOOL] Critic learning rate adjusted to 0.000100 at step 350,000

📚 EPISODE HORIZON UPDATE at 350,784 steps:
   Episode horizon: 1500 steps
[CYCLE] Update 315/401 | Step 350,784/500,000 | Episode 400 | Time: 33306.9s
   📊 Metrics: Return=+28.13% | Sharpe=0.670 | DD=13.47% | Turnover=32.10%
   🎚️ Intra-Step TAPE: potential=0.5994 | delta_reward=-0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1684 | critic_loss=0.3817 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1909 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   🧠 Objective Experts: aux_loss=-0.2102 | router_entropy=-0.0045 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.278 | risk=0.541 | discipline=0.182
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6704 | ema=0.6434 | best_ema=0.7089 | no_improve=0 | grace_until=361,248

[DOWN] PPO GAMMA UPDATE at 350,784 steps:
   gamma: 0.9980

[DOWN] PPO GAE-λ UPDATE at 350,784 steps:
   gae_lambda: 0.9700
[CYCLE] Update 316/401 | Step 352,296/500,000 | Episode 400 | Time: 33426.0s
   📊 Metrics: Return=+31.97% | Sharpe=0.684 | DD=13.47% | Turnover=32.42%
   🎚️ Intra-Step TAPE: potential=0.6650 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1420 | critic_loss=0.5423 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2711 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   🧠 Objective Experts: aux_loss=-0.1841 | router_entropy=-0.0046 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.312 | risk=0.467 | discipline=0.221
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6837 | ema=0.6474 | best_ema=0.7089 | no_improve=0 | grace_until=361,248
   🔬 Alpha Diversity: mean=2.35 | std=2.48 | range=[1.15, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.82 | AMZN=3.20 | MSFT=1.81  BOT: GLD=1.35 | BRK-B=1.34 | KO=1.34
   🧬 FiLM: seq(dg=0.0135, db=0.0088, sat=0.0%) | latent(dg=0.1063, db=0.0630, sat=0.0%) | asset(dg=0.0052, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=134 (32.2%), low_vol=166 (39.9%), medium_vol=116 (27.9%)
[CYCLE] Update 317/401 | Step 353,808/500,000 | Episode 400 | Time: 33545.3s
   📊 Metrics: Return=+40.50% | Sharpe=0.788 | DD=13.47% | Turnover=32.43%
   🎚️ Intra-Step TAPE: potential=0.7540 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1922 | critic_loss=0.5467 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2733 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   🧠 Objective Experts: aux_loss=-0.2337 | router_entropy=-0.0047 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.336 | risk=0.416 | discipline=0.248
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.7878 | ema=0.6614 | best_ema=0.7089 | no_improve=0 | grace_until=361,248
[CYCLE] Update 318/401 | Step 355,320/500,000 | Episode 400 | Time: 33664.3s
   📊 Metrics: Return=+40.65% | Sharpe=0.702 | DD=13.47% | Turnover=32.59%
   🎚️ Intra-Step TAPE: potential=0.2222 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0650 | critic_loss=0.7468 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3734 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   🧠 Objective Experts: aux_loss=-0.1070 | router_entropy=-0.0047 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.298 | risk=0.484 | discipline=0.218
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.7020 | ema=0.6655 | best_ema=0.7089 | no_improve=0 | grace_until=361,248
   🔬 Alpha Diversity: mean=2.35 | std=2.47 | range=[1.14, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.92 | AMZN=2.62 | CAT=1.93  BOT: BRK-B=1.34 | KO=1.34 | GLD=1.33
   🧬 FiLM: seq(dg=0.0125, db=0.0084, sat=0.0%) | latent(dg=0.1041, db=0.0618, sat=0.0%) | asset(dg=0.0052, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=134 (32.2%), low_vol=166 (39.9%), medium_vol=116 (27.9%)
[CYCLE] Update 319/401 | Step 356,832/500,000 | Episode 401 | Time: 33783.2s
   📊 Metrics: Return=+44.57% | Sharpe=0.672 | DD=20.64% | Turnover=32.76%
   🎚️ Intra-Step TAPE: potential=0.2437 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0305 | critic_loss=0.9075 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4537 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   🧠 Objective Experts: aux_loss=-0.0717 | router_entropy=-0.0044 | diversity_loss=0.0118 | mask=[1, 1, 1] | router=return=0.259 | risk=0.581 | discipline=0.160
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6717 | ema=0.6661 | best_ema=0.7089 | no_improve=0 | grace_until=361,248
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.21% / trig 16.50%) | terminal=0.000 (peak 0.006) | TAPE=0.3556
   📈 Benchmark Relative: 1/N shaping=-0.008 (EW ret=0.00352) | SPY shaping=-0.001 (SPY ret=0.00243)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00402_shp0p724_actor.weights.h5 (Sharpe=0.724, MDD=21.94%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00403_shp0p892_actor.weights.h5 (Sharpe=0.892, MDD=17.35%)
[CYCLE] Update 320/401 | Step 358,344/500,000 | Episode 403 | Time: 33903.2s
   📊 Metrics: Return=+71.69% | Sharpe=0.892 | DD=17.35% | Turnover=32.95%
   🎚️ Intra-Step TAPE: potential=0.2356 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0323 | critic_loss=0.7989 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3994 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   🧠 Objective Experts: aux_loss=-0.0735 | router_entropy=-0.0044 | diversity_loss=0.0118 | mask=[1, 1, 1] | router=return=0.271 | risk=0.561 | discipline=0.169
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.8918 | ema=0.6887 | best_ema=0.7089 | no_improve=0 | grace_until=361,248
   🔬 Alpha Diversity: mean=2.32 | std=2.52 | range=[1.13, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.02 | AMZN=2.06 | CAT=1.82  BOT: XOM=1.37 | KO=1.35 | BRK-B=1.34
   🧬 FiLM: seq(dg=0.0103, db=0.0073, sat=0.0%) | latent(dg=0.1001, db=0.0593, sat=0.0%) | asset(dg=0.0050, db=0.0027, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=135 (32.2%), low_vol=166 (39.6%), medium_vol=118 (28.2%)
   🔒 Drawdown λ snapshot=0.008 (peak 0.008, dd 17.87% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.4810
   📈 Benchmark Relative: 1/N shaping=-0.008 (EW ret=0.00352) | SPY shaping=-0.001 (SPY ret=0.00243)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00404_shp1p082_actor.weights.h5 (Sharpe=1.082, MDD=13.15%)
[CYCLE] Update 321/401 | Step 359,856/500,000 | Episode 404 | Time: 34022.9s
   📊 Metrics: Return=+90.01% | Sharpe=1.082 | DD=13.15% | Turnover=33.20%
   🎚️ Intra-Step TAPE: potential=0.6264 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0989 | critic_loss=0.7638 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3819 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.1409 | router_entropy=-0.0046 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.328 | risk=0.457 | discipline=0.214
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=1.0819 | ema=0.7280 | best_ema=0.7280 | no_improve=0 | grace_until=361,248
   🔒 Drawdown λ snapshot=0.000 (peak 0.008, dd 3.13% / trig 16.50%) | terminal=0.000 (peak 0.602) | TAPE=0.5431
   📈 Benchmark Relative: 1/N shaping=-0.008 (EW ret=0.00352) | SPY shaping=-0.001 (SPY ret=0.00243)
[CYCLE] Update 322/401 | Step 361,368/500,000 | Episode 404 | Time: 34142.5s
   📊 Metrics: Return=+43.58% | Sharpe=0.468 | DD=20.97% | Turnover=32.61%
   🎚️ Intra-Step TAPE: potential=0.2270 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1305 | critic_loss=0.8418 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4209 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   🧠 Objective Experts: aux_loss=-0.1719 | router_entropy=-0.0045 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.306 | risk=0.488 | discipline=0.207
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.4685 | ema=0.7021 | best_ema=0.7280 | no_improve=1
   🔬 Alpha Diversity: mean=2.33 | std=2.50 | range=[1.13, 10.59] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.87 | NVDA=2.91 | CAT=1.66  BOT: NEE=1.37 | XOM=1.37 | KO=1.36
   🧬 FiLM: seq(dg=0.0132, db=0.0086, sat=0.0%) | latent(dg=0.1054, db=0.0625, sat=0.0%) | asset(dg=0.0052, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=135 (32.1%), low_vol=166 (39.5%), medium_vol=119 (28.3%)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00405_shp0p773_actor.weights.h5 (Sharpe=0.773, MDD=18.80%)
[CYCLE] Update 323/401 | Step 362,880/500,000 | Episode 406 | Time: 34262.2s
   📊 Metrics: Return=+51.95% | Sharpe=0.537 | DD=20.97% | Turnover=32.57%
   🎚️ Intra-Step TAPE: potential=0.6416 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1220 | critic_loss=0.5971 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2986 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   🧠 Objective Experts: aux_loss=-0.1638 | router_entropy=-0.0043 | diversity_loss=0.0119 | mask=[1, 1, 1] | router=return=0.272 | risk=0.564 | discipline=0.164
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5369 | ema=0.6855 | best_ema=0.7280 | no_improve=2
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.56% / trig 16.50%) | terminal=0.000 (peak 0.008) | TAPE=0.3085
   📈 Benchmark Relative: 1/N shaping=-0.006 (EW ret=0.00352) | SPY shaping=-0.000 (SPY ret=0.00243)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00411_shp0p729_actor.weights.h5 (Sharpe=0.729, MDD=11.82%)
[CYCLE] Update 324/401 | Step 364,392/500,000 | Episode 412 | Time: 34381.7s
   📊 Metrics: Return=+41.76% | Sharpe=0.305 | DD=27.63% | Turnover=31.67%
   🎚️ Intra-Step TAPE: potential=0.3557 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0723 | critic_loss=1.5963 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7982 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.1143 | router_entropy=-0.0045 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.296 | risk=0.481 | discipline=0.223
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.2420 | ema=0.6412 | best_ema=0.7280 | no_improve=3
   🔬 Alpha Diversity: mean=2.34 | std=2.45 | range=[1.11, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.76 | NVDA=2.99 | CAT=1.98  BOT: GLD=1.35 | NEE=1.35 | KO=1.34
   🧬 FiLM: seq(dg=0.0139, db=0.0089, sat=0.0%) | latent(dg=0.1066, db=0.0632, sat=0.0%) | asset(dg=0.0054, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=139 (32.5%), low_vol=170 (39.7%), medium_vol=119 (27.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.05% / trig 16.50%) | terminal=1.459 (peak 1.672) | TAPE=0.2473
   📈 Benchmark Relative: 1/N shaping=-0.013 (EW ret=0.01133) | SPY shaping=-0.001 (SPY ret=0.00914)
      💾 Sharpe-threshold checkpoint saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00414_shp0p701_actor.weights.h5 (Sharpe=0.701, MDD=12.81%)

🎛️ EXECUTION BETA UPDATE at 365,904 steps:
   action_execution_beta: 0.750 (w_exec=(1-β)w_prev + βw_raw)
   ⏹️ Early-stop transition reset: reason=action_execution_beta_update | grace_until=380,904 | best_ema_reset=yes
[CYCLE] Update 325/401 | Step 365,904/500,000 | Episode 416 | Time: 34501.2s
   📊 Metrics: Return=+63.58% | Sharpe=0.619 | DD=12.16% | Turnover=32.42%
   🎚️ Intra-Step TAPE: potential=0.2410 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0644 | critic_loss=0.9396 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4698 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   🧠 Objective Experts: aux_loss=0.0216 | router_entropy=-0.0046 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.320 | risk=0.453 | discipline=0.226
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6189 | ema=0.6390 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.26% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3572
   📈 Benchmark Relative: 1/N shaping=-0.018 (EW ret=0.01042) | SPY shaping=-0.002 (SPY ret=0.00813)
[CYCLE] Update 326/401 | Step 367,416/500,000 | Episode 416 | Time: 34620.2s
   📊 Metrics: Return=-1.76% | Sharpe=-0.247 | DD=8.65% | Turnover=34.37%
   🎚️ Intra-Step TAPE: potential=0.2315 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0051 | critic_loss=0.6223 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3111 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   🧠 Objective Experts: aux_loss=-0.0365 | router_entropy=-0.0046 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.325 | risk=0.432 | discipline=0.242
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.2471 | ema=0.5503 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
   🔬 Alpha Diversity: mean=2.34 | std=2.48 | range=[1.15, 10.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.76 | NVDA=3.08 | CAT=1.90  BOT: NEE=1.34 | KO=1.31 | BRK-B=1.29
   🧬 FiLM: seq(dg=0.0155, db=0.0096, sat=0.0%) | latent(dg=0.1092, db=0.0647, sat=0.0%) | asset(dg=0.0052, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=140 (32.4%), low_vol=170 (39.4%), medium_vol=122 (28.2%)
[CYCLE] Update 327/401 | Step 368,928/500,000 | Episode 416 | Time: 34739.3s
   📊 Metrics: Return=-6.28% | Sharpe=-0.465 | DD=13.59% | Turnover=36.46%
   🎚️ Intra-Step TAPE: potential=0.2470 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1163 | critic_loss=0.5930 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2965 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   🧠 Objective Experts: aux_loss=-0.1586 | router_entropy=-0.0047 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.326 | risk=0.410 | discipline=0.264
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.4774 | ema=0.4476 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
[CYCLE] Update 328/401 | Step 370,440/500,000 | Episode 416 | Time: 34858.5s
   📊 Metrics: Return=+1.86% | Sharpe=-0.019 | DD=13.59% | Turnover=36.86%
   🎚️ Intra-Step TAPE: potential=0.2450 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1545 | critic_loss=0.6126 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3063 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0212
   🧠 Objective Experts: aux_loss=-0.1957 | router_entropy=-0.0048 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.364 | risk=0.345 | discipline=0.291
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.0350 | ema=0.3993 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
   🔬 Alpha Diversity: mean=2.33 | std=2.49 | range=[1.15, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.85 | AMZN=3.43 | MSFT=1.79  BOT: NEE=1.34 | KO=1.31 | BRK-B=1.30
   🧬 FiLM: seq(dg=0.0179, db=0.0108, sat=0.0%) | latent(dg=0.1152, db=0.0683, sat=0.0%) | asset(dg=0.0053, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=140 (32.4%), low_vol=170 (39.4%), medium_vol=122 (28.2%)
[CYCLE] Update 329/401 | Step 371,952/500,000 | Episode 416 | Time: 34978.3s
   📊 Metrics: Return=+28.01% | Sharpe=0.682 | DD=13.59% | Turnover=36.78%
   🎚️ Intra-Step TAPE: potential=0.7483 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0092 | critic_loss=1.0756 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5378 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   🧠 Objective Experts: aux_loss=-0.0323 | router_entropy=-0.0046 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.314 | risk=0.437 | discipline=0.250
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6668 | ema=0.4261 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
[CYCLE] Update 330/401 | Step 373,464/500,000 | Episode 416 | Time: 35097.9s
   📊 Metrics: Return=+28.30% | Sharpe=0.607 | DD=13.59% | Turnover=37.19%
   🎚️ Intra-Step TAPE: potential=0.2430 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0749 | critic_loss=0.7446 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3723 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   🧠 Objective Experts: aux_loss=-0.1163 | router_entropy=-0.0044 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.283 | risk=0.515 | discipline=0.202
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5885 | ema=0.4423 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
   🔬 Alpha Diversity: mean=2.32 | std=2.51 | range=[1.13, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.22 | AMZN=1.86 | MSFT=1.75  BOT: NEE=1.36 | GLD=1.36 | KO=1.33
   🧬 FiLM: seq(dg=0.0126, db=0.0083, sat=0.0%) | latent(dg=0.1051, db=0.0623, sat=0.0%) | asset(dg=0.0053, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=140 (32.4%), low_vol=170 (39.4%), medium_vol=122 (28.2%)
[CYCLE] Update 331/401 | Step 374,976/500,000 | Episode 416 | Time: 35217.0s
   📊 Metrics: Return=+32.30% | Sharpe=0.625 | DD=13.59% | Turnover=37.18%
   🎚️ Intra-Step TAPE: potential=0.2591 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0138 | critic_loss=0.7401 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3701 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0221
   🧠 Objective Experts: aux_loss=-0.0286 | router_entropy=-0.0046 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.327 | risk=0.440 | discipline=0.233
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6062 | ema=0.4587 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
[CYCLE] Update 332/401 | Step 376,488/500,000 | Episode 416 | Time: 35336.2s
   📊 Metrics: Return=+33.24% | Sharpe=0.585 | DD=13.59% | Turnover=37.50%
   🎚️ Intra-Step TAPE: potential=0.4724 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.2050 | critic_loss=0.7259 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3630 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   🧠 Objective Experts: aux_loss=-0.2468 | router_entropy=-0.0046 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.325 | risk=0.440 | discipline=0.235
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5632 | ema=0.4692 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
   🔬 Alpha Diversity: mean=2.33 | std=2.48 | range=[1.15, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.94 | AMZN=3.88 | MSFT=1.67  BOT: NEE=1.35 | KO=1.32 | BRK-B=1.31
   🧬 FiLM: seq(dg=0.0148, db=0.0093, sat=0.0%) | latent(dg=0.1094, db=0.0648, sat=0.0%) | asset(dg=0.0053, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=140 (32.4%), low_vol=170 (39.4%), medium_vol=122 (28.2%)
[CYCLE] Update 333/401 | Step 378,000/500,000 | Episode 416 | Time: 35456.3s
   📊 Metrics: Return=+37.23% | Sharpe=0.600 | DD=13.59% | Turnover=37.76%
   🎚️ Intra-Step TAPE: potential=0.6341 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1743 | critic_loss=0.5365 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2682 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   🧠 Objective Experts: aux_loss=-0.2160 | router_entropy=-0.0045 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.310 | risk=0.476 | discipline=0.214
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5760 | ema=0.4798 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
[CYCLE] Update 334/401 | Step 379,512/500,000 | Episode 417 | Time: 35575.7s
   📊 Metrics: Return=+56.65% | Sharpe=0.553 | DD=11.21% | Turnover=35.63%
   🎚️ Intra-Step TAPE: potential=0.2317 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1231 | critic_loss=0.9986 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4993 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0210
   🧠 Objective Experts: aux_loss=0.0820 | router_entropy=-0.0044 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.271 | risk=0.543 | discipline=0.186
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5475 | ema=0.4866 | best_ema=0.6412 | no_improve=0 | grace_until=380,904
   🔬 Alpha Diversity: mean=2.30 | std=2.55 | range=[1.13, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.67 | AMZN=1.96 | MSFT=1.68  BOT: KO=1.36 | GLD=1.36 | BRK-B=1.35
   🧬 FiLM: seq(dg=0.0119, db=0.0081, sat=0.0%) | latent(dg=0.1054, db=0.0626, sat=0.0%) | asset(dg=0.0052, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=140 (32.3%), low_vol=171 (39.5%), medium_vol=122 (28.2%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.81% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.3340
   📈 Benchmark Relative: 1/N shaping=-0.025 (EW ret=0.01605) | SPY shaping=-0.003 (SPY ret=0.01278)

🧭 REWARD PHASE UPDATE at 381,024 steps:
   C_ramp_2 | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t0.45/bm1.00/tt0.30
   objective_expert_mask=[1.0, 1.0, 1.0]
   ⏹️ Early-stop transition reset: reason=reward_phase:C_ramp_2 | grace_until=396,024 | best_ema_reset=yes
[CYCLE] Update 335/401 | Step 381,024/500,000 | Episode 417 | Time: 35694.9s
   📊 Metrics: Return=+41.84% | Sharpe=0.562 | DD=13.59% | Turnover=37.93%
   🎚️ Intra-Step TAPE: potential=0.2322 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1298 | critic_loss=0.8750 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4375 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0213
   🧠 Objective Experts: aux_loss=-0.1712 | router_entropy=-0.0042 | diversity_loss=0.0118 | mask=[1, 1, 1] | router=return=0.250 | risk=0.615 | discipline=0.135
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5370 | ema=0.4916 | best_ema=0.4916 | no_improve=0 | grace_until=396,024

🌡️ TEMPERATURE UPDATE at 381,024 steps:
   temperature: 0.8500
   ⏹️ Early-stop transition reset: reason=temperature_update | grace_until=396,024 | best_ema_reset=yes
[CYCLE] Update 336/401 | Step 382,536/500,000 | Episode 419 | Time: 35815.3s
   📊 Metrics: Return=+47.74% | Sharpe=0.407 | DD=12.88% | Turnover=36.25%
   🎚️ Intra-Step TAPE: potential=0.3287 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1647 | critic_loss=1.4679 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7340 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   🧠 Objective Experts: aux_loss=-0.2062 | router_entropy=-0.0043 | diversity_loss=0.0118 | mask=[1, 1, 1] | router=return=0.258 | risk=0.578 | discipline=0.164
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3963 | ema=0.4821 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
   🔬 Alpha Diversity: mean=2.31 | std=2.52 | range=[1.13, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=2.91 | AMZN=2.09 | MSFT=1.75  BOT: XOM=1.36 | BRK-B=1.36 | KO=1.34
   🧬 FiLM: seq(dg=0.0104, db=0.0073, sat=0.0%) | latent(dg=0.1016, db=0.0603, sat=0.0%) | asset(dg=0.0051, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=140 (32.2%), low_vol=172 (39.5%), medium_vol=123 (28.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.002, dd 5.19% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2935
   📈 Benchmark Relative: 1/N shaping=0.007 (EW ret=-0.00317) | SPY shaping=0.000 (SPY ret=-0.00233)
[CYCLE] Update 337/401 | Step 384,048/500,000 | Episode 420 | Time: 35934.8s
   📊 Metrics: Return=+45.05% | Sharpe=0.357 | DD=17.37% | Turnover=36.67%
   🎚️ Intra-Step TAPE: potential=0.2629 | delta_reward=-0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1070 | critic_loss=0.7354 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3677 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0211
   🧠 Objective Experts: aux_loss=-0.1482 | router_entropy=-0.0045 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.299 | risk=0.484 | discipline=0.217
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3430 | ema=0.4682 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
   🔒 Drawdown λ snapshot=0.000 (peak 0.002, dd 3.86% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.2755
   📈 Benchmark Relative: 1/N shaping=-0.015 (EW ret=0.00442) | SPY shaping=-0.001 (SPY ret=0.00233)
[CYCLE] Update 338/401 | Step 385,560/500,000 | Episode 420 | Time: 36054.0s
   📊 Metrics: Return=+49.60% | Sharpe=0.475 | DD=18.50% | Turnover=38.25%
   🎚️ Intra-Step TAPE: potential=0.5382 | delta_reward=+0.0024
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1386 | critic_loss=0.9735 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4868 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   🧠 Objective Experts: aux_loss=-0.1803 | router_entropy=-0.0045 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.287 | risk=0.519 | discipline=0.194
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.4476 | ema=0.4661 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
   🔬 Alpha Diversity: mean=2.33 | std=2.48 | range=[1.12, 10.58] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.27 | NVDA=2.85 | CAT=2.11  BOT: XOM=1.36 | NEE=1.35 | KO=1.33
   🧬 FiLM: seq(dg=0.0123, db=0.0081, sat=0.0%) | latent(dg=0.1028, db=0.0609, sat=0.0%) | asset(dg=0.0054, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=141 (32.3%), low_vol=172 (39.4%), medium_vol=123 (28.2%)
[CYCLE] Update 339/401 | Step 387,072/500,000 | Episode 422 | Time: 36174.0s
   📊 Metrics: Return=+52.89% | Sharpe=0.494 | DD=18.50% | Turnover=38.33%
   🎚️ Intra-Step TAPE: potential=0.2320 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0297 | critic_loss=1.3399 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6699 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   🧠 Objective Experts: aux_loss=-0.0714 | router_entropy=-0.0043 | diversity_loss=0.0120 | mask=[1, 1, 1] | router=return=0.275 | risk=0.555 | discipline=0.170
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.4659 | ema=0.4661 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 6.12% / trig 16.50%) | terminal=0.000 (peak 0.002) | TAPE=0.3012
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=-0.00055) | SPY shaping=-0.004 (SPY ret=0.00153)
[CYCLE] Update 340/401 | Step 388,584/500,000 | Episode 428 | Time: 36293.9s
   📊 Metrics: Return=+41.50% | Sharpe=0.353 | DD=14.12% | Turnover=37.71%
   🎚️ Intra-Step TAPE: potential=0.2277 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0397 | critic_loss=1.7482 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8741 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.0025 | router_entropy=-0.0047 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.327 | risk=0.423 | discipline=0.250
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3297 | ema=0.4525 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
   🔬 Alpha Diversity: mean=2.35 | std=2.44 | range=[1.11, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.37 | AMZN=3.53 | CAT=2.12  BOT: GLD=1.33 | KO=1.32 | XOM=1.31
   🧬 FiLM: seq(dg=0.0156, db=0.0097, sat=0.0%) | latent(dg=0.1095, db=0.0649, sat=0.0%) | asset(dg=0.0055, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=144 (32.4%), low_vol=173 (39.0%), medium_vol=127 (28.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.88% / trig 16.50%) | terminal=0.000 (peak 1.094) | TAPE=0.2817
   📈 Benchmark Relative: 1/N shaping=-0.007 (EW ret=0.00191) | SPY shaping=-0.002 (SPY ret=0.00234)
[CYCLE] Update 341/401 | Step 390,096/500,000 | Episode 432 | Time: 36413.4s
   📊 Metrics: Return=+60.21% | Sharpe=0.578 | DD=17.58% | Turnover=39.10%
   🎚️ Intra-Step TAPE: potential=0.2217 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0346 | critic_loss=1.5700 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7850 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   🧠 Objective Experts: aux_loss=-0.0778 | router_entropy=-0.0049 | diversity_loss=0.0127 | mask=[1, 1, 1] | router=return=0.384 | risk=0.309 | discipline=0.307
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5433 | ema=0.4615 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.37% / trig 16.50%) | terminal=0.000 (peak 0.001) | TAPE=0.3339
   📈 Benchmark Relative: 1/N shaping=-0.013 (EW ret=0.00465) | SPY shaping=0.003 (SPY ret=0.00051)
[CYCLE] Update 342/401 | Step 391,608/500,000 | Episode 432 | Time: 36533.5s
   📊 Metrics: Return=+3.06% | Sharpe=0.076 | DD=10.10% | Turnover=40.98%
   🎚️ Intra-Step TAPE: potential=0.5176 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1205 | critic_loss=1.0076 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5038 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=-0.1635 | router_entropy=-0.0048 | diversity_loss=0.0128 | mask=[1, 1, 1] | router=return=0.371 | risk=0.343 | discipline=0.286
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.0250 | ema=0.4179 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
   🔬 Alpha Diversity: mean=2.38 | std=2.39 | range=[1.12, 10.53] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.87 | AMZN=4.56 | JPM=2.27  BOT: XOM=1.32 | NEE=1.31 | KO=1.29
   🧬 FiLM: seq(dg=0.0185, db=0.0110, sat=0.0%) | latent(dg=0.1165, db=0.0691, sat=0.0%) | asset(dg=0.0055, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=145 (32.4%), low_vol=174 (38.8%), medium_vol=129 (28.8%)
[CYCLE] Update 343/401 | Step 393,120/500,000 | Episode 432 | Time: 36653.4s
   📊 Metrics: Return=+4.74% | Sharpe=0.120 | DD=10.10% | Turnover=40.47%
   🎚️ Intra-Step TAPE: potential=0.2306 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1208 | critic_loss=0.7867 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3934 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0224
   🧠 Objective Experts: aux_loss=-0.1638 | router_entropy=-0.0048 | diversity_loss=0.0128 | mask=[1, 1, 1] | router=return=0.343 | risk=0.380 | discipline=0.277
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.0728 | ema=0.3834 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
[CYCLE] Update 344/401 | Step 394,632/500,000 | Episode 432 | Time: 36773.1s
   📊 Metrics: Return=+0.01% | Sharpe=-0.131 | DD=10.10% | Turnover=40.34%
   🎚️ Intra-Step TAPE: potential=0.2341 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0595 | critic_loss=0.6523 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3261 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   🧠 Objective Experts: aux_loss=-0.1026 | router_entropy=-0.0049 | diversity_loss=0.0130 | mask=[1, 1, 1] | router=return=0.390 | risk=0.306 | discipline=0.304
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1764 | ema=0.3274 | best_ema=0.4916 | no_improve=0 | grace_until=396,024
   🔬 Alpha Diversity: mean=2.37 | std=2.40 | range=[1.11, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.06 | AMZN=4.11 | CAT=1.90  BOT: GLD=1.34 | NEE=1.33 | KO=1.30
   🧬 FiLM: seq(dg=0.0195, db=0.0115, sat=0.0%) | latent(dg=0.1179, db=0.0700, sat=0.0%) | asset(dg=0.0055, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=145 (32.4%), low_vol=174 (38.8%), medium_vol=129 (28.8%)
[CYCLE] Update 345/401 | Step 396,144/500,000 | Episode 432 | Time: 36893.4s
   📊 Metrics: Return=+1.68% | Sharpe=-0.073 | DD=10.10% | Turnover=40.26%
   🎚️ Intra-Step TAPE: potential=0.2444 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0161 | critic_loss=0.8144 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4072 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0219
   🧠 Objective Experts: aux_loss=-0.0265 | router_entropy=-0.0049 | diversity_loss=0.0130 | mask=[1, 1, 1] | router=return=0.382 | risk=0.298 | discipline=0.320
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1182 | ema=0.2829 | best_ema=0.4916 | no_improve=1

🎯 ENTROPY COEF UPDATE at 396,144 steps:
   entropy_coef: 0.0003
[CYCLE] Update 346/401 | Step 397,656/500,000 | Episode 432 | Time: 37013.6s
   📊 Metrics: Return=+0.87% | Sharpe=-0.116 | DD=10.10% | Turnover=40.14%
   🎚️ Intra-Step TAPE: potential=0.2423 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0667 | critic_loss=0.6693 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3347 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0224
   🧠 Objective Experts: aux_loss=-0.1058 | router_entropy=-0.0048 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.341 | risk=0.412 | discipline=0.247
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1596 | ema=0.2386 | best_ema=0.4916 | no_improve=2
   🔬 Alpha Diversity: mean=2.35 | std=2.42 | range=[1.11, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.86 | AMZN=3.01 | CAT=2.01  BOT: XOM=1.39 | NEE=1.34 | KO=1.31
   🧬 FiLM: seq(dg=0.0152, db=0.0095, sat=0.0%) | latent(dg=0.1097, db=0.0652, sat=0.0%) | asset(dg=0.0054, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=145 (32.4%), low_vol=174 (38.8%), medium_vol=129 (28.8%)
[CYCLE] Update 347/401 | Step 399,168/500,000 | Episode 432 | Time: 37133.4s
   📊 Metrics: Return=+16.23% | Sharpe=0.291 | DD=11.08% | Turnover=39.60%
   🎚️ Intra-Step TAPE: potential=0.7434 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0686 | critic_loss=0.5973 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.2986 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0226
   🧠 Objective Experts: aux_loss=-0.1078 | router_entropy=-0.0047 | diversity_loss=0.0125 | mask=[1, 1, 1] | router=return=0.331 | risk=0.442 | discipline=0.226
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.2519 | ema=0.2399 | best_ema=0.4916 | no_improve=3
[CYCLE] Update 348/401 | Step 400,680/500,000 | Episode 432 | Time: 37254.3s
   📊 Metrics: Return=+22.57% | Sharpe=0.362 | DD=11.99% | Turnover=39.09%
   🎚️ Intra-Step TAPE: potential=0.7422 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1101 | critic_loss=0.7288 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3644 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   🧠 Objective Experts: aux_loss=-0.1486 | router_entropy=-0.0048 | diversity_loss=0.0125 | mask=[1, 1, 1] | router=return=0.348 | risk=0.397 | discipline=0.255
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3271 | ema=0.2486 | best_ema=0.4916 | no_improve=4
   🔬 Alpha Diversity: mean=2.34 | std=2.45 | range=[1.13, 10.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.18 | AMZN=4.04 | CAT=1.71  BOT: NEE=1.34 | KO=1.31 | BRK-B=1.29
   🧬 FiLM: seq(dg=0.0157, db=0.0097, sat=0.0%) | latent(dg=0.1099, db=0.0653, sat=0.0%) | asset(dg=0.0053, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=145 (32.4%), low_vol=174 (38.8%), medium_vol=129 (28.8%)
[CYCLE] Update 349/401 | Step 402,192/500,000 | Episode 432 | Time: 37375.0s
   📊 Metrics: Return=+36.06% | Sharpe=0.542 | DD=11.99% | Turnover=38.97%
   🎚️ Intra-Step TAPE: potential=0.6548 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1158 | critic_loss=0.6830 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3415 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   🧠 Objective Experts: aux_loss=-0.1543 | router_entropy=-0.0048 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.353 | risk=0.384 | discipline=0.263
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5080 | ema=0.2746 | best_ema=0.4916 | no_improve=5
[CYCLE] Update 350/401 | Step 403,704/500,000 | Episode 433 | Time: 37496.2s
   📊 Metrics: Return=+42.65% | Sharpe=0.403 | DD=19.61% | Turnover=39.06%
   🎚️ Intra-Step TAPE: potential=0.7388 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0852 | critic_loss=0.7323 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3662 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0217
   🧠 Objective Experts: aux_loss=-0.1232 | router_entropy=-0.0047 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.311 | risk=0.462 | discipline=0.226
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3683 | ema=0.2840 | best_ema=0.4916 | no_improve=6
   🔬 Alpha Diversity: mean=2.33 | std=2.48 | range=[1.11, 10.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.24 | AMZN=2.80 | MSFT=1.72  BOT: KO=1.33 | XOM=1.32 | BRK-B=1.31
   🧬 FiLM: seq(dg=0.0134, db=0.0086, sat=0.0%) | latent(dg=0.1057, db=0.0628, sat=0.0%) | asset(dg=0.0053, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=146 (32.5%), low_vol=174 (38.8%), medium_vol=129 (28.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.20% / trig 16.50%) | terminal=0.000 (peak 0.004) | TAPE=0.2785
   📈 Benchmark Relative: 1/N shaping=0.024 (EW ret=-0.01028) | SPY shaping=0.000 (SPY ret=-0.00647)

📚 TURNOVER CURRICULUM UPDATE at 405,216 steps:
   Turnover penalty scalar: 0.2
   ⏹️ Early-stop transition reset: reason=turnover_scalar_update | grace_until=420,216 | best_ema_reset=yes
[CYCLE] Update 351/401 | Step 405,216/500,000 | Episode 433 | Time: 37617.5s
   📊 Metrics: Return=+50.24% | Sharpe=0.639 | DD=11.99% | Turnover=38.97%
   🎚️ Intra-Step TAPE: potential=0.6516 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0977 | critic_loss=0.9861 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4931 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0214
   🧠 Objective Experts: aux_loss=-0.1355 | router_entropy=-0.0045 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.275 | risk=0.554 | discipline=0.171
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6051 | ema=0.3161 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
[CYCLE] Update 352/401 | Step 406,728/500,000 | Episode 435 | Time: 37738.7s
   📊 Metrics: Return=+36.63% | Sharpe=0.361 | DD=18.54% | Turnover=38.92%
   🎚️ Intra-Step TAPE: potential=0.7184 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1352 | critic_loss=1.7749 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8875 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0215
   🧠 Objective Experts: aux_loss=-0.1731 | router_entropy=-0.0045 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.283 | risk=0.521 | discipline=0.195
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3274 | ema=0.3172 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
   🔬 Alpha Diversity: mean=2.31 | std=2.51 | range=[1.13, 10.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.27 | AMZN=2.63 | MSFT=1.77  BOT: NEE=1.41 | KO=1.36 | BRK-B=1.33
   🧬 FiLM: seq(dg=0.0116, db=0.0077, sat=0.0%) | latent(dg=0.1015, db=0.0603, sat=0.0%) | asset(dg=0.0053, db=0.0028, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=146 (32.4%), low_vol=174 (38.6%), medium_vol=131 (29.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.44% / trig 16.50%) | terminal=0.000 (peak 0.003) | TAPE=0.2720
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=-0.00188) | SPY shaping=-0.001 (SPY ret=-0.00152)
[CYCLE] Update 353/401 | Step 408,240/500,000 | Episode 436 | Time: 37859.9s
   📊 Metrics: Return=+15.28% | Sharpe=0.111 | DD=29.20% | Turnover=37.62%
   🎚️ Intra-Step TAPE: potential=0.5115 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1321 | critic_loss=1.4274 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7137 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.1704 | router_entropy=-0.0048 | diversity_loss=0.0124 | mask=[1, 1, 1] | router=return=0.334 | risk=0.408 | discipline=0.258
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.0122 | ema=0.2843 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.09% / trig 16.50%) | terminal=1.419 (peak 1.584) | TAPE=0.2233
   📈 Benchmark Relative: 1/N shaping=0.025 (EW ret=0.00181) | SPY shaping=0.010 (SPY ret=-0.00047)
[CYCLE] Update 354/401 | Step 409,752/500,000 | Episode 437 | Time: 37981.0s
   📊 Metrics: Return=+44.64% | Sharpe=0.345 | DD=25.10% | Turnover=37.57%
   🎚️ Intra-Step TAPE: potential=0.3403 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1072 | critic_loss=0.9635 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4818 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0228
   🧠 Objective Experts: aux_loss=-0.1465 | router_entropy=-0.0048 | diversity_loss=0.0125 | mask=[1, 1, 1] | router=return=0.352 | risk=0.413 | discipline=0.235
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3203 | ema=0.2879 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
   🔬 Alpha Diversity: mean=2.38 | std=2.36 | range=[1.10, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.55 | AMZN=3.35 | CAT=2.13  BOT: GLD=1.35 | NEE=1.32 | KO=1.31
   🧬 FiLM: seq(dg=0.0160, db=0.0098, sat=0.0%) | latent(dg=0.1105, db=0.0657, sat=0.0%) | asset(dg=0.0058, db=0.0031, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=147 (32.5%), low_vol=174 (38.4%), medium_vol=132 (29.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.58% / trig 16.50%) | terminal=0.000 (peak 0.170) | TAPE=0.2591
   📈 Benchmark Relative: 1/N shaping=-0.024 (EW ret=0.02513) | SPY shaping=0.015 (SPY ret=-0.00231)
[CYCLE] Update 355/401 | Step 411,264/500,000 | Episode 439 | Time: 38102.4s
   📊 Metrics: Return=+31.72% | Sharpe=0.239 | DD=27.14% | Turnover=37.21%
   🎚️ Intra-Step TAPE: potential=0.6184 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1100 | critic_loss=1.7784 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8892 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=-0.1487 | router_entropy=-0.0046 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.315 | risk=0.468 | discipline=0.216
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.1689 | ema=0.2760 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.23% / trig 16.50%) | terminal=0.000 (peak 1.374) | TAPE=0.2393
   📈 Benchmark Relative: 1/N shaping=0.041 (EW ret=-0.00139) | SPY shaping=0.014 (SPY ret=-0.00362)

🧪 AUX-RETURN COEF UPDATE at 411,264 steps:
   aux_return_pred_coef: 0.2500
[CYCLE] Update 356/401 | Step 412,776/500,000 | Episode 444 | Time: 38223.4s
   📊 Metrics: Return=+54.96% | Sharpe=0.388 | DD=28.92% | Turnover=36.96%
   🎚️ Intra-Step TAPE: potential=0.5072 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0333 | critic_loss=1.9971 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.9985 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   🧠 Objective Experts: aux_loss=-0.0719 | router_entropy=-0.0048 | diversity_loss=0.0125 | mask=[1, 1, 1] | router=return=0.339 | risk=0.391 | discipline=0.270
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.2770 | ema=0.2761 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
   🔬 Alpha Diversity: mean=2.37 | std=2.38 | range=[1.11, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=4.44 | NVDA=4.33 | CAT=2.22  BOT: NEE=1.30 | KO=1.28 | XOM=1.27
   🧬 FiLM: seq(dg=0.0171, db=0.0103, sat=0.0%) | latent(dg=0.1117, db=0.0664, sat=0.0%) | asset(dg=0.0057, db=0.0030, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=150 (32.6%), low_vol=175 (38.0%), medium_vol=135 (29.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 4.03% / trig 16.50%) | terminal=0.215 (peak 0.697) | TAPE=0.2586
   📈 Benchmark Relative: 1/N shaping=-0.005 (EW ret=0.00129) | SPY shaping=-0.004 (SPY ret=0.00291)
[CYCLE] Update 357/401 | Step 414,288/500,000 | Episode 448 | Time: 38344.6s
   📊 Metrics: Return=+30.76% | Sharpe=0.238 | DD=30.09% | Turnover=37.41%
   🎚️ Intra-Step TAPE: potential=0.2449 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0696 | critic_loss=1.5201 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.7601 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   🧠 Objective Experts: aux_loss=-0.1088 | router_entropy=-0.0050 | diversity_loss=0.0128 | mask=[1, 1, 1] | router=return=0.373 | risk=0.320 | discipline=0.307
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.0950 | ema=0.2580 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 3.67% / trig 16.50%) | terminal=3.528 (peak 4.208) | TAPE=0.2348
   📈 Benchmark Relative: 1/N shaping=0.005 (EW ret=-0.00308) | SPY shaping=-0.004 (SPY ret=0.00070)
[CYCLE] Update 358/401 | Step 415,800/500,000 | Episode 448 | Time: 38465.5s
   📊 Metrics: Return=+4.72% | Sharpe=0.171 | DD=8.14% | Turnover=38.41%
   🎚️ Intra-Step TAPE: potential=0.3772 | delta_reward=-0.0021
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0497 | critic_loss=1.1574 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5787 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0226
   🧠 Objective Experts: aux_loss=0.0108 | router_entropy=-0.0050 | diversity_loss=0.0128 | mask=[1, 1, 1] | router=return=0.347 | risk=0.354 | discipline=0.299
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.1415 | ema=0.2463 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
   🔬 Alpha Diversity: mean=2.38 | std=2.36 | range=[1.08, 10.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.57 | AMZN=3.73 | CAT=2.43  BOT: XOM=1.30 | NEE=1.30 | KO=1.28
   🧬 FiLM: seq(dg=0.0187, db=0.0111, sat=0.0%) | latent(dg=0.1142, db=0.0679, sat=0.0%) | asset(dg=0.0057, db=0.0030, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=151 (32.5%), low_vol=176 (37.9%), medium_vol=137 (29.5%)
[CYCLE] Update 359/401 | Step 417,312/500,000 | Episode 448 | Time: 38586.5s
   📊 Metrics: Return=-0.97% | Sharpe=-0.157 | DD=13.55% | Turnover=38.28%
   🎚️ Intra-Step TAPE: potential=0.2464 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0055 | critic_loss=0.8659 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4330 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=-0.0329 | router_entropy=-0.0048 | diversity_loss=0.0127 | mask=[1, 1, 1] | router=return=0.343 | risk=0.397 | discipline=0.261
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1854 | ema=0.2031 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
[CYCLE] Update 360/401 | Step 418,824/500,000 | Episode 448 | Time: 38707.4s
   📊 Metrics: Return=+7.24% | Sharpe=0.159 | DD=13.55% | Turnover=37.85%
   🎚️ Intra-Step TAPE: potential=0.2409 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0335 | critic_loss=1.0137 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5068 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=-0.0722 | router_entropy=-0.0049 | diversity_loss=0.0129 | mask=[1, 1, 1] | router=return=0.349 | risk=0.370 | discipline=0.282
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.1348 | ema=0.1963 | best_ema=0.3161 | no_improve=0 | grace_until=420,216
   🔬 Alpha Diversity: mean=2.36 | std=2.40 | range=[1.11, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.40 | AMZN=3.88 | JPM=1.95  BOT: NEE=1.32 | BRK-B=1.30 | KO=1.29
   🧬 FiLM: seq(dg=0.0174, db=0.0103, sat=0.0%) | latent(dg=0.1111, db=0.0661, sat=0.0%) | asset(dg=0.0056, db=0.0030, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=151 (32.5%), low_vol=176 (37.9%), medium_vol=137 (29.5%)
[CYCLE] Update 361/401 | Step 420,336/500,000 | Episode 448 | Time: 38828.5s
   📊 Metrics: Return=+27.21% | Sharpe=0.622 | DD=14.08% | Turnover=37.55%
   🎚️ Intra-Step TAPE: potential=0.7465 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0704 | critic_loss=0.7581 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3791 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=0.0316 | router_entropy=-0.0050 | diversity_loss=0.0130 | mask=[1, 1, 1] | router=return=0.369 | risk=0.330 | discipline=0.301
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=1512 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.5996 | ema=0.2366 | best_ema=0.3161 | no_improve=1

📚 PPO ROLLOUT UPDATE at 420,336 steps:
   Timesteps per update: 2016
   ⏹️ Early-stop transition reset: reason=rollout_update | grace_until=435,336 | best_ema_reset=yes
[CYCLE] Update 362/401 | Step 422,352/500,000 | Episode 448 | Time: 38986.6s
   📊 Metrics: Return=+34.31% | Sharpe=0.670 | DD=14.08% | Turnover=37.96%
   🎚️ Intra-Step TAPE: potential=0.7346 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0679 | critic_loss=0.9679 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4840 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   🧠 Objective Experts: aux_loss=-0.1069 | router_entropy=-0.0050 | diversity_loss=0.0129 | mask=[1, 1, 1] | router=return=0.361 | risk=0.362 | discipline=0.277
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6449 | ema=0.2775 | best_ema=0.2775 | no_improve=0 | grace_until=435,336
   🔬 Alpha Diversity: mean=2.38 | std=2.36 | range=[1.11, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.56 | AMZN=4.10 | CAT=1.82  BOT: BRK-B=1.34 | NEE=1.30 | KO=1.28
   🧬 FiLM: seq(dg=0.0173, db=0.0102, sat=0.0%) | latent(dg=0.1100, db=0.0655, sat=0.0%) | asset(dg=0.0056, db=0.0030, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=151 (32.5%), low_vol=176 (37.9%), medium_vol=137 (29.5%)
[CYCLE] Update 363/401 | Step 424,368/500,000 | Episode 448 | Time: 39142.0s
   📊 Metrics: Return=+39.88% | Sharpe=0.688 | DD=14.08% | Turnover=38.17%
   🎚️ Intra-Step TAPE: potential=0.5959 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0215 | critic_loss=1.0964 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.5482 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   🧠 Objective Experts: aux_loss=-0.0597 | router_entropy=-0.0048 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.327 | risk=0.419 | discipline=0.254
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6604 | ema=0.3158 | best_ema=0.3158 | no_improve=0 | grace_until=435,336
[CYCLE] Update 364/401 | Step 426,384/500,000 | Episode 448 | Time: 39297.6s
   📊 Metrics: Return=+45.13% | Sharpe=0.696 | DD=14.08% | Turnover=38.20%
   🎚️ Intra-Step TAPE: potential=0.7207 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0576 | critic_loss=0.9920 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.4960 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0223
   🧠 Objective Experts: aux_loss=-0.0958 | router_entropy=-0.0048 | diversity_loss=0.0125 | mask=[1, 1, 1] | router=return=0.331 | risk=0.431 | discipline=0.238
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.6682 | ema=0.3510 | best_ema=0.3510 | no_improve=0 | grace_until=435,336
   🔬 Alpha Diversity: mean=2.34 | std=2.42 | range=[1.11, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.06 | AMZN=2.33 | MSFT=2.03  BOT: NEE=1.34 | BRK-B=1.31 | KO=1.29
   🧬 FiLM: seq(dg=0.0145, db=0.0089, sat=0.0%) | latent(dg=0.1076, db=0.0640, sat=0.0%) | asset(dg=0.0054, db=0.0029, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=151 (32.5%), low_vol=176 (37.9%), medium_vol=137 (29.5%)
[CYCLE] Update 365/401 | Step 428,400/500,000 | Episode 449 | Time: 39453.6s
   📊 Metrics: Return=+59.88% | Sharpe=0.434 | DD=27.71% | Turnover=37.49%
   🎚️ Intra-Step TAPE: potential=0.2364 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0285 | critic_loss=1.2088 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6044 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.0092 | router_entropy=-0.0047 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.312 | risk=0.476 | discipline=0.213
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3472 | ema=0.3506 | best_ema=0.3510 | no_improve=0 | grace_until=435,336
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 5.20% / trig 16.50%) | terminal=1.780 (peak 2.374) | TAPE=0.2701
   📈 Benchmark Relative: 1/N shaping=0.016 (EW ret=-0.00414) | SPY shaping=0.009 (SPY ret=-0.00771)

🎛️ EXECUTION BETA UPDATE at 430,416 steps:
   action_execution_beta: 0.900 (w_exec=(1-β)w_prev + βw_raw)
   ⏹️ Early-stop transition reset: reason=action_execution_beta_update | grace_until=445,416 | best_ema_reset=yes
[CYCLE] Update 366/401 | Step 430,416/500,000 | Episode 450 | Time: 39609.8s
   📊 Metrics: Return=+12.45% | Sharpe=0.086 | DD=27.97% | Turnover=37.34%
   🎚️ Intra-Step TAPE: potential=0.2341 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0293 | critic_loss=1.3147 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6574 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0216
   🧠 Objective Experts: aux_loss=-0.0668 | router_entropy=-0.0046 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.294 | risk=0.504 | discipline=0.202
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.0051 | ema=0.3151 | best_ema=0.3506 | no_improve=0 | grace_until=445,416
   🔬 Alpha Diversity: mean=2.32 | std=2.47 | range=[1.11, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.97 | AMZN=2.58 | MSFT=1.66  BOT: XOM=1.36 | KO=1.35 | BRK-B=1.34
   🧬 FiLM: seq(dg=0.0128, db=0.0082, sat=0.0%) | latent(dg=0.1033, db=0.0615, sat=0.0%) | asset(dg=0.0056, db=0.0030, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=151 (32.4%), low_vol=177 (38.0%), medium_vol=138 (29.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 13.63% / trig 16.50%) | terminal=4.819 (peak 4.853) | TAPE=0.2252
   📈 Benchmark Relative: 1/N shaping=0.011 (EW ret=-0.01444) | SPY shaping=0.010 (SPY ret=-0.01938)
[CYCLE] Update 367/401 | Step 432,432/500,000 | Episode 452 | Time: 39765.5s
   📊 Metrics: Return=+35.57% | Sharpe=0.281 | DD=23.65% | Turnover=38.81%
   🎚️ Intra-Step TAPE: potential=0.2252 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1375 | critic_loss=3.6221 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.8111 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0221
   🧠 Objective Experts: aux_loss=-0.1754 | router_entropy=-0.0046 | diversity_loss=0.0122 | mask=[1, 1, 1] | router=return=0.302 | risk=0.500 | discipline=0.198
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.2483 | ema=0.3084 | best_ema=0.3506 | no_improve=0 | grace_until=445,416
   🔒 Drawdown λ snapshot=0.000 (peak 0.006, dd 8.08% / trig 16.50%) | terminal=0.000 (peak 1.064) | TAPE=0.2507
   📈 Benchmark Relative: 1/N shaping=-0.007 (EW ret=-0.00291) | SPY shaping=-0.007 (SPY ret=0.00038)
[CYCLE] Update 368/401 | Step 434,448/500,000 | Episode 454 | Time: 39921.4s
   📊 Metrics: Return=+50.07% | Sharpe=0.460 | DD=20.24% | Turnover=40.31%
   🎚️ Intra-Step TAPE: potential=0.7125 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1337 | critic_loss=1.7814 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.8907 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   🧠 Objective Experts: aux_loss=-0.1716 | router_entropy=-0.0047 | diversity_loss=0.0121 | mask=[1, 1, 1] | router=return=0.311 | risk=0.472 | discipline=0.218
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.4146 | ema=0.3190 | best_ema=0.3506 | no_improve=0 | grace_until=445,416
   🔬 Alpha Diversity: mean=2.35 | std=2.40 | range=[1.09, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.17 | AMZN=2.94 | CAT=2.24  BOT: NEE=1.32 | KO=1.30 | BRK-B=1.30
   🧬 FiLM: seq(dg=0.0139, db=0.0086, sat=0.0%) | latent(dg=0.1029, db=0.0612, sat=0.0%) | asset(dg=0.0056, db=0.0030, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=151 (32.1%), low_vol=179 (38.1%), medium_vol=140 (29.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 16.50%) | terminal=0.000 (peak 0.006) | TAPE=0.2874
   📈 Benchmark Relative: 1/N shaping=0.029 (EW ret=-0.00035) | SPY shaping=0.001 (SPY ret=0.00352)
[CYCLE] Update 369/401 | Step 436,464/500,000 | Episode 460 | Time: 40077.2s
   📊 Metrics: Return=+41.07% | Sharpe=0.379 | DD=22.65% | Turnover=41.56%
   🎚️ Intra-Step TAPE: potential=0.2164 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0779 | critic_loss=2.0196 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.0098 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   🧠 Objective Experts: aux_loss=0.0401 | router_entropy=-0.0049 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.350 | risk=0.383 | discipline=0.267
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3225 | ema=0.3194 | best_ema=0.3506 | no_improve=0 | grace_until=445,416
   🔒 Drawdown λ snapshot=0.073 (peak 0.073, dd 25.70% / trig 16.50%) | terminal=0.000 (peak 0.161) | TAPE=0.2676
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.00031) | SPY shaping=0.000 (SPY ret=-0.00025)
[CYCLE] Update 370/401 | Step 438,480/500,000 | Episode 464 | Time: 40232.5s
   📊 Metrics: Return=+59.59% | Sharpe=0.556 | DD=20.84% | Turnover=42.01%
   🎚️ Intra-Step TAPE: potential=0.6557 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0052 | critic_loss=2.1085 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.0543 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0220
   🧠 Objective Experts: aux_loss=-0.0328 | router_entropy=-0.0050 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.356 | risk=0.342 | discipline=0.303
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.4957 | ema=0.3370 | best_ema=0.3506 | no_improve=0 | grace_until=445,416
   🔬 Alpha Diversity: mean=2.36 | std=2.39 | range=[1.09, 10.49] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.02 | AMZN=3.77 | CAT=1.95  BOT: XOM=1.36 | NEE=1.30 | KO=1.29
   🧬 FiLM: seq(dg=0.0192, db=0.0112, sat=0.0%) | latent(dg=0.1138, db=0.0678, sat=0.0%) | asset(dg=0.0057, db=0.0031, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=154 (32.1%), low_vol=182 (37.9%), medium_vol=144 (30.0%)
   🔒 Drawdown λ snapshot=0.291 (peak 0.320, dd 10.62% / trig 16.50%) | terminal=0.000 (peak 2.646) | TAPE=0.3130
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=0.00151) | SPY shaping=0.002 (SPY ret=-0.00024)

🧭 REWARD PHASE UPDATE at 440,496 steps:
   C_full_tape | base=True dsr=True turnover=True benchmark=True terminal=True | weights=b1.00/d1.00/t1.00/bm1.00/tt1.00
   objective_expert_mask=[1.0, 1.0, 1.0]
   ⏹️ Early-stop transition reset: reason=reward_phase:C_full_tape | grace_until=455,496 | best_ema_reset=yes
[CYCLE] Update 371/401 | Step 440,496/500,000 | Episode 464 | Time: 40388.0s
   📊 Metrics: Return=-11.74% | Sharpe=-0.308 | DD=28.31% | Turnover=46.77%
   🎚️ Intra-Step TAPE: potential=0.6086 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0309 | critic_loss=1.3105 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.6553 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   🧠 Objective Experts: aux_loss=-0.0697 | router_entropy=-0.0050 | diversity_loss=0.0128 | mask=[1, 1, 1] | router=return=0.362 | risk=0.341 | discipline=0.297
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=504 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.4887 | ema=0.2544 | best_ema=0.3370 | no_improve=0 | grace_until=455,496

📚 PPO BATCH SIZE UPDATE at 440,496 steps:
   Batch size: 672
   ⏹️ Early-stop transition reset: reason=batch_size_update | grace_until=455,496 | best_ema_reset=yes
[CYCLE] Update 372/401 | Step 442,512/500,000 | Episode 464 | Time: 40535.9s
   📊 Metrics: Return=-14.62% | Sharpe=-0.339 | DD=28.31% | Turnover=46.22%
   🎚️ Intra-Step TAPE: potential=0.5191 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0729 | critic_loss=5.9650 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.9825 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   🧠 Objective Experts: aux_loss=-0.1118 | router_entropy=-0.0050 | diversity_loss=0.0129 | mask=[1, 1, 1] | router=return=0.374 | risk=0.328 | discipline=0.299
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.5149 | ema=0.1775 | best_ema=0.2544 | no_improve=0 | grace_until=455,496
   🔬 Alpha Diversity: mean=2.39 | std=2.33 | range=[1.10, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=5.09 | NVDA=5.06 | CAT=2.29  BOT: XOM=1.30 | NEE=1.27 | KO=1.26
   🧬 FiLM: seq(dg=0.0197, db=0.0114, sat=0.0%) | latent(dg=0.1126, db=0.0671, sat=0.0%) | asset(dg=0.0058, db=0.0031, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=154 (32.1%), low_vol=182 (37.9%), medium_vol=144 (30.0%)
[CYCLE] Update 373/401 | Step 444,528/500,000 | Episode 464 | Time: 40674.6s
   📊 Metrics: Return=-14.81% | Sharpe=-0.319 | DD=28.31% | Turnover=47.46%
   🎚️ Intra-Step TAPE: potential=0.2401 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1276 | critic_loss=2.8659 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.4330 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0227
   🧠 Objective Experts: aux_loss=-0.1664 | router_entropy=-0.0050 | diversity_loss=0.0128 | mask=[1, 1, 1] | router=return=0.376 | risk=0.331 | discipline=0.292
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.5047 | ema=0.1093 | best_ema=0.2544 | no_improve=0 | grace_until=455,496
[CYCLE] Update 374/401 | Step 446,544/500,000 | Episode 464 | Time: 40813.9s
   📊 Metrics: Return=-10.25% | Sharpe=-0.209 | DD=28.31% | Turnover=48.27%
   🎚️ Intra-Step TAPE: potential=0.6805 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1216 | critic_loss=3.0964 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.5482 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0224
   🧠 Objective Experts: aux_loss=-0.1599 | router_entropy=-0.0049 | diversity_loss=0.0125 | mask=[1, 1, 1] | router=return=0.331 | risk=0.414 | discipline=0.255
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.4020 | ema=0.0581 | best_ema=0.2544 | no_improve=0 | grace_until=455,496
   🔬 Alpha Diversity: mean=2.35 | std=2.40 | range=[1.10, 10.52] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.04 | AMZN=2.89 | MSFT=2.22  BOT: NEE=1.32 | KO=1.30 | BRK-B=1.27
   🧬 FiLM: seq(dg=0.0159, db=0.0095, sat=0.0%) | latent(dg=0.1047, db=0.0623, sat=0.0%) | asset(dg=0.0056, db=0.0030, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=154 (32.1%), low_vol=182 (37.9%), medium_vol=144 (30.0%)
[CYCLE] Update 375/401 | Step 448,560/500,000 | Episode 464 | Time: 40956.5s
   📊 Metrics: Return=-12.19% | Sharpe=-0.232 | DD=28.31% | Turnover=48.51%
   🎚️ Intra-Step TAPE: potential=0.2613 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1831 | critic_loss=3.1760 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.5880 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0225
   🧠 Objective Experts: aux_loss=-0.2215 | router_entropy=-0.0048 | diversity_loss=0.0124 | mask=[1, 1, 1] | router=return=0.323 | risk=0.445 | discipline=0.232
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.4272 | ema=0.0096 | best_ema=0.2544 | no_improve=0 | grace_until=455,496
[CYCLE] Update 376/401 | Step 450,576/500,000 | Episode 464 | Time: 41096.6s
   📊 Metrics: Return=-11.65% | Sharpe=-0.212 | DD=28.31% | Turnover=48.55%
   🎚️ Intra-Step TAPE: potential=0.2395 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1072 | critic_loss=2.7537 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.3769 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0222
   🧠 Objective Experts: aux_loss=-0.1453 | router_entropy=-0.0048 | diversity_loss=0.0124 | mask=[1, 1, 1] | router=return=0.316 | risk=0.450 | discipline=0.234
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.4076 | ema=-0.0321 | best_ema=0.2544 | no_improve=0 | grace_until=455,496
   🔬 Alpha Diversity: mean=2.34 | std=2.42 | range=[1.10, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=3.90 | NVDA=3.73 | JPM=1.76  BOT: NEE=1.33 | KO=1.30 | BRK-B=1.28
   🧬 FiLM: seq(dg=0.0146, db=0.0089, sat=0.0%) | latent(dg=0.1034, db=0.0616, sat=0.0%) | asset(dg=0.0058, db=0.0031, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=154 (32.1%), low_vol=182 (37.9%), medium_vol=144 (30.0%)

🌡️ TEMPERATURE UPDATE at 450,576 steps:
   temperature: 0.8000
   ⏹️ Early-stop transition reset: reason=temperature_update | grace_until=465,576 | best_ema_reset=yes
[CYCLE] Update 377/401 | Step 452,592/500,000 | Episode 465 | Time: 41237.4s
   📊 Metrics: Return=+14.40% | Sharpe=0.099 | DD=27.29% | Turnover=46.43%
   🎚️ Intra-Step TAPE: potential=0.2136 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0888 | critic_loss=2.8339 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.4169 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0218
   🧠 Objective Experts: aux_loss=-0.1264 | router_entropy=-0.0047 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.312 | risk=0.467 | discipline=0.221
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.0542 | ema=-0.0343 | best_ema=-0.0321 | no_improve=0 | grace_until=465,576
   🔒 Drawdown λ snapshot=1.255 (peak 1.278, dd 21.49% / trig 16.50%) | terminal=4.270 (peak 5.000) | TAPE=0.2257
   📈 Benchmark Relative: 1/N shaping=-0.009 (EW ret=0.00182) | SPY shaping=0.003 (SPY ret=-0.00173)
[CYCLE] Update 378/401 | Step 454,608/500,000 | Episode 466 | Time: 41381.1s
   📊 Metrics: Return=+47.79% | Sharpe=0.446 | DD=16.67% | Turnover=48.92%
   🎚️ Intra-Step TAPE: potential=0.2274 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1215 | critic_loss=2.9738 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.4869 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0224
   🧠 Objective Experts: aux_loss=-0.1598 | router_entropy=-0.0046 | diversity_loss=0.0123 | mask=[1, 1, 1] | router=return=0.295 | risk=0.519 | discipline=0.186
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.3269 | ema=0.0018 | best_ema=0.0018 | no_improve=0 | grace_until=465,576
   🔬 Alpha Diversity: mean=2.34 | std=2.40 | range=[1.09, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.61 | AMZN=2.30 | CAT=1.95  BOT: BRK-B=1.42 | NEE=1.36 | KO=1.32
   🧬 FiLM: seq(dg=0.0126, db=0.0078, sat=0.0%) | latent(dg=0.0973, db=0.0579, sat=0.0%) | asset(dg=0.0059, db=0.0032, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=155 (32.2%), low_vol=182 (37.8%), medium_vol=145 (30.1%)
   🔒 Drawdown λ snapshot=1.115 (peak 1.299, dd 10.45% / trig 16.50%) | terminal=0.000 (peak 3.614) | TAPE=0.2902
   📈 Benchmark Relative: 1/N shaping=0.031 (EW ret=-0.01283) | SPY shaping=-0.001 (SPY ret=-0.00689)
[CYCLE] Update 379/401 | Step 456,624/500,000 | Episode 468 | Time: 41524.7s
   📊 Metrics: Return=+29.08% | Sharpe=0.252 | DD=15.05% | Turnover=48.74%
   🎚️ Intra-Step TAPE: potential=0.6364 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1188 | critic_loss=3.9210 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.9605 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0235
   🧠 Objective Experts: aux_loss=-0.1582 | router_entropy=-0.0048 | diversity_loss=0.0124 | mask=[1, 1, 1] | router=return=0.334 | risk=0.451 | discipline=0.214
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.1339 | ema=0.0150 | best_ema=0.0150 | no_improve=0 | grace_until=465,576
   🔒 Drawdown λ snapshot=0.676 (peak 1.299, dd 0.33% / trig 16.50%) | terminal=0.000 (peak 0.000) | TAPE=0.2612
   📈 Benchmark Relative: 1/N shaping=0.038 (EW ret=-0.01450) | SPY shaping=0.008 (SPY ret=-0.01353)

🎯 ENTROPY COEF UPDATE at 456,624 steps:
   entropy_coef: 0.0001
[CYCLE] Update 380/401 | Step 458,640/500,000 | Episode 470 | Time: 41665.3s
   📊 Metrics: Return=+12.75% | Sharpe=0.083 | DD=28.31% | Turnover=48.63%
   🎚️ Intra-Step TAPE: potential=0.7413 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.2148 | critic_loss=3.4185 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.7092 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   🧠 Objective Experts: aux_loss=-0.2499 | router_entropy=-0.0048 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.344 | risk=0.410 | discipline=0.246
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1136 | ema=0.0022 | best_ema=0.0150 | no_improve=0 | grace_until=465,576
   🔬 Alpha Diversity: mean=2.37 | std=2.34 | range=[1.08, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.29 | AMZN=3.36 | CAT=2.28  BOT: NEE=1.33 | KO=1.28 | BRK-B=1.27
   🧬 FiLM: seq(dg=0.0167, db=0.0099, sat=0.0%) | latent(dg=0.1095, db=0.0653, sat=0.0%) | asset(dg=0.0059, db=0.0032, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=156 (32.1%), low_vol=183 (37.7%), medium_vol=147 (30.2%)
   🔒 Drawdown λ snapshot=0.115 (peak 0.254, dd 0.57% / trig 16.50%) | terminal=0.339 (peak 1.299) | TAPE=0.2220
   📈 Benchmark Relative: 1/N shaping=-0.027 (EW ret=0.00913) | SPY shaping=0.003 (SPY ret=0.00248)
[CYCLE] Update 381/401 | Step 460,656/500,000 | Episode 476 | Time: 41804.6s
   📊 Metrics: Return=+27.97% | Sharpe=0.240 | DD=20.26% | Turnover=48.66%
   🎚️ Intra-Step TAPE: potential=0.7073 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0459 | critic_loss=3.4760 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.7380 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0230
   🧠 Objective Experts: aux_loss=-0.0813 | router_entropy=-0.0049 | diversity_loss=0.0127 | mask=[1, 1, 1] | router=return=0.342 | risk=0.406 | discipline=0.252
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.1231 | ema=0.0142 | best_ema=0.0150 | no_improve=0 | grace_until=465,576
   🔒 Drawdown λ snapshot=0.000 (peak 0.254, dd 1.47% / trig 16.50%) | terminal=0.000 (peak 0.007) | TAPE=0.2513
   📈 Benchmark Relative: 1/N shaping=0.015 (EW ret=-0.01450) | SPY shaping=0.002 (SPY ret=-0.01353)
[CYCLE] Update 382/401 | Step 462,672/500,000 | Episode 480 | Time: 41943.6s
   📊 Metrics: Return=+15.23% | Sharpe=0.093 | DD=19.88% | Turnover=49.87%
   🎚️ Intra-Step TAPE: potential=0.7256 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1171 | critic_loss=3.8662 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.9331 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   🧠 Objective Experts: aux_loss=-0.1526 | router_entropy=-0.0051 | diversity_loss=0.0130 | mask=[1, 1, 1] | router=return=0.358 | risk=0.355 | discipline=0.288
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.0344 | ema=0.0094 | best_ema=0.0150 | no_improve=0 | grace_until=465,576
   🔬 Alpha Diversity: mean=2.39 | std=2.31 | range=[1.08, 10.53] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.44 | AMZN=3.83 | CAT=2.62  BOT: XOM=1.31 | NEE=1.29 | KO=1.26
   🧬 FiLM: seq(dg=0.0194, db=0.0111, sat=0.0%) | latent(dg=0.1073, db=0.0640, sat=0.0%) | asset(dg=0.0059, db=0.0032, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=158 (31.9%), low_vol=189 (38.1%), medium_vol=149 (30.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.254, dd 4.47% / trig 16.50%) | terminal=0.000 (peak 0.005) | TAPE=0.2377
   📈 Benchmark Relative: 1/N shaping=-0.007 (EW ret=-0.00337) | SPY shaping=0.002 (SPY ret=-0.00610)
[CYCLE] Update 383/401 | Step 464,688/500,000 | Episode 480 | Time: 42082.7s
   📊 Metrics: Return=+39.19% | Sharpe=1.002 | DD=19.50% | Turnover=43.73%
   🎚️ Intra-Step TAPE: potential=0.2164 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1184 | critic_loss=2.6666 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.3333 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0228
   🧠 Objective Experts: aux_loss=-0.1536 | router_entropy=-0.0051 | diversity_loss=0.0130 | mask=[1, 1, 1] | router=return=0.375 | risk=0.339 | discipline=0.286
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.9276 | ema=0.1012 | best_ema=0.1012 | no_improve=0 | grace_until=465,576

📚 EPISODE HORIZON UPDATE at 466,704 steps:
   Episode horizon: 1716 steps
[CYCLE] Update 384/401 | Step 466,704/500,000 | Episode 480 | Time: 42221.8s
   📊 Metrics: Return=+22.99% | Sharpe=0.452 | DD=28.82% | Turnover=45.04%
   🎚️ Intra-Step TAPE: potential=0.2530 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0218 | critic_loss=2.5561 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.2781 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0229
   🧠 Objective Experts: aux_loss=-0.0137 | router_entropy=-0.0051 | diversity_loss=0.0131 | mask=[1, 1, 1] | router=return=0.391 | risk=0.317 | discipline=0.293
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.2742 | ema=0.1185 | best_ema=0.1185 | no_improve=0
   🔬 Alpha Diversity: mean=2.39 | std=2.30 | range=[1.08, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.47 | AMZN=3.50 | CAT=2.28  BOT: BRK-B=1.36 | NEE=1.32 | KO=1.26
   🧬 FiLM: seq(dg=0.0211, db=0.0120, sat=0.0%) | latent(dg=0.1085, db=0.0648, sat=0.0%) | asset(dg=0.0059, db=0.0032, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=158 (31.9%), low_vol=189 (38.1%), medium_vol=149 (30.0%)

📚 EPISODE HORIZON UPDATE at 468,720 steps:
   Episode horizon: 1972 steps
[CYCLE] Update 385/401 | Step 468,720/500,000 | Episode 480 | Time: 42361.0s
   📊 Metrics: Return=+23.21% | Sharpe=0.374 | DD=28.82% | Turnover=44.53%
   🎚️ Intra-Step TAPE: potential=0.4658 | delta_reward=+0.0023
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0865 | critic_loss=3.1971 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.5985 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0235
   🧠 Objective Experts: aux_loss=-0.1228 | router_entropy=-0.0051 | diversity_loss=0.0133 | mask=[1, 1, 1] | router=return=0.402 | risk=0.315 | discipline=0.283
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.2010 | ema=0.1268 | best_ema=0.1268 | no_improve=0

📚 TURNOVER CURRICULUM UPDATE at 470,736 steps:
   Turnover penalty scalar: 0.3
   ⏹️ Early-stop transition reset: reason=turnover_scalar_update | grace_until=485,736 | best_ema_reset=yes

📚 EPISODE HORIZON UPDATE at 470,736 steps:
   Episode horizon: 2227 steps
[CYCLE] Update 386/401 | Step 470,736/500,000 | Episode 480 | Time: 42500.0s
   📊 Metrics: Return=+15.97% | Sharpe=0.234 | DD=28.82% | Turnover=44.33%
   🎚️ Intra-Step TAPE: potential=0.2288 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1250 | critic_loss=3.3389 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.6694 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0237
   🧠 Objective Experts: aux_loss=-0.1617 | router_entropy=-0.0051 | diversity_loss=0.0133 | mask=[1, 1, 1] | router=return=0.401 | risk=0.317 | discipline=0.283
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.0621 | ema=0.1203 | best_ema=0.1268 | no_improve=0 | grace_until=485,736
   🔬 Alpha Diversity: mean=2.42 | std=2.23 | range=[1.08, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=5.60 | AMZN=4.00 | CAT=2.86  BOT: NEE=1.32 | BRK-B=1.25 | KO=1.22
   🧬 FiLM: seq(dg=0.0200, db=0.0115, sat=0.0%) | latent(dg=0.1069, db=0.0639, sat=0.0%) | asset(dg=0.0059, db=0.0033, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=158 (31.9%), low_vol=189 (38.1%), medium_vol=149 (30.0%)

📚 EPISODE HORIZON UPDATE at 472,752 steps:
   Episode horizon: 2483 steps
[CYCLE] Update 387/401 | Step 472,752/500,000 | Episode 480 | Time: 42639.0s
   📊 Metrics: Return=+22.85% | Sharpe=0.280 | DD=28.82% | Turnover=44.12%
   🎚️ Intra-Step TAPE: potential=0.2807 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0255 | critic_loss=7.5250 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=3.7625 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0235
   🧠 Objective Experts: aux_loss=-0.0617 | router_entropy=-0.0051 | diversity_loss=0.0132 | mask=[1, 1, 1] | router=return=0.380 | risk=0.343 | discipline=0.277
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.1102 | ema=0.1193 | best_ema=0.1268 | no_improve=0 | grace_until=485,736

📚 EPISODE HORIZON UPDATE at 474,768 steps:
   Episode horizon: 2739 steps
[CYCLE] Update 388/401 | Step 474,768/500,000 | Episode 480 | Time: 42777.9s
   📊 Metrics: Return=+24.19% | Sharpe=0.263 | DD=28.82% | Turnover=44.24%
   🎚️ Intra-Step TAPE: potential=0.2533 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1564 | critic_loss=5.1894 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.5947 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0238
   🧠 Objective Experts: aux_loss=-0.1927 | router_entropy=-0.0051 | diversity_loss=0.0131 | mask=[1, 1, 1] | router=return=0.356 | risk=0.386 | discipline=0.258
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.0917 | ema=0.1165 | best_ema=0.1268 | no_improve=0 | grace_until=485,736
   🔬 Alpha Diversity: mean=2.40 | std=2.27 | range=[1.08, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.56 | CAT=2.98 | AMZN=2.89  BOT: NEE=1.37 | BRK-B=1.25 | KO=1.24
   🧬 FiLM: seq(dg=0.0158, db=0.0093, sat=0.0%) | latent(dg=0.0959, db=0.0571, sat=0.0%) | asset(dg=0.0058, db=0.0032, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=158 (31.9%), low_vol=189 (38.1%), medium_vol=149 (30.0%)

📚 EPISODE HORIZON UPDATE at 476,784 steps:
   Episode horizon set to full dataset
[CYCLE] Update 389/401 | Step 476,784/500,000 | Episode 480 | Time: 42916.9s
   📊 Metrics: Return=+27.77% | Sharpe=0.267 | DD=28.82% | Turnover=44.22%
   🎚️ Intra-Step TAPE: potential=0.5348 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0884 | critic_loss=5.2596 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.6298 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0235
   🧠 Objective Experts: aux_loss=-0.1243 | router_entropy=-0.0050 | diversity_loss=0.0129 | mask=[1, 1, 1] | router=return=0.321 | risk=0.424 | discipline=0.255
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.0966 | ema=0.1145 | best_ema=0.1268 | no_improve=0 | grace_until=485,736

📚 EPISODE HORIZON UPDATE at 478,800 steps:
   Episode horizon set to full dataset
[CYCLE] Update 390/401 | Step 478,800/500,000 | Episode 480 | Time: 43056.2s
   📊 Metrics: Return=+26.05% | Sharpe=0.228 | DD=28.82% | Turnover=44.22%
   🎚️ Intra-Step TAPE: potential=0.2703 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1739 | critic_loss=5.0578 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.5289 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0231
   🧠 Objective Experts: aux_loss=-0.2094 | router_entropy=-0.0050 | diversity_loss=0.0128 | mask=[1, 1, 1] | router=return=0.319 | risk=0.427 | discipline=0.254
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.0572 | ema=0.1088 | best_ema=0.1268 | no_improve=0 | grace_until=485,736
   🔬 Alpha Diversity: mean=2.36 | std=2.35 | range=[1.08, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.97 | AMZN=3.75 | CAT=2.16  BOT: BRK-B=1.41 | NEE=1.38 | KO=1.25
   🧬 FiLM: seq(dg=0.0145, db=0.0088, sat=0.0%) | latent(dg=0.1013, db=0.0605, sat=0.0%) | asset(dg=0.0059, db=0.0032, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=158 (31.9%), low_vol=189 (38.1%), medium_vol=149 (30.0%)

🎛️ EXECUTION BETA UPDATE at 480,816 steps:
   action_execution_beta: 1.000 (w_exec=(1-β)w_prev + βw_raw)
   ⏹️ Early-stop transition reset: reason=action_execution_beta_update | grace_until=495,816 | best_ema_reset=yes

📚 EPISODE HORIZON UPDATE at 480,816 steps:
   Episode horizon set to full dataset
[CYCLE] Update 391/401 | Step 480,816/500,000 | Episode 480 | Time: 43195.9s
   📊 Metrics: Return=+21.96% | Sharpe=0.175 | DD=28.82% | Turnover=44.41%
   🎚️ Intra-Step TAPE: potential=0.3480 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1283 | critic_loss=4.3799 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.1899 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0234
   🧠 Objective Experts: aux_loss=-0.1639 | router_entropy=-0.0048 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.306 | risk=0.488 | discipline=0.206
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.0028 | ema=0.0982 | best_ema=0.1088 | no_improve=0 | grace_until=495,816

📚 EPISODE HORIZON UPDATE at 482,832 steps:
   Episode horizon set to full dataset
[CYCLE] Update 392/401 | Step 482,832/500,000 | Episode 481 | Time: 43335.4s
   📊 Metrics: Return=+9.16% | Sharpe=0.021 | DD=28.36% | Turnover=49.99%
   🎚️ Intra-Step TAPE: potential=0.5127 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1138 | critic_loss=11.0763 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=5.5381 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0235
   🧠 Objective Experts: aux_loss=-0.1495 | router_entropy=-0.0048 | diversity_loss=0.0125 | mask=[1, 1, 1] | router=return=0.313 | risk=0.483 | discipline=0.204
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1878 | ema=0.0696 | best_ema=0.1088 | no_improve=0 | grace_until=495,816
   🔬 Alpha Diversity: mean=2.38 | std=2.30 | range=[1.08, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.37 | MSFT=2.52 | CAT=2.40  BOT: NEE=1.40 | GLD=1.34 | KO=1.26
   🧬 FiLM: seq(dg=0.0142, db=0.0087, sat=0.0%) | latent(dg=0.0974, db=0.0581, sat=0.0%) | asset(dg=0.0059, db=0.0033, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=159 (32.0%), low_vol=189 (38.0%), medium_vol=149 (30.0%)
   🔒 Drawdown λ snapshot=3.322 (peak 3.322, dd 19.30% / trig 16.50%) | terminal=0.732 (peak 0.735) | TAPE=0.2095
   📈 Benchmark Relative: 1/N shaping=-0.005 (EW ret=0.00352) | SPY shaping=0.000 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 484,848 steps:
   Episode horizon set to full dataset
[CYCLE] Update 393/401 | Step 484,848/500,000 | Episode 482 | Time: 43475.1s
   📊 Metrics: Return=+37.72% | Sharpe=0.316 | DD=23.45% | Turnover=50.09%
   🎚️ Intra-Step TAPE: potential=0.7413 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.2084 | critic_loss=4.2333 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.1167 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0235
   🧠 Objective Experts: aux_loss=-0.2442 | router_entropy=-0.0047 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.334 | risk=0.463 | discipline=0.203
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.1866 | ema=0.0813 | best_ema=0.1088 | no_improve=0 | grace_until=495,816
   🔒 Drawdown λ snapshot=3.625 (peak 3.640, dd 12.80% / trig 16.50%) | terminal=0.000 (peak 3.721) | TAPE=0.2489
   📈 Benchmark Relative: 1/N shaping=-0.009 (EW ret=0.00352) | SPY shaping=-0.001 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 486,864 steps:
   Episode horizon set to full dataset
[CYCLE] Update 394/401 | Step 486,864/500,000 | Episode 484 | Time: 43614.9s
   📊 Metrics: Return=+40.04% | Sharpe=0.244 | DD=23.97% | Turnover=50.15%
   🎚️ Intra-Step TAPE: potential=0.2248 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1292 | critic_loss=5.2774 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.6387 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0241
   🧠 Objective Experts: aux_loss=-0.1657 | router_entropy=-0.0048 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.329 | risk=0.477 | discipline=0.194
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=0.1139 | ema=0.0846 | best_ema=0.1088 | no_improve=0 | grace_until=495,816
   🔬 Alpha Diversity: mean=2.40 | std=2.24 | range=[1.08, 10.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.67 | AMZN=2.91 | CAT=2.63  BOT: BRK-B=1.52 | NEE=1.31 | KO=1.27
   🧬 FiLM: seq(dg=0.0140, db=0.0085, sat=0.0%) | latent(dg=0.0987, db=0.0589, sat=0.0%) | asset(dg=0.0060, db=0.0033, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=160 (32.0%), low_vol=190 (38.0%), medium_vol=150 (30.0%)
   🔒 Drawdown λ snapshot=3.355 (peak 3.640, dd 7.07% / trig 16.50%) | terminal=0.000 (peak 0.044) | TAPE=0.2409
   📈 Benchmark Relative: 1/N shaping=-0.011 (EW ret=0.00352) | SPY shaping=-0.001 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 488,880 steps:
   Episode horizon set to full dataset
[CYCLE] Update 395/401 | Step 488,880/500,000 | Episode 485 | Time: 43754.6s
   📊 Metrics: Return=-3.12% | Sharpe=-0.071 | DD=35.58% | Turnover=49.39%
   🎚️ Intra-Step TAPE: potential=0.2625 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.2148 | critic_loss=4.6519 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.3260 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0232
   🧠 Objective Experts: aux_loss=-0.2500 | router_entropy=-0.0047 | diversity_loss=0.0124 | mask=[1, 1, 1] | router=return=0.291 | risk=0.532 | discipline=0.176
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.4489 | ema=0.0312 | best_ema=0.1088 | no_improve=0 | grace_until=495,816
   🔒 Drawdown λ snapshot=3.017 (peak 3.640, dd 4.86% / trig 16.50%) | terminal=3.778 (peak 5.000) | TAPE=0.2104
   📈 Benchmark Relative: 1/N shaping=-0.012 (EW ret=0.00352) | SPY shaping=-0.001 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 490,896 steps:
   Episode horizon set to full dataset
[CYCLE] Update 396/401 | Step 490,896/500,000 | Episode 489 | Time: 43893.9s
   📊 Metrics: Return=+27.66% | Sharpe=0.168 | DD=28.39% | Turnover=50.21%
   🎚️ Intra-Step TAPE: potential=0.2439 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0724 | critic_loss=3.9818 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.9909 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0228
   🧠 Objective Experts: aux_loss=-0.1075 | router_entropy=-0.0047 | diversity_loss=0.0126 | mask=[1, 1, 1] | router=return=0.314 | risk=0.479 | discipline=0.207
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.0435 | ema=0.0237 | best_ema=0.1088 | no_improve=0 | grace_until=495,816
   🔬 Alpha Diversity: mean=2.34 | std=2.37 | range=[1.08, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.69 | AMZN=2.55 | CAT=2.23  BOT: BRK-B=1.45 | NEE=1.37 | KO=1.32
   🧬 FiLM: seq(dg=0.0135, db=0.0083, sat=0.0%) | latent(dg=0.1034, db=0.0618, sat=0.0%) | asset(dg=0.0060, db=0.0033, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=161 (31.9%), low_vol=192 (38.0%), medium_vol=152 (30.1%)
   🔒 Drawdown λ snapshot=2.638 (peak 3.640, dd 3.21% / trig 16.50%) | terminal=0.479 (peak 0.495) | TAPE=0.2249
   📈 Benchmark Relative: 1/N shaping=-0.009 (EW ret=0.00352) | SPY shaping=-0.001 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 492,912 steps:
   Episode horizon set to full dataset
[CYCLE] Update 397/401 | Step 492,912/500,000 | Episode 489 | Time: 44033.3s
   📊 Metrics: Return=+43.10% | Sharpe=0.214 | DD=31.07% | Turnover=48.81%
   🎚️ Intra-Step TAPE: potential=0.2324 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1135 | critic_loss=4.8036 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.4018 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0237
   🧠 Objective Experts: aux_loss=-0.1495 | router_entropy=-0.0048 | diversity_loss=0.0127 | mask=[1, 1, 1] | router=return=0.309 | risk=0.484 | discipline=0.206
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.0503 | ema=0.0163 | best_ema=0.1088 | no_improve=0 | grace_until=495,816

📚 EPISODE HORIZON UPDATE at 494,928 steps:
   Episode horizon set to full dataset
[CYCLE] Update 398/401 | Step 494,928/500,000 | Episode 491 | Time: 44173.0s
   📊 Metrics: Return=+10.33% | Sharpe=0.014 | DD=25.95% | Turnover=50.55%
   🎚️ Intra-Step TAPE: potential=0.2064 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.0927 | critic_loss=5.2986 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.6493 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0243
   🧠 Objective Experts: aux_loss=-0.1296 | router_entropy=-0.0049 | diversity_loss=0.0129 | mask=[1, 1, 1] | router=return=0.316 | risk=0.445 | discipline=0.238
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1421 | ema=0.0005 | best_ema=0.1088 | no_improve=0 | grace_until=495,816
   🔬 Alpha Diversity: mean=2.38 | std=2.22 | range=[1.07, 10.54] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=3.84 | AMZN=3.23 | CAT=2.33  BOT: NEE=1.40 | GLD=1.31 | KO=1.29
   🧬 FiLM: seq(dg=0.0153, db=0.0092, sat=0.0%) | latent(dg=0.1024, db=0.0613, sat=0.0%) | asset(dg=0.0062, db=0.0034, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=162 (32.0%), low_vol=192 (37.9%), medium_vol=153 (30.2%)
   🔒 Drawdown λ snapshot=1.959 (peak 3.640, dd 16.16% / trig 16.50%) | terminal=0.710 (peak 3.163) | TAPE=0.2160
   📈 Benchmark Relative: 1/N shaping=-0.011 (EW ret=0.00352) | SPY shaping=-0.001 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 496,944 steps:
   Episode horizon set to full dataset
[CYCLE] Update 399/401 | Step 496,944/500,000 | Episode 493 | Time: 44312.7s
   📊 Metrics: Return=+46.10% | Sharpe=0.179 | DD=33.61% | Turnover=50.27%
   🎚️ Intra-Step TAPE: potential=0.6731 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0096 | critic_loss=4.6360 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.3180 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.0273 | router_entropy=-0.0050 | diversity_loss=0.0131 | mask=[1, 1, 1] | router=return=0.364 | risk=0.376 | discipline=0.260
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1585 | ema=-0.0154 | best_ema=0.1088 | no_improve=1
   🔒 Drawdown λ snapshot=2.279 (peak 3.640, dd 13.99% / trig 16.50%) | terminal=4.394 (peak 5.000) | TAPE=0.2242
   📈 Benchmark Relative: 1/N shaping=-0.003 (EW ret=0.00352) | SPY shaping=0.001 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 498,960 steps:
   Episode horizon set to full dataset
[CYCLE] Update 400/401 | Step 498,960/500,000 | Episode 494 | Time: 44452.1s
   📊 Metrics: Return=+3.23% | Sharpe=-0.020 | DD=31.24% | Turnover=50.25%
   🎚️ Intra-Step TAPE: potential=0.6253 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1310 | critic_loss=5.2534 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.6267 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0242
   🧠 Objective Experts: aux_loss=-0.1679 | router_entropy=-0.0051 | diversity_loss=0.0132 | mask=[1, 1, 1] | router=return=0.365 | risk=0.380 | discipline=0.255
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.3001 | ema=-0.0439 | best_ema=0.1088 | no_improve=2
   🔬 Alpha Diversity: mean=2.43 | std=2.20 | range=[1.08, 10.55] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=4.24 | CAT=3.55 | AMZN=3.24  BOT: BRK-B=1.34 | NEE=1.31 | KO=1.25
   🧬 FiLM: seq(dg=0.0172, db=0.0100, sat=0.0%) | latent(dg=0.0991, db=0.0592, sat=0.0%) | asset(dg=0.0061, db=0.0034, sat=0.0%)
   🧭 Regime Start Dist (train resets): high_vol=163 (32.0%), low_vol=192 (37.6%), medium_vol=155 (30.4%)
   🔒 Drawdown λ snapshot=2.383 (peak 3.640, dd 13.62% / trig 16.50%) | terminal=3.893 (peak 5.000) | TAPE=0.2093
   📈 Benchmark Relative: 1/N shaping=-0.005 (EW ret=0.00352) | SPY shaping=0.000 (SPY ret=0.00243)

📚 EPISODE HORIZON UPDATE at 500,000 steps:
   Episode horizon set to full dataset
[CYCLE] Update 401/401 | Step 500,000/500,000 | Episode 496 | Time: 44545.8s
   📊 Metrics: Return=+41.10% | Sharpe=0.183 | DD=31.49% | Turnover=50.89%
   🎚️ Intra-Step TAPE: potential=0.4283 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=-0.1019 | critic_loss=4.4204 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=2.2102 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0000 | dispersion_loss=0.0246
   🧠 Objective Experts: aux_loss=-0.1393 | router_entropy=-0.0051 | diversity_loss=0.0133 | mask=[1, 1, 1] | router=return=0.384 | risk=0.357 | discipline=0.259
   ⚙️ Optimizer: actor_lr=0.000010 | critic_lr=0.000100 | target_kl=0.0000 | rollout=2016 | batch_size=672 | gamma=0.9980 | gae_lambda=0.9700
   ⏹️ Early-stop monitor: score=-0.1086 | ema=-0.0503 | best_ema=0.1088 | no_improve=3
   🔒 Drawdown λ snapshot=1.658 (peak 1.745, dd 2.08% / trig 16.50%) | terminal=3.214 (peak 4.667) | TAPE=0.2232
   📈 Benchmark Relative: 1/N shaping=-0.007 (EW ret=0.00352) | SPY shaping=-0.000 (SPY ret=0.00243)

[OK] THREE-COMPONENT TAPE v3 training completed!
   Total episodes: 496
   Total timesteps: 500,000
   Training time: 44545.79s (742.43min)
📊 Training summary saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/logs/Exp6_TCN_FUSION_Enhanced_TAPE_training_20260326_065026_summary.csv
💾 Final models saved: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00496_shp0p183_actor.weights.h5, /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00496_shp0p183_critic.weights.h5
🎯 Default selected checkpoint: final high-watermark-style checkpoint
[OK] Training complete
checkpoint_prefix: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints_run20/exp6_tape_hw_ep00496_shp0p183
