# Baseline & Novelty Experimental Results

This directory contains the experimental evaluations, generated research figures, diagnostic plots, and performance tables for both the **Baseline Models** (reproducing Rossi et al., 2025) and our **Novelty Models** (Anomaly-Aware extensions).

```text
results/
├── README.md                                 # Master results guide (Baseline vs Novelty)
│
├── baseline/                                 # BASELINE RESULTS (Rossi et al., 2025 reproduction)
│   ├── hbnn/                                 # Baseline HBNN Experimental Outputs
│   │   ├── res/                              # Error tables, predicted vs actual CSVs
│   │   ├── plots/                            # Baseline service confidence & TPR vs SR plots
│   │   ├── time/                             # Baseline training & inference runtimes
│   │   └── service_level_metrics.csv         # Full baseline service-level metrics table
│   └── lstmd/                                # Baseline LSTMD Experimental Outputs (38 Figures)
│       └── figures/                          # Heatmaps, Table 1 comparisons, service rates,
│                                             # calibration, interval widths, training logs,
│                                             # contact_sheet.png, and README.txt
│
└── novelty/                                  # NOVELTY RESULTS (Anomaly-Aware Framework)
    ├── lstm/                                 # Novelty LSTM v3 Balanced (33 files)
    │   ├── figures/                          # 23 generated plots, contact sheet, heatmaps
    │   ├── tables/                           # Paired ratios & resource-level metrics CSVs
    │   └── docs/                             # Executive summary & figure captions
    ├── lstmd/                                # Novelty Probabilistic LSTMD (23 files)
    │   ├── figures/                          # 19 generated plots, case studies & contact sheet
    │   ├── latex/                            # IEEE manuscript & lstmd_results_section.tex
    │   └── scripts/                          # Plotting & metric formatting scripts
    └── hbnn/                                 # Novelty Bayesian HBNN (35 files)
        ├── figures/                          # 25 generated plots, uncertainty split, contact sheet
        ├── latex/                            # IEEE manuscript & hbnn_results_section.tex
        ├── scripts/                          # Plotting & table generation scripts
        └── docs/                             # Asset notes & documentation
```

---

## 📊 Summary of Baseline vs. Novelty LSTMD Results

| Metric Category | Baseline LSTMD (`results/baseline/lstmd/`) | Novelty LSTMD (`results/novelty/lstmd/`) |
| :--- | :--- | :--- |
| **Input Signals** | Raw CPU & memory observations (`time`, `avgcpu`, `avgmem`) | Raw observations + **unsupervised anomaly flags, continuous severity scores, and spike jump indicators** |
| **Figure Bundle** | 38 research figures + `contact_sheet.png` + `README.txt` | 19 research figures + `CONTACT_SHEET.jpg` + LaTeX section |
| **Table 1 vs. Paper** | `05_table1_*`, `06_paper_comparison_*`, `07_percent_difference_vs_paper.png` | Validated reproduction in `05_raw_vs_paper_comparison.png` |
| **Service Metrics** | `08_service_rate_*`, `09_tpr_*`, `10_calibration_error_*`, `10_mean_interval_width_*` | Service reliability vs. SLO target in `07_service_rate_vs_target.png`, `09_interval_coverage_*` |
| **Training Logs** | Detailed histories for M-B, M-U, S-B, S-U (`13_training_history_*.png`) | Median training/validation loss curves (`13_learning_curves_by_family.png`) |
| **Novelty Paired Ratio** | N/A (Standard Baseline) | **`04_anomaly_raw_error_ratio.png`** (Direct anomaly/raw paired ratios showing improvements) |

---

## 📊 Summary of Baseline vs. Novelty HBNN Results

| Metric Category | Baseline HBNN (`results/baseline/hbnn/`) | Novelty HBNN (`results/novelty/hbnn/`) |
| :--- | :--- | :--- |
| **Input Signals** | Raw traces (`multibivariate/HBNN-w288-h2.csv` tuned params) | Raw traces + multi-channel anomaly indicators |
| **Outputs** | `res/` error CSVs, `plots/` service curves, `time/` CSVs | 25 generated research figures, `CONTACT_SHEET.jpg`, LaTeX report |
| **Uncertainty Split** | Aleatoric + Epistemic predictive variance | **`04_uncertainty_decomposition.png`** (explicit variance decomposition under spikes) |
| **Spike Metrics** | Standard aggregate MSE | **`11_spike_mse.png`**, **`12_spike_mae.png`**, **`13_spike_underprediction.png`** |
