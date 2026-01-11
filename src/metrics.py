import numpy as np


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
