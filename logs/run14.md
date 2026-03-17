[START] Starting training
Architecture: MLP
max_total_timesteps: 300000
num_parallel_envs: 4

================================================================================
EXPERIMENT 6: MLP Enhanced + TAPE Three-Component
================================================================================
Architecture: MLP
Results root: /content/tcn_tape_vectorized_version_clean/results
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
   📈 Benchmark Shaping (1/N): ENABLED | scalar=8.0 | mode=signed_clipped | clip=0.0200
   📈 Benchmark Shaping (SPY): ENABLED | scalar=5.0 | mode=signed_clipped | clip=0.0200
   🔐 Lagrangian CVaR: ENABLED | threshold=-0.035 | lr=0.002 | lambda_max=2.0 | penalty_scale=0.75
   Alpha Regularization: hhi_coef=0.005 | dispersion_coef=0.02 | target_std=0.1
   Risk Aux: sharpe_coef=0.0 | mvo_coef=0.0 | cvar_coef=0.0
   🧪 Aux Per-Asset Return Head: ENABLED | coef=0.35
   🔒 Dirichlet Alpha Cap: 16.0
   🔒 Drawdown dual controller (requested): target=27.00%, tolerance=-2.00% (trigger boundary ≈ 25.00%), lr=0.100, λ_init=0.05, λ_floor=0.00, λ_max=5.00, penalty_coef=0.50
   📐 Position constraints: max_single_asset=35%, min_cash=2%
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

🤖 Creating MLP agent with Dirichlet distribution for Exp 6...
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
   [BRAIN] Recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DNA] State augmentation: enabled=False
   [DOWN] Distributional critic: enabled=False | num_quantiles=1
   🎛️ Dirichlet controls: activation=exp_tanh | temperature=0.8 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Dual-head consistency coef: 0.0
   🧩 Mixture Regularizers: balance_coef=0.005 | separation_coef=0.06 | gate_entropy_coef=0.001 | component_dispersion_coef=0.04 | target_std=0.3 | min_distance=0.18
   PPO update: epochs=3, batch_size=252, target_kl=0.0000, entropy_coef=0.0030
   [DOWN] PPO gamma schedule: 0.9900@0 => 0.9950@100,000 => 0.9980@220,000
   [DOWN] PPO GAE-λ schedule: 0.9200@0 => 0.9500@100,000 => 0.9700@220,000
   🎯 Entropy coef schedule: 0.0030@0 => 0.0030@100,000 => 0.0025@200,000 => 0.0015@280,000
   🧪 Aux-return coef schedule: 0.3500@0 => 0.3000@100,000 => 0.2500@220,000
   🌡️ Temperature schedule: 0.8000@0 => 0.7000@100,000 => 0.6000@220,000
   📐 PPO rollout schedule: 1008@0 => 1512@100,000 => 2016@220,000
   🧺 PPO batch-size schedule: 252@0 => 336@100,000 => 504@220,000
📊 Training metrics will stream to /content/tcn_tape_vectorized_version_clean/results/logs/Exp6_MLP_Enhanced_TAPE_training_20260317_154729_episodes.csv
🧪 Step diagnostics will stream to /content/tcn_tape_vectorized_version_clean/results/logs/Exp6_MLP_Enhanced_TAPE_training_20260317_154729_step_diagnostics.csv

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
   🏆 Deterministic-validation checkpoints: enabled (every 5 episodes | mode=mode | min_sharpe=0.50 | min_delta=0.000 | alpha_diag=True | horizon=scheduled (0@756 => 100,000@1008 => 250,000@1500 => 400,000@full))
      ↳ Multi-horizon selector: enabled (252:0.35, 504:0.30, 756:0.20, 1008:0.15) | dd_penalty_coef=0.250
      ↳ Stochastic sanity gate: enabled (runs=3, horizon=252, min_mean_sharpe=0.00, max_std=1.50)
      ↳ SPY outperformance gate: enabled (required>0.00% over the same validation horizon)
      ↳ Equal-weight gate: enabled (required>0.00% over the same validation horizon)
   🧷 Legacy checkpoint routes: disabled (high-watermark/step/periodic/tape/rare)
   [OK] Checkpoint selector default: deterministic validation multi-horizon composite score
   💾 High-watermark checkpoints: disabled
   ⏹️ Training early-stop: enabled (warmup=100,000 steps, patience=25 updates, min_delta=0.010, hard_dd=60.0% x 12)
[RCPT] Active feature manifest saved: /content/tcn_tape_vectorized_version_clean/results/logs/Exp6_MLP_Enhanced_TAPE_training_20260317_154729_active_feature_manifest.json
[RCPT] Training metadata saved: /content/tcn_tape_vectorized_version_clean/results/logs/Exp6_MLP_Enhanced_TAPE_training_20260317_154729_metadata.json
[CYCLE] Update 1/219 | Step 1,008/300,000 | Episode 0 | Time: 57.3s
   📊 Metrics: Return=+15.20% | Sharpe=1.596 | DD=3.78% | Turnover=33.72%
   🎚️ Intra-Step TAPE: potential=0.7308 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1577 | critic_loss=2.1800 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=1.0900 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0013
   🧩 Mixture Head: gate_entropy=1.0448 | balance_loss=0.0001 | separation_loss=0.0065 | component_dispersion_loss=0.0096
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5964 | ema=1.5964 | best_ema=1.5964 | no_improve=0
[CYCLE] Update 2/219 | Step 2,016/300,000 | Episode 0 | Time: 104.4s
   📊 Metrics: Return=+35.12% | Sharpe=1.375 | DD=8.56% | Turnover=31.80%
   🎚️ Intra-Step TAPE: potential=0.2744 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1127 | critic_loss=0.7957 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3979 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0826 | balance_loss=0.0000 | separation_loss=0.0067 | component_dispersion_loss=0.0097
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3747 | ema=1.5742 | best_ema=1.5742 | no_improve=0
   🔬 Alpha Diversity: mean=9.80 | std=3.36 | range=[0.67, 16.00] | cap_hit=4.1%
   🏷️ Alpha Per-Asset  TOP: MSFT=12.21 | NEE=11.02 | JNJ=10.75  BOT: GLD=9.79 | NVDA=7.44 | XOM=7.29
   🎛️ Mixture Usage: C0=38.0% | C1=33.4% | C2=28.6%
   🧭 Regime Start Dist (train resets): high_vol=2 (50.0%), low_vol=1 (25.0%), medium_vol=1 (25.0%)
[CYCLE] Update 3/219 | Step 3,024/300,000 | Episode 4 | Time: 151.5s
   📊 Metrics: Return=+21.65% | Sharpe=0.460 | DD=12.73% | Turnover=31.54%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1068 | critic_loss=0.7737 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.3868 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0868 | balance_loss=0.0000 | separation_loss=0.0069 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4603 | ema=1.4628 | best_ema=1.4628 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.050) | TAPE=0.3016
   📈 Benchmark Relative: 1/N shaping=0.013 (EW ret=-0.01358) | SPY shaping=0.010 (SPY ret=-0.01396)
[CYCLE] Update 4/219 | Step 4,032/300,000 | Episode 4 | Time: 198.4s
   📊 Metrics: Return=+22.87% | Sharpe=2.734 | DD=2.61% | Turnover=26.89%
   🎚️ Intra-Step TAPE: potential=0.7529 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1028 | critic_loss=0.2753 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.1376 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0860 | balance_loss=0.0000 | separation_loss=0.0070 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.7340 | ema=1.5899 | best_ema=1.5899 | no_improve=0
   🔬 Alpha Diversity: mean=8.76 | std=2.78 | range=[1.51, 16.00] | cap_hit=0.8%
   🏷️ Alpha Per-Asset  TOP: MSFT=9.96 | NEE=9.82 | PG=9.77  BOT: XOM=8.28 | NVDA=7.22 | JPM=7.20
   🎛️ Mixture Usage: C0=37.1% | C1=34.4% | C2=28.5%
   🧭 Regime Start Dist (train resets): high_vol=2 (25.0%), low_vol=4 (50.0%), medium_vol=2 (25.0%)
[CYCLE] Update 5/219 | Step 5,040/300,000 | Episode 4 | Time: 245.6s
   📊 Metrics: Return=+12.77% | Sharpe=0.369 | DD=21.07% | Turnover=27.48%
   🎚️ Intra-Step TAPE: potential=0.2304 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.1010 | critic_loss=0.5910 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2955 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0880 | balance_loss=0.0000 | separation_loss=0.0070 | component_dispersion_loss=0.0098
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3693 | ema=1.4679 | best_ema=1.4679 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.191 | Return=+14.67% | DD=25.09%
         Multi-horizon: score=-0.295 | details=252:-0.639/25.1%, 504:-0.197/25.1%, 756:0.112/25.1%, 1008:0.191/25.1%
         SPY relative: spy_return=+41.94% | outperformance=-27.26%
         Equal-weight relative: ew_return=+93.18% | outperformance=-78.51%
[CYCLE] Update 6/219 | Step 6,048/300,000 | Episode 8 | Time: 599.9s
   📊 Metrics: Return=+24.16% | Sharpe=0.503 | DD=12.97% | Turnover=27.26%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0999 | critic_loss=0.4785 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.2392 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0868 | balance_loss=0.0000 | separation_loss=0.0071 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5033 | ema=1.3714 | best_ema=1.3714 | no_improve=0
   🔬 Alpha Diversity: mean=7.79 | std=2.44 | range=[1.18, 15.93] | cap_hit=0.2%
   🏷️ Alpha Per-Asset  TOP: NEE=8.77 | CAT=8.65 | JNJ=8.36  BOT: PG=7.62 | JPM=6.90 | NVDA=6.79
   🎛️ Mixture Usage: C0=36.4% | C1=31.2% | C2=32.4%
   🧭 Regime Start Dist (train resets): high_vol=4 (33.3%), low_vol=4 (33.3%), medium_vol=4 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3110
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=-0.00445) | SPY shaping=0.002 (SPY ret=-0.00511)
[CYCLE] Update 7/219 | Step 7,056/300,000 | Episode 8 | Time: 646.9s
   📊 Metrics: Return=+8.54% | Sharpe=0.535 | DD=8.91% | Turnover=26.09%
   🎚️ Intra-Step TAPE: potential=0.2867 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0989 | critic_loss=0.1928 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0964 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0875 | balance_loss=0.0000 | separation_loss=0.0071 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5351 | ema=1.2878 | best_ema=1.2878 | no_improve=0
[CYCLE] Update 8/219 | Step 8,064/300,000 | Episode 8 | Time: 694.2s
   📊 Metrics: Return=+31.09% | Sharpe=0.978 | DD=9.24% | Turnover=25.65%
   🎚️ Intra-Step TAPE: potential=0.3318 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0975 | critic_loss=0.1980 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0990 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0867 | balance_loss=0.0000 | separation_loss=0.0071 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9785 | ema=1.2569 | best_ema=1.2569 | no_improve=0
   🔬 Alpha Diversity: mean=7.23 | std=2.08 | range=[1.46, 15.97] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: NEE=8.30 | GLD=8.16 | JNJ=7.78  BOT: CAT=6.91 | XOM=6.79 | MSFT=6.73
   🎛️ Mixture Usage: C0=35.9% | C1=31.4% | C2=32.6%
   🧭 Regime Start Dist (train resets): high_vol=4 (33.3%), low_vol=4 (33.3%), medium_vol=4 (33.3%)
      🧪 Deterministic validation: Sharpe=-0.252 | Return=-10.93% | DD=26.46%
         Multi-horizon: score=-0.744 | details=252:-1.092/26.5%, 504:-0.596/26.5%, 756:-0.392/26.5%, 1008:-0.252/26.5%
         SPY relative: spy_return=+41.94% | outperformance=-52.87%
         Equal-weight relative: ew_return=+93.18% | outperformance=-104.11%
[CYCLE] Update 9/219 | Step 9,072/300,000 | Episode 12 | Time: 1050.7s
   📊 Metrics: Return=+39.72% | Sharpe=0.823 | DD=19.80% | Turnover=25.37%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0997 | critic_loss=0.2940 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.1470 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0858 | balance_loss=0.0000 | separation_loss=0.0072 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8232 | ema=1.2135 | best_ema=1.2135 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4085
   📈 Benchmark Relative: 1/N shaping=-0.002 (EW ret=0.00396) | SPY shaping=-0.002 (SPY ret=0.00410)
[CYCLE] Update 10/219 | Step 10,080/300,000 | Episode 12 | Time: 1097.7s
   📊 Metrics: Return=+6.40% | Sharpe=0.424 | DD=10.61% | Turnover=25.23%
   🎚️ Intra-Step TAPE: potential=0.2503 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0975 | critic_loss=0.1400 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0700 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0892 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4242 | ema=1.1346 | best_ema=1.1346 | no_improve=0
   🔬 Alpha Diversity: mean=7.09 | std=1.86 | range=[1.87, 15.86] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: NEE=7.52 | XOM=7.38 | CAT=7.36  BOT: NVDA=7.03 | AMZN=6.89 | JPM=6.62
   🎛️ Mixture Usage: C0=35.1% | C1=29.9% | C2=35.0%
   🧭 Regime Start Dist (train resets): high_vol=5 (31.2%), low_vol=4 (25.0%), medium_vol=7 (43.8%)
[CYCLE] Update 11/219 | Step 11,088/300,000 | Episode 12 | Time: 1144.9s
   📊 Metrics: Return=+23.38% | Sharpe=0.852 | DD=10.61% | Turnover=25.29%
   🎚️ Intra-Step TAPE: potential=0.6536 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0963 | critic_loss=0.1296 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0648 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0892 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8519 | ema=1.1063 | best_ema=1.1063 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.101 | Return=+8.86% | DD=23.78%
         Multi-horizon: score=-0.424 | details=252:-0.893/23.8%, 504:-0.216/23.8%, 756:-0.011/23.8%, 1008:0.101/23.8%
         SPY relative: spy_return=+41.94% | outperformance=-33.08%
         Equal-weight relative: ew_return=+93.18% | outperformance=-84.32%
[CYCLE] Update 12/219 | Step 12,096/300,000 | Episode 16 | Time: 1500.8s
   📊 Metrics: Return=+52.23% | Sharpe=1.144 | DD=10.28% | Turnover=25.29%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0968 | critic_loss=0.1889 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0944 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0882 | balance_loss=0.0000 | separation_loss=0.0074 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.1439 | ema=1.1101 | best_ema=1.1101 | no_improve=0
   🔬 Alpha Diversity: mean=6.90 | std=1.81 | range=[1.42, 15.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.00 | XOM=7.39 | CAT=7.20  BOT: AMZN=6.59 | MSFT=6.53 | PG=6.26
   🎛️ Mixture Usage: C0=31.2% | C1=30.6% | C2=38.2%
   🧭 Regime Start Dist (train resets): high_vol=7 (35.0%), low_vol=5 (25.0%), medium_vol=8 (40.0%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5369
   📈 Benchmark Relative: 1/N shaping=-0.010 (EW ret=-0.00707) | SPY shaping=-0.013 (SPY ret=-0.00562)
[CYCLE] Update 13/219 | Step 13,104/300,000 | Episode 16 | Time: 1547.8s
   📊 Metrics: Return=+13.19% | Sharpe=0.921 | DD=9.52% | Turnover=24.06%
   🎚️ Intra-Step TAPE: potential=0.2436 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0954 | critic_loss=0.1694 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0847 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0858 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9214 | ema=1.0912 | best_ema=1.0912 | no_improve=0
[CYCLE] Update 14/219 | Step 14,112/300,000 | Episode 16 | Time: 1595.0s
   📊 Metrics: Return=+43.58% | Sharpe=1.649 | DD=9.52% | Turnover=24.00%
   🎚️ Intra-Step TAPE: potential=0.7544 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0969 | critic_loss=0.1920 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0960 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0890 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6489 | ema=1.1470 | best_ema=1.1470 | no_improve=0
   🔬 Alpha Diversity: mean=6.98 | std=1.87 | range=[1.70, 15.29] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.26 | CAT=7.74 | JNJ=7.55  BOT: NVDA=6.56 | AMZN=6.26 | MSFT=6.18
   🎛️ Mixture Usage: C0=32.1% | C1=30.5% | C2=37.4%
   🧭 Regime Start Dist (train resets): high_vol=7 (35.0%), low_vol=5 (25.0%), medium_vol=8 (40.0%)
      🧪 Deterministic validation: Sharpe=0.105 | Return=+9.19% | DD=28.80%
         Multi-horizon: score=-0.618 | details=252:-1.285/28.8%, 504:-0.339/28.8%, 756:-0.050/28.8%, 1008:0.105/28.8%
         SPY relative: spy_return=+41.94% | outperformance=-32.74%
         Equal-weight relative: ew_return=+93.18% | outperformance=-83.99%
[CYCLE] Update 15/219 | Step 15,120/300,000 | Episode 20 | Time: 1953.8s
   📊 Metrics: Return=+69.41% | Sharpe=1.441 | DD=9.07% | Turnover=24.38%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0992 | critic_loss=0.1898 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0949 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0881 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.4414 | ema=1.1764 | best_ema=1.1764 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5949
   📈 Benchmark Relative: 1/N shaping=0.005 (EW ret=0.00233) | SPY shaping=0.020 (SPY ret=-0.00109)
[CYCLE] Update 16/219 | Step 16,128/300,000 | Episode 20 | Time: 2001.2s
   📊 Metrics: Return=+12.99% | Sharpe=1.057 | DD=5.15% | Turnover=24.95%
   🎚️ Intra-Step TAPE: potential=0.5436 | delta_reward=-0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0966 | critic_loss=0.1149 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0575 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0875 | balance_loss=0.0000 | separation_loss=0.0074 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0571 | ema=1.1645 | best_ema=1.1645 | no_improve=0
   🔬 Alpha Diversity: mean=6.85 | std=1.97 | range=[1.28, 15.81] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: NEE=8.42 | JNJ=7.65 | CAT=7.61  BOT: JPM=6.07 | NVDA=6.02 | MSFT=5.85
   🎛️ Mixture Usage: C0=31.5% | C1=30.8% | C2=37.7%
   🧭 Regime Start Dist (train resets): high_vol=8 (33.3%), low_vol=8 (33.3%), medium_vol=8 (33.3%)
[CYCLE] Update 17/219 | Step 17,136/300,000 | Episode 20 | Time: 2048.6s
   📊 Metrics: Return=+15.07% | Sharpe=0.542 | DD=6.78% | Turnover=24.35%
   🎚️ Intra-Step TAPE: potential=0.2427 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0969 | critic_loss=0.1035 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0517 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0829 | balance_loss=0.0000 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5424 | ema=1.1023 | best_ema=1.1023 | no_improve=0
[CYCLE] Update 18/219 | Step 18,144/300,000 | Episode 24 | Time: 2095.6s
   📊 Metrics: Return=+40.46% | Sharpe=0.879 | DD=11.92% | Turnover=23.30%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0970 | critic_loss=0.0813 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0407 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0828 | balance_loss=0.0000 | separation_loss=0.0074 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8787 | ema=1.0799 | best_ema=1.0799 | no_improve=0
   🔬 Alpha Diversity: mean=6.81 | std=1.87 | range=[1.03, 15.51] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.35 | JNJ=7.77 | CAT=7.58  BOT: NVDA=6.19 | PG=6.18 | MSFT=5.76
   🎛️ Mixture Usage: C0=30.0% | C1=30.6% | C2=39.5%
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=10 (35.7%), medium_vol=8 (28.6%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4747
   📈 Benchmark Relative: 1/N shaping=-0.014 (EW ret=-0.00150) | SPY shaping=-0.015 (SPY ret=-0.00024)
[CYCLE] Update 19/219 | Step 19,152/300,000 | Episode 24 | Time: 2143.1s
   📊 Metrics: Return=-2.83% | Sharpe=-0.294 | DD=10.90% | Turnover=25.05%
   🎚️ Intra-Step TAPE: potential=0.2462 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0949 | critic_loss=0.0813 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0406 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0832 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.2940 | ema=0.9425 | best_ema=0.9425 | no_improve=0
[CYCLE] Update 20/219 | Step 20,160/300,000 | Episode 24 | Time: 2190.4s
   📊 Metrics: Return=+29.41% | Sharpe=0.948 | DD=10.90% | Turnover=24.14%
   🎚️ Intra-Step TAPE: potential=0.7196 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0964 | critic_loss=0.0915 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0457 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0820 | balance_loss=0.0000 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9477 | ema=0.9430 | best_ema=0.9430 | no_improve=0
   🔬 Alpha Diversity: mean=6.74 | std=1.86 | range=[1.72, 15.29] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.36 | JNJ=7.64 | CAT=7.34  BOT: XOM=6.15 | MSFT=5.75 | PG=5.50
   🎛️ Mixture Usage: C0=33.2% | C1=27.3% | C2=39.5%
   🧭 Regime Start Dist (train resets): high_vol=10 (35.7%), low_vol=10 (35.7%), medium_vol=8 (28.6%)
      🧪 Deterministic validation: Sharpe=0.522 | Return=+39.40% | DD=25.54%
         Multi-horizon: score=-0.260 | details=252:-0.898/25.5%, 504:-0.144/25.5%, 756:0.416/25.5%, 1008:0.522/25.5%
         SPY relative: spy_return=+41.94% | outperformance=-2.54%
         Equal-weight relative: ew_return=+93.18% | outperformance=-53.78%
         [WARN] SPY gate rejected checkpoint (outperformance=-2.54%, required>0.00%).
[CYCLE] Update 21/219 | Step 21,168/300,000 | Episode 28 | Time: 2546.8s
   📊 Metrics: Return=+47.08% | Sharpe=1.003 | DD=11.34% | Turnover=23.41%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0959 | critic_loss=0.1637 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0818 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0793 | balance_loss=0.0000 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0027 | ema=0.9490 | best_ema=0.9490 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5261
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=0.00185) | SPY shaping=-0.001 (SPY ret=0.00221)
[CYCLE] Update 22/219 | Step 22,176/300,000 | Episode 28 | Time: 2594.1s
   📊 Metrics: Return=+3.61% | Sharpe=0.195 | DD=10.62% | Turnover=23.84%
   🎚️ Intra-Step TAPE: potential=0.5736 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0962 | critic_loss=0.0872 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0436 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0842 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1955 | ema=0.8736 | best_ema=0.8736 | no_improve=0
   🔬 Alpha Diversity: mean=6.88 | std=2.04 | range=[1.58, 15.08] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.89 | JNJ=7.74 | CAT=7.62  BOT: NVDA=6.13 | PG=6.03 | MSFT=5.64
   🎛️ Mixture Usage: C0=35.7% | C1=28.5% | C2=35.8%
   🧭 Regime Start Dist (train resets): high_vol=11 (34.4%), low_vol=12 (37.5%), medium_vol=9 (28.1%)
[CYCLE] Update 23/219 | Step 23,184/300,000 | Episode 28 | Time: 2641.2s
   📊 Metrics: Return=+8.59% | Sharpe=0.255 | DD=10.62% | Turnover=24.64%
   🎚️ Intra-Step TAPE: potential=0.2613 | delta_reward=-0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0968 | critic_loss=0.0569 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0284 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0811 | balance_loss=0.0000 | separation_loss=0.0074 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2547 | ema=0.8118 | best_ema=0.8118 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.395 | Return=+30.13% | DD=25.54%
         Multi-horizon: score=-0.310 | details=252:-0.815/25.5%, 504:-0.254/25.5%, 756:0.280/25.5%, 1008:0.395/25.5%
         SPY relative: spy_return=+41.94% | outperformance=-11.81%
         Equal-weight relative: ew_return=+93.18% | outperformance=-63.05%
[CYCLE] Update 24/219 | Step 24,192/300,000 | Episode 32 | Time: 2996.8s
   📊 Metrics: Return=+38.90% | Sharpe=0.811 | DD=11.50% | Turnover=24.26%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0938 | critic_loss=0.0807 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0403 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0774 | balance_loss=0.0000 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8114 | ema=0.8117 | best_ema=0.8117 | no_improve=0
   🔬 Alpha Diversity: mean=6.69 | std=1.74 | range=[0.63, 15.35] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.14 | NVDA=6.95 | AMZN=6.94  BOT: JNJ=6.08 | MSFT=5.90 | PG=5.74
   🎛️ Mixture Usage: C0=31.4% | C1=27.9% | C2=40.7%
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=12 (33.3%), medium_vol=12 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4428
   📈 Benchmark Relative: 1/N shaping=-0.023 (EW ret=0.00446) | SPY shaping=-0.013 (SPY ret=0.00416)
[CYCLE] Update 25/219 | Step 25,200/300,000 | Episode 32 | Time: 3044.1s
   📊 Metrics: Return=+10.65% | Sharpe=0.884 | DD=4.19% | Turnover=22.77%
   🎚️ Intra-Step TAPE: potential=0.5916 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0915 | critic_loss=0.0666 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0333 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0835 | balance_loss=0.0000 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8837 | ema=0.8189 | best_ema=0.8189 | no_improve=0
[CYCLE] Update 26/219 | Step 26,208/300,000 | Episode 32 | Time: 3091.5s
   📊 Metrics: Return=+12.23% | Sharpe=0.427 | DD=8.07% | Turnover=23.25%
   🎚️ Intra-Step TAPE: potential=0.5693 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0956 | critic_loss=0.0971 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0485 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0839 | balance_loss=0.0000 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4273 | ema=0.7798 | best_ema=0.7798 | no_improve=0
   🔬 Alpha Diversity: mean=6.63 | std=1.73 | range=[1.32, 15.95] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=7.91 | CAT=7.36 | XOM=7.08  BOT: JPM=6.17 | MSFT=6.17 | PG=5.89
   🎛️ Mixture Usage: C0=27.7% | C1=33.5% | C2=38.8%
   🧭 Regime Start Dist (train resets): high_vol=12 (33.3%), low_vol=12 (33.3%), medium_vol=12 (33.3%)
      🧪 Deterministic validation: Sharpe=0.307 | Return=+22.91% | DD=22.17%
         Multi-horizon: score=-0.136 | details=252:-0.565/22.2%, 504:-0.024/22.2%, 756:0.391/22.2%, 1008:0.307/22.2%
         SPY relative: spy_return=+41.94% | outperformance=-19.02%
         Equal-weight relative: ew_return=+93.18% | outperformance=-70.27%
[CYCLE] Update 27/219 | Step 27,216/300,000 | Episode 36 | Time: 3447.3s
   📊 Metrics: Return=+23.42% | Sharpe=0.528 | DD=8.20% | Turnover=23.37%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0960 | critic_loss=0.0663 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0332 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0825 | balance_loss=0.0000 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5275 | ema=0.7545 | best_ema=0.7545 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3209
   📈 Benchmark Relative: 1/N shaping=0.009 (EW ret=0.00246) | SPY shaping=0.002 (SPY ret=0.00330)
[CYCLE] Update 28/219 | Step 28,224/300,000 | Episode 36 | Time: 3494.9s
   📊 Metrics: Return=+23.96% | Sharpe=2.035 | DD=8.08% | Turnover=23.50%
   🎚️ Intra-Step TAPE: potential=0.4830 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0942 | critic_loss=0.0565 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0283 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0840 | balance_loss=0.0000 | separation_loss=0.0072 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.0348 | ema=0.8826 | best_ema=0.8826 | no_improve=0
   🔬 Alpha Diversity: mean=6.66 | std=1.93 | range=[1.25, 15.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.25 | CAT=7.52 | MSFT=7.01  BOT: GLD=6.04 | JNJ=6.03 | PG=5.72
   🎛️ Mixture Usage: C0=30.9% | C1=30.7% | C2=38.5%
   🧭 Regime Start Dist (train resets): high_vol=15 (37.5%), low_vol=13 (32.5%), medium_vol=12 (30.0%)
[CYCLE] Update 29/219 | Step 29,232/300,000 | Episode 36 | Time: 3542.2s
   📊 Metrics: Return=+19.25% | Sharpe=0.563 | DD=20.09% | Turnover=25.14%
   🎚️ Intra-Step TAPE: potential=0.3780 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0955 | critic_loss=0.0675 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0337 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0755 | balance_loss=0.0000 | separation_loss=0.0071 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5627 | ema=0.8506 | best_ema=0.8506 | no_improve=0
   🔐 Lagrangian CVaR: λ=0.0000 | penalty=-0.0000 | rolling_cvar=-0.03635
      🧪 Deterministic validation: Sharpe=0.258 | Return=+19.42% | DD=27.54%
         Multi-horizon: score=-0.295 | details=252:-0.855/27.5%, 504:-0.126/27.5%, 756:0.363/27.5%, 1008:0.258/27.5%
         SPY relative: spy_return=+41.94% | outperformance=-22.51%
         Equal-weight relative: ew_return=+93.18% | outperformance=-73.76%
[CYCLE] Update 30/219 | Step 30,240/300,000 | Episode 40 | Time: 3899.7s
   📊 Metrics: Return=+71.88% | Sharpe=0.909 | DD=28.46% | Turnover=25.59%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0964 | critic_loss=0.1740 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0870 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0798 | balance_loss=0.0000 | separation_loss=0.0072 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9088 | ema=0.8564 | best_ema=0.8564 | no_improve=0
   🔬 Alpha Diversity: mean=6.53 | std=1.79 | range=[0.78, 15.81] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=7.53 | CAT=7.09 | NVDA=6.83  BOT: XOM=6.28 | JNJ=6.10 | PG=5.62
   🎛️ Mixture Usage: C0=31.5% | C1=30.1% | C2=38.4%
   🧭 Regime Start Dist (train resets): high_vol=15 (34.1%), low_vol=14 (31.8%), medium_vol=15 (34.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.005) | TAPE=0.4480
   📈 Benchmark Relative: 1/N shaping=0.015 (EW ret=-0.00212) | SPY shaping=0.008 (SPY ret=-0.00179)
[CYCLE] Update 31/219 | Step 31,248/300,000 | Episode 40 | Time: 3946.7s
   📊 Metrics: Return=+4.96% | Sharpe=0.343 | DD=9.05% | Turnover=27.23%
   🎚️ Intra-Step TAPE: potential=0.2499 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0950 | critic_loss=0.0649 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0325 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0812 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3432 | ema=0.8051 | best_ema=0.8051 | no_improve=0
[CYCLE] Update 32/219 | Step 32,256/300,000 | Episode 40 | Time: 3994.2s
   📊 Metrics: Return=+7.33% | Sharpe=0.191 | DD=12.89% | Turnover=25.27%
   🎚️ Intra-Step TAPE: potential=0.3667 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0931 | critic_loss=0.0775 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0388 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0811 | balance_loss=0.0000 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1912 | ema=0.7437 | best_ema=0.7437 | no_improve=0
   🔬 Alpha Diversity: mean=6.42 | std=1.45 | range=[1.50, 14.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=7.23 | NVDA=7.06 | CAT=6.79  BOT: MSFT=6.11 | PG=5.71 | JNJ=5.63
   🎛️ Mixture Usage: C0=26.4% | C1=32.7% | C2=40.9%
   🧭 Regime Start Dist (train resets): high_vol=15 (34.1%), low_vol=14 (31.8%), medium_vol=15 (34.1%)
[CYCLE] Update 33/219 | Step 33,264/300,000 | Episode 44 | Time: 4041.5s
   📊 Metrics: Return=+60.05% | Sharpe=1.265 | DD=10.57% | Turnover=23.52%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0924 | critic_loss=0.0810 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0405 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0756 | balance_loss=0.0001 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2650 | ema=0.7958 | best_ema=0.7958 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5676
   📈 Benchmark Relative: 1/N shaping=-0.001 (EW ret=0.00359) | SPY shaping=0.002 (SPY ret=0.00301)
[CYCLE] Update 34/219 | Step 34,272/300,000 | Episode 44 | Time: 4088.8s
   📊 Metrics: Return=-7.03% | Sharpe=-0.495 | DD=19.76% | Turnover=22.66%
   🎚️ Intra-Step TAPE: potential=0.2405 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0937 | critic_loss=0.0672 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0336 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0717 | balance_loss=0.0001 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4946 | ema=0.6668 | best_ema=0.6668 | no_improve=0
   🔬 Alpha Diversity: mean=6.50 | std=1.59 | range=[1.78, 14.95] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=7.06 | PG=6.67 | CAT=6.67  BOT: JNJ=6.38 | XOM=6.31 | JPM=6.17
   🎛️ Mixture Usage: C0=26.2% | C1=32.5% | C2=41.3%
   🧭 Regime Start Dist (train resets): high_vol=16 (33.3%), low_vol=16 (33.3%), medium_vol=16 (33.3%)
[CYCLE] Update 35/219 | Step 35,280/300,000 | Episode 44 | Time: 4136.3s
   📊 Metrics: Return=+0.04% | Sharpe=-0.067 | DD=19.76% | Turnover=23.67%
   🎚️ Intra-Step TAPE: potential=0.2218 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0965 | critic_loss=0.0462 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0231 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0712 | balance_loss=0.0001 | separation_loss=0.0073 | component_dispersion_loss=0.0099
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0670 | ema=0.5934 | best_ema=0.5934 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.414 | Return=+29.94% | DD=19.83%
         Multi-horizon: score=-0.102 | details=252:-0.509/19.8%, 504:-0.016/19.8%, 756:0.342/19.8%, 1008:0.414/19.8%
         SPY relative: spy_return=+41.94% | outperformance=-12.00%
         Equal-weight relative: ew_return=+93.18% | outperformance=-63.25%
[CYCLE] Update 36/219 | Step 36,288/300,000 | Episode 48 | Time: 4491.8s
   📊 Metrics: Return=+54.69% | Sharpe=1.092 | DD=10.20% | Turnover=23.62%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0958 | critic_loss=0.0528 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0264 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0645 | balance_loss=0.0001 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0921 | ema=0.6433 | best_ema=0.6433 | no_improve=0
   🔬 Alpha Diversity: mean=6.52 | std=1.79 | range=[1.27, 14.86] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: MSFT=7.90 | PG=7.22 | CAT=7.20  BOT: JPM=5.87 | AMZN=5.73 | NEE=5.45
   🎛️ Mixture Usage: C0=24.2% | C1=33.1% | C2=42.7%
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=18 (34.6%), medium_vol=17 (32.7%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5305
   📈 Benchmark Relative: 1/N shaping=-0.011 (EW ret=-0.00185) | SPY shaping=-0.016 (SPY ret=0.00000)
[CYCLE] Update 37/219 | Step 37,296/300,000 | Episode 48 | Time: 4538.9s
   📊 Metrics: Return=+2.51% | Sharpe=0.100 | DD=8.31% | Turnover=25.54%
   🎚️ Intra-Step TAPE: potential=0.2608 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0944 | critic_loss=0.0406 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0203 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0774 | balance_loss=0.0000 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1005 | ema=0.5890 | best_ema=0.5890 | no_improve=0
[CYCLE] Update 38/219 | Step 38,304/300,000 | Episode 48 | Time: 4586.3s
   📊 Metrics: Return=+8.99% | Sharpe=0.258 | DD=9.86% | Turnover=25.02%
   🎚️ Intra-Step TAPE: potential=0.4283 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0942 | critic_loss=0.0375 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0188 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0721 | balance_loss=0.0001 | separation_loss=0.0074 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2576 | ema=0.5559 | best_ema=0.5559 | no_improve=0
   🔬 Alpha Diversity: mean=6.49 | std=1.69 | range=[1.35, 15.15] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.35 | MSFT=6.76 | PG=6.74  BOT: XOM=6.21 | JPM=6.20 | AMZN=5.94
   🎛️ Mixture Usage: C0=29.3% | C1=31.4% | C2=39.3%
   🧭 Regime Start Dist (train resets): high_vol=17 (32.7%), low_vol=18 (34.6%), medium_vol=17 (32.7%)
      🧪 Deterministic validation: Sharpe=0.643 | Return=+46.96% | DD=21.82%
         Multi-horizon: score=-0.032 | details=252:-0.623/21.8%, 504:0.100/21.8%, 756:0.573/21.8%, 1008:0.643/21.8%
         SPY relative: spy_return=+41.94% | outperformance=+5.03%
         Equal-weight relative: ew_return=+93.18% | outperformance=-46.22%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-46.22%, required>0.00%).
[CYCLE] Update 39/219 | Step 39,312/300,000 | Episode 52 | Time: 4942.3s
   📊 Metrics: Return=+30.11% | Sharpe=0.463 | DD=25.57% | Turnover=24.74%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0935 | critic_loss=0.0377 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0188 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0646 | balance_loss=0.0001 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4635 | ema=0.5466 | best_ema=0.5466 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.001) | TAPE=0.2754
   📈 Benchmark Relative: 1/N shaping=-0.065 (EW ret=0.00982) | SPY shaping=-0.068 (SPY ret=0.01522)
[CYCLE] Update 40/219 | Step 40,320/300,000 | Episode 52 | Time: 4989.0s
   📊 Metrics: Return=+5.91% | Sharpe=0.453 | DD=4.97% | Turnover=23.38%
   🎚️ Intra-Step TAPE: potential=0.2288 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0944 | critic_loss=0.0482 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0241 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0691 | balance_loss=0.0001 | separation_loss=0.0076 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4534 | ema=0.5373 | best_ema=0.5373 | no_improve=0
   🔬 Alpha Diversity: mean=6.50 | std=1.68 | range=[0.89, 15.86] | cap_hit=0.1%
   🏷️ Alpha Per-Asset  TOP: NEE=7.69 | GLD=6.92 | NVDA=6.81  BOT: PG=5.94 | XOM=5.91 | JNJ=5.38
   🎛️ Mixture Usage: C0=30.1% | C1=28.2% | C2=41.8%
   🧭 Regime Start Dist (train resets): high_vol=18 (32.1%), low_vol=20 (35.7%), medium_vol=18 (32.1%)
[CYCLE] Update 41/219 | Step 41,328/300,000 | Episode 52 | Time: 5036.1s
   📊 Metrics: Return=+9.05% | Sharpe=0.284 | DD=8.10% | Turnover=23.67%
   🎚️ Intra-Step TAPE: potential=0.2474 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0937 | critic_loss=0.0426 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0213 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0594 | balance_loss=0.0001 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2838 | ema=0.5119 | best_ema=0.5119 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.720 | Return=+54.68% | DD=21.76%
         Multi-horizon: score=0.016 | details=252:-0.633/21.8%, 504:0.158/21.8%, 756:0.682/21.8%, 1008:0.720/21.8%
         SPY relative: spy_return=+41.94% | outperformance=+12.74%
         Equal-weight relative: ew_return=+93.18% | outperformance=-38.50%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-38.50%, required>0.00%).
[CYCLE] Update 42/219 | Step 42,336/300,000 | Episode 56 | Time: 5394.4s
   📊 Metrics: Return=+4.58% | Sharpe=0.011 | DD=10.42% | Turnover=23.58%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0943 | critic_loss=0.0719 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0360 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0506 | balance_loss=0.0002 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0107 | ema=0.4618 | best_ema=0.4618 | no_improve=0
   🔬 Alpha Diversity: mean=6.40 | std=1.31 | range=[1.41, 14.99] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=7.16 | NVDA=7.08 | CAT=6.65  BOT: GLD=6.05 | PG=5.83 | MSFT=5.75
   🎛️ Mixture Usage: C0=28.5% | C1=27.0% | C2=44.5%
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=20 (33.3%), medium_vol=20 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2466
   📈 Benchmark Relative: 1/N shaping=-0.015 (EW ret=0.00146) | SPY shaping=0.009 (SPY ret=-0.00225)
[CYCLE] Update 43/219 | Step 43,344/300,000 | Episode 56 | Time: 5441.3s
   📊 Metrics: Return=+1.82% | Sharpe=0.065 | DD=20.05% | Turnover=21.52%
   🎚️ Intra-Step TAPE: potential=0.7382 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0941 | critic_loss=0.0611 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0306 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0397 | balance_loss=0.0002 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0650 | ema=0.4221 | best_ema=0.4221 | no_improve=0
[CYCLE] Update 44/219 | Step 44,352/300,000 | Episode 56 | Time: 5488.7s
   📊 Metrics: Return=+2.43% | Sharpe=0.066 | DD=26.31% | Turnover=22.83%
   🎚️ Intra-Step TAPE: potential=0.2198 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0975 | critic_loss=0.0382 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0191 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0219 | balance_loss=0.0003 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0663 | ema=0.3866 | best_ema=0.3866 | no_improve=0
   🔬 Alpha Diversity: mean=6.31 | std=1.55 | range=[1.76, 14.85] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=7.86 | NVDA=6.76 | GLD=6.71  BOT: JPM=5.73 | AMZN=5.69 | MSFT=5.39
   🎛️ Mixture Usage: C0=24.9% | C1=27.4% | C2=47.7%
   🧭 Regime Start Dist (train resets): high_vol=20 (33.3%), low_vol=20 (33.3%), medium_vol=20 (33.3%)
      🧪 Deterministic validation: Sharpe=0.583 | Return=+43.32% | DD=22.45%
         Multi-horizon: score=-0.014 | details=252:-0.558/22.4%, 504:0.162/22.4%, 756:0.506/22.4%, 1008:0.583/22.4%
         SPY relative: spy_return=+41.94% | outperformance=+1.39%
         Equal-weight relative: ew_return=+93.18% | outperformance=-49.86%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-49.86%, required>0.00%).
[CYCLE] Update 45/219 | Step 45,360/300,000 | Episode 60 | Time: 5845.6s
   📊 Metrics: Return=+76.84% | Sharpe=1.644 | DD=9.36% | Turnover=22.56%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0967 | critic_loss=0.1207 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0604 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0048 | balance_loss=0.0004 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6438 | ema=0.5123 | best_ema=0.5123 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.6197
   📈 Benchmark Relative: 1/N shaping=-0.000 (EW ret=-0.00323) | SPY shaping=0.000 (SPY ret=-0.00332)
[CYCLE] Update 46/219 | Step 46,368/300,000 | Episode 60 | Time: 5892.6s
   📊 Metrics: Return=+1.03% | Sharpe=0.006 | DD=16.98% | Turnover=22.84%
   🎚️ Intra-Step TAPE: potential=0.5185 | delta_reward=-0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0941 | critic_loss=0.0360 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0180 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0441 | balance_loss=0.0002 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0057 | ema=0.4616 | best_ema=0.4616 | no_improve=0
   🔬 Alpha Diversity: mean=6.32 | std=1.66 | range=[1.76, 15.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.01 | PG=6.76 | GLD=6.60  BOT: AMZN=5.55 | XOM=5.43 | MSFT=5.34
   🎛️ Mixture Usage: C0=25.7% | C1=25.1% | C2=49.2%
   🧭 Regime Start Dist (train resets): high_vol=22 (34.4%), low_vol=21 (32.8%), medium_vol=21 (32.8%)
[CYCLE] Update 47/219 | Step 47,376/300,000 | Episode 60 | Time: 5939.7s
   📊 Metrics: Return=+28.17% | Sharpe=0.590 | DD=26.30% | Turnover=23.20%
   🎚️ Intra-Step TAPE: potential=0.6939 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0954 | critic_loss=0.0421 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0210 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0410 | balance_loss=0.0002 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5902 | ema=0.4745 | best_ema=0.4745 | no_improve=0
[CYCLE] Update 48/219 | Step 48,384/300,000 | Episode 64 | Time: 5987.7s
   📊 Metrics: Return=+59.59% | Sharpe=1.281 | DD=9.48% | Turnover=23.58%
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0965 | critic_loss=0.1355 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0678 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0409 | balance_loss=0.0002 | separation_loss=0.0074 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2811 | ema=0.5551 | best_ema=0.5551 | no_improve=0
   🔬 Alpha Diversity: mean=6.59 | std=2.21 | range=[0.96, 15.84] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=9.29 | GLD=7.36 | PG=6.94  BOT: XOM=5.45 | MSFT=5.16 | JNJ=4.91
   🎛️ Mixture Usage: C0=26.0% | C1=26.6% | C2=47.4%
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=23 (33.8%), medium_vol=22 (32.4%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5671
   📈 Benchmark Relative: 1/N shaping=0.007 (EW ret=0.00582) | SPY shaping=0.027 (SPY ret=0.00130)
[CYCLE] Update 49/219 | Step 49,392/300,000 | Episode 64 | Time: 6035.0s
   📊 Metrics: Return=+6.70% | Sharpe=0.406 | DD=16.07% | Turnover=24.44%
   🎚️ Intra-Step TAPE: potential=0.7479 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0940 | critic_loss=0.0555 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0278 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0441 | balance_loss=0.0002 | separation_loss=0.0074 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4056 | ema=0.5402 | best_ema=0.5402 | no_improve=0

📚 EPISODE HORIZON UPDATE at 50,400 steps:
   Episode horizon: 766 steps
[CYCLE] Update 50/219 | Step 50,400/300,000 | Episode 64 | Time: 6083.0s
   📊 Metrics: Return=+14.64% | Sharpe=0.337 | DD=25.72% | Turnover=24.40%
   🎚️ Intra-Step TAPE: potential=0.2255 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0944 | critic_loss=0.0440 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0220 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0516 | balance_loss=0.0001 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3372 | ema=0.5199 | best_ema=0.5199 | no_improve=0
   🔬 Alpha Diversity: mean=6.40 | std=1.74 | range=[2.05, 15.33] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NEE=8.49 | GLD=7.08 | PG=6.63  BOT: XOM=5.47 | AMZN=5.41 | MSFT=4.85
   🎛️ Mixture Usage: C0=25.4% | C1=29.9% | C2=44.7%
   🧭 Regime Start Dist (train resets): high_vol=23 (33.8%), low_vol=23 (33.8%), medium_vol=22 (32.4%)

📚 EPISODE HORIZON UPDATE at 51,408 steps:
   Episode horizon: 791 steps
[CYCLE] Update 51/219 | Step 51,408/300,000 | Episode 64 | Time: 6130.4s
   📊 Metrics: Return=+57.42% | Sharpe=0.782 | DD=25.72% | Turnover=23.92%
   🎚️ Intra-Step TAPE: potential=0.7260 | delta_reward=+0.0013
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0940 | critic_loss=0.0392 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0196 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0395 | balance_loss=0.0002 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7822 | ema=0.5461 | best_ema=0.5461 | no_improve=0
      🧪 Deterministic validation: Sharpe=0.618 | Return=+45.33% | DD=22.91%
         Multi-horizon: score=0.005 | details=252:-0.495/22.9%, 504:0.136/22.9%, 756:0.510/22.9%, 1008:0.618/22.9%
         SPY relative: spy_return=+41.94% | outperformance=+3.39%
         Equal-weight relative: ew_return=+93.18% | outperformance=-47.85%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-47.85%, required>0.00%).

📚 EPISODE HORIZON UPDATE at 52,416 steps:
   Episode horizon: 817 steps
[CYCLE] Update 52/219 | Step 52,416/300,000 | Episode 68 | Time: 6488.5s
   📊 Metrics: Return=+41.39% | Sharpe=0.581 | DD=25.99% | Turnover=24.50%
   🎚️ Intra-Step TAPE: potential=0.2426 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0927 | critic_loss=0.0548 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0274 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0513 | balance_loss=0.0001 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5812 | ema=0.5496 | best_ema=0.5496 | no_improve=0
   🔬 Alpha Diversity: mean=6.40 | std=1.53 | range=[1.82, 15.11] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.58 | NEE=7.41 | JNJ=7.29  BOT: JPM=6.13 | AMZN=5.40 | MSFT=5.05
   🎛️ Mixture Usage: C0=25.2% | C1=29.0% | C2=45.8%
   🧭 Regime Start Dist (train resets): high_vol=24 (33.3%), low_vol=24 (33.3%), medium_vol=24 (33.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 5.63% / trig 25.00%) | terminal=0.000 (peak 0.001) | TAPE=0.3100
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=-0.01939) | SPY shaping=-0.009 (SPY ret=-0.01736)

📚 EPISODE HORIZON UPDATE at 53,424 steps:
   Episode horizon: 842 steps
[CYCLE] Update 53/219 | Step 53,424/300,000 | Episode 68 | Time: 6535.4s
   📊 Metrics: Return=+6.82% | Sharpe=0.182 | DD=25.11% | Turnover=23.32%
   🎚️ Intra-Step TAPE: potential=0.7220 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0925 | critic_loss=0.0363 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0181 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0398 | balance_loss=0.0002 | separation_loss=0.0076 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1820 | ema=0.5129 | best_ema=0.5129 | no_improve=0

📚 EPISODE HORIZON UPDATE at 54,432 steps:
   Episode horizon: 868 steps
[CYCLE] Update 54/219 | Step 54,432/300,000 | Episode 68 | Time: 6583.3s
   📊 Metrics: Return=+37.53% | Sharpe=0.560 | DD=25.11% | Turnover=23.03%
   🎚️ Intra-Step TAPE: potential=0.7212 | delta_reward=+0.0008
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0941 | critic_loss=0.0315 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0157 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0431 | balance_loss=0.0002 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5600 | ema=0.5176 | best_ema=0.5176 | no_improve=0
   🔬 Alpha Diversity: mean=6.49 | std=1.73 | range=[0.94, 15.65] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=8.10 | CAT=7.55 | NVDA=7.01  BOT: PG=5.96 | MSFT=5.64 | AMZN=5.45
   🎛️ Mixture Usage: C0=27.3% | C1=24.6% | C2=48.1%
   🧭 Regime Start Dist (train resets): high_vol=24 (33.3%), low_vol=24 (33.3%), medium_vol=24 (33.3%)
      🧪 Deterministic validation: Sharpe=0.736 | Return=+55.81% | DD=21.39%
         Multi-horizon: score=0.110 | details=252:-0.453/21.4%, 504:0.239/21.4%, 756:0.699/21.4%, 1008:0.736/21.4%
         SPY relative: spy_return=+41.94% | outperformance=+13.88%
         Equal-weight relative: ew_return=+93.18% | outperformance=-37.37%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-37.37%, required>0.00%).

📚 EPISODE HORIZON UPDATE at 55,440 steps:
   Episode horizon: 893 steps
[CYCLE] Update 55/219 | Step 55,440/300,000 | Episode 72 | Time: 6942.0s
   📊 Metrics: Return=+33.75% | Sharpe=0.638 | DD=14.03% | Turnover=22.66%
   🎚️ Intra-Step TAPE: potential=0.2269 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0942 | critic_loss=0.0861 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0431 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0475 | balance_loss=0.0002 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6379 | ema=0.5296 | best_ema=0.5296 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 8.22% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3531
   📈 Benchmark Relative: 1/N shaping=-0.010 (EW ret=0.00059) | SPY shaping=-0.006 (SPY ret=0.00060)

📚 EPISODE HORIZON UPDATE at 56,448 steps:
   Episode horizon: 918 steps
[CYCLE] Update 56/219 | Step 56,448/300,000 | Episode 72 | Time: 6989.1s
   📊 Metrics: Return=+10.58% | Sharpe=0.419 | DD=16.91% | Turnover=22.39%
   🎚️ Intra-Step TAPE: potential=0.7318 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0938 | critic_loss=0.0436 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0218 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0300 | balance_loss=0.0002 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4192 | ema=0.5186 | best_ema=0.5186 | no_improve=0
   🔬 Alpha Diversity: mean=6.32 | std=1.52 | range=[1.71, 14.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.34 | NEE=7.18 | GLD=6.82  BOT: XOM=6.11 | MSFT=5.20 | AMZN=5.12
   🎛️ Mixture Usage: C0=22.7% | C1=25.9% | C2=51.4%
   🧭 Regime Start Dist (train resets): high_vol=26 (34.2%), low_vol=26 (34.2%), medium_vol=24 (31.6%)

📚 EPISODE HORIZON UPDATE at 57,456 steps:
   Episode horizon: 944 steps
[CYCLE] Update 57/219 | Step 57,456/300,000 | Episode 72 | Time: 7036.3s
   📊 Metrics: Return=+14.11% | Sharpe=0.273 | DD=26.46% | Turnover=22.89%
   🎚️ Intra-Step TAPE: potential=0.2181 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0955 | critic_loss=0.0535 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0268 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0334 | balance_loss=0.0002 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2728 | ema=0.4940 | best_ema=0.4940 | no_improve=0

📚 EPISODE HORIZON UPDATE at 58,464 steps:
   Episode horizon: 969 steps
[CYCLE] Update 58/219 | Step 58,464/300,000 | Episode 72 | Time: 7083.5s
   📊 Metrics: Return=+66.08% | Sharpe=0.772 | DD=26.46% | Turnover=23.49%
   🎚️ Intra-Step TAPE: potential=0.6215 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0944 | critic_loss=0.0285 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0143 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0353 | balance_loss=0.0002 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7722 | ema=0.5218 | best_ema=0.5218 | no_improve=0
   🔬 Alpha Diversity: mean=6.34 | std=1.67 | range=[1.38, 14.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.14 | JNJ=7.09 | NEE=7.02  BOT: XOM=5.76 | AMZN=5.57 | MSFT=5.13
   🎛️ Mixture Usage: C0=24.0% | C1=29.6% | C2=46.4%
   🧭 Regime Start Dist (train resets): high_vol=26 (34.2%), low_vol=26 (34.2%), medium_vol=24 (31.6%)
      🧪 Deterministic validation: Sharpe=0.653 | Return=+49.21% | DD=20.39%
         Multi-horizon: score=0.153 | details=252:-0.298/20.4%, 504:0.261/20.4%, 756:0.661/20.4%, 1008:0.653/20.4%
         SPY relative: spy_return=+41.94% | outperformance=+7.27%
         Equal-weight relative: ew_return=+93.18% | outperformance=-43.97%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-43.97%, required>0.00%).

📚 EPISODE HORIZON UPDATE at 59,472 steps:
   Episode horizon: 995 steps
[CYCLE] Update 59/219 | Step 59,472/300,000 | Episode 76 | Time: 7444.9s
   📊 Metrics: Return=+62.47% | Sharpe=0.970 | DD=11.81% | Turnover=22.77%
   🎚️ Intra-Step TAPE: potential=0.5696 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0934 | critic_loss=0.1059 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0529 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0403 | balance_loss=0.0002 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9700 | ema=0.5666 | best_ema=0.5666 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5047
   📈 Benchmark Relative: 1/N shaping=0.001 (EW ret=-0.00059) | SPY shaping=0.002 (SPY ret=-0.00091)

📚 TURNOVER CURRICULUM UPDATE at 60,480 steps:
   Turnover penalty scalar: 0.15

🎛️ EXECUTION BETA UPDATE at 60,480 steps:
   action_execution_beta: 0.650 (w_exec=(1-β)w_prev + βw_raw)

📚 EPISODE HORIZON UPDATE at 60,480 steps:
   Episode horizon: 1008 steps
[CYCLE] Update 60/219 | Step 60,480/300,000 | Episode 76 | Time: 7492.3s
   📊 Metrics: Return=+49.25% | Sharpe=1.982 | DD=8.89% | Turnover=21.95%
   🎚️ Intra-Step TAPE: potential=0.6431 | delta_reward=+0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0912 | critic_loss=0.0276 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0342 | balance_loss=0.0002 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.9824 | ema=0.7082 | best_ema=0.7082 | no_improve=0
   🔬 Alpha Diversity: mean=6.18 | std=1.40 | range=[1.44, 14.24] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.16 | NEE=6.93 | NVDA=6.84  BOT: PG=5.91 | AMZN=5.24 | MSFT=5.02
   🎛️ Mixture Usage: C0=23.2% | C1=26.7% | C2=50.1%
   🧭 Regime Start Dist (train resets): high_vol=27 (33.8%), low_vol=27 (33.8%), medium_vol=26 (32.5%)
[CYCLE] Update 61/219 | Step 61,488/300,000 | Episode 76 | Time: 7539.8s
   📊 Metrics: Return=+75.16% | Sharpe=1.726 | DD=9.75% | Turnover=25.40%
   🎚️ Intra-Step TAPE: potential=0.2288 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0937 | critic_loss=0.0325 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0163 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0257 | balance_loss=0.0002 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.7260 | ema=0.8100 | best_ema=0.8100 | no_improve=0
[CYCLE] Update 62/219 | Step 62,496/300,000 | Episode 76 | Time: 7588.1s
   📊 Metrics: Return=+84.41% | Sharpe=1.239 | DD=16.94% | Turnover=26.95%
   🎚️ Intra-Step TAPE: potential=0.7374 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0952 | critic_loss=0.0386 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0193 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0278 | balance_loss=0.0002 | separation_loss=0.0076 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2387 | ema=0.8529 | best_ema=0.8529 | no_improve=0
   🔬 Alpha Diversity: mean=6.17 | std=1.73 | range=[1.07, 14.44] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=7.11 | CAT=7.03 | MSFT=6.85  BOT: JNJ=5.98 | GLD=5.11 | PG=4.00
   🎛️ Mixture Usage: C0=25.0% | C1=28.2% | C2=46.8%
   🧭 Regime Start Dist (train resets): high_vol=27 (33.8%), low_vol=27 (33.8%), medium_vol=26 (32.5%)
      🧪 Deterministic validation: Sharpe=0.577 | Return=+43.58% | DD=21.96%
         Multi-horizon: score=0.068 | details=252:-0.399/22.0%, 504:0.224/22.0%, 756:0.546/22.0%, 1008:0.577/22.0%
         SPY relative: spy_return=+41.94% | outperformance=+1.64%
         Equal-weight relative: ew_return=+93.18% | outperformance=-49.60%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-49.60%, required>0.00%).
[CYCLE] Update 63/219 | Step 63,504/300,000 | Episode 80 | Time: 7947.2s
   📊 Metrics: Return=+51.35% | Sharpe=0.766 | DD=12.19% | Turnover=28.03%
   🎚️ Intra-Step TAPE: potential=0.5986 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0932 | critic_loss=0.0740 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0370 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0468 | balance_loss=0.0001 | separation_loss=0.0073 | component_dispersion_loss=0.0100
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7658 | ema=0.8442 | best_ema=0.8442 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4030
   📈 Benchmark Relative: 1/N shaping=-0.012 (EW ret=0.00059) | SPY shaping=-0.013 (SPY ret=0.00178)
[CYCLE] Update 64/219 | Step 64,512/300,000 | Episode 80 | Time: 7994.2s
   📊 Metrics: Return=+10.78% | Sharpe=0.484 | DD=6.42% | Turnover=32.69%
   🎚️ Intra-Step TAPE: potential=0.2438 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0916 | critic_loss=0.0402 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0201 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0465 | balance_loss=0.0002 | separation_loss=0.0075 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4844 | ema=0.8082 | best_ema=0.8082 | no_improve=0
   🔬 Alpha Diversity: mean=6.32 | std=1.61 | range=[1.52, 14.18] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.59 | CAT=7.24 | NEE=6.96  BOT: PG=5.86 | AMZN=5.54 | JNJ=5.49
   🎛️ Mixture Usage: C0=24.0% | C1=29.5% | C2=46.5%
   🧭 Regime Start Dist (train resets): high_vol=28 (33.3%), low_vol=28 (33.3%), medium_vol=28 (33.3%)
[CYCLE] Update 65/219 | Step 65,520/300,000 | Episode 80 | Time: 8041.5s
   📊 Metrics: Return=+13.02% | Sharpe=0.313 | DD=7.91% | Turnover=32.28%
   🎚️ Intra-Step TAPE: potential=0.2877 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0925 | critic_loss=0.0599 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0299 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0418 | balance_loss=0.0002 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3125 | ema=0.7586 | best_ema=0.7586 | no_improve=0
[CYCLE] Update 66/219 | Step 66,528/300,000 | Episode 80 | Time: 8088.9s
   📊 Metrics: Return=+23.57% | Sharpe=0.393 | DD=11.75% | Turnover=32.11%
   🎚️ Intra-Step TAPE: potential=0.7459 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0917 | critic_loss=0.0337 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0168 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0472 | balance_loss=0.0001 | separation_loss=0.0076 | component_dispersion_loss=0.0101
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3933 | ema=0.7221 | best_ema=0.7221 | no_improve=0
   🔬 Alpha Diversity: mean=6.34 | std=1.63 | range=[1.48, 14.49] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.74 | CAT=7.59 | JNJ=6.97  BOT: XOM=5.62 | MSFT=5.24 | AMZN=5.19
   🎛️ Mixture Usage: C0=24.3% | C1=32.7% | C2=43.0%
   🧭 Regime Start Dist (train resets): high_vol=28 (33.3%), low_vol=28 (33.3%), medium_vol=28 (33.3%)
[CYCLE] Update 67/219 | Step 67,536/300,000 | Episode 84 | Time: 8136.2s
   📊 Metrics: Return=+34.73% | Sharpe=0.539 | DD=13.66% | Turnover=31.69%
   🎚️ Intra-Step TAPE: potential=0.6318 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0910 | critic_loss=0.0462 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0231 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0393 | balance_loss=0.0002 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5386 | ema=0.7037 | best_ema=0.7037 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.08% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3198
   📈 Benchmark Relative: 1/N shaping=0.004 (EW ret=0.00078) | SPY shaping=0.002 (SPY ret=0.00094)
[CYCLE] Update 68/219 | Step 68,544/300,000 | Episode 84 | Time: 8183.9s
   📊 Metrics: Return=+41.34% | Sharpe=1.688 | DD=9.99% | Turnover=30.36%
   🎚️ Intra-Step TAPE: potential=0.6208 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0903 | critic_loss=0.0343 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0172 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0279 | balance_loss=0.0002 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.6884 | ema=0.8022 | best_ema=0.8022 | no_improve=0
   🔬 Alpha Diversity: mean=6.17 | std=1.41 | range=[1.45, 15.02] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.14 | NVDA=7.02 | NEE=6.95  BOT: PG=5.92 | MSFT=5.23 | AMZN=5.19
   🎛️ Mixture Usage: C0=21.8% | C1=33.5% | C2=44.6%
   🧭 Regime Start Dist (train resets): high_vol=30 (34.1%), low_vol=28 (31.8%), medium_vol=30 (34.1%)
[CYCLE] Update 69/219 | Step 69,552/300,000 | Episode 84 | Time: 8231.4s
   📊 Metrics: Return=+68.97% | Sharpe=1.596 | DD=9.99% | Turnover=29.79%
   🎚️ Intra-Step TAPE: potential=0.2230 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0897 | critic_loss=0.0265 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0132 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0217 | balance_loss=0.0002 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5964 | ema=0.8816 | best_ema=0.8816 | no_improve=0
[CYCLE] Update 70/219 | Step 70,560/300,000 | Episode 84 | Time: 8279.0s
   📊 Metrics: Return=+70.79% | Sharpe=1.067 | DD=20.69% | Turnover=30.43%
   🎚️ Intra-Step TAPE: potential=0.7269 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0926 | critic_loss=0.0276 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0296 | balance_loss=0.0002 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.0665 | ema=0.9001 | best_ema=0.9001 | no_improve=0
   🔬 Alpha Diversity: mean=6.14 | std=1.39 | range=[1.81, 14.19] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.46 | JNJ=6.92 | NEE=6.50  BOT: AMZN=5.72 | MSFT=5.55 | PG=5.06
   🎛️ Mixture Usage: C0=26.3% | C1=28.5% | C2=45.2%
   🧭 Regime Start Dist (train resets): high_vol=30 (34.1%), low_vol=28 (31.8%), medium_vol=30 (34.1%)
      🧪 Deterministic validation: Sharpe=0.596 | Return=+42.09% | DD=20.21%
         Multi-horizon: score=0.022 | details=252:-0.410/20.2%, 504:0.103/20.2%, 756:0.482/20.2%, 1008:0.596/20.2%
         SPY relative: spy_return=+41.94% | outperformance=+0.15%
         Equal-weight relative: ew_return=+93.18% | outperformance=-51.09%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-51.09%, required>0.00%).
[CYCLE] Update 71/219 | Step 71,568/300,000 | Episode 88 | Time: 8641.6s
   📊 Metrics: Return=+55.81% | Sharpe=0.604 | DD=26.71% | Turnover=31.07%
   🎚️ Intra-Step TAPE: potential=0.2254 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0894 | critic_loss=0.0544 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0272 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0100 | balance_loss=0.0002 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6036 | ema=0.8704 | best_ema=0.8704 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 8.39% / trig 25.00%) | terminal=0.000 (peak 0.002) | TAPE=0.3155
   📈 Benchmark Relative: 1/N shaping=-0.004 (EW ret=-0.00038) | SPY shaping=0.028 (SPY ret=-0.00644)
[CYCLE] Update 72/219 | Step 72,576/300,000 | Episode 88 | Time: 8689.3s
   📊 Metrics: Return=+11.14% | Sharpe=0.392 | DD=19.16% | Turnover=31.20%
   🎚️ Intra-Step TAPE: potential=0.7151 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0921 | critic_loss=0.0381 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0191 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=1.0474 | balance_loss=0.0001 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3919 | ema=0.8226 | best_ema=0.8226 | no_improve=0
   🔬 Alpha Diversity: mean=6.34 | std=1.76 | range=[1.18, 15.03] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: AMZN=7.40 | JNJ=7.04 | CAT=6.91  BOT: GLD=5.95 | NEE=5.88 | PG=4.32
   🎛️ Mixture Usage: C0=25.0% | C1=31.2% | C2=43.8%
   🧭 Regime Start Dist (train resets): high_vol=30 (32.6%), low_vol=32 (34.8%), medium_vol=30 (32.6%)
[CYCLE] Update 73/219 | Step 73,584/300,000 | Episode 88 | Time: 8736.9s
   📊 Metrics: Return=+5.26% | Sharpe=0.097 | DD=28.01% | Turnover=30.76%
   🎚️ Intra-Step TAPE: potential=0.2142 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0922 | critic_loss=0.0277 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0138 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0574 | balance_loss=0.0000 | separation_loss=0.0077 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0968 | ema=0.7500 | best_ema=0.7500 | no_improve=0
[CYCLE] Update 74/219 | Step 74,592/300,000 | Episode 88 | Time: 8784.8s
   📊 Metrics: Return=+44.57% | Sharpe=0.530 | DD=28.01% | Turnover=30.64%
   🎚️ Intra-Step TAPE: potential=0.6177 | delta_reward=-0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0942 | critic_loss=0.0342 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0171 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0500 | balance_loss=0.0001 | separation_loss=0.0079 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5296 | ema=0.7280 | best_ema=0.7280 | no_improve=0
   🔬 Alpha Diversity: mean=6.22 | std=1.23 | range=[2.06, 13.48] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.25 | XOM=6.72 | NVDA=6.43  BOT: MSFT=5.93 | AMZN=5.80 | PG=5.68
   🎛️ Mixture Usage: C0=25.3% | C1=33.3% | C2=41.4%
   🧭 Regime Start Dist (train resets): high_vol=30 (32.6%), low_vol=32 (34.8%), medium_vol=30 (32.6%)
      🧪 Deterministic validation: Sharpe=0.539 | Return=+39.06% | DD=20.95%
         Multi-horizon: score=0.006 | details=252:-0.405/21.0%, 504:0.075/21.0%, 756:0.480/21.0%, 1008:0.539/21.0%
         SPY relative: spy_return=+41.94% | outperformance=-2.87%
         Equal-weight relative: ew_return=+93.18% | outperformance=-54.12%
         [WARN] SPY gate rejected checkpoint (outperformance=-2.87%, required>0.00%).
[CYCLE] Update 75/219 | Step 75,600/300,000 | Episode 92 | Time: 9147.6s
   📊 Metrics: Return=+59.29% | Sharpe=0.616 | DD=26.54% | Turnover=30.70%
   🎚️ Intra-Step TAPE: potential=0.2301 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0906 | critic_loss=0.0507 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0253 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0595 | balance_loss=0.0000 | separation_loss=0.0079 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6155 | ema=0.7167 | best_ema=0.7167 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 6.04% / trig 25.00%) | terminal=0.000 (peak 0.002) | TAPE=0.3139
   📈 Benchmark Relative: 1/N shaping=-0.018 (EW ret=0.00633) | SPY shaping=0.015 (SPY ret=0.00116)
[CYCLE] Update 76/219 | Step 76,608/300,000 | Episode 92 | Time: 9195.5s
   📊 Metrics: Return=-6.53% | Sharpe=-0.445 | DD=15.29% | Turnover=29.72%
   🎚️ Intra-Step TAPE: potential=0.2443 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0891 | critic_loss=0.0310 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0155 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0564 | balance_loss=0.0000 | separation_loss=0.0079 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.4447 | ema=0.6006 | best_ema=0.6006 | no_improve=0
   🔬 Alpha Diversity: mean=6.07 | std=1.16 | range=[2.10, 13.31] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=6.88 | NVDA=6.53 | NEE=6.52  BOT: XOM=5.85 | AMZN=5.60 | MSFT=5.08
   🎛️ Mixture Usage: C0=26.8% | C1=34.0% | C2=39.2%
   🧭 Regime Start Dist (train resets): high_vol=32 (33.3%), low_vol=32 (33.3%), medium_vol=32 (33.3%)
[CYCLE] Update 77/219 | Step 77,616/300,000 | Episode 92 | Time: 9243.4s
   📊 Metrics: Return=+12.81% | Sharpe=0.277 | DD=15.29% | Turnover=30.27%
   🎚️ Intra-Step TAPE: potential=0.5496 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0918 | critic_loss=0.0364 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0182 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0481 | balance_loss=0.0001 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.2772 | ema=0.5682 | best_ema=0.5682 | no_improve=0
[CYCLE] Update 78/219 | Step 78,624/300,000 | Episode 92 | Time: 9291.4s
   📊 Metrics: Return=+33.39% | Sharpe=0.588 | DD=15.29% | Turnover=30.19%
   🎚️ Intra-Step TAPE: potential=0.7389 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0924 | critic_loss=0.0392 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0196 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0454 | balance_loss=0.0001 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5884 | ema=0.5703 | best_ema=0.5703 | no_improve=0
   🔬 Alpha Diversity: mean=6.14 | std=1.32 | range=[2.22, 14.07] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.18 | GLD=6.91 | NEE=6.65  BOT: PG=5.89 | AMZN=5.66 | MSFT=5.12
   🎛️ Mixture Usage: C0=25.8% | C1=33.5% | C2=40.7%
   🧭 Regime Start Dist (train resets): high_vol=32 (33.3%), low_vol=32 (33.3%), medium_vol=32 (33.3%)
      🧪 Deterministic validation: Sharpe=0.554 | Return=+40.19% | DD=22.49%
         Multi-horizon: score=-0.021 | details=252:-0.426/22.5%, 504:0.025/22.5%, 756:0.471/22.5%, 1008:0.554/22.5%
         SPY relative: spy_return=+41.94% | outperformance=-1.74%
         Equal-weight relative: ew_return=+93.18% | outperformance=-52.99%
         [WARN] SPY gate rejected checkpoint (outperformance=-1.74%, required>0.00%).
[CYCLE] Update 79/219 | Step 79,632/300,000 | Episode 96 | Time: 9652.5s
   📊 Metrics: Return=+54.87% | Sharpe=0.779 | DD=17.97% | Turnover=30.46%
   🎚️ Intra-Step TAPE: potential=0.7450 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0953 | critic_loss=0.0555 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0277 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0485 | balance_loss=0.0000 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7787 | ema=0.5911 | best_ema=0.5911 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.94% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4042
   📈 Benchmark Relative: 1/N shaping=-0.003 (EW ret=0.00290) | SPY shaping=0.006 (SPY ret=0.00136)
[CYCLE] Update 80/219 | Step 80,640/300,000 | Episode 96 | Time: 9700.6s
   📊 Metrics: Return=+35.47% | Sharpe=1.599 | DD=8.82% | Turnover=29.83%
   🎚️ Intra-Step TAPE: potential=0.7488 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0907 | critic_loss=0.0367 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0183 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0465 | balance_loss=0.0000 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5993 | ema=0.6919 | best_ema=0.6919 | no_improve=0
   🔬 Alpha Diversity: mean=6.09 | std=1.16 | range=[2.25, 13.56] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.19 | GLD=6.79 | NVDA=6.50  BOT: PG=5.93 | AMZN=5.39 | MSFT=4.98
   🎛️ Mixture Usage: C0=22.6% | C1=32.4% | C2=44.9%
   🧭 Regime Start Dist (train resets): high_vol=34 (34.0%), low_vol=33 (33.0%), medium_vol=33 (33.0%)
[CYCLE] Update 81/219 | Step 81,648/300,000 | Episode 96 | Time: 9748.4s
   📊 Metrics: Return=+52.93% | Sharpe=1.344 | DD=8.82% | Turnover=29.68%
   🎚️ Intra-Step TAPE: potential=0.2861 | delta_reward=+0.0003
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0911 | critic_loss=0.0323 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0162 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0471 | balance_loss=0.0000 | separation_loss=0.0079 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3435 | ema=0.7571 | best_ema=0.7571 | no_improve=0
[CYCLE] Update 82/219 | Step 82,656/300,000 | Episode 96 | Time: 9796.3s
   📊 Metrics: Return=+55.39% | Sharpe=0.894 | DD=17.90% | Turnover=29.44%
   🎚️ Intra-Step TAPE: potential=0.2596 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0905 | critic_loss=0.0337 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0168 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0443 | balance_loss=0.0000 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8944 | ema=0.7708 | best_ema=0.7708 | no_improve=0
   🔬 Alpha Diversity: mean=6.06 | std=1.16 | range=[2.12, 14.05] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=7.04 | GLD=6.70 | NVDA=6.43  BOT: AMZN=5.83 | PG=5.76 | MSFT=4.89
   🎛️ Mixture Usage: C0=28.5% | C1=31.0% | C2=40.6%
   🧭 Regime Start Dist (train resets): high_vol=34 (34.0%), low_vol=33 (33.0%), medium_vol=33 (33.0%)
      🧪 Deterministic validation: Sharpe=0.583 | Return=+42.15% | DD=19.72%
         Multi-horizon: score=-0.004 | details=252:-0.442/19.7%, 504:0.051/19.7%, 756:0.487/19.7%, 1008:0.583/19.7%
         SPY relative: spy_return=+41.94% | outperformance=+0.22%
         Equal-weight relative: ew_return=+93.18% | outperformance=-51.03%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-51.03%, required>0.00%).
[CYCLE] Update 83/219 | Step 83,664/300,000 | Episode 100 | Time: 10156.8s
   📊 Metrics: Return=+2.56% | Sharpe=-0.057 | DD=12.83% | Turnover=30.36%
   🎚️ Intra-Step TAPE: potential=0.2475 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0910 | critic_loss=0.0686 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0343 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0346 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=-0.0566 | ema=0.6881 | best_ema=0.6881 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.94% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2443
   📈 Benchmark Relative: 1/N shaping=0.019 (EW ret=-0.01772) | SPY shaping=0.019 (SPY ret=-0.01905)
[CYCLE] Update 84/219 | Step 84,672/300,000 | Episode 100 | Time: 10204.7s
   📊 Metrics: Return=+4.02% | Sharpe=0.101 | DD=11.80% | Turnover=30.06%
   🎚️ Intra-Step TAPE: potential=0.5141 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0912 | critic_loss=0.0232 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0116 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0288 | balance_loss=0.0000 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.1007 | ema=0.6293 | best_ema=0.6293 | no_improve=0
   🔬 Alpha Diversity: mean=5.99 | std=1.20 | range=[1.95, 13.60] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=6.71 | JNJ=6.64 | NVDA=6.50  BOT: XOM=5.91 | AMZN=5.79 | MSFT=4.67
   🎛️ Mixture Usage: C0=24.3% | C1=34.9% | C2=40.8%
   🧭 Regime Start Dist (train resets): high_vol=35 (33.7%), low_vol=35 (33.7%), medium_vol=34 (32.7%)
[CYCLE] Update 85/219 | Step 85,680/300,000 | Episode 100 | Time: 10252.8s
   📊 Metrics: Return=+16.76% | Sharpe=0.393 | DD=11.80% | Turnover=29.82%
   🎚️ Intra-Step TAPE: potential=0.2466 | delta_reward=+0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0905 | critic_loss=0.0286 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0143 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0231 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.3927 | ema=0.6057 | best_ema=0.6057 | no_improve=0
[CYCLE] Update 86/219 | Step 86,688/300,000 | Episode 100 | Time: 10301.3s
   📊 Metrics: Return=+51.60% | Sharpe=0.925 | DD=11.80% | Turnover=29.68%
   🎚️ Intra-Step TAPE: potential=0.7550 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0907 | critic_loss=0.0212 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0106 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0275 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9250 | ema=0.6376 | best_ema=0.6376 | no_improve=0
   🔬 Alpha Diversity: mean=5.92 | std=1.14 | range=[2.44, 13.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=6.68 | CAT=6.62 | NVDA=6.31  BOT: JPM=5.76 | AMZN=5.42 | MSFT=5.13
   🎛️ Mixture Usage: C0=22.6% | C1=38.8% | C2=38.6%
   🧭 Regime Start Dist (train resets): high_vol=35 (33.7%), low_vol=35 (33.7%), medium_vol=34 (32.7%)
[CYCLE] Update 87/219 | Step 87,696/300,000 | Episode 104 | Time: 10349.8s
   📊 Metrics: Return=+31.15% | Sharpe=0.485 | DD=12.11% | Turnover=30.90%
   🎚️ Intra-Step TAPE: potential=0.7554 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0911 | critic_loss=0.0702 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0351 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0107 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.4851 | ema=0.6224 | best_ema=0.6224 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3026
   📈 Benchmark Relative: 1/N shaping=-0.008 (EW ret=0.00648) | SPY shaping=-0.013 (SPY ret=0.00814)
[CYCLE] Update 88/219 | Step 88,704/300,000 | Episode 104 | Time: 10398.2s
   📊 Metrics: Return=+2.12% | Sharpe=0.017 | DD=21.17% | Turnover=30.43%
   🎚️ Intra-Step TAPE: potential=0.2350 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0897 | critic_loss=0.0496 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0248 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0246 | balance_loss=0.0001 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0171 | ema=0.5618 | best_ema=0.5618 | no_improve=0
   🔬 Alpha Diversity: mean=5.89 | std=1.37 | range=[1.61, 13.46] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=7.19 | NVDA=6.88 | NEE=6.13  BOT: CAT=5.67 | XOM=4.94 | MSFT=4.63
   🎛️ Mixture Usage: C0=24.5% | C1=35.2% | C2=40.3%
   🧭 Regime Start Dist (train resets): high_vol=36 (33.3%), low_vol=36 (33.3%), medium_vol=36 (33.3%)
[CYCLE] Update 89/219 | Step 89,712/300,000 | Episode 104 | Time: 10446.5s
   📊 Metrics: Return=+25.75% | Sharpe=0.607 | DD=21.17% | Turnover=30.40%
   🎚️ Intra-Step TAPE: potential=0.7448 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0907 | critic_loss=0.0287 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0144 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0184 | balance_loss=0.0001 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6070 | ema=0.5664 | best_ema=0.5664 | no_improve=0
[CYCLE] Update 90/219 | Step 90,720/300,000 | Episode 104 | Time: 10494.9s
   📊 Metrics: Return=+51.66% | Sharpe=0.612 | DD=26.57% | Turnover=30.51%
   🎚️ Intra-Step TAPE: potential=0.5563 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0905 | critic_loss=0.0278 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0139 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9907 | balance_loss=0.0002 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.6125 | ema=0.5710 | best_ema=0.5710 | no_improve=0
   🔬 Alpha Diversity: mean=5.76 | std=1.40 | range=[1.29, 12.98] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=7.80 | NEE=6.86 | NVDA=6.24  BOT: CAT=5.42 | XOM=4.60 | MSFT=4.54
   🎛️ Mixture Usage: C0=18.5% | C1=32.6% | C2=48.9%
   🧭 Regime Start Dist (train resets): high_vol=36 (33.3%), low_vol=36 (33.3%), medium_vol=36 (33.3%)
      🧪 Deterministic validation: Sharpe=0.805 | Return=+58.01% | DD=19.13%
         Multi-horizon: score=0.118 | details=252:-0.441/19.1%, 504:0.213/19.1%, 756:0.677/19.1%, 1008:0.805/19.1%
         SPY relative: spy_return=+41.94% | outperformance=+16.08%
         Equal-weight relative: ew_return=+93.18% | outperformance=-35.17%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-35.17%, required>0.00%).
[CYCLE] Update 91/219 | Step 91,728/300,000 | Episode 108 | Time: 10854.2s
   📊 Metrics: Return=+49.67% | Sharpe=0.747 | DD=12.35% | Turnover=32.25%
   🎚️ Intra-Step TAPE: potential=0.7166 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0921 | critic_loss=0.0447 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0224 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9674 | balance_loss=0.0002 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.7470 | ema=0.5886 | best_ema=0.5886 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4125
   📈 Benchmark Relative: 1/N shaping=-0.017 (EW ret=0.01218) | SPY shaping=0.011 (SPY ret=0.00780)
[CYCLE] Update 92/219 | Step 92,736/300,000 | Episode 108 | Time: 10902.6s
   📊 Metrics: Return=+36.73% | Sharpe=1.566 | DD=9.63% | Turnover=31.85%
   🎚️ Intra-Step TAPE: potential=0.7235 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0891 | critic_loss=0.0388 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0194 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0014
   🧩 Mixture Head: gate_entropy=0.9950 | balance_loss=0.0001 | separation_loss=0.0076 | component_dispersion_loss=0.0102
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.5657 | ema=0.6863 | best_ema=0.6863 | no_improve=0
   🔬 Alpha Diversity: mean=5.87 | std=1.58 | range=[1.13, 13.04] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=7.47 | NVDA=7.00 | NEE=6.92  BOT: CAT=4.93 | MSFT=4.69 | XOM=4.38
   🎛️ Mixture Usage: C0=18.4% | C1=34.8% | C2=46.8%
   🧭 Regime Start Dist (train resets): high_vol=37 (33.0%), low_vol=37 (33.0%), medium_vol=38 (33.9%)
[CYCLE] Update 93/219 | Step 93,744/300,000 | Episode 108 | Time: 10951.4s
   📊 Metrics: Return=+58.01% | Sharpe=1.399 | DD=9.63% | Turnover=31.18%
   🎚️ Intra-Step TAPE: potential=0.2478 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0887 | critic_loss=0.0299 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0150 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0105 | balance_loss=0.0001 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.3989 | ema=0.7576 | best_ema=0.7576 | no_improve=0
[CYCLE] Update 94/219 | Step 94,752/300,000 | Episode 108 | Time: 11000.5s
   📊 Metrics: Return=+57.72% | Sharpe=0.911 | DD=20.84% | Turnover=31.00%
   🎚️ Intra-Step TAPE: potential=0.2625 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0904 | critic_loss=0.0393 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0196 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0153 | balance_loss=0.0001 | separation_loss=0.0079 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.9113 | ema=0.7729 | best_ema=0.7729 | no_improve=0
   🔬 Alpha Diversity: mean=5.86 | std=1.15 | range=[1.83, 12.47] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JNJ=6.67 | NVDA=6.59 | NEE=6.32  BOT: PG=5.64 | AMZN=5.32 | MSFT=4.84
   🎛️ Mixture Usage: C0=22.1% | C1=35.4% | C2=42.5%
   🧭 Regime Start Dist (train resets): high_vol=37 (33.0%), low_vol=37 (33.0%), medium_vol=38 (33.9%)
      🧪 Deterministic validation: Sharpe=0.807 | Return=+59.50% | DD=19.64%
         Multi-horizon: score=0.179 | details=252:-0.387/19.6%, 504:0.316/19.6%, 756:0.741/19.6%, 1008:0.807/19.6%
         SPY relative: spy_return=+41.94% | outperformance=+17.56%
         Equal-weight relative: ew_return=+93.18% | outperformance=-33.68%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-33.68%, required>0.00%).
[CYCLE] Update 95/219 | Step 95,760/300,000 | Episode 112 | Time: 11360.4s
   📊 Metrics: Return=+54.85% | Sharpe=0.583 | DD=25.96% | Turnover=31.84%
   🎚️ Intra-Step TAPE: potential=0.2440 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0905 | critic_loss=0.0638 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0319 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0212 | balance_loss=0.0001 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.5825 | ema=0.7539 | best_ema=0.7539 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.96% / trig 25.00%) | terminal=0.000 (peak 0.001) | TAPE=0.3094
   📈 Benchmark Relative: 1/N shaping=-0.018 (EW ret=0.00331) | SPY shaping=-0.007 (SPY ret=0.00245)
[CYCLE] Update 96/219 | Step 96,768/300,000 | Episode 112 | Time: 11407.9s
   📊 Metrics: Return=+44.64% | Sharpe=2.418 | DD=3.42% | Turnover=30.64%
   🎚️ Intra-Step TAPE: potential=0.7438 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0881 | critic_loss=0.0367 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0184 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0105 | balance_loss=0.0001 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=2.4177 | ema=0.9203 | best_ema=0.9203 | no_improve=0
   🔬 Alpha Diversity: mean=5.92 | std=1.34 | range=[1.39, 13.23] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.16 | JPM=6.43 | JNJ=6.42  BOT: GLD=5.52 | PG=5.08 | MSFT=4.50
   🎛️ Mixture Usage: C0=21.7% | C1=37.3% | C2=41.0%
   🧭 Regime Start Dist (train resets): high_vol=39 (33.6%), low_vol=38 (32.8%), medium_vol=39 (33.6%)
[CYCLE] Update 97/219 | Step 97,776/300,000 | Episode 112 | Time: 11455.2s
   📊 Metrics: Return=+48.76% | Sharpe=1.272 | DD=8.92% | Turnover=30.86%
   🎚️ Intra-Step TAPE: potential=0.2216 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0901 | critic_loss=0.0561 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0280 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0066 | balance_loss=0.0001 | separation_loss=0.0079 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=1.2715 | ema=0.9554 | best_ema=0.9554 | no_improve=0
[CYCLE] Update 98/219 | Step 98,784/300,000 | Episode 112 | Time: 11502.9s
   📊 Metrics: Return=+53.42% | Sharpe=0.854 | DD=21.19% | Turnover=31.08%
   🎚️ Intra-Step TAPE: potential=0.4291 | delta_reward=+0.0015
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0885 | critic_loss=0.0414 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0207 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9995 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8537 | ema=0.9452 | best_ema=0.9452 | no_improve=0
   🔬 Alpha Diversity: mean=5.87 | std=1.30 | range=[1.96, 11.96] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=6.81 | CAT=6.52 | NEE=6.48  BOT: AMZN=5.42 | PG=5.00 | MSFT=4.55
   🎛️ Mixture Usage: C0=20.4% | C1=36.4% | C2=43.2%
   🧭 Regime Start Dist (train resets): high_vol=39 (33.6%), low_vol=38 (32.8%), medium_vol=39 (33.6%)
      🧪 Deterministic validation: Sharpe=0.761 | Return=+55.97% | DD=21.50%
         Multi-horizon: score=0.144 | details=252:-0.407/21.5%, 504:0.317/21.5%, 756:0.656/21.5%, 1008:0.761/21.5%
         SPY relative: spy_return=+41.94% | outperformance=+14.04%
         Equal-weight relative: ew_return=+93.18% | outperformance=-37.21%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-37.21%, required>0.00%).
[CYCLE] Update 99/219 | Step 99,792/300,000 | Episode 116 | Time: 11861.3s
   📊 Metrics: Return=+57.60% | Sharpe=0.806 | DD=11.33% | Turnover=32.01%
   🎚️ Intra-Step TAPE: potential=0.3609 | delta_reward=-0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0924 | critic_loss=0.1134 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0567 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0138 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000030 | critic_lr=0.000150 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.8058 | ema=0.9313 | best_ema=0.9313 | no_improve=0
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.88% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4384
   📈 Benchmark Relative: 1/N shaping=0.002 (EW ret=-0.01873) | SPY shaping=0.001 (SPY ret=-0.01869)
   [TOOL] Actor learning rate adjusted to 0.000020 at step 100,000
   [TOOL] Critic learning rate adjusted to 0.000120 at step 100,000
[CYCLE] Update 100/219 | Step 100,800/300,000 | Episode 116 | Time: 11908.8s
   📊 Metrics: Return=+3.73% | Sharpe=0.082 | DD=8.86% | Turnover=31.95%
   🎚️ Intra-Step TAPE: potential=0.2399 | delta_reward=-0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0903 | critic_loss=0.0311 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0155 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0275 | balance_loss=0.0000 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1008 | batch_size=252 | gamma=0.9900 | gae_lambda=0.9200
   ⏹️ Early-stop monitor: score=0.0825 | ema=0.8464 | best_ema=0.8464 | no_improve=0
   🔬 Alpha Diversity: mean=6.04 | std=1.43 | range=[1.41, 14.12] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: NVDA=7.35 | JNJ=6.77 | JPM=6.67  BOT: PG=5.49 | GLD=5.19 | MSFT=4.57
   🎛️ Mixture Usage: C0=21.4% | C1=37.6% | C2=41.0%
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
   temperature: 0.7000
[CYCLE] Update 101/219 | Step 102,312/300,000 | Episode 116 | Time: 11979.0s
   📊 Metrics: Return=+28.76% | Sharpe=0.585 | DD=11.53% | Turnover=31.77%
   🎚️ Intra-Step TAPE: potential=0.5962 | delta_reward=-0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0930 | critic_loss=0.0850 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0425 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0308 | balance_loss=0.0000 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.5851 | ema=0.8203 | best_ema=0.8464 | no_improve=1
      🧪 Deterministic validation: Sharpe=0.558 | Return=+41.41% | DD=23.78%
         Multi-horizon: score=-0.046 | details=252:-0.619/23.8%, 504:0.183/23.8%, 756:0.459/23.8%, 1008:0.558/23.8%
         SPY relative: spy_return=+41.94% | outperformance=-0.53%
         Equal-weight relative: ew_return=+93.18% | outperformance=-51.77%
         [WARN] SPY gate rejected checkpoint (outperformance=-0.53%, required>0.00%).
[CYCLE] Update 102/219 | Step 103,824/300,000 | Episode 120 | Time: 12361.5s
   📊 Metrics: Return=+26.15% | Sharpe=0.380 | DD=13.05% | Turnover=31.13%
   🎚️ Intra-Step TAPE: potential=0.6698 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0960 | critic_loss=0.0681 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0341 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0141 | balance_loss=0.0001 | separation_loss=0.0078 | component_dispersion_loss=0.0103
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.3798 | ema=0.7762 | best_ema=0.8464 | no_improve=2
   🔬 Alpha Diversity: mean=7.16 | std=1.50 | range=[1.67, 12.82] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: JPM=8.12 | NVDA=8.11 | JNJ=7.90  BOT: GLD=6.50 | PG=6.28 | MSFT=5.68
   🎛️ Mixture Usage: C0=23.5% | C1=35.8% | C2=40.7%
   🧭 Regime Start Dist (train resets): high_vol=42 (33.9%), low_vol=42 (33.9%), medium_vol=40 (32.3%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.15% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.2848
   📈 Benchmark Relative: 1/N shaping=-0.017 (EW ret=0.00759) | SPY shaping=0.009 (SPY ret=0.00366)
[CYCLE] Update 103/219 | Step 105,336/300,000 | Episode 120 | Time: 12430.7s
   📊 Metrics: Return=+68.27% | Sharpe=2.179 | DD=9.24% | Turnover=30.05%
   🎚️ Intra-Step TAPE: potential=0.3462 | delta_reward=+0.0009
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0919 | critic_loss=0.0549 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0274 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9918 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.1791 | ema=0.9165 | best_ema=0.9165 | no_improve=0
[CYCLE] Update 104/219 | Step 106,848/300,000 | Episode 120 | Time: 12499.9s
   📊 Metrics: Return=+67.96% | Sharpe=1.067 | DD=19.16% | Turnover=29.53%
   🎚️ Intra-Step TAPE: potential=0.2459 | delta_reward=-0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0929 | critic_loss=0.0513 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0256 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0175 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0669 | ema=0.9315 | best_ema=0.9315 | no_improve=0
   🔬 Alpha Diversity: mean=6.97 | std=1.36 | range=[2.89, 13.45] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.45 | NEE=7.93 | JNJ=7.51  BOT: PG=6.41 | AMZN=6.17 | MSFT=5.35
   🎛️ Mixture Usage: C0=24.4% | C1=33.0% | C2=42.6%
   🧭 Regime Start Dist (train resets): high_vol=42 (33.9%), low_vol=42 (33.9%), medium_vol=40 (32.3%)
[CYCLE] Update 105/219 | Step 108,360/300,000 | Episode 124 | Time: 12568.9s
   📊 Metrics: Return=+61.20% | Sharpe=0.838 | DD=18.22% | Turnover=29.88%
   🎚️ Intra-Step TAPE: potential=0.2500 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0864 | critic_loss=0.1111 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0556 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0052 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8377 | ema=0.9222 | best_ema=0.9315 | no_improve=1
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 7.30% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4381
   📈 Benchmark Relative: 1/N shaping=0.000 (EW ret=-0.02418) | SPY shaping=0.030 (SPY ret=-0.03007)
[CYCLE] Update 106/219 | Step 109,872/300,000 | Episode 124 | Time: 12638.0s
   📊 Metrics: Return=+26.41% | Sharpe=0.647 | DD=13.35% | Turnover=29.17%
   🎚️ Intra-Step TAPE: potential=0.7540 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0959 | critic_loss=0.0304 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0152 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9625 | balance_loss=0.0002 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6465 | ema=0.8946 | best_ema=0.9315 | no_improve=2
   🔬 Alpha Diversity: mean=6.95 | std=1.34 | range=[2.63, 13.27] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.06 | NEE=7.85 | JPM=7.51  BOT: PG=6.52 | AMZN=5.94 | MSFT=5.47
   🎛️ Mixture Usage: C0=20.5% | C1=29.6% | C2=49.9%
   🧭 Regime Start Dist (train resets): high_vol=44 (34.4%), low_vol=43 (33.6%), medium_vol=41 (32.0%)
      🧪 Deterministic validation: Sharpe=0.775 | Return=+56.44% | DD=17.80%
         Multi-horizon: score=0.197 | details=252:-0.252/17.8%, 504:0.278/17.8%, 756:0.649/17.8%, 1008:0.775/17.8%
         SPY relative: spy_return=+41.94% | outperformance=+14.50%
         Equal-weight relative: ew_return=+93.18% | outperformance=-36.75%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-36.75%, required>0.00%).
[CYCLE] Update 107/219 | Step 111,384/300,000 | Episode 128 | Time: 13021.0s
   📊 Metrics: Return=+51.17% | Sharpe=0.724 | DD=18.82% | Turnover=29.28%
   🎚️ Intra-Step TAPE: potential=0.2274 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0961 | critic_loss=0.0465 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0233 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9832 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7236 | ema=0.8775 | best_ema=0.9315 | no_improve=3
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.81% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3766
   📈 Benchmark Relative: 1/N shaping=0.027 (EW ret=0.00581) | SPY shaping=0.004 (SPY ret=0.00846)
[CYCLE] Update 108/219 | Step 112,896/300,000 | Episode 128 | Time: 13090.3s
   📊 Metrics: Return=+1.74% | Sharpe=-0.018 | DD=11.59% | Turnover=29.32%
   🎚️ Intra-Step TAPE: potential=0.6869 | delta_reward=+0.0010
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0879 | critic_loss=0.0438 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0219 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0119 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=-0.0180 | ema=0.7879 | best_ema=0.9315 | no_improve=4
   🔬 Alpha Diversity: mean=6.99 | std=1.40 | range=[2.42, 13.57] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.07 | NEE=7.80 | NVDA=7.76  BOT: PG=6.57 | AMZN=6.10 | MSFT=5.18
   🎛️ Mixture Usage: C0=21.5% | C1=34.2% | C2=44.3%
   🧭 Regime Start Dist (train resets): high_vol=44 (33.3%), low_vol=44 (33.3%), medium_vol=44 (33.3%)
[CYCLE] Update 109/219 | Step 114,408/300,000 | Episode 128 | Time: 13159.5s
   📊 Metrics: Return=+41.22% | Sharpe=0.847 | DD=11.59% | Turnover=28.94%
   🎚️ Intra-Step TAPE: potential=0.6251 | delta_reward=+0.0011
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0872 | critic_loss=0.0445 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0222 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9922 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8472 | ema=0.7939 | best_ema=0.9315 | no_improve=5
      🧪 Deterministic validation: Sharpe=0.767 | Return=+55.37% | DD=18.06%
         Multi-horizon: score=0.169 | details=252:-0.328/18.1%, 504:0.268/18.1%, 756:0.669/18.1%, 1008:0.767/18.1%
         SPY relative: spy_return=+41.94% | outperformance=+13.43%
         Equal-weight relative: ew_return=+93.18% | outperformance=-37.81%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-37.81%, required>0.00%).
[CYCLE] Update 110/219 | Step 115,920/300,000 | Episode 132 | Time: 13541.6s
   📊 Metrics: Return=+47.03% | Sharpe=0.750 | DD=14.12% | Turnover=29.39%
   🎚️ Intra-Step TAPE: potential=0.2477 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0877 | critic_loss=0.0544 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0272 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9570 | balance_loss=0.0002 | separation_loss=0.0082 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7497 | ema=0.7894 | best_ema=0.9315 | no_improve=6
   🔬 Alpha Diversity: mean=6.97 | std=1.29 | range=[2.71, 12.77] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.26 | NEE=7.70 | NVDA=7.60  BOT: PG=6.43 | AMZN=6.03 | MSFT=5.65
   🎛️ Mixture Usage: C0=18.3% | C1=28.5% | C2=53.2%
   🧭 Regime Start Dist (train resets): high_vol=45 (33.1%), low_vol=45 (33.1%), medium_vol=46 (33.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 5.04% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4012
   📈 Benchmark Relative: 1/N shaping=-0.009 (EW ret=0.01175) | SPY shaping=-0.017 (SPY ret=0.01400)
[CYCLE] Update 111/219 | Step 117,432/300,000 | Episode 132 | Time: 13611.0s
   📊 Metrics: Return=+8.26% | Sharpe=0.227 | DD=7.99% | Turnover=28.90%
   🎚️ Intra-Step TAPE: potential=0.2451 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0895 | critic_loss=0.0448 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0224 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=1.0127 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2269 | ema=0.7332 | best_ema=0.9315 | no_improve=7
[CYCLE] Update 112/219 | Step 118,944/300,000 | Episode 132 | Time: 13680.0s
   📊 Metrics: Return=+36.19% | Sharpe=0.638 | DD=10.54% | Turnover=28.74%
   🎚️ Intra-Step TAPE: potential=0.4579 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0855 | critic_loss=0.0402 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0201 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9999 | balance_loss=0.0001 | separation_loss=0.0082 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6377 | ema=0.7236 | best_ema=0.9315 | no_improve=8
   🔬 Alpha Diversity: mean=6.98 | std=1.30 | range=[2.93, 13.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.56 | NEE=7.88 | NVDA=7.34  BOT: AMZN=6.40 | PG=6.38 | MSFT=5.17
   🎛️ Mixture Usage: C0=21.9% | C1=34.1% | C2=44.0%
   🧭 Regime Start Dist (train resets): high_vol=45 (33.1%), low_vol=45 (33.1%), medium_vol=46 (33.8%)
      🧪 Deterministic validation: Sharpe=0.756 | Return=+55.35% | DD=18.61%
         Multi-horizon: score=0.146 | details=252:-0.397/18.6%, 504:0.295/18.6%, 756:0.647/18.6%, 1008:0.756/18.6%
         SPY relative: spy_return=+41.94% | outperformance=+13.42%
         Equal-weight relative: ew_return=+93.18% | outperformance=-37.83%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-37.83%, required>0.00%).
[CYCLE] Update 113/219 | Step 120,456/300,000 | Episode 136 | Time: 14059.1s
   📊 Metrics: Return=+64.30% | Sharpe=1.010 | DD=12.66% | Turnover=28.79%
   🎚️ Intra-Step TAPE: potential=0.3551 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0923 | critic_loss=0.0457 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0228 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9788 | balance_loss=0.0001 | separation_loss=0.0083 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.0104 | ema=0.7523 | best_ema=0.9315 | no_improve=9
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.01% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5266
   📈 Benchmark Relative: 1/N shaping=0.038 (EW ret=0.00669) | SPY shaping=0.048 (SPY ret=0.00176)
[CYCLE] Update 114/219 | Step 121,968/300,000 | Episode 136 | Time: 14127.7s
   📊 Metrics: Return=+46.64% | Sharpe=1.196 | DD=11.28% | Turnover=28.60%
   🎚️ Intra-Step TAPE: potential=0.6374 | delta_reward=-0.0007
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0876 | critic_loss=0.0215 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0108 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0016
   🧩 Mixture Head: gate_entropy=0.9824 | balance_loss=0.0001 | separation_loss=0.0083 | component_dispersion_loss=0.0106
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.1957 | ema=0.7967 | best_ema=0.9315 | no_improve=10
   🔬 Alpha Diversity: mean=6.91 | std=1.28 | range=[3.24, 14.15] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.60 | NEE=7.72 | NVDA=7.33  BOT: AMZN=6.26 | PG=6.25 | MSFT=5.07
   🎛️ Mixture Usage: C0=19.3% | C1=33.5% | C2=47.2%
   🧭 Regime Start Dist (train resets): high_vol=46 (32.9%), low_vol=46 (32.9%), medium_vol=48 (34.3%)
      🧪 Deterministic validation: Sharpe=0.721 | Return=+51.20% | DD=17.85%
         Multi-horizon: score=0.138 | details=252:-0.329/17.9%, 504:0.205/17.9%, 756:0.642/17.9%, 1008:0.721/17.9%
         SPY relative: spy_return=+41.94% | outperformance=+9.26%
         Equal-weight relative: ew_return=+93.18% | outperformance=-41.98%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-41.98%, required>0.00%).
[CYCLE] Update 115/219 | Step 123,480/300,000 | Episode 140 | Time: 14508.9s
   📊 Metrics: Return=+65.81% | Sharpe=0.676 | DD=28.82% | Turnover=28.16%
   🎚️ Intra-Step TAPE: potential=0.7237 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0912 | critic_loss=0.0765 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0383 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9695 | balance_loss=0.0002 | separation_loss=0.0082 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6764 | ema=0.7846 | best_ema=0.9315 | no_improve=11
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.00% / trig 25.00%) | terminal=0.000 (peak 0.008) | TAPE=0.3286
   📈 Benchmark Relative: 1/N shaping=-0.011 (EW ret=0.00106) | SPY shaping=-0.000 (SPY ret=-0.00024)
[CYCLE] Update 116/219 | Step 124,992/300,000 | Episode 140 | Time: 14577.7s
   📊 Metrics: Return=+42.33% | Sharpe=2.364 | DD=3.41% | Turnover=27.68%
   🎚️ Intra-Step TAPE: potential=0.7525 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0978 | critic_loss=0.0508 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0254 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9398 | balance_loss=0.0003 | separation_loss=0.0082 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=2.3635 | ema=0.9425 | best_ema=0.9425 | no_improve=0
   🔬 Alpha Diversity: mean=6.73 | std=1.37 | range=[2.21, 13.40] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.00 | NVDA=7.25 | JNJ=7.17  BOT: AMZN=6.66 | PG=6.04 | MSFT=4.97
   🎛️ Mixture Usage: C0=18.9% | C1=28.5% | C2=52.6%
   🧭 Regime Start Dist (train resets): high_vol=48 (33.3%), low_vol=48 (33.3%), medium_vol=48 (33.3%)
[CYCLE] Update 117/219 | Step 126,504/300,000 | Episode 140 | Time: 14646.5s
   📊 Metrics: Return=+43.55% | Sharpe=0.865 | DD=17.59% | Turnover=27.38%
   🎚️ Intra-Step TAPE: potential=0.2839 | delta_reward=-0.0012
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0945 | critic_loss=0.0696 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0348 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9539 | balance_loss=0.0002 | separation_loss=0.0082 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8648 | ema=0.9348 | best_ema=0.9425 | no_improve=1
[CYCLE] Update 118/219 | Step 128,016/300,000 | Episode 144 | Time: 14715.5s
   📊 Metrics: Return=+63.29% | Sharpe=0.916 | DD=18.59% | Turnover=27.61%
   🎚️ Intra-Step TAPE: potential=0.6784 | delta_reward=+0.0006
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0936 | critic_loss=0.0587 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0294 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9524 | balance_loss=0.0002 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9159 | ema=0.9329 | best_ema=0.9425 | no_improve=2
   🔬 Alpha Diversity: mean=6.82 | std=1.35 | range=[2.24, 14.09] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.33 | JNJ=7.38 | XOM=7.37  BOT: AMZN=6.23 | PG=6.12 | MSFT=5.02
   🎛️ Mixture Usage: C0=17.3% | C1=29.9% | C2=52.8%
   🧭 Regime Start Dist (train resets): high_vol=48 (32.4%), low_vol=50 (33.8%), medium_vol=50 (33.8%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 1.34% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4673
   📈 Benchmark Relative: 1/N shaping=-0.010 (EW ret=0.01060) | SPY shaping=0.004 (SPY ret=0.00862)
[CYCLE] Update 119/219 | Step 129,528/300,000 | Episode 144 | Time: 14784.2s
   📊 Metrics: Return=+39.09% | Sharpe=1.405 | DD=8.58% | Turnover=27.87%
   🎚️ Intra-Step TAPE: potential=0.5211 | delta_reward=+0.0004
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0893 | critic_loss=0.0238 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0119 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9812 | balance_loss=0.0001 | separation_loss=0.0080 | component_dispersion_loss=0.0104
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.4052 | ema=0.9801 | best_ema=0.9801 | no_improve=0
[CYCLE] Update 120/219 | Step 131,040/300,000 | Episode 144 | Time: 14853.5s
   📊 Metrics: Return=+18.97% | Sharpe=0.266 | DD=24.69% | Turnover=28.13%
   🎚️ Intra-Step TAPE: potential=0.2001 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0918 | critic_loss=0.0255 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0128 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9576 | balance_loss=0.0002 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.2657 | ema=0.9087 | best_ema=0.9801 | no_improve=1
   🔬 Alpha Diversity: mean=6.79 | std=1.39 | range=[2.02, 13.79] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.03 | NEE=7.45 | XOM=7.42  BOT: AMZN=6.15 | PG=6.03 | MSFT=4.89
   🎛️ Mixture Usage: C0=18.8% | C1=30.4% | C2=50.9%
   🧭 Regime Start Dist (train resets): high_vol=48 (32.4%), low_vol=50 (33.8%), medium_vol=50 (33.8%)
      🧪 Deterministic validation: Sharpe=0.603 | Return=+43.19% | DD=19.22%
         Multi-horizon: score=0.002 | details=252:-0.480/19.2%, 504:0.097/19.2%, 756:0.494/19.2%, 1008:0.603/19.2%
         SPY relative: spy_return=+41.94% | outperformance=+1.26%
         Equal-weight relative: ew_return=+93.18% | outperformance=-49.99%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-49.99%, required>0.00%).
[CYCLE] Update 121/219 | Step 132,552/300,000 | Episode 148 | Time: 15232.4s
   📊 Metrics: Return=+61.85% | Sharpe=0.958 | DD=11.93% | Turnover=29.03%
   🎚️ Intra-Step TAPE: potential=0.5200 | delta_reward=-0.0002
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0930 | critic_loss=0.1119 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0559 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9878 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9584 | ema=0.9136 | best_ema=0.9801 | no_improve=2
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.56% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.5124
   📈 Benchmark Relative: 1/N shaping=0.046 (EW ret=-0.03983) | SPY shaping=0.039 (SPY ret=-0.04182)
[CYCLE] Update 122/219 | Step 134,064/300,000 | Episode 148 | Time: 15301.5s
   📊 Metrics: Return=+67.22% | Sharpe=1.622 | DD=9.71% | Turnover=28.40%
   🎚️ Intra-Step TAPE: potential=0.2270 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0948 | critic_loss=0.0199 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0100 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9704 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=1.6215 | ema=0.9844 | best_ema=0.9801 | no_improve=3
   🔬 Alpha Diversity: mean=6.80 | std=1.39 | range=[2.33, 13.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.38 | JNJ=7.44 | NEE=7.15  BOT: PG=6.44 | AMZN=6.18 | MSFT=4.93
   🎛️ Mixture Usage: C0=18.1% | C1=36.3% | C2=45.6%
   🧭 Regime Start Dist (train resets): high_vol=51 (33.6%), low_vol=51 (33.6%), medium_vol=50 (32.9%)
      🧪 Deterministic validation: Sharpe=0.708 | Return=+52.17% | DD=21.70%
         Multi-horizon: score=0.000 | details=252:-0.584/21.7%, 504:0.133/21.7%, 756:0.566/21.7%, 1008:0.708/21.7%
         SPY relative: spy_return=+41.94% | outperformance=+10.23%
         Equal-weight relative: ew_return=+93.18% | outperformance=-41.01%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-41.01%, required>0.00%).
[CYCLE] Update 123/219 | Step 135,576/300,000 | Episode 152 | Time: 15682.2s
   📊 Metrics: Return=+67.87% | Sharpe=0.697 | DD=25.12% | Turnover=28.57%
   🎚️ Intra-Step TAPE: potential=0.2521 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0811 | critic_loss=0.0439 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0220 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9876 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6970 | ema=0.9557 | best_ema=0.9801 | no_improve=4
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 2.71% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.3530
   📈 Benchmark Relative: 1/N shaping=-0.005 (EW ret=0.00305) | SPY shaping=-0.001 (SPY ret=0.00267)
[CYCLE] Update 124/219 | Step 137,088/300,000 | Episode 152 | Time: 15751.0s
   📊 Metrics: Return=+13.16% | Sharpe=0.611 | DD=6.62% | Turnover=29.31%
   🎚️ Intra-Step TAPE: potential=0.5773 | delta_reward=+0.0005
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0898 | critic_loss=0.0345 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0173 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9850 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.6106 | ema=0.9212 | best_ema=0.9801 | no_improve=5
   🔬 Alpha Diversity: mean=6.77 | std=1.37 | range=[2.00, 13.32] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.22 | NVDA=7.33 | JNJ=7.27  BOT: AMZN=6.45 | PG=6.34 | MSFT=5.07
   🎛️ Mixture Usage: C0=20.4% | C1=41.4% | C2=38.2%
   🧭 Regime Start Dist (train resets): high_vol=52 (33.3%), low_vol=52 (33.3%), medium_vol=52 (33.3%)
[CYCLE] Update 125/219 | Step 138,600/300,000 | Episode 152 | Time: 15820.0s
   📊 Metrics: Return=+4.46% | Sharpe=0.005 | DD=15.84% | Turnover=29.12%
   🎚️ Intra-Step TAPE: potential=0.2445 | delta_reward=-0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0954 | critic_loss=0.0338 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0169 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9736 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.0053 | ema=0.8296 | best_ema=0.9801 | no_improve=6
      🧪 Deterministic validation: Sharpe=0.683 | Return=+50.15% | DD=23.14%
         Multi-horizon: score=-0.037 | details=252:-0.634/23.1%, 504:0.118/23.1%, 756:0.524/23.1%, 1008:0.683/23.1%
         SPY relative: spy_return=+41.94% | outperformance=+8.22%
         Equal-weight relative: ew_return=+93.18% | outperformance=-43.03%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-43.03%, required>0.00%).

📚 TURNOVER CURRICULUM UPDATE at 140,112 steps:
   Turnover penalty scalar: 0.2

🎛️ EXECUTION BETA UPDATE at 140,112 steps:
   action_execution_beta: 0.800 (w_exec=(1-β)w_prev + βw_raw)
[CYCLE] Update 126/219 | Step 140,112/300,000 | Episode 156 | Time: 16200.2s
   📊 Metrics: Return=+58.60% | Sharpe=0.828 | DD=18.32% | Turnover=28.72%
   🎚️ Intra-Step TAPE: potential=0.2996 | delta_reward=+0.0001
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0948 | critic_loss=0.0340 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0170 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9770 | balance_loss=0.0001 | separation_loss=0.0082 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.8280 | ema=0.8294 | best_ema=0.9801 | no_improve=7
   🔬 Alpha Diversity: mean=6.70 | std=1.25 | range=[2.28, 13.64] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.27 | NEE=7.21 | GLD=7.21  BOT: PG=6.25 | AMZN=6.05 | MSFT=4.84
   🎛️ Mixture Usage: C0=20.0% | C1=40.2% | C2=39.8%
   🧭 Regime Start Dist (train resets): high_vol=55 (34.4%), low_vol=52 (32.5%), medium_vol=53 (33.1%)
   🔒 Drawdown λ snapshot=0.000 (peak 0.000, dd 0.87% / trig 25.00%) | terminal=0.000 (peak 0.000) | TAPE=0.4321
   📈 Benchmark Relative: 1/N shaping=-0.014 (EW ret=0.00867) | SPY shaping=-0.005 (SPY ret=0.00788)
[CYCLE] Update 127/219 | Step 141,624/300,000 | Episode 156 | Time: 16268.9s
   📊 Metrics: Return=+31.46% | Sharpe=0.974 | DD=10.08% | Turnover=34.72%
   🎚️ Intra-Step TAPE: potential=0.6253 | delta_reward=+0.0016
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0903 | critic_loss=0.0236 | mean_adv=0.0000
   🧮 Loss Detail: critic_scaled=0.0118 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9735 | balance_loss=0.0001 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.9736 | ema=0.8439 | best_ema=0.9801 | no_improve=8
[CYCLE] Update 128/219 | Step 143,136/300,000 | Episode 156 | Time: 16338.3s
   📊 Metrics: Return=+42.99% | Sharpe=0.731 | DD=11.87% | Turnover=35.55%
   🎚️ Intra-Step TAPE: potential=0.2243 | delta_reward=+0.0000
   🎯 Profile: BalancedGrowth
   [BRAIN] Training: actor_loss=0.0878 | critic_loss=0.0213 | mean_adv=-0.0000
   🧮 Loss Detail: critic_scaled=0.0106 | risk_aux_total=0.0000 | sharpe_proxy=0.0000 | sharpe_loss=0.0000 | mvo_loss=0.0000 | cvar_proxy=0.0000 | cvar_loss=0.0000 | cvar_coef=0.0000 | hhi_loss=0.0005 | dispersion_loss=0.0015
   🧩 Mixture Head: gate_entropy=0.9516 | balance_loss=0.0002 | separation_loss=0.0081 | component_dispersion_loss=0.0105
   ⚙️ Optimizer: actor_lr=0.000020 | critic_lr=0.000120 | target_kl=0.0000 | rollout=1512 | batch_size=336 | gamma=0.9950 | gae_lambda=0.9500
   ⏹️ Early-stop monitor: score=0.7315 | ema=0.8326 | best_ema=0.9801 | no_improve=9
   🔬 Alpha Diversity: mean=6.54 | std=1.33 | range=[1.99, 13.42] | cap_hit=0.0%
   🏷️ Alpha Per-Asset  TOP: CAT=8.17 | NEE=7.39 | GLD=7.30  BOT: AMZN=6.38 | XOM=6.33 | MSFT=4.58
   🎛️ Mixture Usage: C0=18.5% | C1=37.8% | C2=43.8%
   🧭 Regime Start Dist (train resets): high_vol=55 (34.4%), low_vol=52 (32.5%), medium_vol=53 (33.1%)
      🧪 Deterministic validation: Sharpe=0.610 | Return=+43.53% | DD=19.65%
         Multi-horizon: score=-0.010 | details=252:-0.474/19.6%, 504:0.068/19.6%, 756:0.466/19.6%, 1008:0.610/19.6%
         SPY relative: spy_return=+41.94% | outperformance=+1.59%
         Equal-weight relative: ew_return=+93.18% | outperformance=-49.65%
         [WARN] Equal-weight gate rejected checkpoint (outperformance=-49.65%, required>0.00%).