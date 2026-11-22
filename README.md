# IT307 Machine Learning Project: Cloud Workload Forecasting (Baseline & Novelty)

## 📌 Project Overview
This project investigates deep learning and uncertainty-aware workload forecasting for cloud resource management across Google and Alibaba Cloud cluster traces. It comprises:
1. **The Baseline System**: Reproduction of the benchmark paper *“Forecasting workload in cloud computing: towards uncertainty-aware predictions and transfer learning”* (Rossi et al., *Cluster Computing*, 2025) sourced from [`grass-overflow/ML_Proj`](https://github.com/grass-overflow/ML_Proj) and our standalone baseline notebooks.
2. **The Novelty System**: Our proposed **Anomaly-Aware Workload Forecasting Extension**, augmenting deep models (LSTM, LSTMD, HBNN) with multi-channel unsupervised anomaly detection indicators to cure chronic peak under-prediction and improve calibration.

---

## 🗂️ Unified Project Structure

```text
IT307_ML_Project/
├── README.md                                          # Master documentation (Baseline + Novelty)
├── reference_paper/                                   # Reference Research Paper (Rossi et al., 2025)
│   ├── Rossi2025_Forecasting_Workload_in_Cloud_Computing.pdf
│   └── s10586-024-04933-2.pdf
│
├── baseline/                                          # BASELINE SYSTEM (Rossi et al., 2025)
│   ├── README_BASELINE_REPO.md                        # Original repository README
│   ├── EXPERIMENTS_SETUP.md                           # Baseline hardware, split & run instructions
│   ├── requirements-cpu.txt                           # CPU environment dependencies
│   ├── code/                                          # Baseline Training & Benchmark Notebooks
│   │   ├── lstmd_workload_forecasting_baseline.ipynb  # Baseline LSTMD standalone notebook (all 4 table configs)
│   │   ├── hbnn_training.py                           # Baseline HBNN training script
│   │   ├── HBNN_benchmark.ipynb                       # Baseline HBNN benchmark notebook
│   │   ├── HBNN_Eval.ipynb & HBNN_PLOTS.ipynb         # Baseline HBNN evaluation & plot generation
│   │   ├── lstm_training.py & lstmd_training.py       # Baseline LSTM / LSTMD runners
│   │   └── LSTM_benchmark.ipynb & LSTMD_benchmark.ipynb
│   ├── hyperparams/                                   # Paper-tuned hyperparameters (CSV)
│   │   ├── bivariate/                                 # Bivariate single-trace hyperparams
│   │   ├── multibivariate/                            # Bivariate multi-trace hyperparams
│   │   ├── multiunivariate/                           # Univariate multi-trace hyperparams
│   │   └── univariate/                                # Univariate single-trace hyperparams
│   ├── util/                                          # Core modules (custom_keras, dataset, metrics, plots)
│   └── results/                                       # Baseline experimental outputs
│       ├── hbnn/                                      # Baseline HBNN error & time outputs
│       └── lstmd/                                     # Baseline LSTMD 38 analytical figures
│
├── code/                                              # NOVELTY CODE PIPELINE
│   ├── anomaly_detection_dataset_generation.ipynb     # Step 1: Anomaly detector & flag generator notebook
│   ├── generate_anomaly_dataset.py                    # Standalone CLI Python version of Step 1
│   ├── lstm_workload_forecasting.ipynb                # Novelty Model 1: Balanced LSTM v3 pipeline
│   ├── lstmd_workload_forecasting.ipynb               # Novelty Model 2: Probabilistic LSTMD (11 traces)
│   └── hbnn_workload_forecasting.ipynb                # Novelty Model 3: Anomaly-Aware Bayesian HBNN
│
├── dataset/                                           # TRACE DATASETS
│   ├── preprocessed_without_anomalies.zip             # Anomaly-flagged traces (Novelty inputs)
│   ├── with_anomalies.zip                             # Raw time-series traces (Baseline inputs)
│   ├── preprocessed_without_anomalies/               # Extracted CSV traces
│   └── with_anomalies/                               # Extracted raw CSV traces
│
└── results/                                           # ALL EXPERIMENTAL RESULTS
    ├── README.md                                      # Guide comparing Baseline vs Novelty results
    ├── baseline/                                      # BASELINE RESULTS (Rossi et al., 2025)
    │   ├── hbnn/                                      # Baseline HBNN error tables, runtimes & plots
    │   └── lstmd/                                     # Baseline LSTMD: 38 research figures + contact sheet
    └── novelty/                                       # NOVELTY RESULTS (Anomaly-Aware Framework)
        ├── lstm/                                      # 23 generated plots, tables, notes + contact sheet
        ├── lstmd/                                     # 19 generated plots, case studies & LaTeX report
        └── hbnn/                                      # 25 generated plots, uncertainty & LaTeX report
```

---

## 🔬 Model-by-Model Comparison

### 1. LSTMD (Probabilistic Forecaster)
- **Baseline Notebook**: [`baseline/code/lstmd_workload_forecasting_baseline.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/lstmd_workload_forecasting_baseline.ipynb)
- **Baseline Results (38 Figures)**: [`results/baseline/lstmd/figures/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/baseline/lstmd/figures) — Heatmaps (`02_mse_heatmap_*.png`), Table 1 vs. paper (`05_table1_*.png`, `06_paper_comparison_*.png`), service rate curves (`08_service_rate_*.png`), TPR (`09_tpr_*.png`), and training logs (`13_training_history_*.png`). Visual index: [`contact_sheet.png`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/baseline/lstmd/figures/contact_sheet.png).
- **Novelty Notebook**: [`code/lstmd_workload_forecasting.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/code/lstmd_workload_forecasting.ipynb)
- **Novelty Results (23 Files)**: [`results/novelty/lstmd/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/lstmd) — Includes direct paired ratio comparisons (`04_anomaly_raw_error_ratio.png`), spike detection case studies (`15_spike_detection_case_study.png`), and complete LaTeX publication report (`lstmd_results_section.tex`). Visual index: [`CONTACT_SHEET.jpg`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/lstmd/figures/CONTACT_SHEET.jpg).

### 2. HBNN (Bayesian Neural Network)
- **Baseline Script & Notebooks**: [`baseline/code/hbnn_training.py`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/hbnn_training.py), [`baseline/code/HBNN_benchmark.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/HBNN_benchmark.ipynb)
- **Baseline Results**: [`results/baseline/hbnn/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/baseline/hbnn) — Error CSVs, training times, and service rate curves.
- **Novelty Notebook**: [`code/hbnn_workload_forecasting.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/code/hbnn_workload_forecasting.ipynb)
- **Novelty Results (35 Files)**: [`results/novelty/hbnn/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/hbnn) — Direct paired ratios (`03_mse_paired_ratio.png`), uncertainty decomposition (`04_uncertainty_decomposition.png`), and spike MSE/under-prediction (`11_spike_mse.png`, `13_spike_underprediction.png`). Visual index: [`CONTACT_SHEET.jpg`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/hbnn/figures/CONTACT_SHEET.jpg).

### 3. LSTM (Deterministic Forecaster)
- **Baseline Scripts**: [`baseline/code/lstm_training.py`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/lstm_training.py), [`baseline/code/LSTM_benchmark.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/LSTM_benchmark.ipynb)
- **Novelty Notebook**: [`code/lstm_workload_forecasting.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/code/lstm_workload_forecasting.ipynb)
- **Novelty Results (33 Files)**: [`results/novelty/lstm/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/lstm) — Paired ratios, under-prediction penalties, and sensitivity across seeds. Visual index: [`CONTACT_SHEET.jpg`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/lstm/figures/CONTACT_SHEET.jpg).
