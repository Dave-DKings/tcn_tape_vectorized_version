# Long-Horizon Upgrade Implementation Walkthrough

This note documents the full implementation of five configurable upgrades for the TCN+PPO portfolio system:

1. Multi-horizon robust checkpoint selection
2. Adaptive CVaR-constrained PPO auxiliary
3. Recurrent memory (LSTM) in actor/critic paths
4. Regime-aware policy/value conditioning
5. Distributional critic (quantile outputs)

All upgrades are behind flags so the baseline model can be restored by setting toggles to `False`.

## 1) Multi-Horizon Checkpoint Selection

### What was added
Training-side deterministic validation now supports multi-horizon scoring and optional stochastic sanity gating.

### Math
For each horizon \(h \in H\):

- Deterministic validation Sharpe: \(S_h\)
- Deterministic max drawdown (absolute): \(D_h\)
- Horizon score:
\[
q_h = S_h - \lambda_{DD} D_h
\]
where \(\lambda_{DD} \ge 0\) is configurable.

Composite selection score:
\[
Q = \sum_{h \in H} w_h q_h, \quad \sum_h w_h = 1,\; w_h \ge 0
\]

Checkpoint save criteria:
1. Primary-horizon Sharpe \(S_{primary} \ge S_{min}\)
2. Composite score improvement:
\[
Q > Q_{best} + \Delta_{min}
\]
3. If stochastic sanity gate is enabled, pass:
\[
\bar S_{sto} \ge S_{sto,min}, \quad \sigma_{sto} \le \sigma_{sto,max}
\]

### Numeric example
Horizons: \([252, 504, 756, 1008]\), weights \([0.35, 0.30, 0.20, 0.15]\), \(\lambda_{DD}=0.25\)

Suppose:
- \(S=[1.10, 0.95, 0.90, 0.88]\)
- \(D=[0.08, 0.10, 0.11, 0.12]\)

Then:
- \(q_{252}=1.10-0.25\cdot0.08=1.08\)
- \(q_{504}=0.95-0.25\cdot0.10=0.925\)
- \(q_{756}=0.90-0.25\cdot0.11=0.8725\)
- \(q_{1008}=0.88-0.25\cdot0.12=0.85\)

Composite:
\[
Q=0.35(1.08)+0.30(0.925)+0.20(0.8725)+0.15(0.85)=0.958
\]

If current best is \(Q_{best}=0.950\) and \(\Delta_{min}=0.005\), this checkpoint qualifies (assuming gate pass).

## 2) Adaptive CVaR Auxiliary in PPO

### What was added
The actor risk auxiliary already supported CVaR proxy penalty. It now supports adaptive coefficient control.

Actor auxiliary total:
\[
L_{aux}=L_{sharpe}+L_{mvo}+L_{cvar}
\]
with:
\[
L_{cvar}=\lambda_{cvar}\cdot \text{CVaR}_{\alpha}(\ell),\quad \ell=-r_p
\]
where \(r_p\) is proxy portfolio return per sample.

Tail proxy used in implementation:
- Sort losses descending
- Take top \(\lceil \alpha N \rceil\)
- Average them

Adaptive coefficient update:
\[
\lambda_{cvar}^{t+1}=\text{clip}\Big(\lambda_{cvar}^{t}+\eta\big(\widehat{\text{CVaR}}_{\alpha}^{t}-c_{target}\big),\; \lambda_{min},\lambda_{max}\Big)
\]

### Numeric example
Let:
- Current \(\lambda_{cvar}=0.010\)
- Target \(c_{target}=0.020\)
- Observed \(\widehat{CVaR}=0.035\)
- Adapt rate \(\eta=0.05\)

Update:
\[
\lambda' = 0.010 + 0.05(0.035-0.020)=0.01075
\]
If bounds are \([0, 0.05]\), new \(\lambda_{cvar}=0.01075\).

## 3) Recurrent Memory (LSTM)

### What was added
Optional LSTM layers were inserted in actor and critic sequence pathways.

- `TCNActor`: TCN blocks -> optional LSTM -> pooling
- `TCNAttentionActor`: TCN -> projection -> attention -> optional LSTM -> pooling
- `TCNFusionActor`: per-asset TCN -> optional asset LSTM; context branch -> optional global LSTM
- Same pattern mirrored in critic classes

### Effect
This allows temporal state persistence beyond pure convolutional receptive aggregation and helps with regime persistence patterns.

## 4) Regime-Aware Conditioning

### What was added
Optional regime summary features are computed from sequence tensor \(X \in \mathbb{R}^{B\times T\times F}\):

\[
\mu = \text{mean}(X),\;
\sigma = \text{std}(X),\;
\tau = \text{mean}(X_{T}) - \text{mean}(X_{1}),\;
\delta = \text{mean}(|X_{t}-X_{t-1}|),\;
\nu = \text{mean}(|X|)
\]

Regime vector:
\[
z=[\mu,\sigma,\tau,\delta,\nu] \in \mathbb{R}^{5}
\]

Then:
\[
e=\phi(z)\quad\text{(MLP)}
\]
\[
h'=\psi([h,e])
\]
where \(h\) is the pooled latent and \(\psi\) is a fusion dense layer.

### Numeric example
If sequence summary gives:
- \(\mu=0.002\), \(\sigma=0.018\), \(\tau=-0.004\), \(\delta=0.011\), \(\nu=0.013\)
then \(z=[0.002,0.018,-0.004,0.011,0.013]\), embedded and fused into actor/critic latent before output head.

## 5) Distributional Critic (Quantile)

### What was added
Critic heads can output \(N_q\) quantiles instead of a scalar:
\[
Z_\theta(s) = [q_1(s),\dots,q_{N_q}(s)]
\]

Scalar value used for rollout/GAE remains mean quantile:
\[
V(s)=\frac{1}{N_q}\sum_i q_i(s)
\]

Training loss (normalized targets) uses quantile Huber:
\[
L_Q = \mathbb{E}_{i}\left[\left|\tau_i - \mathbb{1}_{\delta_i<0}\right|\cdot \mathcal{H}_\kappa(\delta_i)\right],
\quad \delta_i = y - q_i
\]

with anchor term:
\[
L_{critic}=L_Q + \beta\cdot \text{MSE}(y,\bar q)
\]
where \(\bar q\) is mean quantile and \(\beta\) is configurable.

### Numeric example
Let target normalized return \(y=0.40\), predicted quantiles
\([0.10, 0.20, 0.35, 0.55, 0.80]\).
Then residuals are
\([0.30, 0.20, 0.05, -0.15, -0.40]\), each weighted by quantile fraction penalty and Huber term. This penalizes tail misestimation directly instead of only mean error.

## Config Surface (On/Off Switches)

### Agent-level toggles
- `recurrent_memory_enabled`
- `recurrent_memory_units`
- `recurrent_memory_dropout`
- `regime_conditioning_enabled`
- `regime_conditioning_hidden_dim`
- `regime_conditioning_dropout`
- `distributional_critic_enabled`
- `distributional_num_quantiles`

### PPO-level toggles
- `risk_aux_cvar_adaptive_enabled`
- `risk_aux_cvar_target`
- `risk_aux_cvar_adapt_lr`
- `risk_aux_cvar_min_coef`
- `risk_aux_cvar_max_coef`
- `distributional_huber_kappa`
- `distributional_mean_loss_coef`

### Checkpoint-selector toggles
- `deterministic_validation_multi_horizon_enabled`
- `deterministic_validation_multi_horizon_limits`
- `deterministic_validation_multi_horizon_weights`
- `deterministic_validation_multi_horizon_dd_penalty_coef`
- `deterministic_validation_stochastic_sanity_enabled`
- `deterministic_validation_stochastic_sanity_runs`
- `deterministic_validation_stochastic_sanity_episode_length_limit`
- `deterministic_validation_stochastic_sanity_min_mean_sharpe`
- `deterministic_validation_stochastic_sanity_max_sharpe_std`

## Backward Compatibility

- All new capabilities default to OFF in config.
- Existing training/evaluation behavior is preserved unless toggles are enabled.
- Metadata and checkpoint records now include selection-score context and multi-horizon diagnostics when enabled.
- Evaluation path auto-detects distributional critic quantile count from critic checkpoints when possible.

## Files Updated

- `src/agents/actor_critic_tf.py`
- `src/agents/ppo_agent_tf.py`
- `src/notebook_helpers/tcn_phase1.py`
- `src/config.py`

## Validation Performed

- Static compile checks passed for updated Python files.
- Runtime smoke test could not be executed in this shell because `numpy` is unavailable in the current environment.
