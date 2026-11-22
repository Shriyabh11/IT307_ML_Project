# LSTM experimental results: figure package

## Contents inspected
The uploaded archive was inspected independently. It contains 94 files:
.csv: 49, .keras: 39, .png: 6.

- CSV files: 49
- Training-history CSVs: 39
- Prediction CSVs: 4
- Original raster figures preserved: 6
- Excel workbooks: 0
- Log/text files: 0
- Nested ZIP files: 0
- Keras model files: 39 (retained in the source archive; not loaded)

No Excel files, standalone logs, or nested ZIPs were present. The `.keras` model artifacts were inventoried but not executed or loaded.

## Generated figures
- `01_median_mse_heatmap.png`: Median MSE by model and resource across available datasets.
- `01_median_mae_heatmap.png`: Median MAE by model and resource across available datasets.
- `02_mse_dataset_resource_heatmap.png`: MSE across each model × dataset × resource combination.
- `02_mae_dataset_resource_heatmap.png`: MAE across each model × dataset × resource combination.
- `03_experiment_vs_paper.png`: Experiment versus paper reference values for CPU/memory MSE and MAE.
- `04_tpr_vs_service_rate.png`: TPR versus service rate, with reported standard-deviation error bars.
- `05_service_level_calibration_diagnostics.png`: Coverage, calibration error, and interval width across nominal service levels.
- `06_training_validation_loss_by_family.png`: Mean training and validation loss curves across history files grouped by model family.
- `07_training_validation_mae_by_family.png`: Mean training and validation MAE curves across history files grouped by model family.
- `08_prediction_vs_ground_truth.png`: Prediction versus ground truth, sampled deterministically up to 5,000 rows per model.
- `09_residual_diagnostics.png`: Residual distribution and residual-versus-fitted diagnostics.
- `10_training_efficiency_convergence.png`: Training duration and best validation loss against best epoch.
- `11_aggregate_service_performance.png`: Aggregate service rate and empirical coverage by model/resource.

## Source-data mapping and notes
- `LSTM_model_metrics.csv` supports the MSE/MAE heatmaps.
- `LSTM_table1_vs_paper.csv` supports the paper-reference comparison. Values are plotted exactly as supplied; no external verification of the cited paper values was performed.
- `LSTM_tpr_vs_sr_data.csv` supports TPR/service-rate curves and uses the supplied mean and standard deviation fields.
- `LSTM_service_level_metrics.csv` supports service-level, coverage, calibration-error, and interval-width diagnostics.
- `history/*.csv` supports training/validation loss and MAE histories. Curves are arithmetic means across available history files within each model family; they are not single-run curves.
- `predictions/*.csv` supports prediction-versus-label and residual diagnostics. Scatter/hexbin views use deterministic subsamples for readability; aggregate residual histograms use up to 10,000 sampled rows per model.
- `LSTM_fit_log.csv` supports training-time and best-epoch diagnostics.

## Unsupported plots / limitations
- RMSE is not explicitly provided. It was not inferred from MSE because the metric's scale/aggregation semantics are not established in the archive.
- Precision, recall, F1, and FPR are not present as named fields and were not fabricated or derived.
- No separate calibration-bin predictions, probability scores, or per-sample prediction intervals are supplied. Calibration and interval plots therefore use only the provided service-level summary fields.
- No separate validation predictions or test-set split metadata beyond the supplied CSVs are available.
- The original PNG figures are preserved unchanged under `original_figures/`.
- CSV files are copied under `data_inventory/` for traceability. The source `.keras` model files remain available in the original uploaded ZIP but are not duplicated into this package.

## CSV inventory
- `lstm_output/LSTM_fit_log.csv`: 39 rows × 13 columns; columns: model, tag, hp, resources, n_train, n_val, epochs_run, best_epoch, best_val_loss, train_minutes, batch_size, optimizer, model_file
- `lstm_output/LSTM_model_metrics.csv`: 96 rows × 7 columns; columns: model, dataset, resource, MSE, MAE, n_test, training
- `lstm_output/LSTM_service_level_metrics.csv`: 1,056 rows × 9 columns; columns: model, dataset, resource, service_level, SR, TPR, coverage, calibration_error, mean_interval_width
- `lstm_output/LSTM_table1.csv`: 4 rows × 6 columns; columns: Model, CPU_MSE, CPU_MAE, Memory_MSE, Memory_MAE, traces
- `lstm_output/LSTM_table1_vs_paper.csv`: 4 rows × 10 columns; columns: Model, CPU_MSE, paper_CPU_MSE, CPU_MAE, paper_CPU_MAE, Memory_MSE, paper_Memory_MSE, Memory_MAE, paper_Memory_MAE, traces
- `lstm_output/LSTM_tpr_vs_sr_data.csv`: 88 rows × 8 columns; columns: model, resource, service_level, SR_mean, SR_std, TPR_mean, TPR_std, n_traces
- `lstm_output/history/M-B-LSTM__all.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/M-U-LSTM__all__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/M-U-LSTM__all__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__ali18.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__ali20_c.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__ali20_g.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc11.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc19_a.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc19_b.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc19_c.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc19_d.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc19_e.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc19_f.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc19_g.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-B-LSTM__gc19_h.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__ali18__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__ali18__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__ali20_c__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__ali20_c__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__ali20_g__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__ali20_g__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc11__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc11__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_a__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_a__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_b__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_b__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_c__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_c__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_d__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_d__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_e__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_e__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_f__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_f__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_g__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_g__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_h__cpu.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/history/S-U-LSTM__gc19_h__mem.csv`: 500 rows × 5 columns; columns: epoch, loss, mae, val_loss, val_mae
- `lstm_output/predictions/LSTM_M-B_predictions.csv`: 35,050 rows × 6 columns; columns: model, dataset, resource, step, pred, label
- `lstm_output/predictions/LSTM_M-U_predictions.csv`: 35,050 rows × 6 columns; columns: model, dataset, resource, step, pred, label
- `lstm_output/predictions/LSTM_S-B_predictions.csv`: 35,050 rows × 6 columns; columns: model, dataset, resource, step, pred, label
- `lstm_output/predictions/LSTM_S-U_predictions.csv`: 35,050 rows × 6 columns; columns: model, dataset, resource, step, pred, label
