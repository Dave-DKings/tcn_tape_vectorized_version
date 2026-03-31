fixed_252_year: completed=0 pending_now=15
[RUN] fixed_252_year -> year_001 | bucket=2020 | start=2020-01-02 | h=252

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
   Market Regime: Pre-COVID (through 2020-02)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $130,383.44
   Total Return: +30.38%
   Annualized Return: +30.38%
   Sharpe Ratio: 0.9264 (annualized)
   Sortino Ratio: 1.2862 (annualized)
   Max Drawdown: 29.15%
   Volatility (Ann.): 32.27%
   Turnover: 3.29%
   Win Rate: 60.16%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=3

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=25342):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +18.84%
   Annualized Return: +18.84%
   Sharpe: 0.6479
   Volatility (Ann.): 31.26%
   Max DD: 29.26%
   Turnover (episode): 25.73%
   Turnover (step): mean=25.731% | p95=36.762% | max=44.062%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.259%
   Raw/Executed turnover: raw_mean=46.784% | executed/raw=0.550

[RAND] Run 2/32 (Seed=25343):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +29.32%
   Annualized Return: +29.32%
   Sharpe: 0.9179
   Volatility (Ann.): 31.34%
   Max DD: 28.03%
   Turnover (episode): 25.21%
   Turnover (step): mean=25.207% | p95=36.161% | max=50.153%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.242%
   Raw/Executed turnover: raw_mean=45.831% | executed/raw=0.550

[RAND] Run 3/32 (Seed=25344):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +25.13%
   Annualized Return: +25.13%
   Sharpe: 0.8143
   Volatility (Ann.): 31.23%
   Max DD: 27.23%
   Turnover (episode): 24.89%
   Turnover (step): mean=24.895% | p95=35.309% | max=41.175%
   Turnover vs target: target=35.000% | exceed_rate=6.0% | mean_excess=0.163%
   Raw/Executed turnover: raw_mean=45.263% | executed/raw=0.550

[RAND] Run 4/32 (Seed=25345):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +20.92%
   Annualized Return: +20.92%
   Sharpe: 0.7037
   Volatility (Ann.): 31.27%
   Max DD: 29.90%
   Turnover (episode): 26.08%
   Turnover (step): mean=26.076% | p95=37.885% | max=44.401%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.304%
   Raw/Executed turnover: raw_mean=47.410% | executed/raw=0.550

[RAND] Run 5/32 (Seed=25346):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +26.27%
   Annualized Return: +26.27%
   Sharpe: 0.8483
   Volatility (Ann.): 30.92%
   Max DD: 26.91%
   Turnover (episode): 25.53%
   Turnover (step): mean=25.532% | p95=37.107% | max=46.351%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.260%
   Raw/Executed turnover: raw_mean=46.422% | executed/raw=0.550

[RAND] Run 6/32 (Seed=25347):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +16.39%
   Annualized Return: +16.39%
   Sharpe: 0.5828
   Volatility (Ann.): 31.12%
   Max DD: 29.66%
   Turnover (episode): 24.93%
   Turnover (step): mean=24.928% | p95=35.515% | max=45.302%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.223%
   Raw/Executed turnover: raw_mean=45.323% | executed/raw=0.550

[RAND] Run 7/32 (Seed=25348):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +18.52%
   Annualized Return: +18.52%
   Sharpe: 0.6392
   Volatility (Ann.): 31.28%
   Max DD: 29.92%
   Turnover (episode): 26.01%
   Turnover (step): mean=26.006% | p95=36.971% | max=42.319%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.325%
   Raw/Executed turnover: raw_mean=47.284% | executed/raw=0.550

[RAND] Run 8/32 (Seed=25349):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +20.70%
   Annualized Return: +20.70%
   Sharpe: 0.6941
   Volatility (Ann.): 31.59%
   Max DD: 30.19%
   Turnover (episode): 25.54%
   Turnover (step): mean=25.543% | p95=36.797% | max=47.573%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.351%
   Raw/Executed turnover: raw_mean=46.441% | executed/raw=0.550

[RAND] Run 9/32 (Seed=25350):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +19.12%
   Annualized Return: +19.12%
   Sharpe: 0.6591
   Volatility (Ann.): 30.96%
   Max DD: 28.50%
   Turnover (episode): 25.28%
   Turnover (step): mean=25.278% | p95=34.981% | max=39.342%
   Turnover vs target: target=35.000% | exceed_rate=5.2% | mean_excess=0.121%
   Raw/Executed turnover: raw_mean=45.960% | executed/raw=0.550

[RAND] Run 10/32 (Seed=25351):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +24.11%
   Annualized Return: +24.11%
   Sharpe: 0.7805
   Volatility (Ann.): 31.75%
   Max DD: 29.66%
   Turnover (episode): 25.31%
   Turnover (step): mean=25.313% | p95=36.633% | max=44.230%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.224%
   Raw/Executed turnover: raw_mean=46.024% | executed/raw=0.550

[RAND] Run 11/32 (Seed=25352):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +24.27%
   Annualized Return: +24.27%
   Sharpe: 0.7840
   Volatility (Ann.): 31.72%
   Max DD: 28.09%
   Turnover (episode): 25.84%
   Turnover (step): mean=25.840% | p95=36.427% | max=45.358%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.298%
   Raw/Executed turnover: raw_mean=46.983% | executed/raw=0.550

[RAND] Run 12/32 (Seed=25353):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +22.14%
   Annualized Return: +22.14%
   Sharpe: 0.7522
   Volatility (Ann.): 30.12%
   Max DD: 28.24%
   Turnover (episode): 24.55%
   Turnover (step): mean=24.549% | p95=35.342% | max=43.381%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.155%
   Raw/Executed turnover: raw_mean=44.634% | executed/raw=0.550

[RAND] Run 13/32 (Seed=25354):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +21.39%
   Annualized Return: +21.39%
   Sharpe: 0.7141
   Volatility (Ann.): 31.41%
   Max DD: 30.21%
   Turnover (episode): 24.61%
   Turnover (step): mean=24.606% | p95=33.737% | max=45.249%
   Turnover vs target: target=35.000% | exceed_rate=4.4% | mean_excess=0.158%
   Raw/Executed turnover: raw_mean=44.738% | executed/raw=0.550

[RAND] Run 14/32 (Seed=25355):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +19.56%
   Annualized Return: +19.56%
   Sharpe: 0.6644
   Volatility (Ann.): 31.54%
   Max DD: 30.57%
   Turnover (episode): 24.73%
   Turnover (step): mean=24.734% | p95=34.624% | max=46.967%
   Turnover vs target: target=35.000% | exceed_rate=4.0% | mean_excess=0.157%
   Raw/Executed turnover: raw_mean=44.970% | executed/raw=0.550

[RAND] Run 15/32 (Seed=25356):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +24.59%
   Annualized Return: +24.59%
   Sharpe: 0.7979
   Volatility (Ann.): 31.37%
   Max DD: 29.01%
   Turnover (episode): 25.24%
   Turnover (step): mean=25.236% | p95=35.281% | max=44.288%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.148%
   Raw/Executed turnover: raw_mean=45.883% | executed/raw=0.550

[RAND] Run 16/32 (Seed=25357):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +20.63%
   Annualized Return: +20.63%
   Sharpe: 0.6938
   Volatility (Ann.): 31.46%
   Max DD: 29.60%
   Turnover (episode): 25.36%
   Turnover (step): mean=25.355% | p95=36.760% | max=46.982%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.298%
   Raw/Executed turnover: raw_mean=46.101% | executed/raw=0.550

[RAND] Run 17/32 (Seed=25358):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +18.70%
   Annualized Return: +18.70%
   Sharpe: 0.6447
   Volatility (Ann.): 31.23%
   Max DD: 29.05%
   Turnover (episode): 24.65%
   Turnover (step): mean=24.647% | p95=35.864% | max=47.847%
   Turnover vs target: target=35.000% | exceed_rate=5.6% | mean_excess=0.188%
   Raw/Executed turnover: raw_mean=44.813% | executed/raw=0.550

[RAND] Run 18/32 (Seed=25359):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +24.29%
   Annualized Return: +24.29%
   Sharpe: 0.7962
   Volatility (Ann.): 30.97%
   Max DD: 26.86%
   Turnover (episode): 25.15%
   Turnover (step): mean=25.155% | p95=38.141% | max=47.798%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.376%
   Raw/Executed turnover: raw_mean=45.736% | executed/raw=0.550

[RAND] Run 19/32 (Seed=25360):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +24.63%
   Annualized Return: +24.63%
   Sharpe: 0.7912
   Volatility (Ann.): 31.91%
   Max DD: 29.62%
   Turnover (episode): 25.10%
   Turnover (step): mean=25.098% | p95=36.710% | max=45.913%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.259%
   Raw/Executed turnover: raw_mean=45.633% | executed/raw=0.550

[RAND] Run 20/32 (Seed=25361):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +21.50%
   Annualized Return: +21.50%
   Sharpe: 0.7167
   Volatility (Ann.): 31.45%
   Max DD: 29.32%
   Turnover (episode): 24.71%
   Turnover (step): mean=24.709% | p95=34.837% | max=45.754%
   Turnover vs target: target=35.000% | exceed_rate=5.2% | mean_excess=0.234%
   Raw/Executed turnover: raw_mean=44.925% | executed/raw=0.550

[RAND] Run 21/32 (Seed=25362):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +19.17%
   Annualized Return: +19.17%
   Sharpe: 0.6584
   Volatility (Ann.): 31.13%
   Max DD: 28.99%
   Turnover (episode): 24.80%
   Turnover (step): mean=24.799% | p95=37.721% | max=48.116%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.333%
   Raw/Executed turnover: raw_mean=45.090% | executed/raw=0.550

[RAND] Run 22/32 (Seed=25363):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +18.24%
   Annualized Return: +18.24%
   Sharpe: 0.6231
   Volatility (Ann.): 32.14%
   Max DD: 30.80%
   Turnover (episode): 24.94%
   Turnover (step): mean=24.943% | p95=37.064% | max=43.906%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.268%
   Raw/Executed turnover: raw_mean=45.352% | executed/raw=0.550

[RAND] Run 23/32 (Seed=25364):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +22.21%
   Annualized Return: +22.21%
   Sharpe: 0.7467
   Volatility (Ann.): 30.65%
   Max DD: 29.01%
   Turnover (episode): 25.14%
   Turnover (step): mean=25.141% | p95=37.604% | max=44.261%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.357%
   Raw/Executed turnover: raw_mean=45.712% | executed/raw=0.550

[RAND] Run 24/32 (Seed=25365):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +23.02%
   Annualized Return: +23.02%
   Sharpe: 0.7587
   Volatility (Ann.): 31.27%
   Max DD: 29.33%
   Turnover (episode): 24.84%
   Turnover (step): mean=24.839% | p95=36.759% | max=44.883%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.253%
   Raw/Executed turnover: raw_mean=45.161% | executed/raw=0.550

[RAND] Run 25/32 (Seed=25366):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +22.83%
   Annualized Return: +22.83%
   Sharpe: 0.7601
   Volatility (Ann.): 30.86%
   Max DD: 28.56%
   Turnover (episode): 24.92%
   Turnover (step): mean=24.916% | p95=36.299% | max=45.464%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.194%
   Raw/Executed turnover: raw_mean=45.302% | executed/raw=0.550

[RAND] Run 26/32 (Seed=25367):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +21.90%
   Annualized Return: +21.90%
   Sharpe: 0.7250
   Volatility (Ann.): 31.63%
   Max DD: 28.33%
   Turnover (episode): 24.86%
   Turnover (step): mean=24.859% | p95=34.789% | max=40.303%
   Turnover vs target: target=35.000% | exceed_rate=5.2% | mean_excess=0.114%
   Raw/Executed turnover: raw_mean=45.198% | executed/raw=0.550

[RAND] Run 27/32 (Seed=25368):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +21.46%
   Annualized Return: +21.46%
   Sharpe: 0.7119
   Volatility (Ann.): 31.72%
   Max DD: 29.23%
   Turnover (episode): 25.90%
   Turnover (step): mean=25.900% | p95=37.331% | max=44.319%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.331%
   Raw/Executed turnover: raw_mean=47.091% | executed/raw=0.550

[RAND] Run 28/32 (Seed=25369):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +21.77%
   Annualized Return: +21.77%
   Sharpe: 0.7244
   Volatility (Ann.): 31.37%
   Max DD: 29.14%
   Turnover (episode): 25.05%
   Turnover (step): mean=25.051% | p95=36.463% | max=47.690%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.324%
   Raw/Executed turnover: raw_mean=45.548% | executed/raw=0.550

[RAND] Run 29/32 (Seed=25370):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +23.80%
   Annualized Return: +23.80%
   Sharpe: 0.7715
   Volatility (Ann.): 31.81%
   Max DD: 31.20%
   Turnover (episode): 24.84%
   Turnover (step): mean=24.836% | p95=34.570% | max=40.195%
   Turnover vs target: target=35.000% | exceed_rate=4.0% | mean_excess=0.125%
   Raw/Executed turnover: raw_mean=45.157% | executed/raw=0.550

[RAND] Run 30/32 (Seed=25371):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +19.78%
   Annualized Return: +19.78%
   Sharpe: 0.6753
   Volatility (Ann.): 31.09%
   Max DD: 28.79%
   Turnover (episode): 24.93%
   Turnover (step): mean=24.931% | p95=34.631% | max=46.056%
   Turnover vs target: target=35.000% | exceed_rate=4.8% | mean_excess=0.205%
   Raw/Executed turnover: raw_mean=45.328% | executed/raw=0.550

[RAND] Run 31/32 (Seed=25372):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +22.46%
   Annualized Return: +22.46%
   Sharpe: 0.7489
   Volatility (Ann.): 30.93%
   Max DD: 27.49%
   Turnover (episode): 24.50%
   Turnover (step): mean=24.499% | p95=34.914% | max=45.109%
   Turnover vs target: target=35.000% | exceed_rate=4.4% | mean_excess=0.152%
   Raw/Executed turnover: raw_mean=44.544% | executed/raw=0.550

[RAND] Run 32/32 (Seed=25373):
   Start Date: 2020-01-02 | Regime: Pre-COVID (through 2020-02)
   Days Traded: 252 (1.00 years)
   Total Return: +21.39%
   Annualized Return: +21.39%
   Sharpe: 0.7201
   Volatility (Ann.): 30.96%
   Max DD: 27.50%
   Turnover (episode): 24.72%
   Turnover (step): mean=24.718% | p95=36.369% | max=45.169%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.252%
   Raw/Executed turnover: raw_mean=44.943% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +21.85%
   Std:  2.70%
   Min:  +16.39%
   Max:  +29.32%

Annualized Return (%):
   Mean: +21.85%
   Std:  2.70%
   Min:  +16.39%
   Max:  +29.32%

Sharpe Ratio (annualized):
   Mean: 0.7271
   Std:  0.0709
   Min:  0.5828
   Max:  0.9179

Volatility (Ann. %):
   Mean: +31.30%
   Std:  0.40%
   Min:  +30.12%
   Max:  +32.14%

Max Drawdown (%):
   Mean: 29.01%
   Std:  1.09%
   Min:  26.86%
   Max:  31.20%

Turnover (%):
   Mean: 25.12%
   Std:  0.44%

Turnover Step Detail (%):
   Mean(step mean): 25.121%
   Mean(step p95):  36.136%
   Mean(step max):  44.997%
   Mean exceed rate: 6.9%
   Mean excess over target: 0.239%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_215414.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs
      status=ok rows=32 copied=9
[RUN] fixed_252_year -> year_002 | bucket=2020 | start=2020-07-02 | h=252

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
   Market Regime: COVID Recovery (2020-05 to 2020-12)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $147,861.04
   Total Return: +47.86%
   Annualized Return: +47.86%
   Sharpe Ratio: 2.4571 (annualized)
   Sortino Ratio: 3.6658 (annualized)
   Max Drawdown: 7.94%
   Volatility (Ann.): 15.69%
   Turnover: 3.48%
   Win Rate: 60.56%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=25468):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +37.15%
   Annualized Return: +37.15%
   Sharpe: 1.9869
   Volatility (Ann.): 15.59%
   Max DD: 8.18%
   Turnover (episode): 25.20%
   Turnover (step): mean=25.204% | p95=36.233% | max=46.657%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.353%
   Raw/Executed turnover: raw_mean=45.826% | executed/raw=0.550

[RAND] Run 2/32 (Seed=25469):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +41.08%
   Annualized Return: +41.08%
   Sharpe: 2.1850
   Volatility (Ann.): 15.46%
   Max DD: 8.99%
   Turnover (episode): 26.25%
   Turnover (step): mean=26.246% | p95=38.131% | max=44.559%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.446%
   Raw/Executed turnover: raw_mean=47.721% | executed/raw=0.550

[RAND] Run 3/32 (Seed=25470):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +35.19%
   Annualized Return: +35.19%
   Sharpe: 1.9333
   Volatility (Ann.): 15.24%
   Max DD: 8.48%
   Turnover (episode): 24.64%
   Turnover (step): mean=24.642% | p95=36.148% | max=45.662%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.268%
   Raw/Executed turnover: raw_mean=44.804% | executed/raw=0.550

[RAND] Run 4/32 (Seed=25471):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +40.08%
   Annualized Return: +40.08%
   Sharpe: 2.1333
   Volatility (Ann.): 15.51%
   Max DD: 9.43%
   Turnover (episode): 25.34%
   Turnover (step): mean=25.342% | p95=38.817% | max=50.347%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.480%
   Raw/Executed turnover: raw_mean=46.077% | executed/raw=0.550

[RAND] Run 5/32 (Seed=25472):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +37.48%
   Annualized Return: +37.48%
   Sharpe: 1.9908
   Volatility (Ann.): 15.68%
   Max DD: 8.79%
   Turnover (episode): 25.02%
   Turnover (step): mean=25.025% | p95=35.769% | max=48.603%
   Turnover vs target: target=35.000% | exceed_rate=6.0% | mean_excess=0.259%
   Raw/Executed turnover: raw_mean=45.500% | executed/raw=0.550

[RAND] Run 6/32 (Seed=25473):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +35.21%
   Annualized Return: +35.21%
   Sharpe: 1.9023
   Volatility (Ann.): 15.52%
   Max DD: 8.07%
   Turnover (episode): 25.98%
   Turnover (step): mean=25.975% | p95=37.608% | max=46.039%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.362%
   Raw/Executed turnover: raw_mean=47.228% | executed/raw=0.550

[RAND] Run 7/32 (Seed=25474):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +34.81%
   Annualized Return: +34.81%
   Sharpe: 1.8752
   Volatility (Ann.): 15.59%
   Max DD: 8.07%
   Turnover (episode): 25.84%
   Turnover (step): mean=25.836% | p95=37.365% | max=47.648%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.342%
   Raw/Executed turnover: raw_mean=46.974% | executed/raw=0.550

[RAND] Run 8/32 (Seed=25475):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +42.31%
   Annualized Return: +42.31%
   Sharpe: 2.2302
   Volatility (Ann.): 15.55%
   Max DD: 8.43%
   Turnover (episode): 25.85%
   Turnover (step): mean=25.855% | p95=35.418% | max=42.249%
   Turnover vs target: target=35.000% | exceed_rate=6.0% | mean_excess=0.199%
   Raw/Executed turnover: raw_mean=47.008% | executed/raw=0.550

[RAND] Run 9/32 (Seed=25476):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +42.63%
   Annualized Return: +42.63%
   Sharpe: 2.2309
   Volatility (Ann.): 15.65%
   Max DD: 8.72%
   Turnover (episode): 25.99%
   Turnover (step): mean=25.991% | p95=36.515% | max=42.344%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.275%
   Raw/Executed turnover: raw_mean=47.256% | executed/raw=0.550

[RAND] Run 10/32 (Seed=25477):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +37.74%
   Annualized Return: +37.74%
   Sharpe: 2.0163
   Volatility (Ann.): 15.57%
   Max DD: 9.03%
   Turnover (episode): 25.65%
   Turnover (step): mean=25.648% | p95=36.218% | max=48.808%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.339%
   Raw/Executed turnover: raw_mean=46.633% | executed/raw=0.550

[RAND] Run 11/32 (Seed=25478):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +42.26%
   Annualized Return: +42.26%
   Sharpe: 2.1933
   Volatility (Ann.): 15.81%
   Max DD: 8.59%
   Turnover (episode): 25.17%
   Turnover (step): mean=25.174% | p95=36.231% | max=40.312%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.185%
   Raw/Executed turnover: raw_mean=45.771% | executed/raw=0.550

[RAND] Run 12/32 (Seed=25479):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +33.38%
   Annualized Return: +33.38%
   Sharpe: 1.8021
   Volatility (Ann.): 15.63%
   Max DD: 9.09%
   Turnover (episode): 25.08%
   Turnover (step): mean=25.081% | p95=35.275% | max=42.762%
   Turnover vs target: target=35.000% | exceed_rate=5.6% | mean_excess=0.198%
   Raw/Executed turnover: raw_mean=45.603% | executed/raw=0.550

[RAND] Run 13/32 (Seed=25480):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +39.37%
   Annualized Return: +39.37%
   Sharpe: 2.1212
   Volatility (Ann.): 15.34%
   Max DD: 7.58%
   Turnover (episode): 24.99%
   Turnover (step): mean=24.993% | p95=35.661% | max=45.580%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.181%
   Raw/Executed turnover: raw_mean=45.443% | executed/raw=0.550

[RAND] Run 14/32 (Seed=25481):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +36.42%
   Annualized Return: +36.42%
   Sharpe: 1.9547
   Volatility (Ann.): 15.57%
   Max DD: 9.04%
   Turnover (episode): 26.53%
   Turnover (step): mean=26.527% | p95=38.355% | max=47.814%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.400%
   Raw/Executed turnover: raw_mean=48.232% | executed/raw=0.550

[RAND] Run 15/32 (Seed=25482):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +40.67%
   Annualized Return: +40.67%
   Sharpe: 2.1485
   Volatility (Ann.): 15.60%
   Max DD: 8.40%
   Turnover (episode): 25.18%
   Turnover (step): mean=25.181% | p95=37.126% | max=45.124%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.243%
   Raw/Executed turnover: raw_mean=45.783% | executed/raw=0.550

[RAND] Run 16/32 (Seed=25483):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +35.90%
   Annualized Return: +35.90%
   Sharpe: 1.8936
   Volatility (Ann.): 15.89%
   Max DD: 8.38%
   Turnover (episode): 26.44%
   Turnover (step): mean=26.443% | p95=36.450% | max=43.530%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.235%
   Raw/Executed turnover: raw_mean=48.079% | executed/raw=0.550

[RAND] Run 17/32 (Seed=25484):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +41.17%
   Annualized Return: +41.17%
   Sharpe: 2.1395
   Volatility (Ann.): 15.85%
   Max DD: 9.68%
   Turnover (episode): 25.10%
   Turnover (step): mean=25.102% | p95=38.835% | max=45.331%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.346%
   Raw/Executed turnover: raw_mean=45.640% | executed/raw=0.550

[RAND] Run 18/32 (Seed=25485):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +39.47%
   Annualized Return: +39.47%
   Sharpe: 2.0658
   Volatility (Ann.): 15.83%
   Max DD: 9.12%
   Turnover (episode): 24.94%
   Turnover (step): mean=24.939% | p95=37.058% | max=48.906%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.297%
   Raw/Executed turnover: raw_mean=45.343% | executed/raw=0.550

[RAND] Run 19/32 (Seed=25486):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +39.39%
   Annualized Return: +39.39%
   Sharpe: 2.0919
   Volatility (Ann.): 15.58%
   Max DD: 8.85%
   Turnover (episode): 25.27%
   Turnover (step): mean=25.267% | p95=37.708% | max=43.534%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.357%
   Raw/Executed turnover: raw_mean=45.941% | executed/raw=0.550

[RAND] Run 20/32 (Seed=25487):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +41.30%
   Annualized Return: +41.30%
   Sharpe: 2.1813
   Volatility (Ann.): 15.57%
   Max DD: 9.64%
   Turnover (episode): 25.52%
   Turnover (step): mean=25.522% | p95=36.304% | max=47.480%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.263%
   Raw/Executed turnover: raw_mean=46.403% | executed/raw=0.550

[RAND] Run 21/32 (Seed=25488):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +42.34%
   Annualized Return: +42.34%
   Sharpe: 2.1695
   Volatility (Ann.): 16.03%
   Max DD: 9.78%
   Turnover (episode): 25.88%
   Turnover (step): mean=25.882% | p95=38.507% | max=43.983%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.404%
   Raw/Executed turnover: raw_mean=47.058% | executed/raw=0.550

[RAND] Run 22/32 (Seed=25489):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +43.27%
   Annualized Return: +43.27%
   Sharpe: 2.2491
   Volatility (Ann.): 15.73%
   Max DD: 8.04%
   Turnover (episode): 26.01%
   Turnover (step): mean=26.011% | p95=38.203% | max=45.926%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.385%
   Raw/Executed turnover: raw_mean=47.293% | executed/raw=0.550

[RAND] Run 23/32 (Seed=25490):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +45.43%
   Annualized Return: +45.43%
   Sharpe: 2.3397
   Volatility (Ann.): 15.77%
   Max DD: 8.13%
   Turnover (episode): 26.37%
   Turnover (step): mean=26.371% | p95=38.736% | max=47.215%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.415%
   Raw/Executed turnover: raw_mean=47.948% | executed/raw=0.550

[RAND] Run 24/32 (Seed=25491):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +38.25%
   Annualized Return: +38.25%
   Sharpe: 2.0260
   Volatility (Ann.): 15.69%
   Max DD: 10.02%
   Turnover (episode): 26.01%
   Turnover (step): mean=26.009% | p95=37.504% | max=47.472%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.352%
   Raw/Executed turnover: raw_mean=47.290% | executed/raw=0.550

[RAND] Run 25/32 (Seed=25492):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +43.78%
   Annualized Return: +43.78%
   Sharpe: 2.2649
   Volatility (Ann.): 15.78%
   Max DD: 9.50%
   Turnover (episode): 26.14%
   Turnover (step): mean=26.140% | p95=38.625% | max=44.073%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.337%
   Raw/Executed turnover: raw_mean=47.527% | executed/raw=0.550

[RAND] Run 26/32 (Seed=25493):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +41.42%
   Annualized Return: +41.42%
   Sharpe: 2.1826
   Volatility (Ann.): 15.60%
   Max DD: 8.83%
   Turnover (episode): 26.58%
   Turnover (step): mean=26.581% | p95=38.054% | max=43.927%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.391%
   Raw/Executed turnover: raw_mean=48.330% | executed/raw=0.550

[RAND] Run 27/32 (Seed=25494):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +39.40%
   Annualized Return: +39.40%
   Sharpe: 2.0786
   Volatility (Ann.): 15.69%
   Max DD: 7.98%
   Turnover (episode): 25.87%
   Turnover (step): mean=25.874% | p95=37.466% | max=45.761%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.329%
   Raw/Executed turnover: raw_mean=47.044% | executed/raw=0.550

[RAND] Run 28/32 (Seed=25495):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +37.31%
   Annualized Return: +37.31%
   Sharpe: 1.9934
   Volatility (Ann.): 15.60%
   Max DD: 8.62%
   Turnover (episode): 26.81%
   Turnover (step): mean=26.815% | p95=37.972% | max=46.813%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.429%
   Raw/Executed turnover: raw_mean=48.754% | executed/raw=0.550

[RAND] Run 29/32 (Seed=25496):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +39.30%
   Annualized Return: +39.30%
   Sharpe: 2.0690
   Volatility (Ann.): 15.73%
   Max DD: 8.21%
   Turnover (episode): 25.23%
   Turnover (step): mean=25.232% | p95=36.515% | max=48.107%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.274%
   Raw/Executed turnover: raw_mean=45.876% | executed/raw=0.550

[RAND] Run 30/32 (Seed=25497):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +34.33%
   Annualized Return: +34.33%
   Sharpe: 1.8725
   Volatility (Ann.): 15.41%
   Max DD: 8.96%
   Turnover (episode): 26.14%
   Turnover (step): mean=26.143% | p95=39.521% | max=45.107%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.435%
   Raw/Executed turnover: raw_mean=47.534% | executed/raw=0.550

[RAND] Run 31/32 (Seed=25498):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +38.36%
   Annualized Return: +38.36%
   Sharpe: 2.0367
   Volatility (Ann.): 15.64%
   Max DD: 8.86%
   Turnover (episode): 25.64%
   Turnover (step): mean=25.644% | p95=37.345% | max=45.655%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.324%
   Raw/Executed turnover: raw_mean=46.625% | executed/raw=0.550

[RAND] Run 32/32 (Seed=25499):
   Start Date: 2020-07-02 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +41.28%
   Annualized Return: +41.28%
   Sharpe: 2.1971
   Volatility (Ann.): 15.44%
   Max DD: 8.19%
   Turnover (episode): 25.87%
   Turnover (step): mean=25.873% | p95=37.148% | max=43.834%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.280%
   Raw/Executed turnover: raw_mean=47.041% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +39.30%
   Std:  3.02%
   Min:  +33.38%
   Max:  +45.43%

Annualized Return (%):
   Mean: +39.30%
   Std:  3.02%
   Min:  +33.38%
   Max:  +45.43%

Sharpe Ratio (annualized):
   Mean: 2.0798
   Std:  0.1337
   Min:  1.8021
   Max:  2.3397

Volatility (Ann. %):
   Mean: +15.63%
   Std:  0.16%
   Min:  +15.24%
   Max:  +16.03%

Max Drawdown (%):
   Mean: 8.74%
   Std:  0.60%
   Min:  7.58%
   Max:  10.02%

Turnover (%):
   Mean: 25.71%
   Std:  0.56%

Turnover Step Detail (%):
   Mean(step mean): 25.705%
   Mean(step p95):  37.276%
   Mean(step max):  45.661%
   Mean exceed rate: 8.9%
   Mean excess over target: 0.324%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_222255.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs
      status=ok rows=32 copied=9
[RUN] fixed_252_year -> year_003 | bucket=2020 | start=2020-12-31 | h=252

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
   Start Date: 2020-12-31
   Market Regime: COVID Recovery (2020-05 to 2020-12)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $143,260.53
   Total Return: +43.26%
   Annualized Return: +43.26%
   Sharpe Ratio: 2.2351 (annualized)
   Sortino Ratio: 3.5398 (annualized)
   Max Drawdown: 6.44%
   Volatility (Ann.): 15.83%
   Turnover: 3.10%
   Win Rate: 57.37%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=25594):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +29.67%
   Annualized Return: +29.67%
   Sharpe: 1.6371
   Volatility (Ann.): 15.46%
   Max DD: 6.55%
   Turnover (episode): 25.00%
   Turnover (step): mean=24.998% | p95=36.595% | max=45.845%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.290%
   Raw/Executed turnover: raw_mean=45.451% | executed/raw=0.550

[RAND] Run 2/32 (Seed=25595):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +24.96%
   Annualized Return: +24.96%
   Sharpe: 1.3873
   Volatility (Ann.): 15.58%
   Max DD: 6.44%
   Turnover (episode): 26.06%
   Turnover (step): mean=26.057% | p95=37.712% | max=53.205%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.369%
   Raw/Executed turnover: raw_mean=47.377% | executed/raw=0.550

[RAND] Run 3/32 (Seed=25596):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +24.64%
   Annualized Return: +24.64%
   Sharpe: 1.3433
   Volatility (Ann.): 15.93%
   Max DD: 6.91%
   Turnover (episode): 26.20%
   Turnover (step): mean=26.198% | p95=36.475% | max=48.216%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.249%
   Raw/Executed turnover: raw_mean=47.632% | executed/raw=0.550

[RAND] Run 4/32 (Seed=25597):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +27.06%
   Annualized Return: +27.06%
   Sharpe: 1.4950
   Volatility (Ann.): 15.58%
   Max DD: 6.06%
   Turnover (episode): 26.32%
   Turnover (step): mean=26.322% | p95=37.562% | max=42.643%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.324%
   Raw/Executed turnover: raw_mean=47.859% | executed/raw=0.550

[RAND] Run 5/32 (Seed=25598):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +24.87%
   Annualized Return: +24.87%
   Sharpe: 1.3889
   Volatility (Ann.): 15.50%
   Max DD: 6.47%
   Turnover (episode): 25.25%
   Turnover (step): mean=25.246% | p95=36.335% | max=43.890%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.250%
   Raw/Executed turnover: raw_mean=45.902% | executed/raw=0.550

[RAND] Run 6/32 (Seed=25599):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +27.24%
   Annualized Return: +27.24%
   Sharpe: 1.4922
   Volatility (Ann.): 15.71%
   Max DD: 6.79%
   Turnover (episode): 25.30%
   Turnover (step): mean=25.302% | p95=34.772% | max=43.640%
   Turnover vs target: target=35.000% | exceed_rate=4.8% | mean_excess=0.139%
   Raw/Executed turnover: raw_mean=46.003% | executed/raw=0.550

[RAND] Run 7/32 (Seed=25600):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +26.64%
   Annualized Return: +26.64%
   Sharpe: 1.4745
   Volatility (Ann.): 15.57%
   Max DD: 6.14%
   Turnover (episode): 24.68%
   Turnover (step): mean=24.680% | p95=35.624% | max=45.424%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.216%
   Raw/Executed turnover: raw_mean=44.873% | executed/raw=0.550

[RAND] Run 8/32 (Seed=25601):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +24.72%
   Annualized Return: +24.72%
   Sharpe: 1.3875
   Volatility (Ann.): 15.42%
   Max DD: 7.24%
   Turnover (episode): 26.47%
   Turnover (step): mean=26.469% | p95=38.890% | max=44.102%
   Turnover vs target: target=35.000% | exceed_rate=14.3% | mean_excess=0.456%
   Raw/Executed turnover: raw_mean=48.125% | executed/raw=0.550

[RAND] Run 9/32 (Seed=25602):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +23.78%
   Annualized Return: +23.78%
   Sharpe: 1.3158
   Volatility (Ann.): 15.71%
   Max DD: 6.62%
   Turnover (episode): 26.26%
   Turnover (step): mean=26.259% | p95=36.279% | max=47.287%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.312%
   Raw/Executed turnover: raw_mean=47.744% | executed/raw=0.550

[RAND] Run 10/32 (Seed=25603):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +23.57%
   Annualized Return: +23.57%
   Sharpe: 1.3116
   Volatility (Ann.): 15.63%
   Max DD: 6.83%
   Turnover (episode): 25.73%
   Turnover (step): mean=25.729% | p95=35.912% | max=45.402%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.245%
   Raw/Executed turnover: raw_mean=46.779% | executed/raw=0.550

[RAND] Run 11/32 (Seed=25604):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +29.40%
   Annualized Return: +29.40%
   Sharpe: 1.6069
   Volatility (Ann.): 15.64%
   Max DD: 6.17%
   Turnover (episode): 26.40%
   Turnover (step): mean=26.404% | p95=37.020% | max=44.981%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.256%
   Raw/Executed turnover: raw_mean=48.008% | executed/raw=0.550

[RAND] Run 12/32 (Seed=25605):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +26.01%
   Annualized Return: +26.01%
   Sharpe: 1.4367
   Volatility (Ann.): 15.63%
   Max DD: 7.19%
   Turnover (episode): 26.06%
   Turnover (step): mean=26.061% | p95=38.372% | max=45.545%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.421%
   Raw/Executed turnover: raw_mean=47.384% | executed/raw=0.550

[RAND] Run 13/32 (Seed=25606):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +26.60%
   Annualized Return: +26.60%
   Sharpe: 1.4703
   Volatility (Ann.): 15.59%
   Max DD: 6.93%
   Turnover (episode): 25.97%
   Turnover (step): mean=25.970% | p95=38.244% | max=53.261%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.486%
   Raw/Executed turnover: raw_mean=47.219% | executed/raw=0.550

[RAND] Run 14/32 (Seed=25607):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +26.02%
   Annualized Return: +26.02%
   Sharpe: 1.4230
   Volatility (Ann.): 15.81%
   Max DD: 5.45%
   Turnover (episode): 25.82%
   Turnover (step): mean=25.822% | p95=37.034% | max=49.233%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.323%
   Raw/Executed turnover: raw_mean=46.949% | executed/raw=0.550

[RAND] Run 15/32 (Seed=25608):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +23.83%
   Annualized Return: +23.83%
   Sharpe: 1.3371
   Volatility (Ann.): 15.47%
   Max DD: 7.13%
   Turnover (episode): 25.94%
   Turnover (step): mean=25.941% | p95=36.403% | max=48.457%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.251%
   Raw/Executed turnover: raw_mean=47.166% | executed/raw=0.550

[RAND] Run 16/32 (Seed=25609):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +24.57%
   Annualized Return: +24.57%
   Sharpe: 1.3474
   Volatility (Ann.): 15.84%
   Max DD: 7.26%
   Turnover (episode): 25.31%
   Turnover (step): mean=25.312% | p95=35.065% | max=42.556%
   Turnover vs target: target=35.000% | exceed_rate=5.6% | mean_excess=0.128%
   Raw/Executed turnover: raw_mean=46.022% | executed/raw=0.550

[RAND] Run 17/32 (Seed=25610):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +27.46%
   Annualized Return: +27.46%
   Sharpe: 1.5254
   Volatility (Ann.): 15.46%
   Max DD: 6.18%
   Turnover (episode): 24.95%
   Turnover (step): mean=24.948% | p95=37.197% | max=43.941%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.243%
   Raw/Executed turnover: raw_mean=45.360% | executed/raw=0.550

[RAND] Run 18/32 (Seed=25611):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +21.94%
   Annualized Return: +21.94%
   Sharpe: 1.2312
   Volatility (Ann.): 15.55%
   Max DD: 7.37%
   Turnover (episode): 25.33%
   Turnover (step): mean=25.326% | p95=37.492% | max=51.128%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.322%
   Raw/Executed turnover: raw_mean=46.046% | executed/raw=0.550

[RAND] Run 19/32 (Seed=25612):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +27.71%
   Annualized Return: +27.71%
   Sharpe: 1.5261
   Volatility (Ann.): 15.60%
   Max DD: 6.38%
   Turnover (episode): 25.93%
   Turnover (step): mean=25.931% | p95=38.030% | max=56.500%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.422%
   Raw/Executed turnover: raw_mean=47.148% | executed/raw=0.550

[RAND] Run 20/32 (Seed=25613):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +24.57%
   Annualized Return: +24.57%
   Sharpe: 1.3702
   Volatility (Ann.): 15.54%
   Max DD: 6.90%
   Turnover (episode): 25.91%
   Turnover (step): mean=25.915% | p95=36.433% | max=46.502%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.280%
   Raw/Executed turnover: raw_mean=47.118% | executed/raw=0.550

[RAND] Run 21/32 (Seed=25614):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +21.38%
   Annualized Return: +21.38%
   Sharpe: 1.2143
   Volatility (Ann.): 15.36%
   Max DD: 6.83%
   Turnover (episode): 27.10%
   Turnover (step): mean=27.099% | p95=39.103% | max=50.824%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.462%
   Raw/Executed turnover: raw_mean=49.272% | executed/raw=0.550

[RAND] Run 22/32 (Seed=25615):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +28.38%
   Annualized Return: +28.38%
   Sharpe: 1.5592
   Volatility (Ann.): 15.60%
   Max DD: 6.78%
   Turnover (episode): 25.48%
   Turnover (step): mean=25.484% | p95=37.001% | max=46.358%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.275%
   Raw/Executed turnover: raw_mean=46.335% | executed/raw=0.550

[RAND] Run 23/32 (Seed=25616):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +27.70%
   Annualized Return: +27.70%
   Sharpe: 1.5327
   Volatility (Ann.): 15.51%
   Max DD: 6.84%
   Turnover (episode): 25.48%
   Turnover (step): mean=25.476% | p95=36.281% | max=44.001%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.230%
   Raw/Executed turnover: raw_mean=46.319% | executed/raw=0.550

[RAND] Run 24/32 (Seed=25617):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +28.58%
   Annualized Return: +28.58%
   Sharpe: 1.5813
   Volatility (Ann.): 15.47%
   Max DD: 6.99%
   Turnover (episode): 25.97%
   Turnover (step): mean=25.966% | p95=36.834% | max=47.708%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.244%
   Raw/Executed turnover: raw_mean=47.211% | executed/raw=0.550

[RAND] Run 25/32 (Seed=25618):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +28.57%
   Annualized Return: +28.57%
   Sharpe: 1.5993
   Volatility (Ann.): 15.27%
   Max DD: 6.65%
   Turnover (episode): 25.33%
   Turnover (step): mean=25.333% | p95=37.195% | max=46.371%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.356%
   Raw/Executed turnover: raw_mean=46.059% | executed/raw=0.550

[RAND] Run 26/32 (Seed=25619):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +29.51%
   Annualized Return: +29.51%
   Sharpe: 1.6193
   Volatility (Ann.): 15.56%
   Max DD: 6.66%
   Turnover (episode): 25.81%
   Turnover (step): mean=25.815% | p95=38.912% | max=43.828%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.402%
   Raw/Executed turnover: raw_mean=46.936% | executed/raw=0.550

[RAND] Run 27/32 (Seed=25620):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +26.71%
   Annualized Return: +26.71%
   Sharpe: 1.4813
   Volatility (Ann.): 15.53%
   Max DD: 6.20%
   Turnover (episode): 25.23%
   Turnover (step): mean=25.234% | p95=37.125% | max=47.999%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.343%
   Raw/Executed turnover: raw_mean=45.880% | executed/raw=0.550

[RAND] Run 28/32 (Seed=25621):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +27.56%
   Annualized Return: +27.56%
   Sharpe: 1.5006
   Volatility (Ann.): 15.80%
   Max DD: 6.38%
   Turnover (episode): 25.68%
   Turnover (step): mean=25.680% | p95=36.310% | max=43.021%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.179%
   Raw/Executed turnover: raw_mean=46.691% | executed/raw=0.550

[RAND] Run 29/32 (Seed=25622):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +25.51%
   Annualized Return: +25.51%
   Sharpe: 1.4301
   Volatility (Ann.): 15.40%
   Max DD: 6.43%
   Turnover (episode): 26.31%
   Turnover (step): mean=26.306% | p95=37.102% | max=43.081%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.288%
   Raw/Executed turnover: raw_mean=47.829% | executed/raw=0.550

[RAND] Run 30/32 (Seed=25623):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +23.58%
   Annualized Return: +23.58%
   Sharpe: 1.3136
   Volatility (Ann.): 15.61%
   Max DD: 6.66%
   Turnover (episode): 25.77%
   Turnover (step): mean=25.772% | p95=36.967% | max=44.980%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.317%
   Raw/Executed turnover: raw_mean=46.858% | executed/raw=0.550

[RAND] Run 31/32 (Seed=25624):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +23.06%
   Annualized Return: +23.06%
   Sharpe: 1.2854
   Volatility (Ann.): 15.62%
   Max DD: 7.03%
   Turnover (episode): 25.02%
   Turnover (step): mean=25.021% | p95=36.087% | max=44.089%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.215%
   Raw/Executed turnover: raw_mean=45.493% | executed/raw=0.550

[RAND] Run 32/32 (Seed=25625):
   Start Date: 2020-12-31 | Regime: COVID Recovery (2020-05 to 2020-12)
   Days Traded: 252 (1.00 years)
   Total Return: +23.76%
   Annualized Return: +23.76%
   Sharpe: 1.3357
   Volatility (Ann.): 15.43%
   Max DD: 6.50%
   Turnover (episode): 25.52%
   Turnover (step): mean=25.517% | p95=36.317% | max=43.851%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.249%
   Raw/Executed turnover: raw_mean=46.395% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +25.93%
   Std:  2.22%
   Min:  +21.38%
   Max:  +29.67%

Annualized Return (%):
   Mean: +25.93%
   Std:  2.22%
   Min:  +21.38%
   Max:  +29.67%

Sharpe Ratio (annualized):
   Mean: 1.4363
   Std:  0.1155
   Min:  1.2143
   Max:  1.6371

Volatility (Ann. %):
   Mean: +15.57%
   Std:  0.14%
   Min:  +15.27%
   Max:  +15.93%

Max Drawdown (%):
   Mean: 6.66%
   Std:  0.42%
   Min:  5.45%
   Max:  7.37%

Turnover (%):
   Mean: 25.74%
   Std:  0.53%

Turnover Step Detail (%):
   Mean(step mean): 25.737%
   Mean(step p95):  36.959%
   Mean(step max):  46.496%
   Mean exceed rate: 8.6%
   Mean excess over target: 0.298%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_225209.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs
      status=ok rows=32 copied=9
[RUN] fixed_252_year -> year_004 | bucket=2021 | start=2021-01-04 | h=252

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
   Start Date: 2021-01-04
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $140,262.26
   Total Return: +40.26%
   Annualized Return: +40.26%
   Sharpe Ratio: 2.1707 (annualized)
   Sortino Ratio: 3.4436 (annualized)
   Max Drawdown: 6.44%
   Volatility (Ann.): 15.28%
   Turnover: 3.68%
   Win Rate: 57.77%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=25595):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +25.44%
   Annualized Return: +25.44%
   Sharpe: 1.4311
   Volatility (Ann.): 15.35%
   Max DD: 7.61%
   Turnover (episode): 25.53%
   Turnover (step): mean=25.529% | p95=35.981% | max=47.187%
   Turnover vs target: target=35.000% | exceed_rate=6.0% | mean_excess=0.212%
   Raw/Executed turnover: raw_mean=46.417% | executed/raw=0.550

[RAND] Run 2/32 (Seed=25596):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +23.92%
   Annualized Return: +23.92%
   Sharpe: 1.3638
   Volatility (Ann.): 15.18%
   Max DD: 7.25%
   Turnover (episode): 25.79%
   Turnover (step): mean=25.794% | p95=38.042% | max=47.870%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.371%
   Raw/Executed turnover: raw_mean=46.899% | executed/raw=0.550

[RAND] Run 3/32 (Seed=25597):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +24.30%
   Annualized Return: +24.30%
   Sharpe: 1.3664
   Volatility (Ann.): 15.41%
   Max DD: 7.05%
   Turnover (episode): 25.62%
   Turnover (step): mean=25.618% | p95=38.586% | max=45.234%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.417%
   Raw/Executed turnover: raw_mean=46.578% | executed/raw=0.550

[RAND] Run 4/32 (Seed=25598):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +25.56%
   Annualized Return: +25.56%
   Sharpe: 1.4167
   Volatility (Ann.): 15.59%
   Max DD: 6.56%
   Turnover (episode): 26.02%
   Turnover (step): mean=26.024% | p95=37.086% | max=43.532%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.281%
   Raw/Executed turnover: raw_mean=47.316% | executed/raw=0.550

[RAND] Run 5/32 (Seed=25599):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +27.90%
   Annualized Return: +27.90%
   Sharpe: 1.5469
   Volatility (Ann.): 15.47%
   Max DD: 6.23%
   Turnover (episode): 25.86%
   Turnover (step): mean=25.864% | p95=37.558% | max=47.042%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.351%
   Raw/Executed turnover: raw_mean=47.026% | executed/raw=0.550

[RAND] Run 6/32 (Seed=25600):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +27.71%
   Annualized Return: +27.71%
   Sharpe: 1.5395
   Volatility (Ann.): 15.44%
   Max DD: 6.32%
   Turnover (episode): 25.93%
   Turnover (step): mean=25.927% | p95=37.361% | max=46.975%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.370%
   Raw/Executed turnover: raw_mean=47.140% | executed/raw=0.550

[RAND] Run 7/32 (Seed=25601):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +28.03%
   Annualized Return: +28.03%
   Sharpe: 1.5647
   Volatility (Ann.): 15.34%
   Max DD: 6.34%
   Turnover (episode): 26.39%
   Turnover (step): mean=26.392% | p95=37.651% | max=45.741%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.388%
   Raw/Executed turnover: raw_mean=47.986% | executed/raw=0.550

[RAND] Run 8/32 (Seed=25602):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +26.87%
   Annualized Return: +26.87%
   Sharpe: 1.4850
   Volatility (Ann.): 15.58%
   Max DD: 6.69%
   Turnover (episode): 26.22%
   Turnover (step): mean=26.225% | p95=37.131% | max=43.427%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.284%
   Raw/Executed turnover: raw_mean=47.681% | executed/raw=0.550

[RAND] Run 9/32 (Seed=25603):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +27.38%
   Annualized Return: +27.38%
   Sharpe: 1.4968
   Volatility (Ann.): 15.74%
   Max DD: 6.45%
   Turnover (episode): 25.22%
   Turnover (step): mean=25.219% | p95=35.920% | max=40.174%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.159%
   Raw/Executed turnover: raw_mean=45.854% | executed/raw=0.550

[RAND] Run 10/32 (Seed=25604):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +25.02%
   Annualized Return: +25.02%
   Sharpe: 1.3862
   Volatility (Ann.): 15.63%
   Max DD: 7.36%
   Turnover (episode): 26.25%
   Turnover (step): mean=26.249% | p95=36.262% | max=45.691%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.247%
   Raw/Executed turnover: raw_mean=47.725% | executed/raw=0.550

[RAND] Run 11/32 (Seed=25605):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +26.51%
   Annualized Return: +26.51%
   Sharpe: 1.4658
   Volatility (Ann.): 15.59%
   Max DD: 7.83%
   Turnover (episode): 25.45%
   Turnover (step): mean=25.453% | p95=35.951% | max=49.196%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.243%
   Raw/Executed turnover: raw_mean=46.279% | executed/raw=0.550

[RAND] Run 12/32 (Seed=25606):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +23.77%
   Annualized Return: +23.77%
   Sharpe: 1.3278
   Volatility (Ann.): 15.55%
   Max DD: 6.20%
   Turnover (episode): 25.74%
   Turnover (step): mean=25.740% | p95=36.790% | max=46.410%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.277%
   Raw/Executed turnover: raw_mean=46.800% | executed/raw=0.550

[RAND] Run 13/32 (Seed=25607):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +24.16%
   Annualized Return: +24.16%
   Sharpe: 1.3449
   Volatility (Ann.): 15.59%
   Max DD: 7.32%
   Turnover (episode): 26.37%
   Turnover (step): mean=26.372% | p95=37.324% | max=43.243%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.289%
   Raw/Executed turnover: raw_mean=47.949% | executed/raw=0.550

[RAND] Run 14/32 (Seed=25608):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +25.98%
   Annualized Return: +25.98%
   Sharpe: 1.4382
   Volatility (Ann.): 15.60%
   Max DD: 7.09%
   Turnover (episode): 25.44%
   Turnover (step): mean=25.436% | p95=35.994% | max=45.148%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.277%
   Raw/Executed turnover: raw_mean=46.248% | executed/raw=0.550

[RAND] Run 15/32 (Seed=25609):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +27.05%
   Annualized Return: +27.05%
   Sharpe: 1.5261
   Volatility (Ann.): 15.22%
   Max DD: 6.44%
   Turnover (episode): 26.06%
   Turnover (step): mean=26.059% | p95=37.411% | max=50.239%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.422%
   Raw/Executed turnover: raw_mean=47.380% | executed/raw=0.550

[RAND] Run 16/32 (Seed=25610):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +25.42%
   Annualized Return: +25.42%
   Sharpe: 1.4091
   Volatility (Ann.): 15.60%
   Max DD: 6.34%
   Turnover (episode): 25.48%
   Turnover (step): mean=25.476% | p95=37.169% | max=43.994%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.258%
   Raw/Executed turnover: raw_mean=46.319% | executed/raw=0.550

[RAND] Run 17/32 (Seed=25611):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +28.69%
   Annualized Return: +28.69%
   Sharpe: 1.5837
   Volatility (Ann.): 15.50%
   Max DD: 6.49%
   Turnover (episode): 26.05%
   Turnover (step): mean=26.055% | p95=36.553% | max=47.132%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.320%
   Raw/Executed turnover: raw_mean=47.373% | executed/raw=0.550

[RAND] Run 18/32 (Seed=25612):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +26.52%
   Annualized Return: +26.52%
   Sharpe: 1.4821
   Volatility (Ann.): 15.40%
   Max DD: 6.81%
   Turnover (episode): 25.64%
   Turnover (step): mean=25.640% | p95=37.381% | max=44.278%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.302%
   Raw/Executed turnover: raw_mean=46.619% | executed/raw=0.550

[RAND] Run 19/32 (Seed=25613):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +25.01%
   Annualized Return: +25.01%
   Sharpe: 1.4011
   Volatility (Ann.): 15.44%
   Max DD: 7.39%
   Turnover (episode): 25.88%
   Turnover (step): mean=25.879% | p95=37.483% | max=48.944%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.356%
   Raw/Executed turnover: raw_mean=47.053% | executed/raw=0.550

[RAND] Run 20/32 (Seed=25614):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +27.06%
   Annualized Return: +27.06%
   Sharpe: 1.4998
   Volatility (Ann.): 15.52%
   Max DD: 6.54%
   Turnover (episode): 25.08%
   Turnover (step): mean=25.080% | p95=37.188% | max=43.141%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.324%
   Raw/Executed turnover: raw_mean=45.601% | executed/raw=0.550

[RAND] Run 21/32 (Seed=25615):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +21.29%
   Annualized Return: +21.29%
   Sharpe: 1.2180
   Volatility (Ann.): 15.24%
   Max DD: 6.62%
   Turnover (episode): 26.03%
   Turnover (step): mean=26.033% | p95=36.114% | max=43.628%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.228%
   Raw/Executed turnover: raw_mean=47.333% | executed/raw=0.550

[RAND] Run 22/32 (Seed=25616):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +22.94%
   Annualized Return: +22.94%
   Sharpe: 1.2934
   Volatility (Ann.): 15.42%
   Max DD: 6.11%
   Turnover (episode): 25.54%
   Turnover (step): mean=25.545% | p95=39.206% | max=44.351%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.408%
   Raw/Executed turnover: raw_mean=46.445% | executed/raw=0.550

[RAND] Run 23/32 (Seed=25617):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +23.88%
   Annualized Return: +23.88%
   Sharpe: 1.3390
   Volatility (Ann.): 15.47%
   Max DD: 6.70%
   Turnover (episode): 26.07%
   Turnover (step): mean=26.068% | p95=36.828% | max=47.766%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.261%
   Raw/Executed turnover: raw_mean=47.397% | executed/raw=0.550

[RAND] Run 24/32 (Seed=25618):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +31.84%
   Annualized Return: +31.84%
   Sharpe: 1.7219
   Volatility (Ann.): 15.69%
   Max DD: 6.22%
   Turnover (episode): 26.36%
   Turnover (step): mean=26.362% | p95=36.769% | max=49.500%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.278%
   Raw/Executed turnover: raw_mean=47.931% | executed/raw=0.550

[RAND] Run 25/32 (Seed=25619):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +23.26%
   Annualized Return: +23.26%
   Sharpe: 1.3099
   Volatility (Ann.): 15.43%
   Max DD: 7.29%
   Turnover (episode): 24.90%
   Turnover (step): mean=24.899% | p95=35.665% | max=44.123%
   Turnover vs target: target=35.000% | exceed_rate=6.0% | mean_excess=0.186%
   Raw/Executed turnover: raw_mean=45.272% | executed/raw=0.550

[RAND] Run 26/32 (Seed=25620):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +29.18%
   Annualized Return: +29.18%
   Sharpe: 1.6209
   Volatility (Ann.): 15.37%
   Max DD: 6.46%
   Turnover (episode): 26.07%
   Turnover (step): mean=26.065% | p95=37.088% | max=43.724%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.317%
   Raw/Executed turnover: raw_mean=47.391% | executed/raw=0.550

[RAND] Run 27/32 (Seed=25621):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +25.59%
   Annualized Return: +25.59%
   Sharpe: 1.4263
   Volatility (Ann.): 15.50%
   Max DD: 6.42%
   Turnover (episode): 25.67%
   Turnover (step): mean=25.672% | p95=38.493% | max=50.890%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.415%
   Raw/Executed turnover: raw_mean=46.676% | executed/raw=0.550

[RAND] Run 28/32 (Seed=25622):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +29.17%
   Annualized Return: +29.17%
   Sharpe: 1.6028
   Volatility (Ann.): 15.55%
   Max DD: 6.85%
   Turnover (episode): 25.69%
   Turnover (step): mean=25.694% | p95=37.073% | max=42.686%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.273%
   Raw/Executed turnover: raw_mean=46.717% | executed/raw=0.550

[RAND] Run 29/32 (Seed=25623):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +26.25%
   Annualized Return: +26.25%
   Sharpe: 1.4312
   Volatility (Ann.): 15.85%
   Max DD: 7.04%
   Turnover (episode): 25.47%
   Turnover (step): mean=25.471% | p95=37.591% | max=47.540%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.309%
   Raw/Executed turnover: raw_mean=46.311% | executed/raw=0.550

[RAND] Run 30/32 (Seed=25624):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +27.83%
   Annualized Return: +27.83%
   Sharpe: 1.5277
   Volatility (Ann.): 15.64%
   Max DD: 6.41%
   Turnover (episode): 25.67%
   Turnover (step): mean=25.674% | p95=35.657% | max=41.706%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.180%
   Raw/Executed turnover: raw_mean=46.680% | executed/raw=0.550

[RAND] Run 31/32 (Seed=25625):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +26.46%
   Annualized Return: +26.46%
   Sharpe: 1.4506
   Volatility (Ann.): 15.74%
   Max DD: 7.51%
   Turnover (episode): 25.76%
   Turnover (step): mean=25.759% | p95=36.573% | max=46.698%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.249%
   Raw/Executed turnover: raw_mean=46.835% | executed/raw=0.550

[RAND] Run 32/32 (Seed=25626):
   Start Date: 2021-01-04 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: +27.61%
   Annualized Return: +27.61%
   Sharpe: 1.5124
   Volatility (Ann.): 15.69%
   Max DD: 7.56%
   Turnover (episode): 24.75%
   Turnover (step): mean=24.754% | p95=36.720% | max=45.682%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.293%
   Raw/Executed turnover: raw_mean=45.008% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +26.18%
   Std:  2.16%
   Min:  +21.29%
   Max:  +31.84%

Annualized Return (%):
   Mean: +26.18%
   Std:  2.16%
   Min:  +21.29%
   Max:  +31.84%

Sharpe Ratio (annualized):
   Mean: 1.4541
   Std:  0.1076
   Min:  1.2180
   Max:  1.7219

Volatility (Ann. %):
   Mean: +15.51%
   Std:  0.16%
   Min:  +15.18%
   Max:  +15.85%

Max Drawdown (%):
   Mean: 6.80%
   Std:  0.49%
   Min:  6.11%
   Max:  7.83%

Turnover (%):
   Mean: 25.75%
   Std:  0.41%

Turnover Step Detail (%):
   Mean(step mean): 25.751%
   Mean(step p95):  37.019%
   Mean(step max):  45.715%
   Mean exceed rate: 8.9%
   Mean excess over target: 0.298%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_232154.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs
      status=ok rows=32 copied=9
[RUN] fixed_252_year -> year_005 | bucket=2021 | start=2021-07-06 | h=252

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
   Start Date: 2021-07-06
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $102,170.60
   Total Return: +2.17%
   Annualized Return: +2.17%
   Sharpe Ratio: 0.1001 (annualized)
   Sortino Ratio: 0.1414 (annualized)
   Max Drawdown: 14.57%
   Volatility (Ann.): 18.16%
   Turnover: 2.54%
   Win Rate: 53.78%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=5

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=25721):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.94%
   Annualized Return: -3.94%
   Sharpe: -0.2589
   Volatility (Ann.): 17.41%
   Max DD: 17.30%
   Turnover (episode): 25.99%
   Turnover (step): mean=25.990% | p95=38.377% | max=42.011%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.343%
   Raw/Executed turnover: raw_mean=47.255% | executed/raw=0.550

[RAND] Run 2/32 (Seed=25722):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -2.46%
   Annualized Return: -2.46%
   Sharpe: -0.1762
   Volatility (Ann.): 17.13%
   Max DD: 16.65%
   Turnover (episode): 25.59%
   Turnover (step): mean=25.590% | p95=36.997% | max=42.852%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.298%
   Raw/Executed turnover: raw_mean=46.527% | executed/raw=0.550

[RAND] Run 3/32 (Seed=25723):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -7.01%
   Annualized Return: -7.01%
   Sharpe: -0.4391
   Volatility (Ann.): 17.60%
   Max DD: 20.00%
   Turnover (episode): 25.23%
   Turnover (step): mean=25.228% | p95=37.311% | max=44.928%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.261%
   Raw/Executed turnover: raw_mean=45.870% | executed/raw=0.550

[RAND] Run 4/32 (Seed=25724):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -0.19%
   Annualized Return: -0.19%
   Sharpe: -0.0361
   Volatility (Ann.): 17.57%
   Max DD: 14.43%
   Turnover (episode): 26.17%
   Turnover (step): mean=26.170% | p95=38.531% | max=48.929%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.425%
   Raw/Executed turnover: raw_mean=47.581% | executed/raw=0.550

[RAND] Run 5/32 (Seed=25725):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -2.31%
   Annualized Return: -2.31%
   Sharpe: -0.1675
   Volatility (Ann.): 17.12%
   Max DD: 14.51%
   Turnover (episode): 24.96%
   Turnover (step): mean=24.962% | p95=37.749% | max=48.783%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.343%
   Raw/Executed turnover: raw_mean=45.386% | executed/raw=0.550

[RAND] Run 6/32 (Seed=25726):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -4.67%
   Annualized Return: -4.67%
   Sharpe: -0.2890
   Volatility (Ann.): 17.92%
   Max DD: 18.14%
   Turnover (episode): 25.22%
   Turnover (step): mean=25.215% | p95=36.242% | max=41.863%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.199%
   Raw/Executed turnover: raw_mean=45.846% | executed/raw=0.550

[RAND] Run 7/32 (Seed=25727):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -6.06%
   Annualized Return: -6.06%
   Sharpe: -0.3814
   Volatility (Ann.): 17.60%
   Max DD: 18.22%
   Turnover (episode): 25.19%
   Turnover (step): mean=25.191% | p95=36.937% | max=48.308%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.291%
   Raw/Executed turnover: raw_mean=45.802% | executed/raw=0.550

[RAND] Run 8/32 (Seed=25728):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.80%
   Annualized Return: -3.80%
   Sharpe: -0.2464
   Volatility (Ann.): 17.58%
   Max DD: 17.87%
   Turnover (episode): 24.87%
   Turnover (step): mean=24.870% | p95=36.528% | max=45.002%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.272%
   Raw/Executed turnover: raw_mean=45.218% | executed/raw=0.550

[RAND] Run 9/32 (Seed=25729):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -6.99%
   Annualized Return: -6.99%
   Sharpe: -0.4453
   Volatility (Ann.): 17.40%
   Max DD: 18.43%
   Turnover (episode): 25.16%
   Turnover (step): mean=25.161% | p95=36.778% | max=49.400%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.324%
   Raw/Executed turnover: raw_mean=45.748% | executed/raw=0.550

[RAND] Run 10/32 (Seed=25730):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -0.80%
   Annualized Return: -0.80%
   Sharpe: -0.0730
   Volatility (Ann.): 17.43%
   Max DD: 14.98%
   Turnover (episode): 24.78%
   Turnover (step): mean=24.775% | p95=37.064% | max=48.241%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.288%
   Raw/Executed turnover: raw_mean=45.046% | executed/raw=0.550

[RAND] Run 11/32 (Seed=25731):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -5.10%
   Annualized Return: -5.10%
   Sharpe: -0.3245
   Volatility (Ann.): 17.56%
   Max DD: 17.44%
   Turnover (episode): 25.76%
   Turnover (step): mean=25.756% | p95=35.990% | max=41.075%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.154%
   Raw/Executed turnover: raw_mean=46.828% | executed/raw=0.550

[RAND] Run 12/32 (Seed=25732):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.82%
   Annualized Return: -3.82%
   Sharpe: -0.2568
   Volatility (Ann.): 17.20%
   Max DD: 17.81%
   Turnover (episode): 25.85%
   Turnover (step): mean=25.845% | p95=36.610% | max=51.188%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.296%
   Raw/Executed turnover: raw_mean=46.991% | executed/raw=0.550

[RAND] Run 13/32 (Seed=25733):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.39%
   Annualized Return: -3.39%
   Sharpe: -0.2259
   Volatility (Ann.): 17.41%
   Max DD: 17.02%
   Turnover (episode): 25.64%
   Turnover (step): mean=25.644% | p95=37.168% | max=48.703%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.322%
   Raw/Executed turnover: raw_mean=46.626% | executed/raw=0.550

[RAND] Run 14/32 (Seed=25734):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.29%
   Annualized Return: -3.29%
   Sharpe: -0.2200
   Volatility (Ann.): 17.41%
   Max DD: 17.79%
   Turnover (episode): 24.68%
   Turnover (step): mean=24.678% | p95=35.104% | max=46.596%
   Turnover vs target: target=35.000% | exceed_rate=5.2% | mean_excess=0.219%
   Raw/Executed turnover: raw_mean=44.869% | executed/raw=0.550

[RAND] Run 15/32 (Seed=25735):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -5.82%
   Annualized Return: -5.82%
   Sharpe: -0.3693
   Volatility (Ann.): 17.52%
   Max DD: 18.70%
   Turnover (episode): 24.93%
   Turnover (step): mean=24.929% | p95=33.282% | max=43.884%
   Turnover vs target: target=35.000% | exceed_rate=3.2% | mean_excess=0.144%
   Raw/Executed turnover: raw_mean=45.325% | executed/raw=0.550

[RAND] Run 16/32 (Seed=25736):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.03%
   Annualized Return: -3.03%
   Sharpe: -0.2018
   Volatility (Ann.): 17.54%
   Max DD: 16.02%
   Turnover (episode): 26.30%
   Turnover (step): mean=26.295% | p95=37.313% | max=51.569%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.304%
   Raw/Executed turnover: raw_mean=47.810% | executed/raw=0.550

[RAND] Run 17/32 (Seed=25737):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -6.14%
   Annualized Return: -6.14%
   Sharpe: -0.3916
   Volatility (Ann.): 17.42%
   Max DD: 17.87%
   Turnover (episode): 25.75%
   Turnover (step): mean=25.755% | p95=38.251% | max=43.045%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.386%
   Raw/Executed turnover: raw_mean=46.827% | executed/raw=0.550

[RAND] Run 18/32 (Seed=25738):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -7.43%
   Annualized Return: -7.43%
   Sharpe: -0.4662
   Volatility (Ann.): 17.57%
   Max DD: 20.19%
   Turnover (episode): 25.56%
   Turnover (step): mean=25.555% | p95=36.527% | max=43.470%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.238%
   Raw/Executed turnover: raw_mean=46.464% | executed/raw=0.550

[RAND] Run 19/32 (Seed=25739):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -5.27%
   Annualized Return: -5.27%
   Sharpe: -0.3423
   Volatility (Ann.): 17.31%
   Max DD: 17.43%
   Turnover (episode): 25.32%
   Turnover (step): mean=25.316% | p95=37.472% | max=57.063%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.411%
   Raw/Executed turnover: raw_mean=46.029% | executed/raw=0.550

[RAND] Run 20/32 (Seed=25740):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -1.39%
   Annualized Return: -1.39%
   Sharpe: -0.1037
   Volatility (Ann.): 17.67%
   Max DD: 17.35%
   Turnover (episode): 26.34%
   Turnover (step): mean=26.340% | p95=37.630% | max=49.468%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.396%
   Raw/Executed turnover: raw_mean=47.891% | executed/raw=0.550

[RAND] Run 21/32 (Seed=25741):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -2.50%
   Annualized Return: -2.50%
   Sharpe: -0.1748
   Volatility (Ann.): 17.31%
   Max DD: 14.98%
   Turnover (episode): 25.10%
   Turnover (step): mean=25.104% | p95=37.085% | max=45.285%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.249%
   Raw/Executed turnover: raw_mean=45.643% | executed/raw=0.550

[RAND] Run 22/32 (Seed=25742):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -2.43%
   Annualized Return: -2.43%
   Sharpe: -0.1628
   Volatility (Ann.): 17.71%
   Max DD: 16.16%
   Turnover (episode): 25.61%
   Turnover (step): mean=25.615% | p95=37.449% | max=50.670%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.390%
   Raw/Executed turnover: raw_mean=46.572% | executed/raw=0.550

[RAND] Run 23/32 (Seed=25743):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -2.09%
   Annualized Return: -2.09%
   Sharpe: -0.1499
   Volatility (Ann.): 17.35%
   Max DD: 17.22%
   Turnover (episode): 25.79%
   Turnover (step): mean=25.791% | p95=37.137% | max=52.353%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.334%
   Raw/Executed turnover: raw_mean=46.894% | executed/raw=0.550

[RAND] Run 24/32 (Seed=25744):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -5.17%
   Annualized Return: -5.17%
   Sharpe: -0.3373
   Volatility (Ann.): 17.27%
   Max DD: 18.05%
   Turnover (episode): 25.04%
   Turnover (step): mean=25.045% | p95=34.799% | max=51.089%
   Turnover vs target: target=35.000% | exceed_rate=4.4% | mean_excess=0.197%
   Raw/Executed turnover: raw_mean=45.536% | executed/raw=0.550

[RAND] Run 25/32 (Seed=25745):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -1.62%
   Annualized Return: -1.62%
   Sharpe: -0.1197
   Volatility (Ann.): 17.51%
   Max DD: 15.22%
   Turnover (episode): 25.31%
   Turnover (step): mean=25.310% | p95=37.156% | max=50.163%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.396%
   Raw/Executed turnover: raw_mean=46.018% | executed/raw=0.550

[RAND] Run 26/32 (Seed=25746):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -8.94%
   Annualized Return: -8.94%
   Sharpe: -0.5481
   Volatility (Ann.): 17.85%
   Max DD: 19.42%
   Turnover (episode): 25.69%
   Turnover (step): mean=25.686% | p95=39.222% | max=45.502%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.491%
   Raw/Executed turnover: raw_mean=46.701% | executed/raw=0.550

[RAND] Run 27/32 (Seed=25747):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -4.12%
   Annualized Return: -4.12%
   Sharpe: -0.2620
   Volatility (Ann.): 17.71%
   Max DD: 15.79%
   Turnover (episode): 25.15%
   Turnover (step): mean=25.155% | p95=36.562% | max=50.398%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.311%
   Raw/Executed turnover: raw_mean=45.736% | executed/raw=0.550

[RAND] Run 28/32 (Seed=25748):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -0.36%
   Annualized Return: -0.36%
   Sharpe: -0.0488
   Volatility (Ann.): 17.33%
   Max DD: 15.13%
   Turnover (episode): 25.37%
   Turnover (step): mean=25.366% | p95=36.080% | max=44.508%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.188%
   Raw/Executed turnover: raw_mean=46.121% | executed/raw=0.550

[RAND] Run 29/32 (Seed=25749):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -0.19%
   Annualized Return: -0.19%
   Sharpe: -0.0395
   Volatility (Ann.): 17.28%
   Max DD: 15.37%
   Turnover (episode): 25.57%
   Turnover (step): mean=25.574% | p95=37.219% | max=45.577%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.309%
   Raw/Executed turnover: raw_mean=46.499% | executed/raw=0.550

[RAND] Run 30/32 (Seed=25750):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -6.67%
   Annualized Return: -6.67%
   Sharpe: -0.4201
   Volatility (Ann.): 17.55%
   Max DD: 19.10%
   Turnover (episode): 26.29%
   Turnover (step): mean=26.287% | p95=38.628% | max=48.744%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.528%
   Raw/Executed turnover: raw_mean=47.795% | executed/raw=0.550

[RAND] Run 31/32 (Seed=25751):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.49%
   Annualized Return: -3.49%
   Sharpe: -0.2297
   Volatility (Ann.): 17.49%
   Max DD: 17.31%
   Turnover (episode): 25.66%
   Turnover (step): mean=25.663% | p95=36.122% | max=43.481%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.230%
   Raw/Executed turnover: raw_mean=46.660% | executed/raw=0.550

[RAND] Run 32/32 (Seed=25752):
   Start Date: 2021-07-06 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -3.90%
   Annualized Return: -3.90%
   Sharpe: -0.2505
   Volatility (Ann.): 17.63%
   Max DD: 16.27%
   Turnover (episode): 24.68%
   Turnover (step): mean=24.684% | p95=35.159% | max=54.880%
   Turnover vs target: target=35.000% | exceed_rate=5.6% | mean_excess=0.263%
   Raw/Executed turnover: raw_mean=44.879% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: -3.89%
   Std:  2.26%
   Min:  -8.94%
   Max:  -0.19%

Annualized Return (%):
   Mean: -3.89%
   Std:  2.26%
   Min:  -8.94%
   Max:  -0.19%

Sharpe Ratio (annualized):
   Mean: -0.2549
   Std:  0.1335
   Min:  -0.5481
   Max:  -0.0361

Volatility (Ann. %):
   Mean: +17.48%
   Std:  0.19%
   Min:  +17.12%
   Max:  +17.92%

Max Drawdown (%):
   Mean: 17.13%
   Std:  1.56%
   Min:  14.43%
   Max:  20.19%

Turnover (%):
   Mean: 25.45%
   Std:  0.47%

Turnover Step Detail (%):
   Mean(step mean): 25.455%
   Mean(step p95):  36.890%
   Mean(step max):  47.470%
   Mean exceed rate: 8.4%
   Mean excess over target: 0.306%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260329_235117.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs
      status=ok rows=32 copied=9
[RUN] fixed_252_year -> year_006 | bucket=2021 | start=2021-12-31 | h=252

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
   Start Date: 2021-12-31
   Market Regime: Post-Pandemic Rally (2021)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $86,318.57
   Total Return: -13.68%
   Annualized Return: -13.68%
   Sharpe Ratio: -0.7078 (annualized)
   Sortino Ratio: -0.9617 (annualized)
   Max Drawdown: 22.29%
   Volatility (Ann.): 20.65%
   Turnover: 4.10%
   Win Rate: 49.40%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=25846):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.42%
   Annualized Return: -19.42%
   Sharpe: -1.0625
   Volatility (Ann.): 20.32%
   Max DD: 24.54%
   Turnover (episode): 25.93%
   Turnover (step): mean=25.928% | p95=38.074% | max=44.847%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.323%
   Raw/Executed turnover: raw_mean=47.142% | executed/raw=0.550

[RAND] Run 2/32 (Seed=25847):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -22.26%
   Annualized Return: -22.26%
   Sharpe: -1.2437
   Volatility (Ann.): 20.26%
   Max DD: 26.05%
   Turnover (episode): 25.76%
   Turnover (step): mean=25.756% | p95=37.833% | max=48.361%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.385%
   Raw/Executed turnover: raw_mean=46.830% | executed/raw=0.550

[RAND] Run 3/32 (Seed=25848):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.42%
   Annualized Return: -19.42%
   Sharpe: -1.0616
   Volatility (Ann.): 20.33%
   Max DD: 24.47%
   Turnover (episode): 24.67%
   Turnover (step): mean=24.671% | p95=34.999% | max=45.326%
   Turnover vs target: target=35.000% | exceed_rate=5.2% | mean_excess=0.164%
   Raw/Executed turnover: raw_mean=44.857% | executed/raw=0.550

[RAND] Run 4/32 (Seed=25849):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -17.43%
   Annualized Return: -17.43%
   Sharpe: -0.8863
   Volatility (Ann.): 21.36%
   Max DD: 23.74%
   Turnover (episode): 25.99%
   Turnover (step): mean=25.990% | p95=37.215% | max=48.804%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.349%
   Raw/Executed turnover: raw_mean=47.254% | executed/raw=0.550

[RAND] Run 5/32 (Seed=25850):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -20.26%
   Annualized Return: -20.26%
   Sharpe: -1.0820
   Volatility (Ann.): 20.83%
   Max DD: 25.65%
   Turnover (episode): 26.46%
   Turnover (step): mean=26.458% | p95=38.504% | max=44.053%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.395%
   Raw/Executed turnover: raw_mean=48.106% | executed/raw=0.550

[RAND] Run 6/32 (Seed=25851):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -21.44%
   Annualized Return: -21.44%
   Sharpe: -1.1727
   Volatility (Ann.): 20.54%
   Max DD: 26.35%
   Turnover (episode): 25.65%
   Turnover (step): mean=25.652% | p95=36.579% | max=43.507%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.265%
   Raw/Executed turnover: raw_mean=46.639% | executed/raw=0.550

[RAND] Run 7/32 (Seed=25852):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.57%
   Annualized Return: -19.57%
   Sharpe: -1.0356
   Volatility (Ann.): 20.91%
   Max DD: 25.54%
   Turnover (episode): 25.35%
   Turnover (step): mean=25.349% | p95=37.496% | max=48.202%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.355%
   Raw/Executed turnover: raw_mean=46.088% | executed/raw=0.550

[RAND] Run 8/32 (Seed=25853):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.98%
   Annualized Return: -19.98%
   Sharpe: -1.0733
   Volatility (Ann.): 20.70%
   Max DD: 25.27%
   Turnover (episode): 25.35%
   Turnover (step): mean=25.353% | p95=35.703% | max=48.925%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.205%
   Raw/Executed turnover: raw_mean=46.097% | executed/raw=0.550

[RAND] Run 9/32 (Seed=25854):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.65%
   Annualized Return: -19.65%
   Sharpe: -1.0304
   Volatility (Ann.): 21.08%
   Max DD: 24.52%
   Turnover (episode): 26.29%
   Turnover (step): mean=26.289% | p95=39.107% | max=47.470%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.452%
   Raw/Executed turnover: raw_mean=47.798% | executed/raw=0.550

[RAND] Run 10/32 (Seed=25855):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -17.70%
   Annualized Return: -17.70%
   Sharpe: -0.9333
   Volatility (Ann.): 20.76%
   Max DD: 24.89%
   Turnover (episode): 25.52%
   Turnover (step): mean=25.521% | p95=36.351% | max=42.403%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.260%
   Raw/Executed turnover: raw_mean=46.401% | executed/raw=0.550

[RAND] Run 11/32 (Seed=25856):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.39%
   Annualized Return: -19.39%
   Sharpe: -1.0228
   Volatility (Ann.): 20.94%
   Max DD: 25.57%
   Turnover (episode): 25.84%
   Turnover (step): mean=25.838% | p95=38.416% | max=53.129%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.477%
   Raw/Executed turnover: raw_mean=46.978% | executed/raw=0.550

[RAND] Run 12/32 (Seed=25857):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.91%
   Annualized Return: -19.91%
   Sharpe: -1.0695
   Volatility (Ann.): 20.69%
   Max DD: 24.82%
   Turnover (episode): 25.85%
   Turnover (step): mean=25.852% | p95=36.986% | max=47.751%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.305%
   Raw/Executed turnover: raw_mean=47.003% | executed/raw=0.550

[RAND] Run 13/32 (Seed=25858):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -17.71%
   Annualized Return: -17.71%
   Sharpe: -0.9601
   Volatility (Ann.): 20.30%
   Max DD: 23.49%
   Turnover (episode): 25.68%
   Turnover (step): mean=25.679% | p95=35.882% | max=43.605%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.178%
   Raw/Executed turnover: raw_mean=46.690% | executed/raw=0.550

[RAND] Run 14/32 (Seed=25859):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -20.79%
   Annualized Return: -20.79%
   Sharpe: -1.1265
   Volatility (Ann.): 20.63%
   Max DD: 26.53%
   Turnover (episode): 25.74%
   Turnover (step): mean=25.741% | p95=37.174% | max=45.895%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.301%
   Raw/Executed turnover: raw_mean=46.801% | executed/raw=0.550

[RAND] Run 15/32 (Seed=25860):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -20.08%
   Annualized Return: -20.08%
   Sharpe: -1.0534
   Volatility (Ann.): 21.13%
   Max DD: 26.07%
   Turnover (episode): 26.92%
   Turnover (step): mean=26.916% | p95=38.578% | max=48.808%
   Turnover vs target: target=35.000% | exceed_rate=12.7% | mean_excess=0.459%
   Raw/Executed turnover: raw_mean=48.939% | executed/raw=0.550

[RAND] Run 16/32 (Seed=25861):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -17.45%
   Annualized Return: -17.45%
   Sharpe: -0.9488
   Volatility (Ann.): 20.22%
   Max DD: 23.42%
   Turnover (episode): 25.85%
   Turnover (step): mean=25.847% | p95=36.541% | max=46.224%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.271%
   Raw/Executed turnover: raw_mean=46.995% | executed/raw=0.550

[RAND] Run 17/32 (Seed=25862):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.98%
   Annualized Return: -19.98%
   Sharpe: -1.0440
   Volatility (Ann.): 21.18%
   Max DD: 25.26%
   Turnover (episode): 26.70%
   Turnover (step): mean=26.695% | p95=39.053% | max=48.436%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.508%
   Raw/Executed turnover: raw_mean=48.536% | executed/raw=0.550

[RAND] Run 18/32 (Seed=25863):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -18.52%
   Annualized Return: -18.52%
   Sharpe: -0.9982
   Volatility (Ann.): 20.47%
   Max DD: 23.57%
   Turnover (episode): 25.13%
   Turnover (step): mean=25.129% | p95=38.312% | max=47.620%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.359%
   Raw/Executed turnover: raw_mean=45.689% | executed/raw=0.550

[RAND] Run 19/32 (Seed=25864):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -20.08%
   Annualized Return: -20.08%
   Sharpe: -1.0612
   Volatility (Ann.): 21.00%
   Max DD: 26.52%
   Turnover (episode): 25.83%
   Turnover (step): mean=25.827% | p95=36.495% | max=47.996%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.292%
   Raw/Executed turnover: raw_mean=46.958% | executed/raw=0.550

[RAND] Run 20/32 (Seed=25865):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -25.15%
   Annualized Return: -25.15%
   Sharpe: -1.3781
   Volatility (Ann.): 20.94%
   Max DD: 28.51%
   Turnover (episode): 26.29%
   Turnover (step): mean=26.287% | p95=37.474% | max=49.115%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.437%
   Raw/Executed turnover: raw_mean=47.794% | executed/raw=0.550

[RAND] Run 21/32 (Seed=25866):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -21.25%
   Annualized Return: -21.25%
   Sharpe: -1.1283
   Volatility (Ann.): 21.04%
   Max DD: 25.10%
   Turnover (episode): 25.86%
   Turnover (step): mean=25.858% | p95=37.350% | max=48.014%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.315%
   Raw/Executed turnover: raw_mean=47.014% | executed/raw=0.550

[RAND] Run 22/32 (Seed=25867):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -24.76%
   Annualized Return: -24.76%
   Sharpe: -1.3618
   Volatility (Ann.): 20.82%
   Max DD: 28.67%
   Turnover (episode): 24.93%
   Turnover (step): mean=24.934% | p95=37.325% | max=48.638%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.309%
   Raw/Executed turnover: raw_mean=45.335% | executed/raw=0.550

[RAND] Run 23/32 (Seed=25868):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.39%
   Annualized Return: -19.39%
   Sharpe: -1.0350
   Volatility (Ann.): 20.74%
   Max DD: 25.11%
   Turnover (episode): 25.91%
   Turnover (step): mean=25.910% | p95=37.449% | max=43.978%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.295%
   Raw/Executed turnover: raw_mean=47.109% | executed/raw=0.550

[RAND] Run 24/32 (Seed=25869):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -20.08%
   Annualized Return: -20.08%
   Sharpe: -1.0819
   Volatility (Ann.): 20.65%
   Max DD: 25.14%
   Turnover (episode): 25.10%
   Turnover (step): mean=25.096% | p95=37.475% | max=41.194%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.263%
   Raw/Executed turnover: raw_mean=45.629% | executed/raw=0.550

[RAND] Run 25/32 (Seed=25870):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -21.58%
   Annualized Return: -21.58%
   Sharpe: -1.1403
   Volatility (Ann.): 21.17%
   Max DD: 26.87%
   Turnover (episode): 25.33%
   Turnover (step): mean=25.325% | p95=38.002% | max=46.725%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.329%
   Raw/Executed turnover: raw_mean=46.046% | executed/raw=0.550

[RAND] Run 26/32 (Seed=25871):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -18.04%
   Annualized Return: -18.04%
   Sharpe: -0.9749
   Volatility (Ann.): 20.39%
   Max DD: 24.45%
   Turnover (episode): 25.55%
   Turnover (step): mean=25.554% | p95=37.796% | max=46.483%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.367%
   Raw/Executed turnover: raw_mean=46.461% | executed/raw=0.550

[RAND] Run 27/32 (Seed=25872):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -22.08%
   Annualized Return: -22.08%
   Sharpe: -1.1978
   Volatility (Ann.): 20.76%
   Max DD: 26.17%
   Turnover (episode): 26.61%
   Turnover (step): mean=26.612% | p95=38.173% | max=48.131%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.431%
   Raw/Executed turnover: raw_mean=48.385% | executed/raw=0.550

[RAND] Run 28/32 (Seed=25873):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -21.82%
   Annualized Return: -21.82%
   Sharpe: -1.1859
   Volatility (Ann.): 20.70%
   Max DD: 26.26%
   Turnover (episode): 25.81%
   Turnover (step): mean=25.807% | p95=38.778% | max=48.242%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.445%
   Raw/Executed turnover: raw_mean=46.922% | executed/raw=0.550

[RAND] Run 29/32 (Seed=25874):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -25.01%
   Annualized Return: -25.01%
   Sharpe: -1.3655
   Volatility (Ann.): 20.99%
   Max DD: 30.10%
   Turnover (episode): 26.73%
   Turnover (step): mean=26.727% | p95=37.292% | max=46.528%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.398%
   Raw/Executed turnover: raw_mean=48.595% | executed/raw=0.550

[RAND] Run 30/32 (Seed=25875):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.25%
   Annualized Return: -19.25%
   Sharpe: -1.0517
   Volatility (Ann.): 20.33%
   Max DD: 24.36%
   Turnover (episode): 26.24%
   Turnover (step): mean=26.241% | p95=38.010% | max=45.902%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.350%
   Raw/Executed turnover: raw_mean=47.712% | executed/raw=0.550

[RAND] Run 31/32 (Seed=25876):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -21.29%
   Annualized Return: -21.29%
   Sharpe: -1.1371
   Volatility (Ann.): 20.94%
   Max DD: 26.31%
   Turnover (episode): 26.14%
   Turnover (step): mean=26.141% | p95=37.160% | max=48.689%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.294%
   Raw/Executed turnover: raw_mean=47.529% | executed/raw=0.550

[RAND] Run 32/32 (Seed=25877):
   Start Date: 2021-12-31 | Regime: Post-Pandemic Rally (2021)
   Days Traded: 252 (1.00 years)
   Total Return: -19.16%
   Annualized Return: -19.16%
   Sharpe: -1.0128
   Volatility (Ann.): 20.88%
   Max DD: 25.15%
   Turnover (episode): 25.28%
   Turnover (step): mean=25.277% | p95=35.647% | max=51.663%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.251%
   Raw/Executed turnover: raw_mean=45.958% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: -20.31%
   Std:  2.01%
   Min:  -25.15%
   Max:  -17.43%

Annualized Return (%):
   Mean: -20.31%
   Std:  2.01%
   Min:  -25.15%
   Max:  -17.43%

Sharpe Ratio (annualized):
   Mean: -1.0912
   Std:  0.1197
   Min:  -1.3781
   Max:  -0.8863

Volatility (Ann. %):
   Mean: +20.75%
   Std:  0.31%
   Min:  +20.22%
   Max:  +21.36%

Max Drawdown (%):
   Mean: 25.58%
   Std:  1.49%
   Min:  23.42%
   Max:  30.10%

Turnover (%):
   Mean: 25.82%
   Std:  0.54%

Turnover Step Detail (%):
   Mean(step mean): 25.821%
   Mean(step p95):  37.413%
   Mean(step max):  47.021%
   Mean exceed rate: 9.4%
   Mean excess over target: 0.337%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260330_002046.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs
      status=ok rows=32 copied=9
[RUN] fixed_252_year -> year_007 | bucket=2022 | start=2022-01-03 | h=252

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
   Start Date: 2022-01-03
   Market Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $82,167.05
   Total Return: -17.83%
   Annualized Return: -17.83%
   Sharpe Ratio: -0.9024 (annualized)
   Sortino Ratio: -1.2149 (annualized)
   Max Drawdown: 22.84%
   Volatility (Ann.): 21.48%
   Turnover: 4.25%
   Win Rate: 50.20%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=25847):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -20.89%
   Annualized Return: -20.89%
   Sharpe: -1.1121
   Volatility (Ann.): 20.96%
   Max DD: 24.08%
   Turnover (episode): 25.97%
   Turnover (step): mean=25.967% | p95=36.312% | max=45.891%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.274%
   Raw/Executed turnover: raw_mean=47.213% | executed/raw=0.550

[RAND] Run 2/32 (Seed=25848):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -19.95%
   Annualized Return: -19.95%
   Sharpe: -1.0561
   Volatility (Ann.): 20.94%
   Max DD: 24.54%
   Turnover (episode): 25.64%
   Turnover (step): mean=25.635% | p95=37.394% | max=46.599%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.330%
   Raw/Executed turnover: raw_mean=46.609% | executed/raw=0.550

[RAND] Run 3/32 (Seed=25849):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -16.90%
   Annualized Return: -16.90%
   Sharpe: -0.8919
   Volatility (Ann.): 20.66%
   Max DD: 21.92%
   Turnover (episode): 26.28%
   Turnover (step): mean=26.276% | p95=37.110% | max=46.066%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.414%
   Raw/Executed turnover: raw_mean=47.774% | executed/raw=0.550

[RAND] Run 4/32 (Seed=25850):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -22.31%
   Annualized Return: -22.31%
   Sharpe: -1.2169
   Volatility (Ann.): 20.69%
   Max DD: 26.31%
   Turnover (episode): 25.69%
   Turnover (step): mean=25.689% | p95=36.347% | max=54.785%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.328%
   Raw/Executed turnover: raw_mean=46.708% | executed/raw=0.550

[RAND] Run 5/32 (Seed=25851):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -28.20%
   Annualized Return: -28.20%
   Sharpe: -1.5873
   Volatility (Ann.): 20.82%
   Max DD: 31.32%
   Turnover (episode): 26.26%
   Turnover (step): mean=26.258% | p95=38.149% | max=44.651%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.388%
   Raw/Executed turnover: raw_mean=47.742% | executed/raw=0.550

[RAND] Run 6/32 (Seed=25852):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -21.44%
   Annualized Return: -21.44%
   Sharpe: -1.1490
   Volatility (Ann.): 20.90%
   Max DD: 26.70%
   Turnover (episode): 26.00%
   Turnover (step): mean=25.996% | p95=36.048% | max=50.642%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.349%
   Raw/Executed turnover: raw_mean=47.265% | executed/raw=0.550

[RAND] Run 7/32 (Seed=25853):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -19.08%
   Annualized Return: -19.08%
   Sharpe: -0.9875
   Volatility (Ann.): 21.25%
   Max DD: 24.07%
   Turnover (episode): 26.09%
   Turnover (step): mean=26.086% | p95=35.762% | max=43.713%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.216%
   Raw/Executed turnover: raw_mean=47.428% | executed/raw=0.550

[RAND] Run 8/32 (Seed=25854):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -21.44%
   Annualized Return: -21.44%
   Sharpe: -1.1542
   Volatility (Ann.): 20.82%
   Max DD: 25.49%
   Turnover (episode): 26.65%
   Turnover (step): mean=26.651% | p95=38.333% | max=49.261%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.440%
   Raw/Executed turnover: raw_mean=48.457% | executed/raw=0.550

[RAND] Run 9/32 (Seed=25855):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -18.90%
   Annualized Return: -18.90%
   Sharpe: -0.9974
   Volatility (Ann.): 20.88%
   Max DD: 23.54%
   Turnover (episode): 25.18%
   Turnover (step): mean=25.175% | p95=36.960% | max=49.714%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.305%
   Raw/Executed turnover: raw_mean=45.773% | executed/raw=0.550

[RAND] Run 10/32 (Seed=25856):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -19.91%
   Annualized Return: -19.91%
   Sharpe: -1.0807
   Volatility (Ann.): 20.51%
   Max DD: 24.62%
   Turnover (episode): 26.89%
   Turnover (step): mean=26.894% | p95=39.551% | max=50.724%
   Turnover vs target: target=35.000% | exceed_rate=13.9% | mean_excess=0.696%
   Raw/Executed turnover: raw_mean=48.898% | executed/raw=0.550

[RAND] Run 11/32 (Seed=25857):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -20.52%
   Annualized Return: -20.52%
   Sharpe: -1.1117
   Volatility (Ann.): 20.61%
   Max DD: 24.39%
   Turnover (episode): 25.75%
   Turnover (step): mean=25.750% | p95=37.301% | max=47.679%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.343%
   Raw/Executed turnover: raw_mean=46.817% | executed/raw=0.550

[RAND] Run 12/32 (Seed=25858):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -21.29%
   Annualized Return: -21.29%
   Sharpe: -1.1288
   Volatility (Ann.): 21.07%
   Max DD: 24.40%
   Turnover (episode): 25.76%
   Turnover (step): mean=25.757% | p95=37.716% | max=50.094%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.416%
   Raw/Executed turnover: raw_mean=46.831% | executed/raw=0.550

[RAND] Run 13/32 (Seed=25859):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -22.48%
   Annualized Return: -22.48%
   Sharpe: -1.2077
   Volatility (Ann.): 20.98%
   Max DD: 26.90%
   Turnover (episode): 26.52%
   Turnover (step): mean=26.518% | p95=38.148% | max=43.477%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.319%
   Raw/Executed turnover: raw_mean=48.215% | executed/raw=0.550

[RAND] Run 14/32 (Seed=25860):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -23.24%
   Annualized Return: -23.24%
   Sharpe: -1.2654
   Volatility (Ann.): 20.83%
   Max DD: 26.71%
   Turnover (episode): 25.63%
   Turnover (step): mean=25.634% | p95=35.561% | max=43.483%
   Turnover vs target: target=35.000% | exceed_rate=6.0% | mean_excess=0.224%
   Raw/Executed turnover: raw_mean=46.608% | executed/raw=0.550

[RAND] Run 15/32 (Seed=25861):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -18.20%
   Annualized Return: -18.20%
   Sharpe: -0.9637
   Volatility (Ann.): 20.75%
   Max DD: 22.21%
   Turnover (episode): 26.13%
   Turnover (step): mean=26.130% | p95=37.418% | max=51.787%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.365%
   Raw/Executed turnover: raw_mean=47.510% | executed/raw=0.550

[RAND] Run 16/32 (Seed=25862):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -24.25%
   Annualized Return: -24.25%
   Sharpe: -1.3297
   Volatility (Ann.): 20.82%
   Max DD: 26.28%
   Turnover (episode): 25.88%
   Turnover (step): mean=25.882% | p95=37.631% | max=46.449%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.336%
   Raw/Executed turnover: raw_mean=47.058% | executed/raw=0.550

[RAND] Run 17/32 (Seed=25863):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -20.62%
   Annualized Return: -20.62%
   Sharpe: -1.1110
   Volatility (Ann.): 20.71%
   Max DD: 22.89%
   Turnover (episode): 25.73%
   Turnover (step): mean=25.727% | p95=36.869% | max=49.389%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.268%
   Raw/Executed turnover: raw_mean=46.777% | executed/raw=0.550

[RAND] Run 18/32 (Seed=25864):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -21.78%
   Annualized Return: -21.78%
   Sharpe: -1.1810
   Volatility (Ann.): 20.73%
   Max DD: 26.56%
   Turnover (episode): 25.78%
   Turnover (step): mean=25.781% | p95=37.023% | max=50.035%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.410%
   Raw/Executed turnover: raw_mean=46.874% | executed/raw=0.550

[RAND] Run 19/32 (Seed=25865):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -19.51%
   Annualized Return: -19.51%
   Sharpe: -1.0229
   Volatility (Ann.): 21.06%
   Max DD: 23.22%
   Turnover (episode): 25.29%
   Turnover (step): mean=25.286% | p95=36.593% | max=44.415%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.222%
   Raw/Executed turnover: raw_mean=45.974% | executed/raw=0.550

[RAND] Run 20/32 (Seed=25866):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -24.70%
   Annualized Return: -24.70%
   Sharpe: -1.3407
   Volatility (Ann.): 21.06%
   Max DD: 29.59%
   Turnover (episode): 26.13%
   Turnover (step): mean=26.125% | p95=36.499% | max=43.596%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.234%
   Raw/Executed turnover: raw_mean=47.501% | executed/raw=0.550

[RAND] Run 21/32 (Seed=25867):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -20.51%
   Annualized Return: -20.51%
   Sharpe: -1.1060
   Volatility (Ann.): 20.68%
   Max DD: 24.09%
   Turnover (episode): 25.78%
   Turnover (step): mean=25.775% | p95=36.912% | max=47.381%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.270%
   Raw/Executed turnover: raw_mean=46.864% | executed/raw=0.550

[RAND] Run 22/32 (Seed=25868):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -18.99%
   Annualized Return: -18.99%
   Sharpe: -0.9931
   Volatility (Ann.): 21.05%
   Max DD: 23.11%
   Turnover (episode): 26.13%
   Turnover (step): mean=26.132% | p95=36.416% | max=47.046%
   Turnover vs target: target=35.000% | exceed_rate=7.6% | mean_excess=0.323%
   Raw/Executed turnover: raw_mean=47.514% | executed/raw=0.550

[RAND] Run 23/32 (Seed=25869):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -22.02%
   Annualized Return: -22.02%
   Sharpe: -1.1874
   Volatility (Ann.): 20.86%
   Max DD: 25.62%
   Turnover (episode): 26.63%
   Turnover (step): mean=26.628% | p95=38.464% | max=48.355%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.474%
   Raw/Executed turnover: raw_mean=48.415% | executed/raw=0.550

[RAND] Run 24/32 (Seed=25870):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -23.61%
   Annualized Return: -23.61%
   Sharpe: -1.3071
   Volatility (Ann.): 20.57%
   Max DD: 25.95%
   Turnover (episode): 25.98%
   Turnover (step): mean=25.975% | p95=37.456% | max=43.454%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.331%
   Raw/Executed turnover: raw_mean=47.227% | executed/raw=0.550

[RAND] Run 25/32 (Seed=25871):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -18.46%
   Annualized Return: -18.46%
   Sharpe: -0.9746
   Volatility (Ann.): 20.82%
   Max DD: 23.10%
   Turnover (episode): 25.41%
   Turnover (step): mean=25.415% | p95=38.237% | max=45.355%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.371%
   Raw/Executed turnover: raw_mean=46.209% | executed/raw=0.550

[RAND] Run 26/32 (Seed=25872):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -22.62%
   Annualized Return: -22.62%
   Sharpe: -1.2524
   Volatility (Ann.): 20.46%
   Max DD: 26.84%
   Turnover (episode): 25.89%
   Turnover (step): mean=25.891% | p95=36.537% | max=43.880%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.213%
   Raw/Executed turnover: raw_mean=47.075% | executed/raw=0.550

[RAND] Run 27/32 (Seed=25873):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -18.61%
   Annualized Return: -18.61%
   Sharpe: -0.9973
   Volatility (Ann.): 20.59%
   Max DD: 24.21%
   Turnover (episode): 26.18%
   Turnover (step): mean=26.176% | p95=37.528% | max=43.841%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.294%
   Raw/Executed turnover: raw_mean=47.592% | executed/raw=0.550

[RAND] Run 28/32 (Seed=25874):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -21.10%
   Annualized Return: -21.10%
   Sharpe: -1.1412
   Volatility (Ann.): 20.71%
   Max DD: 25.53%
   Turnover (episode): 25.09%
   Turnover (step): mean=25.094% | p95=36.714% | max=45.430%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.281%
   Raw/Executed turnover: raw_mean=45.626% | executed/raw=0.550

[RAND] Run 29/32 (Seed=25875):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -18.71%
   Annualized Return: -18.71%
   Sharpe: -0.9796
   Volatility (Ann.): 20.99%
   Max DD: 25.08%
   Turnover (episode): 25.32%
   Turnover (step): mean=25.320% | p95=36.334% | max=42.384%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.234%
   Raw/Executed turnover: raw_mean=46.036% | executed/raw=0.550

[RAND] Run 30/32 (Seed=25876):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -19.21%
   Annualized Return: -19.21%
   Sharpe: -1.0295
   Volatility (Ann.): 20.65%
   Max DD: 25.33%
   Turnover (episode): 25.69%
   Turnover (step): mean=25.685% | p95=36.907% | max=47.118%
   Turnover vs target: target=35.000% | exceed_rate=8.0% | mean_excess=0.307%
   Raw/Executed turnover: raw_mean=46.700% | executed/raw=0.550

[RAND] Run 31/32 (Seed=25877):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -25.23%
   Annualized Return: -25.23%
   Sharpe: -1.4104
   Volatility (Ann.): 20.59%
   Max DD: 27.33%
   Turnover (episode): 25.98%
   Turnover (step): mean=25.984% | p95=37.951% | max=49.309%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.452%
   Raw/Executed turnover: raw_mean=47.243% | executed/raw=0.550

[RAND] Run 32/32 (Seed=25878):
   Start Date: 2022-01-03 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: -19.20%
   Annualized Return: -19.20%
   Sharpe: -1.0336
   Volatility (Ann.): 20.57%
   Max DD: 22.73%
   Turnover (episode): 25.56%
   Turnover (step): mean=25.564% | p95=36.247% | max=46.121%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.287%
   Raw/Executed turnover: raw_mean=46.480% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: -21.06%
   Std:  2.41%
   Min:  -28.20%
   Max:  -16.90%

Annualized Return (%):
   Mean: -21.06%
   Std:  2.41%
   Min:  -28.20%
   Max:  -16.90%

Sharpe Ratio (annualized):
   Mean: -1.1346
   Std:  0.1505
   Min:  -1.5873
   Max:  -0.8919

Volatility (Ann. %):
   Mean: +20.80%
   Std:  0.19%
   Min:  +20.46%
   Max:  +21.25%

Max Drawdown (%):
   Mean: 25.15%
   Std:  2.05%
   Min:  21.92%
   Max:  31.32%

Turnover (%):
   Mean: 25.90%
   Std:  0.43%

Turnover Step Detail (%):
   Mean(step mean): 25.902%
   Mean(step p95):  37.138%
   Mean(step max):  46.941%
   Mean exceed rate: 9.3%
   Mean excess over target: 0.335%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260330_005019.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs
      status=ok rows=32 copied=9
[RUN] fixed_252_year -> year_008 | bucket=2022 | start=2022-07-05 | h=252

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
   Start Date: 2022-07-05
   Market Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $136,380.13
   Total Return: +36.38%
   Annualized Return: +36.38%
   Sharpe Ratio: 1.4493 (annualized)
   Sortino Ratio: 2.2477 (annualized)
   Max Drawdown: 20.16%
   Volatility (Ann.): 21.77%
   Turnover: 3.63%
   Win Rate: 51.79%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=6

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=25972):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +30.43%
   Annualized Return: +30.43%
   Sharpe: 1.2041
   Volatility (Ann.): 22.63%
   Max DD: 22.22%
   Turnover (episode): 26.17%
   Turnover (step): mean=26.166% | p95=39.018% | max=47.949%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.474%
   Raw/Executed turnover: raw_mean=47.575% | executed/raw=0.550

[RAND] Run 2/32 (Seed=25973):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +34.02%
   Annualized Return: +34.02%
   Sharpe: 1.3416
   Volatility (Ann.): 22.29%
   Max DD: 21.73%
   Turnover (episode): 26.60%
   Turnover (step): mean=26.602% | p95=38.050% | max=46.991%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.450%
   Raw/Executed turnover: raw_mean=48.367% | executed/raw=0.550

[RAND] Run 3/32 (Seed=25974):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +36.68%
   Annualized Return: +36.68%
   Sharpe: 1.4186
   Volatility (Ann.): 22.50%
   Max DD: 20.80%
   Turnover (episode): 26.26%
   Turnover (step): mean=26.259% | p95=38.281% | max=45.456%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.421%
   Raw/Executed turnover: raw_mean=47.743% | executed/raw=0.550

[RAND] Run 4/32 (Seed=25975):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +32.26%
   Annualized Return: +32.26%
   Sharpe: 1.2900
   Volatility (Ann.): 22.12%
   Max DD: 21.78%
   Turnover (episode): 26.50%
   Turnover (step): mean=26.496% | p95=37.713% | max=44.279%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.401%
   Raw/Executed turnover: raw_mean=48.174% | executed/raw=0.550

[RAND] Run 5/32 (Seed=25976):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +33.71%
   Annualized Return: +33.71%
   Sharpe: 1.3388
   Volatility (Ann.): 22.14%
   Max DD: 20.03%
   Turnover (episode): 25.97%
   Turnover (step): mean=25.971% | p95=36.558% | max=49.524%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.358%
   Raw/Executed turnover: raw_mean=47.221% | executed/raw=0.550

[RAND] Run 6/32 (Seed=25977):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +40.71%
   Annualized Return: +40.71%
   Sharpe: 1.5208
   Volatility (Ann.): 22.98%
   Max DD: 20.98%
   Turnover (episode): 25.54%
   Turnover (step): mean=25.537% | p95=37.753% | max=45.201%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.294%
   Raw/Executed turnover: raw_mean=46.431% | executed/raw=0.550

[RAND] Run 7/32 (Seed=25978):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +33.38%
   Annualized Return: +33.38%
   Sharpe: 1.3197
   Volatility (Ann.): 22.30%
   Max DD: 21.47%
   Turnover (episode): 25.40%
   Turnover (step): mean=25.401% | p95=36.869% | max=48.285%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.337%
   Raw/Executed turnover: raw_mean=46.183% | executed/raw=0.550

[RAND] Run 8/32 (Seed=25979):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +37.62%
   Annualized Return: +37.62%
   Sharpe: 1.4634
   Volatility (Ann.): 22.24%
   Max DD: 21.10%
   Turnover (episode): 25.98%
   Turnover (step): mean=25.983% | p95=36.227% | max=48.669%
   Turnover vs target: target=35.000% | exceed_rate=6.8% | mean_excess=0.329%
   Raw/Executed turnover: raw_mean=47.243% | executed/raw=0.550

[RAND] Run 9/32 (Seed=25980):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +33.04%
   Annualized Return: +33.04%
   Sharpe: 1.3068
   Volatility (Ann.): 22.33%
   Max DD: 22.16%
   Turnover (episode): 25.72%
   Turnover (step): mean=25.718% | p95=38.223% | max=46.203%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.350%
   Raw/Executed turnover: raw_mean=46.761% | executed/raw=0.550

[RAND] Run 10/32 (Seed=25981):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +36.41%
   Annualized Return: +36.41%
   Sharpe: 1.4040
   Volatility (Ann.): 22.62%
   Max DD: 20.72%
   Turnover (episode): 26.43%
   Turnover (step): mean=26.430% | p95=36.323% | max=43.818%
   Turnover vs target: target=35.000% | exceed_rate=10.4% | mean_excess=0.248%
   Raw/Executed turnover: raw_mean=48.054% | executed/raw=0.550

[RAND] Run 11/32 (Seed=25982):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +36.29%
   Annualized Return: +36.29%
   Sharpe: 1.4256
   Volatility (Ann.): 22.14%
   Max DD: 20.96%
   Turnover (episode): 26.15%
   Turnover (step): mean=26.149% | p95=38.644% | max=49.391%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.414%
   Raw/Executed turnover: raw_mean=47.543% | executed/raw=0.550

[RAND] Run 12/32 (Seed=25983):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +36.59%
   Annualized Return: +36.59%
   Sharpe: 1.4281
   Volatility (Ann.): 22.27%
   Max DD: 20.80%
   Turnover (episode): 25.89%
   Turnover (step): mean=25.887% | p95=37.131% | max=45.727%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.288%
   Raw/Executed turnover: raw_mean=47.067% | executed/raw=0.550

[RAND] Run 13/32 (Seed=25984):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +41.63%
   Annualized Return: +41.63%
   Sharpe: 1.5923
   Volatility (Ann.): 22.26%
   Max DD: 19.15%
   Turnover (episode): 25.72%
   Turnover (step): mean=25.718% | p95=37.405% | max=47.498%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.346%
   Raw/Executed turnover: raw_mean=46.761% | executed/raw=0.550

[RAND] Run 14/32 (Seed=25985):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +33.96%
   Annualized Return: +33.96%
   Sharpe: 1.3273
   Volatility (Ann.): 22.53%
   Max DD: 22.11%
   Turnover (episode): 25.85%
   Turnover (step): mean=25.850% | p95=37.611% | max=48.289%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.339%
   Raw/Executed turnover: raw_mean=47.000% | executed/raw=0.550

[RAND] Run 15/32 (Seed=25986):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +33.92%
   Annualized Return: +33.92%
   Sharpe: 1.3113
   Volatility (Ann.): 22.84%
   Max DD: 21.73%
   Turnover (episode): 25.66%
   Turnover (step): mean=25.660% | p95=35.899% | max=45.759%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.213%
   Raw/Executed turnover: raw_mean=46.654% | executed/raw=0.550

[RAND] Run 16/32 (Seed=25987):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +29.33%
   Annualized Return: +29.33%
   Sharpe: 1.1775
   Volatility (Ann.): 22.37%
   Max DD: 22.62%
   Turnover (episode): 26.25%
   Turnover (step): mean=26.254% | p95=37.293% | max=45.745%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.337%
   Raw/Executed turnover: raw_mean=47.735% | executed/raw=0.550

[RAND] Run 17/32 (Seed=25988):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +34.21%
   Annualized Return: +34.21%
   Sharpe: 1.3310
   Volatility (Ann.): 22.63%
   Max DD: 20.75%
   Turnover (episode): 26.13%
   Turnover (step): mean=26.126% | p95=37.793% | max=44.510%
   Turnover vs target: target=35.000% | exceed_rate=12.4% | mean_excess=0.398%
   Raw/Executed turnover: raw_mean=47.502% | executed/raw=0.550

[RAND] Run 18/32 (Seed=25989):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +30.78%
   Annualized Return: +30.78%
   Sharpe: 1.2380
   Volatility (Ann.): 22.15%
   Max DD: 21.75%
   Turnover (episode): 25.71%
   Turnover (step): mean=25.708% | p95=37.192% | max=49.985%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.405%
   Raw/Executed turnover: raw_mean=46.743% | executed/raw=0.550

[RAND] Run 19/32 (Seed=25990):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +33.31%
   Annualized Return: +33.31%
   Sharpe: 1.3181
   Volatility (Ann.): 22.28%
   Max DD: 20.93%
   Turnover (episode): 26.18%
   Turnover (step): mean=26.180% | p95=37.172% | max=50.869%
   Turnover vs target: target=35.000% | exceed_rate=11.2% | mean_excess=0.380%
   Raw/Executed turnover: raw_mean=47.600% | executed/raw=0.550

[RAND] Run 20/32 (Seed=25991):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +32.57%
   Annualized Return: +32.57%
   Sharpe: 1.2916
   Volatility (Ann.): 22.31%
   Max DD: 22.31%
   Turnover (episode): 26.34%
   Turnover (step): mean=26.341% | p95=37.438% | max=46.091%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.354%
   Raw/Executed turnover: raw_mean=47.893% | executed/raw=0.550

[RAND] Run 21/32 (Seed=25992):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +29.11%
   Annualized Return: +29.11%
   Sharpe: 1.1858
   Volatility (Ann.): 22.00%
   Max DD: 21.17%
   Turnover (episode): 26.41%
   Turnover (step): mean=26.414% | p95=38.288% | max=48.289%
   Turnover vs target: target=35.000% | exceed_rate=12.0% | mean_excess=0.466%
   Raw/Executed turnover: raw_mean=48.025% | executed/raw=0.550

[RAND] Run 22/32 (Seed=25993):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +41.27%
   Annualized Return: +41.27%
   Sharpe: 1.5650
   Volatility (Ann.): 22.52%
   Max DD: 21.18%
   Turnover (episode): 26.36%
   Turnover (step): mean=26.363% | p95=38.724% | max=47.013%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.384%
   Raw/Executed turnover: raw_mean=47.933% | executed/raw=0.550

[RAND] Run 23/32 (Seed=25994):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +27.50%
   Annualized Return: +27.50%
   Sharpe: 1.1211
   Volatility (Ann.): 22.19%
   Max DD: 20.48%
   Turnover (episode): 26.33%
   Turnover (step): mean=26.333% | p95=38.913% | max=44.079%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.402%
   Raw/Executed turnover: raw_mean=47.878% | executed/raw=0.550

[RAND] Run 24/32 (Seed=25995):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +35.47%
   Annualized Return: +35.47%
   Sharpe: 1.3918
   Volatility (Ann.): 22.26%
   Max DD: 21.72%
   Turnover (episode): 26.25%
   Turnover (step): mean=26.247% | p95=37.843% | max=50.875%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.393%
   Raw/Executed turnover: raw_mean=47.723% | executed/raw=0.550

[RAND] Run 25/32 (Seed=25996):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +36.57%
   Annualized Return: +36.57%
   Sharpe: 1.4102
   Volatility (Ann.): 22.60%
   Max DD: 20.50%
   Turnover (episode): 27.11%
   Turnover (step): mean=27.115% | p95=38.005% | max=50.175%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.473%
   Raw/Executed turnover: raw_mean=49.300% | executed/raw=0.550

[RAND] Run 26/32 (Seed=25997):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +33.69%
   Annualized Return: +33.69%
   Sharpe: 1.3216
   Volatility (Ann.): 22.47%
   Max DD: 21.65%
   Turnover (episode): 26.02%
   Turnover (step): mean=26.021% | p95=37.838% | max=45.188%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.409%
   Raw/Executed turnover: raw_mean=47.311% | executed/raw=0.550

[RAND] Run 27/32 (Seed=25998):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +29.54%
   Annualized Return: +29.54%
   Sharpe: 1.1826
   Volatility (Ann.): 22.42%
   Max DD: 21.58%
   Turnover (episode): 26.65%
   Turnover (step): mean=26.651% | p95=37.810% | max=47.967%
   Turnover vs target: target=35.000% | exceed_rate=11.6% | mean_excess=0.339%
   Raw/Executed turnover: raw_mean=48.457% | executed/raw=0.550

[RAND] Run 28/32 (Seed=25999):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +31.62%
   Annualized Return: +31.62%
   Sharpe: 1.2461
   Volatility (Ann.): 22.60%
   Max DD: 21.75%
   Turnover (episode): 25.92%
   Turnover (step): mean=25.925% | p95=36.167% | max=43.112%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.204%
   Raw/Executed turnover: raw_mean=47.136% | executed/raw=0.550

[RAND] Run 29/32 (Seed=26000):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +33.88%
   Annualized Return: +33.88%
   Sharpe: 1.3484
   Volatility (Ann.): 22.06%
   Max DD: 20.52%
   Turnover (episode): 25.67%
   Turnover (step): mean=25.668% | p95=35.447% | max=45.451%
   Turnover vs target: target=35.000% | exceed_rate=6.4% | mean_excess=0.246%
   Raw/Executed turnover: raw_mean=46.669% | executed/raw=0.550

[RAND] Run 30/32 (Seed=26001):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +28.84%
   Annualized Return: +28.84%
   Sharpe: 1.1539
   Volatility (Ann.): 22.53%
   Max DD: 22.54%
   Turnover (episode): 26.10%
   Turnover (step): mean=26.095% | p95=36.788% | max=46.215%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.271%
   Raw/Executed turnover: raw_mean=47.446% | executed/raw=0.550

[RAND] Run 31/32 (Seed=26002):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +32.56%
   Annualized Return: +32.56%
   Sharpe: 1.2954
   Volatility (Ann.): 22.23%
   Max DD: 22.31%
   Turnover (episode): 26.71%
   Turnover (step): mean=26.712% | p95=38.580% | max=48.111%
   Turnover vs target: target=35.000% | exceed_rate=10.8% | mean_excess=0.415%
   Raw/Executed turnover: raw_mean=48.568% | executed/raw=0.550

[RAND] Run 32/32 (Seed=26003):
   Start Date: 2022-07-05 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +35.06%
   Annualized Return: +35.06%
   Sharpe: 1.3681
   Volatility (Ann.): 22.45%
   Max DD: 20.07%
   Turnover (episode): 25.94%
   Turnover (step): mean=25.936% | p95=37.100% | max=46.791%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.316%
   Raw/Executed turnover: raw_mean=47.157% | executed/raw=0.550

================================================================================
SUMMARY: STOCHASTIC EVALUATION STATISTICS
================================================================================

Total Return (%):
   Mean: +33.94%
   Std:  3.48%
   Min:  +27.50%
   Max:  +41.63%

Annualized Return (%):
   Mean: +33.94%
   Std:  3.48%
   Min:  +27.50%
   Max:  +41.63%

Sharpe Ratio (annualized):
   Mean: 1.3325
   Std:  0.1135
   Min:  1.1211
   Max:  1.5923

Volatility (Ann. %):
   Mean: +22.38%
   Std:  0.23%
   Min:  +22.00%
   Max:  +22.98%

Max Drawdown (%):
   Mean: 21.30%
   Std:  0.81%
   Min:  19.15%
   Max:  22.62%

Turnover (%):
   Mean: 26.12%
   Std:  0.38%

Turnover Step Detail (%):
   Mean(step mean): 26.122%
   Mean(step p95):  37.503%
   Mean(step max):  46.985%
   Mean exceed rate: 9.8%
   Mean excess over target: 0.358%
   Mean executed/raw ratio: 0.550

💾 Evaluation results saved: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs/exp6_custom_eval_20260330_012004.csv
💾 Per-track artifacts saved in: /content/eval_restore/tcn_fusion_results/high_watermark_checkpoints_run21/logs
      status=ok rows=32 copied=9
[RUN] fixed_252_year -> year_009 | bucket=2022 | start=2022-12-30 | h=252

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
   Market Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Episode Length: 252 days (1.00 years)
   Final Portfolio Value: $140,027.28
   Total Return: +40.03%
   Annualized Return: +40.03%
   Sharpe Ratio: 2.3029 (annualized)
   Sortino Ratio: 4.1629 (annualized)
   Max Drawdown: 7.05%
   Volatility (Ann.): 14.26%
   Turnover: 2.70%
   Win Rate: 52.19%
   Diagnostics: action_uniques=252, alpha<=1 frac=0.000, argmax_alpha_uniques=4

================================================================================
STOCHASTIC EVALUATIONS (Random Start = False, 32 Runs)
================================================================================

[RAND] Run 1/32 (Seed=26097):
   Start Date: 2022-12-30 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +40.60%
   Annualized Return: +40.60%
   Sharpe: 2.0622
   Volatility (Ann.): 16.28%
   Max DD: 7.69%
   Turnover (episode): 26.17%
   Turnover (step): mean=26.175% | p95=37.288% | max=51.241%
   Turnover vs target: target=35.000% | exceed_rate=10.0% | mean_excess=0.309%
   Raw/Executed turnover: raw_mean=47.591% | executed/raw=0.550

[RAND] Run 2/32 (Seed=26098):
   Start Date: 2022-12-30 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +43.97%
   Annualized Return: +43.97%
   Sharpe: 2.1946
   Volatility (Ann.): 16.39%
   Max DD: 7.13%
   Turnover (episode): 25.73%
   Turnover (step): mean=25.727% | p95=38.125% | max=46.724%
   Turnover vs target: target=35.000% | exceed_rate=9.2% | mean_excess=0.408%
   Raw/Executed turnover: raw_mean=46.777% | executed/raw=0.550

[RAND] Run 3/32 (Seed=26099):
   Start Date: 2022-12-30 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +39.11%
   Annualized Return: +39.11%
   Sharpe: 1.9687
   Volatility (Ann.): 16.53%
   Max DD: 7.03%
   Turnover (episode): 26.25%
   Turnover (step): mean=26.248% | p95=38.277% | max=49.567%
   Turnover vs target: target=35.000% | exceed_rate=9.6% | mean_excess=0.385%
   Raw/Executed turnover: raw_mean=47.723% | executed/raw=0.550

[RAND] Run 4/32 (Seed=26100):
   Start Date: 2022-12-30 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +46.64%
   Annualized Return: +46.64%
   Sharpe: 2.3295
   Volatility (Ann.): 16.22%
   Max DD: 7.15%
   Turnover (episode): 26.30%
   Turnover (step): mean=26.304% | p95=36.476% | max=46.085%
   Turnover vs target: target=35.000% | exceed_rate=7.2% | mean_excess=0.251%
   Raw/Executed turnover: raw_mean=47.826% | executed/raw=0.550

[RAND] Run 5/32 (Seed=26101):
   Start Date: 2022-12-30 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +43.02%
   Annualized Return: +43.02%
   Sharpe: 2.1569
   Volatility (Ann.): 16.36%
   Max DD: 6.51%
   Turnover (episode): 26.15%
   Turnover (step): mean=26.151% | p95=36.058% | max=43.795%
   Turnover vs target: target=35.000% | exceed_rate=8.4% | mean_excess=0.241%
   Raw/Executed turnover: raw_mean=47.547% | executed/raw=0.550

[RAND] Run 6/32 (Seed=26102):
   Start Date: 2022-12-30 | Regime: Inflation Shock / Fed Tightening (2022 to 2023-07-26)
   Days Traded: 252 (1.00 years)
   Total Return: +42.91%
   Annualized Return: +42.91%
   Sharpe: 2.1664
   Volatility (Ann.): 16.25%
   Max DD: 7.34%
   Turnover (episode): 26.36%
   Turnover (step): mean=26.356% | p95=37.725% | max=48.410%
   Turnover vs target: target=35.000% | exceed_rate=8.8% | mean_excess=0.344%
   Raw/Executed turnover: raw_mean=47.920% | executed/raw=0.550
