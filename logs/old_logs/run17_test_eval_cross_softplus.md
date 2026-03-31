[LOOK] Stage 1/2: deterministic sweep (no stochastic during sweep)

[1/11] Sweep checkpoint: high_watermark__ep0001__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $129,176.79
   Total Return: +29.18%
   Annualized Return: +29.18%
   Sharpe Ratio: 0.8763 (annualized)
   Sortino Ratio: 1.2458 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 33.49%
   Turnover: 1.40%
   Win Rate: 54.58%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.392, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $162,240.14
   Total Return: +62.24%
   Annualized Return: +62.24%
   Sharpe Ratio: 2.2104 (annualized)
   Sortino Ratio: 3.3617 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 22.22%
   Turnover: 0.97%
   Win Rate: 54.98%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.410, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $160,977.01
   Total Return: +60.98%
   Annualized Return: +60.98%
   Sharpe Ratio: 2.5535 (annualized)
   Sortino Ratio: 4.0014 (annualized)
   Max Drawdown: 10.55%
   Volatility (Ann.): 18.64%
   Turnover: 0.74%
   Win Rate: 55.38%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.450, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $154,364.21
   Total Return: +54.36%
   Annualized Return: +54.36%
   Sharpe Ratio: 2.4595 (annualized)
   Sortino Ratio: 3.9314 (annualized)
   Max Drawdown: 7.64%
   Volatility (Ann.): 17.56%
   Turnover: 0.67%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.397, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $199,375.58
   Total Return: +99.38%
   Annualized Return: +41.20%
   Sharpe Ratio: 1.3547 (annualized)
   Sortino Ratio: 1.9706 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 26.71%
   Turnover: 0.95%
   Win Rate: 55.47%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.397, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $222,973.42
   Total Return: +122.97%
   Annualized Return: +49.32%
   Sharpe Ratio: 1.9733 (annualized)
   Sortino Ratio: 3.0228 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 20.43%
   Turnover: 0.77%
   Win Rate: 55.27%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.384, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $154,397.41
   Total Return: +54.40%
   Annualized Return: +24.26%
   Sharpe Ratio: 1.0353 (annualized)
   Sortino Ratio: 1.5050 (annualized)
   Max Drawdown: 20.97%
   Volatility (Ann.): 21.31%
   Turnover: 0.66%
   Win Rate: 52.68%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.397, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $144,850.30
   Total Return: +44.85%
   Annualized Return: +20.35%
   Sharpe Ratio: 0.8225 (annualized)
   Sortino Ratio: 1.2147 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 23.53%
   Turnover: 0.67%
   Win Rate: 52.88%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.385, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $187,087.48
   Total Return: +87.09%
   Annualized Return: +23.22%
   Sharpe Ratio: 0.8317 (annualized)
   Sortino Ratio: 1.2042 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 27.23%
   Turnover: 0.86%
   Win Rate: 53.25%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.389, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $253,987.84
   Total Return: +153.99%
   Annualized Return: +36.44%
   Sharpe Ratio: 1.3699 (annualized)
   Sortino Ratio: 2.0615 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 23.25%
   Turnover: 0.77%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.386, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $249,319.33
   Total Return: +149.32%
   Annualized Return: +35.60%
   Sharpe Ratio: 1.3833 (annualized)
   Sortino Ratio: 2.1174 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 22.44%
   Turnover: 0.72%
   Win Rate: 52.85%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.396, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $231,905.16
   Total Return: +131.91%
   Annualized Return: +32.36%
   Sharpe Ratio: 1.3186 (annualized)
   Sortino Ratio: 2.0152 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 21.56%
   Turnover: 0.71%
   Win Rate: 54.04%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.381, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $299,526.83
   Total Return: +199.53%
   Annualized Return: +31.56%
   Sharpe Ratio: 1.1426 (annualized)
   Sortino Ratio: 1.6881 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 25.05%
   Turnover: 0.84%
   Win Rate: 54.02%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.385, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $417,356.80
   Total Return: +317.36%
   Annualized Return: +42.93%
   Sharpe Ratio: 1.6800 (annualized)
   Sortino Ratio: 2.5830 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 21.49%
   Turnover: 0.75%
   Win Rate: 54.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.380, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $407,518.55
   Total Return: +307.52%
   Annualized Return: +42.08%
   Sharpe Ratio: 1.7086 (annualized)
   Sortino Ratio: 2.6448 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 20.68%
   Turnover: 0.71%
   Win Rate: 54.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.384, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $366,051.16
   Total Return: +266.05%
   Annualized Return: +38.32%
   Sharpe Ratio: 1.5923 (annualized)
   Sortino Ratio: 2.4431 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 20.47%
   Turnover: 0.70%
   Win Rate: 55.81%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.358, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[2/11] Sweep checkpoint: high_watermark__ep0006__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $129,176.79
   Total Return: +29.18%
   Annualized Return: +29.18%
   Sharpe Ratio: 0.8763 (annualized)
   Sortino Ratio: 1.2458 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 33.49%
   Turnover: 1.40%
   Win Rate: 54.58%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.392, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $162,240.14
   Total Return: +62.24%
   Annualized Return: +62.24%
   Sharpe Ratio: 2.2104 (annualized)
   Sortino Ratio: 3.3617 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 22.22%
   Turnover: 0.97%
   Win Rate: 54.98%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.410, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $160,977.01
   Total Return: +60.98%
   Annualized Return: +60.98%
   Sharpe Ratio: 2.5535 (annualized)
   Sortino Ratio: 4.0014 (annualized)
   Max Drawdown: 10.55%
   Volatility (Ann.): 18.64%
   Turnover: 0.74%
   Win Rate: 55.38%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.450, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $154,364.21
   Total Return: +54.36%
   Annualized Return: +54.36%
   Sharpe Ratio: 2.4595 (annualized)
   Sortino Ratio: 3.9314 (annualized)
   Max Drawdown: 7.64%
   Volatility (Ann.): 17.56%
   Turnover: 0.67%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.397, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $199,375.58
   Total Return: +99.38%
   Annualized Return: +41.20%
   Sharpe Ratio: 1.3547 (annualized)
   Sortino Ratio: 1.9706 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 26.71%
   Turnover: 0.95%
   Win Rate: 55.47%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.397, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $222,973.42
   Total Return: +122.97%
   Annualized Return: +49.32%
   Sharpe Ratio: 1.9733 (annualized)
   Sortino Ratio: 3.0228 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 20.43%
   Turnover: 0.77%
   Win Rate: 55.27%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.384, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $154,397.41
   Total Return: +54.40%
   Annualized Return: +24.26%
   Sharpe Ratio: 1.0353 (annualized)
   Sortino Ratio: 1.5050 (annualized)
   Max Drawdown: 20.97%
   Volatility (Ann.): 21.31%
   Turnover: 0.66%
   Win Rate: 52.68%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.397, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $144,850.30
   Total Return: +44.85%
   Annualized Return: +20.35%
   Sharpe Ratio: 0.8225 (annualized)
   Sortino Ratio: 1.2147 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 23.53%
   Turnover: 0.67%
   Win Rate: 52.88%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.385, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $187,087.48
   Total Return: +87.09%
   Annualized Return: +23.22%
   Sharpe Ratio: 0.8317 (annualized)
   Sortino Ratio: 1.2042 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 27.23%
   Turnover: 0.86%
   Win Rate: 53.25%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.389, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $253,987.84
   Total Return: +153.99%
   Annualized Return: +36.44%
   Sharpe Ratio: 1.3699 (annualized)
   Sortino Ratio: 2.0615 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 23.25%
   Turnover: 0.77%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.386, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $249,319.33
   Total Return: +149.32%
   Annualized Return: +35.60%
   Sharpe Ratio: 1.3833 (annualized)
   Sortino Ratio: 2.1174 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 22.44%
   Turnover: 0.72%
   Win Rate: 52.85%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.396, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $231,905.16
   Total Return: +131.91%
   Annualized Return: +32.36%
   Sharpe Ratio: 1.3186 (annualized)
   Sortino Ratio: 2.0152 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 21.56%
   Turnover: 0.71%
   Win Rate: 54.04%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.381, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $299,526.83
   Total Return: +199.53%
   Annualized Return: +31.56%
   Sharpe Ratio: 1.1426 (annualized)
   Sortino Ratio: 1.6881 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 25.05%
   Turnover: 0.84%
   Win Rate: 54.02%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.385, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $417,356.80
   Total Return: +317.36%
   Annualized Return: +42.93%
   Sharpe Ratio: 1.6800 (annualized)
   Sortino Ratio: 2.5830 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 21.49%
   Turnover: 0.75%
   Win Rate: 54.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.380, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $407,518.55
   Total Return: +307.52%
   Annualized Return: +42.08%
   Sharpe Ratio: 1.7086 (annualized)
   Sortino Ratio: 2.6448 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 20.68%
   Turnover: 0.71%
   Win Rate: 54.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.384, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00006_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $366,051.16
   Total Return: +266.05%
   Annualized Return: +38.32%
   Sharpe Ratio: 1.5923 (annualized)
   Sortino Ratio: 2.4431 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 20.47%
   Turnover: 0.70%
   Win Rate: 55.81%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.358, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[3/11] Sweep checkpoint: high_watermark__ep0007__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $129,176.79
   Total Return: +29.18%
   Annualized Return: +29.18%
   Sharpe Ratio: 0.8763 (annualized)
   Sortino Ratio: 1.2458 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 33.49%
   Turnover: 1.40%
   Win Rate: 54.58%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.392, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $162,240.14
   Total Return: +62.24%
   Annualized Return: +62.24%
   Sharpe Ratio: 2.2104 (annualized)
   Sortino Ratio: 3.3617 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 22.22%
   Turnover: 0.97%
   Win Rate: 54.98%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.410, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $160,977.01
   Total Return: +60.98%
   Annualized Return: +60.98%
   Sharpe Ratio: 2.5535 (annualized)
   Sortino Ratio: 4.0014 (annualized)
   Max Drawdown: 10.55%
   Volatility (Ann.): 18.64%
   Turnover: 0.74%
   Win Rate: 55.38%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.450, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $154,364.21
   Total Return: +54.36%
   Annualized Return: +54.36%
   Sharpe Ratio: 2.4595 (annualized)
   Sortino Ratio: 3.9314 (annualized)
   Max Drawdown: 7.64%
   Volatility (Ann.): 17.56%
   Turnover: 0.67%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.397, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $199,375.58
   Total Return: +99.38%
   Annualized Return: +41.20%
   Sharpe Ratio: 1.3547 (annualized)
   Sortino Ratio: 1.9706 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 26.71%
   Turnover: 0.95%
   Win Rate: 55.47%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.397, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $222,973.42
   Total Return: +122.97%
   Annualized Return: +49.32%
   Sharpe Ratio: 1.9733 (annualized)
   Sortino Ratio: 3.0228 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 20.43%
   Turnover: 0.77%
   Win Rate: 55.27%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.384, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $154,397.41
   Total Return: +54.40%
   Annualized Return: +24.26%
   Sharpe Ratio: 1.0353 (annualized)
   Sortino Ratio: 1.5050 (annualized)
   Max Drawdown: 20.97%
   Volatility (Ann.): 21.31%
   Turnover: 0.66%
   Win Rate: 52.68%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.397, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $144,850.30
   Total Return: +44.85%
   Annualized Return: +20.35%
   Sharpe Ratio: 0.8225 (annualized)
   Sortino Ratio: 1.2147 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 23.53%
   Turnover: 0.67%
   Win Rate: 52.88%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.385, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $187,087.48
   Total Return: +87.09%
   Annualized Return: +23.22%
   Sharpe Ratio: 0.8317 (annualized)
   Sortino Ratio: 1.2042 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 27.23%
   Turnover: 0.86%
   Win Rate: 53.25%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.389, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $253,987.84
   Total Return: +153.99%
   Annualized Return: +36.44%
   Sharpe Ratio: 1.3699 (annualized)
   Sortino Ratio: 2.0615 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 23.25%
   Turnover: 0.77%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.386, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $249,319.33
   Total Return: +149.32%
   Annualized Return: +35.60%
   Sharpe Ratio: 1.3833 (annualized)
   Sortino Ratio: 2.1174 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 22.44%
   Turnover: 0.72%
   Win Rate: 52.85%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.396, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $231,905.16
   Total Return: +131.91%
   Annualized Return: +32.36%
   Sharpe Ratio: 1.3186 (annualized)
   Sortino Ratio: 2.0152 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 21.56%
   Turnover: 0.71%
   Win Rate: 54.04%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.381, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $299,526.83
   Total Return: +199.53%
   Annualized Return: +31.56%
   Sharpe Ratio: 1.1426 (annualized)
   Sortino Ratio: 1.6881 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 25.05%
   Turnover: 0.84%
   Win Rate: 54.02%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.385, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $417,356.80
   Total Return: +317.36%
   Annualized Return: +42.93%
   Sharpe Ratio: 1.6800 (annualized)
   Sortino Ratio: 2.5830 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 21.49%
   Turnover: 0.75%
   Win Rate: 54.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.380, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $407,518.55
   Total Return: +307.52%
   Annualized Return: +42.08%
   Sharpe Ratio: 1.7086 (annualized)
   Sortino Ratio: 2.6448 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 20.68%
   Turnover: 0.71%
   Win Rate: 54.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.384, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p893_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $366,051.16
   Total Return: +266.05%
   Annualized Return: +38.32%
   Sharpe Ratio: 1.5923 (annualized)
   Sortino Ratio: 2.4431 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 20.47%
   Turnover: 0.70%
   Win Rate: 55.81%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.358, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[4/11] Sweep checkpoint: high_watermark__ep0008__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $129,176.79
   Total Return: +29.18%
   Annualized Return: +29.18%
   Sharpe Ratio: 0.8763 (annualized)
   Sortino Ratio: 1.2458 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 33.49%
   Turnover: 1.40%
   Win Rate: 54.58%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.392, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $162,240.14
   Total Return: +62.24%
   Annualized Return: +62.24%
   Sharpe Ratio: 2.2104 (annualized)
   Sortino Ratio: 3.3617 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 22.22%
   Turnover: 0.97%
   Win Rate: 54.98%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.410, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $160,977.01
   Total Return: +60.98%
   Annualized Return: +60.98%
   Sharpe Ratio: 2.5535 (annualized)
   Sortino Ratio: 4.0014 (annualized)
   Max Drawdown: 10.55%
   Volatility (Ann.): 18.64%
   Turnover: 0.74%
   Win Rate: 55.38%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.450, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $154,364.21
   Total Return: +54.36%
   Annualized Return: +54.36%
   Sharpe Ratio: 2.4595 (annualized)
   Sortino Ratio: 3.9314 (annualized)
   Max Drawdown: 7.64%
   Volatility (Ann.): 17.56%
   Turnover: 0.67%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.397, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $199,375.58
   Total Return: +99.38%
   Annualized Return: +41.20%
   Sharpe Ratio: 1.3547 (annualized)
   Sortino Ratio: 1.9706 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 26.71%
   Turnover: 0.95%
   Win Rate: 55.47%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.397, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $222,973.42
   Total Return: +122.97%
   Annualized Return: +49.32%
   Sharpe Ratio: 1.9733 (annualized)
   Sortino Ratio: 3.0228 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 20.43%
   Turnover: 0.77%
   Win Rate: 55.27%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.384, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $154,397.41
   Total Return: +54.40%
   Annualized Return: +24.26%
   Sharpe Ratio: 1.0353 (annualized)
   Sortino Ratio: 1.5050 (annualized)
   Max Drawdown: 20.97%
   Volatility (Ann.): 21.31%
   Turnover: 0.66%
   Win Rate: 52.68%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.397, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $144,850.30
   Total Return: +44.85%
   Annualized Return: +20.35%
   Sharpe Ratio: 0.8225 (annualized)
   Sortino Ratio: 1.2147 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 23.53%
   Turnover: 0.67%
   Win Rate: 52.88%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.385, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $187,087.48
   Total Return: +87.09%
   Annualized Return: +23.22%
   Sharpe Ratio: 0.8317 (annualized)
   Sortino Ratio: 1.2042 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 27.23%
   Turnover: 0.86%
   Win Rate: 53.25%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.389, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $253,987.84
   Total Return: +153.99%
   Annualized Return: +36.44%
   Sharpe Ratio: 1.3699 (annualized)
   Sortino Ratio: 2.0615 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 23.25%
   Turnover: 0.77%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.386, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $249,319.33
   Total Return: +149.32%
   Annualized Return: +35.60%
   Sharpe Ratio: 1.3833 (annualized)
   Sortino Ratio: 2.1174 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 22.44%
   Turnover: 0.72%
   Win Rate: 52.85%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.396, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $231,905.16
   Total Return: +131.91%
   Annualized Return: +32.36%
   Sharpe Ratio: 1.3186 (annualized)
   Sortino Ratio: 2.0152 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 21.56%
   Turnover: 0.71%
   Win Rate: 54.04%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.381, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $299,526.83
   Total Return: +199.53%
   Annualized Return: +31.56%
   Sharpe Ratio: 1.1426 (annualized)
   Sortino Ratio: 1.6881 (annualized)
   Max Drawdown: 26.52%
   Volatility (Ann.): 25.05%
   Turnover: 0.84%
   Win Rate: 54.02%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.385, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $417,356.80
   Total Return: +317.36%
   Annualized Return: +42.93%
   Sharpe Ratio: 1.6800 (annualized)
   Sortino Ratio: 2.5830 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 21.49%
   Turnover: 0.75%
   Win Rate: 54.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.380, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $407,518.55
   Total Return: +307.52%
   Annualized Return: +42.08%
   Sharpe Ratio: 1.7086 (annualized)
   Sortino Ratio: 2.6448 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 20.68%
   Turnover: 0.71%
   Win Rate: 54.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.384, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p099_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $366,051.16
   Total Return: +266.05%
   Annualized Return: +38.32%
   Sharpe Ratio: 1.5923 (annualized)
   Sortino Ratio: 2.4431 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 20.47%
   Turnover: 0.70%
   Win Rate: 55.81%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.358, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[5/11] Sweep checkpoint: high_watermark__ep0010__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $116,807.75
   Total Return: +16.81%
   Annualized Return: +16.81%
   Sharpe Ratio: 0.5692 (annualized)
   Sortino Ratio: 0.7811 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 34.35%
   Turnover: 0.74%
   Win Rate: 54.98%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $160,505.42
   Total Return: +60.51%
   Annualized Return: +60.51%
   Sharpe Ratio: 2.2060 (annualized)
   Sortino Ratio: 3.3457 (annualized)
   Max Drawdown: 10.52%
   Volatility (Ann.): 21.72%
   Turnover: 0.63%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $151,979.61
   Total Return: +51.98%
   Annualized Return: +51.98%
   Sharpe Ratio: 2.4233 (annualized)
   Sortino Ratio: 3.7111 (annualized)
   Max Drawdown: 10.34%
   Volatility (Ann.): 17.14%
   Turnover: 0.68%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.174, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $145,026.55
   Total Return: +45.03%
   Annualized Return: +45.03%
   Sharpe Ratio: 2.3750 (annualized)
   Sortino Ratio: 3.7422 (annualized)
   Max Drawdown: 6.39%
   Volatility (Ann.): 15.39%
   Turnover: 0.56%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $167,743.04
   Total Return: +67.74%
   Annualized Return: +29.52%
   Sharpe Ratio: 1.0365 (annualized)
   Sortino Ratio: 1.4504 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 26.51%
   Turnover: 0.62%
   Win Rate: 56.26%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $213,236.88
   Total Return: +113.24%
   Annualized Return: +46.03%
   Sharpe Ratio: 2.0133 (annualized)
   Sortino Ratio: 3.0666 (annualized)
   Max Drawdown: 10.52%
   Volatility (Ann.): 18.75%
   Turnover: 0.55%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $149,770.62
   Total Return: +49.77%
   Annualized Return: +22.38%
   Sharpe Ratio: 1.0847 (annualized)
   Sortino Ratio: 1.5606 (annualized)
   Max Drawdown: 17.27%
   Volatility (Ann.): 18.40%
   Turnover: 0.55%
   Win Rate: 54.08%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.170, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $138,157.50
   Total Return: +38.16%
   Annualized Return: +17.54%
   Sharpe Ratio: 0.8079 (annualized)
   Sortino Ratio: 1.1865 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 20.09%
   Turnover: 0.49%
   Win Rate: 52.49%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $159,798.04
   Total Return: +59.80%
   Annualized Return: +16.91%
   Sharpe Ratio: 0.6616 (annualized)
   Sortino Ratio: 0.9312 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 25.65%
   Turnover: 0.55%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $232,121.07
   Total Return: +132.12%
   Annualized Return: +32.41%
   Sharpe Ratio: 1.3740 (annualized)
   Sortino Ratio: 2.0528 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 20.56%
   Turnover: 0.52%
   Win Rate: 54.44%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $215,125.50
   Total Return: +115.13%
   Annualized Return: +29.09%
   Sharpe Ratio: 1.3252 (annualized)
   Sortino Ratio: 1.9945 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 19.20%
   Turnover: 0.54%
   Win Rate: 53.38%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.169, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $202,696.21
   Total Return: +102.70%
   Annualized Return: +26.56%
   Sharpe Ratio: 1.2690 (annualized)
   Sortino Ratio: 1.9112 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 18.36%
   Turnover: 0.51%
   Win Rate: 53.91%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $234,445.88
   Total Return: +134.45%
   Annualized Return: +23.74%
   Sharpe Ratio: 0.9464 (annualized)
   Sortino Ratio: 1.3516 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 23.33%
   Turnover: 0.55%
   Win Rate: 54.32%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $364,486.66
   Total Return: +264.49%
   Annualized Return: +38.17%
   Sharpe Ratio: 1.6989 (annualized)
   Sortino Ratio: 2.5839 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 18.95%
   Turnover: 0.53%
   Win Rate: 55.51%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $337,015.49
   Total Return: +237.02%
   Annualized Return: +35.49%
   Sharpe Ratio: 1.6926 (annualized)
   Sortino Ratio: 2.5758 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 17.73%
   Turnover: 0.54%
   Win Rate: 55.31%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.168, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $304,580.87
   Total Return: +204.58%
   Annualized Return: +32.11%
   Sharpe Ratio: 1.5804 (annualized)
   Sortino Ratio: 2.3929 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 17.34%
   Turnover: 0.51%
   Win Rate: 55.61%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[6/11] Sweep checkpoint: high_watermark__ep0011__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $116,807.75
   Total Return: +16.81%
   Annualized Return: +16.81%
   Sharpe Ratio: 0.5692 (annualized)
   Sortino Ratio: 0.7811 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 34.35%
   Turnover: 0.74%
   Win Rate: 54.98%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $160,505.42
   Total Return: +60.51%
   Annualized Return: +60.51%
   Sharpe Ratio: 2.2060 (annualized)
   Sortino Ratio: 3.3457 (annualized)
   Max Drawdown: 10.52%
   Volatility (Ann.): 21.72%
   Turnover: 0.63%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $151,979.61
   Total Return: +51.98%
   Annualized Return: +51.98%
   Sharpe Ratio: 2.4233 (annualized)
   Sortino Ratio: 3.7111 (annualized)
   Max Drawdown: 10.34%
   Volatility (Ann.): 17.14%
   Turnover: 0.68%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.174, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $145,026.55
   Total Return: +45.03%
   Annualized Return: +45.03%
   Sharpe Ratio: 2.3750 (annualized)
   Sortino Ratio: 3.7422 (annualized)
   Max Drawdown: 6.39%
   Volatility (Ann.): 15.39%
   Turnover: 0.56%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $167,743.04
   Total Return: +67.74%
   Annualized Return: +29.52%
   Sharpe Ratio: 1.0365 (annualized)
   Sortino Ratio: 1.4504 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 26.51%
   Turnover: 0.62%
   Win Rate: 56.26%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $213,236.88
   Total Return: +113.24%
   Annualized Return: +46.03%
   Sharpe Ratio: 2.0133 (annualized)
   Sortino Ratio: 3.0666 (annualized)
   Max Drawdown: 10.52%
   Volatility (Ann.): 18.75%
   Turnover: 0.55%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $149,770.62
   Total Return: +49.77%
   Annualized Return: +22.38%
   Sharpe Ratio: 1.0847 (annualized)
   Sortino Ratio: 1.5606 (annualized)
   Max Drawdown: 17.27%
   Volatility (Ann.): 18.40%
   Turnover: 0.55%
   Win Rate: 54.08%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.170, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $138,157.50
   Total Return: +38.16%
   Annualized Return: +17.54%
   Sharpe Ratio: 0.8079 (annualized)
   Sortino Ratio: 1.1865 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 20.09%
   Turnover: 0.49%
   Win Rate: 52.49%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $159,798.04
   Total Return: +59.80%
   Annualized Return: +16.91%
   Sharpe Ratio: 0.6616 (annualized)
   Sortino Ratio: 0.9312 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 25.65%
   Turnover: 0.55%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $232,121.07
   Total Return: +132.12%
   Annualized Return: +32.41%
   Sharpe Ratio: 1.3740 (annualized)
   Sortino Ratio: 2.0528 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 20.56%
   Turnover: 0.52%
   Win Rate: 54.44%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $215,125.50
   Total Return: +115.13%
   Annualized Return: +29.09%
   Sharpe Ratio: 1.3252 (annualized)
   Sortino Ratio: 1.9945 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 19.20%
   Turnover: 0.54%
   Win Rate: 53.38%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.169, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $202,696.21
   Total Return: +102.70%
   Annualized Return: +26.56%
   Sharpe Ratio: 1.2690 (annualized)
   Sortino Ratio: 1.9112 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 18.36%
   Turnover: 0.51%
   Win Rate: 53.91%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $234,445.88
   Total Return: +134.45%
   Annualized Return: +23.74%
   Sharpe Ratio: 0.9464 (annualized)
   Sortino Ratio: 1.3516 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 23.33%
   Turnover: 0.55%
   Win Rate: 54.32%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $364,486.66
   Total Return: +264.49%
   Annualized Return: +38.17%
   Sharpe Ratio: 1.6989 (annualized)
   Sortino Ratio: 2.5839 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 18.95%
   Turnover: 0.53%
   Win Rate: 55.51%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $337,015.49
   Total Return: +237.02%
   Annualized Return: +35.49%
   Sharpe Ratio: 1.6926 (annualized)
   Sortino Ratio: 2.5758 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 17.73%
   Turnover: 0.54%
   Win Rate: 55.31%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.168, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00011_shp0p871_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $304,580.87
   Total Return: +204.58%
   Annualized Return: +32.11%
   Sharpe Ratio: 1.5804 (annualized)
   Sortino Ratio: 2.3929 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 17.34%
   Turnover: 0.51%
   Win Rate: 55.61%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[7/11] Sweep checkpoint: high_watermark__ep0013__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $116,807.75
   Total Return: +16.81%
   Annualized Return: +16.81%
   Sharpe Ratio: 0.5692 (annualized)
   Sortino Ratio: 0.7811 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 34.35%
   Turnover: 0.74%
   Win Rate: 54.98%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $160,505.42
   Total Return: +60.51%
   Annualized Return: +60.51%
   Sharpe Ratio: 2.2060 (annualized)
   Sortino Ratio: 3.3457 (annualized)
   Max Drawdown: 10.52%
   Volatility (Ann.): 21.72%
   Turnover: 0.63%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $151,979.61
   Total Return: +51.98%
   Annualized Return: +51.98%
   Sharpe Ratio: 2.4233 (annualized)
   Sortino Ratio: 3.7111 (annualized)
   Max Drawdown: 10.34%
   Volatility (Ann.): 17.14%
   Turnover: 0.68%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.174, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $145,026.55
   Total Return: +45.03%
   Annualized Return: +45.03%
   Sharpe Ratio: 2.3750 (annualized)
   Sortino Ratio: 3.7422 (annualized)
   Max Drawdown: 6.39%
   Volatility (Ann.): 15.39%
   Turnover: 0.56%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $167,743.04
   Total Return: +67.74%
   Annualized Return: +29.52%
   Sharpe Ratio: 1.0365 (annualized)
   Sortino Ratio: 1.4504 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 26.51%
   Turnover: 0.62%
   Win Rate: 56.26%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $213,236.88
   Total Return: +113.24%
   Annualized Return: +46.03%
   Sharpe Ratio: 2.0133 (annualized)
   Sortino Ratio: 3.0666 (annualized)
   Max Drawdown: 10.52%
   Volatility (Ann.): 18.75%
   Turnover: 0.55%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $149,770.62
   Total Return: +49.77%
   Annualized Return: +22.38%
   Sharpe Ratio: 1.0847 (annualized)
   Sortino Ratio: 1.5606 (annualized)
   Max Drawdown: 17.27%
   Volatility (Ann.): 18.40%
   Turnover: 0.55%
   Win Rate: 54.08%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.170, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $138,157.50
   Total Return: +38.16%
   Annualized Return: +17.54%
   Sharpe Ratio: 0.8079 (annualized)
   Sortino Ratio: 1.1865 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 20.09%
   Turnover: 0.49%
   Win Rate: 52.49%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $159,798.04
   Total Return: +59.80%
   Annualized Return: +16.91%
   Sharpe Ratio: 0.6616 (annualized)
   Sortino Ratio: 0.9312 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 25.65%
   Turnover: 0.55%
   Win Rate: 53.51%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $232,121.07
   Total Return: +132.12%
   Annualized Return: +32.41%
   Sharpe Ratio: 1.3740 (annualized)
   Sortino Ratio: 2.0528 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 20.56%
   Turnover: 0.52%
   Win Rate: 54.44%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $215,125.50
   Total Return: +115.13%
   Annualized Return: +29.09%
   Sharpe Ratio: 1.3252 (annualized)
   Sortino Ratio: 1.9945 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 19.20%
   Turnover: 0.54%
   Win Rate: 53.38%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.169, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $202,696.21
   Total Return: +102.70%
   Annualized Return: +26.56%
   Sharpe Ratio: 1.2690 (annualized)
   Sortino Ratio: 1.9112 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 18.36%
   Turnover: 0.51%
   Win Rate: 53.91%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $234,445.88
   Total Return: +134.45%
   Annualized Return: +23.74%
   Sharpe Ratio: 0.9464 (annualized)
   Sortino Ratio: 1.3516 (annualized)
   Max Drawdown: 32.18%
   Volatility (Ann.): 23.33%
   Turnover: 0.55%
   Win Rate: 54.32%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $364,486.66
   Total Return: +264.49%
   Annualized Return: +38.17%
   Sharpe Ratio: 1.6989 (annualized)
   Sortino Ratio: 2.5839 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 18.95%
   Turnover: 0.53%
   Win Rate: 55.51%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $337,015.49
   Total Return: +237.02%
   Annualized Return: +35.49%
   Sharpe Ratio: 1.6926 (annualized)
   Sortino Ratio: 2.5758 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 17.73%
   Turnover: 0.54%
   Win Rate: 55.31%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.168, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00013_shp1p094_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $304,580.87
   Total Return: +204.58%
   Annualized Return: +32.11%
   Sharpe Ratio: 1.5804 (annualized)
   Sortino Ratio: 2.3929 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 17.34%
   Turnover: 0.51%
   Win Rate: 55.61%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[8/11] Sweep checkpoint: high_watermark__ep0020__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $112,219.89
   Total Return: +12.22%
   Annualized Return: +12.22%
   Sharpe Ratio: 0.4507 (annualized)
   Sortino Ratio: 0.6202 (annualized)
   Max Drawdown: 32.56%
   Volatility (Ann.): 34.74%
   Turnover: 1.08%
   Win Rate: 53.78%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.443, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $156,681.62
   Total Return: +56.68%
   Annualized Return: +56.68%
   Sharpe Ratio: 1.9677 (annualized)
   Sortino Ratio: 2.9807 (annualized)
   Max Drawdown: 10.73%
   Volatility (Ann.): 23.30%
   Turnover: 1.07%
   Win Rate: 53.78%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.355, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $147,502.22
   Total Return: +47.50%
   Annualized Return: +47.50%
   Sharpe Ratio: 2.1954 (annualized)
   Sortino Ratio: 3.3649 (annualized)
   Max Drawdown: 10.62%
   Volatility (Ann.): 17.59%
   Turnover: 1.04%
   Win Rate: 54.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.329, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $141,128.62
   Total Return: +41.13%
   Annualized Return: +41.13%
   Sharpe Ratio: 2.1956 (annualized)
   Sortino Ratio: 3.4245 (annualized)
   Max Drawdown: 6.31%
   Volatility (Ann.): 15.40%
   Turnover: 0.81%
   Win Rate: 56.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.300, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $155,746.37
   Total Return: +55.75%
   Annualized Return: +24.80%
   Sharpe Ratio: 0.8902 (annualized)
   Sortino Ratio: 1.2460 (annualized)
   Max Drawdown: 32.56%
   Volatility (Ann.): 26.76%
   Turnover: 0.91%
   Win Rate: 54.87%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.363, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $208,227.47
   Total Return: +108.23%
   Annualized Return: +44.30%
   Sharpe Ratio: 1.8545 (annualized)
   Sortino Ratio: 2.8288 (annualized)
   Max Drawdown: 10.73%
   Volatility (Ann.): 19.82%
   Turnover: 0.88%
   Win Rate: 55.27%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.316, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $141,142.20
   Total Return: +41.14%
   Annualized Return: +18.80%
   Sharpe Ratio: 0.9001 (annualized)
   Sortino Ratio: 1.2917 (annualized)
   Max Drawdown: 19.56%
   Volatility (Ann.): 18.99%
   Turnover: 0.82%
   Win Rate: 52.49%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.313, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $135,238.39
   Total Return: +35.24%
   Annualized Return: +16.29%
   Sharpe Ratio: 0.7348 (annualized)
   Sortino Ratio: 1.0817 (annualized)
   Max Drawdown: 24.85%
   Volatility (Ann.): 20.84%
   Turnover: 0.78%
   Win Rate: 52.68%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.271, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $149,246.05
   Total Return: +49.25%
   Annualized Return: +14.28%
   Sharpe Ratio: 0.5659 (annualized)
   Sortino Ratio: 0.7990 (annualized)
   Max Drawdown: 32.56%
   Volatility (Ann.): 26.21%
   Turnover: 0.85%
   Win Rate: 52.85%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.323, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $216,963.08
   Total Return: +116.96%
   Annualized Return: +29.46%
   Sharpe Ratio: 1.2207 (annualized)
   Sortino Ratio: 1.8224 (annualized)
   Max Drawdown: 24.85%
   Volatility (Ann.): 21.45%
   Turnover: 0.88%
   Win Rate: 53.25%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.300, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $195,741.35
   Total Return: +95.74%
   Annualized Return: +25.09%
   Sharpe Ratio: 1.1438 (annualized)
   Sortino Ratio: 1.7121 (annualized)
   Max Drawdown: 24.85%
   Volatility (Ann.): 19.54%
   Turnover: 0.85%
   Win Rate: 52.19%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.303, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $191,852.76
   Total Return: +91.85%
   Annualized Return: +24.26%
   Sharpe Ratio: 1.1477 (annualized)
   Sortino Ratio: 1.7158 (annualized)
   Max Drawdown: 24.85%
   Volatility (Ann.): 18.76%
   Turnover: 0.83%
   Win Rate: 54.17%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.276, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $211,724.40
   Total Return: +111.72%
   Annualized Return: +20.63%
   Sharpe Ratio: 0.8274 (annualized)
   Sortino Ratio: 1.1799 (annualized)
   Max Drawdown: 32.56%
   Volatility (Ann.): 23.71%
   Turnover: 0.87%
   Win Rate: 53.92%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.314, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $339,099.98
   Total Return: +239.10%
   Annualized Return: +35.70%
   Sharpe Ratio: 1.5559 (annualized)
   Sortino Ratio: 2.3515 (annualized)
   Max Drawdown: 24.85%
   Volatility (Ann.): 19.61%
   Turnover: 0.89%
   Win Rate: 54.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.291, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $310,390.85
   Total Return: +210.39%
   Annualized Return: +32.73%
   Sharpe Ratio: 1.5565 (annualized)
   Sortino Ratio: 2.3520 (annualized)
   Max Drawdown: 24.85%
   Volatility (Ann.): 17.99%
   Turnover: 0.90%
   Win Rate: 54.72%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.291, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $286,480.28
   Total Return: +186.48%
   Annualized Return: +30.10%
   Sharpe Ratio: 1.4817 (annualized)
   Sortino Ratio: 2.2290 (annualized)
   Max Drawdown: 24.85%
   Volatility (Ann.): 17.48%
   Turnover: 0.88%
   Win Rate: 55.91%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.274, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[9/11] Sweep checkpoint: high_watermark__ep0025__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $107,145.41
   Total Return: +7.15%
   Annualized Return: +7.15%
   Sharpe Ratio: 0.3161 (annualized)
   Sortino Ratio: 0.4292 (annualized)
   Max Drawdown: 33.23%
   Volatility (Ann.): 33.46%
   Turnover: 1.25%
   Win Rate: 56.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.446, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $151,008.80
   Total Return: +51.01%
   Annualized Return: +51.01%
   Sharpe Ratio: 2.0934 (annualized)
   Sortino Ratio: 3.1820 (annualized)
   Max Drawdown: 9.49%
   Volatility (Ann.): 19.77%
   Turnover: 1.04%
   Win Rate: 58.96%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.405, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $139,800.60
   Total Return: +39.80%
   Annualized Return: +39.80%
   Sharpe Ratio: 2.1395 (annualized)
   Sortino Ratio: 3.2710 (annualized)
   Max Drawdown: 9.00%
   Volatility (Ann.): 15.36%
   Turnover: 1.17%
   Win Rate: 57.77%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.442, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $136,948.20
   Total Return: +36.95%
   Annualized Return: +36.95%
   Sharpe Ratio: 2.1388 (annualized)
   Sortino Ratio: 3.3145 (annualized)
   Max Drawdown: 6.39%
   Volatility (Ann.): 14.32%
   Turnover: 0.75%
   Win Rate: 56.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.427, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $142,937.74
   Total Return: +42.94%
   Annualized Return: +19.56%
   Sharpe Ratio: 0.7504 (annualized)
   Sortino Ratio: 1.0355 (annualized)
   Max Drawdown: 33.23%
   Volatility (Ann.): 25.62%
   Turnover: 0.93%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.440, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $191,104.25
   Total Return: +91.10%
   Annualized Return: +38.24%
   Sharpe Ratio: 1.8842 (annualized)
   Sortino Ratio: 2.8611 (annualized)
   Max Drawdown: 9.49%
   Volatility (Ann.): 16.94%
   Turnover: 0.81%
   Win Rate: 57.46%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.410, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $137,408.42
   Total Return: +37.41%
   Annualized Return: +17.22%
   Sharpe Ratio: 0.9389 (annualized)
   Sortino Ratio: 1.3458 (annualized)
   Max Drawdown: 15.01%
   Volatility (Ann.): 16.26%
   Turnover: 0.84%
   Win Rate: 54.67%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.421, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $134,954.75
   Total Return: +34.95%
   Annualized Return: +16.17%
   Sharpe Ratio: 0.8172 (annualized)
   Sortino Ratio: 1.2074 (annualized)
   Max Drawdown: 19.88%
   Volatility (Ann.): 17.92%
   Turnover: 0.64%
   Win Rate: 52.29%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.394, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $140,857.10
   Total Return: +40.86%
   Annualized Return: +12.10%
   Sharpe Ratio: 0.5130 (annualized)
   Sortino Ratio: 0.7158 (annualized)
   Max Drawdown: 33.23%
   Volatility (Ann.): 24.14%
   Turnover: 0.80%
   Win Rate: 53.77%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.414, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $202,139.02
   Total Return: +102.14%
   Annualized Return: +26.44%
   Sharpe Ratio: 1.2683 (annualized)
   Sortino Ratio: 1.8941 (annualized)
   Max Drawdown: 19.88%
   Volatility (Ann.): 18.28%
   Turnover: 0.74%
   Win Rate: 54.44%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.391, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $180,354.30
   Total Return: +80.35%
   Annualized Return: +21.72%
   Sharpe Ratio: 1.1372 (annualized)
   Sortino Ratio: 1.6991 (annualized)
   Max Drawdown: 19.88%
   Volatility (Ann.): 16.82%
   Turnover: 0.77%
   Win Rate: 52.85%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.395, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $180,753.60
   Total Return: +80.75%
   Annualized Return: +21.81%
   Sharpe Ratio: 1.1810 (annualized)
   Sortino Ratio: 1.7661 (annualized)
   Max Drawdown: 19.88%
   Volatility (Ann.): 16.16%
   Turnover: 0.65%
   Win Rate: 53.38%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.393, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $188,659.00
   Total Return: +88.66%
   Annualized Return: +17.20%
   Sharpe Ratio: 0.7492 (annualized)
   Sortino Ratio: 1.0542 (annualized)
   Max Drawdown: 33.23%
   Volatility (Ann.): 21.73%
   Turnover: 0.77%
   Win Rate: 54.22%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.408, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $287,954.65
   Total Return: +187.95%
   Annualized Return: +30.27%
   Sharpe Ratio: 1.5526 (annualized)
   Sortino Ratio: 2.3381 (annualized)
   Max Drawdown: 19.88%
   Volatility (Ann.): 16.67%
   Turnover: 0.72%
   Win Rate: 55.31%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.391, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $256,904.66
   Total Return: +156.90%
   Annualized Return: +26.60%
   Sharpe Ratio: 1.4816 (annualized)
   Sortino Ratio: 2.2215 (annualized)
   Max Drawdown: 19.88%
   Volatility (Ann.): 15.41%
   Turnover: 0.75%
   Win Rate: 54.82%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.391, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00025_shp1p287_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 1008 days (4.00 years)
   Final Portfolio Value: $241,410.56
   Total Return: +141.41%
   Annualized Return: +24.65%
   Sharpe Ratio: 1.4093 (annualized)
   Sortino Ratio: 2.1011 (annualized)
   Max Drawdown: 19.88%
   Volatility (Ann.): 15.05%
   Turnover: 0.67%
   Win Rate: 55.11%
   Diagnostics: action_uniques=1008, alpha<=1 frac=0.378, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

[10/11] Sweep checkpoint: high_watermark__ep0032__step-00001

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $107,145.41
   Total Return: +7.15%
   Annualized Return: +7.15%
   Sharpe Ratio: 0.3161 (annualized)
   Sortino Ratio: 0.4292 (annualized)
   Max Drawdown: 33.23%
   Volatility (Ann.): 33.46%
   Turnover: 1.25%
   Win Rate: 56.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.446, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $151,008.80
   Total Return: +51.01%
   Annualized Return: +51.01%
   Sharpe Ratio: 2.0934 (annualized)
   Sortino Ratio: 3.1820 (annualized)
   Max Drawdown: 9.49%
   Volatility (Ann.): 19.77%
   Turnover: 1.04%
   Win Rate: 58.96%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.405, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $139,800.60
   Total Return: +39.80%
   Annualized Return: +39.80%
   Sharpe Ratio: 2.1395 (annualized)
   Sortino Ratio: 3.2710 (annualized)
   Max Drawdown: 9.00%
   Volatility (Ann.): 15.36%
   Turnover: 1.17%
   Win Rate: 57.77%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.442, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $136,948.20
   Total Return: +36.95%
   Annualized Return: +36.95%
   Sharpe Ratio: 2.1388 (annualized)
   Sortino Ratio: 3.3145 (annualized)
   Max Drawdown: 6.39%
   Volatility (Ann.): 14.32%
   Turnover: 0.75%
   Win Rate: 56.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.427, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $142,937.74
   Total Return: +42.94%
   Annualized Return: +19.56%
   Sharpe Ratio: 0.7504 (annualized)
   Sortino Ratio: 1.0355 (annualized)
   Max Drawdown: 33.23%
   Volatility (Ann.): 25.62%
   Turnover: 0.93%
   Win Rate: 56.66%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.440, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $191,104.25
   Total Return: +91.10%
   Annualized Return: +38.24%
   Sharpe Ratio: 1.8842 (annualized)
   Sortino Ratio: 2.8611 (annualized)
   Max Drawdown: 9.49%
   Volatility (Ann.): 16.94%
   Turnover: 0.81%
   Win Rate: 57.46%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.410, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $137,408.42
   Total Return: +37.41%
   Annualized Return: +17.22%
   Sharpe Ratio: 0.9389 (annualized)
   Sortino Ratio: 1.3458 (annualized)
   Max Drawdown: 15.01%
   Volatility (Ann.): 16.26%
   Turnover: 0.84%
   Win Rate: 54.67%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.421, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $134,954.75
   Total Return: +34.95%
   Annualized Return: +16.17%
   Sharpe Ratio: 0.8172 (annualized)
   Sortino Ratio: 1.2074 (annualized)
   Max Drawdown: 19.88%
   Volatility (Ann.): 17.92%
   Turnover: 0.64%
   Win Rate: 52.29%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.394, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Final Portfolio Value: $140,857.10
   Total Return: +40.86%
   Annualized Return: +12.10%
   Sharpe Ratio: 0.5130 (annualized)
   Sortino Ratio: 0.7158 (annualized)
   Max Drawdown: 33.23%
   Volatility (Ann.): 24.14%
   Turnover: 0.80%
   Win Rate: 53.77%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.414, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00032_shp0p810_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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


[1/39] high_watermark__ep0001__step-00001 | covid_crash | start=2020-03-12
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-03-12
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $177,331.61
   Total Return: +77.33%
   Annualized Return: +77.33%
   Sharpe Ratio: 1.8703 (annualized)
   Sortino Ratio: 2.8514 (annualized)
   Max Drawdown: 14.52%
   Volatility (Ann.): 32.55%
   Turnover: 1.05%
   Win Rate: 55.38%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.388, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.870254072429964
  [2/39] high_watermark__ep0001__step-00001 | covid_crash | start=2020-04-27
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-04-27
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $159,501.51
   Total Return: +59.50%
   Annualized Return: +59.50%
   Sharpe Ratio: 2.1916 (annualized)
   Sortino Ratio: 3.2454 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 21.57%
   Turnover: 0.72%
   Win Rate: 55.38%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.428, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.191608885877633
  [3/39] high_watermark__ep0001__step-00001 | covid_crash | start=2020-06-09
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-06-09
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $156,039.21
   Total Return: +56.04%
   Annualized Return: +56.04%
   Sharpe Ratio: 2.2674 (annualized)
   Sortino Ratio: 3.3786 (annualized)
   Max Drawdown: 10.87%
   Volatility (Ann.): 19.70%
   Turnover: 0.82%
   Win Rate: 55.78%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.458, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.2674486468896657
  [4/39] high_watermark__ep0001__step-00001 | inflation_rates | start=2022-05-03
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2022-05-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $128,146.87
   Total Return: +28.15%
   Annualized Return: +28.15%
   Sharpe Ratio: 0.9922 (annualized)
   Sortino Ratio: 1.5144 (annualized)
   Max Drawdown: 19.01%
   Volatility (Ann.): 26.67%
   Turnover: 0.91%
   Win Rate: 50.60%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.370, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=0.9922455709494784
  [5/39] high_watermark__ep0001__step-00001 | inflation_rates | start=2022-12-30
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2022-12-30
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $152,147.04
   Total Return: +52.15%
   Annualized Return: +52.15%
   Sharpe Ratio: 2.5861 (annualized)
   Sortino Ratio: 4.5647 (annualized)
   Max Drawdown: 6.46%
   Volatility (Ann.): 16.03%
   Turnover: 1.23%
   Win Rate: 57.37%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.378, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.5860628514386366
  [6/39] high_watermark__ep0001__step-00001 | inflation_rates | start=2023-08-31
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2023-08-31
   Market Regime: Market Stabilization (2023)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $155,707.85
   Total Return: +55.71%
   Annualized Return: +55.71%
   Sharpe Ratio: 2.8137 (annualized)
   Sortino Ratio: 4.5261 (annualized)
   Max Drawdown: 9.89%
   Volatility (Ann.): 15.54%
   Turnover: 0.77%
   Win Rate: 60.16%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.343, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.813710851429983
  [7/39] high_watermark__ep0001__step-00001 | post_covid_recovery | start=2020-09-30
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-09-30
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $150,898.16
   Total Return: +50.90%
   Annualized Return: +50.90%
   Sharpe Ratio: 2.3405 (annualized)
   Sortino Ratio: 3.6566 (annualized)
   Max Drawdown: 7.43%
   Volatility (Ann.): 17.47%
   Turnover: 0.69%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.424, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.3405064189965756
  [8/39] high_watermark__ep0001__step-00001 | post_covid_recovery | start=2021-04-05
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2021-04-05
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $136,721.17
   Total Return: +36.72%
   Annualized Return: +36.72%
   Sharpe Ratio: 1.6779 (annualized)
   Sortino Ratio: 2.6031 (annualized)
   Max Drawdown: 9.61%
   Volatility (Ann.): 18.57%
   Turnover: 0.69%
   Win Rate: 55.78%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.358, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.6778812975271713
  [9/39] high_watermark__ep0001__step-00001 | post_covid_recovery | start=2021-10-01
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2021-10-01
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $87,554.88
   Total Return: -12.45%
   Annualized Return: -12.45%
   Sharpe Ratio: -0.4699 (annualized)
   Sortino Ratio: -0.6432 (annualized)
   Max Drawdown: 26.42%
   Volatility (Ann.): 25.63%
   Turnover: 0.70%
   Win Rate: 48.61%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.362, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=-0.46992806156595124
  [10/39] high_watermark__ep0001__step-00001 | pre_covid | start=2020-01-27
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-01-27
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $139,797.66
   Total Return: +39.80%
   Annualized Return: +39.80%
   Sharpe Ratio: 1.0987 (annualized)
   Sortino Ratio: 1.5680 (annualized)
   Max Drawdown: 27.39%
   Volatility (Ann.): 34.14%
   Turnover: 1.06%
   Win Rate: 54.98%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.375, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.0987127518349462
  [11/39] high_watermark__ep0001__step-00001 | recent | start=2024-04-11
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2024-04-11
   Market Regime: Continued Growth (2024)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $113,495.82
   Total Return: +13.50%
   Annualized Return: +13.50%
   Sharpe Ratio: 0.5937 (annualized)
   Sortino Ratio: 0.8657 (annualized)
   Max Drawdown: 15.74%
   Volatility (Ann.): 22.18%
   Turnover: 0.85%
   Win Rate: 58.17%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.276, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=0.5936841230132495
  [12/39] high_watermark__ep0001__step-00001 | recent | start=2024-10-29
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00001_shp1p251_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2024-10-29
   Market Regime: Continued Growth (2024)
   Episode Length: 209 days (0.83 years)
   Final Portfolio Value: $122,311.71
   Total Return: +22.31%
   Annualized Return: +27.49%
   Sharpe Ratio: 1.1554 (annualized)
   Sortino Ratio: 1.7530 (annualized)
   Max Drawdown: 15.74%
   Volatility (Ann.): 21.37%
   Turnover: 0.89%
   Win Rate: 59.62%
   Diagnostics: action_uniques=209, alpha<=1 frac=0.364, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.155419254963163
  [14/39] high_watermark__ep0010__step-00001 | covid_crash | start=2020-03-12
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-03-12
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $173,406.34
   Total Return: +73.41%
   Annualized Return: +73.41%
   Sharpe Ratio: 1.8911 (annualized)
   Sortino Ratio: 2.8707 (annualized)
   Max Drawdown: 13.16%
   Volatility (Ann.): 30.69%
   Turnover: 0.62%
   Win Rate: 57.77%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.8911338055220657
  [15/39] high_watermark__ep0010__step-00001 | covid_crash | start=2020-04-27
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-04-27
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $154,451.32
   Total Return: +54.45%
   Annualized Return: +54.45%
   Sharpe Ratio: 2.2334 (annualized)
   Sortino Ratio: 3.2555 (annualized)
   Max Drawdown: 10.52%
   Volatility (Ann.): 19.53%
   Turnover: 0.73%
   Win Rate: 58.17%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.2334153631963702
  [16/39] high_watermark__ep0010__step-00001 | covid_crash | start=2020-06-09
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-06-09
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $148,621.14
   Total Return: +48.62%
   Annualized Return: +48.62%
   Sharpe Ratio: 2.1504 (annualized)
   Sortino Ratio: 3.1173 (annualized)
   Max Drawdown: 10.52%
   Volatility (Ann.): 18.38%
   Turnover: 0.72%
   Win Rate: 57.77%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.171, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.150370901435433
  [17/39] high_watermark__ep0010__step-00001 | inflation_rates | start=2022-05-03
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2022-05-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $120,496.62
   Total Return: +20.50%
   Annualized Return: +20.50%
   Sharpe Ratio: 0.8481 (annualized)
   Sortino Ratio: 1.2760 (annualized)
   Max Drawdown: 17.42%
   Volatility (Ann.): 22.79%
   Turnover: 0.51%
   Win Rate: 50.20%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=0.8481312051676531
  [18/39] high_watermark__ep0010__step-00001 | inflation_rates | start=2022-12-30
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2022-12-30
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $143,788.84
   Total Return: +43.79%
   Annualized Return: +43.79%
   Sharpe Ratio: 2.5599 (annualized)
   Sortino Ratio: 4.2722 (annualized)
   Max Drawdown: 5.71%
   Volatility (Ann.): 13.85%
   Turnover: 0.63%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.179, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.559936276916037
  [19/39] high_watermark__ep0010__step-00001 | inflation_rates | start=2023-08-31
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2023-08-31
   Market Regime: Market Stabilization (2023)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $150,729.12
   Total Return: +50.73%
   Annualized Return: +50.73%
   Sharpe Ratio: 3.1114 (annualized)
   Sortino Ratio: 4.9742 (annualized)
   Max Drawdown: 8.00%
   Volatility (Ann.): 12.88%
   Turnover: 0.60%
   Win Rate: 59.76%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=3.111433754867895
  [20/39] high_watermark__ep0010__step-00001 | post_covid_recovery | start=2020-09-30
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-09-30
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $144,446.23
   Total Return: +44.45%
   Annualized Return: +44.45%
   Sharpe Ratio: 2.3126 (annualized)
   Sortino Ratio: 3.6055 (annualized)
   Max Drawdown: 6.68%
   Volatility (Ann.): 15.65%
   Turnover: 0.57%
   Win Rate: 58.17%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.3125573232665477
  [21/39] high_watermark__ep0010__step-00001 | post_covid_recovery | start=2021-04-05
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2021-04-05
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $132,145.58
   Total Return: +32.15%
   Annualized Return: +32.15%
   Sharpe Ratio: 1.7814 (annualized)
   Sortino Ratio: 2.7387 (annualized)
   Max Drawdown: 6.99%
   Volatility (Ann.): 15.26%
   Turnover: 0.49%
   Win Rate: 56.57%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.7814472037227125
  [22/39] high_watermark__ep0010__step-00001 | post_covid_recovery | start=2021-10-01
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2021-10-01
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $90,425.89
   Total Return: -9.57%
   Annualized Return: -9.57%
   Sharpe Ratio: -0.4552 (annualized)
   Sortino Ratio: -0.6165 (annualized)
   Max Drawdown: 23.28%
   Volatility (Ann.): 21.48%
   Turnover: 0.44%
   Win Rate: 49.40%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=-0.455176242862752
  [23/39] high_watermark__ep0010__step-00001 | pre_covid | start=2020-01-27
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-01-27
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $127,337.43
   Total Return: +27.34%
   Annualized Return: +27.34%
   Sharpe Ratio: 0.8330 (annualized)
   Sortino Ratio: 1.1570 (annualized)
   Max Drawdown: 30.49%
   Volatility (Ann.): 33.54%
   Turnover: 0.66%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=0.833017644131559
  [24/39] high_watermark__ep0010__step-00001 | recent | start=2024-04-11
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2024-04-11
   Market Regime: Continued Growth (2024)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $114,733.38
   Total Return: +14.73%
   Annualized Return: +14.73%
   Sharpe Ratio: 0.7187 (annualized)
   Sortino Ratio: 1.0470 (annualized)
   Max Drawdown: 13.09%
   Volatility (Ann.): 18.92%
   Turnover: 0.50%
   Win Rate: 57.77%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.167, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=0.7187152227626551
  [25/39] high_watermark__ep0010__step-00001 | recent | start=2024-10-29
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00010_shp1p264_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2024-10-29
   Market Regime: Continued Growth (2024)
   Episode Length: 209 days (0.83 years)
   Final Portfolio Value: $121,549.48
   Total Return: +21.55%
   Annualized Return: +26.53%
   Sharpe Ratio: 1.2606 (annualized)
   Sortino Ratio: 1.9205 (annualized)
   Max Drawdown: 13.09%
   Volatility (Ann.): 18.54%
   Turnover: 0.54%
   Win Rate: 57.21%
   Diagnostics: action_uniques=209, alpha<=1 frac=0.167, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.260553771232103
  [27/39] high_watermark__ep0020__step-00001 | covid_crash | start=2020-03-12
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-03-12
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $166,975.91
   Total Return: +66.98%
   Annualized Return: +66.98%
   Sharpe Ratio: 1.6681 (annualized)
   Sortino Ratio: 2.5252 (annualized)
   Max Drawdown: 14.75%
   Volatility (Ann.): 32.95%
   Turnover: 1.06%
   Win Rate: 54.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.358, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.6681343196777902
  [28/39] high_watermark__ep0020__step-00001 | covid_crash | start=2020-04-27
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-04-27
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $153,178.42
   Total Return: +53.18%
   Annualized Return: +53.18%
   Sharpe Ratio: 2.1186 (annualized)
   Sortino Ratio: 3.0899 (annualized)
   Max Drawdown: 10.73%
   Volatility (Ann.): 20.26%
   Turnover: 1.13%
   Win Rate: 55.38%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.368, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.118583131056024
  [29/39] high_watermark__ep0020__step-00001 | covid_crash | start=2020-06-09
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-06-09
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $148,058.72
   Total Return: +48.06%
   Annualized Return: +48.06%
   Sharpe Ratio: 2.0997 (annualized)
   Sortino Ratio: 3.0814 (annualized)
   Max Drawdown: 10.73%
   Volatility (Ann.): 18.67%
   Turnover: 1.21%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.325, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.09968998056316
  [30/39] high_watermark__ep0020__step-00001 | inflation_rates | start=2022-05-03
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2022-05-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $116,913.10
   Total Return: +16.91%
   Annualized Return: +16.91%
   Sharpe Ratio: 0.7108 (annualized)
   Sortino Ratio: 1.0711 (annualized)
   Max Drawdown: 17.13%
   Volatility (Ann.): 22.99%
   Turnover: 1.01%
   Win Rate: 49.00%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.260, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=0.7107807205558311
  [31/39] high_watermark__ep0020__step-00001 | inflation_rates | start=2022-12-30
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2022-12-30
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $138,315.06
   Total Return: +38.32%
   Annualized Return: +38.32%
   Sharpe Ratio: 2.4328 (annualized)
   Sortino Ratio: 3.8828 (annualized)
   Max Drawdown: 5.85%
   Volatility (Ann.): 12.92%
   Turnover: 1.38%
   Win Rate: 57.77%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.271, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.43279829351219
  [32/39] high_watermark__ep0020__step-00001 | inflation_rates | start=2023-08-31
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2023-08-31
   Market Regime: Market Stabilization (2023)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $151,402.12
   Total Return: +51.40%
   Annualized Return: +51.40%
   Sharpe Ratio: 3.3350 (annualized)
   Sortino Ratio: 5.2682 (annualized)
   Max Drawdown: 7.11%
   Volatility (Ann.): 12.12%
   Turnover: 1.09%
   Win Rate: 61.35%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.294, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=3.3350439501076385
  [33/39] high_watermark__ep0020__step-00001 | post_covid_recovery | start=2020-09-30
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-09-30
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $140,906.59
   Total Return: +40.91%
   Annualized Return: +40.91%
   Sharpe Ratio: 2.1311 (annualized)
   Sortino Ratio: 3.3041 (annualized)
   Max Drawdown: 6.50%
   Volatility (Ann.): 15.82%
   Turnover: 0.85%
   Win Rate: 56.18%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.320, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=2.1310785964639885
  [34/39] high_watermark__ep0020__step-00001 | post_covid_recovery | start=2021-04-05
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2021-04-05
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $130,729.34
   Total Return: +30.73%
   Annualized Return: +30.73%
   Sharpe Ratio: 1.7055 (annualized)
   Sortino Ratio: 2.6259 (annualized)
   Max Drawdown: 8.55%
   Volatility (Ann.): 15.30%
   Turnover: 0.77%
   Win Rate: 56.97%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.280, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.7055388647432739
  [35/39] high_watermark__ep0020__step-00001 | post_covid_recovery | start=2021-10-01
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2021-10-01
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $92,896.01
   Total Return: -7.10%
   Annualized Return: -7.10%
   Sharpe Ratio: -0.2949 (annualized)
   Sortino Ratio: -0.4051 (annualized)
   Max Drawdown: 24.85%
   Volatility (Ann.): 22.92%
   Turnover: 0.78%
   Win Rate: 50.60%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.231, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=-0.29486367396276636
  [36/39] high_watermark__ep0020__step-00001 | pre_covid | start=2020-01-27
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2020-01-27
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $120,514.79
   Total Return: +20.51%
   Annualized Return: +20.51%
   Sharpe Ratio: 0.6533 (annualized)
   Sortino Ratio: 0.9031 (annualized)
   Max Drawdown: 32.69%
   Volatility (Ann.): 35.15%
   Turnover: 1.07%
   Win Rate: 55.38%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.376, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=0.6532966996375447
  [37/39] high_watermark__ep0020__step-00001 | recent | start=2024-04-11
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2024-04-11
   Market Regime: Continued Growth (2024)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $115,698.93
   Total Return: +15.70%
   Annualized Return: +15.70%
   Sharpe Ratio: 0.7569 (annualized)
   Sortino Ratio: 1.1237 (annualized)
   Max Drawdown: 13.26%
   Volatility (Ann.): 19.12%
   Turnover: 0.92%
   Win Rate: 58.96%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.241, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=0.7569183437699061
  [38/39] high_watermark__ep0020__step-00001 | recent | start=2024-10-29
================================================================================
LOADING CUSTOM CHECKPOINT: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932
================================================================================
[OK] Found actor weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_actor.weights.h5
[OK] Found critic weights: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00020_shp0p932_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128] | kernel=5 | dilations=[1, 2, 4] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
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
   Start Date: 2024-10-29
   Market Regime: Continued Growth (2024)
   Episode Length: 209 days (0.83 years)
   Final Portfolio Value: $122,847.85
   Total Return: +22.85%
   Annualized Return: +28.16%
   Sharpe Ratio: 1.2535 (annualized)
   Sortino Ratio: 1.9570 (annualized)
   Max Drawdown: 13.28%
   Volatility (Ann.): 19.87%
   Turnover: 0.92%
   Win Rate: 57.21%
   Diagnostics: action_uniques=209, alpha<=1 frac=0.297, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)
 | sh=1.253477089800584

Regime sweep complete: 36 successful evals, 0 failures