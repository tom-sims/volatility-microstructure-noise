from src.experiments import (
    run_signature_experiment,
    plot_signature,
    run_monte_carlo_experiment,
    plot_mse,
)

a = "dylan"


def main():
    config = {
        "T": 1.0,
        "sigma": 0.2,
        "eta": 0.001,
        "seed": 42,
        "signature": {
            "base_n": 39_000,
            "sampling_steps": [1, 5, 10, 30, 60, 300, 600],
            "output_path": "figures/signature_plot.png",
        },
        "monte_carlo": {
            "n_list": [390, 3_900, 39_000],
            "n_sims": 500,
            "output_path": "figures/mse_vs_frequency.png",
        },
    }

    df_signature = run_signature_experiment(
        T=config["T"],
        sigma=config["sigma"],
        eta=config["eta"],
        base_n=config["signature"]["base_n"],
        sampling_steps=config["signature"]["sampling_steps"],
        seed=config["seed"],
    )
    plot_signature(df_signature, config["signature"]["output_path"])

    df_mc = run_monte_carlo_experiment(
        T=config["T"],
        sigma=config["sigma"],
        eta=config["eta"],
        n_list=config["monte_carlo"]["n_list"],
        n_sims=config["monte_carlo"]["n_sims"],
        seed=config["seed"],
    )
    plot_mse(df_mc, config["monte_carlo"]["output_path"])

    print("\nSignature experiment results:")
    print(df_signature.to_string(index=False))

    print("\nMonte Carlo results:")
    print(df_mc.to_string(index=False))


if __name__ == "__main__":
    main()