import numpy as np

def simulate_efficient_price(n, t, sigma, seed=None):
    rng = np.random.default_rng(seed)
    dt = t / n
    z = rng.standard_normal(size=n)

    dX = sigma * np.sqrt(dt) * z 

    x = np.empty(n + 1)
    x[0] = 0.0
    x[1:] = np.cumsum(dX)
    return x

def add_microstructure_noise(x, eta, seed=None):
    rng = np.random.default_rng(seed)
    epsilon = rng.normal(0.0, eta, size=len(x))  
    return x + epsilon

def true_integrated_variance(t, sigma):
    return (sigma ** 2) * t