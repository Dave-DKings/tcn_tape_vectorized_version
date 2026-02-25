"""
Feature signal diagnostics for prepared Phase1/Phase2 panel data.

This module computes cross-sectional Information Coefficient (IC) statistics
between feature values at date t and forward returns over multiple horizons.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd


ID_COLUMNS = {
    "Date",
    "Ticker",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Adj Close",
    "day",
    "tic",
    "date",
}


@dataclass
class FeatureSignalReport:
    """Container for feature signal diagnostic outputs."""

    summary_wide: pd.DataFrame
    summary_long: pd.DataFrame
    regime_long: pd.DataFrame
    meta: Dict[str, object]


def _classify_feature_group(column_name: str) -> str:
    """Map feature names to compact group labels for diagnostics."""
    col = str(column_name)
    if col.startswith("LogReturn_"):
        return "log_returns"
    if col.startswith(("RollingVolatility_", "DownsideSemiVar_", "RealizedSkew_", "RealizedKurtosis_")):
        return "rolling_stats"
    if col.startswith(
        (
            "EMA_",
            "BBL_",
            "BBM_",
            "BBU_",
            "MACD_",
            "MACDh_",
            "MACDs_",
            "RSI_",
            "STOCHk_",
            "STOCHd_",
            "WILLR_",
            "SMA_",
            "ADX_",
            "DMP_",
            "DMN_",
            "ATRr_",
            "NATR_",
            "VOL_SMA_",
            "OBV",
            "MFI_",
        )
    ):
        return "technical"
    if col.startswith("Covariance_"):
        return "covariance"
    if col.startswith("Fundamental_"):
        return "fundamental"
    if col.startswith("Regime_"):
        return "regime"
    if col.startswith("Actuarial_"):
        return "actuarial"
    if col.startswith(
        (
            "CrossSectional_ZScore_",
            "Residual_Momentum_",
            "Volume_Percentile_",
            "YieldCurve_",
            "ShortTerm_Reversal_",
            "VolOfVol_",
        )
    ) or col in {"Beta_to_Market", "Market_Return_1d", "OBV_Delta_Norm_21"}:
        return "alpha_quant"
    if col.endswith(("_level", "_diff", "_zscore", "_yoy", "_mom", "_slope")):
        return "macro"
    return "other"


def _safe_spearman_corr(x: np.ndarray, y: np.ndarray, min_obs: int = 5) -> float:
    """Spearman correlation with finite-mask handling and minimum sample guard."""
    mask = np.isfinite(x) & np.isfinite(y)
    if int(mask.sum()) < min_obs:
        return np.nan
    x_rank = pd.Series(x[mask]).rank(method="average").to_numpy(dtype=np.float64)
    y_rank = pd.Series(y[mask]).rank(method="average").to_numpy(dtype=np.float64)
    x_std = float(np.std(x_rank))
    y_std = float(np.std(y_rank))
    if x_std <= 1e-12 or y_std <= 1e-12:
        return np.nan
    return float(np.corrcoef(x_rank, y_rank)[0, 1])


def _infer_feature_columns(df: pd.DataFrame, explicit: Optional[Sequence[str]] = None) -> List[str]:
    """Infer numeric feature columns, excluding identifiers and known target columns."""
    if explicit is not None:
        return [c for c in explicit if c in df.columns]

    numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    excluded_prefixes = ("fwd_return_",)
    excluded_exact = {"next_return_1d", "next_return_5d", "next_return_21d"}
    features: List[str] = []
    for col in numeric_cols:
        if col in ID_COLUMNS or col in excluded_exact:
            continue
        if col.startswith(excluded_prefixes):
            continue
        features.append(col)
    return features


def add_forward_returns(
    df: pd.DataFrame,
    *,
    horizons: Sequence[int] = (1, 5, 21),
    date_col: str = "Date",
    ticker_col: str = "Ticker",
    close_col: str = "Close",
    log_return_1d_col: str = "LogReturn_1d",
) -> pd.DataFrame:
    """
    Add forward return columns `fwd_return_{h}d` using close prices.

    If close is unavailable, falls back to compounding `LogReturn_1d`.
    """
    out = df.copy()
    if date_col in out.columns:
        out[date_col] = pd.to_datetime(out[date_col], errors="coerce")
    out = out.sort_values([ticker_col, date_col]).reset_index(drop=True)

    for horizon in horizons:
        col_name = f"fwd_return_{int(horizon)}d"
        if close_col in out.columns:
            out[col_name] = (
                out.groupby(ticker_col, observed=True)[close_col].shift(-int(horizon))
                / out[close_col]
                - 1.0
            )
            continue

        if log_return_1d_col not in out.columns:
            raise ValueError(
                f"Cannot compute forward returns: neither '{close_col}' nor '{log_return_1d_col}' is available."
            )

        def _compound_forward(g: pd.Series) -> pd.Series:
            vals = pd.to_numeric(g, errors="coerce").to_numpy(dtype=np.float64)
            acc = np.full_like(vals, np.nan, dtype=np.float64)
            h = int(horizon)
            if h <= 0:
                return pd.Series(acc, index=g.index)
            for i in range(len(vals)):
                j = i + h
                if j > len(vals):
                    continue
                window = vals[i + 1 : j + 1]
                if len(window) != h or not np.all(np.isfinite(window)):
                    continue
                acc[i] = np.expm1(np.sum(window))
            return pd.Series(acc, index=g.index)

        out[col_name] = out.groupby(ticker_col, observed=True)[log_return_1d_col].transform(_compound_forward)

    return out


def compute_feature_signal_report(
    panel_df: pd.DataFrame,
    *,
    feature_columns: Optional[Sequence[str]] = None,
    horizons: Sequence[int] = (1, 5, 21),
    date_col: str = "Date",
    ticker_col: str = "Ticker",
    min_cross_section_assets: int = 5,
    regime_column: str = "VIX_zscore",
    regime_quantiles: Tuple[float, float] = (0.33, 0.67),
) -> FeatureSignalReport:
    """
    Compute feature-vs-forward-return IC diagnostics and regime splits.
    """
    df = add_forward_returns(
        panel_df,
        horizons=horizons,
        date_col=date_col,
        ticker_col=ticker_col,
    )

    features = _infer_feature_columns(df, explicit=feature_columns)
    if not features:
        raise ValueError("No feature columns found for diagnostics.")

    if date_col not in df.columns or ticker_col not in df.columns:
        raise ValueError(f"Panel must contain '{date_col}' and '{ticker_col}' columns.")

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col, ticker_col]).copy()

    regimes_by_date = pd.DataFrame(index=pd.Index([], name=date_col))
    if regime_column in df.columns:
        daily_regime_signal = (
            pd.to_numeric(df[regime_column], errors="coerce")
            .groupby(df[date_col])
            .mean()
            .replace([np.inf, -np.inf], np.nan)
            .dropna()
        )
        if len(daily_regime_signal) >= 20:
            q_low, q_high = daily_regime_signal.quantile(regime_quantiles).tolist()
            regimes_by_date = pd.DataFrame(
                {
                    "regime": np.where(
                        daily_regime_signal <= q_low,
                        "low_vol",
                        np.where(daily_regime_signal >= q_high, "high_vol", "mid_vol"),
                    )
                },
                index=daily_regime_signal.index,
            )

    long_rows: List[Dict[str, object]] = []
    regime_rows: List[Dict[str, object]] = []

    grouped = list(df.groupby(date_col, observed=True))

    for feat in features:
        feat_vals = pd.to_numeric(df[feat], errors="coerce")
        feat_missing_rate = float((~np.isfinite(feat_vals.to_numpy(dtype=np.float64))).mean())
        feat_std = float(np.nanstd(feat_vals.to_numpy(dtype=np.float64)))
        feat_nunique = int(pd.Series(feat_vals).nunique(dropna=True))
        feat_group = _classify_feature_group(feat)

        for h in horizons:
            target_col = f"fwd_return_{int(h)}d"
            if target_col not in df.columns:
                continue

            daily_ic_records: List[Tuple[pd.Timestamp, float]] = []
            for date_val, g in grouped:
                x = pd.to_numeric(g[feat], errors="coerce").to_numpy(dtype=np.float64)
                y = pd.to_numeric(g[target_col], errors="coerce").to_numpy(dtype=np.float64)
                ic_val = _safe_spearman_corr(x, y, min_obs=min_cross_section_assets)
                if np.isfinite(ic_val):
                    daily_ic_records.append((pd.Timestamp(date_val), float(ic_val)))

            if not daily_ic_records:
                long_rows.append(
                    {
                        "feature": feat,
                        "feature_group": feat_group,
                        "horizon_days": int(h),
                        "ic_mean": np.nan,
                        "ic_std": np.nan,
                        "ic_ir": np.nan,
                        "ic_hit_rate": np.nan,
                        "n_dates": 0,
                        "missing_rate": feat_missing_rate,
                        "feature_std": feat_std,
                        "n_unique": feat_nunique,
                    }
                )
                continue

            ic_df = pd.DataFrame(daily_ic_records, columns=[date_col, "ic"])
            ic_vals = ic_df["ic"].to_numpy(dtype=np.float64)
            ic_mean = float(np.nanmean(ic_vals))
            ic_std = float(np.nanstd(ic_vals))
            ic_ir = float(ic_mean / ic_std) if ic_std > 1e-12 else np.nan
            sign = 1.0 if ic_mean >= 0 else -1.0
            ic_hit_rate = float(np.mean(sign * ic_vals > 0))
            n_dates = int(len(ic_vals))

            long_rows.append(
                {
                    "feature": feat,
                    "feature_group": feat_group,
                    "horizon_days": int(h),
                    "ic_mean": ic_mean,
                    "ic_std": ic_std,
                    "ic_ir": ic_ir,
                    "ic_hit_rate": ic_hit_rate,
                    "n_dates": n_dates,
                    "missing_rate": feat_missing_rate,
                    "feature_std": feat_std,
                    "n_unique": feat_nunique,
                }
            )

            if not regimes_by_date.empty:
                joined = ic_df.merge(
                    regimes_by_date.reset_index(),
                    on=date_col,
                    how="left",
                ).dropna(subset=["regime"])
                if not joined.empty:
                    for regime_name, rg in joined.groupby("regime", observed=True):
                        regime_rows.append(
                            {
                                "feature": feat,
                                "feature_group": feat_group,
                                "horizon_days": int(h),
                                "regime": str(regime_name),
                                "ic_mean": float(np.nanmean(rg["ic"].to_numpy(dtype=np.float64))),
                                "ic_std": float(np.nanstd(rg["ic"].to_numpy(dtype=np.float64))),
                                "n_dates": int(len(rg)),
                            }
                        )

    long_df = pd.DataFrame(long_rows)
    regime_df = pd.DataFrame(regime_rows)

    if long_df.empty:
        raise ValueError("No IC statistics could be computed; check data coverage and feature columns.")

    wide_df = long_df.pivot_table(
        index=["feature", "feature_group", "missing_rate", "feature_std", "n_unique"],
        columns="horizon_days",
        values=["ic_mean", "ic_std", "ic_ir", "ic_hit_rate", "n_dates"],
        aggfunc="first",
    )
    wide_df.columns = [f"{metric}_{h}d" for metric, h in wide_df.columns.to_flat_index()]
    wide_df = wide_df.reset_index()

    ic_mean_cols = [c for c in wide_df.columns if c.startswith("ic_mean_")]
    ic_ir_cols = [c for c in wide_df.columns if c.startswith("ic_ir_")]
    if ic_mean_cols:
        wide_df["signal_strength"] = wide_df[ic_mean_cols].abs().mean(axis=1)
    else:
        wide_df["signal_strength"] = np.nan
    if ic_ir_cols:
        wide_df["signal_consistency"] = wide_df[ic_ir_cols].abs().mean(axis=1)
    else:
        wide_df["signal_consistency"] = np.nan

    wide_df = wide_df.sort_values(
        by=["signal_strength", "signal_consistency"],
        ascending=[False, False],
    ).reset_index(drop=True)

    meta = {
        "n_rows": int(len(df)),
        "n_dates": int(df[date_col].nunique()),
        "n_assets": int(df[ticker_col].nunique()),
        "n_features": int(len(features)),
        "horizons": [int(h) for h in horizons],
        "min_cross_section_assets": int(min_cross_section_assets),
        "regime_column": regime_column if regime_column in df.columns else None,
        "regime_enabled": bool(not regimes_by_date.empty),
    }

    return FeatureSignalReport(
        summary_wide=wide_df,
        summary_long=long_df.sort_values(["horizon_days", "ic_mean"], ascending=[True, False]).reset_index(drop=True),
        regime_long=regime_df.sort_values(["regime", "horizon_days", "ic_mean"], ascending=[True, True, False]).reset_index(drop=True)
        if not regime_df.empty
        else regime_df,
        meta=meta,
    )


def save_feature_signal_report(
    report: FeatureSignalReport,
    output_dir: Path | str,
    *,
    stem: str = "feature_signal_report",
) -> Dict[str, Path]:
    """Persist report tables to CSV and return output paths."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    paths = {
        "summary_wide": out_dir / f"{stem}_summary_wide.csv",
        "summary_long": out_dir / f"{stem}_summary_long.csv",
        "regime_long": out_dir / f"{stem}_regime_long.csv",
    }
    report.summary_wide.to_csv(paths["summary_wide"], index=False)
    report.summary_long.to_csv(paths["summary_long"], index=False)
    if report.regime_long is not None and not report.regime_long.empty:
        report.regime_long.to_csv(paths["regime_long"], index=False)

    return paths


def describe_top_features(
    report: FeatureSignalReport,
    *,
    top_k: int = 10,
    horizon_days: int = 21,
) -> pd.DataFrame:
    """Return top-k features ranked by absolute IC at the selected horizon."""
    col = f"ic_mean_{int(horizon_days)}d"
    if col not in report.summary_wide.columns:
        raise ValueError(f"Horizon column not found in report: {col}")
    ranked = report.summary_wide.copy()
    ranked["abs_ic"] = ranked[col].abs()
    ranked = ranked.sort_values("abs_ic", ascending=False).head(int(top_k))
    cols = ["feature", "feature_group", col, f"ic_ir_{int(horizon_days)}d", "missing_rate", "feature_std", "n_unique"]
    cols = [c for c in cols if c in ranked.columns]
    return ranked[cols].reset_index(drop=True)
