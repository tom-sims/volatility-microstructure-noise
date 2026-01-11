# Volatility Estimation with Microstructure Noise

This project looks at how different ways of estimating volatility behave when prices are observed very frequently and contain microstructure noise. The focus is on understanding why realised variance can fail at high sampling frequencies and how alternative estimators perform in comparison.

## Motivation

In theory, using high frequency data should lead to better volatility estimates. However, in practice, financial prices are noisy due to effects such as bid–ask bounce and discrete pricing. I wanted to understand why increasing the sampling frequency can actually make volatility estimates worse and how this shows up in both plots and simulation results.

This project was mainly an exercise in learning how these ideas work in practice rather than just in theory.

## Methodology

I simulated a simple log-price process driven by Brownian motion and then added microstructure noise to represent observed prices. Using this setup, I compared:

Realised variance
Subsampled realised variance
Two-scale realised variance (TSRV)


I looked at how these estimators behave as the sampling frequency increases, both for a single simulated price path and in Monte Carlo experiments. I evaluated their performance using bias, variance and mean squared error.

# Expected Results

Based on theory, realised variance computed on noisy prices should increase as sampling frequency increases, even though the true volatility is fixed. Subsampling should reduce this effect but at the cost of higher variability. TSRV is designed to correct for noise and should therefore be more stable.

## Results and Interpretation

The results are consistent with these expectations. Realised variance on observed prices increases sharply at high frequencies, while realised variance on the efficient price remains stable. In the Monte Carlo experiments, realised variance has much higher mean squared error at high sampling frequencies. Subsampled realised variance performs better but TSRV is the most stable estimator and has the lowest mean squared error overall.

Overall, the results show why high-frequency volatility estimation can be misleading and why noise-robust estimators are useful in practice.

## How to Run
To run the full analysis, install the dependencies and execute:
```
pip install -r requirements.txt
python main.py
```
This will reproduce the main plots and summary results.

