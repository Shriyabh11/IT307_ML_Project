import pandas as pd, numpy as np, glob
R='LSTMD_anomaly_results/lstmd_11trace_anomaly_output_v2/'
modes=['S-U','S-B','M-U','M-B']; res=['avgcpu','avgmem']; RL={'avgcpu':'CPU','avgmem':'Mem.'}
M=pd.read_csv(R+'LSTMD_model_metrics.csv'); M['mode']=M.model.str.extract(r'^([A-Z]-[UB])')
P=pd.concat([pd.read_csv(f) for f in glob.glob(R+'predictions/*.csv')]); P['mode']=P.model.str.extract(r'^([A-Z]-[UB])')
P['e']=P.actual-P.pred
rows=[]
for (m,v,d,r),g in P.groupby(['mode','variant','dataset','resource']):
    s=g[g.spike_actual==1]
    rows.append(dict(mode=m,variant=v,dataset=d,resource=r,spike_MSE=(s.e**2).mean(),spike_under=(s.e>0).mean()*100,under=(g.e>0).mean()*100,nsp=len(s)))
T=pd.DataFrame(rows).merge(M[['mode','variant','dataset','resource','MSE','MAE']],on=['mode','variant','dataset','resource'])
assert T.nsp.min()>0
SV=pd.read_csv(R+'LSTMD_service_summary.csv'); SV['mode']=SV.model.str.extract(r'^([A-Z]-[UB])')
CA=pd.read_csv(R+'LSTMD_calibration_summary.csv'); CA['mode']=CA.model.str.extract(r'^([A-Z]-[UB])')
def paired(col):
    k=['mode','dataset','resource']
    a=T[T.variant=='anomaly'].set_index(k)[col]; r=T[T.variant=='raw'].set_index(k)[col]
    return (a/r).rename(col)
PR=pd.concat([paired(c) for c in ['MSE','MAE','spike_MSE']],axis=1).reset_index()
