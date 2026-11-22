# Baseline & Novelty Experimental Results

This directory contains experimental evaluations, research figures, diagnostics, and metrics tables across both the **Baseline Models** (reproducing Rossi et al., 2025) and our **Novelty Models** (Anomaly-Aware extensions).

```text
results/
├── README.md                                 # Master results guide (Baseline vs Novelty)
│
├── baseline/                                 # BASELINE RESULTS (Rossi et al., 2025 reproduction)
│   ├── lstm/                                 # Baseline LSTM Outputs (Publication Figures & Data)
│   │   ├── figures/                          # Publication heatmaps, calibration, loss curves & contact sheet
│   │   ├── original_figures/                 # Original TPR vs SR and Table 1 comparison figures
│   │   ├── data_inventory/                   # Fit logs, metrics, predictions, training histories
│   │   └── README.md                         # Detailed data & figure inventory documentation
│   ├── lstmd/                                # Baseline LSTMD Outputs
│   │   └── figures/                          # Heatmaps, Table 1 comparisons, service rates,
│   │                                         # calibration, interval widths, training logs,
│   │                                         # contact_sheet.png, and README.txt
│   └── hbnn/                                 # Baseline HBNN Experimental Outputs
│       ├── figures/                          # Service confidence & TPR vs SR plots
│       ├── res/                              # Error tables, predicted vs actual CSVs
│       ├── time/                             # Baseline training & inference runtimes
│       └── service_level_metrics.csv         # Full baseline service-level metrics table
│
└── novelty/                                  # NOVELTY RESULTS (Anomaly-Aware Framework)
    ├── lstm/                                 # Novelty LSTM v3 Balanced
    │   ├── figures/                          # Research plots, contact sheet, heatmaps
    │   ├── tables/                           # Paired ratios & resource-level metrics CSVs
    │   └── docs/                             # Executive summary & figure captions
    ├── lstmd/                                # Novelty Probabilistic LSTMD
    │   ├── figures/                          # Research plots, case studies & contact sheet
    │   ├── latex/                            # IEEE manuscript & lstmd_results_section.tex
    │   └── scripts/                          # Plotting & metric formatting scripts
    └── hbnn/                                 # Novelty Bayesian HBNN
        ├── figures/                          # Research plots, uncertainty split, contact sheet
        ├── latex/                            # IEEE manuscript & hbnn_results_section.tex
        ├── scripts/                          # Plotting & table generation scripts
        └── docs/                             # Asset notes & documentation
```

---

## Complete Architecture Comparison

| Model | Baseline System (`results/baseline/`) | Novelty Extension (`results/novelty/`) |
| :--- | :--- | :--- |
| **LSTM** | Standard Conv1D-LSTM point forecaster (`results/baseline/lstm/` with publication figures, data CSVs, and paper comparison). | Balanced LSTM conditioned on anomaly flags, volatility scores, and spike jump indicators (`results/novelty/lstm/`). |
| **LSTMD** | Probabilistic Conv1D-LSTM with Gaussian NLL output (`results/baseline/lstmd/` with analytical figures). | Multi-channel anomaly-aware LSTMD evaluating Gaussian NLL under sudden workload spikes (`results/novelty/lstmd/`). |
| **HBNN** | Bayesian DenseVariational neural network predicting aleatoric + epistemic uncertainty (`results/baseline/hbnn/`). | Anomaly-aware HBNN evaluating explicit uncertainty decomposition and spike under-prediction alleviation (`results/novelty/hbnn/`). |
