import pandas as pd, numpy as np
D=pd.read_csv('/tmp/hb/HBNN_presentation_analysis/HBNN_aggregated_comparisons.csv')
T={t:D[D.table==t].dropna(axis=1,how='all').drop(columns=['table']).reset_index(drop=True) for t in D.table.unique()}
modes=['S-U','S-B','M-U','M-B']; res=['avgcpu','avgmem']
ov,sp,sv,ca,rt,pr=T['overall_metrics'],T['spike_metrics'],T['service_level_metrics'],T['calibration'],T['runtime'],T['paired_anomaly_raw_ratios']
