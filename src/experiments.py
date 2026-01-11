import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.simulation import (
    simulate_efficient_price,
    add_microstructure_noise,
    true_integrated_variance,
)

from src.estimators import (
    realised_variance,
    subsampled_realised_variance,
    tsrv,
)

from src.metrics import (
    compute_bias,
    compute_variance,
    compute_mse,
)


def run_signature_experiment(
    T,
    sigma,
    eta,
    base_n,
    sampling_steps,
    seed=None,
):
    rng = np.random.default_rng(seed)

    X = simulate_efficient_price(base_n, T, sigma, seed=rng.integers(1e9))
    Y = add_microstructure_noise(X, eta, seed=rng.integers(1e9))

    results = []

    for k in sampling_steps:
        sub_X = X[::k]
        sub_Y = Y[::k]

        rv_x = realised_variance(sub_X)
        rv_y = realised_variance(sub_Y)

        results.append(
            {
                "k": k,
                "effective_n": len(sub_X) - 1,
                "rv_efficient": rv_x,
                "rv_observed": rv_y,
            }
        )

    return pd.DataFrame(results)


def plot_signature(df, save_path=None):
    plt.figure()
    plt.plot(df["effective_n"], df["rv_observed"], marker="o", label="Observed price")
    plt.plot(df["effective_n"], df["rv_efficient"], marker="o", label="Efficient price")
    plt.xlabel("Number of observations")
    plt.ylabel("Realised variance")
    plt.legend()
    plt.gca().invert_xaxis()

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()


def run_monte_carlo_experiment(
    T,
    sigma,
    eta,
    n_list,
    n_sims,
    seed=None,
):
    rng = np.random.default_rng(seed)
    truth = true_integrated_variance(T, sigma)

    rows = []

    for n in n_list:
        rv_vals = []
        subsampled_vals = []
        tsrv_vals = []

        for _ in range(n_sims):
            X = simulate_efficient_price(n, T, sigma, seed=rng.integers(1e9))
            Y = add_microstructure_noise(X, eta, seed=rng.integers(1e9))

            rv_vals.append(realised_variance(Y))
            subsampled_vals.append(subsampled_realised_variance(Y, k=5))
            tsrv_vals.append(tsrv(Y))

        rows.append(
            {
                "n": n,
                "estimator": "RV",
                "bias": compute_bias(rv_vals, truth),
                "variance": compute_variance(rv_vals),
                "mse": compute_mse(rv_vals, truth),
            }
        )

        rows.append(
            {
                "n": n,
                "estimator": "Subsampled RV",
                "bias": compute_bias(subsampled_vals, truth),
                "variance": compute_variance(subsampled_vals),
                "mse": compute_mse(subsampled_vals, truth),
            }
        )

        rows.append(
            {
                "n": n,
                "estimator": "TSRV",
                "bias": compute_bias(tsrv_vals, truth),
                "variance": compute_variance(tsrv_vals),
                "mse": compute_mse(tsrv_vals, truth),
            }
        )

    return pd.DataFrame(rows)


def plot_mse(df, save_path=None):
    plt.figure()

    for name, g in df.groupby("estimator"):
        plt.plot(g["n"], g["mse"], marker="o", label=name)

    plt.xlabel("Number of observations")
    plt.ylabel("Mean squared error")
    plt.legend()
    plt.xscale("log")

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight")
    plt.close()