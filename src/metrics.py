import numpy as np
import pandas as pd


def compute_bias(estimates, truth):
    est = np.asarray(estimates, dtype=float).ravel()
    est = est[np.isfinite(est)]
    if est.size == 0:
        return np.nan
    return float(np.mean(est) - truth)


def compute_variance(estimates, ddof=1):
    est = np.asarray(estimates, dtype=float).ravel()
    est = est[np.isfinite(est)]
    if est.size == 0:
        return np.nan
    if est.size == 1:
        return 0.0
    return float(np.var(est, ddof=ddof))


def compute_mse(estimates, truth):
    est = np.asarray(estimates, dtype=float).ravel()
    est = est[np.isfinite(est)]
    if est.size == 0:
        return np.nan
    return float(np.mean((est - truth) ** 2))


def compute_rmse(estimates, truth):
    est = np.asarray(estimates, dtype=float).ravel()
    est = est[np.isfinite(est)]
    if est.size == 0:
        return np.nan
    return float(np.sqrt(np.mean((est - truth) ** 2)))


def compute_mae(estimates, truth):
    est = np.asarray(estimates, dtype=float).ravel()
    est = est[np.isfinite(est)]
    if est.size == 0:
        return np.nan
    return float(np.mean(np.abs(est - truth)))


def summarise_estimates(estimates_by_method, truth):
    rows = []

    for method, estimates in estimates_by_method.items():
        est = np.asarray(estimates, dtype=float).ravel()
        est = est[np.isfinite(est)]

        if est.size == 0:
            rows.append(
                {
                    "method": method,
                    "n": 0,
                    "mean": np.nan,
                    "std": np.nan,
                    "bias": np.nan,
                    "variance": np.nan,
                    "mse": np.nan,
                    "rmse": np.nan,
                    "mae": np.nan,
                }
            )
            continue

        rows.append(
            {
                "method": method,
                "n": len(est),
                "mean": float(np.mean(est)),
                "std": float(np.std(est, ddof=1)) if len(est) > 1 else 0.0,
                "bias": float(np.mean(est) - truth),
                "variance": float(np.var(est, ddof=1)) if len(est) > 1 else 0.0,
                "mse": float(np.mean((est - truth) ** 2)),
                "rmse": float(np.sqrt(np.mean((est - truth) ** 2))),
                "mae": float(np.mean(np.abs(est - truth))),
            }
        )

    return pd.DataFrame(rows).set_index("method")