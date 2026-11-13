from lhelp import *
import codes,math
def d_mcmc(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L23A)],30,150,690,15,20)
    import math as m
    if t>=ts[2]:
        a=Ax(790,200,440,200,(-4,8),(0,1.1));a.axes(d,(-4,0,4,8),());lab(d,1000,182,"target (unnormalised)",WHITE,15)
        a.curve(d,lambda x:m.exp(-x*x/2)+0.5*m.exp(-(x-4)**2/2),TEAL,4)
    cards(d,t,ts,[(3,"sample mean","1.18  (exact 1.33)",GOLD),(3,"share above 2","0.31  (exact ≈ 0.34)",GOLD)],770,430,470,40,8,16)
    tw(d,sc,t,5,'TWIST #1 — a random walk that visits by probability')
def d_unc(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L23B),(4,L23C)],30,150,690,15,20)
    if t>=ts[2] and t<ts[4]:
        lab(d,1000,175,"prediction spread (sd)",WHITE,15);hbars(d,790,200,[("inside data",0.09),("far outside",0.78)],0.8,w=240,col=[GRN,RED],lw=110,fmt="{:g}")
    if t>=ts[4]:
        lab(d,1000,175,"KL(q || p) for three choices of q",WHITE,15)
        cards(d,t,ts,[(4,"narrow on one bump","0.69",GRN),(4,"wide, in the middle","2.02",GOLD),(4,"narrow, in the middle","5.42",RED)],770,200,470,44,10,16)
    tw(d,sc,t,5,'TWIST #2 — turn one answer into a spread')
def d_wk(d,t,sc):walk(d,sc,t,[(WK23,1,2)])
SCENES=[("title",mk_title('Bayesian Methods and Uncertainty','MCMC · ensembles · variational inference'),""),("mcmc",d_mcmc,'Room 1 · MCMC'),("unc",d_unc,'Room 2 · Uncertainty'),("wk",d_wk,'Walkthrough · accept step'),("end",mk_end('Bayesian methods — complete',['Metropolis', 'ensemble', 'spread', 'variational'],'next: causality and game theory'),"")]
