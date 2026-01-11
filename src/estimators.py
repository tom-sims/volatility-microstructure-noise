import numpy as np

def realised_variance(prices):
    returns = np.diff(prices)
    returns_squared = returns**2
    rv = np.sum(returns_squared)
    return rv

def subsampled_realised_variance(prices, k):
    pass

def tsrv(prices, K):
    pass

