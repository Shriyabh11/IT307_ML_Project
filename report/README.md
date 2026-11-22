# Project Report & Publication Manuscript

This folder contains the final 8-page IEEE conference format research paper for the IT307 Machine Learning course project:

- **Document Source**: `final.tex`
- **Format**: `\documentclass[conference]{IEEEtran}` (Standard 2-column IEEE format)
- **Title**: *Anomaly-Aware Workload Forecasting for Cloud Resource Management*
- **Institution**: Department of Information Technology, National Institute of Technology Karnataka (NITK), Surathkal

---

## Included Report Assets

The figure assets referenced in `final.tex` are placed directly in this directory for seamless compilation:
- `01_error_metric_ratios.png`: Paired error metric ratios (LSTM novelty).
- `02_underprediction_ratios.png`: Under-prediction penalty comparison.
- `lstmd_fig_summary.png`: Summary comparison plots for LSTMD.
- `hbnn_fig_ratio.pdf`: Paired anomaly-to-raw ratio distribution for HBNN.
- `hbnn_fig_service.png`: Service reliability and provisioned ratio curves for HBNN.

---

## Compilation Instructions

### Option 1: Overleaf (Recommended)
1. Zip this `report/` folder or upload the files directly to a new project on [Overleaf](https://www.overleaf.com/).
2. Set compiler to **pdfLaTeX** and build.

### Option 2: Local LaTeX Installation
Run the standard two-pass compilation in terminal:
```bash
pdflatex final.tex
bibtex final
pdflatex final.tex
pdflatex final.tex
```
