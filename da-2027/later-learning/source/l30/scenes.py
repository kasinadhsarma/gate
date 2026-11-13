from lhelp import *
import codes,math
def d_mark(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L30A)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"stationary distribution",WHITE,15);hbars(d,790,200,[("sunny",0.833),("rainy",0.167)],1,w=240,col=[GOLD,TEAL],lw=80,fmt="{:.3f}")
    cards(d,t,ts,[(3,"random walk, 100 steps: variance","≈ 100",GRN)],770,330,470,44)
    tw(d,sc,t,5,'TWIST #1 — forget the start; spread like sqrt(time)')
def d_conc(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L30B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"P(|mean - 0.5| >= 0.1)",WHITE,15);hbars(d,790,200,[("simulated",0.0004),("Chebyshev",0.083),("Hoeffding",0.271)],0.3,w=220,col=[GRN,GOLD,RED],lw=100,fmt="{:g}")
    cards(d,t,ts,[(3,"sd of the mean: simulated","0.0289",TEAL),(3,"sigma / sqrt(n)","0.0289",GOLD)],770,340,470,44,10,16)
    tw(d,sc,t,5,'TWIST #2 — bounds for the worst case, CLT for typical')
def d_wk(d,t,sc):walk(d,sc,t,[(WK30,1,2)])
SCENES=[("title",mk_title('Advanced Probability 1','Markov chains · random walks · limit theorems'),""),("mark",d_mark,'Room 1 · Stochastic processes'),("conc",d_conc,'Room 2 · Concentration and CLT'),("wk",d_wk,'Walkthrough · Markov step'),("end",mk_end('Advanced probability 1 — complete',['Markov chain', 'random walk', 'Chebyshev', 'CLT'],'next: information theory and estimation'),"")]
