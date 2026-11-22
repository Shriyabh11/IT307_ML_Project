exec(open('/tmp/hbfig/prep.py').read())
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
plt.rcParams.update({'font.family':'serif','font.serif':['Liberation Serif','TeX Gyre Termes','DejaVu Serif'],'mathtext.fontset':'stix',
 'font.size':8,'axes.labelsize':8,'axes.titlesize':8.5,'xtick.labelsize':7.5,'ytick.labelsize':7.5,'legend.fontsize':7.5,
 'axes.linewidth':0.6,'xtick.major.width':0.6,'ytick.major.width':0.6,'pdf.fonttype':42,'axes.spines.top':False,'axes.spines.right':False,
 'axes.grid':True,'grid.color':'#DDDDDD','grid.linewidth':0.4,'axes.axisbelow':True})
RAW,ANO='#8C8C8C','#D55E00'; CFG={'S-U':'#0072B2','S-B':'#009E73','M-U':'#E69F00','M-B':'#CC79A7'}
modes=['S-U','S-B','M-U','M-B']; res=['avgcpu','avgmem']; RL={'avgcpu':'CPU','avgmem':'Memory'}
def g(df,m,v,r=None):
    x=df[(df['mode']==m)&(df.variant==v)]
    return x[x.resource==r].iloc[0] if r else x
SE=lambda sd,n:sd/np.sqrt(n)
def legend4(fig,y=1.02):
    h=[Patch(fc=RAW,ec='k',lw=.4,label='Raw, CPU'),Patch(fc=ANO,ec='k',lw=.4,label='Anomaly-aware, CPU'),
       Patch(fc=RAW,ec='k',lw=.4,hatch='////',label='Raw, memory'),Patch(fc=ANO,ec='k',lw=.4,hatch='////',label='Anomaly-aware, memory')]
    fig.legend(handles=h,loc='upper center',ncol=4,frameon=False,bbox_to_anchor=(0.5,y),handlelength=1.6,columnspacing=1.6)
def bars4(ax,df,mcol,sdcol,log=False,scale=1.0):
    w=0.19; x0=np.arange(4)
    for j,(r,v) in enumerate([('avgcpu','raw'),('avgcpu','anomaly'),('avgmem','raw'),('avgmem','anomaly')]):
        vals=[g(df,m,v,r)[mcol]*scale for m in modes]; err=[SE(g(df,m,v,r)[sdcol]*scale,g(df,m,v,r).n_trace_seed) for m in modes]
        if log: err=[[min(e,0.4*val) for e,val in zip(err,vals)],err]
        ax.bar(x0+(j-1.5)*w,vals,w,color=RAW if v=='raw' else ANO,hatch='////' if r=='avgmem' else None,ec='k',lw=.4,yerr=err,capsize=1.5,error_kw={'lw':.6})
    ax.set_xticks(x0); ax.set_xticklabels(modes)
# ---------- Fig 1: accuracy
fig,ax=plt.subplots(1,2,figsize=(7.16,2.45)); 
bars4(ax[0],ov,'MSE_mean','MSE_sd',log=True); ax[0].set_yscale('log'); ax[0].set_yticks([0.002,0.005,0.01,0.02,0.05]); ax[0].set_yticklabels(['0.002','0.005','0.01','0.02','0.05']); ax[0].minorticks_off(); ax[0].set_ylim(0.0018,0.09); ax[0].set_ylabel('MSE (log scale)'); ax[0].set_title('(a) Overall MSE',loc='left')
bars4(ax[1],ov,'MAE_mean','MAE_sd'); ax[1].set_ylabel('MAE'); ax[1].set_title('(b) Overall MAE',loc='left')
for a in ax: a.set_xlabel('Configuration')
legend4(fig); fig.tight_layout(rect=(0,0,1,0.9)); fig.savefig('hbnn_fig_accuracy.pdf'); fig.savefig('hbnn_fig_accuracy.png',dpi=200); plt.close()
# ---------- Fig 2: paired ratio
fig,ax=plt.subplots(1,2,figsize=(7.16,2.3),sharey=True)
mets=[('MSE','MSE','#4C72B0'),('MAE','MAE','#55A868'),('underprediction_rate','Under-prediction rate','#C44E52')]
for a,r in zip(ax,res):
    w=0.24
    for j,(k,lab,c) in enumerate(mets):
        vals=[pr[(pr['mode']==m)&(pr.resource==r)&(pr.metric==k)].iloc[0] for m in modes]
        a.bar(np.arange(4)+(j-1)*w,[v.mean_paired_anomaly_over_raw for v in vals],w,color=c,ec='k',lw=.4,label=lab,
              yerr=[SE(v.sd_paired_anomaly_over_raw,v.n_pairs) for v in vals],capsize=1.5,error_kw={'lw':.6})
    a.axhline(1,color='k',lw=.8,ls='--'); a.set_xticks(range(4)); a.set_xticklabels(modes); a.set_xlabel('Configuration'); a.set_ylim(0,1.9)
    a.set_title(f'({"ab"[res.index(r)]}) {RL[r]}',loc='left')
ax[0].set_ylabel('Paired ratio, anomaly-aware / raw')
ax[1].text(0.985,0.96,'below 1: anomaly-aware better',transform=ax[1].transAxes,fontsize=7,style='italic',color='#444',ha='right',va='top')
h,l=ax[0].get_legend_handles_labels(); fig.legend(h,l,loc='upper center',ncol=3,frameon=False,bbox_to_anchor=(0.5,1.03))
fig.tight_layout(rect=(0,0,1,0.9)); fig.savefig('hbnn_fig_ratio.pdf'); fig.savefig('hbnn_fig_ratio.png',dpi=200); plt.close()
# ---------- Fig 3: service level
fig,ax=plt.subplots(1,2,figsize=(7.16,2.7))
lv=[90,95,99,99.5]
def curve(m,v):
    x=sv[(sv['mode']==m)&(sv.variant==v)].groupby('service_level')[['SR_mean','TPR_mean']].mean(); return x
a=ax[0]; a.plot([86,100],[86,100],color='k',lw=.8,ls=':'); 
for m in modes:
    for v,ls in (('raw','--'),('anomaly','-')):
        c=curve(m,v); a.plot(lv,c.SR_mean.values,ls=ls,color=CFG[m],marker='o',ms=3,lw=1.1)
a.set_xlabel('Target service level (%)'); a.set_ylabel('Realised success rate, SR (%)'); a.set_title('(a) Calibration of the upper bound',loc='left'); a.set_xlim(89.5,100); a.set_ylim(86.5,100.3)
a=ax[1]
for m in modes:
    for v,ls in (('raw','--'),('anomaly','-')):
        c=curve(m,v); a.plot(c.SR_mean.values,c.TPR_mean.values,ls=ls,color=CFG[m],marker='o',ms=3,lw=1.1)
a.set_yscale('log'); a.set_yticks([100,150,200,300]); a.set_yticklabels(['100','150','200','300']); a.minorticks_off()
a.set_xlabel('Realised SR (%)'); a.set_ylabel('Total predicted resources, TPR (%)'); a.set_title('(b) Resource cost of coverage',loc='left')
h=[Line2D([],[],color=CFG[m],lw=1.6,label=m) for m in modes]+[Line2D([],[],color='k',lw=1.1,ls='--',label='Raw'),Line2D([],[],color='k',lw=1.1,ls='-',label='Anomaly-aware')]
fig.legend(handles=h,loc='upper center',ncol=6,frameon=False,bbox_to_anchor=(0.5,1.03))
fig.tight_layout(rect=(0,0,1,0.9)); fig.savefig('hbnn_fig_service.pdf'); fig.savefig('hbnn_fig_service.png',dpi=200); plt.close()
# ---------- Fig 4: spike and uncertainty (mean over CPU, memory)
fig,ax=plt.subplots(1,3,figsize=(7.16,2.35))
def mo(df,col,v,m,scale=1): return df[(df['mode']==m)&(df.variant==v)][col].mean()*scale
w=0.36
for a,(df,col,sc,yl,ti,lg) in zip(ax,[(sp,'spike_MSE_mean',1,'Spike MSE','(a) Spike-period MSE',True),(sp,'spike_underprediction_mean',100,'Spike points under-predicted (%)','(b) Spike under-prediction',False)]):
    for j,(v,c) in enumerate((('raw',RAW),('anomaly',ANO))):
        a.bar(np.arange(4)+(j-.5)*w,[mo(df,col,v,m,sc) for m in modes],w,color=c,ec='k',lw=.4,label='Raw' if v=='raw' else 'Anomaly-aware')
    a.set_xticks(range(4)); a.set_xticklabels(modes); a.set_ylabel(yl); a.set_title(ti,loc='left'); a.set_xlabel('Configuration')
    if lg: a.set_yscale('log'); a.set_yticks([0.01,0.02,0.04,0.07]); a.set_yticklabels(['0.01','0.02','0.04','0.07']); a.minorticks_off()
ax[1].set_ylim(0,105)
a=ax[2]
for j,(v,c) in enumerate((('raw',RAW),('anomaly',ANO))):
    sh=[ (ov[(ov['mode']==m)&(ov.variant==v)].epistemic_variance_mean/ov[(ov['mode']==m)&(ov.variant==v)].total_variance_mean).mean()*100 for m in modes]
    a.bar(np.arange(4)+(j-.5)*w,sh,w,color=c,ec='k',lw=.4)
a.set_xticks(range(4)); a.set_xticklabels(modes); a.set_ylabel('Epistemic share of variance (%)'); a.set_title('(c) Uncertainty split',loc='left'); a.set_xlabel('Configuration')
h,l=ax[0].get_legend_handles_labels(); fig.legend(h,l,loc='upper center',ncol=2,frameon=False,bbox_to_anchor=(0.5,1.03))
fig.tight_layout(rect=(0,0,1,0.9)); fig.savefig('hbnn_fig_spike.pdf'); fig.savefig('hbnn_fig_spike.png',dpi=200); plt.close()
print('ok')
