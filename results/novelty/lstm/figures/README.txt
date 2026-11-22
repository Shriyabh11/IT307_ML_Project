LSTM v3 balanced results: generated research figures
====================================================

Source archive: results (13).zip
Source directory: lstm_v3_balanced

The archive contains summary/metric CSVs and model weight files, but no exported
per-timestep prediction CSVs or training-history CSVs. Therefore this package
focuses on figures supported by the available metric tables. It does not invent
prediction trajectories or learning curves.

Figure guide
------------
01  Test MSE, MAE, and spike MSE by configuration and resource
02  Per-trace test MSE and MAE heatmaps
03  Paired test metric ratios relative to raw_mse baseline
04  Spike MAE, overall underprediction, and spike underprediction comparisons
05  Mean signed prediction bias (actual minus prediction)
06  Validation versus test MSE
07  Test MSE variability across traces and seeds
08  Screen-validation metric comparisons (MSE, MAE, spike MSE, spike MAE)
00  Original images supplied in the archive, including the existing heatmaps/ratio plot

Interpretation notes
--------------------
- Configuration labels are preserved exactly as supplied: raw_mse, score_mse,
  score_mild1, and all_mse. The archive does not define their full methodological
  meanings, so this package does not infer or rename them.
- Paired ratios are plotted as provided. The baseline is raw_mse; a ratio of 1
  indicates equality with that baseline.
- Means and distributions are calculated from the supplied trace/seed metrics.
- Validation and test splits are kept distinct.
- No prediction time-series plots or learning curves were fabricated because
  the archive does not include per-step predictions or training histories.
- Check the experimental protocol and metric definitions before publication.
