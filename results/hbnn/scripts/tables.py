exec(open('/tmp/hbfig/prep.py').read())
modes=['S-U','S-B','M-U','M-B']; res=['avgcpu','avgmem']; RL={'avgcpu':'CPU','avgmem':'Mem.'}
def row(df,m,v,r): x=df[(df['mode']==m)&(df.variant==v)&(df.resource==r)]; return x.iloc[0]
def bold_lo(a,b,fmt):  # bold the smaller (better) of raw / anomaly
    sa,sb=fmt.format(a),fmt.format(b)
    return (sa,r'\textbf{'+sb+'}') if b<a else (r'\textbf{'+sa+'}',sb)
L=[]
L.append(r'''\begin{table*}[!t]
\caption{HBNN with and without anomaly-aware inputs, mean over 11 traces and 3 seeds. Spike under-prediction is the share of spike points where the mean forecast lies below the actual demand. Lower is better in every column; the better value of each pair is in bold.}
\label{tab:hbnn_acc}
\centering
\footnotesize
\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{llcccccccc}
\toprule
 & & \multicolumn{2}{c}{MSE} & \multicolumn{2}{c}{MAE} & \multicolumn{2}{c}{Spike MSE} & \multicolumn{2}{c}{Spike under-pred. (\%)}\\
\cmidrule(lr){3-4}\cmidrule(lr){5-6}\cmidrule(lr){7-8}\cmidrule(lr){9-10}
Config. & Res. & Raw & Anomaly & Raw & Anomaly & Raw & Anomaly & Raw & Anomaly\\
\midrule''')
for m in modes:
    for i,r in enumerate(res):
        a,b=row(ov,m,'raw',r),row(ov,m,'anomaly',r); sa,sb=row(sp,m,'raw',r),row(sp,m,'anomaly',r)
        c=[bold_lo(a.MSE_mean,b.MSE_mean,'{:.4f}'),bold_lo(a.MAE_mean,b.MAE_mean,'{:.3f}'),bold_lo(sa.spike_MSE_mean,sb.spike_MSE_mean,'{:.4f}'),
           bold_lo(sa.spike_underprediction_mean*100,sb.spike_underprediction_mean*100,'{:.1f}')]
        cells=' & '.join(f'{x} & {y}' for x,y in c)
        L.append(f'{m if i==0 else ""} & {RL[r]} & {cells}\\\\')
    if m!='M-B': L.append(r'\addlinespace[2pt]')
L.append(r'''\bottomrule
\end{tabular}
\end{table*}
''')
# service table
L.append(r'''\begin{table}[!t]
\caption{Service-level behaviour of the HBNN upper bound (mean over CPU and memory, 11 traces, 3 seeds). SR is the realised success rate, TPR the total predicted resources as a percentage of actual demand, and Cal.\ the mean absolute gap between realised and target SR over the four target levels.}
\label{tab:hbnn_service}
\centering
\footnotesize
\setlength{\tabcolsep}{3.6pt}
\begin{tabular}{llcccccc}
\toprule
 & & \multicolumn{2}{c}{95\% target} & \multicolumn{2}{c}{99\% target} & Cal. & Epist.\\
\cmidrule(lr){3-4}\cmidrule(lr){5-6}
Config. & Input & SR & TPR & SR & TPR & (pp) & (\%)\\
\midrule''')
for m in modes:
    for i,v in enumerate(['raw','anomaly']):
        x=sv[(sv['mode']==m)&(sv.variant==v)]
        g=lambda lvl,c: x[np.isclose(x.service_level,lvl)][c].mean()
        cal=ca[(ca['mode']==m)&(ca.variant==v)].calibration_MAE_pp.mean()
        o=ov[(ov['mode']==m)&(ov.variant==v)]; ep=(o.epistemic_variance_mean/o.total_variance_mean).mean()*100
        L.append(f'{m if i==0 else ""} & {"Raw" if v=="raw" else "Anomaly"} & {g(0.95,"SR_mean"):.1f} & {g(0.95,"TPR_mean"):.1f} & {g(0.99,"SR_mean"):.1f} & {g(0.99,"TPR_mean"):.1f} & {cal:.2f} & {ep:.1f}\\\\')
    if m!='M-B': L.append(r'\addlinespace[2pt]')
L.append(r'''\bottomrule
\end{tabular}
\end{table}''')
open('/tmp/hbfig/hbnn_tables.tex','w').write('\n'.join(L)); print('\n'.join(L))
