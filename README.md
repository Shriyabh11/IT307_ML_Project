# IT307 Machine Learning Project: Cloud Workload Forecasting (Baseline & Novelty)

## 📌 Project Overview
This project investigates deep learning and uncertainty-aware workload forecasting for cloud resource management across Google and Alibaba Cloud cluster traces. It comprises:
1. **The Baseline System**: Complete reproduction of the benchmark paper *“Forecasting workload in cloud computing: towards uncertainty-aware predictions and transfer learning”* (Rossi et al., *Cluster Computing*, 2025) sourced from [`grass-overflow/ML_Proj`](https://github.com/grass-overflow/ML_Proj) and our standalone baseline notebooks for **LSTM**, **LSTMD**, and **HBNN**.
2. **The Novelty System**: Our proposed **Anomaly-Aware Workload Forecasting Extension**, augmenting deep models (LSTM, LSTMD, HBNN) with multi-channel unsupervised anomaly detection indicators to alleviate chronic peak under-prediction and improve calibration.

---

## 🗂️ Unified Project Structure

```text
IT307_ML_Project/
├── README.md                                          # Master documentation (Baseline + Novelty)
├── reference_paper/                                   # Reference Research Paper (Rossi et al., 2025)
│   └── Rossi2025_Forecasting_Workload_in_Cloud_Computing.pdf
│
├── baseline/                                          # BASELINE SYSTEM (Rossi et al., 2025)
│   ├── README_BASELINE_REPO.md                        # Original repository README
│   ├── EXPERIMENTS_SETUP.md                           # Baseline hardware, split & run instructions
│   ├── requirements-cpu.txt                           # CPU environment dependencies
│   ├── code/                                          # Baseline Training & Benchmark Notebooks
│   │   ├── lstm_workload_forecasting_baseline.ipynb   # Baseline LSTM standalone notebook (all 4 table configs + TPR vs SR)
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
│   └── util/                                          # Core modules (custom_keras, dataset, metrics, plots)
│
├── code/                                              # NOVELTY CODE PIPELINE
│   ├── anomaly_detection_dataset_generation.ipynb     # Step 1: Anomaly detector & flag generator notebook
│   ├── generate_anomaly_dataset.py                    # Standalone CLI Python version of Step 1
│   ├── lstm_workload_forecasting.ipynb                # Novelty Model 1: Balanced LSTM v3 pipeline
│   ├── lstmd_workload_forecasting.ipynb               # Novelty Model 2: Probabilistic LSTMD (11 traces)
│   └── hbnn_workload_forecasting.ipynb                # Novelty Model 3: Anomaly-Aware Bayesian HBNN
│
├── dataset/                                           # TRACE DATASETS
│   ├── preprocessed_without_anomalies/               # Extracted CSV traces (Novelty inputs)
│   └── with_anomalies/                               # Extracted raw CSV traces (Baseline inputs)
│
└── results/                                           # ALL EXPERIMENTAL RESULTS
    ├── README.md                                      # Guide comparing Baseline vs Novelty results
    ├── baseline/                                      # BASELINE RESULTS (Rossi et al., 2025)
    │   ├── lstm/                                      # Baseline LSTM: 11 publication figures + 49 data CSVs
    │   ├── lstmd/                                     # Baseline LSTMD: 38 analytical figures + contact sheet
    │   └── hbnn/                                      # Baseline HBNN: error tables, runtimes & plots
    └── novelty/                                       # NOVELTY RESULTS (Anomaly-Aware Framework)
        ├── lstm/                                      # Novelty LSTM: 23 generated plots, tables, notes + contact sheet
        ├── lstmd/                                     # Novelty LSTMD: 19 generated plots, case studies & LaTeX report
        └── hbnn/                                      # Novelty HBNN: 25 generated plots, uncertainty & LaTeX report
```

---

## 🔬 Model-by-Model Comparison

### 1. LSTM (Deterministic Forecaster)
- **Baseline Notebook**: [`baseline/code/lstm_workload_forecasting_baseline.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/lstm_workload_forecasting_baseline.ipynb)
- **Baseline Results**: [`results/baseline/lstm/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/baseline/lstm) — 11 publication figures (heatmaps, experiment vs. paper, TPR vs. SR, calibration diagnostics, residual diagnostics, learning curves) + 49 data inventory CSVs. Visual index: [`contact_sheet.png`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/baseline/lstm/contact_sheet.png).
- **Novelty Notebook**: [`code/lstm_workload_forecasting.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/code/lstm_workload_forecasting.ipynb)
- **Novelty Results (33 Files)**: [`results/novelty/lstm/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/lstm) — Paired anomaly/raw ratios, under-prediction penalties, signed prediction bias, and sensitivity across seeds. Visual index: [`CONTACT_SHEET.jpg`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/lstm/figures/CONTACT_SHEET.jpg).

### 2. LSTMD (Probabilistic Forecaster)
- **Baseline Notebook**: [`baseline/code/lstmd_workload_forecasting_baseline.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/lstmd_workload_forecasting_baseline.ipynb)
- **Baseline Results (38 Figures)**: [`results/baseline/lstmd/figures/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/baseline/lstmd/figures) — Heatmaps (`02_mse_heatmap_*.png`), Table 1 vs. paper (`05_table1_*.png`, `06_paper_comparison_*.png`), service rate curves (`08_service_rate_*.png`), TPR (`09_tpr_*.png`), and training logs (`13_training_history_*.png`). Visual index: [`contact_sheet.png`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/baseline/lstmd/figures/contact_sheet.png).
- **Novelty Notebook**: [`code/lstmd_workload_forecasting.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/code/lstmd_workload_forecasting.ipynb)
- **Novelty Results (23 Files)**: [`results/novelty/lstmd/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/lstmd) — Includes direct paired ratio comparisons (`04_anomaly_raw_error_ratio.png`), spike detection case studies (`15_spike_detection_case_study.png`), and complete LaTeX publication report (`lstmd_results_section.tex`). Visual index: [`CONTACT_SHEET.jpg`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/lstmd/figures/CONTACT_SHEET.jpg).

### 3. HBNN (Bayesian Neural Network)
- **Baseline Script & Notebooks**: [`baseline/code/hbnn_training.py`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/hbnn_training.py), [`baseline/code/HBNN_benchmark.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/baseline/code/HBNN_benchmark.ipynb)
- **Baseline Results**: [`results/baseline/hbnn/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/baseline/hbnn) — Error CSVs, training times, and service rate curves.
- **Novelty Notebook**: [`code/hbnn_workload_forecasting.ipynb`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/code/hbnn_workload_forecasting.ipynb)
- **Novelty Results (35 Files)**: [`results/novelty/hbnn/`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/hbnn) — Direct paired ratios (`03_mse_paired_ratio.png`), uncertainty decomposition (`04_uncertainty_decomposition.png`), and spike MSE/under-prediction (`11_spike_mse.png`, `13_spike_underprediction.png`). Visual index: [`CONTACT_SHEET.jpg`](file:///C:/Users/shriy/.gemini/antigravity/scratch/IT307_ML_Project/results/novelty/hbnn/figures/CONTACT_SHEET.jpg).
