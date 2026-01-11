import numpy as np

def realised_variance(prices):
    prices = np.asarray(prices)
    if prices.ndim != 1:
        raise ValueError("prices must be a 1D array")
    if len(prices) < 2:
        raise ValueError("prices must have length >= 2")

    return float(np.sum(np.diff(prices) ** 2))

def subsampled_realised_variance(prices, k):
    prices = np.asarray(prices)

    if prices.ndim != 1:
        raise ValueError("prices must be a 1D array")
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be an integer >= 1")
    if len(prices) < 2:
        raise ValueError("prices must have length >= 2")

    sub = prices[::k]
    if len(sub) < 2:
        return 0.0

    return float(np.sum(np.diff(sub) ** 2))

def tsrv(prices, K=None):
    prices = np.asarray(prices)

    if prices.ndim != 1:
        raise ValueError("prices must be a 1D array")
    if len(prices) < 3:
        return 0.0

    n = len(prices) - 1

    if K is None:
        K = int(np.sqrt(n))
    if not isinstance(K, int) or K < 2:
        raise ValueError("K must be an integer >= 2")
    if K > n:
        K = n

    rv_fast = float(np.sum(np.diff(prices) ** 2))

    rv_sum = 0.0
    m_sum = 0

    for j in range(K):
        sub = prices[j::K]
        m_j = len(sub) - 1
        if m_j <= 0:
            continue
        rv_sum += float(np.sum(np.diff(sub) ** 2))
        m_sum += m_j

    if m_sum == 0:
        return 0.0

    rv_slow_avg = rv_sum / K
    m_bar = m_sum / K

    ratio = m_bar / n
    denom = 1.0 - ratio
    if denom <= 0:
        return 0.0

    tsrv_est = (rv_slow_avg - ratio * rv_fast) / denom
    return float(max(tsrv_est, 0.0))