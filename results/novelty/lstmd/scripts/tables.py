exec(open('scripts/prep.py').read())
def cell(df,m,v,r,c): x=df[(df['mode']==m)&(df.variant==v)&(df.resource==r)]; return x[c].mean()
def bold_lo(a,b,fmt):
    sa,sb=fmt.format(a),fmt.format(b)
    if sa==sb: return sa,sb
    return (sa,r'\textbf{'+sb+'}') if b<a else (r'\textbf{'+sa+'}',sb)
L=[]
L.append(r'''\begin{table*}[!t]
\caption{LSTMD with and without anomaly-aware inputs, mean over 11 traces (one run per trace). Spike under-prediction is the share of spike points where the mean forecast lies below the actual demand. Lower is better in every column; the better value of each pair is in bold.}
\label{tab:lstmd_acc}
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
        c=[bold_lo(cell(T,m,'raw',r,'MSE'),cell(T,m,'anomaly',r,'MSE'),'{:.4f}'),
           bold_lo(cell(T,m,'raw',r,'MAE'),cell(T,m,'anomaly',r,'MAE'),'{:.3f}'),
           bold_lo(cell(T,m,'raw',r,'spike_MSE'),cell(T,m,'anomaly',r,'spike_MSE'),'{:.4f}'),
           bold_lo(cell(T,m,'raw',r,'spike_under'),cell(T,m,'anomaly',r,'spike_under'),'{:.1f}')]
        L.append(f'{m if i==0 else ""} & {RL[r]} & '+' & '.join(f'{x} & {y}' for x,y in c)+r'\\')
    if m!='M-B': L.append(r'\addlinespace[2pt]')
L.append(r'''\bottomrule
\end{tabular}
\end{table*}
''')
L.append(r'''\begin{table}[!t]
\caption{Service-level behaviour of the LSTMD upper bound (mean over CPU, memory and 11 traces, one run per trace). SR is the realised success rate, TPR the total predicted resources as a percentage of actual demand, and Cal.\ the mean absolute gap between realised and target SR over the eleven target levels from 90\% to 99.5\%.}
\label{tab:lstmd_service}
\centering
\footnotesize
\setlength{\tabcolsep}{3.6pt}
\begin{tabular}{llccccc}
\toprule
 & & \multicolumn{2}{c}{95\% target} & \multicolumn{2}{c}{99\% target} & Cal.\\
\cmidrule(lr){3-4}\cmidrule(lr){5-6}
Config. & Input & SR & TPR & SR & TPR & (pp)\\
\midrule''')
for m in modes:
    for i,v in enumerate(['raw','anomaly']):
        x=SV[(SV['mode']==m)&(SV.variant==v)]
        g=lambda lvl,c: x[np.isclose(x.service_level,lvl)][c].mean()
        cal=CA[(CA['mode']==m)&(CA.variant==v)].calibration_MAE_pp.mean()
        L.append(f'{m if i==0 else ""} & {"Raw" if v=="raw" else "Anomaly"} & {g(0.95,"SR"):.1f} & {g(0.95,"TPR"):.1f} & {g(0.99,"SR"):.1f} & {g(0.99,"TPR"):.1f} & {cal:.2f}'+r'\\')
    if m!='M-B': L.append(r'\addlinespace[2pt]')
L.append(r'''\bottomrule
\end{tabular}
\end{table}''')
open('scripts/lstmd_tables.tex','w').write('\n'.join(L)); print('\n'.join(L))
