 Streaming output truncated to the last 5000 lines.
   Min:  0.3625
   Max:  1.0072

Volatility (Ann. %):
   Mean: +16.61%
   Std:  0.40%
   Min:  +16.05%
   Max:  +17.23%

Max Drawdown (%):
   Mean: 14.63%
   Std:  1.58%
   Min:  11.90%
   Max:  17.08%

Turnover (%):
   Mean: 26.83%
   Std:  0.45%

Turnover Step Detail (%):
   Mean(step mean): 26.834%
   Mean(step p95):  37.839%
   Mean(step max):  48.359%
   Mean exceed rate: 11.1%
   Mean excess over target: 0.391%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260328_223748.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2024-07-22
   Market Regime: Continued Growth (2024)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $118,604.39
   Total Return: +18.60%
   Annualized Return: +18.60%
   Sharpe Ratio: 1.0646 (annualized)
   Sortino Ratio: 1.5539 (annualized)
   Max Drawdown: 13.60%
   Volatility (Ann.): 15.33%
   Turnover: 3.64%
   Win Rate: 57.37%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=11286):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +13.70%
   Annualized Return: +13.70%
   Sharpe: 0.7543
   Volatility (Ann.): 16.18%
   Max DD: 12.26%
   Turnover (episode): 26.88%
   Turnover (step): mean=26.882% | p95=38.748% | max=50.515%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.516%
   Raw/Executed turnover: raw_mean=48.876% | executed/raw=0.550

[RAND] Run 2/16 (Seed=11287):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +12.65%
   Annualized Return: +12.65%
   Sharpe: 0.6997
   Volatility (Ann.): 16.09%
   Max DD: 14.12%
   Turnover (episode): 26.36%
   Turnover (step): mean=26.363% | p95=39.013% | max=45.783%
   Turnover vs target: target=35.000% | exceed_rate=12.7% | mean_excess=0.493%
   Raw/Executed turnover: raw_mean=47.932% | executed/raw=0.550

[RAND] Run 3/16 (Seed=11288):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +12.98%
   Annualized Return: +12.98%
   Sharpe: 0.6982
   Volatility (Ann.): 16.70%
   Max DD: 15.00%
   Turnover (episode): 26.89%
   Turnover (step): mean=26.885% | p95=39.185% | max=50.466%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.523%
   Raw/Executed turnover: raw_mean=48.882% | executed/raw=0.550

[RAND] Run 4/16 (Seed=11289):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.30%
   Annualized Return: +6.30%
   Sharpe: 0.3315
   Volatility (Ann.): 16.69%
   Max DD: 18.34%
   Turnover (episode): 26.54%
   Turnover (step): mean=26.544% | p95=37.363% | max=46.210%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.329%
   Raw/Executed turnover: raw_mean=48.262% | executed/raw=0.550

[RAND] Run 5/16 (Seed=11290):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +5.97%
   Annualized Return: +5.97%
   Sharpe: 0.3305
   Volatility (Ann.): 15.02%
   Max DD: 16.23%
   Turnover (episode): 27.34%
   Turnover (step): mean=27.339% | p95=38.446% | max=46.827%
   Turnover vs target: target=35.000% | exceed_rate=14.3% | mean_excess=0.496%
   Raw/Executed turnover: raw_mean=49.706% | executed/raw=0.550

[RAND] Run 6/16 (Seed=11291):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +15.59%
   Annualized Return: +15.59%
   Sharpe: 0.8429
   Volatility (Ann.): 16.52%
   Max DD: 14.03%
   Turnover (episode): 27.60%
   Turnover (step): mean=27.600% | p95=38.979% | max=47.894%
   Turnover vs target: target=35.000% | exceed_rate=13.1% | mean_excess=0.465%
   Raw/Executed turnover: raw_mean=50.181% | executed/raw=0.550

[RAND] Run 7/16 (Seed=11292):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +14.63%
   Annualized Return: +14.63%
   Sharpe: 0.8229
   Volatility (Ann.): 15.75%
   Max DD: 14.26%
   Turnover (episode): 26.29%
   Turnover (step): mean=26.294% | p95=37.503% | max=48.100%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.419%
   Raw/Executed turnover: raw_mean=47.808% | executed/raw=0.550

[RAND] Run 8/16 (Seed=11293):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +8.36%
   Annualized Return: +8.36%
   Sharpe: 0.4492
   Volatility (Ann.): 16.57%
   Max DD: 14.84%
   Turnover (episode): 27.13%
   Turnover (step): mean=27.134% | p95=39.077% | max=48.495%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.428%
   Raw/Executed turnover: raw_mean=49.334% | executed/raw=0.550

[RAND] Run 9/16 (Seed=11294):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +9.68%
   Annualized Return: +9.68%
   Sharpe: 0.5332
   Volatility (Ann.): 16.10%
   Max DD: 16.47%
   Turnover (episode): 27.01%
   Turnover (step): mean=27.005% | p95=40.195% | max=50.663%
   Turnover vs target: target=35.000% | exceed_rate=14.3% | mean_excess=0.614%
   Raw/Executed turnover: raw_mean=49.101% | executed/raw=0.550

[RAND] Run 10/16 (Seed=11295):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +12.93%
   Annualized Return: +12.93%
   Sharpe: 0.6945
   Volatility (Ann.): 16.73%
   Max DD: 15.41%
   Turnover (episode): 26.10%
   Turnover (step): mean=26.101% | p95=38.487% | max=48.515%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.483%
   Raw/Executed turnover: raw_mean=47.457% | executed/raw=0.550

[RAND] Run 11/16 (Seed=11296):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +11.75%
   Annualized Return: +11.75%
   Sharpe: 0.6481
   Volatility (Ann.): 16.16%
   Max DD: 14.12%
   Turnover (episode): 26.30%
   Turnover (step): mean=26.302% | p95=36.221% | max=46.111%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.247%
   Raw/Executed turnover: raw_mean=47.821% | executed/raw=0.550

[RAND] Run 12/16 (Seed=11297):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +11.39%
   Annualized Return: +11.39%
   Sharpe: 0.6158
   Volatility (Ann.): 16.58%
   Max DD: 14.95%
   Turnover (episode): 26.58%
   Turnover (step): mean=26.582% | p95=37.461% | max=49.834%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.364%
   Raw/Executed turnover: raw_mean=48.330% | executed/raw=0.550

[RAND] Run 13/16 (Seed=11298):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +13.87%
   Annualized Return: +13.87%
   Sharpe: 0.7597
   Volatility (Ann.): 16.29%
   Max DD: 13.46%
   Turnover (episode): 26.10%
   Turnover (step): mean=26.100% | p95=37.825% | max=46.786%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.339%
   Raw/Executed turnover: raw_mean=47.455% | executed/raw=0.550

[RAND] Run 14/16 (Seed=11299):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +10.49%
   Annualized Return: +10.49%
   Sharpe: 0.5853
   Volatility (Ann.): 15.87%
   Max DD: 12.87%
   Turnover (episode): 26.67%
   Turnover (step): mean=26.673% | p95=37.476% | max=46.788%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.370%
   Raw/Executed turnover: raw_mean=48.496% | executed/raw=0.550

[RAND] Run 15/16 (Seed=11300):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +15.30%
   Annualized Return: +15.30%
   Sharpe: 0.8207
   Volatility (Ann.): 16.69%
   Max DD: 13.71%
   Turnover (episode): 26.96%
   Turnover (step): mean=26.959% | p95=38.538% | max=44.930%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.473%
   Raw/Executed turnover: raw_mean=49.016% | executed/raw=0.550

[RAND] Run 16/16 (Seed=11301):
   Start Date: 2024-07-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.97%
   Annualized Return: +6.97%
   Sharpe: 0.3699
   Volatility (Ann.): 16.70%
   Max DD: 15.29%
   Turnover (episode): 26.37%
   Turnover (step): mean=26.371% | p95=38.164% | max=43.439%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.363%
   Raw/Executed turnover: raw_mean=47.947% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +11.41%
   Std:  3.15%
   Min:  +5.97%
   Max:  +15.59%

Annualized Return (%):
   Mean: +11.41%
   Std:  3.15%
   Min:  +5.97%
   Max:  +15.59%

Sharpe Ratio (annualized):
   Mean: 0.6223
   Std:  0.1742
   Min:  0.3305
   Max:  0.8429

Volatility (Ann. %):
   Mean: +16.29%
   Std:  0.47%
   Min:  +15.02%
   Max:  +16.73%

Max Drawdown (%):
   Mean: 14.71%
   Std:  1.48%
   Min:  12.26%
   Max:  18.34%

Turnover (%):
   Mean: 26.70%
   Std:  0.44%

Turnover Step Detail (%):
   Mean(step mean): 26.696%
   Mean(step p95):  38.293%
   Mean(step max):  47.585%
   Mean exceed rate: 11.6%
   Mean excess over target: 0.432%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260328_230349.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2020-03-31
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $204,615.14
   Total Return: +104.62%
   Annualized Return: +43.04%
   Sharpe Ratio: 1.9628 (annualized)
   Sortino Ratio: 2.9365 (annualized)
   Max Drawdown: 11.77%
   Volatility (Ann.): 18.11%
   Turnover: 3.46%
   Win Rate: 58.05%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20203):
   Start Date: 2021-02-24 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +13.60%
   Annualized Return: +13.60%
   Sharpe: 0.7717
   Volatility (Ann.): 15.60%
   Max DD: 11.27%
   Turnover (episode): 25.46%
   Turnover (step): mean=25.460% | p95=36.110% | max=43.657%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.234%
   Raw/Executed turnover: raw_mean=46.291% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20204):
   Start Date: 2020-08-20 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +20.83%
   Annualized Return: +20.83%
   Sharpe: 1.2608
   Volatility (Ann.): 14.31%
   Max DD: 8.03%
   Turnover (episode): 26.13%
   Turnover (step): mean=26.130% | p95=36.642% | max=54.625%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.329%
   Raw/Executed turnover: raw_mean=47.508% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20205):
   Start Date: 2020-12-24 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +27.41%
   Annualized Return: +27.41%
   Sharpe: 1.5378
   Volatility (Ann.): 15.29%
   Max DD: 7.12%
   Turnover (episode): 26.80%
   Turnover (step): mean=26.802% | p95=39.747% | max=48.871%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.546%
   Raw/Executed turnover: raw_mean=48.731% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20206):
   Start Date: 2020-09-21 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +24.31%
   Annualized Return: +24.31%
   Sharpe: 1.4360
   Volatility (Ann.): 14.58%
   Max DD: 6.82%
   Turnover (episode): 25.20%
   Turnover (step): mean=25.205% | p95=37.213% | max=47.739%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.317%
   Raw/Executed turnover: raw_mean=45.827% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20207):
   Start Date: 2020-04-29 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +43.24%
   Annualized Return: +43.24%
   Sharpe: 2.0367
   Volatility (Ann.): 17.51%
   Max DD: 9.06%
   Turnover (episode): 25.53%
   Turnover (step): mean=25.532% | p95=36.091% | max=43.699%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.257%
   Raw/Executed turnover: raw_mean=46.422% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20208):
   Start Date: 2021-03-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +24.11%
   Annualized Return: +24.11%
   Sharpe: 1.3542
   Volatility (Ann.): 15.43%
   Max DD: 12.74%
   Turnover (episode): 25.78%
   Turnover (step): mean=25.782% | p95=37.169% | max=43.186%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.299%
   Raw/Executed turnover: raw_mean=46.876% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20209):
   Start Date: 2020-08-28 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +26.73%
   Annualized Return: +26.73%
   Sharpe: 1.5430
   Volatility (Ann.): 14.85%
   Max DD: 9.09%
   Turnover (episode): 26.20%
   Turnover (step): mean=26.199% | p95=36.837% | max=53.238%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.387%
   Raw/Executed turnover: raw_mean=47.634% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20210):
   Start Date: 2020-09-08 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +30.79%
   Annualized Return: +30.79%
   Sharpe: 1.7804
   Volatility (Ann.): 14.63%
   Max DD: 6.78%
   Turnover (episode): 25.49%
   Turnover (step): mean=25.492% | p95=37.441% | max=44.774%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.311%
   Raw/Executed turnover: raw_mean=46.350% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20211):
   Start Date: 2020-04-29 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +40.63%
   Annualized Return: +40.63%
   Sharpe: 1.8751
   Volatility (Ann.): 18.08%
   Max DD: 8.35%
   Turnover (episode): 25.48%
   Turnover (step): mean=25.480% | p95=37.070% | max=43.317%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.328%
   Raw/Executed turnover: raw_mean=46.328% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20212):
   Start Date: 2020-08-07 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +31.15%
   Annualized Return: +31.15%
   Sharpe: 1.7758
   Volatility (Ann.): 14.84%
   Max DD: 8.42%
   Turnover (episode): 26.11%
   Turnover (step): mean=26.109% | p95=39.278% | max=49.423%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.500%
   Raw/Executed turnover: raw_mean=47.470% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20213):
   Start Date: 2020-07-17 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +29.92%
   Annualized Return: +29.92%
   Sharpe: 1.5926
   Volatility (Ann.): 16.08%
   Max DD: 10.34%
   Turnover (episode): 26.14%
   Turnover (step): mean=26.140% | p95=38.489% | max=49.014%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.467%
   Raw/Executed turnover: raw_mean=47.526% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20214):
   Start Date: 2020-09-09 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +28.00%
   Annualized Return: +28.00%
   Sharpe: 1.6825
   Volatility (Ann.): 14.15%
   Max DD: 6.15%
   Turnover (episode): 25.61%
   Turnover (step): mean=25.615% | p95=37.403% | max=57.087%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.387%
   Raw/Executed turnover: raw_mean=46.572% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20215):
   Start Date: 2021-01-29 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +19.85%
   Annualized Return: +19.85%
   Sharpe: 1.0705
   Volatility (Ann.): 16.39%
   Max DD: 12.73%
   Turnover (episode): 25.18%
   Turnover (step): mean=25.177% | p95=35.987% | max=45.243%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.187%
   Raw/Executed turnover: raw_mean=45.777% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20216):
   Start Date: 2020-04-09 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +40.81%
   Annualized Return: +40.81%
   Sharpe: 1.8723
   Volatility (Ann.): 18.19%
   Max DD: 8.30%
   Turnover (episode): 25.88%
   Turnover (step): mean=25.876% | p95=37.068% | max=46.194%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.288%
   Raw/Executed turnover: raw_mean=47.047% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20217):
   Start Date: 2021-03-26 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +22.00%
   Annualized Return: +22.00%
   Sharpe: 1.2344
   Volatility (Ann.): 15.55%
   Max DD: 12.82%
   Turnover (episode): 25.08%
   Turnover (step): mean=25.082% | p95=36.017% | max=46.482%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.214%
   Raw/Executed turnover: raw_mean=45.604% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20218):
   Start Date: 2020-09-10 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +22.35%
   Annualized Return: +22.35%
   Sharpe: 1.3751
   Volatility (Ann.): 14.00%
   Max DD: 6.63%
   Turnover (episode): 25.43%
   Turnover (step): mean=25.432% | p95=38.749% | max=44.983%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.461%
   Raw/Executed turnover: raw_mean=46.239% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +27.86%
   Std:  8.17%
   Min:  +13.60%
   Max:  +43.24%

Annualized Return (%):
   Mean: +27.86%
   Std:  8.17%
   Min:  +13.60%
   Max:  +43.24%

Sharpe Ratio (annualized):
   Mean: 1.5124
   Std:  0.3315
   Min:  0.7717
   Max:  2.0367

Volatility (Ann. %):
   Mean: +15.59%
   Std:  1.34%
   Min:  +14.00%
   Max:  +18.19%

Max Drawdown (%):
   Mean: 9.04%
   Std:  2.29%
   Min:  6.15%
   Max:  12.82%

Turnover (%):
   Mean: 25.72%
   Std:  0.46%

Turnover Step Detail (%):
   Mean(step mean): 25.719%
   Mean(step p95):  37.332%
   Mean(step max):  47.596%
   Mean exceed rate: 9.4%
   Mean excess over target: 0.344%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260328_233125.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2020-06-02
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $167,408.31
   Total Return: +67.41%
   Annualized Return: +29.39%
   Sharpe Ratio: 1.4681 (annualized)
   Sortino Ratio: 2.1022 (annualized)
   Max Drawdown: 12.88%
   Volatility (Ann.): 17.26%
   Turnover: 3.37%
   Win Rate: 57.26%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20246):
   Start Date: 2020-12-07 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +24.25%
   Annualized Return: +24.25%
   Sharpe: 1.4894
   Volatility (Ann.): 13.96%
   Max DD: 5.02%
   Turnover (episode): 25.44%
   Turnover (step): mean=25.437% | p95=36.039% | max=47.469%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.188%
   Raw/Executed turnover: raw_mean=46.249% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20247):
   Start Date: 2021-05-12 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +10.84%
   Annualized Return: +10.84%
   Sharpe: 0.5877
   Volatility (Ann.): 16.53%
   Max DD: 15.19%
   Turnover (episode): 24.71%
   Turnover (step): mean=24.705% | p95=33.008% | max=43.547%
   Turnover vs target: target=35.000% | exceed_rate=2.8% | mean_excess=0.079%
   Raw/Executed turnover: raw_mean=44.919% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20248):
   Start Date: 2020-07-20 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +27.26%
   Annualized Return: +27.26%
   Sharpe: 1.5802
   Volatility (Ann.): 14.76%
   Max DD: 7.27%
   Turnover (episode): 25.69%
   Turnover (step): mean=25.693% | p95=36.372% | max=50.257%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.293%
   Raw/Executed turnover: raw_mean=46.714% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20249):
   Start Date: 2020-11-19 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +35.37%
   Annualized Return: +35.37%
   Sharpe: 2.1040
   Volatility (Ann.): 13.98%
   Max DD: 5.29%
   Turnover (episode): 25.30%
   Turnover (step): mean=25.299% | p95=36.701% | max=43.815%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.291%
   Raw/Executed turnover: raw_mean=45.998% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20250):
   Start Date: 2021-02-09 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +15.30%
   Annualized Return: +15.30%
   Sharpe: 0.8290
   Volatility (Ann.): 16.49%
   Max DD: 12.62%
   Turnover (episode): 24.95%
   Turnover (step): mean=24.954% | p95=36.730% | max=52.014%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.352%
   Raw/Executed turnover: raw_mean=45.372% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20251):
   Start Date: 2021-02-19 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +11.14%
   Annualized Return: +11.14%
   Sharpe: 0.6461
   Volatility (Ann.): 15.12%
   Max DD: 12.82%
   Turnover (episode): 25.69%
   Turnover (step): mean=25.691% | p95=36.536% | max=44.462%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.287%
   Raw/Executed turnover: raw_mean=46.711% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20252):
   Start Date: 2021-06-02 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +3.20%
   Annualized Return: +3.20%
   Sharpe: 0.1540
   Volatility (Ann.): 16.85%
   Max DD: 14.94%
   Turnover (episode): 24.78%
   Turnover (step): mean=24.781% | p95=34.071% | max=47.621%
   Turnover vs target: target=35.000% | exceed_rate=4.0% | mean_excess=0.118%
   Raw/Executed turnover: raw_mean=45.057% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20253):
   Start Date: 2020-12-30 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +26.87%
   Annualized Return: +26.87%
   Sharpe: 1.5231
   Volatility (Ann.): 15.15%
   Max DD: 7.07%
   Turnover (episode): 25.43%
   Turnover (step): mean=25.434% | p95=36.221% | max=44.896%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.263%
   Raw/Executed turnover: raw_mean=46.243% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20254):
   Start Date: 2020-12-22 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +22.21%
   Annualized Return: +22.21%
   Sharpe: 1.2508
   Volatility (Ann.): 15.48%
   Max DD: 7.10%
   Turnover (episode): 25.78%
   Turnover (step): mean=25.778% | p95=37.619% | max=47.507%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.367%
   Raw/Executed turnover: raw_mean=46.869% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20255):
   Start Date: 2020-06-08 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +34.20%
   Annualized Return: +34.20%
   Sharpe: 1.6900
   Volatility (Ann.): 17.19%
   Max DD: 8.65%
   Turnover (episode): 25.63%
   Turnover (step): mean=25.630% | p95=36.885% | max=44.481%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.324%
   Raw/Executed turnover: raw_mean=46.600% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20256):
   Start Date: 2020-07-29 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +29.98%
   Annualized Return: +29.98%
   Sharpe: 1.5939
   Volatility (Ann.): 16.10%
   Max DD: 10.87%
   Turnover (episode): 24.96%
   Turnover (step): mean=24.959% | p95=35.510% | max=48.812%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.185%
   Raw/Executed turnover: raw_mean=45.380% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20257):
   Start Date: 2020-08-11 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +28.88%
   Annualized Return: +28.88%
   Sharpe: 1.6172
   Volatility (Ann.): 15.25%
   Max DD: 7.55%
   Turnover (episode): 25.48%
   Turnover (step): mean=25.484% | p95=37.925% | max=46.451%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.304%
   Raw/Executed turnover: raw_mean=46.334% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20258):
   Start Date: 2020-12-01 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +35.43%
   Annualized Return: +35.43%
   Sharpe: 2.0610
   Volatility (Ann.): 14.32%
   Max DD: 4.64%
   Turnover (episode): 25.87%
   Turnover (step): mean=25.874% | p95=38.544% | max=51.805%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.513%
   Raw/Executed turnover: raw_mean=47.044% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20259):
   Start Date: 2021-05-24 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +2.19%
   Annualized Return: +2.19%
   Sharpe: 0.0953
   Volatility (Ann.): 16.79%
   Max DD: 16.67%
   Turnover (episode): 24.40%
   Turnover (step): mean=24.397% | p95=36.239% | max=43.401%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.231%
   Raw/Executed turnover: raw_mean=44.359% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20260):
   Start Date: 2020-07-14 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +31.45%
   Annualized Return: +31.45%
   Sharpe: 1.7260
   Volatility (Ann.): 15.46%
   Max DD: 9.64%
   Turnover (episode): 25.61%
   Turnover (step): mean=25.612% | p95=37.500% | max=45.790%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.351%
   Raw/Executed turnover: raw_mean=46.567% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20261):
   Start Date: 2021-03-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +23.73%
   Annualized Return: +23.73%
   Sharpe: 1.3504
   Volatility (Ann.): 15.22%
   Max DD: 12.04%
   Turnover (episode): 25.71%
   Turnover (step): mean=25.709% | p95=36.223% | max=44.414%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.226%
   Raw/Executed turnover: raw_mean=46.743% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +22.64%
   Std:  10.94%
   Min:  +2.19%
   Max:  +35.43%

Annualized Return (%):
   Mean: +22.64%
   Std:  10.94%
   Min:  +2.19%
   Max:  +35.43%

Sharpe Ratio (annualized):
   Mean: 1.2686
   Std:  0.6229
   Min:  0.0953
   Max:  2.1040

Volatility (Ann. %):
   Mean: +15.54%
   Std:  1.02%
   Min:  +13.96%
   Max:  +17.19%

Max Drawdown (%):
   Mean: 9.84%
   Std:  3.86%
   Min:  4.64%
   Max:  16.67%

Turnover (%):
   Mean: 25.34%
   Std:  0.44%

Turnover Step Detail (%):
   Mean(step mean): 25.340%
   Mean(step p95):  36.383%
   Mean(step max):  46.671%
   Mean exceed rate: 7.5%
   Mean excess over target: 0.273%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260328_235859.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2020-07-31
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $152,257.20
   Total Return: +52.26%
   Annualized Return: +23.39%
   Sharpe Ratio: 1.1919 (annualized)
   Sortino Ratio: 1.7180 (annualized)
   Max Drawdown: 15.43%
   Volatility (Ann.): 17.27%
   Turnover: 3.44%
   Win Rate: 56.86%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20288):
   Start Date: 2021-07-14 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -2.68%
   Annualized Return: -2.68%
   Sharpe: -0.1811
   Volatility (Ann.): 17.52%
   Max DD: 16.31%
   Turnover (episode): 25.10%
   Turnover (step): mean=25.104% | p95=35.750% | max=39.727%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.140%
   Raw/Executed turnover: raw_mean=45.644% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20289):
   Start Date: 2021-03-29 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +20.27%
   Annualized Return: +20.27%
   Sharpe: 1.1484
   Volatility (Ann.): 15.45%
   Max DD: 12.47%
   Turnover (episode): 25.18%
   Turnover (step): mean=25.182% | p95=37.328% | max=41.507%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.301%
   Raw/Executed turnover: raw_mean=45.785% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20290):
   Start Date: 2021-03-12 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +15.99%
   Annualized Return: +15.99%
   Sharpe: 0.9154
   Volatility (Ann.): 15.40%
   Max DD: 11.71%
   Turnover (episode): 24.93%
   Turnover (step): mean=24.934% | p95=37.391% | max=41.210%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.307%
   Raw/Executed turnover: raw_mean=45.334% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20291):
   Start Date: 2021-03-11 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +12.66%
   Annualized Return: +12.66%
   Sharpe: 0.7379
   Volatility (Ann.): 15.08%
   Max DD: 10.79%
   Turnover (episode): 25.75%
   Turnover (step): mean=25.749% | p95=37.194% | max=54.357%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.387%
   Raw/Executed turnover: raw_mean=46.817% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20292):
   Start Date: 2020-12-10 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +25.84%
   Annualized Return: +25.84%
   Sharpe: 1.5219
   Volatility (Ann.): 14.56%
   Max DD: 5.19%
   Turnover (episode): 24.88%
   Turnover (step): mean=24.876% | p95=37.043% | max=44.089%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.262%
   Raw/Executed turnover: raw_mean=45.229% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20293):
   Start Date: 2021-07-27 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.06%
   Annualized Return: -3.06%
   Sharpe: -0.2026
   Volatility (Ann.): 17.57%
   Max DD: 16.96%
   Turnover (episode): 25.94%
   Turnover (step): mean=25.944% | p95=35.855% | max=54.045%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.262%
   Raw/Executed turnover: raw_mean=47.172% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20294):
   Start Date: 2020-10-12 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +16.61%
   Annualized Return: +16.61%
   Sharpe: 1.0305
   Volatility (Ann.): 14.00%
   Max DD: 6.13%
   Turnover (episode): 26.27%
   Turnover (step): mean=26.266% | p95=37.167% | max=45.392%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.378%
   Raw/Executed turnover: raw_mean=47.757% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20295):
   Start Date: 2021-05-24 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +3.71%
   Annualized Return: +3.71%
   Sharpe: 0.1836
   Volatility (Ann.): 16.83%
   Max DD: 14.15%
   Turnover (episode): 24.30%
   Turnover (step): mean=24.301% | p95=35.597% | max=46.872%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.233%
   Raw/Executed turnover: raw_mean=44.183% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20296):
   Start Date: 2021-07-19 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -8.12%
   Annualized Return: -8.12%
   Sharpe: -0.5368
   Volatility (Ann.): 16.88%
   Max DD: 19.36%
   Turnover (episode): 24.93%
   Turnover (step): mean=24.935% | p95=34.926% | max=48.936%
   Turnover vs target: target=35.000% | exceed_rate=5.2% | mean_excess=0.241%
   Raw/Executed turnover: raw_mean=45.336% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20297):
   Start Date: 2021-03-25 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +16.95%
   Annualized Return: +16.95%
   Sharpe: 0.9894
   Volatility (Ann.): 15.03%
   Max DD: 11.75%
   Turnover (episode): 26.01%
   Turnover (step): mean=26.009% | p95=38.283% | max=46.318%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.388%
   Raw/Executed turnover: raw_mean=47.289% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20298):
   Start Date: 2021-07-15 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -5.73%
   Annualized Return: -5.73%
   Sharpe: -0.3582
   Volatility (Ann.): 17.70%
   Max DD: 19.68%
   Turnover (episode): 24.75%
   Turnover (step): mean=24.746% | p95=36.589% | max=45.310%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.244%
   Raw/Executed turnover: raw_mean=44.994% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20299):
   Start Date: 2021-06-15 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +4.13%
   Annualized Return: +4.13%
   Sharpe: 0.2069
   Volatility (Ann.): 17.25%
   Max DD: 14.23%
   Turnover (episode): 25.70%
   Turnover (step): mean=25.696% | p95=36.479% | max=45.994%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.289%
   Raw/Executed turnover: raw_mean=46.720% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20300):
   Start Date: 2021-01-20 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +22.16%
   Annualized Return: +22.16%
   Sharpe: 1.2413
   Volatility (Ann.): 15.57%
   Max DD: 6.44%
   Turnover (episode): 26.54%
   Turnover (step): mean=26.541% | p95=38.856% | max=49.058%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.465%
   Raw/Executed turnover: raw_mean=48.256% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20301):
   Start Date: 2020-08-17 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +22.46%
   Annualized Return: +22.46%
   Sharpe: 1.3177
   Volatility (Ann.): 14.77%
   Max DD: 8.76%
   Turnover (episode): 25.63%
   Turnover (step): mean=25.634% | p95=35.986% | max=42.623%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.178%
   Raw/Executed turnover: raw_mean=46.606% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20302):
   Start Date: 2020-11-27 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +34.62%
   Annualized Return: +34.62%
   Sharpe: 2.0823
   Volatility (Ann.): 13.85%
   Max DD: 5.23%
   Turnover (episode): 26.01%
   Turnover (step): mean=26.006% | p95=37.807% | max=49.094%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.414%
   Raw/Executed turnover: raw_mean=47.284% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20303):
   Start Date: 2021-01-15 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +24.13%
   Annualized Return: +24.13%
   Sharpe: 1.3078
   Volatility (Ann.): 16.07%
   Max DD: 6.22%
   Turnover (episode): 25.22%
   Turnover (step): mean=25.220% | p95=36.165% | max=46.305%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.232%
   Raw/Executed turnover: raw_mean=45.855% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +12.50%
   Std:  12.86%
   Min:  -8.12%
   Max:  +34.62%

Annualized Return (%):
   Mean: +12.50%
   Std:  12.86%
   Min:  -8.12%
   Max:  +34.62%

Sharpe Ratio (annualized):
   Mean: 0.7128
   Std:  0.7668
   Min:  -0.5368
   Max:  2.0823

Volatility (Ann. %):
   Mean: +15.85%
   Std:  1.30%
   Min:  +13.85%
   Max:  +17.70%

Max Drawdown (%):
   Mean: 11.59%
   Std:  4.94%
   Min:  5.19%
   Max:  19.68%

Turnover (%):
   Mean: 25.45%
   Std:  0.62%

Turnover Step Detail (%):
   Mean(step mean): 25.446%
   Mean(step p95):  36.776%
   Mean(step max):  46.302%
   Mean exceed rate: 8.3%
   Mean excess over target: 0.295%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_002631.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2022-05-03
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $170,131.38
   Total Return: +70.13%
   Annualized Return: +30.43%
   Sharpe Ratio: 1.4261 (annualized)
   Sortino Ratio: 2.1990 (annualized)
   Max Drawdown: 19.48%
   Volatility (Ann.): 18.48%
   Turnover: 3.44%
   Win Rate: 52.88%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20730):
   Start Date: 2022-10-14 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +47.15%
   Annualized Return: +47.15%
   Sharpe: 2.1750
   Volatility (Ann.): 17.64%
   Max DD: 7.70%
   Turnover (episode): 27.65%
   Turnover (step): mean=27.651% | p95=40.630% | max=47.897%
   Turnover vs target: target=35.000% | exceed_rate=17.9% | mean_excess=0.784%
   Raw/Executed turnover: raw_mean=50.275% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20731):
   Start Date: 2023-01-20 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +33.18%
   Annualized Return: +33.18%
   Sharpe: 1.9321
   Volatility (Ann.): 14.40%
   Max DD: 6.82%
   Turnover (episode): 27.17%
   Turnover (step): mean=27.166% | p95=37.298% | max=50.127%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.415%
   Raw/Executed turnover: raw_mean=49.392% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20732):
   Start Date: 2023-04-28 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +34.28%
   Annualized Return: +34.28%
   Sharpe: 2.2175
   Volatility (Ann.): 12.83%
   Max DD: 7.41%
   Turnover (episode): 27.35%
   Turnover (step): mean=27.348% | p95=40.851% | max=48.728%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.599%
   Raw/Executed turnover: raw_mean=49.724% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20733):
   Start Date: 2022-11-14 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +29.31%
   Annualized Return: +29.31%
   Sharpe: 1.5977
   Volatility (Ann.): 15.68%
   Max DD: 8.03%
   Turnover (episode): 26.65%
   Turnover (step): mean=26.654% | p95=37.186% | max=48.438%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.357%
   Raw/Executed turnover: raw_mean=48.461% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20734):
   Start Date: 2023-04-04 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +50.56%
   Annualized Return: +50.56%
   Sharpe: 3.0252
   Volatility (Ann.): 13.22%
   Max DD: 6.00%
   Turnover (episode): 26.50%
   Turnover (step): mean=26.503% | p95=37.949% | max=49.342%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.419%
   Raw/Executed turnover: raw_mean=48.188% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20735):
   Start Date: 2023-05-04 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +37.37%
   Annualized Return: +37.37%
   Sharpe: 2.2089
   Volatility (Ann.): 13.98%
   Max DD: 8.59%
   Turnover (episode): 26.20%
   Turnover (step): mean=26.197% | p95=37.497% | max=46.498%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.368%
   Raw/Executed turnover: raw_mean=47.631% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20736):
   Start Date: 2022-07-18 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +48.08%
   Annualized Return: +48.08%
   Sharpe: 1.9998
   Volatility (Ann.): 19.70%
   Max DD: 15.29%
   Turnover (episode): 26.80%
   Turnover (step): mean=26.800% | p95=38.948% | max=46.391%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.417%
   Raw/Executed turnover: raw_mean=48.728% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20737):
   Start Date: 2022-07-14 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +37.64%
   Annualized Return: +37.64%
   Sharpe: 1.4612
   Volatility (Ann.): 22.30%
   Max DD: 20.42%
   Turnover (episode): 26.60%
   Turnover (step): mean=26.603% | p95=36.227% | max=43.749%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.267%
   Raw/Executed turnover: raw_mean=48.369% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20738):
   Start Date: 2022-05-31 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +12.47%
   Annualized Return: +12.47%
   Sharpe: 0.5432
   Volatility (Ann.): 22.89%
   Max DD: 23.88%
   Turnover (episode): 27.21%
   Turnover (step): mean=27.208% | p95=38.297% | max=45.924%
   Turnover vs target: target=35.000% | exceed_rate=13.1% | mean_excess=0.465%
   Raw/Executed turnover: raw_mean=49.469% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20739):
   Start Date: 2023-04-26 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +41.81%
   Annualized Return: +41.81%
   Sharpe: 2.3932
   Volatility (Ann.): 14.25%
   Max DD: 8.69%
   Turnover (episode): 26.69%
   Turnover (step): mean=26.694% | p95=39.691% | max=45.449%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.574%
   Raw/Executed turnover: raw_mean=48.535% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20740):
   Start Date: 2022-10-27 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +40.46%
   Annualized Return: +40.46%
   Sharpe: 1.8515
   Volatility (Ann.): 18.25%
   Max DD: 7.46%
   Turnover (episode): 26.79%
   Turnover (step): mean=26.788% | p95=38.344% | max=47.824%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.484%
   Raw/Executed turnover: raw_mean=48.706% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20741):
   Start Date: 2023-03-17 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +45.75%
   Annualized Return: +45.75%
   Sharpe: 2.7851
   Volatility (Ann.): 13.19%
   Max DD: 6.78%
   Turnover (episode): 25.63%
   Turnover (step): mean=25.630% | p95=37.825% | max=52.615%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.480%
   Raw/Executed turnover: raw_mean=46.600% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20742):
   Start Date: 2022-08-16 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +21.07%
   Annualized Return: +21.07%
   Sharpe: 0.9717
   Volatility (Ann.): 19.71%
   Max DD: 15.64%
   Turnover (episode): 26.97%
   Turnover (step): mean=26.971% | p95=38.956% | max=47.458%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.458%
   Raw/Executed turnover: raw_mean=49.039% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20743):
   Start Date: 2023-04-19 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +33.57%
   Annualized Return: +33.57%
   Sharpe: 2.1504
   Volatility (Ann.): 12.99%
   Max DD: 7.31%
   Turnover (episode): 27.04%
   Turnover (step): mean=27.041% | p95=39.305% | max=46.762%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.570%
   Raw/Executed turnover: raw_mean=49.165% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20744):
   Start Date: 2023-03-03 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +40.00%
   Annualized Return: +40.00%
   Sharpe: 2.3060
   Volatility (Ann.): 14.23%
   Max DD: 7.86%
   Turnover (episode): 26.86%
   Turnover (step): mean=26.863% | p95=38.534% | max=49.771%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.431%
   Raw/Executed turnover: raw_mean=48.843% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20745):
   Start Date: 2022-09-22 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +45.87%
   Annualized Return: +45.87%
   Sharpe: 1.9665
   Volatility (Ann.): 19.21%
   Max DD: 7.62%
   Turnover (episode): 26.33%
   Turnover (step): mean=26.327% | p95=39.159% | max=49.667%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.469%
   Raw/Executed turnover: raw_mean=47.867% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +37.41%
   Std:  10.18%
   Min:  +12.47%
   Max:  +50.56%

Annualized Return (%):
   Mean: +37.41%
   Std:  10.18%
   Min:  +12.47%
   Max:  +50.56%

Sharpe Ratio (annualized):
   Mean: 1.9741
   Std:  0.6169
   Min:  0.5432
   Max:  3.0252

Volatility (Ann. %):
   Mean: +16.53%
   Std:  3.42%
   Min:  +12.83%
   Max:  +22.89%

Max Drawdown (%):
   Mean: 10.34%
   Std:  5.41%
   Min:  6.00%
   Max:  23.88%

Turnover (%):
   Mean: 26.78%
   Std:  0.48%

Turnover Step Detail (%):
   Mean(step mean): 26.778%
   Mean(step p95):  38.543%
   Mean(step max):  47.915%
   Mean exceed rate: 12.0%
   Mean excess over target: 0.472%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_005410.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2022-12-30
   Market Regime: Rate Hikes / Tech Correction (2022)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $184,207.81
   Total Return: +84.21%
   Annualized Return: +35.72%
   Sharpe Ratio: 2.2924 (annualized)
   Sortino Ratio: 3.9353 (annualized)
   Max Drawdown: 7.05%
   Volatility (Ann.): 12.85%
   Turnover: 3.16%
   Win Rate: 55.07%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20897):
   Start Date: 2023-01-06 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +33.48%
   Annualized Return: +33.48%
   Sharpe: 2.0042
   Volatility (Ann.): 13.97%
   Max DD: 7.60%
   Turnover (episode): 26.69%
   Turnover (step): mean=26.693% | p95=37.209% | max=58.104%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.400%
   Raw/Executed turnover: raw_mean=48.533% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20898):
   Start Date: 2023-07-07 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +28.46%
   Annualized Return: +28.46%
   Sharpe: 2.0648
   Volatility (Ann.): 11.54%
   Max DD: 7.60%
   Turnover (episode): 26.85%
   Turnover (step): mean=26.851% | p95=39.061% | max=47.172%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.458%
   Raw/Executed turnover: raw_mean=48.820% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20899):
   Start Date: 2023-04-28 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +38.96%
   Annualized Return: +38.96%
   Sharpe: 2.4739
   Volatility (Ann.): 12.89%
   Max DD: 6.57%
   Turnover (episode): 27.33%
   Turnover (step): mean=27.329% | p95=40.840% | max=47.834%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.702%
   Raw/Executed turnover: raw_mean=49.689% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20900):
   Start Date: 2023-08-08 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +16.47%
   Annualized Return: +16.47%
   Sharpe: 1.2333
   Volatility (Ann.): 11.33%
   Max DD: 8.90%
   Turnover (episode): 27.46%
   Turnover (step): mean=27.464% | p95=40.902% | max=50.360%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.698%
   Raw/Executed turnover: raw_mean=49.935% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20901):
   Start Date: 2023-10-06 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +33.04%
   Annualized Return: +33.04%
   Sharpe: 2.5966
   Volatility (Ann.): 10.49%
   Max DD: 5.69%
   Turnover (episode): 27.59%
   Turnover (step): mean=27.593% | p95=40.075% | max=49.052%
   Turnover vs target: target=35.000% | exceed_rate=15.1% | mean_excess=0.596%
   Raw/Executed turnover: raw_mean=50.169% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20902):
   Start Date: 2023-03-03 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +39.95%
   Annualized Return: +39.95%
   Sharpe: 2.3319
   Volatility (Ann.): 14.05%
   Max DD: 7.56%
   Turnover (episode): 26.55%
   Turnover (step): mean=26.545% | p95=37.679% | max=44.819%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.378%
   Raw/Executed turnover: raw_mean=48.264% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20903):
   Start Date: 2023-11-08 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +31.04%
   Annualized Return: +31.04%
   Sharpe: 2.2298
   Volatility (Ann.): 11.59%
   Max DD: 5.43%
   Turnover (episode): 26.92%
   Turnover (step): mean=26.920% | p95=38.663% | max=46.910%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.450%
   Raw/Executed turnover: raw_mean=48.946% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20904):
   Start Date: 2023-12-29 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +25.68%
   Annualized Return: +25.68%
   Sharpe: 2.0696
   Volatility (Ann.): 10.40%
   Max DD: 5.19%
   Turnover (episode): 27.28%
   Turnover (step): mean=27.285% | p95=38.697% | max=49.121%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.542%
   Raw/Executed turnover: raw_mean=49.608% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20905):
   Start Date: 2023-08-18 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +26.42%
   Annualized Return: +26.42%
   Sharpe: 1.9795
   Volatility (Ann.): 11.21%
   Max DD: 6.43%
   Turnover (episode): 27.82%
   Turnover (step): mean=27.816% | p95=39.914% | max=53.098%
   Turnover vs target: target=35.000% | exceed_rate=16.7% | mean_excess=0.816%
   Raw/Executed turnover: raw_mean=50.574% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20906):
   Start Date: 2023-10-19 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +30.44%
   Annualized Return: +30.44%
   Sharpe: 2.3668
   Volatility (Ann.): 10.68%
   Max DD: 5.57%
   Turnover (episode): 27.43%
   Turnover (step): mean=27.429% | p95=38.857% | max=46.094%
   Turnover vs target: target=35.000% | exceed_rate=12.7% | mean_excess=0.506%
   Raw/Executed turnover: raw_mean=49.872% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20907):
   Start Date: 2023-04-28 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +34.65%
   Annualized Return: +34.65%
   Sharpe: 2.1830
   Volatility (Ann.): 13.18%
   Max DD: 7.21%
   Turnover (episode): 27.39%
   Turnover (step): mean=27.385% | p95=38.467% | max=49.219%
   Turnover vs target: target=35.000% | exceed_rate=14.7% | mean_excess=0.494%
   Raw/Executed turnover: raw_mean=49.792% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20908):
   Start Date: 2023-11-01 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +33.14%
   Annualized Return: +33.14%
   Sharpe: 2.4975
   Volatility (Ann.): 10.96%
   Max DD: 5.27%
   Turnover (episode): 28.14%
   Turnover (step): mean=28.141% | p95=39.435% | max=52.234%
   Turnover vs target: target=35.000% | exceed_rate=18.3% | mean_excess=0.637%
   Raw/Executed turnover: raw_mean=51.165% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20909):
   Start Date: 2023-10-27 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +36.82%
   Annualized Return: +36.82%
   Sharpe: 2.7072
   Volatility (Ann.): 11.13%
   Max DD: 5.26%
   Turnover (episode): 27.97%
   Turnover (step): mean=27.971% | p95=40.504% | max=73.474%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.697%
   Raw/Executed turnover: raw_mean=50.857% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20910):
   Start Date: 2023-01-20 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +38.49%
   Annualized Return: +38.49%
   Sharpe: 2.1284
   Volatility (Ann.): 14.96%
   Max DD: 6.87%
   Turnover (episode): 26.56%
   Turnover (step): mean=26.559% | p95=37.751% | max=58.565%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.446%
   Raw/Executed turnover: raw_mean=48.289% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20911):
   Start Date: 2023-06-23 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +25.54%
   Annualized Return: +25.54%
   Sharpe: 1.8382
   Volatility (Ann.): 11.72%
   Max DD: 7.30%
   Turnover (episode): 27.42%
   Turnover (step): mean=27.420% | p95=38.219% | max=49.248%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.466%
   Raw/Executed turnover: raw_mean=49.855% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20912):
   Start Date: 2023-03-23 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +42.15%
   Annualized Return: +42.15%
   Sharpe: 2.5151
   Volatility (Ann.): 13.63%
   Max DD: 7.73%
   Turnover (episode): 26.39%
   Turnover (step): mean=26.394% | p95=38.615% | max=46.601%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.394%
   Raw/Executed turnover: raw_mean=47.990% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +32.17%
   Std:  6.64%
   Min:  +16.47%
   Max:  +42.15%

Annualized Return (%):
   Mean: +32.17%
   Std:  6.64%
   Min:  +16.47%
   Max:  +42.15%

Sharpe Ratio (annualized):
   Mean: 2.2012
   Std:  0.3574
   Min:  1.2333
   Max:  2.7072

Volatility (Ann. %):
   Mean: +12.11%
   Std:  1.45%
   Min:  +10.40%
   Max:  +14.96%

Max Drawdown (%):
   Mean: 6.64%
   Std:  1.13%
   Min:  5.19%
   Max:  8.90%

Turnover (%):
   Mean: 27.24%
   Std:  0.53%

Turnover Step Detail (%):
   Mean(step mean): 27.237%
   Mean(step p95):  39.055%
   Mean(step max):  51.369%
   Mean exceed rate: 13.0%
   Mean excess over target: 0.542%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_012146.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2023-08-31
   Market Regime: Market Stabilization (2023)
   Episode Length: 501 days (1.99 years)
   Final Portfolio Value: $150,402.22
   Total Return: +50.40%
   Annualized Return: +22.79%
   Sharpe Ratio: 1.6692 (annualized)
   Sortino Ratio: 2.4939 (annualized)
   Max Drawdown: 8.30%
   Volatility (Ann.): 11.54%
   Turnover: 3.32%
   Win Rate: 59.00%
   Diagnostics: action_uniques=501, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=21064):
   Start Date: 2024-03-07 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +2.11%
   Annualized Return: +2.11%
   Sharpe: 0.0571
   Volatility (Ann.): 8.74%
   Max DD: 6.29%
   Turnover (episode): 28.13%
   Turnover (step): mean=28.131% | p95=40.037% | max=56.626%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.648%
   Raw/Executed turnover: raw_mean=51.148% | executed/raw=0.550

[RAND] Run 2/16 (Seed=21065):
   Start Date: 2024-08-16 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.37%
   Annualized Return: +6.37%
   Sharpe: 0.4487
   Volatility (Ann.): 10.66%
   Max DD: 11.40%
   Turnover (episode): 27.29%
   Turnover (step): mean=27.294% | p95=40.315% | max=48.681%
   Turnover vs target: target=35.000% | exceed_rate=15.5% | mean_excess=0.728%
   Raw/Executed turnover: raw_mean=49.625% | executed/raw=0.550

[RAND] Run 3/16 (Seed=21066):
   Start Date: 2024-04-18 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.58%
   Annualized Return: +6.58%
   Sharpe: 0.4227
   Volatility (Ann.): 12.20%
   Max DD: 9.30%
   Turnover (episode): 27.63%
   Turnover (step): mean=27.626% | p95=38.929% | max=49.301%
   Turnover vs target: target=35.000% | exceed_rate=15.5% | mean_excess=0.586%
   Raw/Executed turnover: raw_mean=50.229% | executed/raw=0.550

[RAND] Run 4/16 (Seed=21067):
   Start Date: 2024-01-18 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +17.90%
   Annualized Return: +17.90%
   Sharpe: 1.5154
   Volatility (Ann.): 9.93%
   Max DD: 5.16%
   Turnover (episode): 27.81%
   Turnover (step): mean=27.814% | p95=40.873% | max=54.205%
   Turnover vs target: target=35.000% | exceed_rate=19.9% | mean_excess=0.847%
   Raw/Executed turnover: raw_mean=50.572% | executed/raw=0.550

[RAND] Run 5/16 (Seed=21068):
   Start Date: 2023-11-09 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +36.15%
   Annualized Return: +36.15%
   Sharpe: 2.6414
   Volatility (Ann.): 11.22%
   Max DD: 5.04%
   Turnover (episode): 26.75%
   Turnover (step): mean=26.752% | p95=37.495% | max=63.594%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.413%
   Raw/Executed turnover: raw_mean=48.640% | executed/raw=0.550

[RAND] Run 6/16 (Seed=21069):
   Start Date: 2023-09-28 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +34.80%
   Annualized Return: +34.80%
   Sharpe: 2.5990
   Volatility (Ann.): 11.01%
   Max DD: 5.36%
   Turnover (episode): 27.35%
   Turnover (step): mean=27.349% | p95=37.723% | max=58.576%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.517%
   Raw/Executed turnover: raw_mean=49.725% | executed/raw=0.550

[RAND] Run 7/16 (Seed=21070):
   Start Date: 2024-03-18 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +9.18%
   Annualized Return: +9.18%
   Sharpe: 0.7535
   Volatility (Ann.): 9.70%
   Max DD: 5.09%
   Turnover (episode): 26.63%
   Turnover (step): mean=26.631% | p95=38.816% | max=56.227%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.535%
   Raw/Executed turnover: raw_mean=48.420% | executed/raw=0.550

[RAND] Run 8/16 (Seed=21071):
   Start Date: 2024-08-27 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +2.25%
   Annualized Return: +2.25%
   Sharpe: 0.0778
   Volatility (Ann.): 11.10%
   Max DD: 11.80%
   Turnover (episode): 27.10%
   Turnover (step): mean=27.105% | p95=39.003% | max=48.899%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.538%
   Raw/Executed turnover: raw_mean=49.281% | executed/raw=0.550

[RAND] Run 9/16 (Seed=21072):
   Start Date: 2024-03-18 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.37%
   Annualized Return: +6.37%
   Sharpe: 0.5028
   Volatility (Ann.): 9.24%
   Max DD: 4.63%
   Turnover (episode): 26.55%
   Turnover (step): mean=26.551% | p95=40.199% | max=48.369%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.599%
   Raw/Executed turnover: raw_mean=48.275% | executed/raw=0.550

[RAND] Run 10/16 (Seed=21073):
   Start Date: 2024-05-30 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +5.27%
   Annualized Return: +5.27%
   Sharpe: 0.3449
   Volatility (Ann.): 10.92%
   Max DD: 9.63%
   Turnover (episode): 27.08%
   Turnover (step): mean=27.083% | p95=39.051% | max=52.605%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.530%
   Raw/Executed turnover: raw_mean=49.242% | executed/raw=0.550

[RAND] Run 11/16 (Seed=21074):
   Start Date: 2024-04-18 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +8.68%
   Annualized Return: +8.68%
   Sharpe: 0.5855
   Volatility (Ann.): 12.14%
   Max DD: 9.31%
   Turnover (episode): 27.96%
   Turnover (step): mean=27.955% | p95=40.854% | max=51.323%
   Turnover vs target: target=35.000% | exceed_rate=15.5% | mean_excess=0.757%
   Raw/Executed turnover: raw_mean=50.828% | executed/raw=0.550

[RAND] Run 12/16 (Seed=21075):
   Start Date: 2024-07-18 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +12.40%
   Annualized Return: +12.40%
   Sharpe: 0.8916
   Volatility (Ann.): 11.71%
   Max DD: 9.56%
   Turnover (episode): 28.03%
   Turnover (step): mean=28.029% | p95=40.505% | max=51.259%
   Turnover vs target: target=35.000% | exceed_rate=19.5% | mean_excess=0.770%
   Raw/Executed turnover: raw_mean=50.962% | executed/raw=0.550

[RAND] Run 13/16 (Seed=21076):
   Start Date: 2024-04-11 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +0.42%
   Annualized Return: +0.42%
   Sharpe: -0.0688
   Volatility (Ann.): 12.11%
   Max DD: 10.96%
   Turnover (episode): 26.48%
   Turnover (step): mean=26.484% | p95=37.586% | max=47.910%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.350%
   Raw/Executed turnover: raw_mean=48.153% | executed/raw=0.550

[RAND] Run 14/16 (Seed=21077):
   Start Date: 2024-08-06 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +18.17%
   Annualized Return: +18.17%
   Sharpe: 1.4024
   Volatility (Ann.): 10.97%
   Max DD: 8.17%
   Turnover (episode): 27.68%
   Turnover (step): mean=27.679% | p95=40.042% | max=59.571%
   Turnover vs target: target=35.000% | exceed_rate=13.1% | mean_excess=0.691%
   Raw/Executed turnover: raw_mean=50.326% | executed/raw=0.550

[RAND] Run 15/16 (Seed=21078):
   Start Date: 2023-11-15 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +26.96%
   Annualized Return: +26.96%
   Sharpe: 2.1112
   Volatility (Ann.): 10.69%
   Max DD: 5.39%
   Turnover (episode): 26.23%
   Turnover (step): mean=26.227% | p95=38.139% | max=50.506%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.453%
   Raw/Executed turnover: raw_mean=47.686% | executed/raw=0.550

[RAND] Run 16/16 (Seed=21079):
   Start Date: 2023-09-22 | Regime: Market Stabilization (2023)
   Days Traded: 252 (1.00 years)
   Total Return: +28.53%
   Annualized Return: +28.53%
   Sharpe: 2.0719
   Volatility (Ann.): 11.53%
   Max DD: 7.12%
   Turnover (episode): 27.18%
   Turnover (step): mean=27.177% | p95=40.406% | max=52.928%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.615%
   Raw/Executed turnover: raw_mean=49.413% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +13.88%
   Std:  11.83%
   Min:  +0.42%
   Max:  +36.15%

Annualized Return (%):
   Mean: +13.88%
   Std:  11.83%
   Min:  +0.42%
   Max:  +36.15%

Sharpe Ratio (annualized):
   Mean: 1.0223
   Std:  0.9127
   Min:  -0.0688
   Max:  2.6414

Volatility (Ann. %):
   Mean: +10.87%
   Std:  1.03%
   Min:  +8.74%
   Max:  +12.20%

Max Drawdown (%):
   Mean: 7.76%
   Std:  2.54%
   Min:  4.63%
   Max:  11.80%

Turnover (%):
   Mean: 27.24%
   Std:  0.60%

Turnover Step Detail (%):
   Mean(step mean): 27.243%
   Mean(step p95):  39.373%
   Mean(step max):  53.161%
   Mean exceed rate: 13.7%
   Mean excess over target: 0.599%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_014924.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2020-11-19
   Market Regime: COVID Recovery (2020 Q2-Q4)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $127,200.49
   Total Return: +27.20%
   Annualized Return: +12.78%
   Sharpe Ratio: 0.6506 (annualized)
   Sortino Ratio: 0.9289 (annualized)
   Max Drawdown: 24.06%
   Volatility (Ann.): 17.97%
   Turnover: 3.53%
   Win Rate: 54.47%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20366):
   Start Date: 2021-09-21 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -6.18%
   Annualized Return: -6.18%
   Sharpe: -0.3232
   Volatility (Ann.): 19.85%
   Max DD: 19.92%
   Turnover (episode): 24.87%
   Turnover (step): mean=24.871% | p95=35.509% | max=44.503%
   Turnover vs target: target=35.000% | exceed_rate=5.6% | mean_excess=0.161%
   Raw/Executed turnover: raw_mean=45.220% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20367):
   Start Date: 2021-09-27 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -16.67%
   Annualized Return: -16.67%
   Sharpe: -0.9203
   Volatility (Ann.): 19.89%
   Max DD: 26.67%
   Turnover (episode): 25.55%
   Turnover (step): mean=25.551% | p95=37.164% | max=47.317%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.274%
   Raw/Executed turnover: raw_mean=46.457% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20368):
   Start Date: 2021-02-24 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +10.25%
   Annualized Return: +10.25%
   Sharpe: 0.5787
   Volatility (Ann.): 15.60%
   Max DD: 12.17%
   Turnover (episode): 26.23%
   Turnover (step): mean=26.233% | p95=37.040% | max=47.456%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.305%
   Raw/Executed turnover: raw_mean=47.697% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20369):
   Start Date: 2021-10-08 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -15.11%
   Annualized Return: -15.11%
   Sharpe: -0.8152
   Volatility (Ann.): 20.12%
   Max DD: 25.53%
   Turnover (episode): 25.05%
   Turnover (step): mean=25.055% | p95=36.674% | max=46.892%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.315%
   Raw/Executed turnover: raw_mean=45.554% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20370):
   Start Date: 2021-10-18 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -18.44%
   Annualized Return: -18.44%
   Sharpe: -0.9977
   Volatility (Ann.): 20.40%
   Max DD: 27.55%
   Turnover (episode): 25.35%
   Turnover (step): mean=25.354% | p95=35.543% | max=47.147%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.267%
   Raw/Executed turnover: raw_mean=46.097% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20371):
   Start Date: 2021-08-11 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +5.69%
   Annualized Return: +5.69%
   Sharpe: 0.2945
   Volatility (Ann.): 17.10%
   Max DD: 14.50%
   Turnover (episode): 25.47%
   Turnover (step): mean=25.469% | p95=37.661% | max=47.659%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.362%
   Raw/Executed turnover: raw_mean=46.308% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20372):
   Start Date: 2021-03-03 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +18.64%
   Annualized Return: +18.64%
   Sharpe: 1.0224
   Volatility (Ann.): 16.12%
   Max DD: 12.01%
   Turnover (episode): 25.11%
   Turnover (step): mean=25.112% | p95=36.333% | max=46.556%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.267%
   Raw/Executed turnover: raw_mean=45.658% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20373):
   Start Date: 2021-05-20 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +4.51%
   Annualized Return: +4.51%
   Sharpe: 0.2309
   Volatility (Ann.): 16.43%
   Max DD: 12.18%
   Turnover (episode): 25.28%
   Turnover (step): mean=25.283% | p95=36.105% | max=49.750%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.273%
   Raw/Executed turnover: raw_mean=45.969% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20374):
   Start Date: 2021-06-23 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -2.40%
   Annualized Return: -2.40%
   Sharpe: -0.1697
   Volatility (Ann.): 17.29%
   Max DD: 18.48%
   Turnover (episode): 24.66%
   Turnover (step): mean=24.660% | p95=36.019% | max=44.053%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.228%
   Raw/Executed turnover: raw_mean=44.836% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20375):
   Start Date: 2021-09-22 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -10.00%
   Annualized Return: -10.00%
   Sharpe: -0.5439
   Volatility (Ann.): 19.57%
   Max DD: 22.51%
   Turnover (episode): 25.79%
   Turnover (step): mean=25.787% | p95=37.284% | max=41.629%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.281%
   Raw/Executed turnover: raw_mean=46.885% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20376):
   Start Date: 2021-08-05 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +4.13%
   Annualized Return: +4.13%
   Sharpe: 0.2068
   Volatility (Ann.): 17.34%
   Max DD: 17.99%
   Turnover (episode): 25.86%
   Turnover (step): mean=25.857% | p95=36.981% | max=49.630%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.313%
   Raw/Executed turnover: raw_mean=47.012% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20377):
   Start Date: 2021-09-28 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -13.79%
   Annualized Return: -13.79%
   Sharpe: -0.7493
   Volatility (Ann.): 19.88%
   Max DD: 25.27%
   Turnover (episode): 24.13%
   Turnover (step): mean=24.128% | p95=34.192% | max=49.066%
   Turnover vs target: target=35.000% | exceed_rate=4.0% | mean_excess=0.159%
   Raw/Executed turnover: raw_mean=43.869% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20378):
   Start Date: 2021-08-27 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -11.41%
   Annualized Return: -11.41%
   Sharpe: -0.6793
   Volatility (Ann.): 18.34%
   Max DD: 20.28%
   Turnover (episode): 25.14%
   Turnover (step): mean=25.139% | p95=35.968% | max=42.848%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.229%
   Raw/Executed turnover: raw_mean=45.708% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20379):
   Start Date: 2021-08-12 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +5.07%
   Annualized Return: +5.07%
   Sharpe: 0.2558
   Volatility (Ann.): 17.99%
   Max DD: 16.82%
   Turnover (episode): 25.66%
   Turnover (step): mean=25.662% | p95=36.785% | max=42.984%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.258%
   Raw/Executed turnover: raw_mean=46.658% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20380):
   Start Date: 2021-05-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +16.85%
   Annualized Return: +16.85%
   Sharpe: 0.9162
   Volatility (Ann.): 16.36%
   Max DD: 11.91%
   Turnover (episode): 24.95%
   Turnover (step): mean=24.955% | p95=37.244% | max=48.450%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.297%
   Raw/Executed turnover: raw_mean=45.373% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20381):
   Start Date: 2021-06-11 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +1.08%
   Annualized Return: +1.08%
   Sharpe: 0.0269
   Volatility (Ann.): 16.38%
   Max DD: 15.59%
   Turnover (episode): 25.46%
   Turnover (step): mean=25.460% | p95=36.396% | max=41.108%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.176%
   Raw/Executed turnover: raw_mean=46.291% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: -1.74%
   Std:  11.82%
   Min:  -18.44%
   Max:  +18.64%

Annualized Return (%):
   Mean: -1.74%
   Std:  11.82%
   Min:  -18.44%
   Max:  +18.64%

Sharpe Ratio (annualized):
   Mean: -0.1041
   Std:  0.6457
   Min:  -0.9977
   Max:  1.0224

Volatility (Ann. %):
   Mean: +18.04%
   Std:  1.68%
   Min:  +15.60%
   Max:  +20.40%

Max Drawdown (%):
   Mean: 18.71%
   Std:  5.52%
   Min:  11.91%
   Max:  27.55%

Turnover (%):
   Mean: 25.29%
   Std:  0.51%

Turnover Step Detail (%):
   Mean(step mean): 25.286%
   Mean(step p95):  36.431%
   Mean(step max):  46.066%
   Mean exceed rate: 7.4%
   Mean excess over target: 0.260%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_021700.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2021-05-04
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $123,559.63
   Total Return: +23.56%
   Annualized Return: +11.16%
   Sharpe Ratio: 0.5495 (annualized)
   Sortino Ratio: 0.7961 (annualized)
   Max Drawdown: 24.06%
   Volatility (Ann.): 18.95%
   Turnover: 3.71%
   Win Rate: 52.49%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=7

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20478):
   Start Date: 2021-05-18 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +10.64%
   Annualized Return: +10.64%
   Sharpe: 0.5667
   Volatility (Ann.): 16.95%
   Max DD: 15.40%
   Turnover (episode): 24.79%
   Turnover (step): mean=24.794% | p95=35.799% | max=44.357%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.175%
   Raw/Executed turnover: raw_mean=45.079% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20479):
   Start Date: 2021-06-15 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -1.33%
   Annualized Return: -1.33%
   Sharpe: -0.1151
   Volatility (Ann.): 16.75%
   Max DD: 15.40%
   Turnover (episode): 24.94%
   Turnover (step): mean=24.939% | p95=35.541% | max=45.076%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.249%
   Raw/Executed turnover: raw_mean=45.344% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20480):
   Start Date: 2022-03-14 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -3.35%
   Annualized Return: -3.35%
   Sharpe: -0.1191
   Volatility (Ann.): 23.06%
   Max DD: 25.78%
   Turnover (episode): 26.52%
   Turnover (step): mean=26.519% | p95=36.145% | max=43.259%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.228%
   Raw/Executed turnover: raw_mean=48.216% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20481):
   Start Date: 2022-03-02 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -11.28%
   Annualized Return: -11.28%
   Sharpe: -0.4945
   Volatility (Ann.): 22.98%
   Max DD: 31.78%
   Turnover (episode): 26.91%
   Turnover (step): mean=26.912% | p95=37.241% | max=45.634%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.371%
   Raw/Executed turnover: raw_mean=48.931% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20482):
   Start Date: 2021-10-05 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -8.63%
   Annualized Return: -8.63%
   Sharpe: -0.4459
   Volatility (Ann.): 20.19%
   Max DD: 25.61%
   Turnover (episode): 25.87%
   Turnover (step): mean=25.870% | p95=36.350% | max=45.865%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.187%
   Raw/Executed turnover: raw_mean=47.036% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20483):
   Start Date: 2021-11-03 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.30%
   Annualized Return: -19.30%
   Sharpe: -1.0944
   Volatility (Ann.): 19.70%
   Max DD: 25.96%
   Turnover (episode): 25.07%
   Turnover (step): mean=25.075% | p95=36.595% | max=45.332%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.281%
   Raw/Executed turnover: raw_mean=45.590% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20484):
   Start Date: 2021-12-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -10.11%
   Annualized Return: -10.11%
   Sharpe: -0.5524
   Volatility (Ann.): 19.51%
   Max DD: 24.30%
   Turnover (episode): 24.99%
   Turnover (step): mean=24.992% | p95=36.143% | max=40.737%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.182%
   Raw/Executed turnover: raw_mean=45.439% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20485):
   Start Date: 2022-01-14 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -12.94%
   Annualized Return: -12.94%
   Sharpe: -0.5960
   Volatility (Ann.): 22.45%
   Max DD: 24.39%
   Turnover (episode): 25.99%
   Turnover (step): mean=25.986% | p95=38.009% | max=52.467%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.540%
   Raw/Executed turnover: raw_mean=47.248% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20486):
   Start Date: 2021-07-08 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -0.65%
   Annualized Return: -0.65%
   Sharpe: -0.0571
   Volatility (Ann.): 17.95%
   Max DD: 16.19%
   Turnover (episode): 24.90%
   Turnover (step): mean=24.900% | p95=35.047% | max=47.913%
   Turnover vs target: target=35.000% | exceed_rate=5.2% | mean_excess=0.249%
   Raw/Executed turnover: raw_mean=45.274% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20487):
   Start Date: 2021-09-17 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -9.64%
   Annualized Return: -9.64%
   Sharpe: -0.5355
   Volatility (Ann.): 19.24%
   Max DD: 19.76%
   Turnover (episode): 25.96%
   Turnover (step): mean=25.964% | p95=37.067% | max=50.295%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.346%
   Raw/Executed turnover: raw_mean=47.208% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20488):
   Start Date: 2022-01-28 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -12.92%
   Annualized Return: -12.92%
   Sharpe: -0.5983
   Volatility (Ann.): 22.35%
   Max DD: 28.23%
   Turnover (episode): 25.47%
   Turnover (step): mean=25.472% | p95=37.218% | max=42.768%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.254%
   Raw/Executed turnover: raw_mean=46.312% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20489):
   Start Date: 2021-07-28 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -5.39%
   Annualized Return: -5.39%
   Sharpe: -0.3417
   Volatility (Ann.): 17.57%
   Max DD: 20.12%
   Turnover (episode): 24.84%
   Turnover (step): mean=24.840% | p95=35.050% | max=41.766%
   Turnover vs target: target=35.000% | exceed_rate=5.6% | mean_excess=0.111%
   Raw/Executed turnover: raw_mean=45.163% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20490):
   Start Date: 2021-08-09 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +0.78%
   Annualized Return: +0.78%
   Sharpe: 0.0226
   Volatility (Ann.): 17.95%
   Max DD: 18.38%
   Turnover (episode): 25.34%
   Turnover (step): mean=25.336% | p95=35.643% | max=45.060%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.166%
   Raw/Executed turnover: raw_mean=46.066% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20491):
   Start Date: 2022-01-24 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -6.68%
   Annualized Return: -6.68%
   Sharpe: -0.2785
   Volatility (Ann.): 22.76%
   Max DD: 28.12%
   Turnover (episode): 26.84%
   Turnover (step): mean=26.838% | p95=39.363% | max=45.727%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.482%
   Raw/Executed turnover: raw_mean=48.797% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20492):
   Start Date: 2022-03-23 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -9.78%
   Annualized Return: -9.78%
   Sharpe: -0.4303
   Volatility (Ann.): 22.66%
   Max DD: 29.88%
   Turnover (episode): 26.42%
   Turnover (step): mean=26.425% | p95=37.949% | max=48.018%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.416%
   Raw/Executed turnover: raw_mean=48.045% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20493):
   Start Date: 2021-08-09 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +1.51%
   Annualized Return: +1.51%
   Sharpe: 0.0616
   Volatility (Ann.): 17.70%
   Max DD: 17.93%
   Turnover (episode): 25.59%
   Turnover (step): mean=25.595% | p95=37.138% | max=46.412%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.323%
   Raw/Executed turnover: raw_mean=46.536% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: -6.19%
   Std:  7.25%
   Min:  -19.30%
   Max:  +10.64%

Annualized Return (%):
   Mean: -6.19%
   Std:  7.25%
   Min:  -19.30%
   Max:  +10.64%

Sharpe Ratio (annualized):
   Mean: -0.3130
   Std:  0.3754
   Min:  -1.0944
   Max:  0.5667

Volatility (Ann. %):
   Mean: +19.99%
   Std:  2.38%
   Min:  +16.75%
   Max:  +23.06%

Max Drawdown (%):
   Mean: 22.95%
   Std:  5.37%
   Min:  15.40%
   Max:  31.78%

Turnover (%):
   Mean: 25.65%
   Std:  0.73%

Turnover Step Detail (%):
   Mean(step mean): 25.654%
   Mean(step p95):  36.644%
   Mean(step max):  45.668%
   Mean exceed rate: 8.6%
   Mean excess over target: 0.285%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_024437.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2021-10-12
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $138,576.39
   Total Return: +38.58%
   Annualized Return: +17.72%
   Sharpe Ratio: 0.8261 (annualized)
   Sortino Ratio: 1.2413 (annualized)
   Max Drawdown: 24.20%
   Volatility (Ann.): 19.75%
   Turnover: 3.35%
   Win Rate: 52.09%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20590):
   Start Date: 2022-03-15 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -9.79%
   Annualized Return: -9.79%
   Sharpe: -0.4704
   Volatility (Ann.): 21.36%
   Max DD: 28.36%
   Turnover (episode): 26.12%
   Turnover (step): mean=26.123% | p95=37.634% | max=41.472%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.274%
   Raw/Executed turnover: raw_mean=47.496% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20591):
   Start Date: 2021-11-09 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -23.01%
   Annualized Return: -23.01%
   Sharpe: -1.3257
   Volatility (Ann.): 19.81%
   Max DD: 28.20%
   Turnover (episode): 26.92%
   Turnover (step): mean=26.918% | p95=37.194% | max=48.578%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.284%
   Raw/Executed turnover: raw_mean=48.942% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20592):
   Start Date: 2021-10-20 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -14.81%
   Annualized Return: -14.81%
   Sharpe: -0.7950
   Volatility (Ann.): 20.17%
   Max DD: 25.04%
   Turnover (episode): 25.93%
   Turnover (step): mean=25.928% | p95=37.989% | max=45.493%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.310%
   Raw/Executed turnover: raw_mean=47.141% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20593):
   Start Date: 2022-03-04 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -4.53%
   Annualized Return: -4.53%
   Sharpe: -0.2111
   Volatility (Ann.): 21.01%
   Max DD: 23.87%
   Turnover (episode): 26.22%
   Turnover (step): mean=26.215% | p95=38.013% | max=47.565%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.381%
   Raw/Executed turnover: raw_mean=47.665% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20594):
   Start Date: 2022-10-10 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +52.90%
   Annualized Return: +52.90%
   Sharpe: 2.0800
   Volatility (Ann.): 20.56%
   Max DD: 7.79%
   Turnover (episode): 26.06%
   Turnover (step): mean=26.061% | p95=37.820% | max=50.362%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.433%
   Raw/Executed turnover: raw_mean=47.383% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20595):
   Start Date: 2022-10-10 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +45.97%
   Annualized Return: +45.97%
   Sharpe: 2.0548
   Volatility (Ann.): 18.34%
   Max DD: 7.83%
   Turnover (episode): 26.42%
   Turnover (step): mean=26.416% | p95=37.545% | max=49.938%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.523%
   Raw/Executed turnover: raw_mean=48.028% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20596):
   Start Date: 2022-02-28 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -9.11%
   Annualized Return: -9.11%
   Sharpe: -0.4377
   Volatility (Ann.): 21.27%
   Max DD: 26.56%
   Turnover (episode): 26.63%
   Turnover (step): mean=26.630% | p95=38.107% | max=51.081%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.463%
   Raw/Executed turnover: raw_mean=48.419% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20597):
   Start Date: 2021-11-02 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -20.20%
   Annualized Return: -20.20%
   Sharpe: -1.0972
   Volatility (Ann.): 20.53%
   Max DD: 28.82%
   Turnover (episode): 25.33%
   Turnover (step): mean=25.326% | p95=37.244% | max=48.104%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.350%
   Raw/Executed turnover: raw_mean=46.048% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20598):
   Start Date: 2022-03-14 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -8.79%
   Annualized Return: -8.79%
   Sharpe: -0.3738
   Volatility (Ann.): 22.96%
   Max DD: 27.56%
   Turnover (episode): 26.05%
   Turnover (step): mean=26.050% | p95=39.508% | max=48.232%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.436%
   Raw/Executed turnover: raw_mean=47.364% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20599):
   Start Date: 2022-06-10 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +19.33%
   Annualized Return: +19.33%
   Sharpe: 0.8344
   Volatility (Ann.): 21.70%
   Max DD: 18.90%
   Turnover (episode): 26.57%
   Turnover (step): mean=26.571% | p95=38.313% | max=48.157%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.441%
   Raw/Executed turnover: raw_mean=48.310% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20600):
   Start Date: 2022-02-09 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -11.81%
   Annualized Return: -11.81%
   Sharpe: -0.5228
   Volatility (Ann.): 22.90%
   Max DD: 27.39%
   Turnover (episode): 26.06%
   Turnover (step): mean=26.064% | p95=37.451% | max=42.827%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.287%
   Raw/Executed turnover: raw_mean=47.388% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20601):
   Start Date: 2022-07-11 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +30.96%
   Annualized Return: +30.96%
   Sharpe: 1.2688
   Volatility (Ann.): 21.63%
   Max DD: 21.25%
   Turnover (episode): 26.76%
   Turnover (step): mean=26.757% | p95=38.839% | max=47.645%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.468%
   Raw/Executed turnover: raw_mean=48.649% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20602):
   Start Date: 2022-04-25 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +1.17%
   Annualized Return: +1.17%
   Sharpe: 0.0815
   Volatility (Ann.): 23.30%
   Max DD: 21.57%
   Turnover (episode): 26.73%
   Turnover (step): mean=26.735% | p95=37.978% | max=49.120%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.455%
   Raw/Executed turnover: raw_mean=48.609% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20603):
   Start Date: 2021-11-11 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -15.77%
   Annualized Return: -15.77%
   Sharpe: -0.8557
   Volatility (Ann.): 20.09%
   Max DD: 23.42%
   Turnover (episode): 25.82%
   Turnover (step): mean=25.819% | p95=35.896% | max=46.865%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.231%
   Raw/Executed turnover: raw_mean=46.944% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20604):
   Start Date: 2022-02-16 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: -13.26%
   Annualized Return: -13.26%
   Sharpe: -0.6049
   Volatility (Ann.): 22.65%
   Max DD: 32.06%
   Turnover (episode): 25.78%
   Turnover (step): mean=25.778% | p95=36.127% | max=52.021%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.360%
   Raw/Executed turnover: raw_mean=46.869% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20605):
   Start Date: 2022-10-11 | Regime: Rate Hikes / Tech Correction (2022)
   Days Traded: 252 (1.00 years)
   Total Return: +52.71%
   Annualized Return: +52.71%
   Sharpe: 2.0699
   Volatility (Ann.): 20.61%
   Max DD: 7.73%
   Turnover (episode): 26.50%
   Turnover (step): mean=26.505% | p95=38.110% | max=45.786%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.403%
   Raw/Executed turnover: raw_mean=48.190% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +4.50%
   Std:  26.70%
   Min:  -23.01%
   Max:  +52.90%

Annualized Return (%):
   Mean: +4.50%
   Std:  26.70%
   Min:  -23.01%
   Max:  +52.90%

Sharpe Ratio (annualized):
   Mean: 0.1059
   Std:  1.1698
   Min:  -1.3257
   Max:  2.0800

Volatility (Ann. %):
   Mean: +21.18%
   Std:  1.33%
   Min:  +18.34%
   Max:  +23.30%

Max Drawdown (%):
   Mean: 22.27%
   Std:  7.91%
   Min:  7.73%
   Max:  32.06%

Turnover (%):
   Mean: 26.24%
   Std:  0.43%

Turnover Step Detail (%):
   Mean(step mean): 26.243%
   Mean(step p95):  37.736%
   Mean(step max):  47.703%
   Mean exceed rate: 9.9%
   Mean excess over target: 0.381%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_031217.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2020-01-10
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $187,029.66
   Total Return: +87.03%
   Annualized Return: +36.76%
   Sharpe Ratio: 1.2942 (annualized)
   Sortino Ratio: 1.8366 (annualized)
   Max Drawdown: 28.98%
   Volatility (Ann.): 25.18%
   Turnover: 3.17%
   Win Rate: 59.24%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20148):
   Start Date: 2020-09-24 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +29.78%
   Annualized Return: +29.78%
   Sharpe: 1.8267
   Volatility (Ann.): 13.77%
   Max DD: 6.31%
   Turnover (episode): 26.66%
   Turnover (step): mean=26.659% | p95=38.058% | max=53.363%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.448%
   Raw/Executed turnover: raw_mean=48.471% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20149):
   Start Date: 2020-11-04 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +37.51%
   Annualized Return: +37.51%
   Sharpe: 2.2595
   Volatility (Ann.): 13.70%
   Max DD: 5.07%
   Turnover (episode): 25.27%
   Turnover (step): mean=25.271% | p95=36.239% | max=47.744%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.259%
   Raw/Executed turnover: raw_mean=45.947% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20150):
   Start Date: 2020-12-21 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +24.60%
   Annualized Return: +24.60%
   Sharpe: 1.3718
   Volatility (Ann.): 15.54%
   Max DD: 6.48%
   Turnover (episode): 25.53%
   Turnover (step): mean=25.534% | p95=37.107% | max=43.665%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.263%
   Raw/Executed turnover: raw_mean=46.426% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20151):
   Start Date: 2020-09-14 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +28.28%
   Annualized Return: +28.28%
   Sharpe: 1.6855
   Volatility (Ann.): 14.27%
   Max DD: 6.08%
   Turnover (episode): 25.47%
   Turnover (step): mean=25.468% | p95=36.313% | max=46.364%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.315%
   Raw/Executed turnover: raw_mean=46.306% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20152):
   Start Date: 2020-04-17 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +40.79%
   Annualized Return: +40.79%
   Sharpe: 1.8366
   Volatility (Ann.): 18.58%
   Max DD: 8.14%
   Turnover (episode): 24.61%
   Turnover (step): mean=24.608% | p95=36.304% | max=46.997%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.299%
   Raw/Executed turnover: raw_mean=44.741% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20153):
   Start Date: 2020-11-02 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +42.85%
   Annualized Return: +42.85%
   Sharpe: 2.5915
   Volatility (Ann.): 13.41%
   Max DD: 4.47%
   Turnover (episode): 25.98%
   Turnover (step): mean=25.984% | p95=36.991% | max=43.425%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.206%
   Raw/Executed turnover: raw_mean=47.244% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20154):
   Start Date: 2020-01-21 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +26.53%
   Annualized Return: +26.53%
   Sharpe: 0.8196
   Volatility (Ann.): 33.16%
   Max DD: 28.97%
   Turnover (episode): 24.94%
   Turnover (step): mean=24.937% | p95=36.048% | max=42.191%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.183%
   Raw/Executed turnover: raw_mean=45.339% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20155):
   Start Date: 2020-11-20 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +39.46%
   Annualized Return: +39.46%
   Sharpe: 2.2710
   Volatility (Ann.): 14.29%
   Max DD: 5.02%
   Turnover (episode): 25.91%
   Turnover (step): mean=25.913% | p95=35.929% | max=45.792%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.265%
   Raw/Executed turnover: raw_mean=47.115% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20156):
   Start Date: 2020-01-10 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +31.09%
   Annualized Return: +31.09%
   Sharpe: 0.9353
   Volatility (Ann.): 32.71%
   Max DD: 29.65%
   Turnover (episode): 24.91%
   Turnover (step): mean=24.912% | p95=36.256% | max=44.083%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.208%
   Raw/Executed turnover: raw_mean=45.295% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20157):
   Start Date: 2020-10-21 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +31.59%
   Annualized Return: +31.59%
   Sharpe: 1.8399
   Volatility (Ann.): 14.48%
   Max DD: 5.60%
   Turnover (episode): 25.84%
   Turnover (step): mean=25.841% | p95=37.844% | max=49.155%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.399%
   Raw/Executed turnover: raw_mean=46.984% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20158):
   Start Date: 2020-04-15 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +45.75%
   Annualized Return: +45.75%
   Sharpe: 1.9706
   Volatility (Ann.): 19.13%
   Max DD: 9.10%
   Turnover (episode): 24.62%
   Turnover (step): mean=24.618% | p95=34.538% | max=43.299%
   Turnover vs target: target=35.000% | exceed_rate=4.8% | mean_excess=0.161%
   Raw/Executed turnover: raw_mean=44.759% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20159):
   Start Date: 2020-08-13 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +19.12%
   Annualized Return: +19.12%
   Sharpe: 1.1240
   Volatility (Ann.): 14.85%
   Max DD: 8.92%
   Turnover (episode): 25.44%
   Turnover (step): mean=25.444% | p95=37.721% | max=57.252%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.361%
   Raw/Executed turnover: raw_mean=46.262% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20160):
   Start Date: 2020-05-06 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +49.88%
   Annualized Return: +49.88%
   Sharpe: 2.3128
   Volatility (Ann.): 17.38%
   Max DD: 8.10%
   Turnover (episode): 25.31%
   Turnover (step): mean=25.312% | p95=35.542% | max=43.096%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.173%
   Raw/Executed turnover: raw_mean=46.023% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20161):
   Start Date: 2020-10-27 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +30.96%
   Annualized Return: +30.96%
   Sharpe: 1.8601
   Volatility (Ann.): 14.03%
   Max DD: 4.75%
   Turnover (episode): 25.94%
   Turnover (step): mean=25.942% | p95=38.363% | max=52.240%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.475%
   Raw/Executed turnover: raw_mean=47.168% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20162):
   Start Date: 2020-05-15 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +40.66%
   Annualized Return: +40.66%
   Sharpe: 1.8622
   Volatility (Ann.): 18.24%
   Max DD: 8.36%
   Turnover (episode): 25.63%
   Turnover (step): mean=25.631% | p95=37.892% | max=50.379%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.407%
   Raw/Executed turnover: raw_mean=46.601% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20163):
   Start Date: 2020-12-21 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +25.16%
   Annualized Return: +25.16%
   Sharpe: 1.4012
   Volatility (Ann.): 15.53%
   Max DD: 6.47%
   Turnover (episode): 25.36%
   Turnover (step): mean=25.362% | p95=35.981% | max=45.195%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.290%
   Raw/Executed turnover: raw_mean=46.112% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +34.00%
   Std:  8.64%
   Min:  +19.12%
   Max:  +49.88%

Annualized Return (%):
   Mean: +34.00%
   Std:  8.64%
   Min:  +19.12%
   Max:  +49.88%

Sharpe Ratio (annualized):
   Mean: 1.7480
   Std:  0.5060
   Min:  0.8196
   Max:  2.5915

Volatility (Ann. %):
   Mean: +17.69%
   Std:  6.23%
   Min:  +13.41%
   Max:  +33.16%

Max Drawdown (%):
   Mean: 9.47%
   Std:  7.89%
   Min:  4.47%
   Max:  29.65%

Turnover (%):
   Mean: 25.46%
   Std:  0.54%

Turnover Step Detail (%):
   Mean(step mean): 25.465%
   Mean(step p95):  36.695%
   Mean(step max):  47.140%
   Mean exceed rate: 8.0%
   Mean excess over target: 0.294%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_033955.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2020-01-31
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $170,501.10
   Total Return: +70.50%
   Annualized Return: +30.58%
   Sharpe Ratio: 1.1803 (annualized)
   Sortino Ratio: 1.6809 (annualized)
   Max Drawdown: 25.96%
   Volatility (Ann.): 23.28%
   Turnover: 3.36%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20162):
   Start Date: 2020-06-05 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +34.98%
   Annualized Return: +34.98%
   Sharpe: 1.8048
   Volatility (Ann.): 16.34%
   Max DD: 8.11%
   Turnover (episode): 26.72%
   Turnover (step): mean=26.719% | p95=38.130% | max=57.108%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.406%
   Raw/Executed turnover: raw_mean=48.581% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20163):
   Start Date: 2021-01-12 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +23.87%
   Annualized Return: +23.87%
   Sharpe: 1.3601
   Volatility (Ann.): 15.20%
   Max DD: 6.64%
   Turnover (episode): 26.48%
   Turnover (step): mean=26.476% | p95=38.656% | max=53.357%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.516%
   Raw/Executed turnover: raw_mean=48.138% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20164):
   Start Date: 2020-12-09 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +30.01%
   Annualized Return: +30.01%
   Sharpe: 1.7499
   Volatility (Ann.): 14.53%
   Max DD: 4.75%
   Turnover (episode): 26.14%
   Turnover (step): mean=26.137% | p95=38.668% | max=47.874%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.497%
   Raw/Executed turnover: raw_mean=47.522% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20165):
   Start Date: 2020-09-08 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +27.85%
   Annualized Return: +27.85%
   Sharpe: 1.6297
   Volatility (Ann.): 14.58%
   Max DD: 7.87%
   Turnover (episode): 25.63%
   Turnover (step): mean=25.626% | p95=37.133% | max=42.009%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.260%
   Raw/Executed turnover: raw_mean=46.593% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20166):
   Start Date: 2021-01-05 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +32.02%
   Annualized Return: +32.02%
   Sharpe: 1.7338
   Volatility (Ann.): 15.66%
   Max DD: 6.09%
   Turnover (episode): 25.26%
   Turnover (step): mean=25.263% | p95=36.575% | max=43.617%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.219%
   Raw/Executed turnover: raw_mean=45.933% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20167):
   Start Date: 2020-05-05 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +48.70%
   Annualized Return: +48.70%
   Sharpe: 2.3446
   Volatility (Ann.): 16.76%
   Max DD: 8.20%
   Turnover (episode): 24.93%
   Turnover (step): mean=24.928% | p95=35.502% | max=42.771%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.171%
   Raw/Executed turnover: raw_mean=45.323% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20168):
   Start Date: 2020-10-06 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +24.41%
   Annualized Return: +24.41%
   Sharpe: 1.4763
   Volatility (Ann.): 14.20%
   Max DD: 7.14%
   Turnover (episode): 26.40%
   Turnover (step): mean=26.400% | p95=37.894% | max=56.418%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.421%
   Raw/Executed turnover: raw_mean=48.001% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20169):
   Start Date: 2020-02-19 | Regime: Pre-COVID (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +19.00%
   Annualized Return: +19.00%
   Sharpe: 0.6637
   Volatility (Ann.): 30.30%
   Max DD: 30.47%
   Turnover (episode): 25.21%
   Turnover (step): mean=25.209% | p95=36.228% | max=49.115%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.261%
   Raw/Executed turnover: raw_mean=45.835% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20170):
   Start Date: 2020-05-27 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +30.40%
   Annualized Return: +30.40%
   Sharpe: 1.4921
   Volatility (Ann.): 17.58%
   Max DD: 8.30%
   Turnover (episode): 25.91%
   Turnover (step): mean=25.908% | p95=37.972% | max=44.886%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.338%
   Raw/Executed turnover: raw_mean=47.105% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20171):
   Start Date: 2020-10-12 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +21.57%
   Annualized Return: +21.57%
   Sharpe: 1.2937
   Volatility (Ann.): 14.43%
   Max DD: 6.76%
   Turnover (episode): 26.02%
   Turnover (step): mean=26.016% | p95=37.683% | max=46.137%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.364%
   Raw/Executed turnover: raw_mean=47.301% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20172):
   Start Date: 2020-07-09 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +38.50%
   Annualized Return: +38.50%
   Sharpe: 2.0008
   Volatility (Ann.): 16.00%
   Max DD: 9.21%
   Turnover (episode): 25.40%
   Turnover (step): mean=25.401% | p95=37.794% | max=48.752%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.333%
   Raw/Executed turnover: raw_mean=46.184% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20173):
   Start Date: 2020-09-08 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +26.73%
   Annualized Return: +26.73%
   Sharpe: 1.5980
   Volatility (Ann.): 14.29%
   Max DD: 6.72%
   Turnover (episode): 26.42%
   Turnover (step): mean=26.415% | p95=38.851% | max=49.044%
   Turnover vs target: target=35.000% | exceed_rate=12.7% | mean_excess=0.467%
   Raw/Executed turnover: raw_mean=48.028% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20174):
   Start Date: 2020-04-06 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +55.38%
   Annualized Return: +55.38%
   Sharpe: 2.2583
   Volatility (Ann.): 19.58%
   Max DD: 8.12%
   Turnover (episode): 25.45%
   Turnover (step): mean=25.455% | p95=37.682% | max=50.740%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.363%
   Raw/Executed turnover: raw_mean=46.281% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20175):
   Start Date: 2021-01-19 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +25.80%
   Annualized Return: +25.80%
   Sharpe: 1.4907
   Volatility (Ann.): 14.88%
   Max DD: 6.72%
   Turnover (episode): 25.97%
   Turnover (step): mean=25.973% | p95=36.673% | max=50.426%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.367%
   Raw/Executed turnover: raw_mean=47.224% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20176):
   Start Date: 2020-11-16 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +30.94%
   Annualized Return: +30.94%
   Sharpe: 1.8444
   Volatility (Ann.): 14.15%
   Max DD: 4.90%
   Turnover (episode): 25.19%
   Turnover (step): mean=25.194% | p95=35.974% | max=41.040%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.156%
   Raw/Executed turnover: raw_mean=45.808% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20177):
   Start Date: 2020-10-14 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +27.79%
   Annualized Return: +27.79%
   Sharpe: 1.6066
   Volatility (Ann.): 14.78%
   Max DD: 6.21%
   Turnover (episode): 25.22%
   Turnover (step): mean=25.217% | p95=35.757% | max=48.327%
   Turnover vs target: target=35.000% | exceed_rate=5.6% | mean_excess=0.207%
   Raw/Executed turnover: raw_mean=45.848% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +31.12%
   Std:  9.57%
   Min:  +19.00%
   Max:  +55.38%

Annualized Return (%):
   Mean: +31.12%
   Std:  9.57%
   Min:  +19.00%
   Max:  +55.38%

Sharpe Ratio (annualized):
   Mean: 1.6467
   Std:  0.3936
   Min:  0.6637
   Max:  2.3446

Volatility (Ann. %):
   Mean: +16.45%
   Std:  3.98%
   Min:  +14.15%
   Max:  +30.30%

Max Drawdown (%):
   Mean: 8.51%
   Std:  5.98%
   Min:  4.75%
   Max:  30.47%

Turnover (%):
   Mean: 25.77%
   Std:  0.56%

Turnover Step Detail (%):
   Mean(step mean): 25.771%
   Mean(step p95):  37.323%
   Mean(step max):  48.226%
   Mean exceed rate: 9.2%
   Mean excess over target: 0.334%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_040734.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2020-02-20
   Market Regime: Pre-COVID (2020 Q1)
   Episode Length: 504 days (2.00 years)
   Final Portfolio Value: $166,449.03
   Total Return: +66.45%
   Annualized Return: +29.02%
   Sharpe Ratio: 1.0407 (annualized)
   Sortino Ratio: 1.4767 (annualized)
   Max Drawdown: 27.93%
   Volatility (Ann.): 25.86%
   Turnover: 3.27%
   Win Rate: 58.25%
   Diagnostics: action_uniques=504, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=20175):
   Start Date: 2021-02-05 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +18.85%
   Annualized Return: +18.85%
   Sharpe: 1.0719
   Volatility (Ann.): 15.44%
   Max DD: 10.87%
   Turnover (episode): 26.05%
   Turnover (step): mean=26.051% | p95=36.759% | max=41.252%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.246%
   Raw/Executed turnover: raw_mean=47.365% | executed/raw=0.550

[RAND] Run 2/16 (Seed=20176):
   Start Date: 2020-12-04 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +23.12%
   Annualized Return: +23.12%
   Sharpe: 1.4085
   Volatility (Ann.): 14.13%
   Max DD: 5.05%
   Turnover (episode): 25.44%
   Turnover (step): mean=25.438% | p95=36.126% | max=45.816%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.251%
   Raw/Executed turnover: raw_mean=46.251% | executed/raw=0.550

[RAND] Run 3/16 (Seed=20177):
   Start Date: 2020-11-02 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +43.69%
   Annualized Return: +43.69%
   Sharpe: 2.5409
   Volatility (Ann.): 13.93%
   Max DD: 5.48%
   Turnover (episode): 26.08%
   Turnover (step): mean=26.076% | p95=36.603% | max=41.778%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.233%
   Raw/Executed turnover: raw_mean=47.411% | executed/raw=0.550

[RAND] Run 4/16 (Seed=20178):
   Start Date: 2020-05-27 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +35.54%
   Annualized Return: +35.54%
   Sharpe: 1.7343
   Volatility (Ann.): 17.34%
   Max DD: 8.53%
   Turnover (episode): 25.72%
   Turnover (step): mean=25.722% | p95=36.464% | max=44.652%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.241%
   Raw/Executed turnover: raw_mean=46.767% | executed/raw=0.550

[RAND] Run 5/16 (Seed=20179):
   Start Date: 2020-10-14 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +19.56%
   Annualized Return: +19.56%
   Sharpe: 1.2063
   Volatility (Ann.): 14.05%
   Max DD: 6.44%
   Turnover (episode): 26.16%
   Turnover (step): mean=26.162% | p95=38.682% | max=47.715%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.472%
   Raw/Executed turnover: raw_mean=47.567% | executed/raw=0.550

[RAND] Run 6/16 (Seed=20180):
   Start Date: 2021-02-05 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +15.58%
   Annualized Return: +15.58%
   Sharpe: 0.8561
   Volatility (Ann.): 16.20%
   Max DD: 11.36%
   Turnover (episode): 24.56%
   Turnover (step): mean=24.561% | p95=36.104% | max=43.856%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.217%
   Raw/Executed turnover: raw_mean=44.657% | executed/raw=0.550

[RAND] Run 7/16 (Seed=20181):
   Start Date: 2020-11-13 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +38.41%
   Annualized Return: +38.41%
   Sharpe: 2.2677
   Volatility (Ann.): 13.95%
   Max DD: 5.07%
   Turnover (episode): 24.87%
   Turnover (step): mean=24.866% | p95=35.555% | max=41.573%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.135%
   Raw/Executed turnover: raw_mean=45.211% | executed/raw=0.550

[RAND] Run 8/16 (Seed=20182):
   Start Date: 2020-03-06 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +42.41%
   Annualized Return: +42.41%
   Sharpe: 1.2170
   Volatility (Ann.): 31.70%
   Max DD: 22.23%
   Turnover (episode): 25.38%
   Turnover (step): mean=25.382% | p95=35.996% | max=43.414%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.213%
   Raw/Executed turnover: raw_mean=46.149% | executed/raw=0.550

[RAND] Run 9/16 (Seed=20183):
   Start Date: 2020-03-02 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +25.88%
   Annualized Return: +25.88%
   Sharpe: 0.8344
   Volatility (Ann.): 31.23%
   Max DD: 27.77%
   Turnover (episode): 25.65%
   Turnover (step): mean=25.649% | p95=37.196% | max=43.866%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.316%
   Raw/Executed turnover: raw_mean=46.634% | executed/raw=0.550

[RAND] Run 10/16 (Seed=20184):
   Start Date: 2020-06-01 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +39.36%
   Annualized Return: +39.36%
   Sharpe: 1.8337
   Volatility (Ann.): 17.99%
   Max DD: 8.78%
   Turnover (episode): 26.32%
   Turnover (step): mean=26.319% | p95=37.738% | max=47.045%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.419%
   Raw/Executed turnover: raw_mean=47.852% | executed/raw=0.550

[RAND] Run 11/16 (Seed=20185):
   Start Date: 2020-05-15 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +46.06%
   Annualized Return: +46.06%
   Sharpe: 2.1578
   Volatility (Ann.): 17.43%
   Max DD: 7.74%
   Turnover (episode): 26.72%
   Turnover (step): mean=26.716% | p95=38.505% | max=46.567%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.469%
   Raw/Executed turnover: raw_mean=48.575% | executed/raw=0.550

[RAND] Run 12/16 (Seed=20186):
   Start Date: 2020-03-04 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +31.89%
   Annualized Return: +31.89%
   Sharpe: 1.0473
   Volatility (Ann.): 28.56%
   Max DD: 22.94%
   Turnover (episode): 25.75%
   Turnover (step): mean=25.749% | p95=36.833% | max=42.867%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.220%
   Raw/Executed turnover: raw_mean=46.815% | executed/raw=0.550

[RAND] Run 13/16 (Seed=20187):
   Start Date: 2020-10-08 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +26.77%
   Annualized Return: +26.77%
   Sharpe: 1.5576
   Volatility (Ann.): 14.72%
   Max DD: 7.19%
   Turnover (episode): 25.36%
   Turnover (step): mean=25.360% | p95=35.725% | max=50.711%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.264%
   Raw/Executed turnover: raw_mean=46.109% | executed/raw=0.550

[RAND] Run 14/16 (Seed=20188):
   Start Date: 2021-02-16 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +8.03%
   Annualized Return: +8.03%
   Sharpe: 0.4479
   Volatility (Ann.): 15.62%
   Max DD: 13.60%
   Turnover (episode): 24.93%
   Turnover (step): mean=24.927% | p95=36.126% | max=43.850%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.204%
   Raw/Executed turnover: raw_mean=45.322% | executed/raw=0.550

[RAND] Run 15/16 (Seed=20189):
   Start Date: 2020-10-30 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +37.84%
   Annualized Return: +37.84%
   Sharpe: 2.1899
   Volatility (Ann.): 14.28%
   Max DD: 5.37%
   Turnover (episode): 24.86%
   Turnover (step): mean=24.861% | p95=35.840% | max=50.555%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.242%
   Raw/Executed turnover: raw_mean=45.202% | executed/raw=0.550

[RAND] Run 16/16 (Seed=20190):
   Start Date: 2020-04-17 | Regime: COVID Crash (2020 Q1)
   Days Traded: 252 (1.00 years)
   Total Return: +47.33%
   Annualized Return: +47.33%
   Sharpe: 2.0603
   Volatility (Ann.): 18.79%
   Max DD: 7.97%
   Turnover (episode): 25.35%
   Turnover (step): mean=25.353% | p95=36.241% | max=45.964%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.273%
   Raw/Executed turnover: raw_mean=46.097% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +31.27%
   Std:  11.91%
   Min:  +8.03%
   Max:  +47.33%

Annualized Return (%):
   Mean: +31.27%
   Std:  11.91%
   Min:  +8.03%
   Max:  +47.33%

Sharpe Ratio (annualized):
   Mean: 1.5270
   Std:  0.6100
   Min:  0.4479
   Max:  2.5409

Volatility (Ann. %):
   Mean: +18.46%
   Std:  6.20%
   Min:  +13.93%
   Max:  +31.70%

Max Drawdown (%):
   Mean: 11.02%
   Std:  7.10%
   Min:  5.05%
   Max:  27.77%

Turnover (%):
   Mean: 25.57%
   Std:  0.60%

Turnover Step Detail (%):
   Mean(step mean): 25.574%
   Mean(step p95):  36.656%
   Mean(step max):  45.093%
   Mean exceed rate: 8.4%
   Mean excess over target: 0.276%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_043515.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2024-02-09
   Market Regime: Continued Growth (2024)
   Episode Length: 390 days (1.55 years)
   Final Portfolio Value: $135,670.80
   Total Return: +35.67%
   Annualized Return: +21.79%
   Sharpe Ratio: 1.6592 (annualized)
   Sortino Ratio: 2.4786 (annualized)
   Max Drawdown: 7.98%
   Volatility (Ann.): 11.09%
   Turnover: 3.33%
   Win Rate: 59.38%
   Diagnostics: action_uniques=390, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=21175):
   Start Date: 2024-04-11 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: -1.10%
   Annualized Return: -1.10%
   Sharpe: -0.1912
   Volatility (Ann.): 12.26%
   Max DD: 11.30%
   Turnover (episode): 27.59%
   Turnover (step): mean=27.591% | p95=41.153% | max=57.003%
   Turnover vs target: target=35.000% | exceed_rate=16.7% | mean_excess=0.806%
   Raw/Executed turnover: raw_mean=50.166% | executed/raw=0.550

[RAND] Run 2/16 (Seed=21176):
   Start Date: 2024-08-12 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +10.69%
   Annualized Return: +10.69%
   Sharpe: 0.7850
   Volatility (Ann.): 11.28%
   Max DD: 11.21%
   Turnover (episode): 27.62%
   Turnover (step): mean=27.616% | p95=39.636% | max=52.239%
   Turnover vs target: target=35.000% | exceed_rate=14.7% | mean_excess=0.614%
   Raw/Executed turnover: raw_mean=50.210% | executed/raw=0.550

[RAND] Run 3/16 (Seed=21177):
   Start Date: 2024-05-31 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +5.93%
   Annualized Return: +5.93%
   Sharpe: 0.3774
   Volatility (Ann.): 11.98%
   Max DD: 10.62%
   Turnover (episode): 27.58%
   Turnover (step): mean=27.580% | p95=40.411% | max=49.374%
   Turnover vs target: target=35.000% | exceed_rate=14.3% | mean_excess=0.673%
   Raw/Executed turnover: raw_mean=50.145% | executed/raw=0.550

[RAND] Run 4/16 (Seed=21178):
   Start Date: 2024-06-12 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +4.71%
   Annualized Return: +4.71%
   Sharpe: 0.2838
   Volatility (Ann.): 11.72%
   Max DD: 9.79%
   Turnover (episode): 26.54%
   Turnover (step): mean=26.543% | p95=37.904% | max=44.954%
   Turnover vs target: target=35.000% | exceed_rate=12.7% | mean_excess=0.446%
   Raw/Executed turnover: raw_mean=48.259% | executed/raw=0.550

[RAND] Run 5/16 (Seed=21179):
   Start Date: 2024-06-27 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +5.95%
   Annualized Return: +5.95%
   Sharpe: 0.3707
   Volatility (Ann.): 12.35%
   Max DD: 8.86%
   Turnover (episode): 27.52%
   Turnover (step): mean=27.521% | p95=39.015% | max=54.922%
   Turnover vs target: target=35.000% | exceed_rate=15.5% | mean_excess=0.616%
   Raw/Executed turnover: raw_mean=50.039% | executed/raw=0.550

[RAND] Run 6/16 (Seed=21180):
   Start Date: 2024-05-28 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +4.22%
   Annualized Return: +4.22%
   Sharpe: 0.2470
   Volatility (Ann.): 11.40%
   Max DD: 9.87%
   Turnover (episode): 27.50%
   Turnover (step): mean=27.499% | p95=39.197% | max=51.564%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.541%
   Raw/Executed turnover: raw_mean=49.999% | executed/raw=0.550

[RAND] Run 7/16 (Seed=21181):
   Start Date: 2024-06-26 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +7.02%
   Annualized Return: +7.02%
   Sharpe: 0.4535
   Volatility (Ann.): 12.31%
   Max DD: 8.54%
   Turnover (episode): 27.83%
   Turnover (step): mean=27.834% | p95=39.850% | max=54.257%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.638%
   Raw/Executed turnover: raw_mean=50.607% | executed/raw=0.550

[RAND] Run 8/16 (Seed=21182):
   Start Date: 2024-04-08 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: -4.02%
   Annualized Return: -4.02%
   Sharpe: -0.5368
   Volatility (Ann.): 10.37%
   Max DD: 10.99%
   Turnover (episode): 27.28%
   Turnover (step): mean=27.281% | p95=39.084% | max=51.215%
   Turnover vs target: target=35.000% | exceed_rate=15.9% | mean_excess=0.598%
   Raw/Executed turnover: raw_mean=49.602% | executed/raw=0.550

[RAND] Run 9/16 (Seed=21183):
   Start Date: 2024-07-11 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +8.60%
   Annualized Return: +8.60%
   Sharpe: 0.6057
   Volatility (Ann.): 11.49%
   Max DD: 11.01%
   Turnover (episode): 27.73%
   Turnover (step): mean=27.731% | p95=40.388% | max=49.020%
   Turnover vs target: target=35.000% | exceed_rate=15.5% | mean_excess=0.687%
   Raw/Executed turnover: raw_mean=50.421% | executed/raw=0.550

[RAND] Run 10/16 (Seed=21184):
   Start Date: 2024-03-26 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +4.74%
   Annualized Return: +4.74%
   Sharpe: 0.3120
   Volatility (Ann.): 10.22%
   Max DD: 6.79%
   Turnover (episode): 27.12%
   Turnover (step): mean=27.117% | p95=41.337% | max=48.774%
   Turnover vs target: target=35.000% | exceed_rate=14.3% | mean_excess=0.745%
   Raw/Executed turnover: raw_mean=49.303% | executed/raw=0.550

[RAND] Run 11/16 (Seed=21185):
   Start Date: 2024-03-22 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +9.73%
   Annualized Return: +9.73%
   Sharpe: 0.8353
   Volatility (Ann.): 9.31%
   Max DD: 5.31%
   Turnover (episode): 27.01%
   Turnover (step): mean=27.009% | p95=38.521% | max=49.329%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.463%
   Raw/Executed turnover: raw_mean=49.107% | executed/raw=0.550

[RAND] Run 12/16 (Seed=21186):
   Start Date: 2024-05-03 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +4.19%
   Annualized Return: +4.19%
   Sharpe: 0.2357
   Volatility (Ann.): 12.26%
   Max DD: 9.33%
   Turnover (episode): 27.91%
   Turnover (step): mean=27.907% | p95=41.429% | max=56.564%
   Turnover vs target: target=35.000% | exceed_rate=15.1% | mean_excess=0.900%
   Raw/Executed turnover: raw_mean=50.741% | executed/raw=0.550

[RAND] Run 13/16 (Seed=21187):
   Start Date: 2024-06-06 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +2.87%
   Annualized Return: +2.87%
   Sharpe: 0.1315
   Volatility (Ann.): 11.83%
   Max DD: 10.99%
   Turnover (episode): 28.18%
   Turnover (step): mean=28.183% | p95=40.310% | max=47.822%
   Turnover vs target: target=35.000% | exceed_rate=17.5% | mean_excess=0.724%
   Raw/Executed turnover: raw_mean=51.241% | executed/raw=0.550

[RAND] Run 14/16 (Seed=21188):
   Start Date: 2024-03-19 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +10.70%
   Annualized Return: +10.70%
   Sharpe: 0.8960
   Volatility (Ann.): 9.70%
   Max DD: 4.25%
   Turnover (episode): 27.30%
   Turnover (step): mean=27.297% | p95=40.292% | max=50.478%
   Turnover vs target: target=35.000% | exceed_rate=15.5% | mean_excess=0.738%
   Raw/Executed turnover: raw_mean=49.631% | executed/raw=0.550

[RAND] Run 15/16 (Seed=21189):
   Start Date: 2024-08-26 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +3.92%
   Annualized Return: +3.92%
   Sharpe: 0.2232
   Volatility (Ann.): 11.21%
   Max DD: 12.43%
   Turnover (episode): 27.21%
   Turnover (step): mean=27.205% | p95=39.232% | max=51.725%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.515%
   Raw/Executed turnover: raw_mean=49.464% | executed/raw=0.550

[RAND] Run 16/16 (Seed=21190):
   Start Date: 2024-04-01 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +1.36%
   Annualized Return: +1.36%
   Sharpe: -0.0171
   Volatility (Ann.): 9.60%
   Max DD: 6.22%
   Turnover (episode): 27.16%
   Turnover (step): mean=27.162% | p95=39.002% | max=48.604%
   Turnover vs target: target=35.000% | exceed_rate=14.7% | mean_excess=0.567%
   Raw/Executed turnover: raw_mean=49.385% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +4.97%
   Std:  4.04%
   Min:  -4.02%
   Max:  +10.70%

Annualized Return (%):
   Mean: +4.97%
   Std:  4.04%
   Min:  -4.02%
   Max:  +10.70%

Sharpe Ratio (annualized):
   Mean: 0.3132
   Std:  0.3729
   Min:  -0.5368
   Max:  0.8960

Volatility (Ann. %):
   Mean: +11.21%
   Std:  1.04%
   Min:  +9.31%
   Max:  +12.35%

Max Drawdown (%):
   Mean: 9.22%
   Std:  2.40%
   Min:  4.25%
   Max:  12.43%

Turnover (%):
   Mean: 27.44%
   Std:  0.40%

Turnover Step Detail (%):
   Mean(step mean): 27.442%
   Mean(step p95):  39.798%
   Mean(step max):  51.115%
   Mean exceed rate: 14.7%
   Mean excess over target: 0.642%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_050214.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2024-05-01
   Market Regime: Continued Growth (2024)
   Episode Length: 334 days (1.33 years)
   Final Portfolio Value: $125,616.47
   Total Return: +25.62%
   Annualized Return: +18.78%
   Sharpe Ratio: 1.5086 (annualized)
   Sortino Ratio: 2.2473 (annualized)
   Max Drawdown: 7.98%
   Volatility (Ann.): 10.49%
   Turnover: 3.12%
   Win Rate: 58.56%
   Diagnostics: action_uniques=334, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=21231):
   Start Date: 2024-05-23 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.68%
   Annualized Return: +6.68%
   Sharpe: 0.4716
   Volatility (Ann.): 10.79%
   Max DD: 9.70%
   Turnover (episode): 27.45%
   Turnover (step): mean=27.452% | p95=38.880% | max=52.956%
   Turnover vs target: target=35.000% | exceed_rate=12.7% | mean_excess=0.603%
   Raw/Executed turnover: raw_mean=49.914% | executed/raw=0.550

[RAND] Run 2/16 (Seed=21232):
   Start Date: 2024-08-14 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +15.27%
   Annualized Return: +15.27%
   Sharpe: 1.1002
   Volatility (Ann.): 11.80%
   Max DD: 8.76%
   Turnover (episode): 27.57%
   Turnover (step): mean=27.573% | p95=39.071% | max=48.442%
   Turnover vs target: target=35.000% | exceed_rate=15.1% | mean_excess=0.618%
   Raw/Executed turnover: raw_mean=50.132% | executed/raw=0.550

[RAND] Run 3/16 (Seed=21233):
   Start Date: 2024-05-14 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +9.71%
   Annualized Return: +9.71%
   Sharpe: 0.6742
   Volatility (Ann.): 11.90%
   Max DD: 9.53%
   Turnover (episode): 27.14%
   Turnover (step): mean=27.138% | p95=39.634% | max=47.200%
   Turnover vs target: target=35.000% | exceed_rate=13.1% | mean_excess=0.538%
   Raw/Executed turnover: raw_mean=49.341% | executed/raw=0.550

[RAND] Run 4/16 (Seed=21234):
   Start Date: 2024-06-10 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +0.43%
   Annualized Return: +0.43%
   Sharpe: -0.0795
   Volatility (Ann.): 11.38%
   Max DD: 11.05%
   Turnover (episode): 27.72%
   Turnover (step): mean=27.721% | p95=40.387% | max=52.263%
   Turnover vs target: target=35.000% | exceed_rate=18.3% | mean_excess=0.737%
   Raw/Executed turnover: raw_mean=50.401% | executed/raw=0.550

[RAND] Run 5/16 (Seed=21235):
   Start Date: 2024-08-12 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +16.33%
   Annualized Return: +16.33%
   Sharpe: 1.2238
   Volatility (Ann.): 11.32%
   Max DD: 8.66%
   Turnover (episode): 28.06%
   Turnover (step): mean=28.063% | p95=38.838% | max=55.637%
   Turnover vs target: target=35.000% | exceed_rate=15.9% | mean_excess=0.604%
   Raw/Executed turnover: raw_mean=51.024% | executed/raw=0.550

[RAND] Run 6/16 (Seed=21236):
   Start Date: 2024-05-02 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +15.86%
   Annualized Return: +15.86%
   Sharpe: 1.1819
   Volatility (Ann.): 11.37%
   Max DD: 6.10%
   Turnover (episode): 27.15%
   Turnover (step): mean=27.151% | p95=40.020% | max=52.256%
   Turnover vs target: target=35.000% | exceed_rate=16.3% | mean_excess=0.752%
   Raw/Executed turnover: raw_mean=49.366% | executed/raw=0.550

[RAND] Run 7/16 (Seed=21237):
   Start Date: 2024-06-13 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +5.21%
   Annualized Return: +5.21%
   Sharpe: 0.3267
   Volatility (Ann.): 11.60%
   Max DD: 10.52%
   Turnover (episode): 26.29%
   Turnover (step): mean=26.294% | p95=38.428% | max=51.005%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.468%
   Raw/Executed turnover: raw_mean=47.807% | executed/raw=0.550

[RAND] Run 8/16 (Seed=21238):
   Start Date: 2024-08-14 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +13.24%
   Annualized Return: +13.24%
   Sharpe: 0.9495
   Volatility (Ann.): 11.79%
   Max DD: 10.45%
   Turnover (episode): 26.67%
   Turnover (step): mean=26.666% | p95=37.077% | max=50.141%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.367%
   Raw/Executed turnover: raw_mean=48.484% | executed/raw=0.550

[RAND] Run 9/16 (Seed=21239):
   Start Date: 2024-08-20 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +11.52%
   Annualized Return: +11.52%
   Sharpe: 0.8023
   Volatility (Ann.): 12.09%
   Max DD: 8.50%
   Turnover (episode): 28.43%
   Turnover (step): mean=28.435% | p95=38.827% | max=47.160%
   Turnover vs target: target=35.000% | exceed_rate=16.3% | mean_excess=0.586%
   Raw/Executed turnover: raw_mean=51.699% | executed/raw=0.550

[RAND] Run 10/16 (Seed=21240):
   Start Date: 2024-05-02 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +10.32%
   Annualized Return: +10.32%
   Sharpe: 0.7042
   Volatility (Ann.): 12.24%
   Max DD: 10.82%
   Turnover (episode): 27.76%
   Turnover (step): mean=27.756% | p95=39.714% | max=51.209%
   Turnover vs target: target=35.000% | exceed_rate=16.7% | mean_excess=0.694%
   Raw/Executed turnover: raw_mean=50.465% | executed/raw=0.550

[RAND] Run 11/16 (Seed=21241):
   Start Date: 2024-05-10 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +0.47%
   Annualized Return: +0.47%
   Sharpe: -0.0653
   Volatility (Ann.): 12.04%
   Max DD: 11.26%
   Turnover (episode): 27.39%
   Turnover (step): mean=27.386% | p95=41.124% | max=48.279%
   Turnover vs target: target=35.000% | exceed_rate=17.1% | mean_excess=0.803%
   Raw/Executed turnover: raw_mean=49.792% | executed/raw=0.550

[RAND] Run 12/16 (Seed=21242):
   Start Date: 2024-08-02 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +14.46%
   Annualized Return: +14.46%
   Sharpe: 1.0676
   Volatility (Ann.): 11.46%
   Max DD: 8.25%
   Turnover (episode): 27.82%
   Turnover (step): mean=27.817% | p95=39.988% | max=53.458%
   Turnover vs target: target=35.000% | exceed_rate=15.5% | mean_excess=0.678%
   Raw/Executed turnover: raw_mean=50.577% | executed/raw=0.550

[RAND] Run 13/16 (Seed=21243):
   Start Date: 2024-05-09 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.36%
   Annualized Return: +6.36%
   Sharpe: 0.4178
   Volatility (Ann.): 11.70%
   Max DD: 9.66%
   Turnover (episode): 27.31%
   Turnover (step): mean=27.306% | p95=39.784% | max=48.914%
   Turnover vs target: target=35.000% | exceed_rate=17.1% | mean_excess=0.623%
   Raw/Executed turnover: raw_mean=49.647% | executed/raw=0.550

[RAND] Run 14/16 (Seed=21244):
   Start Date: 2024-05-08 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +0.43%
   Annualized Return: +0.43%
   Sharpe: -0.0772
   Volatility (Ann.): 11.54%
   Max DD: 11.81%
   Turnover (episode): 27.36%
   Turnover (step): mean=27.357% | p95=40.346% | max=52.970%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.706%
   Raw/Executed turnover: raw_mean=49.740% | executed/raw=0.550

[RAND] Run 15/16 (Seed=21245):
   Start Date: 2024-05-07 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +9.39%
   Annualized Return: +9.39%
   Sharpe: 0.6487
   Volatility (Ann.): 11.92%
   Max DD: 7.00%
   Turnover (episode): 27.76%
   Turnover (step): mean=27.756% | p95=39.457% | max=47.310%
   Turnover vs target: target=35.000% | exceed_rate=14.7% | mean_excess=0.594%
   Raw/Executed turnover: raw_mean=50.466% | executed/raw=0.550

[RAND] Run 16/16 (Seed=21246):
   Start Date: 2024-06-18 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.53%
   Annualized Return: +6.53%
   Sharpe: 0.4467
   Volatility (Ann.): 11.18%
   Max DD: 7.55%
   Turnover (episode): 28.22%
   Turnover (step): mean=28.224% | p95=39.540% | max=53.680%
   Turnover vs target: target=35.000% | exceed_rate=16.7% | mean_excess=0.730%
   Raw/Executed turnover: raw_mean=51.316% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +8.89%
   Std:  5.47%
   Min:  +0.43%
   Max:  +16.33%

Annualized Return (%):
   Mean: +8.89%
   Std:  5.47%
   Min:  +0.43%
   Max:  +16.33%

Sharpe Ratio (annualized):
   Mean: 0.6121
   Std:  0.4387
   Min:  -0.0795
   Max:  1.2238

Volatility (Ann. %):
   Mean: +11.63%
   Std:  0.38%
   Min:  +10.79%
   Max:  +12.24%

Max Drawdown (%):
   Mean: 9.35%
   Std:  1.63%
   Min:  6.10%
   Max:  11.81%

Turnover (%):
   Mean: 27.51%
   Std:  0.55%

Turnover Step Detail (%):
   Mean(step mean): 27.506%
   Mean(step p95):  39.445%
   Mean(step max):  50.805%
   Mean exceed rate: 15.0%
   Mean excess over target: 0.631%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_052845.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2024-07-22
   Market Regime: Continued Growth (2024)
   Episode Length: 279 days (1.11 years)
   Final Portfolio Value: $119,169.60
   Total Return: +19.17%
   Annualized Return: +17.16%
   Sharpe Ratio: 1.3053 (annualized)
   Sortino Ratio: 1.9143 (annualized)
   Max Drawdown: 7.98%
   Volatility (Ann.): 11.14%
   Turnover: 3.14%
   Win Rate: 57.91%
   Diagnostics: action_uniques=279, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=21286):
   Start Date: 2024-07-23 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +7.75%
   Annualized Return: +7.75%
   Sharpe: 0.5195
   Volatility (Ann.): 11.98%
   Max DD: 12.35%
   Turnover (episode): 27.52%
   Turnover (step): mean=27.520% | p95=40.631% | max=59.102%
   Turnover vs target: target=35.000% | exceed_rate=14.7% | mean_excess=0.762%
   Raw/Executed turnover: raw_mean=50.036% | executed/raw=0.550

[RAND] Run 2/16 (Seed=21287):
   Start Date: 2024-08-27 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +10.02%
   Annualized Return: +10.02%
   Sharpe: 0.7423
   Volatility (Ann.): 11.07%
   Max DD: 9.44%
   Turnover (episode): 27.48%
   Turnover (step): mean=27.476% | p95=39.691% | max=50.354%
   Turnover vs target: target=35.000% | exceed_rate=14.3% | mean_excess=0.640%
   Raw/Executed turnover: raw_mean=49.956% | executed/raw=0.550

[RAND] Run 3/16 (Seed=21288):
   Start Date: 2024-07-23 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +5.53%
   Annualized Return: +5.53%
   Sharpe: 0.3552
   Volatility (Ann.): 11.49%
   Max DD: 10.13%
   Turnover (episode): 27.19%
   Turnover (step): mean=27.195% | p95=38.035% | max=48.799%
   Turnover vs target: target=35.000% | exceed_rate=13.1% | mean_excess=0.488%
   Raw/Executed turnover: raw_mean=49.445% | executed/raw=0.550

[RAND] Run 4/16 (Seed=21289):
   Start Date: 2024-08-06 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +18.03%
   Annualized Return: +18.03%
   Sharpe: 1.2937
   Volatility (Ann.): 11.88%
   Max DD: 7.88%
   Turnover (episode): 27.99%
   Turnover (step): mean=27.988% | p95=39.414% | max=51.219%
   Turnover vs target: target=35.000% | exceed_rate=15.1% | mean_excess=0.782%
   Raw/Executed turnover: raw_mean=50.888% | executed/raw=0.550

[RAND] Run 5/16 (Seed=21290):
   Start Date: 2024-08-05 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +13.53%
   Annualized Return: +13.53%
   Sharpe: 0.9391
   Volatility (Ann.): 12.26%
   Max DD: 11.11%
   Turnover (episode): 27.25%
   Turnover (step): mean=27.249% | p95=39.143% | max=51.112%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.536%
   Raw/Executed turnover: raw_mean=49.543% | executed/raw=0.550

[RAND] Run 6/16 (Seed=21291):
   Start Date: 2024-07-23 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +10.54%
   Annualized Return: +10.54%
   Sharpe: 0.7680
   Volatility (Ann.): 11.35%
   Max DD: 9.20%
   Turnover (episode): 26.73%
   Turnover (step): mean=26.733% | p95=37.323% | max=48.958%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.304%
   Raw/Executed turnover: raw_mean=48.605% | executed/raw=0.550

[RAND] Run 7/16 (Seed=21292):
   Start Date: 2024-07-31 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +5.10%
   Annualized Return: +5.10%
   Sharpe: 0.3126
   Volatility (Ann.): 11.88%
   Max DD: 11.24%
   Turnover (episode): 27.41%
   Turnover (step): mean=27.412% | p95=39.287% | max=52.324%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.556%
   Raw/Executed turnover: raw_mean=49.841% | executed/raw=0.550

[RAND] Run 8/16 (Seed=21293):
   Start Date: 2024-08-28 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +9.13%
   Annualized Return: +9.13%
   Sharpe: 0.6618
   Volatility (Ann.): 11.21%
   Max DD: 9.44%
   Turnover (episode): 27.76%
   Turnover (step): mean=27.760% | p95=38.678% | max=48.427%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.479%
   Raw/Executed turnover: raw_mean=50.472% | executed/raw=0.550

[RAND] Run 9/16 (Seed=21294):
   Start Date: 2024-08-07 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +21.28%
   Annualized Return: +21.28%
   Sharpe: 1.5875
   Volatility (Ann.): 11.36%
   Max DD: 7.31%
   Turnover (episode): 27.14%
   Turnover (step): mean=27.136% | p95=40.211% | max=47.840%
   Turnover vs target: target=35.000% | exceed_rate=13.1% | mean_excess=0.577%
   Raw/Executed turnover: raw_mean=49.339% | executed/raw=0.550

[RAND] Run 10/16 (Seed=21295):
   Start Date: 2024-08-01 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +6.68%
   Annualized Return: +6.68%
   Sharpe: 0.4236
   Volatility (Ann.): 12.48%
   Max DD: 11.69%
   Turnover (episode): 27.09%
   Turnover (step): mean=27.093% | p95=37.276% | max=51.289%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.384%
   Raw/Executed turnover: raw_mean=49.260% | executed/raw=0.550

[RAND] Run 11/16 (Seed=21296):
   Start Date: 2024-07-24 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +8.57%
   Annualized Return: +8.57%
   Sharpe: 0.5769
   Volatility (Ann.): 12.15%
   Max DD: 12.02%
   Turnover (episode): 27.23%
   Turnover (step): mean=27.235% | p95=38.411% | max=47.266%
   Turnover vs target: target=35.000% | exceed_rate=14.3% | mean_excess=0.498%
   Raw/Executed turnover: raw_mean=49.517% | executed/raw=0.550

[RAND] Run 12/16 (Seed=21297):
   Start Date: 2024-07-24 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +13.91%
   Annualized Return: +13.91%
   Sharpe: 1.0329
   Volatility (Ann.): 11.36%
   Max DD: 7.61%
   Turnover (episode): 28.07%
   Turnover (step): mean=28.070% | p95=39.357% | max=49.230%
   Turnover vs target: target=35.000% | exceed_rate=17.9% | mean_excess=0.707%
   Raw/Executed turnover: raw_mean=51.036% | executed/raw=0.550

[RAND] Run 13/16 (Seed=21298):
   Start Date: 2024-08-23 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +9.87%
   Annualized Return: +9.87%
   Sharpe: 0.7248
   Volatility (Ann.): 11.17%
   Max DD: 10.17%
   Turnover (episode): 27.70%
   Turnover (step): mean=27.700% | p95=39.620% | max=51.856%
   Turnover vs target: target=35.000% | exceed_rate=17.5% | mean_excess=0.715%
   Raw/Executed turnover: raw_mean=50.364% | executed/raw=0.550

[RAND] Run 14/16 (Seed=21299):
   Start Date: 2024-07-24 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +9.16%
   Annualized Return: +9.16%
   Sharpe: 0.6455
   Volatility (Ann.): 11.61%
   Max DD: 8.50%
   Turnover (episode): 27.59%
   Turnover (step): mean=27.590% | p95=39.128% | max=54.140%
   Turnover vs target: target=35.000% | exceed_rate=13.5% | mean_excess=0.569%
   Raw/Executed turnover: raw_mean=50.164% | executed/raw=0.550

[RAND] Run 15/16 (Seed=21300):
   Start Date: 2024-07-24 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +8.50%
   Annualized Return: +8.50%
   Sharpe: 0.5789
   Volatility (Ann.): 11.96%
   Max DD: 10.29%
   Turnover (episode): 27.33%
   Turnover (step): mean=27.326% | p95=39.403% | max=59.952%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.636%
   Raw/Executed turnover: raw_mean=49.684% | executed/raw=0.550

[RAND] Run 16/16 (Seed=21301):
   Start Date: 2024-08-15 | Regime: Continued Growth (2024)
   Days Traded: 252 (1.00 years)
   Total Return: +16.31%
   Annualized Return: +16.31%
   Sharpe: 1.1567
   Volatility (Ann.): 12.03%
   Max DD: 8.17%
   Turnover (episode): 27.44%
   Turnover (step): mean=27.440% | p95=39.500% | max=47.253%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.513%
   Raw/Executed turnover: raw_mean=49.891% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +10.87%
   Std:  4.57%
   Min:  +5.10%
   Max:  +21.28%

Annualized Return (%):
   Mean: +10.87%
   Std:  4.57%
   Min:  +5.10%
   Max:  +21.28%

Sharpe Ratio (annualized):
   Mean: 0.7699
   Std:  0.3519
   Min:  0.3126
   Max:  1.5875

Volatility (Ann. %):
   Mean: +11.70%
   Std:  0.43%
   Min:  +11.07%
   Max:  +12.48%

Max Drawdown (%):
   Mean: 9.78%
   Std:  1.61%
   Min:  7.31%
   Max:  12.35%

Turnover (%):
   Mean: 27.43%
   Std:  0.34%

Turnover Step Detail (%):
   Mean(step mean): 27.433%
   Mean(step p95):  39.069%
   Mean(step max):  51.195%
   Mean exceed rate: 13.4%
   Mean excess over target: 0.572%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_055500.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs

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
   Start Date: 2020-03-31
   Market Regime: COVID Crash (2020 Q1)
   Episode Length: 756 days (3.00 years)
   Final Portfolio Value: $208,419.35
   Total Return: +108.42%
   Annualized Return: +27.74%
   Sharpe Ratio: 1.2515 (annualized)
   Sortino Ratio: 1.8323 (annualized)
   Max Drawdown: 24.06%
   Volatility (Ann.): 19.54%
   Turnover: 3.66%
   Win Rate: 55.50%
   Diagnostics: action_uniques=756, alpha<=1 frac=0.000, argmax_alpha_uniques=8

================================================================================
STOCHASTIC EVALUATIONS (Random Start = True, 16 Runs)
================================================================================

[RAND] Run 1/16 (Seed=30203):
   Start Date: 2020-07-13 | Regime: COVID Recovery (2020 Q2-Q4)
   Days Traded: 252 (1.00 years)
   Total Return: +37.20%
   Annualized Return: +37.20%
   Sharpe: 1.9479
   Volatility (Ann.): 15.94%
   Max DD: 9.31%
   Turnover (episode): 25.57%
   Turnover (step): mean=25.573% | p95=36.361% | max=47.323%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.338%
   Raw/Executed turnover: raw_mean=46.496% | executed/raw=0.550

[RAND] Run 2/16 (Seed=30204):
   Start Date: 2021-11-23 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -20.04%
   Annualized Return: -20.04%
   Sharpe: -1.1121
   Volatility (Ann.): 20.14%
   Max DD: 26.85%
   Turnover (episode): 26.33%
   Turnover (step): mean=26.332% | p95=38.989% | max=47.221%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.450%
   Raw/Executed turnover: raw_mean=47.876% | executed/raw=0.550