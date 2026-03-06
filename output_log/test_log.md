[LOOK] Stage 1/2: deterministic sweep (no stochastic during sweep)

[1/5] Sweep checkpoint: high_watermark__ep0374__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $112,859.47
   Total Return: +12.86%
   Annualized Return: +12.86%
   Sharpe Ratio: 0.4793 (annualized)
   Sortino Ratio: 0.5757 (annualized)
   Max Drawdown: 31.07%
   Volatility (Ann.): 31.62%
   Turnover: 0.56%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.304, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $151,715.27
   Total Return: +51.72%
   Annualized Return: +51.72%
   Sharpe Ratio: 2.2833 (annualized)
   Sortino Ratio: 3.1152 (annualized)
   Max Drawdown: 8.15%
   Volatility (Ann.): 18.20%
   Turnover: 0.46%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.282, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $137,358.06
   Total Return: +37.36%
   Annualized Return: +37.36%
   Sharpe Ratio: 2.2922 (annualized)
   Sortino Ratio: 3.0817 (annualized)
   Max Drawdown: 8.04%
   Volatility (Ann.): 13.44%
   Turnover: 0.40%
   Win Rate: 60.16%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.440, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $133,027.01
   Total Return: +33.03%
   Annualized Return: +33.03%
   Sharpe Ratio: 2.4030 (annualized)
   Sortino Ratio: 3.1793 (annualized)
   Max Drawdown: 5.07%
   Volatility (Ann.): 11.37%
   Turnover: 0.32%
   Win Rate: 58.96%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.643, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $150,827.45
   Total Return: +50.83%
   Annualized Return: +22.81%
   Sharpe Ratio: 0.9032 (annualized)
   Sortino Ratio: 1.0308 (annualized)
   Max Drawdown: 31.07%
   Volatility (Ann.): 23.73%
   Turnover: 0.43%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.458, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $179,441.59
   Total Return: +79.44%
   Annualized Return: +33.96%
   Sharpe Ratio: 1.8714 (annualized)
   Sortino Ratio: 2.6061 (annualized)
   Max Drawdown: 8.86%
   Volatility (Ann.): 15.22%
   Turnover: 0.41%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.467, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $146,742.32
   Total Return: +46.74%
   Annualized Return: +21.14%
   Sharpe Ratio: 1.2935 (annualized)
   Sortino Ratio: 1.7705 (annualized)
   Max Drawdown: 11.63%
   Volatility (Ann.): 14.10%
   Turnover: 0.39%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.501, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $132,166.30
   Total Return: +32.17%
   Annualized Return: +14.96%
   Sharpe Ratio: 0.8873 (annualized)
   Sortino Ratio: 1.3158 (annualized)
   Max Drawdown: 13.51%
   Volatility (Ann.): 14.74%
   Turnover: 0.38%
   Win Rate: 53.28%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.515, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $149,851.56
   Total Return: +49.85%
   Annualized Return: +14.43%
   Sharpe Ratio: 0.6370 (annualized)
   Sortino Ratio: 0.7919 (annualized)
   Max Drawdown: 31.07%
   Volatility (Ann.): 21.83%
   Turnover: 0.43%
   Win Rate: 54.57%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.434, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $181,019.10
   Total Return: +81.02%
   Annualized Return: +21.87%
   Sharpe Ratio: 1.1985 (annualized)
   Sortino Ratio: 1.7529 (annualized)
   Max Drawdown: 13.51%
   Volatility (Ann.): 15.94%
   Turnover: 0.41%
   Win Rate: 55.23%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.412, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $163,361.96
   Total Return: +63.36%
   Annualized Return: +17.77%
   Sharpe Ratio: 1.0805 (annualized)
   Sortino Ratio: 1.5992 (annualized)
   Max Drawdown: 13.51%
   Volatility (Ann.): 14.28%
   Turnover: 0.39%
   Win Rate: 54.44%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.435, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $145,881.60
   Total Return: +45.88%
   Annualized Return: +13.41%
   Sharpe Ratio: 0.8552 (annualized)
   Sortino Ratio: 1.2863 (annualized)
   Max Drawdown: 13.51%
   Volatility (Ann.): 13.49%
   Turnover: 0.38%
   Win Rate: 53.77%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.470, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $165,402.12
   Total Return: +65.40%
   Annualized Return: +13.41%
   Sharpe Ratio: 0.6391 (annualized)
   Sortino Ratio: 0.7982 (annualized)
   Max Drawdown: 31.07%
   Volatility (Ann.): 19.62%
   Turnover: 0.42%
   Win Rate: 54.62%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.420, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $213,045.31
   Total Return: +113.05%
   Annualized Return: +20.81%
   Sharpe Ratio: 1.2395 (annualized)
   Sortino Ratio: 1.7992 (annualized)
   Max Drawdown: 13.51%
   Volatility (Ann.): 14.53%
   Turnover: 0.39%
   Win Rate: 55.21%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.404, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $192,197.73
   Total Return: +92.20%
   Annualized Return: +17.74%
   Sharpe Ratio: 1.1592 (annualized)
   Sortino Ratio: 1.6931 (annualized)
   Max Drawdown: 13.51%
   Volatility (Ann.): 13.15%
   Turnover: 0.38%
   Win Rate: 55.11%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.426, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00374_shp1p215_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $166,920.81
   Total Return: +66.92%
   Annualized Return: +13.67%
   Sharpe Ratio: 0.9294 (annualized)
   Sortino Ratio: 1.3631 (annualized)
   Max Drawdown: 13.51%
   Volatility (Ann.): 12.51%
   Turnover: 0.36%
   Win Rate: 53.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.457, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[2/5] Sweep checkpoint: high_watermark__ep0396__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $113,314.11
   Total Return: +13.31%
   Annualized Return: +13.31%
   Sharpe Ratio: 0.4911 (annualized)
   Sortino Ratio: 0.5920 (annualized)
   Max Drawdown: 31.10%
   Volatility (Ann.): 31.79%
   Turnover: 0.51%
   Win Rate: 56.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.117, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $152,326.51
   Total Return: +52.33%
   Annualized Return: +52.33%
   Sharpe Ratio: 2.2846 (annualized)
   Sortino Ratio: 3.1203 (annualized)
   Max Drawdown: 8.20%
   Volatility (Ann.): 18.38%
   Turnover: 0.40%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.065, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $137,981.70
   Total Return: +37.98%
   Annualized Return: +37.98%
   Sharpe Ratio: 2.3074 (annualized)
   Sortino Ratio: 3.1118 (annualized)
   Max Drawdown: 8.14%
   Volatility (Ann.): 13.56%
   Turnover: 0.34%
   Win Rate: 59.36%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.080, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $132,951.31
   Total Return: +32.95%
   Annualized Return: +32.95%
   Sharpe Ratio: 2.3880 (annualized)
   Sortino Ratio: 3.1650 (annualized)
   Max Drawdown: 5.07%
   Volatility (Ann.): 11.42%
   Turnover: 0.31%
   Win Rate: 58.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.137, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $151,644.97
   Total Return: +51.64%
   Annualized Return: +23.14%
   Sharpe Ratio: 0.9112 (annualized)
   Sortino Ratio: 1.0434 (annualized)
   Max Drawdown: 31.10%
   Volatility (Ann.): 23.85%
   Turnover: 0.40%
   Win Rate: 57.65%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.122, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $180,250.00
   Total Return: +80.25%
   Annualized Return: +34.26%
   Sharpe Ratio: 1.8717 (annualized)
   Sortino Ratio: 2.6064 (annualized)
   Max Drawdown: 8.87%
   Volatility (Ann.): 15.35%
   Turnover: 0.36%
   Win Rate: 57.85%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.128, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $147,151.69
   Total Return: +47.15%
   Annualized Return: +21.31%
   Sharpe Ratio: 1.2956 (annualized)
   Sortino Ratio: 1.7720 (annualized)
   Max Drawdown: 11.56%
   Volatility (Ann.): 14.19%
   Turnover: 0.34%
   Win Rate: 56.26%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.154, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $132,282.10
   Total Return: +32.28%
   Annualized Return: +15.01%
   Sharpe Ratio: 0.8856 (annualized)
   Sortino Ratio: 1.3108 (annualized)
   Max Drawdown: 13.48%
   Volatility (Ann.): 14.84%
   Turnover: 0.34%
   Win Rate: 52.68%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.189, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $150,881.67
   Total Return: +50.88%
   Annualized Return: +14.70%
   Sharpe Ratio: 0.6451 (annualized)
   Sortino Ratio: 0.8042 (annualized)
   Max Drawdown: 31.10%
   Volatility (Ann.): 21.95%
   Turnover: 0.39%
   Win Rate: 54.04%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.162, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $182,352.05
   Total Return: +82.35%
   Annualized Return: +22.17%
   Sharpe Ratio: 1.2054 (annualized)
   Sortino Ratio: 1.7619 (annualized)
   Max Drawdown: 13.48%
   Volatility (Ann.): 16.07%
   Turnover: 0.36%
   Win Rate: 54.83%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.156, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $164,562.41
   Total Return: +64.56%
   Annualized Return: +18.06%
   Sharpe Ratio: 1.0908 (annualized)
   Sortino Ratio: 1.6143 (annualized)
   Max Drawdown: 13.48%
   Volatility (Ann.): 14.38%
   Turnover: 0.34%
   Win Rate: 54.04%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.163, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $146,525.04
   Total Return: +46.53%
   Annualized Return: +13.58%
   Sharpe Ratio: 0.8624 (annualized)
   Sortino Ratio: 1.2941 (annualized)
   Max Drawdown: 13.48%
   Volatility (Ann.): 13.56%
   Turnover: 0.34%
   Win Rate: 53.25%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.156, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $167,127.24
   Total Return: +67.13%
   Annualized Return: +13.70%
   Sharpe Ratio: 0.6500 (annualized)
   Sortino Ratio: 0.8136 (annualized)
   Max Drawdown: 31.10%
   Volatility (Ann.): 19.73%
   Turnover: 0.38%
   Win Rate: 54.12%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.144, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $215,202.32
   Total Return: +115.20%
   Annualized Return: +21.12%
   Sharpe Ratio: 1.2489 (annualized)
   Sortino Ratio: 1.8113 (annualized)
   Max Drawdown: 13.48%
   Volatility (Ann.): 14.63%
   Turnover: 0.35%
   Win Rate: 55.01%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.130, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $194,072.42
   Total Return: +94.07%
   Annualized Return: +18.03%
   Sharpe Ratio: 1.1715 (annualized)
   Sortino Ratio: 1.7098 (annualized)
   Max Drawdown: 13.48%
   Volatility (Ann.): 13.22%
   Turnover: 0.33%
   Win Rate: 54.92%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.131, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00396_shp1p102_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $167,337.97
   Total Return: +67.34%
   Annualized Return: +13.74%
   Sharpe Ratio: 0.9303 (annualized)
   Sortino Ratio: 1.3631 (annualized)
   Max Drawdown: 13.48%
   Volatility (Ann.): 12.57%
   Turnover: 0.32%
   Win Rate: 53.62%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.117, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[3/5] Sweep checkpoint: high_watermark__ep0398__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $113,289.62
   Total Return: +13.29%
   Annualized Return: +13.29%
   Sharpe Ratio: 0.4902 (annualized)
   Sortino Ratio: 0.5918 (annualized)
   Max Drawdown: 31.13%
   Volatility (Ann.): 31.84%
   Turnover: 0.51%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.087, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $152,791.19
   Total Return: +52.79%
   Annualized Return: +52.79%
   Sharpe Ratio: 2.2968 (annualized)
   Sortino Ratio: 3.1388 (annualized)
   Max Drawdown: 8.22%
   Volatility (Ann.): 18.42%
   Turnover: 0.39%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.039, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $138,426.43
   Total Return: +38.43%
   Annualized Return: +38.43%
   Sharpe Ratio: 2.3248 (annualized)
   Sortino Ratio: 3.1417 (annualized)
   Max Drawdown: 8.16%
   Volatility (Ann.): 13.60%
   Turnover: 0.33%
   Win Rate: 59.76%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.054, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $133,210.77
   Total Return: +33.21%
   Annualized Return: +33.21%
   Sharpe Ratio: 2.4007 (annualized)
   Sortino Ratio: 3.1820 (annualized)
   Max Drawdown: 5.07%
   Volatility (Ann.): 11.45%
   Turnover: 0.30%
   Win Rate: 59.36%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.110, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $151,959.07
   Total Return: +51.96%
   Annualized Return: +23.27%
   Sharpe Ratio: 0.9145 (annualized)
   Sortino Ratio: 1.0446 (annualized)
   Max Drawdown: 31.13%
   Volatility (Ann.): 23.89%
   Turnover: 0.39%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.096, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $180,884.59
   Total Return: +80.88%
   Annualized Return: +34.49%
   Sharpe Ratio: 1.8803 (annualized)
   Sortino Ratio: 2.6188 (annualized)
   Max Drawdown: 8.84%
   Volatility (Ann.): 15.37%
   Turnover: 0.36%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.091, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $147,655.57
   Total Return: +47.66%
   Annualized Return: +21.51%
   Sharpe Ratio: 1.3058 (annualized)
   Sortino Ratio: 1.7867 (annualized)
   Max Drawdown: 11.53%
   Volatility (Ann.): 14.22%
   Turnover: 0.33%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.119, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $132,621.14
   Total Return: +32.62%
   Annualized Return: +15.16%
   Sharpe Ratio: 0.8929 (annualized)
   Sortino Ratio: 1.3224 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.86%
   Turnover: 0.34%
   Win Rate: 53.08%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.149, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $151,286.45
   Total Return: +51.29%
   Annualized Return: +14.80%
   Sharpe Ratio: 0.6485 (annualized)
   Sortino Ratio: 0.8075 (annualized)
   Max Drawdown: 31.13%
   Volatility (Ann.): 21.99%
   Turnover: 0.39%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.127, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $183,262.17
   Total Return: +83.26%
   Annualized Return: +22.37%
   Sharpe Ratio: 1.2136 (annualized)
   Sortino Ratio: 1.7751 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 16.10%
   Turnover: 0.36%
   Win Rate: 55.10%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.119, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $165,470.33
   Total Return: +65.47%
   Annualized Return: +18.28%
   Sharpe Ratio: 1.1014 (annualized)
   Sortino Ratio: 1.6322 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.41%
   Turnover: 0.34%
   Win Rate: 54.44%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.124, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $147,250.54
   Total Return: +47.25%
   Annualized Return: +13.77%
   Sharpe Ratio: 0.8732 (annualized)
   Sortino Ratio: 1.3113 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 13.58%
   Turnover: 0.34%
   Win Rate: 53.64%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.116, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $167,974.82
   Total Return: +67.97%
   Annualized Return: +13.84%
   Sharpe Ratio: 0.6556 (annualized)
   Sortino Ratio: 0.8195 (annualized)
   Max Drawdown: 31.13%
   Volatility (Ann.): 19.76%
   Turnover: 0.37%
   Win Rate: 54.42%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.108, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $216,665.62
   Total Return: +116.67%
   Annualized Return: +21.32%
   Sharpe Ratio: 1.2583 (annualized)
   Sortino Ratio: 1.8256 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.66%
   Turnover: 0.35%
   Win Rate: 55.31%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.096, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $195,342.80
   Total Return: +95.34%
   Annualized Return: +18.22%
   Sharpe Ratio: 1.1815 (annualized)
   Sortino Ratio: 1.7261 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 13.25%
   Turnover: 0.33%
   Win Rate: 55.21%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.099, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00398_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $168,220.38
   Total Return: +68.22%
   Annualized Return: +13.89%
   Sharpe Ratio: 0.9392 (annualized)
   Sortino Ratio: 1.3766 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 12.60%
   Turnover: 0.32%
   Win Rate: 53.92%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.087, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[4/5] Sweep checkpoint: high_watermark__ep0408__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $113,822.04
   Total Return: +13.82%
   Annualized Return: +13.82%
   Sharpe Ratio: 0.5047 (annualized)
   Sortino Ratio: 0.6100 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 31.88%
   Turnover: 0.49%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.062, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $153,083.62
   Total Return: +53.08%
   Annualized Return: +53.08%
   Sharpe Ratio: 2.2994 (annualized)
   Sortino Ratio: 3.1445 (annualized)
   Max Drawdown: 8.23%
   Volatility (Ann.): 18.49%
   Turnover: 0.37%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.016, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $138,580.48
   Total Return: +38.58%
   Annualized Return: +38.58%
   Sharpe Ratio: 2.3292 (annualized)
   Sortino Ratio: 3.1521 (annualized)
   Max Drawdown: 8.16%
   Volatility (Ann.): 13.62%
   Turnover: 0.31%
   Win Rate: 59.76%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.021, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $133,098.07
   Total Return: +33.10%
   Annualized Return: +33.10%
   Sharpe Ratio: 2.3920 (annualized)
   Sortino Ratio: 3.1729 (annualized)
   Max Drawdown: 5.04%
   Volatility (Ann.): 11.45%
   Turnover: 0.29%
   Win Rate: 59.36%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.080, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $152,618.88
   Total Return: +52.62%
   Annualized Return: +23.54%
   Sharpe Ratio: 0.9228 (annualized)
   Sortino Ratio: 1.0551 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 23.92%
   Turnover: 0.38%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.071, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $181,385.87
   Total Return: +81.39%
   Annualized Return: +34.68%
   Sharpe Ratio: 1.8848 (annualized)
   Sortino Ratio: 2.6243 (annualized)
   Max Drawdown: 8.78%
   Volatility (Ann.): 15.42%
   Turnover: 0.34%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.050, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $147,857.01
   Total Return: +47.86%
   Annualized Return: +21.60%
   Sharpe Ratio: 1.3092 (annualized)
   Sortino Ratio: 1.7903 (annualized)
   Max Drawdown: 11.50%
   Volatility (Ann.): 14.23%
   Turnover: 0.32%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.068, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $132,682.88
   Total Return: +32.68%
   Annualized Return: +15.19%
   Sharpe Ratio: 0.8932 (annualized)
   Sortino Ratio: 1.3225 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.89%
   Turnover: 0.33%
   Win Rate: 53.08%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.090, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $152,142.80
   Total Return: +52.14%
   Annualized Return: +15.01%
   Sharpe Ratio: 0.6564 (annualized)
   Sortino Ratio: 0.8180 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 22.02%
   Turnover: 0.37%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.081, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $183,923.97
   Total Return: +83.92%
   Annualized Return: +22.52%
   Sharpe Ratio: 1.2182 (annualized)
   Sortino Ratio: 1.7820 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 16.15%
   Turnover: 0.34%
   Win Rate: 55.10%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.070, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $165,888.50
   Total Return: +65.89%
   Annualized Return: +18.38%
   Sharpe Ratio: 1.1055 (annualized)
   Sortino Ratio: 1.6383 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.44%
   Turnover: 0.33%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.072, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $147,375.79
   Total Return: +47.38%
   Annualized Return: +13.80%
   Sharpe Ratio: 0.8742 (annualized)
   Sortino Ratio: 1.3123 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 13.60%
   Turnover: 0.33%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.068, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $168,990.63
   Total Return: +68.99%
   Annualized Return: +14.02%
   Sharpe Ratio: 0.6626 (annualized)
   Sortino Ratio: 0.8292 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 19.79%
   Turnover: 0.36%
   Win Rate: 54.32%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.067, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $217,181.29
   Total Return: +117.18%
   Annualized Return: +21.40%
   Sharpe Ratio: 1.2596 (annualized)
   Sortino Ratio: 1.8274 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.70%
   Turnover: 0.33%
   Win Rate: 55.21%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.055, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $195,702.30
   Total Return: +95.70%
   Annualized Return: +18.28%
   Sharpe Ratio: 1.1834 (annualized)
   Sortino Ratio: 1.7289 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 13.27%
   Turnover: 0.31%
   Win Rate: 55.11%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.057, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $168,379.53
   Total Return: +68.38%
   Annualized Return: +13.91%
   Sharpe Ratio: 0.9402 (annualized)
   Sortino Ratio: 1.3778 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 12.61%
   Turnover: 0.31%
   Win Rate: 53.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.051, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[5/5] Sweep checkpoint: high_watermark__ep0409__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $113,822.04
   Total Return: +13.82%
   Annualized Return: +13.82%
   Sharpe Ratio: 0.5047 (annualized)
   Sortino Ratio: 0.6100 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 31.88%
   Turnover: 0.49%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.062, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $153,083.62
   Total Return: +53.08%
   Annualized Return: +53.08%
   Sharpe Ratio: 2.2994 (annualized)
   Sortino Ratio: 3.1445 (annualized)
   Max Drawdown: 8.23%
   Volatility (Ann.): 18.49%
   Turnover: 0.37%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.016, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $138,580.48
   Total Return: +38.58%
   Annualized Return: +38.58%
   Sharpe Ratio: 2.3292 (annualized)
   Sortino Ratio: 3.1521 (annualized)
   Max Drawdown: 8.16%
   Volatility (Ann.): 13.62%
   Turnover: 0.31%
   Win Rate: 59.76%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.021, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $133,098.07
   Total Return: +33.10%
   Annualized Return: +33.10%
   Sharpe Ratio: 2.3920 (annualized)
   Sortino Ratio: 3.1729 (annualized)
   Max Drawdown: 5.04%
   Volatility (Ann.): 11.45%
   Turnover: 0.29%
   Win Rate: 59.36%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.080, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $152,618.88
   Total Return: +52.62%
   Annualized Return: +23.54%
   Sharpe Ratio: 0.9228 (annualized)
   Sortino Ratio: 1.0551 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 23.92%
   Turnover: 0.38%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.071, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $181,385.87
   Total Return: +81.39%
   Annualized Return: +34.68%
   Sharpe Ratio: 1.8848 (annualized)
   Sortino Ratio: 2.6243 (annualized)
   Max Drawdown: 8.78%
   Volatility (Ann.): 15.42%
   Turnover: 0.34%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.050, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $147,857.01
   Total Return: +47.86%
   Annualized Return: +21.60%
   Sharpe Ratio: 1.3092 (annualized)
   Sortino Ratio: 1.7903 (annualized)
   Max Drawdown: 11.50%
   Volatility (Ann.): 14.23%
   Turnover: 0.32%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.068, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $132,682.88
   Total Return: +32.68%
   Annualized Return: +15.19%
   Sharpe Ratio: 0.8932 (annualized)
   Sortino Ratio: 1.3225 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.89%
   Turnover: 0.33%
   Win Rate: 53.08%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.090, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $152,142.80
   Total Return: +52.14%
   Annualized Return: +15.01%
   Sharpe Ratio: 0.6564 (annualized)
   Sortino Ratio: 0.8180 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 22.02%
   Turnover: 0.37%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.081, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $183,923.97
   Total Return: +83.92%
   Annualized Return: +22.52%
   Sharpe Ratio: 1.2182 (annualized)
   Sortino Ratio: 1.7820 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 16.15%
   Turnover: 0.34%
   Win Rate: 55.10%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.070, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $165,888.50
   Total Return: +65.89%
   Annualized Return: +18.38%
   Sharpe Ratio: 1.1055 (annualized)
   Sortino Ratio: 1.6383 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.44%
   Turnover: 0.33%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.072, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $147,375.79
   Total Return: +47.38%
   Annualized Return: +13.80%
   Sharpe Ratio: 0.8742 (annualized)
   Sortino Ratio: 1.3123 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 13.60%
   Turnover: 0.33%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.068, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $168,990.63
   Total Return: +68.99%
   Annualized Return: +14.02%
   Sharpe Ratio: 0.6626 (annualized)
   Sortino Ratio: 0.8292 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 19.79%
   Turnover: 0.36%
   Win Rate: 54.32%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.067, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $217,181.29
   Total Return: +117.18%
   Annualized Return: +21.40%
   Sharpe Ratio: 1.2596 (annualized)
   Sortino Ratio: 1.8274 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.70%
   Turnover: 0.33%
   Win Rate: 55.21%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.055, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-07-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $195,702.30
   Total Return: +95.70%
   Annualized Return: +18.28%
   Sharpe Ratio: 1.1834 (annualized)
   Sortino Ratio: 1.7289 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 13.27%
   Turnover: 0.31%
   Win Rate: 55.11%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.057, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $168,379.53
   Total Return: +68.38%
   Annualized Return: +13.91%
   Sharpe Ratio: 0.9402 (annualized)
   Sortino Ratio: 1.3778 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 12.61%
   Turnover: 0.31%
   Win Rate: 53.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.051, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)





<div id="df-124d1da7-6189-4a37-874f-3f50910335db" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>checkpoint_label</th>
      <th>checkpoint_prefix</th>
      <th>horizon_days</th>
      <th>starts_used</th>
      <th>det_sharpe_median</th>
      <th>det_sharpe_mean</th>
      <th>det_sharpe_std</th>
      <th>det_return_median</th>
      <th>det_mdd_median</th>
      <th>det_turnover_median</th>
      <th>selection_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>high_watermark__ep0408__step-00001</td>
      <td>/content/eval_restore/tcn_fusion_results/high_...</td>
      <td>252</td>
      <td>4</td>
      <td>2.314306</td>
      <td>1.881350</td>
      <td>0.918553</td>
      <td>0.358393</td>
      <td>0.081970</td>
      <td>0.003405</td>
      <td>2.247154</td>
    </tr>
    <tr>
      <th>1</th>
      <td>high_watermark__ep0408__step-00001</td>
      <td>/content/eval_restore/tcn_fusion_results/high_...</td>
      <td>504</td>
      <td>4</td>
      <td>1.115985</td>
      <td>1.252489</td>
      <td>0.462197</td>
      <td>0.502379</td>
      <td>0.124978</td>
      <td>0.003361</td>
      <td>1.141130</td>
    </tr>
    <tr>
      <th>2</th>
      <td>high_watermark__ep0408__step-00001</td>
      <td>/content/eval_restore/tcn_fusion_results/high_...</td>
      <td>756</td>
      <td>4</td>
      <td>0.989815</td>
      <td>0.963568</td>
      <td>0.249865</td>
      <td>0.590156</td>
      <td>0.134943</td>
      <td>0.003351</td>
      <td>1.068658</td>
    </tr>
    <tr>
      <th>3</th>
      <td>high_watermark__ep0408__step-00001</td>
      <td>/content/eval_restore/tcn_fusion_results/high_...</td>
      <td>1008</td>
      <td>4</td>
      <td>1.061770</td>
      <td>1.011450</td>
      <td>0.269525</td>
      <td>0.823465</td>
      <td>0.134943</td>
      <td>0.003222</td>
      <td>1.207656</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">
      
  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-124d1da7-6189-4a37-874f-3f50910335db')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">
      
  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>
    
  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-124d1da7-6189-4a37-874f-3f50910335db button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-124d1da7-6189-4a37-874f-3f50910335db');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>
  
    </div>
  </div>




  [BEST] Overall robust winner across horizons/start dates

  <div id="df-ab4ff002-f702-4f31-bcaa-a4bba7753015" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>checkpoint_label</th>
      <th>checkpoint_prefix</th>
      <th>overall_weighted_score</th>
      <th>overall_weighted_sharpe</th>
      <th>overall_weighted_return</th>
      <th>overall_weighted_mdd</th>
      <th>horizons_covered</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>high_watermark__ep0409__step-00001</td>
      <td>/content/eval_restore/tcn_fusion_results/high_...</td>
      <td>1.30525</td>
      <td>1.241618</td>
      <td>0.60344</td>
      <td>0.124506</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">
      
  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-ab4ff002-f702-4f31-bcaa-a4bba7753015')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">
      
  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>
    
  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-ab4ff002-f702-4f31-bcaa-a4bba7753015 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-ab4ff002-f702-4f31-bcaa-a4bba7753015');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>
  
    </div>
  </div>



  [RAND] Stage 2/2: stochastic reranking on horizon winners

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $113,822.04
   Total Return: +13.82%
   Annualized Return: +13.82%
   Sharpe Ratio: 0.5047 (annualized)
   Sortino Ratio: 0.6100 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 31.88%
   Turnover: 0.49%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.062, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=752142):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +9.91%
   Annualized Return: +9.91%
   Sharpe: 0.3940
   Volatility (Ann.): 32.07%
   Max DD: 31.46%
   Turnover (episode): 12.61%
   Turnover (step): mean=12.611% | p95=17.023% | max=21.017%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=50.446% | executed/raw=0.250

[RAND] Run 2/8 (Seed=752143):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +11.94%
   Annualized Return: +11.94%
   Sharpe: 0.4505
   Volatility (Ann.): 32.31%
   Max DD: 31.17%
   Turnover (episode): 12.89%
   Turnover (step): mean=12.891% | p95=18.003% | max=22.109%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=51.564% | executed/raw=0.250

[RAND] Run 3/8 (Seed=752144):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +7.35%
   Annualized Return: +7.35%
   Sharpe: 0.3204
   Volatility (Ann.): 32.74%
   Max DD: 31.64%
   Turnover (episode): 13.31%
   Turnover (step): mean=13.310% | p95=18.434% | max=21.546%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.240% | executed/raw=0.250

[RAND] Run 4/8 (Seed=752145):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +9.13%
   Annualized Return: +9.13%
   Sharpe: 0.3719
   Volatility (Ann.): 32.09%
   Max DD: 31.51%
   Turnover (episode): 13.14%
   Turnover (step): mean=13.139% | p95=17.646% | max=23.752%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.558% | executed/raw=0.250

[RAND] Run 5/8 (Seed=752146):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +6.29%
   Annualized Return: +6.29%
   Sharpe: 0.2894
   Volatility (Ann.): 31.92%
   Max DD: 32.02%
   Turnover (episode): 13.16%
   Turnover (step): mean=13.160% | p95=18.241% | max=20.682%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.640% | executed/raw=0.250

[RAND] Run 6/8 (Seed=752147):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +10.80%
   Annualized Return: +10.80%
   Sharpe: 0.4190
   Volatility (Ann.): 32.22%
   Max DD: 31.42%
   Turnover (episode): 13.15%
   Turnover (step): mean=13.147% | p95=17.748% | max=22.136%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.589% | executed/raw=0.250

[RAND] Run 7/8 (Seed=752148):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +13.49%
   Annualized Return: +13.49%
   Sharpe: 0.4924
   Volatility (Ann.): 32.49%
   Max DD: 31.42%
   Turnover (episode): 13.42%
   Turnover (step): mean=13.420% | p95=18.383% | max=22.040%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.681% | executed/raw=0.250

[RAND] Run 8/8 (Seed=752149):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +12.06%
   Annualized Return: +12.06%
   Sharpe: 0.4551
   Volatility (Ann.): 32.02%
   Max DD: 31.69%
   Turnover (episode): 12.93%
   Turnover (step): mean=12.934% | p95=17.609% | max=21.904%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=51.738% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +10.12%
   Std:  2.46%
   Min:  +6.29%
   Max:  +13.49%

Annualized Return (%):
   Mean: +10.12%
   Std:  2.46%
   Min:  +6.29%
   Max:  +13.49%

Sharpe Ratio (annualized):
   Mean: 0.3991
   Std:  0.0696
   Min:  0.2894
   Max:  0.4924

Volatility (Ann. %):
   Mean: +32.23%
   Std:  0.27%
   Min:  +31.92%
   Max:  +32.74%

Max Drawdown (%):
   Mean: 31.54%
   Std:  0.25%
   Min:  31.17%
   Max:  32.02%

Turnover (%):
   Mean: 13.08%
   Std:  0.26%

Turnover Step Detail (%):
   Mean(step mean): 13.077%
   Mean(step p95):  17.886%
   Mean(step max):  21.898%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_212110.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $153,083.62
   Total Return: +53.08%
   Annualized Return: +53.08%
   Sharpe Ratio: 2.2994 (annualized)
   Sortino Ratio: 3.1445 (annualized)
   Max Drawdown: 8.23%
   Volatility (Ann.): 18.49%
   Turnover: 0.37%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.016, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=752205):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +51.26%
   Annualized Return: +51.26%
   Sharpe: 2.2033
   Volatility (Ann.): 18.77%
   Max DD: 8.52%
   Turnover (episode): 13.18%
   Turnover (step): mean=13.183% | p95=17.444% | max=22.074%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.731% | executed/raw=0.250

[RAND] Run 2/8 (Seed=752206):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +49.53%
   Annualized Return: +49.53%
   Sharpe: 2.1538
   Volatility (Ann.): 18.66%
   Max DD: 7.85%
   Turnover (episode): 13.81%
   Turnover (step): mean=13.810% | p95=18.201% | max=25.040%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=55.240% | executed/raw=0.250

[RAND] Run 3/8 (Seed=752207):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +50.61%
   Annualized Return: +50.61%
   Sharpe: 2.1745
   Volatility (Ann.): 18.82%
   Max DD: 8.58%
   Turnover (episode): 13.43%
   Turnover (step): mean=13.426% | p95=17.844% | max=22.152%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.704% | executed/raw=0.250

[RAND] Run 4/8 (Seed=752208):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +48.71%
   Annualized Return: +48.71%
   Sharpe: 2.1455
   Volatility (Ann.): 18.45%
   Max DD: 8.63%
   Turnover (episode): 13.47%
   Turnover (step): mean=13.469% | p95=17.713% | max=20.654%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.877% | executed/raw=0.250

[RAND] Run 5/8 (Seed=752209):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +51.24%
   Annualized Return: +51.24%
   Sharpe: 2.2243
   Volatility (Ann.): 18.57%
   Max DD: 8.08%
   Turnover (episode): 13.15%
   Turnover (step): mean=13.146% | p95=17.624% | max=21.813%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.585% | executed/raw=0.250

[RAND] Run 6/8 (Seed=752210):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +51.86%
   Annualized Return: +51.86%
   Sharpe: 2.2123
   Volatility (Ann.): 18.88%
   Max DD: 8.45%
   Turnover (episode): 13.57%
   Turnover (step): mean=13.572% | p95=18.093% | max=22.345%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.288% | executed/raw=0.250

[RAND] Run 7/8 (Seed=752211):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +52.60%
   Annualized Return: +52.60%
   Sharpe: 2.2220
   Volatility (Ann.): 19.04%
   Max DD: 8.33%
   Turnover (episode): 13.58%
   Turnover (step): mean=13.583% | p95=18.390% | max=21.918%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.330% | executed/raw=0.250

[RAND] Run 8/8 (Seed=752212):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +54.22%
   Annualized Return: +54.22%
   Sharpe: 2.2991
   Volatility (Ann.): 18.84%
   Max DD: 8.30%
   Turnover (episode): 13.32%
   Turnover (step): mean=13.315% | p95=18.492% | max=23.003%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.262% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +51.26%
   Std:  1.72%
   Min:  +48.71%
   Max:  +54.22%

Annualized Return (%):
   Mean: +51.26%
   Std:  1.72%
   Min:  +48.71%
   Max:  +54.22%

Sharpe Ratio (annualized):
   Mean: 2.2044
   Std:  0.0488
   Min:  2.1455
   Max:  2.2991

Volatility (Ann. %):
   Mean: +18.75%
   Std:  0.19%
   Min:  +18.45%
   Max:  +19.04%

Max Drawdown (%):
   Mean: 8.34%
   Std:  0.27%
   Min:  7.85%
   Max:  8.63%

Turnover (%):
   Mean: 13.44%
   Std:  0.22%

Turnover Step Detail (%):
   Mean(step mean): 13.438%
   Mean(step p95):  17.975%
   Mean(step max):  22.375%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_212634.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $152,618.88
   Total Return: +52.62%
   Annualized Return: +23.54%
   Sharpe Ratio: 0.9228 (annualized)
   Sortino Ratio: 1.0551 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 23.92%
   Turnover: 0.38%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.071, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1004142):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +44.72%
   Annualized Return: +20.30%
   Sharpe: 0.8064
   Volatility (Ann.): 24.12%
   Max DD: 30.69%
   Turnover (episode): 13.39%
   Turnover (step): mean=13.389% | p95=18.357% | max=21.580%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.557% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1004143):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +48.37%
   Annualized Return: +21.81%
   Sharpe: 0.8556
   Volatility (Ann.): 24.23%
   Max DD: 30.89%
   Turnover (episode): 13.44%
   Turnover (step): mean=13.445% | p95=18.247% | max=23.042%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.779% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1004144):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +48.71%
   Annualized Return: +21.95%
   Sharpe: 0.8694
   Volatility (Ann.): 23.88%
   Max DD: 30.58%
   Turnover (episode): 13.19%
   Turnover (step): mean=13.195% | p95=17.952% | max=22.258%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.779% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1004145):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +43.22%
   Annualized Return: +19.67%
   Sharpe: 0.7854
   Volatility (Ann.): 24.10%
   Max DD: 31.76%
   Turnover (episode): 13.53%
   Turnover (step): mean=13.528% | p95=18.627% | max=22.979%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.110% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1004146):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +46.34%
   Annualized Return: +20.97%
   Sharpe: 0.8276
   Volatility (Ann.): 24.20%
   Max DD: 30.97%
   Turnover (episode): 13.18%
   Turnover (step): mean=13.177% | p95=18.519% | max=23.691%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.706% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1004147):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +48.05%
   Annualized Return: +21.68%
   Sharpe: 0.8573
   Volatility (Ann.): 23.98%
   Max DD: 30.36%
   Turnover (episode): 13.24%
   Turnover (step): mean=13.241% | p95=18.024% | max=21.133%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.963% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1004148):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +41.64%
   Annualized Return: +19.01%
   Sharpe: 0.7643
   Volatility (Ann.): 24.00%
   Max DD: 31.42%
   Turnover (episode): 13.45%
   Turnover (step): mean=13.447% | p95=18.562% | max=20.726%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.787% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1004149):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +42.78%
   Annualized Return: +19.49%
   Sharpe: 0.7827
   Volatility (Ann.): 23.93%
   Max DD: 30.81%
   Turnover (episode): 13.41%
   Turnover (step): mean=13.410% | p95=18.198% | max=20.094%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.638% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +45.48%
   Std:  2.77%
   Min:  +41.64%
   Max:  +48.71%

Annualized Return (%):
   Mean: +20.61%
   Std:  1.15%
   Min:  +19.01%
   Max:  +21.95%

Sharpe Ratio (annualized):
   Mean: 0.8186
   Std:  0.0397
   Min:  0.7643
   Max:  0.8694

Volatility (Ann. %):
   Mean: +24.05%
   Std:  0.13%
   Min:  +23.88%
   Max:  +24.23%

Max Drawdown (%):
   Mean: 30.93%
   Std:  0.45%
   Min:  30.36%
   Max:  31.76%

Turnover (%):
   Mean: 13.35%
   Std:  0.13%

Turnover Step Detail (%):
   Mean(step mean): 13.354%
   Mean(step p95):  18.311%
   Mean(step max):  21.938%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_213714.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $181,385.87
   Total Return: +81.39%
   Annualized Return: +34.68%
   Sharpe Ratio: 1.8848 (annualized)
   Sortino Ratio: 2.6243 (annualized)
   Max Drawdown: 8.78%
   Volatility (Ann.): 15.42%
   Turnover: 0.34%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.050, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1004205):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +66.79%
   Annualized Return: +29.15%
   Sharpe: 1.5879
   Volatility (Ann.): 15.67%
   Max DD: 10.38%
   Turnover (episode): 13.52%
   Turnover (step): mean=13.520% | p95=18.574% | max=22.789%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.081% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1004206):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +71.82%
   Annualized Return: +31.08%
   Sharpe: 1.6784
   Volatility (Ann.): 15.72%
   Max DD: 9.43%
   Turnover (episode): 13.42%
   Turnover (step): mean=13.420% | p95=17.880% | max=20.656%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.681% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1004207):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +71.92%
   Annualized Return: +31.12%
   Sharpe: 1.7035
   Volatility (Ann.): 15.48%
   Max DD: 8.42%
   Turnover (episode): 13.53%
   Turnover (step): mean=13.527% | p95=18.179% | max=22.910%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.108% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1004208):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +73.30%
   Annualized Return: +31.64%
   Sharpe: 1.7221
   Volatility (Ann.): 15.56%
   Max DD: 8.48%
   Turnover (episode): 13.51%
   Turnover (step): mean=13.512% | p95=18.476% | max=23.254%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.049% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1004209):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +72.55%
   Annualized Return: +31.36%
   Sharpe: 1.7207
   Volatility (Ann.): 15.43%
   Max DD: 8.23%
   Turnover (episode): 13.20%
   Turnover (step): mean=13.197% | p95=17.890% | max=20.208%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.787% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1004210):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +71.05%
   Annualized Return: +30.78%
   Sharpe: 1.6837
   Volatility (Ann.): 15.52%
   Max DD: 10.70%
   Turnover (episode): 13.47%
   Turnover (step): mean=13.470% | p95=18.021% | max=25.028%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.880% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1004211):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +71.51%
   Annualized Return: +30.96%
   Sharpe: 1.6740
   Volatility (Ann.): 15.71%
   Max DD: 9.28%
   Turnover (episode): 13.40%
   Turnover (step): mean=13.397% | p95=18.348% | max=21.616%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.590% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1004212):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +71.62%
   Annualized Return: +31.00%
   Sharpe: 1.6734
   Volatility (Ann.): 15.73%
   Max DD: 9.12%
   Turnover (episode): 13.87%
   Turnover (step): mean=13.872% | p95=18.376% | max=21.592%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=55.488% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +71.32%
   Std:  1.95%
   Min:  +66.79%
   Max:  +73.30%

Annualized Return (%):
   Mean: +30.89%
   Std:  0.75%
   Min:  +29.15%
   Max:  +31.64%

Sharpe Ratio (annualized):
   Mean: 1.6805
   Std:  0.0423
   Min:  1.5879
   Max:  1.7221

Volatility (Ann. %):
   Mean: +15.60%
   Std:  0.12%
   Min:  +15.43%
   Max:  +15.73%

Max Drawdown (%):
   Mean: 9.26%
   Std:  0.91%
   Min:  8.23%
   Max:  10.70%

Turnover (%):
   Mean: 13.49%
   Std:  0.19%

Turnover Step Detail (%):
   Mean(step mean): 13.489%
   Mean(step p95):  18.218%
   Mean(step max):  22.257%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_214734.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $152,142.80
   Total Return: +52.14%
   Annualized Return: +15.01%
   Sharpe Ratio: 0.6564 (annualized)
   Sortino Ratio: 0.8180 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 22.02%
   Turnover: 0.37%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.081, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1256142):
   Start Date: 2020-01-31 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +20.64%
   Annualized Return: +9.84%
   Sharpe: 0.5706
   Volatility (Ann.): 14.97%
   Max DD: 14.57%
   Turnover (episode): 13.26%
   Turnover (step): mean=13.264% | p95=17.978% | max=22.864%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.055% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1256143):
   Start Date: 2020-02-06 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +29.52%
   Annualized Return: +13.81%
   Sharpe: 0.8054
   Volatility (Ann.): 15.04%
   Max DD: 15.24%
   Turnover (episode): 13.16%
   Turnover (step): mean=13.162% | p95=17.401% | max=22.831%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.648% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1256144):
   Start Date: 2020-01-10 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +76.98%
   Annualized Return: +33.04%
   Sharpe: 1.7878
   Volatility (Ann.): 15.58%
   Max DD: 9.04%
   Turnover (episode): 13.30%
   Turnover (step): mean=13.300% | p95=18.003% | max=23.010%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.201% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1256145):
   Start Date: 2020-01-23 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +31.98%
   Annualized Return: +14.88%
   Sharpe: 0.8886
   Volatility (Ann.): 14.62%
   Max DD: 12.56%
   Turnover (episode): 13.38%
   Turnover (step): mean=13.384% | p95=18.500% | max=21.871%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.535% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1256146):
   Start Date: 2020-02-06 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +31.33%
   Annualized Return: +14.60%
   Sharpe: 0.8521
   Volatility (Ann.): 15.02%
   Max DD: 14.34%
   Turnover (episode): 13.05%
   Turnover (step): mean=13.046% | p95=18.375% | max=22.321%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.184% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1256147):
   Start Date: 2020-01-15 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +49.14%
   Annualized Return: +22.12%
   Sharpe: 1.2879
   Volatility (Ann.): 14.88%
   Max DD: 9.01%
   Turnover (episode): 13.66%
   Turnover (step): mean=13.663% | p95=18.258% | max=22.856%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.653% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1256148):
   Start Date: 2020-01-06 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +40.39%
   Annualized Return: +18.49%
   Sharpe: 0.7469
   Volatility (Ann.): 23.95%
   Max DD: 30.64%
   Turnover (episode): 13.43%
   Turnover (step): mean=13.433% | p95=18.208% | max=20.995%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.733% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1256149):
   Start Date: 2020-01-24 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +31.83%
   Annualized Return: +14.82%
   Sharpe: 0.8896
   Volatility (Ann.): 14.52%
   Max DD: 12.11%
   Turnover (episode): 13.47%
   Turnover (step): mean=13.468% | p95=18.052% | max=25.777%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.872% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +38.98%
   Std:  17.46%
   Min:  +20.64%
   Max:  +76.98%

Annualized Return (%):
   Mean: +17.70%
   Std:  7.15%
   Min:  +9.84%
   Max:  +33.04%

Sharpe Ratio (annualized):
   Mean: 0.9786
   Std:  0.3841
   Min:  0.5706
   Max:  1.7878

Volatility (Ann. %):
   Mean: +16.07%
   Std:  3.20%
   Min:  +14.52%
   Max:  +23.95%

Max Drawdown (%):
   Mean: 14.69%
   Std:  6.87%
   Min:  9.01%
   Max:  30.64%

Turnover (%):
   Mean: 13.34%
   Std:  0.19%

Turnover Step Detail (%):
   Mean(step mean): 13.340%
   Mean(step p95):  18.097%
   Mean(step max):  22.816%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_215820.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $183,923.97
   Total Return: +83.92%
   Annualized Return: +22.52%
   Sharpe Ratio: 1.2182 (annualized)
   Sortino Ratio: 1.7820 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 16.15%
   Turnover: 0.34%
   Win Rate: 55.10%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.070, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1256205):
   Start Date: 2020-04-16 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +38.25%
   Annualized Return: +17.58%
   Sharpe: 1.0469
   Volatility (Ann.): 14.64%
   Max DD: 11.25%
   Turnover (episode): 13.41%
   Turnover (step): mean=13.412% | p95=18.113% | max=21.319%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.646% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1256206):
   Start Date: 2020-04-21 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +29.06%
   Annualized Return: +13.60%
   Sharpe: 0.8087
   Volatility (Ann.): 14.69%
   Max DD: 14.54%
   Turnover (episode): 13.04%
   Turnover (step): mean=13.037% | p95=17.660% | max=21.420%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.147% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1256207):
   Start Date: 2020-04-24 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +26.45%
   Annualized Return: +12.45%
   Sharpe: 0.7383
   Volatility (Ann.): 14.71%
   Max DD: 14.86%
   Turnover (episode): 13.18%
   Turnover (step): mean=13.178% | p95=18.019% | max=23.753%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.712% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1256208):
   Start Date: 2020-04-17 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +21.58%
   Annualized Return: +10.27%
   Sharpe: 0.6029
   Volatility (Ann.): 14.77%
   Max DD: 15.02%
   Turnover (episode): 13.32%
   Turnover (step): mean=13.322% | p95=17.926% | max=22.697%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.288% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1256209):
   Start Date: 2020-04-28 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +29.95%
   Annualized Return: +14.00%
   Sharpe: 0.8067
   Volatility (Ann.): 15.26%
   Max DD: 16.26%
   Turnover (episode): 13.37%
   Turnover (step): mean=13.370% | p95=18.457% | max=23.062%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.479% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1256210):
   Start Date: 2020-04-07 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +45.19%
   Annualized Return: +20.50%
   Sharpe: 1.2097
   Volatility (Ann.): 14.71%
   Max DD: 9.20%
   Turnover (episode): 13.70%
   Turnover (step): mean=13.704% | p95=18.834% | max=21.867%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.817% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1256211):
   Start Date: 2020-04-17 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +26.26%
   Annualized Return: +12.37%
   Sharpe: 0.7321
   Volatility (Ann.): 14.74%
   Max DD: 12.72%
   Turnover (episode): 13.47%
   Turnover (step): mean=13.470% | p95=18.064% | max=21.109%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.882% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1256212):
   Start Date: 2020-04-03 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +55.56%
   Annualized Return: +24.72%
   Sharpe: 1.4623
   Volatility (Ann.): 14.51%
   Max DD: 9.37%
   Turnover (episode): 13.48%
   Turnover (step): mean=13.475% | p95=18.457% | max=22.240%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.902% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +34.04%
   Std:  11.47%
   Min:  +21.58%
   Max:  +55.56%

Annualized Return (%):
   Mean: +15.69%
   Std:  4.88%
   Min:  +10.27%
   Max:  +24.72%

Sharpe Ratio (annualized):
   Mean: 0.9259
   Std:  0.2898
   Min:  0.6029
   Max:  1.4623

Volatility (Ann. %):
   Mean: +14.75%
   Std:  0.22%
   Min:  +14.51%
   Max:  +15.26%

Max Drawdown (%):
   Mean: 12.90%
   Std:  2.70%
   Min:  9.20%
   Max:  16.26%

Turnover (%):
   Mean: 13.37%
   Std:  0.20%

Turnover Step Detail (%):
   Mean(step mean): 13.371%
   Mean(step p95):  18.191%
   Mean(step max):  22.184%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_220900.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $168,990.63
   Total Return: +68.99%
   Annualized Return: +14.02%
   Sharpe Ratio: 0.6626 (annualized)
   Sortino Ratio: 0.8292 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 19.79%
   Turnover: 0.36%
   Win Rate: 54.32%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.067, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1508142):
   Start Date: 2020-01-08 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +39.53%
   Annualized Return: +18.12%
   Sharpe: 0.7389
   Volatility (Ann.): 23.73%
   Max DD: 27.40%
   Turnover (episode): 13.31%
   Turnover (step): mean=13.309% | p95=18.033% | max=21.136%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.235% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1508143):
   Start Date: 2020-03-05 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +7.82%
   Annualized Return: +3.84%
   Sharpe: 0.1942
   Volatility (Ann.): 15.05%
   Max DD: 15.89%
   Turnover (episode): 13.33%
   Turnover (step): mean=13.332% | p95=18.365% | max=21.474%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.330% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1508144):
   Start Date: 2020-01-10 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +59.47%
   Annualized Return: +26.28%
   Sharpe: 1.4989
   Volatility (Ann.): 15.04%
   Max DD: 9.45%
   Turnover (episode): 13.44%
   Turnover (step): mean=13.436% | p95=17.905% | max=22.442%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.744% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1508145):
   Start Date: 2020-03-03 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +11.58%
   Annualized Return: +5.63%
   Sharpe: 0.3074
   Volatility (Ann.): 15.13%
   Max DD: 14.99%
   Turnover (episode): 13.14%
   Turnover (step): mean=13.140% | p95=17.786% | max=21.162%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.560% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1508146):
   Start Date: 2020-02-06 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +24.29%
   Annualized Return: +11.49%
   Sharpe: 0.6659
   Volatility (Ann.): 15.10%
   Max DD: 15.87%
   Turnover (episode): 13.68%
   Turnover (step): mean=13.684% | p95=18.334% | max=21.627%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.737% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1508147):
   Start Date: 2020-03-10 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: -3.40%
   Annualized Return: -1.71%
   Sharpe: -0.1695
   Volatility (Ann.): 15.15%
   Max DD: 17.04%
   Turnover (episode): 13.35%
   Turnover (step): mean=13.346% | p95=18.382% | max=22.483%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.385% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1508148):
   Start Date: 2020-02-14 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +9.23%
   Annualized Return: +4.51%
   Sharpe: 0.2375
   Volatility (Ann.): 15.02%
   Max DD: 17.35%
   Turnover (episode): 13.00%
   Turnover (step): mean=13.004% | p95=17.325% | max=22.518%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.015% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1508149):
   Start Date: 2020-02-28 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +11.85%
   Annualized Return: +5.76%
   Sharpe: 0.3154
   Volatility (Ann.): 15.14%
   Max DD: 16.72%
   Turnover (episode): 13.45%
   Turnover (step): mean=13.452% | p95=18.480% | max=21.639%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.809% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +20.05%
   Std:  20.38%
   Min:  -3.40%
   Max:  +59.47%

Annualized Return (%):
   Mean: +9.24%
   Std:  9.03%
   Min:  -1.71%
   Max:  +26.28%

Sharpe Ratio (annualized):
   Mean: 0.4736
   Std:  0.5012
   Min:  -0.1695
   Max:  1.4989

Volatility (Ann. %):
   Mean: +16.17%
   Std:  3.06%
   Min:  +15.02%
   Max:  +23.73%

Max Drawdown (%):
   Mean: 16.84%
   Std:  4.95%
   Min:  9.45%
   Max:  27.40%

Turnover (%):
   Mean: 13.34%
   Std:  0.21%

Turnover Step Detail (%):
   Mean(step mean): 13.338%
   Mean(step p95):  18.076%
   Mean(step max):  21.810%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_221959.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00408_shp1p103_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $217,181.29
   Total Return: +117.18%
   Annualized Return: +21.40%
   Sharpe Ratio: 1.2596 (annualized)
   Sortino Ratio: 1.8274 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.70%
   Turnover: 0.33%
   Win Rate: 55.21%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.055, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1508205):
   Start Date: 2020-05-19 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +15.28%
   Annualized Return: +7.37%
   Sharpe: 0.4167
   Volatility (Ann.): 15.06%
   Max DD: 16.22%
   Turnover (episode): 13.31%
   Turnover (step): mean=13.308% | p95=18.457% | max=21.926%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.233% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1508206):
   Start Date: 2020-04-13 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +38.24%
   Annualized Return: +17.58%
   Sharpe: 1.0714
   Volatility (Ann.): 14.25%
   Max DD: 11.83%
   Turnover (episode): 13.38%
   Turnover (step): mean=13.380% | p95=18.036% | max=24.066%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.520% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1508207):
   Start Date: 2020-05-08 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +13.36%
   Annualized Return: +6.47%
   Sharpe: 0.3616
   Volatility (Ann.): 15.01%
   Max DD: 15.64%
   Turnover (episode): 13.33%
   Turnover (step): mean=13.335% | p95=17.648% | max=22.985%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.339% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1508208):
   Start Date: 2020-06-12 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 504 (2.00 years)
   Total Return: +14.31%
   Annualized Return: +6.91%
   Sharpe: 0.4012
   Volatility (Ann.): 14.31%
   Max DD: 15.42%
   Turnover (episode): 13.32%
   Turnover (step): mean=13.323% | p95=17.961% | max=21.138%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.292% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1508209):
   Start Date: 2020-04-24 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +28.62%
   Annualized Return: +13.41%
   Sharpe: 0.7895
   Volatility (Ann.): 14.86%
   Max DD: 14.51%
   Turnover (episode): 13.23%
   Turnover (step): mean=13.229% | p95=17.904% | max=22.916%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.915% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1508210):
   Start Date: 2020-06-12 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 504 (2.00 years)
   Total Return: +14.83%
   Annualized Return: +7.16%
   Sharpe: 0.4184
   Volatility (Ann.): 14.24%
   Max DD: 14.79%
   Turnover (episode): 13.29%
   Turnover (step): mean=13.287% | p95=18.120% | max=21.403%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.146% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1508211):
   Start Date: 2020-04-21 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +19.60%
   Annualized Return: +9.36%
   Sharpe: 0.5475
   Volatility (Ann.): 14.75%
   Max DD: 16.31%
   Turnover (episode): 13.43%
   Turnover (step): mean=13.430% | p95=17.961% | max=21.109%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.721% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1508212):
   Start Date: 2020-05-04 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +18.53%
   Annualized Return: +8.87%
   Sharpe: 0.5129
   Volatility (Ann.): 14.91%
   Max DD: 15.19%
   Turnover (episode): 13.22%
   Turnover (step): mean=13.222% | p95=17.836% | max=20.895%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.889% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +20.34%
   Std:  8.73%
   Min:  +13.36%
   Max:  +38.24%

Annualized Return (%):
   Mean: +9.64%
   Std:  3.90%
   Min:  +6.47%
   Max:  +17.58%

Sharpe Ratio (annualized):
   Mean: 0.5649
   Std:  0.2454
   Min:  0.3616
   Max:  1.0714

Volatility (Ann. %):
   Mean: +14.67%
   Std:  0.35%
   Min:  +14.24%
   Max:  +15.06%

Max Drawdown (%):
   Mean: 14.99%
   Std:  1.42%
   Min:  11.83%
   Max:  16.31%

Turnover (%):
   Mean: 13.31%
   Std:  0.07%

Turnover Step Detail (%):
   Mean(step mean): 13.314%
   Mean(step p95):  17.990%
   Mean(step max):  22.055%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_223102.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $113,822.04
   Total Return: +13.82%
   Annualized Return: +13.82%
   Sharpe Ratio: 0.5047 (annualized)
   Sortino Ratio: 0.6100 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 31.88%
   Turnover: 0.49%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.062, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=752142):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +9.06%
   Annualized Return: +9.06%
   Sharpe: 0.3692
   Volatility (Ann.): 32.30%
   Max DD: 30.28%
   Turnover (episode): 13.13%
   Turnover (step): mean=13.134% | p95=18.063% | max=21.158%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.534% | executed/raw=0.250

[RAND] Run 2/8 (Seed=752143):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +10.44%
   Annualized Return: +10.44%
   Sharpe: 0.4091
   Volatility (Ann.): 32.09%
   Max DD: 30.39%
   Turnover (episode): 13.17%
   Turnover (step): mean=13.172% | p95=17.822% | max=21.333%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.686% | executed/raw=0.250

[RAND] Run 3/8 (Seed=752144):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +9.46%
   Annualized Return: +9.46%
   Sharpe: 0.3811
   Volatility (Ann.): 32.22%
   Max DD: 31.62%
   Turnover (episode): 12.98%
   Turnover (step): mean=12.983% | p95=17.656% | max=21.392%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=51.931% | executed/raw=0.250

[RAND] Run 4/8 (Seed=752145):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +11.17%
   Annualized Return: +11.17%
   Sharpe: 0.4297
   Volatility (Ann.): 32.03%
   Max DD: 31.13%
   Turnover (episode): 12.99%
   Turnover (step): mean=12.990% | p95=17.331% | max=21.996%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=51.962% | executed/raw=0.250

[RAND] Run 5/8 (Seed=752146):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +9.10%
   Annualized Return: +9.10%
   Sharpe: 0.3717
   Volatility (Ann.): 31.62%
   Max DD: 31.05%
   Turnover (episode): 13.02%
   Turnover (step): mean=13.019% | p95=18.207% | max=21.707%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.075% | executed/raw=0.250

[RAND] Run 6/8 (Seed=752147):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +11.88%
   Annualized Return: +11.88%
   Sharpe: 0.4495
   Volatility (Ann.): 32.11%
   Max DD: 31.28%
   Turnover (episode): 12.77%
   Turnover (step): mean=12.773% | p95=18.209% | max=20.575%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=51.094% | executed/raw=0.250

[RAND] Run 7/8 (Seed=752148):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +11.28%
   Annualized Return: +11.28%
   Sharpe: 0.4336
   Volatility (Ann.): 31.91%
   Max DD: 31.54%
   Turnover (episode): 12.90%
   Turnover (step): mean=12.902% | p95=17.855% | max=20.124%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=51.607% | executed/raw=0.250

[RAND] Run 8/8 (Seed=752149):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +9.85%
   Annualized Return: +9.85%
   Sharpe: 0.3922
   Volatility (Ann.): 32.12%
   Max DD: 30.53%
   Turnover (episode): 13.20%
   Turnover (step): mean=13.196% | p95=18.749% | max=21.312%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.784% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +10.28%
   Std:  1.08%
   Min:  +9.06%
   Max:  +11.88%

Annualized Return (%):
   Mean: +10.28%
   Std:  1.08%
   Min:  +9.06%
   Max:  +11.88%

Sharpe Ratio (annualized):
   Mean: 0.4045
   Std:  0.0306
   Min:  0.3692
   Max:  0.4495

Volatility (Ann. %):
   Mean: +32.05%
   Std:  0.21%
   Min:  +31.62%
   Max:  +32.30%

Max Drawdown (%):
   Mean: 30.98%
   Std:  0.52%
   Min:  30.28%
   Max:  31.62%

Turnover (%):
   Mean: 13.02%
   Std:  0.14%

Turnover Step Detail (%):
   Mean(step mean): 13.021%
   Mean(step p95):  17.986%
   Mean(step max):  21.200%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_223557.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $153,083.62
   Total Return: +53.08%
   Annualized Return: +53.08%
   Sharpe Ratio: 2.2994 (annualized)
   Sortino Ratio: 3.1445 (annualized)
   Max Drawdown: 8.23%
   Volatility (Ann.): 18.49%
   Turnover: 0.37%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.016, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=752205):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +49.58%
   Annualized Return: +49.58%
   Sharpe: 2.1608
   Volatility (Ann.): 18.61%
   Max DD: 8.41%
   Turnover (episode): 13.58%
   Turnover (step): mean=13.580% | p95=18.667% | max=22.600%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.320% | executed/raw=0.250

[RAND] Run 2/8 (Seed=752206):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +56.25%
   Annualized Return: +56.25%
   Sharpe: 2.3479
   Volatility (Ann.): 19.02%
   Max DD: 8.38%
   Turnover (episode): 13.52%
   Turnover (step): mean=13.523% | p95=18.573% | max=24.114%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.093% | executed/raw=0.250

[RAND] Run 3/8 (Seed=752207):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +46.40%
   Annualized Return: +46.40%
   Sharpe: 2.0267
   Volatility (Ann.): 18.79%
   Max DD: 8.61%
   Turnover (episode): 13.45%
   Turnover (step): mean=13.452% | p95=18.124% | max=22.044%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.806% | executed/raw=0.250

[RAND] Run 4/8 (Seed=752208):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +46.03%
   Annualized Return: +46.03%
   Sharpe: 1.9896
   Volatility (Ann.): 19.03%
   Max DD: 8.80%
   Turnover (episode): 13.36%
   Turnover (step): mean=13.361% | p95=17.915% | max=21.033%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.443% | executed/raw=0.250

[RAND] Run 5/8 (Seed=752209):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +51.99%
   Annualized Return: +51.99%
   Sharpe: 2.2082
   Volatility (Ann.): 18.96%
   Max DD: 8.01%
   Turnover (episode): 13.56%
   Turnover (step): mean=13.558% | p95=17.963% | max=21.246%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.233% | executed/raw=0.250

[RAND] Run 6/8 (Seed=752210):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +50.76%
   Annualized Return: +50.76%
   Sharpe: 2.1592
   Volatility (Ann.): 19.02%
   Max DD: 8.58%
   Turnover (episode): 13.58%
   Turnover (step): mean=13.578% | p95=18.014% | max=20.994%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.310% | executed/raw=0.250

[RAND] Run 7/8 (Seed=752211):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +51.33%
   Annualized Return: +51.33%
   Sharpe: 2.1850
   Volatility (Ann.): 18.97%
   Max DD: 8.58%
   Turnover (episode): 13.33%
   Turnover (step): mean=13.326% | p95=18.145% | max=22.091%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.305% | executed/raw=0.250

[RAND] Run 8/8 (Seed=752212):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +50.56%
   Annualized Return: +50.56%
   Sharpe: 2.1916
   Volatility (Ann.): 18.65%
   Max DD: 8.13%
   Turnover (episode): 13.59%
   Turnover (step): mean=13.589% | p95=18.274% | max=21.802%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.358% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +50.36%
   Std:  3.24%
   Min:  +46.03%
   Max:  +56.25%

Annualized Return (%):
   Mean: +50.36%
   Std:  3.24%
   Min:  +46.03%
   Max:  +56.25%

Sharpe Ratio (annualized):
   Mean: 2.1586
   Std:  0.1109
   Min:  1.9896
   Max:  2.3479

Volatility (Ann. %):
   Mean: +18.88%
   Std:  0.18%
   Min:  +18.61%
   Max:  +19.03%

Max Drawdown (%):
   Mean: 8.44%
   Std:  0.26%
   Min:  8.01%
   Max:  8.80%

Turnover (%):
   Mean: 13.50%
   Std:  0.10%

Turnover Step Detail (%):
   Mean(step mean): 13.496%
   Mean(step p95):  18.209%
   Mean(step max):  21.990%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_224052.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $152,618.88
   Total Return: +52.62%
   Annualized Return: +23.54%
   Sharpe Ratio: 0.9228 (annualized)
   Sortino Ratio: 1.0551 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 23.92%
   Turnover: 0.38%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.071, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1004142):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +48.40%
   Annualized Return: +21.82%
   Sharpe: 0.8628
   Volatility (Ann.): 23.95%
   Max DD: 30.28%
   Turnover (episode): 13.31%
   Turnover (step): mean=13.315% | p95=18.424% | max=22.257%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.259% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1004143):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +45.52%
   Annualized Return: +20.63%
   Sharpe: 0.8166
   Volatility (Ann.): 24.19%
   Max DD: 31.78%
   Turnover (episode): 13.37%
   Turnover (step): mean=13.370% | p95=18.031% | max=20.898%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.479% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1004144):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +48.84%
   Annualized Return: +22.00%
   Sharpe: 0.8620
   Volatility (Ann.): 24.23%
   Max DD: 31.10%
   Turnover (episode): 13.27%
   Turnover (step): mean=13.268% | p95=18.332% | max=22.825%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.072% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1004145):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +46.96%
   Annualized Return: +21.23%
   Sharpe: 0.8351
   Volatility (Ann.): 24.25%
   Max DD: 30.72%
   Turnover (episode): 13.34%
   Turnover (step): mean=13.343% | p95=18.095% | max=22.429%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.371% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1004146):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +45.32%
   Annualized Return: +20.55%
   Sharpe: 0.8195
   Volatility (Ann.): 23.94%
   Max DD: 30.88%
   Turnover (episode): 13.31%
   Turnover (step): mean=13.314% | p95=18.252% | max=22.071%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.256% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1004147):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +43.71%
   Annualized Return: +19.88%
   Sharpe: 0.7898
   Volatility (Ann.): 24.21%
   Max DD: 31.62%
   Turnover (episode): 13.39%
   Turnover (step): mean=13.391% | p95=18.281% | max=22.625%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.566% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1004148):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +41.26%
   Annualized Return: +18.85%
   Sharpe: 0.7622
   Volatility (Ann.): 23.84%
   Max DD: 30.81%
   Turnover (episode): 13.33%
   Turnover (step): mean=13.327% | p95=17.943% | max=21.535%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.310% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1004149):
   Start Date: 2020-01-02 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +41.70%
   Annualized Return: +19.04%
   Sharpe: 0.7659
   Volatility (Ann.): 23.98%
   Max DD: 31.15%
   Turnover (episode): 13.30%
   Turnover (step): mean=13.301% | p95=18.570% | max=24.307%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.206% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +45.21%
   Std:  2.85%
   Min:  +41.26%
   Max:  +48.84%

Annualized Return (%):
   Mean: +20.50%
   Std:  1.18%
   Min:  +18.85%
   Max:  +22.00%

Sharpe Ratio (annualized):
   Mean: 0.8142
   Std:  0.0392
   Min:  0.7622
   Max:  0.8628

Volatility (Ann. %):
   Mean: +24.07%
   Std:  0.16%
   Min:  +23.84%
   Max:  +24.25%

Max Drawdown (%):
   Mean: 31.04%
   Std:  0.49%
   Min:  30.28%
   Max:  31.78%

Turnover (%):
   Mean: 13.33%
   Std:  0.04%

Turnover Step Detail (%):
   Mean(step mean): 13.329%
   Mean(step p95):  18.241%
   Mean(step max):  22.368%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_225058.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $181,385.87
   Total Return: +81.39%
   Annualized Return: +34.68%
   Sharpe Ratio: 1.8848 (annualized)
   Sortino Ratio: 2.6243 (annualized)
   Max Drawdown: 8.78%
   Volatility (Ann.): 15.42%
   Turnover: 0.34%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.050, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1004205):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +69.61%
   Annualized Return: +30.24%
   Sharpe: 1.6446
   Volatility (Ann.): 15.64%
   Max DD: 9.44%
   Turnover (episode): 13.69%
   Turnover (step): mean=13.690% | p95=18.378% | max=21.602%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.762% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1004206):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +67.46%
   Annualized Return: +29.41%
   Sharpe: 1.6026
   Volatility (Ann.): 15.65%
   Max DD: 9.39%
   Turnover (episode): 13.52%
   Turnover (step): mean=13.525% | p95=18.191% | max=22.041%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.099% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1004207):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +71.69%
   Annualized Return: +31.03%
   Sharpe: 1.7013
   Volatility (Ann.): 15.46%
   Max DD: 9.39%
   Turnover (episode): 13.42%
   Turnover (step): mean=13.425% | p95=18.634% | max=22.806%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.700% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1004208):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +64.64%
   Annualized Return: +28.31%
   Sharpe: 1.5601
   Volatility (Ann.): 15.52%
   Max DD: 9.78%
   Turnover (episode): 13.37%
   Turnover (step): mean=13.368% | p95=18.170% | max=23.630%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.474% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1004209):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +68.74%
   Annualized Return: +29.90%
   Sharpe: 1.6348
   Volatility (Ann.): 15.57%
   Max DD: 9.53%
   Turnover (episode): 13.51%
   Turnover (step): mean=13.507% | p95=18.082% | max=22.960%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.030% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1004210):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +68.54%
   Annualized Return: +29.82%
   Sharpe: 1.6091
   Volatility (Ann.): 15.81%
   Max DD: 9.86%
   Turnover (episode): 13.51%
   Turnover (step): mean=13.513% | p95=18.187% | max=21.345%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.053% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1004211):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +68.26%
   Annualized Return: +29.72%
   Sharpe: 1.6070
   Volatility (Ann.): 15.77%
   Max DD: 9.56%
   Turnover (episode): 13.69%
   Turnover (step): mean=13.694% | p95=18.503% | max=22.881%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.775% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1004212):
   Start Date: 2020-04-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +67.40%
   Annualized Return: +29.38%
   Sharpe: 1.5972
   Volatility (Ann.): 15.70%
   Max DD: 9.01%
   Turnover (episode): 13.47%
   Turnover (step): mean=13.471% | p95=18.362% | max=21.132%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.884% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +68.29%
   Std:  2.01%
   Min:  +64.64%
   Max:  +71.69%

Annualized Return (%):
   Mean: +29.73%
   Std:  0.78%
   Min:  +28.31%
   Max:  +31.03%

Sharpe Ratio (annualized):
   Mean: 1.6196
   Std:  0.0416
   Min:  1.5601
   Max:  1.7013

Volatility (Ann. %):
   Mean: +15.64%
   Std:  0.12%
   Min:  +15.46%
   Max:  +15.81%

Max Drawdown (%):
   Mean: 9.49%
   Std:  0.26%
   Min:  9.01%
   Max:  9.86%

Turnover (%):
   Mean: 13.52%
   Std:  0.12%

Turnover Step Detail (%):
   Mean(step mean): 13.524%
   Mean(step p95):  18.313%
   Mean(step max):  22.300%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_230141.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $152,142.80
   Total Return: +52.14%
   Annualized Return: +15.01%
   Sharpe Ratio: 0.6564 (annualized)
   Sortino Ratio: 0.8180 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 22.02%
   Turnover: 0.37%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.081, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1256142):
   Start Date: 2020-01-31 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +20.55%
   Annualized Return: +9.80%
   Sharpe: 0.5629
   Volatility (Ann.): 15.16%
   Max DD: 16.20%
   Turnover (episode): 13.42%
   Turnover (step): mean=13.422% | p95=17.802% | max=21.266%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.688% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1256143):
   Start Date: 2020-02-06 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +28.01%
   Annualized Return: +13.14%
   Sharpe: 0.7654
   Volatility (Ann.): 15.06%
   Max DD: 15.30%
   Turnover (episode): 13.36%
   Turnover (step): mean=13.361% | p95=18.098% | max=23.601%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.444% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1256144):
   Start Date: 2020-01-10 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +74.97%
   Annualized Return: +32.28%
   Sharpe: 1.7572
   Volatility (Ann.): 15.52%
   Max DD: 9.93%
   Turnover (episode): 13.58%
   Turnover (step): mean=13.583% | p95=18.053% | max=22.141%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.331% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1256145):
   Start Date: 2020-01-23 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +24.83%
   Annualized Return: +11.73%
   Sharpe: 0.7033
   Volatility (Ann.): 14.48%
   Max DD: 14.43%
   Turnover (episode): 13.28%
   Turnover (step): mean=13.281% | p95=18.028% | max=21.258%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.126% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1256146):
   Start Date: 2020-02-06 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +33.56%
   Annualized Return: +15.57%
   Sharpe: 0.9073
   Volatility (Ann.): 15.04%
   Max DD: 14.67%
   Turnover (episode): 13.27%
   Turnover (step): mean=13.272% | p95=18.085% | max=23.979%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.088% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1256147):
   Start Date: 2020-01-15 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +51.40%
   Annualized Return: +23.04%
   Sharpe: 1.3534
   Volatility (Ann.): 14.69%
   Max DD: 9.61%
   Turnover (episode): 13.69%
   Turnover (step): mean=13.687% | p95=18.153% | max=21.490%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.746% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1256148):
   Start Date: 2020-01-06 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +43.52%
   Annualized Return: +19.80%
   Sharpe: 0.7885
   Volatility (Ann.): 24.14%
   Max DD: 30.11%
   Turnover (episode): 13.32%
   Turnover (step): mean=13.322% | p95=17.796% | max=20.986%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.287% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1256149):
   Start Date: 2020-01-24 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +38.51%
   Annualized Return: +17.69%
   Sharpe: 1.0575
   Volatility (Ann.): 14.57%
   Max DD: 12.98%
   Turnover (episode): 13.29%
   Turnover (step): mean=13.294% | p95=18.064% | max=20.529%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.177% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +39.42%
   Std:  17.56%
   Min:  +20.55%
   Max:  +74.97%

Annualized Return (%):
   Mean: +17.88%
   Std:  7.26%
   Min:  +9.80%
   Max:  +32.28%

Sharpe Ratio (annualized):
   Mean: 0.9869
   Std:  0.3942
   Min:  0.5629
   Max:  1.7572

Volatility (Ann. %):
   Mean: +16.08%
   Std:  3.27%
   Min:  +14.48%
   Max:  +24.14%

Max Drawdown (%):
   Mean: 15.40%
   Std:  6.41%
   Min:  9.61%
   Max:  30.11%

Turnover (%):
   Mean: 13.40%
   Std:  0.15%

Turnover Step Detail (%):
   Mean(step mean): 13.403%
   Mean(step p95):  18.010%
   Mean(step max):  21.906%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_231311.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $183,923.97
   Total Return: +83.92%
   Annualized Return: +22.52%
   Sharpe Ratio: 1.2182 (annualized)
   Sortino Ratio: 1.7820 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 16.15%
   Turnover: 0.34%
   Win Rate: 55.10%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.070, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1256205):
   Start Date: 2020-04-16 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +35.61%
   Annualized Return: +16.45%
   Sharpe: 0.9848
   Volatility (Ann.): 14.57%
   Max DD: 12.23%
   Turnover (episode): 13.40%
   Turnover (step): mean=13.396% | p95=17.882% | max=25.146%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.585% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1256206):
   Start Date: 2020-04-21 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +25.99%
   Annualized Return: +12.24%
   Sharpe: 0.7221
   Volatility (Ann.): 14.80%
   Max DD: 14.48%
   Turnover (episode): 13.02%
   Turnover (step): mean=13.023% | p95=17.886% | max=21.768%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.093% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1256207):
   Start Date: 2020-04-24 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +31.00%
   Annualized Return: +14.45%
   Sharpe: 0.8569
   Volatility (Ann.): 14.74%
   Max DD: 13.18%
   Turnover (episode): 13.44%
   Turnover (step): mean=13.440% | p95=17.936% | max=21.994%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.760% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1256208):
   Start Date: 2020-04-17 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +27.32%
   Annualized Return: +12.83%
   Sharpe: 0.7632
   Volatility (Ann.): 14.67%
   Max DD: 12.87%
   Turnover (episode): 13.44%
   Turnover (step): mean=13.438% | p95=18.036% | max=23.826%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.751% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1256209):
   Start Date: 2020-04-28 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +30.42%
   Annualized Return: +14.20%
   Sharpe: 0.8301
   Volatility (Ann.): 15.00%
   Max DD: 15.47%
   Turnover (episode): 13.36%
   Turnover (step): mean=13.359% | p95=18.078% | max=20.412%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.437% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1256210):
   Start Date: 2020-04-07 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +45.83%
   Annualized Return: +20.76%
   Sharpe: 1.2164
   Volatility (Ann.): 14.82%
   Max DD: 9.67%
   Turnover (episode): 13.52%
   Turnover (step): mean=13.515% | p95=18.349% | max=22.233%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.062% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1256211):
   Start Date: 2020-04-17 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +24.77%
   Annualized Return: +11.70%
   Sharpe: 0.7000
   Volatility (Ann.): 14.52%
   Max DD: 12.94%
   Turnover (episode): 13.26%
   Turnover (step): mean=13.259% | p95=18.164% | max=22.150%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.037% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1256212):
   Start Date: 2020-04-03 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +56.74%
   Annualized Return: +25.19%
   Sharpe: 1.4882
   Volatility (Ann.): 14.51%
   Max DD: 8.57%
   Turnover (episode): 13.68%
   Turnover (step): mean=13.678% | p95=18.501% | max=23.619%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.713% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +34.71%
   Std:  11.16%
   Min:  +24.77%
   Max:  +56.74%

Annualized Return (%):
   Mean: +15.98%
   Std:  4.72%
   Min:  +11.70%
   Max:  +25.19%

Sharpe Ratio (annualized):
   Mean: 0.9452
   Std:  0.2762
   Min:  0.7000
   Max:  1.4882

Volatility (Ann. %):
   Mean: +14.71%
   Std:  0.17%
   Min:  +14.51%
   Max:  +15.00%

Max Drawdown (%):
   Mean: 12.43%
   Std:  2.30%
   Min:  8.57%
   Max:  15.47%

Turnover (%):
   Mean: 13.39%
   Std:  0.19%

Turnover Step Detail (%):
   Mean(step mean): 13.389%
   Mean(step p95):  18.104%
   Mean(step max):  22.643%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_232439.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-01-02
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $168,990.63
   Total Return: +68.99%
   Annualized Return: +14.02%
   Sharpe Ratio: 0.6626 (annualized)
   Sortino Ratio: 0.8292 (annualized)
   Max Drawdown: 31.03%
   Volatility (Ann.): 19.79%
   Turnover: 0.36%
   Win Rate: 54.32%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.067, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1508142):
   Start Date: 2020-01-08 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +39.98%
   Annualized Return: +18.31%
   Sharpe: 0.7512
   Volatility (Ann.): 23.47%
   Max DD: 26.81%
   Turnover (episode): 13.39%
   Turnover (step): mean=13.391% | p95=18.207% | max=22.371%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.563% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1508143):
   Start Date: 2020-03-05 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +11.22%
   Annualized Return: +5.46%
   Sharpe: 0.2965
   Volatility (Ann.): 15.17%
   Max DD: 17.54%
   Turnover (episode): 13.38%
   Turnover (step): mean=13.383% | p95=18.065% | max=20.484%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.532% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1508144):
   Start Date: 2020-01-10 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +62.46%
   Annualized Return: +27.46%
   Sharpe: 1.5636
   Volatility (Ann.): 15.01%
   Max DD: 9.32%
   Turnover (episode): 13.72%
   Turnover (step): mean=13.724% | p95=18.338% | max=21.712%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=54.894% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1508145):
   Start Date: 2020-03-03 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +8.00%
   Annualized Return: +3.92%
   Sharpe: 0.1990
   Volatility (Ann.): 15.30%
   Max DD: 17.06%
   Turnover (episode): 13.19%
   Turnover (step): mean=13.190% | p95=17.892% | max=21.310%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.759% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1508146):
   Start Date: 2020-02-06 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +20.44%
   Annualized Return: +9.75%
   Sharpe: 0.5649
   Volatility (Ann.): 14.98%
   Max DD: 17.54%
   Turnover (episode): 13.11%
   Turnover (step): mean=13.106% | p95=17.568% | max=25.178%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.424% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1508147):
   Start Date: 2020-03-10 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: -0.02%
   Annualized Return: -0.01%
   Sharpe: -0.0571
   Volatility (Ann.): 15.05%
   Max DD: 17.54%
   Turnover (episode): 13.17%
   Turnover (step): mean=13.170% | p95=17.404% | max=20.712%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.678% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1508148):
   Start Date: 2020-02-14 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +11.04%
   Annualized Return: +5.37%
   Sharpe: 0.2912
   Volatility (Ann.): 15.14%
   Max DD: 15.48%
   Turnover (episode): 13.25%
   Turnover (step): mean=13.246% | p95=18.065% | max=20.459%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.985% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1508149):
   Start Date: 2020-02-28 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +15.43%
   Annualized Return: +7.44%
   Sharpe: 0.4199
   Volatility (Ann.): 15.12%
   Max DD: 16.75%
   Turnover (episode): 13.19%
   Turnover (step): mean=13.188% | p95=17.605% | max=20.877%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.752% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +21.07%
   Std:  20.41%
   Min:  -0.02%
   Max:  +62.46%

Annualized Return (%):
   Mean: +9.71%
   Std:  8.94%
   Min:  -0.01%
   Max:  +27.46%

Sharpe Ratio (annualized):
   Mean: 0.5037
   Std:  0.4915
   Min:  -0.0571
   Max:  1.5636

Volatility (Ann. %):
   Mean: +16.16%
   Std:  2.96%
   Min:  +14.98%
   Max:  +23.47%

Max Drawdown (%):
   Mean: 17.25%
   Std:  4.75%
   Min:  9.32%
   Max:  26.81%

Turnover (%):
   Mean: 13.30%
   Std:  0.20%

Turnover Step Detail (%):
   Mean(step mean): 13.300%
   Mean(step p95):  17.893%
   Mean(step max):  21.638%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_233635.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00409_shp1p133_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=True | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=0.5 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2020-04-02
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $217,181.29
   Total Return: +117.18%
   Annualized Return: +21.40%
   Sharpe Ratio: 1.2596 (annualized)
   Sortino Ratio: 1.8274 (annualized)
   Max Drawdown: 13.49%
   Volatility (Ann.): 14.70%
   Turnover: 0.33%
   Win Rate: 55.21%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.055, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 8 Runs)
================================================================================

[RAND] Run 1/8 (Seed=1508205):
   Start Date: 2020-05-19 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +17.73%
   Annualized Return: +8.50%
   Sharpe: 0.4881
   Volatility (Ann.): 14.99%
   Max DD: 14.25%
   Turnover (episode): 13.19%
   Turnover (step): mean=13.191% | p95=17.862% | max=21.572%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=52.762% | executed/raw=0.250

[RAND] Run 2/8 (Seed=1508206):
   Start Date: 2020-04-13 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +38.42%
   Annualized Return: +17.65%
   Sharpe: 1.0617
   Volatility (Ann.): 14.47%
   Max DD: 11.95%
   Turnover (episode): 13.40%
   Turnover (step): mean=13.402% | p95=18.500% | max=22.773%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.610% | executed/raw=0.250

[RAND] Run 3/8 (Seed=1508207):
   Start Date: 2020-05-08 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +10.22%
   Annualized Return: +4.99%
   Sharpe: 0.2666
   Volatility (Ann.): 15.16%
   Max DD: 16.64%
   Turnover (episode): 13.25%
   Turnover (step): mean=13.253% | p95=17.900% | max=20.209%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.012% | executed/raw=0.250

[RAND] Run 4/8 (Seed=1508208):
   Start Date: 2020-06-12 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 504 (2.00 years)
   Total Return: +14.58%
   Annualized Return: +7.04%
   Sharpe: 0.4094
   Volatility (Ann.): 14.31%
   Max DD: 15.58%
   Turnover (episode): 13.38%
   Turnover (step): mean=13.381% | p95=18.293% | max=21.341%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.524% | executed/raw=0.250

[RAND] Run 5/8 (Seed=1508209):
   Start Date: 2020-04-24 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +27.24%
   Annualized Return: +12.80%
   Sharpe: 0.7507
   Volatility (Ann.): 14.93%
   Max DD: 15.82%
   Turnover (episode): 13.39%
   Turnover (step): mean=13.390% | p95=17.901% | max=23.296%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.558% | executed/raw=0.250

[RAND] Run 6/8 (Seed=1508210):
   Start Date: 2020-06-12 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 504 (2.00 years)
   Total Return: +12.28%
   Annualized Return: +5.96%
   Sharpe: 0.3373
   Volatility (Ann.): 14.40%
   Max DD: 15.82%
   Turnover (episode): 13.39%
   Turnover (step): mean=13.386% | p95=17.897% | max=22.164%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.546% | executed/raw=0.250

[RAND] Run 7/8 (Seed=1508211):
   Start Date: 2020-04-21 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +24.31%
   Annualized Return: +11.49%
   Sharpe: 0.6792
   Volatility (Ann.): 14.74%
   Max DD: 15.34%
   Turnover (episode): 13.42%
   Turnover (step): mean=13.423% | p95=17.786% | max=22.670%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.694% | executed/raw=0.250

[RAND] Run 8/8 (Seed=1508212):
   Start Date: 2020-05-04 | Regime: COVID Crash (2020 Q1)
   Days Traded: 504 (2.00 years)
   Total Return: +16.82%
   Annualized Return: +8.08%
   Sharpe: 0.4647
   Volatility (Ann.): 14.88%
   Max DD: 15.30%
   Turnover (episode): 13.39%
   Turnover (step): mean=13.387% | p95=18.122% | max=22.233%
   Turnover vs target: target=35.000% | exceed_rate=0.0% | mean_excess=0.000%
   Raw/Executed turnover: raw_mean=53.548% | executed/raw=0.250

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +20.20%
   Std:  9.34%
   Min:  +10.22%
   Max:  +38.42%

Annualized Return (%):
   Mean: +9.57%
   Std:  4.20%
   Min:  +4.99%
   Max:  +17.65%

Sharpe Ratio (annualized):
   Mean: 0.5572
   Std:  0.2605
   Min:  0.2666
   Max:  1.0617

Volatility (Ann. %):
   Mean: +14.73%
   Std:  0.31%
   Min:  +14.31%
   Max:  +15.16%

Max Drawdown (%):
   Mean: 15.09%
   Std:  1.43%
   Min:  11.95%
   Max:  16.64%

Turnover (%):
   Mean: 13.35%
   Std:  0.08%

Turnover Step Detail (%):
   Mean(step mean): 13.352%
   Mean(step p95):  18.033%
   Mean(step max):  22.032%
   Mean exceed rate: 0.0%
   Mean excess over target: 0.000%
   Mean executed/raw ratio: 0.250

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs/exp6_custom_eval_20260303_234821.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/logs

[PIN] Two-stage evaluation progress summary
completed: 16 failed: 0

[OK] Winner checkpoint evaluations (with stochastic runs)