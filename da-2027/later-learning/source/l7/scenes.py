from lhelp import *
import codes
def d_serve(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L7A)],30,150,690,16,21)
    if t>=ts[2]:
        for i,(n,c) in enumerate([("train",TEAL),("save v1",PUR),("load",GOLD),("validate",RED),("predict",GRN)]):
            if t>=ts[2]+i*1.2:cell(d,770+(i%3)*160,190+(i//3)*70,140,44,n,c,fs=16)
    if t>=ts[3]:
        lab(d,1000,360,"predict(3)  ->  6.02",GRN,18);lab(d,1000,395,'predict("abc") -> rejected',RED,18)
    if t>=ts[4]:lab(d,1000,450,"unit test: predict(0) == bias",GOLD,17)
    tw(d,sc,t,5,"TWIST #1 — version + validation + tests")
def d_drift(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L7B)],30,150,690,16,21)
    if t>=ts[3]:
        G=[("train",[25,25,25,25],TEAL,""),("live ok",[26,24,25,25],GRN,"PSI 0.001"),("live bad",[5,15,30,50],RED,"PSI 0.555")]
        for i,(n,v,c,p) in enumerate(G):
            x=770+i*160;lab(d,x+60,170,n,WHITE,16);vbars(d,x,195,150,[(str(j+1),q) for j,q in enumerate(v)],50,bw=28,gap=8,col=c,fs=12);lab(d,x+60,390,p,GOLD,15)
    if t>=ts[4]:lab(d,1000,450,"PSI > 0.25  =  investigate / retrain",GOLD,17)
    tw(d,sc,t,5,"TWIST #2 — the data drifts, not the model")
def d_wk(d,t,sc):walk(d,sc,t,[(WK7,1,2)])
SCENES=[("title",mk_title("MLOps","serving · tests · drift"),""),("serve",d_serve,"Room 1 · Serving"),("drift",d_drift,"Room 2 · Drift"),("wk",d_wk,"Walkthrough · validation"),("end",mk_end("MLOps — complete",["versioning","validation","unit test","PSI drift"],"next: data engineering"),"")]
