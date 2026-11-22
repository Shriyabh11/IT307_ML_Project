# IT307 Machine Learning Project: Cloud Workload Forecasting

## Project Overview
This project investigates deep learning and uncertainty-aware workload forecasting for cloud resource management across Google and Alibaba Cloud cluster traces. It comprises:
1. **The Baseline System**: Complete reproduction of the benchmark paper *"Forecasting workload in cloud computing: towards uncertainty-aware predictions and transfer learning"* (Rossi et al., *Cluster Computing*, 2025) for **LSTM**, **LSTMD**, and **HBNN**.
2. **The Novelty System**: Our proposed **Anomaly-Aware Workload Forecasting Extension**, augmenting deep models (LSTM, LSTMD, HBNN) with multi-channel unsupervised anomaly detection indicators to alleviate chronic peak under-prediction and improve calibration.

---

## Problem Statement

In large-scale cloud data centers (like Google Cloud and Alibaba Cloud), resource managers must forecast incoming CPU and memory demand a few minutes ahead of time. Accurate forecasting allows the system to spin up or shut down servers dynamically, saving energy and cost while preventing application crashes.

However, conventional forecasting models face a critical operational challenge:
- **Chronic Peak Under-Prediction**: Normal workload patterns are relatively smooth, but real cloud environments regularly experience sudden bursts (flash crowds, batch compute jobs, system failovers). Standard machine learning models (such as baseline LSTM, LSTMD, and HBNN) trained on smooth historical data severely **under-predict** during these critical spikes.
- **The Real-World Cost**: Under-predicting demand causes server CPU saturation, application lag, dropped user requests, and Service Level Objective (SLO) violations. Over-predicting to compensate leads to massive over-provisioning and wasted electricity.

---

## What We Did (Our Solution)

Rather than forcing deep models to predict purely from raw CPU and memory time-series, we introduced an **Anomaly-Aware Forecasting Framework**:
1. **Detect Abnormal Regimes Early**: We built an automated, unsupervised anomaly detection pipeline that analyzes historical rolling windows.
2. **Multi-Channel Conditioning**: Whenever the system detects abnormal behavior or erratic fluctuations, it generates auxiliary feature signals (binary flags, continuous severity scores, and spike jump indicators) and feeds them directly into the deep forecasting models as extra input channels.
3. **Multi-Model Benchmark**: We evaluated whether giving models explicit "anomaly awareness" improves forecasting across three model architectures:
   - **Deterministic LSTM**: Point forecasts with balanced penalty for under-prediction.
   - **Probabilistic LSTMD**: Gaussian distribution forecasting to estimate aleatoric uncertainty.
   - **Bayesian Neural Network (HBNN)**: Quantifies both aleatoric (data noise) and epistemic (model uncertainty) bounds.

---

## What Our Anomalies Are

In this project, an "anomaly" is not just arbitrary synthetic noise. It represents a real operational deviation in cluster traces:
- **Sudden Workload Spikes**: Rapid surges where CPU or memory usage shoots significantly above the local moving trend.
- **Volatility Bursts**: Sudden jumps in variance where demand rapidly fluctuates between high and low values.
- **Regime Shifts**: Periods where workload dynamics fundamentally shift away from steady-state behavior.

### How Anomalies Are Detected & Represented
We generate three auxiliary channels for each time step using an ensemble voting mechanism (Rolling MAD, Robust Z-scores, Jump differences, and an Isolation Forest):
- **`_flag` (Binary Anomaly Flag)**: A 0 or 1 indicator showing whether multiple statistical detectors and the Isolation Forest agreed that the current time step is anomalous.
- **`_score` (Continuous Severity Score)**: A normalized score from 0.0 to 1.0 quantifying how severe or unusual the anomaly is, helping models scale their predictions proportionally.
- **`_spike_eval` (Sudden Jump Indicator)**: A dedicated metric flagging rapid positive changes (jumps) in resource utilization to specifically evaluate model responsiveness to sudden surges.

---

## Unified Project Structure

```text
IT307_ML_Project/
├── README.md                                          # Master documentation (Baseline + Novelty)
├── report/                                            # Final IEEE Conference Report & Manuscript
│   ├── final.tex                                      # 8-page IEEE conference paper source
│   └── README.md                                      # Compilation & asset guide
├── reference_paper/                                   # Reference Research Paper (Rossi et al., 2025)
│   └── Rossi2025_Forecasting_Workload_in_Cloud_Computing.pdf
│
├── baseline/                                          # BASELINE SYSTEM (Rossi et al., 2025)
│   ├── README_BASELINE_REPO.md                        # Original repository README
│   ├── EXPERIMENTS_SETUP.md                           # Baseline hardware, split & run instructions
│   ├── requirements-cpu.txt                           # CPU environment dependencies
│   ├── code/                                          # Baseline Training & Benchmark Notebooks
│   │   ├── lstm_workload_forecasting_baseline.ipynb   # Baseline LSTM notebook
│   │   ├── lstmd_workload_forecasting_baseline.ipynb  # Baseline LSTMD notebook
│   │   ├── hbnn_workload_forecasting_baseline.ipynb   # Baseline HBNN notebook 
│   │   ├── hbnn_training.py, lstm_training.py, lstmd_training.py # Baseline training runners
│   │   └── hbnn_eval.ipynb, hbnn_plots.ipynb, compare_model_metrics.ipynb # Evaluation & plot notebooks
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
│   ├── lstm_workload_forecasting.ipynb                # Novelty Model 1:  LSTM 
│   ├── lstmd_workload_forecasting.ipynb               # Novelty Model 2:  LSTMD
│   └── hbnn_workload_forecasting.ipynb                # Novelty Model 3:  Bayesian HBNN
│
├── dataset/                                           # TRACE DATASETS
│   ├── preprocessed_without_anomalies/               # Extracted CSV traces (Novelty inputs)
│   └── with_anomalies/                               # Extracted raw CSV traces (Baseline inputs)
│
└── results/                                           # ALL EXPERIMENTAL RESULTS
    ├── README.md                                      # Guide comparing Baseline vs Novelty results
    ├── baseline/                                      # BASELINE RESULTS (Rossi et al., 2025)
    │   ├── lstm/                                      # Baseline LSTM: publication figures + data CSVs
    │   ├── lstmd/                                     # Baseline LSTMD: analytical figures + contact sheet
    │   └── hbnn/                                      # Baseline HBNN: figures, error tables & runtimes
    └── novelty/                                       # NOVELTY RESULTS (Anomaly-Aware Framework)
        ├── lstm/                                      # Novelty LSTM: research plots, tables, notes + contact sheet
        ├── lstmd/                                     # Novelty LSTMD: research plots, case studies & LaTeX report
        └── hbnn/                                      # Novelty HBNN: research plots, uncertainty & LaTeX report
```

---

## Model-by-Model Comparison

### 1. LSTM (Deterministic Forecaster)
- **Baseline Notebook**: [`baseline/code/lstm_workload_forecasting_baseline.ipynb`](baseline/code/lstm_workload_forecasting_baseline.ipynb)
- **Baseline Results**: [`results/baseline/lstm/`](results/baseline/lstm/) Visual index: [`contact_sheet.png`](results/baseline/lstm/figures/contact_sheet.png).
- **Novelty Notebook**: [`code/lstm_workload_forecasting.ipynb`](code/lstm_workload_forecasting.ipynb)
- **Novelty Results**: [`results/novelty/lstm/`](results/novelty/lstm/) Visual index: [`contact_sheet.jpg`](results/novelty/lstm/figures/contact_sheet.jpg).

### 2. LSTMD (Probabilistic Forecaster)
- **Baseline Notebook**: [`baseline/code/lstmd_workload_forecasting_baseline.ipynb`](baseline/code/lstmd_workload_forecasting_baseline.ipynb)
- **Baseline Results**: [`results/baseline/lstmd/`](results/baseline/lstmd/)
- **Novelty Notebook**: [`code/lstmd_workload_forecasting.ipynb`](code/lstmd_workload_forecasting.ipynb)
- **Novelty Results**: [`results/novelty/lstmd/`](results/novelty/lstmd/) Visual index: [`contact_sheet.jpg`](results/novelty/lstmd/figures/contact_sheet.jpg).

### 3. HBNN (Bayesian Neural Network)
- **Baseline Standalone Notebook**: [`baseline/code/hbnn_workload_forecasting_baseline.ipynb`](baseline/code/hbnn_workload_forecasting_baseline.ipynb)
- **Baseline Script & Utilities**: [`baseline/code/hbnn_training.py`](baseline/code/hbnn_training.py), [`baseline/code/hbnn_benchmark.ipynb`](baseline/code/hbnn_benchmark.ipynb)
- **Baseline Results**: [`results/baseline/hbnn/`](results/baseline/hbnn/).
- **Novelty Notebook**: [`code/hbnn_workload_forecasting.ipynb`](code/hbnn_workload_forecasting.ipynb)
- **Novelty Results**: [`results/novelty/hbnn/`](results/novelty/hbnn/) Visual index: [`contact_sheet.jpg`](results/novelty/hbnn/figures/contact_sheet.jpg).
