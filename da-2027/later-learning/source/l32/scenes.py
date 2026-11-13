from lhelp import *
import codes,math
def d_np(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L32A)],30,150,690,15,20)
    cards(d,t,ts,[(2,"KDE at 0  /  true density","0.407  /  0.399",TEAL),(3,"bootstrap sd of the median","0.172",GOLD),(4,"P(Z > 3) by importance sampling","0.0014",GRN),(4,"true value","0.00135",GRY)],770,200,470,48,12,16)
    tw(d,sc,t,5,'TWIST #1 — let the data speak')
def d_glm(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L32B)],30,150,690,15,20)
    cards(d,t,ts,[(2,"logistic weights  w, b","5.39, -2.47",TEAL),(3,"ridge  /  lasso on 3.0","1.5  /  2.5",GOLD),(4,"PAC sample bound","169",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,5,'TWIST #2 — match the model, shrink, size the data')
def d_wk(d,t,sc):walk(d,sc,t,[(WK32,1,2)])
SCENES=[("title",mk_title('Advanced Statistics 2','resampling · GLMs · regularisation · PAC'),""),("np",d_np,'Room 1 · Nonparametric and resampling'),("glm",d_glm,'Room 2 · GLMs and learning theory'),("wk",d_wk,'Walkthrough · ridge and lasso'),("end",mk_end('Advanced statistics 2 — complete',['KDE', 'bootstrap', 'GLM', 'PAC bound'],'next: calculus optimization'),"")]
