 Streaming output truncated to the last 5000 lines.

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00516_shp1p132
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00516_shp1p132_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00516_shp1p132_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $319,703.42
   Total Return: +219.70%
   Annualized Return: +33.72%
   Sharpe Ratio: 1.5464 (annualized)
   Sortino Ratio: 2.3260 (annualized)
   Max Drawdown: 26.53%
   Volatility (Ann.): 18.66%
   Turnover: 3.41%
   Win Rate: 56.11%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00516_shp1p132
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00516_shp1p132_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00516_shp1p132_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $305,733.97
   Total Return: +205.73%
   Annualized Return: +32.23%
   Sharpe Ratio: 1.5079 (annualized)
   Sortino Ratio: 2.2808 (annualized)
   Max Drawdown: 26.53%
   Volatility (Ann.): 18.36%
   Turnover: 3.41%
   Win Rate: 55.51%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $123,283.99
   Total Return: +23.28%
   Annualized Return: +23.28%
   Sharpe Ratio: 0.7524 (annualized)
   Sortino Ratio: 1.0440 (annualized)
   Max Drawdown: 29.36%
   Volatility (Ann.): 32.24%
   Turnover: 3.61%
   Win Rate: 57.37%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $148,345.24
   Total Return: +48.35%
   Annualized Return: +48.35%
   Sharpe Ratio: 2.3858 (annualized)
   Sortino Ratio: 3.5376 (annualized)
   Max Drawdown: 8.61%
   Volatility (Ann.): 16.34%
   Turnover: 3.66%
   Win Rate: 58.96%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $136,902.93
   Total Return: +36.90%
   Annualized Return: +36.90%
   Sharpe Ratio: 2.0961 (annualized)
   Sortino Ratio: 3.1575 (annualized)
   Max Drawdown: 7.51%
   Volatility (Ann.): 14.62%
   Turnover: 3.90%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $164,038.84
   Total Return: +64.04%
   Annualized Return: +28.08%
   Sharpe Ratio: 1.0376 (annualized)
   Sortino Ratio: 1.4686 (annualized)
   Max Drawdown: 29.36%
   Volatility (Ann.): 25.03%
   Turnover: 3.50%
   Win Rate: 56.86%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $177,396.00
   Total Return: +77.40%
   Annualized Return: +33.19%
   Sharpe Ratio: 1.8012 (annualized)
   Sortino Ratio: 2.6901 (annualized)
   Max Drawdown: 11.40%
   Volatility (Ann.): 15.52%
   Turnover: 3.61%
   Win Rate: 57.65%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $138,019.26
   Total Return: +38.02%
   Annualized Return: +17.48%
   Sharpe Ratio: 0.9636 (annualized)
   Sortino Ratio: 1.3918 (annualized)
   Max Drawdown: 15.16%
   Volatility (Ann.): 16.04%
   Turnover: 3.79%
   Win Rate: 54.47%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $136,381.18
   Total Return: +36.38%
   Annualized Return: +10.90%
   Sharpe Ratio: 0.4750 (annualized)
   Sortino Ratio: 0.6641 (annualized)
   Max Drawdown: 29.36%
   Volatility (Ann.): 23.44%
   Turnover: 3.83%
   Win Rate: 53.77%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $186,793.02
   Total Return: +86.79%
   Annualized Return: +23.16%
   Sharpe Ratio: 1.1566 (annualized)
   Sortino Ratio: 1.6941 (annualized)
   Max Drawdown: 25.34%
   Volatility (Ann.): 17.68%
   Turnover: 3.69%
   Win Rate: 54.57%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $194,420.43
   Total Return: +94.42%
   Annualized Return: +24.81%
   Sharpe Ratio: 1.2208 (annualized)
   Sortino Ratio: 1.8400 (annualized)
   Max Drawdown: 25.34%
   Volatility (Ann.): 17.87%
   Turnover: 3.59%
   Win Rate: 53.38%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $217,004.98
   Total Return: +117.00%
   Annualized Return: +21.37%
   Sharpe Ratio: 0.9048 (annualized)
   Sortino Ratio: 1.3052 (annualized)
   Max Drawdown: 29.36%
   Volatility (Ann.): 21.90%
   Turnover: 3.45%
   Win Rate: 53.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $288,300.31
   Total Return: +188.30%
   Annualized Return: +30.31%
   Sharpe Ratio: 1.5383 (annualized)
   Sortino Ratio: 2.3393 (annualized)
   Max Drawdown: 25.34%
   Volatility (Ann.): 16.87%
   Turnover: 3.35%
   Win Rate: 55.01%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00511_shp1p147_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $272,101.49
   Total Return: +172.10%
   Annualized Return: +28.43%
   Sharpe Ratio: 1.4732 (annualized)
   Sortino Ratio: 2.2481 (annualized)
   Max Drawdown: 25.34%
   Volatility (Ann.): 16.60%
   Turnover: 3.39%
   Win Rate: 54.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $126,426.46
   Total Return: +26.43%
   Annualized Return: +26.43%
   Sharpe Ratio: 0.8209 (annualized)
   Sortino Ratio: 1.1473 (annualized)
   Max Drawdown: 29.39%
   Volatility (Ann.): 32.88%
   Turnover: 3.01%
   Win Rate: 58.17%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $151,814.01
   Total Return: +51.81%
   Annualized Return: +51.81%
   Sharpe Ratio: 2.4665 (annualized)
   Sortino Ratio: 3.6680 (annualized)
   Max Drawdown: 8.72%
   Volatility (Ann.): 16.77%
   Turnover: 3.07%
   Win Rate: 59.76%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $142,752.16
   Total Return: +42.75%
   Annualized Return: +42.75%
   Sharpe Ratio: 2.2972 (annualized)
   Sortino Ratio: 3.4531 (annualized)
   Max Drawdown: 8.65%
   Volatility (Ann.): 15.21%
   Turnover: 3.04%
   Win Rate: 58.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $172,594.90
   Total Return: +72.59%
   Annualized Return: +31.38%
   Sharpe Ratio: 1.1248 (annualized)
   Sortino Ratio: 1.6022 (annualized)
   Max Drawdown: 29.39%
   Volatility (Ann.): 25.45%
   Turnover: 2.76%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $187,736.08
   Total Return: +87.74%
   Annualized Return: +37.02%
   Sharpe Ratio: 1.9115 (annualized)
   Sortino Ratio: 2.8744 (annualized)
   Max Drawdown: 11.55%
   Volatility (Ann.): 16.17%
   Turnover: 3.13%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $143,598.45
   Total Return: +43.60%
   Annualized Return: +19.83%
   Sharpe Ratio: 1.0046 (annualized)
   Sortino Ratio: 1.4428 (annualized)
   Max Drawdown: 16.16%
   Volatility (Ann.): 17.63%
   Turnover: 3.35%
   Win Rate: 55.27%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $144,548.85
   Total Return: +44.55%
   Annualized Return: +13.07%
   Sharpe Ratio: 0.5421 (annualized)
   Sortino Ratio: 0.7625 (annualized)
   Max Drawdown: 29.39%
   Volatility (Ann.): 24.66%
   Turnover: 3.31%
   Win Rate: 54.97%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $194,232.36
   Total Return: +94.23%
   Annualized Return: +24.77%
   Sharpe Ratio: 1.1560 (annualized)
   Sortino Ratio: 1.6896 (annualized)
   Max Drawdown: 25.45%
   Volatility (Ann.): 19.03%
   Turnover: 3.22%
   Win Rate: 55.50%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $205,591.79
   Total Return: +105.59%
   Annualized Return: +27.16%
   Sharpe Ratio: 1.2436 (annualized)
   Sortino Ratio: 1.8611 (annualized)
   Max Drawdown: 25.45%
   Volatility (Ann.): 19.25%
   Turnover: 3.13%
   Win Rate: 54.57%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $230,757.73
   Total Return: +130.76%
   Annualized Return: +23.25%
   Sharpe Ratio: 0.9424 (annualized)
   Sortino Ratio: 1.3630 (annualized)
   Max Drawdown: 29.39%
   Volatility (Ann.): 22.90%
   Turnover: 3.00%
   Win Rate: 54.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $300,364.16
   Total Return: +200.36%
   Annualized Return: +31.65%
   Sharpe Ratio: 1.5138 (annualized)
   Sortino Ratio: 2.2847 (annualized)
   Max Drawdown: 25.45%
   Volatility (Ann.): 17.94%
   Turnover: 2.96%
   Win Rate: 55.81%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00496_shp1p137_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $289,553.04
   Total Return: +189.55%
   Annualized Return: +30.45%
   Sharpe Ratio: 1.4789 (annualized)
   Sortino Ratio: 2.2368 (annualized)
   Max Drawdown: 25.45%
   Volatility (Ann.): 17.72%
   Turnover: 2.97%
   Win Rate: 55.81%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $132,879.36
   Total Return: +32.88%
   Annualized Return: +32.88%
   Sharpe Ratio: 0.9570 (annualized)
   Sortino Ratio: 1.3433 (annualized)
   Max Drawdown: 29.16%
   Volatility (Ann.): 33.73%
   Turnover: 2.38%
   Win Rate: 58.17%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $158,133.07
   Total Return: +58.13%
   Annualized Return: +58.13%
   Sharpe Ratio: 2.5100 (annualized)
   Sortino Ratio: 3.7175 (annualized)
   Max Drawdown: 8.70%
   Volatility (Ann.): 18.22%
   Turnover: 2.74%
   Win Rate: 59.36%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $147,008.77
   Total Return: +47.01%
   Annualized Return: +47.01%
   Sharpe Ratio: 2.3533 (annualized)
   Sortino Ratio: 3.5302 (annualized)
   Max Drawdown: 8.80%
   Volatility (Ann.): 16.16%
   Turnover: 2.59%
   Win Rate: 58.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $185,317.84
   Total Return: +85.32%
   Annualized Return: +36.13%
   Sharpe Ratio: 1.2319 (annualized)
   Sortino Ratio: 1.7621 (annualized)
   Max Drawdown: 29.16%
   Volatility (Ann.): 26.31%
   Turnover: 2.35%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $199,088.89
   Total Return: +99.09%
   Annualized Return: +41.10%
   Sharpe Ratio: 1.9276 (annualized)
   Sortino Ratio: 2.8881 (annualized)
   Max Drawdown: 11.86%
   Volatility (Ann.): 17.69%
   Turnover: 2.61%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $142,450.61
   Total Return: +42.45%
   Annualized Return: +19.35%
   Sharpe Ratio: 0.8957 (annualized)
   Sortino Ratio: 1.2692 (annualized)
   Max Drawdown: 19.14%
   Volatility (Ann.): 19.77%
   Turnover: 2.82%
   Win Rate: 55.67%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $158,816.21
   Total Return: +58.82%
   Annualized Return: +16.67%
   Sharpe Ratio: 0.6372 (annualized)
   Sortino Ratio: 0.9017 (annualized)
   Max Drawdown: 29.16%
   Volatility (Ann.): 26.76%
   Turnover: 2.83%
   Win Rate: 55.23%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $209,526.44
   Total Return: +109.53%
   Annualized Return: +27.96%
   Sharpe Ratio: 1.1594 (annualized)
   Sortino Ratio: 1.6916 (annualized)
   Max Drawdown: 25.11%
   Volatility (Ann.): 21.61%
   Turnover: 2.82%
   Win Rate: 55.63%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $217,530.90
   Total Return: +117.53%
   Annualized Return: +29.57%
   Sharpe Ratio: 1.2183 (annualized)
   Sortino Ratio: 1.8125 (annualized)
   Max Drawdown: 25.11%
   Volatility (Ann.): 21.59%
   Turnover: 2.61%
   Win Rate: 55.10%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $255,589.90
   Total Return: +155.59%
   Annualized Return: +26.44%
   Sharpe Ratio: 0.9941 (annualized)
   Sortino Ratio: 1.4405 (annualized)
   Max Drawdown: 29.16%
   Volatility (Ann.): 24.72%
   Turnover: 2.60%
   Win Rate: 55.21%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $331,093.51
   Total Return: +231.09%
   Annualized Return: +34.89%
   Sharpe Ratio: 1.4896 (annualized)
   Sortino Ratio: 2.2318 (annualized)
   Max Drawdown: 25.11%
   Volatility (Ann.): 20.16%
   Turnover: 2.66%
   Win Rate: 56.01%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00489_shp1p184_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $319,291.08
   Total Return: +219.29%
   Annualized Return: +33.67%
   Sharpe Ratio: 1.4649 (annualized)
   Sortino Ratio: 2.2040 (annualized)
   Max Drawdown: 25.11%
   Volatility (Ann.): 19.83%
   Turnover: 2.65%
   Win Rate: 55.71%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $127,038.30
   Total Return: +27.04%
   Annualized Return: +27.04%
   Sharpe Ratio: 0.8242 (annualized)
   Sortino Ratio: 1.1443 (annualized)
   Max Drawdown: 29.60%
   Volatility (Ann.): 33.66%
   Turnover: 2.39%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $164,732.96
   Total Return: +64.73%
   Annualized Return: +64.73%
   Sharpe Ratio: 2.5215 (annualized)
   Sortino Ratio: 3.7413 (annualized)
   Max Drawdown: 8.60%
   Volatility (Ann.): 19.89%
   Turnover: 2.52%
   Win Rate: 58.96%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $150,600.01
   Total Return: +50.60%
   Annualized Return: +50.60%
   Sharpe Ratio: 2.4928 (annualized)
   Sortino Ratio: 3.7371 (annualized)
   Max Drawdown: 8.49%
   Volatility (Ann.): 16.24%
   Turnover: 2.48%
   Win Rate: 58.17%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $183,897.00
   Total Return: +83.90%
   Annualized Return: +35.61%
   Sharpe Ratio: 1.2106 (annualized)
   Sortino Ratio: 1.7168 (annualized)
   Max Drawdown: 29.60%
   Volatility (Ann.): 26.50%
   Turnover: 2.24%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $209,770.01
   Total Return: +109.77%
   Annualized Return: +44.83%
   Sharpe Ratio: 2.0232 (annualized)
   Sortino Ratio: 3.0308 (annualized)
   Max Drawdown: 12.09%
   Volatility (Ann.): 18.20%
   Turnover: 2.40%
   Win Rate: 57.26%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $145,365.71
   Total Return: +45.37%
   Annualized Return: +20.57%
   Sharpe Ratio: 1.0063 (annualized)
   Sortino Ratio: 1.4272 (annualized)
   Max Drawdown: 18.93%
   Volatility (Ann.): 18.33%
   Turnover: 2.45%
   Win Rate: 55.27%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $155,874.41
   Total Return: +55.87%
   Annualized Return: +15.95%
   Sharpe Ratio: 0.6216 (annualized)
   Sortino Ratio: 0.8775 (annualized)
   Max Drawdown: 29.60%
   Volatility (Ann.): 26.19%
   Turnover: 2.41%
   Win Rate: 54.04%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $222,144.09
   Total Return: +122.14%
   Annualized Return: +30.48%
   Sharpe Ratio: 1.2625 (annualized)
   Sortino Ratio: 1.8603 (annualized)
   Max Drawdown: 27.65%
   Volatility (Ann.): 21.35%
   Turnover: 2.40%
   Win Rate: 54.83%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $217,980.94
   Total Return: +117.98%
   Annualized Return: +29.66%
   Sharpe Ratio: 1.2657 (annualized)
   Sortino Ratio: 1.8997 (annualized)
   Max Drawdown: 27.65%
   Volatility (Ann.): 20.68%
   Turnover: 2.26%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $245,435.72
   Total Return: +145.44%
   Annualized Return: +25.17%
   Sharpe Ratio: 0.9681 (annualized)
   Sortino Ratio: 1.4004 (annualized)
   Max Drawdown: 29.60%
   Volatility (Ann.): 24.20%
   Turnover: 2.31%
   Win Rate: 54.32%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $351,889.81
   Total Return: +251.89%
   Annualized Return: +36.96%
   Sharpe Ratio: 1.5760 (annualized)
   Sortino Ratio: 2.3909 (annualized)
   Max Drawdown: 27.65%
   Volatility (Ann.): 20.00%
   Turnover: 2.36%
   Win Rate: 55.41%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=9

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00433_shp1p475_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $326,924.36
   Total Return: +226.92%
   Annualized Return: +34.47%
   Sharpe Ratio: 1.5332 (annualized)
   Sortino Ratio: 2.3387 (annualized)
   Max Drawdown: 27.65%
   Volatility (Ann.): 19.26%
   Turnover: 2.43%
   Win Rate: 54.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $130,378.56
   Total Return: +30.38%
   Annualized Return: +30.38%
   Sharpe Ratio: 0.9263 (annualized)
   Sortino Ratio: 1.2860 (annualized)
   Max Drawdown: 29.16%
   Volatility (Ann.): 32.27%
   Turnover: 3.29%
   Win Rate: 60.16%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $158,497.81
   Total Return: +58.50%
   Annualized Return: +58.50%
   Sharpe Ratio: 2.6320 (annualized)
   Sortino Ratio: 3.8813 (annualized)
   Max Drawdown: 8.28%
   Volatility (Ann.): 17.41%
   Turnover: 3.78%
   Win Rate: 62.15%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $147,870.08
   Total Return: +47.87%
   Annualized Return: +47.87%
   Sharpe Ratio: 2.4576 (annualized)
   Sortino Ratio: 3.6667 (annualized)
   Max Drawdown: 7.94%
   Volatility (Ann.): 15.69%
   Turnover: 3.48%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $185,240.07
   Total Return: +85.24%
   Annualized Return: +36.10%
   Sharpe Ratio: 1.2670 (annualized)
   Sortino Ratio: 1.7970 (annualized)
   Max Drawdown: 29.16%
   Volatility (Ann.): 25.38%
   Turnover: 3.17%
   Win Rate: 59.24%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $199,399.09
   Total Return: +99.40%
   Annualized Return: +41.21%
   Sharpe Ratio: 2.0615 (annualized)
   Sortino Ratio: 3.0895 (annualized)
   Max Drawdown: 11.77%
   Volatility (Ann.): 16.48%
   Turnover: 3.27%
   Win Rate: 58.65%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $152,769.58
   Total Return: +52.77%
   Annualized Return: +23.60%
   Sharpe Ratio: 1.2254 (annualized)
   Sortino Ratio: 1.7729 (annualized)
   Max Drawdown: 14.57%
   Volatility (Ann.): 16.88%
   Turnover: 3.18%
   Win Rate: 56.46%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $154,284.14
   Total Return: +54.28%
   Annualized Return: +15.55%
   Sharpe Ratio: 0.6413 (annualized)
   Sortino Ratio: 0.8984 (annualized)
   Max Drawdown: 29.16%
   Volatility (Ann.): 23.99%
   Turnover: 3.48%
   Win Rate: 55.89%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $206,880.52
   Total Return: +106.88%
   Annualized Return: +27.42%
   Sharpe Ratio: 1.2948 (annualized)
   Sortino Ratio: 1.8939 (annualized)
   Max Drawdown: 24.06%
   Volatility (Ann.): 18.55%
   Turnover: 3.52%
   Win Rate: 56.03%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $207,817.86
   Total Return: +107.82%
   Annualized Return: +27.61%
   Sharpe Ratio: 1.3035 (annualized)
   Sortino Ratio: 1.9519 (annualized)
   Max Drawdown: 24.06%
   Volatility (Ann.): 18.54%
   Turnover: 3.32%
   Win Rate: 54.97%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $240,021.09
   Total Return: +140.02%
   Annualized Return: +24.47%
   Sharpe Ratio: 1.0073 (annualized)
   Sortino Ratio: 1.4515 (annualized)
   Max Drawdown: 29.16%
   Volatility (Ann.): 22.26%
   Turnover: 3.24%
   Win Rate: 55.31%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $312,840.08
   Total Return: +212.84%
   Annualized Return: +32.99%
   Sharpe Ratio: 1.6066 (annualized)
   Sortino Ratio: 2.4270 (annualized)
   Max Drawdown: 24.06%
   Volatility (Ann.): 17.49%
   Turnover: 3.30%
   Win Rate: 55.81%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00426_shp1p330_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $282,874.70
   Total Return: +182.87%
   Annualized Return: +29.69%
   Sharpe Ratio: 1.4915 (annualized)
   Sortino Ratio: 2.2554 (annualized)
   Max Drawdown: 24.06%
   Volatility (Ann.): 17.11%
   Turnover: 3.30%
   Win Rate: 55.51%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $129,397.40
   Total Return: +29.40%
   Annualized Return: +29.40%
   Sharpe Ratio: 0.9039 (annualized)
   Sortino Ratio: 1.2537 (annualized)
   Max Drawdown: 29.22%
   Volatility (Ann.): 32.21%
   Turnover: 3.51%
   Win Rate: 58.96%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $158,290.29
   Total Return: +58.29%
   Annualized Return: +58.29%
   Sharpe Ratio: 2.6558 (annualized)
   Sortino Ratio: 3.9404 (annualized)
   Max Drawdown: 8.22%
   Volatility (Ann.): 17.19%
   Turnover: 3.97%
   Win Rate: 61.35%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $147,771.07
   Total Return: +47.77%
   Annualized Return: +47.77%
   Sharpe Ratio: 2.4729 (annualized)
   Sortino Ratio: 3.7060 (annualized)
   Max Drawdown: 7.90%
   Volatility (Ann.): 15.55%
   Turnover: 3.66%
   Win Rate: 59.76%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $183,520.80
   Total Return: +83.52%
   Annualized Return: +35.47%
   Sharpe Ratio: 1.2534 (annualized)
   Sortino Ratio: 1.7766 (annualized)
   Max Drawdown: 29.22%
   Volatility (Ann.): 25.26%
   Turnover: 3.31%
   Win Rate: 58.85%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $198,377.98
   Total Return: +98.38%
   Annualized Return: +40.85%
   Sharpe Ratio: 2.0721 (annualized)
   Sortino Ratio: 3.1159 (annualized)
   Max Drawdown: 11.71%
   Volatility (Ann.): 16.25%
   Turnover: 3.39%
   Win Rate: 58.65%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $151,212.53
   Total Return: +51.21%
   Annualized Return: +22.97%
   Sharpe Ratio: 1.2044 (annualized)
   Sortino Ratio: 1.7411 (annualized)
   Max Drawdown: 15.12%
   Volatility (Ann.): 16.72%
   Turnover: 3.37%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $149,723.52
   Total Return: +49.72%
   Annualized Return: +14.40%
   Sharpe Ratio: 0.6011 (annualized)
   Sortino Ratio: 0.8395 (annualized)
   Max Drawdown: 29.22%
   Volatility (Ann.): 23.89%
   Turnover: 3.63%
   Win Rate: 55.63%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $202,236.34
   Total Return: +102.24%
   Annualized Return: +26.46%
   Sharpe Ratio: 1.2629 (annualized)
   Sortino Ratio: 1.8426 (annualized)
   Max Drawdown: 25.21%
   Volatility (Ann.): 18.39%
   Turnover: 3.62%
   Win Rate: 55.89%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $203,769.59
   Total Return: +103.77%
   Annualized Return: +26.78%
   Sharpe Ratio: 1.2750 (annualized)
   Sortino Ratio: 1.9033 (annualized)
   Max Drawdown: 25.21%
   Volatility (Ann.): 18.42%
   Turnover: 3.45%
   Win Rate: 54.97%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $234,531.56
   Total Return: +134.53%
   Annualized Return: +23.75%
   Sharpe Ratio: 0.9847 (annualized)
   Sortino Ratio: 1.4151 (annualized)
   Max Drawdown: 29.22%
   Volatility (Ann.): 22.16%
   Turnover: 3.36%
   Win Rate: 55.31%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $305,068.62
   Total Return: +205.07%
   Annualized Return: +32.16%
   Sharpe Ratio: 1.5844 (annualized)
   Sortino Ratio: 2.3862 (annualized)
   Max Drawdown: 25.21%
   Volatility (Ann.): 17.32%
   Turnover: 3.36%
   Win Rate: 55.91%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00419_shp1p358_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $276,273.89
   Total Return: +176.27%
   Annualized Return: +28.92%
   Sharpe Ratio: 1.4687 (annualized)
   Sortino Ratio: 2.2118 (annualized)
   Max Drawdown: 25.21%
   Volatility (Ann.): 16.95%
   Turnover: 3.35%
   Win Rate: 55.61%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $129,397.40
   Total Return: +29.40%
   Annualized Return: +29.40%
   Sharpe Ratio: 0.9039 (annualized)
   Sortino Ratio: 1.2537 (annualized)
   Max Drawdown: 29.22%
   Volatility (Ann.): 32.21%
   Turnover: 3.51%
   Win Rate: 58.96%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $158,290.29
   Total Return: +58.29%
   Annualized Return: +58.29%
   Sharpe Ratio: 2.6558 (annualized)
   Sortino Ratio: 3.9404 (annualized)
   Max Drawdown: 8.22%
   Volatility (Ann.): 17.19%
   Turnover: 3.97%
   Win Rate: 61.35%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $147,771.07
   Total Return: +47.77%
   Annualized Return: +47.77%
   Sharpe Ratio: 2.4729 (annualized)
   Sortino Ratio: 3.7060 (annualized)
   Max Drawdown: 7.90%
   Volatility (Ann.): 15.55%
   Turnover: 3.66%
   Win Rate: 59.76%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $183,520.80
   Total Return: +83.52%
   Annualized Return: +35.47%
   Sharpe Ratio: 1.2534 (annualized)
   Sortino Ratio: 1.7766 (annualized)
   Max Drawdown: 29.22%
   Volatility (Ann.): 25.26%
   Turnover: 3.31%
   Win Rate: 58.85%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $198,377.98
   Total Return: +98.38%
   Annualized Return: +40.85%
   Sharpe Ratio: 2.0721 (annualized)
   Sortino Ratio: 3.1159 (annualized)
   Max Drawdown: 11.71%
   Volatility (Ann.): 16.25%
   Turnover: 3.39%
   Win Rate: 58.65%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $151,212.53
   Total Return: +51.21%
   Annualized Return: +22.97%
   Sharpe Ratio: 1.2044 (annualized)
   Sortino Ratio: 1.7411 (annualized)
   Max Drawdown: 15.12%
   Volatility (Ann.): 16.72%
   Turnover: 3.37%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $149,723.52
   Total Return: +49.72%
   Annualized Return: +14.40%
   Sharpe Ratio: 0.6011 (annualized)
   Sortino Ratio: 0.8395 (annualized)
   Max Drawdown: 29.22%
   Volatility (Ann.): 23.89%
   Turnover: 3.63%
   Win Rate: 55.63%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $202,236.34
   Total Return: +102.24%
   Annualized Return: +26.46%
   Sharpe Ratio: 1.2629 (annualized)
   Sortino Ratio: 1.8426 (annualized)
   Max Drawdown: 25.21%
   Volatility (Ann.): 18.39%
   Turnover: 3.62%
   Win Rate: 55.89%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $203,769.59
   Total Return: +103.77%
   Annualized Return: +26.78%
   Sharpe Ratio: 1.2750 (annualized)
   Sortino Ratio: 1.9033 (annualized)
   Max Drawdown: 25.21%
   Volatility (Ann.): 18.42%
   Turnover: 3.45%
   Win Rate: 54.97%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $234,531.56
   Total Return: +134.53%
   Annualized Return: +23.75%
   Sharpe Ratio: 0.9847 (annualized)
   Sortino Ratio: 1.4151 (annualized)
   Max Drawdown: 29.22%
   Volatility (Ann.): 22.16%
   Turnover: 3.36%
   Win Rate: 55.31%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $305,068.62
   Total Return: +205.07%
   Annualized Return: +32.16%
   Sharpe Ratio: 1.5844 (annualized)
   Sortino Ratio: 2.3862 (annualized)
   Max Drawdown: 25.21%
   Volatility (Ann.): 17.32%
   Turnover: 3.36%
   Win Rate: 55.91%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00418_shp1p404_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $276,273.89
   Total Return: +176.27%
   Annualized Return: +28.92%
   Sharpe Ratio: 1.4687 (annualized)
   Sortino Ratio: 2.2118 (annualized)
   Max Drawdown: 25.21%
   Volatility (Ann.): 16.95%
   Turnover: 3.35%
   Win Rate: 55.61%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $125,645.56
   Total Return: +25.65%
   Annualized Return: +25.65%
   Sharpe Ratio: 0.8088 (annualized)
   Sortino Ratio: 1.1174 (annualized)
   Max Drawdown: 29.58%
   Volatility (Ann.): 32.43%
   Turnover: 3.04%
   Win Rate: 57.37%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $148,820.86
   Total Return: +48.82%
   Annualized Return: +48.82%
   Sharpe Ratio: 2.2815 (annualized)
   Sortino Ratio: 3.3037 (annualized)
   Max Drawdown: 8.21%
   Volatility (Ann.): 17.30%
   Turnover: 4.00%
   Win Rate: 59.36%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $139,515.54
   Total Return: +39.52%
   Annualized Return: +39.52%
   Sharpe Ratio: 2.1316 (annualized)
   Sortino Ratio: 3.1436 (annualized)
   Max Drawdown: 7.85%
   Volatility (Ann.): 15.32%
   Turnover: 3.81%
   Win Rate: 58.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $170,625.31
   Total Return: +70.63%
   Annualized Return: +30.62%
   Sharpe Ratio: 1.1009 (annualized)
   Sortino Ratio: 1.5519 (annualized)
   Max Drawdown: 29.58%
   Volatility (Ann.): 25.49%
   Turnover: 3.62%
   Win Rate: 57.46%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $186,700.83
   Total Return: +86.70%
   Annualized Return: +36.64%
   Sharpe Ratio: 1.8574 (annualized)
   Sortino Ratio: 2.7502 (annualized)
   Max Drawdown: 11.55%
   Volatility (Ann.): 16.52%
   Turnover: 3.83%
   Win Rate: 57.65%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $138,651.61
   Total Return: +38.65%
   Annualized Return: +17.75%
   Sharpe Ratio: 0.9273 (annualized)
   Sortino Ratio: 1.3216 (annualized)
   Max Drawdown: 16.68%
   Volatility (Ann.): 17.10%
   Turnover: 3.70%
   Win Rate: 55.27%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $141,013.72
   Total Return: +41.01%
   Annualized Return: +12.14%
   Sharpe Ratio: 0.5102 (annualized)
   Sortino Ratio: 0.7123 (annualized)
   Max Drawdown: 29.58%
   Volatility (Ann.): 24.52%
   Turnover: 3.73%
   Win Rate: 54.30%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $192,009.98
   Total Return: +92.01%
   Annualized Return: +24.29%
   Sharpe Ratio: 1.1247 (annualized)
   Sortino Ratio: 1.6344 (annualized)
   Max Drawdown: 25.84%
   Volatility (Ann.): 19.26%
   Turnover: 3.86%
   Win Rate: 54.83%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $195,282.13
   Total Return: +95.28%
   Annualized Return: +24.99%
   Sharpe Ratio: 1.1596 (annualized)
   Sortino Ratio: 1.7278 (annualized)
   Max Drawdown: 25.84%
   Volatility (Ann.): 19.14%
   Turnover: 3.62%
   Win Rate: 54.04%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $225,512.44
   Total Return: +125.51%
   Annualized Return: +22.54%
   Sharpe Ratio: 0.9207 (annualized)
   Sortino Ratio: 1.3222 (annualized)
   Max Drawdown: 29.58%
   Volatility (Ann.): 22.79%
   Turnover: 3.52%
   Win Rate: 54.02%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $298,734.89
   Total Return: +198.73%
   Annualized Return: +31.47%
   Sharpe Ratio: 1.4934 (annualized)
   Sortino Ratio: 2.2416 (annualized)
   Max Drawdown: 25.84%
   Volatility (Ann.): 18.12%
   Turnover: 3.69%
   Win Rate: 55.01%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/exp6_tape_hw_ep00417_shp1p360_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=False | num_quantiles=17
   🎛️ Eval dirichlet: activation=cross_softplus | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=50.0 | epsilon={'max': 0.2, 'min': 0.02}
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
   Final Portfolio Value: $271,713.19
   Total Return: +171.71%
   Annualized Return: +28.39%
   Sharpe Ratio: 1.3945 (annualized)
   Sortino Ratio: 2.1001 (annualized)
   Max Drawdown: 25.84%
   Volatility (Ann.): 17.64%
   Turnover: 3.74%
   Win Rate: 54.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.000, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

  
    

    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }


  
    
      
      checkpoint_label
      checkpoint_prefix
      years
      horizon_days
      det_sharpe_median
      det_return_median
      det_mdd_median
      det_turnover_median
      selection_score
    
  
  
    
      0
      high_watermark__ep0433
      /content/eval_restore/tcn_fusion_results/high_...
      1
      252
      2.492752
      0.506000
      0.086038
      0.024809
      2.531245
    
    
      1
      high_watermark__ep0426
      /content/eval_restore/tcn_fusion_results/high_...
      2
      504
      1.267035
      0.852401
      0.145721
      0.031838
      1.332327
    
    
      2
      high_watermark__ep0426
      /content/eval_restore/tcn_fusion_results/high_...
      3
      756
      1.294817
      1.068805
      0.240562
      0.034837
      1.336701
    
    
      3
      high_watermark__ep0433
      /content/eval_restore/tcn_fusion_results/high_...
      4
      1008
      1.533250
      2.269244
      0.276462
      0.023620
      1.791213
    
  


    

  
    

  
    
  
    

  
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
  

    
      const buttonEl =
        document.querySelector('#df-81c5edc3-20ed-4ab7-9421-184b955b7879 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-81c5edc3-20ed-4ab7-9421-184b955b7879');
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
    
  


  
    
      .colab-df-generate {
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

      .colab-df-generate:hover {
        background-color: #E2EBFA;
        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
        fill: #174EA6;
      }

      [theme=dark] .colab-df-generate {
        background-color: #3B4455;
        fill: #D2E3FC;
      }

      [theme=dark] .colab-df-generate:hover {
        background-color: #434B5C;
        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
        fill: #FFFFFF;
      }
    
    

  
    
  
    
    
      (() => {
      const buttonEl =
        document.querySelector('#id_575d04a9-1342-44ca-987b-451f3b198341 button.colab-df-generate');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      buttonEl.onclick = () => {
        google.colab.notebook.generateWithVariable('deterministic_horizon_winners');
      }
      })();
    
  

    
  
PosixPath('/content/eval_restore/tcn_fusion_results/analysis/run21/run21_eval_20260328_082510_utc/01_checkpoint_selection/deterministic_horizon_winners.csv')