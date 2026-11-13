from lhelp import *
import codes,math
def d_info(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L31A)],30,150,690,15,20)
    cards(d,t,ts,[(2,"entropy fair / biased coin","1.0  /  0.469",TEAL),(3,"KL(p‖q)  /  KL(q‖p)","0.737  /  0.531",GOLD),(4,"cross-entropy = H + KL","1.737 = 1 + 0.737",GRN),(5,"mutual information","0.278 bits",PUR)],770,200,470,48,12,16)
    tw(d,sc,t,6,'TWIST #1 — cross-entropy = entropy + KL')
def d_mle(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L31B)],30,150,690,15,20)
    import math as m
    if t>=ts[2]:
        a=Ax(790,200,440,200,(0,1),(-400,0));lab(d,1000,182,"log-likelihood of the data",WHITE,15)
        X=[0.28*500*m.log(p)+(1-0.278)*500*m.log(1-p) for p in [0.01]]
        a.curve(d,lambda p:0.278*500*m.log(p)+(1-0.278)*500*m.log(1-p)-300+300,TEAL,4,xr=(0.03,0.97),ylim=(-400,0))
        a.dot(d,0.278,0.278*500*m.log(0.278)+(1-0.278)*500*m.log(1-0.278),GOLD,9);lab(d,a.px(0.278)+14,a.py(-300)-10,"peak = MLE 0.278",GOLD,14,"lm")
    cards(d,t,ts,[(3,"Cramér-Rao sd bound","0.02",GRN)],770,430,470,40)
    tw(d,sc,t,5,'TWIST #2 — best explanation, and how well anything can do')
def d_wk(d,t,sc):walk(d,sc,t,[(WK31,1,2)])
SCENES=[("title",mk_title('Advanced Statistics 1','information theory · maximum likelihood'),""),("info",d_info,'Room 1 · Information theory'),("mle",d_mle,'Room 2 · Estimation'),("wk",d_wk,'Walkthrough · entropy'),("end",mk_end('Information and estimation — complete',['entropy', 'KL', 'MLE', 'Cramér-Rao'],'next: nonparametric methods, GLMs, learning theory'),"")]
