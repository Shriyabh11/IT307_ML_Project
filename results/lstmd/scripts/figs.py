exec(open('scripts/prep.py').read())
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
plt.rcParams.update({'font.family':'serif','font.serif':['Liberation Serif','TeX Gyre Termes','DejaVu Serif'],'mathtext.fontset':'stix',
 'font.size':8,'axes.labelsize':8,'axes.titlesize':8.5,'xtick.labelsize':7.5,'ytick.labelsize':7.5,'legend.fontsize':7.5,
 'axes.linewidth':0.6,'xtick.major.width':0.6,'ytick.major.width':0.6,'pdf.fonttype':42,'axes.spines.top':False,'axes.spines.right':False,
 'axes.grid':True,'grid.color':'#DDDDDD','grid.linewidth':0.4,'axes.axisbelow':True})
CFG={'S-U':'#0072B2','S-B':'#009E73','M-U':'#E69F00','M-B':'#CC79A7'}
SE=lambda x: x.std(ddof=1)/np.sqrt(len(x))
fig,ax=plt.subplots(1,3,figsize=(7.16,2.75))
a=ax[0]; w=0.19
for j,(r,c,col) in enumerate([('avgcpu','MSE','#4C72B0'),('avgmem','MSE','#4C72B0'),('avgcpu','spike_MSE','#DD8452'),('avgmem','spike_MSE','#DD8452')]):
    vals=[PR[(PR['mode']==m)&(PR.resource==r)][c] for m in modes]
    a.bar(np.arange(4)+(j-1.5)*w,[v.mean() for v in vals],w,color=col,hatch='////' if r=='avgmem' else None,ec='k',lw=.4,yerr=[SE(v) for v in vals],capsize=1.5,error_kw={'lw':.6})
a.axhline(1,color='k',lw=.8,ls='--'); a.set_xticks(range(4)); a.set_xticklabels(modes); a.set_ylim(0.4,1.6); a.set_xlabel('Configuration'); a.set_ylabel('Paired ratio, anomaly-aware / raw'); a.set_title('(a) Point and spike error',loc='left')
lv=np.array(sorted(SV.service_level.unique()))*100
def curve(m,v): return SV[(SV['mode']==m)&(SV.variant==v)].groupby('service_level')[['SR','TPR']].mean()
a=ax[1]; a.plot([89,100],[89,100],color='k',lw=.8,ls=':')
for m in modes:
    for v,ls in (('raw','--'),('anomaly','-')):
        c=curve(m,v); a.plot(lv,c.SR.values,ls=ls,color=CFG[m],marker='o',ms=2.5,lw=1.0)
a.set_xlabel('Target service level (%)'); a.set_ylabel('Realised success rate, SR (%)'); a.set_title('(b) Calibration',loc='left'); a.set_xlim(89.5,100); a.set_ylim(86,100.3)
a=ax[2]
for m in modes:
    for v,ls in (('raw','--'),('anomaly','-')):
        c=curve(m,v); a.plot(c.SR.values,c.TPR.values,ls=ls,color=CFG[m],marker='o',ms=2.5,lw=1.0)
a.set_xlabel('Realised SR (%)'); a.set_ylabel('Total predicted resources, TPR (%)'); a.set_title('(c) Resource cost of coverage',loc='left')
h=[Patch(fc='#4C72B0',ec='k',lw=.4,label='MSE'),Patch(fc='#DD8452',ec='k',lw=.4,label='Spike MSE'),Patch(fc='w',ec='k',lw=.4,label='CPU'),Patch(fc='w',ec='k',lw=.4,hatch='////',label='Memory')]
h+= [Line2D([],[],color=CFG[m],lw=1.6,label=m) for m in modes]+[Line2D([],[],color='k',lw=1.1,ls='--',label='Raw'),Line2D([],[],color='k',lw=1.1,ls='-',label='Anomaly-aware')]
fig.legend(handles=h,loc='upper center',ncol=5,frameon=False,bbox_to_anchor=(0.5,1.0),handlelength=1.5,columnspacing=1.2)
fig.tight_layout(rect=(0,0,1,0.84)); fig.savefig('lstmd_fig_summary.pdf'); fig.savefig('lstmd_fig_summary.png',dpi=200); plt.close(); print('ok')
print(PR.groupby(['mode','resource'])[['MSE','spike_MSE']].mean().round(3))
