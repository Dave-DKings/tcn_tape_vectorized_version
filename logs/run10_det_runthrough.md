Found 60 candidate checkpoints

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp1p153
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp1p153_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00002_shp1p153_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $193,016.65
   Total Return: +93.02%
   Annualized Return: +19.78%
   Sharpe Ratio: 1.0446 (annualized)
   Sortino Ratio: 1.4934 (annualized)
   Max Drawdown: 19.96%
   Volatility (Ann.): 16.75%
   Turnover: 0.73%
   Win Rate: 54.53%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.091, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00004_shp1p259
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00004_shp1p259_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00004_shp1p259_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $193,016.65
   Total Return: +93.02%
   Annualized Return: +19.78%
   Sharpe Ratio: 1.0446 (annualized)
   Sortino Ratio: 1.4934 (annualized)
   Max Drawdown: 19.96%
   Volatility (Ann.): 16.75%
   Turnover: 0.73%
   Win Rate: 54.53%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.091, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p769
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p769_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00007_shp0p769_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $165,722.96
   Total Return: +65.72%
   Annualized Return: +14.87%
   Sharpe Ratio: 0.9524 (annualized)
   Sortino Ratio: 1.3437 (annualized)
   Max Drawdown: 16.79%
   Volatility (Ann.): 13.45%
   Turnover: 0.71%
   Win Rate: 54.31%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.702, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p444
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p444_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00008_shp1p444_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $165,722.96
   Total Return: +65.72%
   Annualized Return: +14.87%
   Sharpe Ratio: 0.9524 (annualized)
   Sortino Ratio: 1.3437 (annualized)
   Max Drawdown: 16.79%
   Volatility (Ann.): 13.45%
   Turnover: 0.71%
   Win Rate: 54.31%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.702, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00009_shp0p740
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00009_shp0p740_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00009_shp0p740_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $161,726.66
   Total Return: +61.73%
   Annualized Return: +14.11%
   Sharpe Ratio: 0.9171 (annualized)
   Sortino Ratio: 1.2746 (annualized)
   Max Drawdown: 16.86%
   Volatility (Ann.): 13.20%
   Turnover: 0.66%
   Win Rate: 54.31%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.806, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00015_shp0p747
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00015_shp0p747_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00015_shp0p747_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $170,956.31
   Total Return: +70.96%
   Annualized Return: +15.86%
   Sharpe Ratio: 0.9627 (annualized)
   Sortino Ratio: 1.3543 (annualized)
   Max Drawdown: 18.11%
   Volatility (Ann.): 14.32%
   Turnover: 0.62%
   Win Rate: 54.09%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.939, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00019_shp0p720
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00019_shp0p720_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00019_shp0p720_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $176,727.66
   Total Return: +76.73%
   Annualized Return: +16.92%
   Sharpe Ratio: 0.9731 (annualized)
   Sortino Ratio: 1.3640 (annualized)
   Max Drawdown: 19.02%
   Volatility (Ann.): 15.24%
   Turnover: 0.62%
   Win Rate: 53.98%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.224, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00021_shp1p042
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00021_shp1p042_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00021_shp1p042_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $177,792.90
   Total Return: +77.79%
   Annualized Return: +17.11%
   Sharpe Ratio: 0.9869 (annualized)
   Sortino Ratio: 1.3819 (annualized)
   Max Drawdown: 18.95%
   Volatility (Ann.): 15.19%
   Turnover: 0.57%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.000, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00023_shp1p119
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00023_shp1p119_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00023_shp1p119_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $177,792.90
   Total Return: +77.79%
   Annualized Return: +17.11%
   Sharpe Ratio: 0.9869 (annualized)
   Sortino Ratio: 1.3819 (annualized)
   Max Drawdown: 18.95%
   Volatility (Ann.): 15.19%
   Turnover: 0.57%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.000, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00026_shp0p728
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00026_shp0p728_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00026_shp0p728_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $167,250.76
   Total Return: +67.25%
   Annualized Return: +15.16%
   Sharpe Ratio: 0.9653 (annualized)
   Sortino Ratio: 1.3585 (annualized)
   Max Drawdown: 16.83%
   Volatility (Ann.): 13.54%
   Turnover: 0.62%
   Win Rate: 53.98%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.901, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00030_shp0p949
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00030_shp0p949_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00030_shp0p949_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $169,708.20
   Total Return: +69.71%
   Annualized Return: +15.63%
   Sharpe Ratio: 0.9777 (annualized)
   Sortino Ratio: 1.3782 (annualized)
   Max Drawdown: 17.05%
   Volatility (Ann.): 13.82%
   Turnover: 0.57%
   Win Rate: 53.87%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.816, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00031_shp0p801
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00031_shp0p801_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00031_shp0p801_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $169,708.20
   Total Return: +69.71%
   Annualized Return: +15.63%
   Sharpe Ratio: 0.9777 (annualized)
   Sortino Ratio: 1.3782 (annualized)
   Max Drawdown: 17.05%
   Volatility (Ann.): 13.82%
   Turnover: 0.57%
   Win Rate: 53.87%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.816, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00036_shp0p830
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00036_shp0p830_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00036_shp0p830_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $168,943.92
   Total Return: +68.94%
   Annualized Return: +15.48%
   Sharpe Ratio: 0.9940 (annualized)
   Sortino Ratio: 1.4058 (annualized)
   Max Drawdown: 16.50%
   Volatility (Ann.): 13.41%
   Turnover: 0.53%
   Win Rate: 53.65%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.504, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00038_shp0p741
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00038_shp0p741_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00038_shp0p741_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $169,016.19
   Total Return: +69.02%
   Annualized Return: +15.50%
   Sharpe Ratio: 0.9865 (annualized)
   Sortino Ratio: 1.3942 (annualized)
   Max Drawdown: 16.80%
   Volatility (Ann.): 13.54%
   Turnover: 0.49%
   Win Rate: 53.76%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.876, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00046_shp0p779
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00046_shp0p779_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00046_shp0p779_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $170,791.09
   Total Return: +70.79%
   Annualized Return: +15.83%
   Sharpe Ratio: 0.9741 (annualized)
   Sortino Ratio: 1.3739 (annualized)
   Max Drawdown: 17.73%
   Volatility (Ann.): 14.09%
   Turnover: 0.50%
   Win Rate: 53.87%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.192, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00049_shp1p319
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00049_shp1p319_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00049_shp1p319_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $170,411.23
   Total Return: +70.41%
   Annualized Return: +15.76%
   Sharpe Ratio: 0.9838 (annualized)
   Sortino Ratio: 1.3892 (annualized)
   Max Drawdown: 17.60%
   Volatility (Ann.): 13.86%
   Turnover: 0.45%
   Win Rate: 53.98%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.078, argmax_alpha_uniques=9

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00050_shp1p236
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00050_shp1p236_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00050_shp1p236_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $170,411.23
   Total Return: +70.41%
   Annualized Return: +15.76%
   Sharpe Ratio: 0.9838 (annualized)
   Sortino Ratio: 1.3892 (annualized)
   Max Drawdown: 17.60%
   Volatility (Ann.): 13.86%
   Turnover: 0.45%
   Win Rate: 53.98%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.078, argmax_alpha_uniques=9

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00051_shp0p750
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00051_shp0p750_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00051_shp0p750_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $170,411.23
   Total Return: +70.41%
   Annualized Return: +15.76%
   Sharpe Ratio: 0.9838 (annualized)
   Sortino Ratio: 1.3892 (annualized)
   Max Drawdown: 17.60%
   Volatility (Ann.): 13.86%
   Turnover: 0.45%
   Win Rate: 53.98%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.078, argmax_alpha_uniques=9

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00053_shp1p092
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00053_shp1p092_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00053_shp1p092_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $165,273.62
   Total Return: +65.27%
   Annualized Return: +14.79%
   Sharpe Ratio: 0.9701 (annualized)
   Sortino Ratio: 1.3714 (annualized)
   Max Drawdown: 16.58%
   Volatility (Ann.): 13.07%
   Turnover: 0.51%
   Win Rate: 54.53%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.143, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00054_shp0p865
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00054_shp0p865_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00054_shp0p865_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $165,273.62
   Total Return: +65.27%
   Annualized Return: +14.79%
   Sharpe Ratio: 0.9701 (annualized)
   Sortino Ratio: 1.3714 (annualized)
   Max Drawdown: 16.58%
   Volatility (Ann.): 13.07%
   Turnover: 0.51%
   Win Rate: 54.53%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.143, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00055_shp0p979
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00055_shp0p979_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00055_shp0p979_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $165,273.62
   Total Return: +65.27%
   Annualized Return: +14.79%
   Sharpe Ratio: 0.9701 (annualized)
   Sortino Ratio: 1.3714 (annualized)
   Max Drawdown: 16.58%
   Volatility (Ann.): 13.07%
   Turnover: 0.51%
   Win Rate: 54.53%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.143, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00056_shp0p847
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00056_shp0p847_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00056_shp0p847_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $165,273.62
   Total Return: +65.27%
   Annualized Return: +14.79%
   Sharpe Ratio: 0.9701 (annualized)
   Sortino Ratio: 1.3714 (annualized)
   Max Drawdown: 16.58%
   Volatility (Ann.): 13.07%
   Turnover: 0.51%
   Win Rate: 54.53%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.143, argmax_alpha_uniques=2

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00057_shp0p925
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00057_shp0p925_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00057_shp0p925_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $166,374.05
   Total Return: +66.37%
   Annualized Return: +15.00%
   Sharpe Ratio: 0.9684 (annualized)
   Sortino Ratio: 1.3646 (annualized)
   Max Drawdown: 16.97%
   Volatility (Ann.): 13.32%
   Turnover: 0.48%
   Win Rate: 54.31%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.334, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00058_shp0p890
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00058_shp0p890_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00058_shp0p890_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $166,374.05
   Total Return: +66.37%
   Annualized Return: +15.00%
   Sharpe Ratio: 0.9684 (annualized)
   Sortino Ratio: 1.3646 (annualized)
   Max Drawdown: 16.97%
   Volatility (Ann.): 13.32%
   Turnover: 0.48%
   Win Rate: 54.31%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.334, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00059_shp1p107
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00059_shp1p107_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00059_shp1p107_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $166,374.05
   Total Return: +66.37%
   Annualized Return: +15.00%
   Sharpe Ratio: 0.9684 (annualized)
   Sortino Ratio: 1.3646 (annualized)
   Max Drawdown: 16.97%
   Volatility (Ann.): 13.32%
   Turnover: 0.48%
   Win Rate: 54.31%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.334, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00060_shp0p794
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00060_shp0p794_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00060_shp0p794_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $166,374.05
   Total Return: +66.37%
   Annualized Return: +15.00%
   Sharpe Ratio: 0.9684 (annualized)
   Sortino Ratio: 1.3646 (annualized)
   Max Drawdown: 16.97%
   Volatility (Ann.): 13.32%
   Turnover: 0.48%
   Win Rate: 54.31%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.334, argmax_alpha_uniques=1

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00061_shp0p749
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00061_shp0p749_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00061_shp0p749_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $169,751.21
   Total Return: +69.75%
   Annualized Return: +15.63%
   Sharpe Ratio: 0.9696 (annualized)
   Sortino Ratio: 1.3622 (annualized)
   Max Drawdown: 17.89%
   Volatility (Ann.): 13.96%
   Turnover: 0.49%
   Win Rate: 54.09%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.603, argmax_alpha_uniques=9

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00065_shp1p087
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00065_shp1p087_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00065_shp1p087_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $174,679.29
   Total Return: +74.68%
   Annualized Return: +16.55%
   Sharpe Ratio: 0.9910 (annualized)
   Sortino Ratio: 1.3950 (annualized)
   Max Drawdown: 18.47%
   Volatility (Ann.): 14.54%
   Turnover: 0.46%
   Win Rate: 53.65%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.605, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00066_shp1p231
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00066_shp1p231_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00066_shp1p231_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $174,679.29
   Total Return: +74.68%
   Annualized Return: +16.55%
   Sharpe Ratio: 0.9910 (annualized)
   Sortino Ratio: 1.3950 (annualized)
   Max Drawdown: 18.47%
   Volatility (Ann.): 14.54%
   Turnover: 0.46%
   Win Rate: 53.65%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.605, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00067_shp0p854
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00067_shp0p854_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00067_shp0p854_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $174,679.29
   Total Return: +74.68%
   Annualized Return: +16.55%
   Sharpe Ratio: 0.9910 (annualized)
   Sortino Ratio: 1.3950 (annualized)
   Max Drawdown: 18.47%
   Volatility (Ann.): 14.54%
   Turnover: 0.46%
   Win Rate: 53.65%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.605, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00068_shp1p029
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00068_shp1p029_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00068_shp1p029_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $174,679.29
   Total Return: +74.68%
   Annualized Return: +16.55%
   Sharpe Ratio: 0.9910 (annualized)
   Sortino Ratio: 1.3950 (annualized)
   Max Drawdown: 18.47%
   Volatility (Ann.): 14.54%
   Turnover: 0.46%
   Win Rate: 53.65%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.605, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00070_shp1p004
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00070_shp1p004_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00070_shp1p004_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $180,497.21
   Total Return: +80.50%
   Annualized Return: +17.60%
   Sharpe Ratio: 1.0088 (annualized)
   Sortino Ratio: 1.4173 (annualized)
   Max Drawdown: 19.39%
   Volatility (Ann.): 15.29%
   Turnover: 0.38%
   Win Rate: 53.98%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.091, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp1p207
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp1p207_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00073_shp1p207_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $178,607.72
   Total Return: +78.61%
   Annualized Return: +17.26%
   Sharpe Ratio: 1.0018 (annualized)
   Sortino Ratio: 1.4001 (annualized)
   Max Drawdown: 19.40%
   Volatility (Ann.): 15.07%
   Turnover: 0.38%
   Win Rate: 54.09%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.081, argmax_alpha_uniques=9

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00082_shp0p890
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00082_shp0p890_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00082_shp0p890_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $172,764.05
   Total Return: +72.76%
   Annualized Return: +16.19%
   Sharpe Ratio: 0.9946 (annualized)
   Sortino Ratio: 1.3933 (annualized)
   Max Drawdown: 18.33%
   Volatility (Ann.): 14.12%
   Turnover: 0.40%
   Win Rate: 54.31%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.011, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00086_shp1p070
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00086_shp1p070_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00086_shp1p070_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $174,486.59
   Total Return: +74.49%
   Annualized Return: +16.51%
   Sharpe Ratio: 0.9935 (annualized)
   Sortino Ratio: 1.3903 (annualized)
   Max Drawdown: 18.78%
   Volatility (Ann.): 14.46%
   Turnover: 0.41%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.061, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00087_shp1p050
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00087_shp1p050_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00087_shp1p050_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $174,486.59
   Total Return: +74.49%
   Annualized Return: +16.51%
   Sharpe Ratio: 0.9935 (annualized)
   Sortino Ratio: 1.3903 (annualized)
   Max Drawdown: 18.78%
   Volatility (Ann.): 14.46%
   Turnover: 0.41%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.061, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp1p091
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp1p091_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00088_shp1p091_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $174,486.59
   Total Return: +74.49%
   Annualized Return: +16.51%
   Sharpe Ratio: 0.9935 (annualized)
   Sortino Ratio: 1.3903 (annualized)
   Max Drawdown: 18.78%
   Volatility (Ann.): 14.46%
   Turnover: 0.41%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.061, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp0p815
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp0p815_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00089_shp0p815_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $174,683.41
   Total Return: +74.68%
   Annualized Return: +16.55%
   Sharpe Ratio: 0.9903 (annualized)
   Sortino Ratio: 1.3862 (annualized)
   Max Drawdown: 18.99%
   Volatility (Ann.): 14.55%
   Turnover: 0.36%
   Win Rate: 53.98%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.025, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00093_shp1p129
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00093_shp1p129_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00093_shp1p129_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $175,484.37
   Total Return: +75.48%
   Annualized Return: +16.69%
   Sharpe Ratio: 0.9861 (annualized)
   Sortino Ratio: 1.3846 (annualized)
   Max Drawdown: 19.10%
   Volatility (Ann.): 14.77%
   Turnover: 0.44%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.066, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00096_shp0p992
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00096_shp0p992_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00096_shp0p992_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $175,484.37
   Total Return: +75.48%
   Annualized Return: +16.69%
   Sharpe Ratio: 0.9861 (annualized)
   Sortino Ratio: 1.3846 (annualized)
   Max Drawdown: 19.10%
   Volatility (Ann.): 14.77%
   Turnover: 0.44%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.066, argmax_alpha_uniques=10

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00097_shp0p884
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00097_shp0p884_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00097_shp0p884_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $175,851.49
   Total Return: +75.85%
   Annualized Return: +16.76%
   Sharpe Ratio: 0.9873 (annualized)
   Sortino Ratio: 1.3885 (annualized)
   Max Drawdown: 19.19%
   Volatility (Ann.): 14.82%
   Turnover: 0.43%
   Win Rate: 53.76%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.174, argmax_alpha_uniques=11

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00098_shp0p935
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00098_shp0p935_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00098_shp0p935_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $175,851.49
   Total Return: +75.85%
   Annualized Return: +16.76%
   Sharpe Ratio: 0.9873 (annualized)
   Sortino Ratio: 1.3885 (annualized)
   Max Drawdown: 19.19%
   Volatility (Ann.): 14.82%
   Turnover: 0.43%
   Win Rate: 53.76%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.174, argmax_alpha_uniques=11

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00106_shp0p883
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00106_shp0p883_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00106_shp0p883_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $179,579.41
   Total Return: +79.58%
   Annualized Return: +17.43%
   Sharpe Ratio: 0.9914 (annualized)
   Sortino Ratio: 1.3924 (annualized)
   Max Drawdown: 19.86%
   Volatility (Ann.): 15.44%
   Turnover: 0.41%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.912, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00107_shp1p127
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00107_shp1p127_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00107_shp1p127_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $179,579.41
   Total Return: +79.58%
   Annualized Return: +17.43%
   Sharpe Ratio: 0.9914 (annualized)
   Sortino Ratio: 1.3924 (annualized)
   Max Drawdown: 19.86%
   Volatility (Ann.): 15.44%
   Turnover: 0.41%
   Win Rate: 54.20%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.912, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00109_shp0p930
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00109_shp0p930_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00109_shp0p930_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================

📊 DETERMINISTIC TEST RESULTS:
   Eval Track: det_mean
   Start Date: 2022-01-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 918 days (3.64 years)
   Final Portfolio Value: $180,539.44
   Total Return: +80.54%
   Annualized Return: +17.61%
   Sharpe Ratio: 0.9943 (annualized)
   Sortino Ratio: 1.3960 (annualized)
   Max Drawdown: 20.11%
   Volatility (Ann.): 15.56%
   Turnover: 0.39%
   Win Rate: 54.09%
   Diagnostics: action_uniques=918, alpha<=1 frac=0.975, argmax_alpha_uniques=9

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 0 Runs)
================================================================================

[IDEA] Skipped stochastic evaluation (num_eval_runs=0)

================================================================================
LOADING CUSTOM CHECKPOINT: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00110_shp1p171
================================================================================
[OK] Found actor weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00110_shp1p171_actor.weights.h5
[OK] Found critic weights: /content/tcn_tape_vectorized_version_clean/tcn_fusion_results/high_watermark_checkpoints/exp6_tape_hw_ep00110_shp1p171_critic.weights.h5
🏗️ Recreating evaluation environments...
   🧭 Checkpoint architecture: TCN_FUSION (attention=True, fusion=True, source=path)
   🧱 Eval TCN stack: filters=[64, 96, 128, 128, 128] | kernel=5 | dilations=[1, 2, 4, 8, 16] | dropout=0.15
   🧩 Eval fusion core: embed=128 | heads=4 | dropout=0.1
   🔀 Eval mixer (A4): enabled=False | layers=1 | expansion=2.0 | dropout=0.1
   🎯 Eval alpha head (A3): dims=[128, 64] | dropout=0.05
   🧭 Eval fusion v2 cross-attn: asset_identity=True | context_cross_attn=False | ctx_heads=4 | ctx_dropout=0.1 | per_asset_alpha_head=True
   [BRAIN] Eval recurrent memory: enabled=False | units=64 | dropout=0.1
   [GLOBE] Eval regime conditioning: enabled=True | mode=film | hidden_dim=32 | dropout=0.05
   [DOWN] Eval distributional critic: enabled=True | num_quantiles=17
   🎛️ Eval dirichlet: activation=exp_tanh | temperature=1.2 | adaptive_temp=False | adaptive_base=1.0 | adaptive_slope=0.0 | adaptive_range=[0.8, 2.5] | alpha_cap=16.0 | epsilon={'max': 0.2, 'min': 0.02}
   🧷 Eval dual-head: enabled=False | blend_schedule=[{'threshold': 0, 'rho': 0.35}, {'threshold': 30000, 'rho': 0.55}, {'threshold': 60000, 'rho': 0.7}] | eval_rho_det=0.9 | eval_rho_stoch=0.6 | use_constraints=False
   🧷 Eval dual-head consistency coef: 0.0
[TOOL] Building models before loading weights...
   [OK] Models built successfully
📂 Loading checkpoint weights...
   [OK] Weights loaded successfully
   🎯 Deterministic eval policy modes: ['mean']
   🎯 Stochastic eval policy mode:     sample

================================================================================
DETERMINISTIC EVALUATION (det_mean)
================================================================================