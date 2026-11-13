from lhelp import *
import codes,math
def beta(a,b):
    c=math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b));return lambda x:c*x**(a-1)*(1-x)**(b-1)
def d_bay(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L6A)],30,150,690,16,21)
    if t>=ts[2]:
        a=Ax(790,190,430,260,(0,0.4),(0,14));a.axes(d,(0,0.1,0.2,0.3,0.4),(0,5,10));lab(d,1000,170,"belief about click rate",WHITE,16)
        a.curve(d,beta(13,89),TEAL,4)
        if t>=ts[4]:a.curve(d,beta(19,83),GOLD,4);lab(d,1130,230,"B: 18/100",GOLD,15);lab(d,900,230,"A: 12/100",TEAL,15)
    if t>=ts[4]+3:lab(d,1000,500,"P(B better) = 0.88",GRN,20)
    tw(d,sc,t,5,"TWIST #1 — a posterior is an updatable belief")
def d_ab(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L6B)],30,150,690,16,21)
    if t>=ts[2]:
        a=Ax(790,200,430,220,(-4,4),(0,0.45));a.axes(d,(-4,-2,0,2,4),());a.curve(d,lambda z:math.exp(-z*z/2)/2.5066,TEAL,4)
        for z in (-1.96,1.96):d.line([a.P(z,0),a.P(z,0.45)],fill=RED,width=3)
        lab(d,1000,180,"noise-only z values",WHITE,16)
        if t>=ts[2]+3:d.line([a.P(1.96,0),a.P(1.96,0.4)],fill=GOLD,width=5);lab(d,a.px(1.96)+10,a.py(0.42),"our z = 1.96",GOLD,15,"lm")
    if t>=ts[3]:lab(d,1000,470,"plan ahead: 2031 users per arm",GRN,20)
    tw(d,sc,t,5,"TWIST #2 — fix the sample size before the test")
def d_wk(d,t,sc):walk(d,sc,t,[(WK6,1,2)])
SCENES=[("title",mk_title("Bayesian Methods and A/B Tests","posteriors · z test · sample size"),""),("bay",d_bay,"Room 1 · Bayes"),("ab",d_ab,"Room 2 · A/B tests"),("wk",d_wk,"Walkthrough · Beta update"),("end",mk_end("Bayes and A/B — complete",["Beta posterior","P(B better)","z test","sample size"],"next: MLOps"),"")]
