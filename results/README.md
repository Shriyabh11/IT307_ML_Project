# Baseline & Novelty Experimental Results

This directory contains experimental evaluations, research figures, diagnostics, and metrics tables across both the **Baseline Models** (reproducing Rossi et al., 2025) and our **Novelty Models** (Anomaly-Aware extensions).

```text
results/
├── README.md # Master results guide (Baseline vs Novelty)
│
├── baseline/ # BASELINE RESULTS (Rossi et al., 2025 reproduction)
│ ├── lstm/ # Baseline LSTM Outputs (Publication Figures & Data)
│ │ ├── figures/ # 11 publication heatmaps, calibration, loss curves & contact sheet
│ │ ├── original_figures/ # Original TPR vs SR and Table 1 comparison figures
│ │ ├── data_inventory/ # 49 CSVs (fit logs, metrics, predictions, training histories)
│ │ └── README.md # Detailed data & figure inventory documentation
│ ├── lstmd/ # Baseline LSTMD Outputs (38 Figures)
│ │ └── figures/ # Heatmaps, Table 1 comparisons, service rates,
│ │ # calibration, interval widths, training logs,
│ │ # contact_sheet.png, and README.txt
│ └── hbnn/ # Baseline HBNN Experimental Outputs
│ ├── res/ # Error tables, predicted vs actual CSVs
│ ├── plots/ # Baseline service confidence & TPR vs SR plots
│ ├── time/ # Baseline training & inference runtimes
│ └── service_level_metrics.csv # Full baseline service-level metrics table
│
└── novelty/ # NOVELTY RESULTS (Anomaly-Aware Framework)
 ├── lstm/ # Novelty LSTM v3 Balanced (33 files)
 │ ├── figures/ # 23 generated plots, contact sheet, heatmaps
 │ ├── tables/ # Paired ratios & resource-level metrics CSVs
 │ └── docs/ # Executive summary & figure captions
 ├── lstmd/ # Novelty Probabilistic LSTMD (23 files)
 │ ├── figures/ # 19 generated plots, case studies & contact sheet
 │ ├── latex/ # IEEE manuscript & lstmd_results_section.tex
 │ └── scripts/ # Plotting & metric formatting scripts
 └── hbnn/ # Novelty Bayesian HBNN (35 files)
 ├── figures/ # 25 generated plots, uncertainty split, contact sheet
 ├── latex/ # IEEE manuscript & hbnn_results_section.tex
 ├── scripts/ # Plotting & table generation scripts
 └── docs/ # Asset notes & documentation
```

---

## Complete Architecture Comparison

| Model | Baseline System (`results/baseline/`) | Novelty Extension (`results/novelty/`) |
| :--- | :--- | :--- |
| **LSTM** | Standard Conv1D-LSTM point forecaster (`results/baseline/lstm/` with 11 publication figures, 49 data CSVs, and paper comparison). | Balanced LSTM conditioned on anomaly flags, volatility scores, and spike jump indicators (`results/novelty/lstm/`). |
| **LSTMD** | Probabilistic Conv1D-LSTM with Gaussian NLL output (`results/baseline/lstmd/` with 38 figures). | Multi-channel anomaly-aware LSTMD evaluating Gaussian NLL under sudden workload spikes (`results/novelty/lstmd/`). |
| **HBNN** | Bayesian DenseVariational neural network predicting aleatoric + epistemic uncertainty (`results/baseline/hbnn/`). | Anomaly-aware HBNN evaluating explicit uncertainty decomposition and spike under-prediction alleviation (`results/novelty/hbnn/`). |
