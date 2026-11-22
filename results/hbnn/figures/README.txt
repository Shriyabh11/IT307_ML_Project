HBNN generated research figures
================================

Source archive: results (12).zip
Source folder: HBNN_11trace_anomaly_output

Generated from the supplied HBNN CSV metrics, paired ratios, prediction exports,
service-level metrics, spike metrics, calibration summaries, fit logs, and training
history files. Two original supplied image files are also included.

Figure guide
------------
01  MSE, MAE, and RMSE by model mode, resource, and raw/anomaly variant
02  Per-trace MSE heatmaps for raw and anomaly-aware training
03  Paired anomaly/raw MSE and MAE ratios; values below 1 favour anomaly-aware
04  Aleatoric and epistemic uncertainty decomposition
05  Calibration MAE and RMSE
06  Achieved service rate versus target service level
07  Spike recall versus target service level
08  Over-prediction versus target service level
09  Under-prediction versus target service level
10  Calibration error versus target service level
11-13 Spike-specific MSE, MAE, and underprediction
14  Median training and validation learning curves by mode
15  Best epoch, training time, and inference time diagnostics
16  gc11 actual/raw/anomaly prediction comparisons for CPU and memory
17  gc11 total predictive variance over time for CPU and memory
00  Original images supplied in the archive

Method notes
------------
- Aggregations use the source CSV values; no metric values were fabricated.
- Performance and service plots aggregate across available traces and seeds.
- Paired ratios retain their paired source observations.
- Learning curves show median trajectories across available history files for each mode/variant.
- Prediction case studies use gc11, seed 0, and the first 500 test steps.
- Prediction and utilization scales follow the source CSVs.
- Interpret service metrics using the precise definitions in the experiment protocol;
  this package visualizes the reported columns without redefining them.
- Check the paper's experimental protocol and metric definitions before publication.
