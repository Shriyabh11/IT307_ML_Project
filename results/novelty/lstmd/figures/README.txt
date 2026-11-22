LSTMD generated research figures
================================

Source: LSTMD_anomaly_results (1).zip
Figures are generated from the CSV result tables, prediction exports, and training-history CSVs.
The original supplied CPU MSE figure is included as 00_original_cpu_mse_comparison.png.

Figure index
------------
00  Original CPU MSE comparison supplied in the archive
01  Mean test MSE and MAE by model/variant, CPU and memory
02  Per-dataset/resource test MSE heatmap
02  Per-dataset/resource test MAE heatmap
04  Distribution of anomaly/raw error ratios (ratio < 1 favours anomaly-aware)
05  Raw-model results versus paper-reported metrics
06  Calibration MAE and RMSE
07  Achieved service rate versus target service level
08  Spike recall versus target service level
09  Two-sided interval coverage versus target service level
10  Over-prediction versus target service level
11  Over/under-prediction trade-off
12  Best-epoch and training-time fit diagnostics
13  Median training/validation learning curves by model family
14  Actual versus predicted gc11 CPU and memory case studies
15  gc11 CPU spike-detection case study
16  M-B per-trace CPU and memory MSE: raw versus anomaly-aware

Notes
-----
- All plotted values come from the supplied CSV files. No values were fabricated.
- Prediction case studies use the first 350 test steps (600 for the spike case study) of gc11.
- Learning curves show the median loss trajectory across history files grouped by model family.
- Service-level plots use medians across datasets for each model, variant, resource, and target level.
- Units and normalization follow the source result files. Error metrics are shown as recorded.
- These figures are exploratory research visuals. Check the paper's metric definitions and
  experimental protocol before using any figure as a final publication claim.
