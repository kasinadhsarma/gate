from lhelp import *
import codes
def d_q(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L5A)],30,150,690,15,20)
    V=[0.73,0.81,0.9,1.0,0.0]
    if t>=ts[2]:
        for i in range(5):cell(d,770+i*95,220,88,70,"GOAL" if i==4 else f"s{i}",GOLD if i==4 else TEAL,fs=16)
    if t>=ts[4]:
        for i in range(4):
            if t>=ts[4]+0.8+i*1.2:
                lab(d,770+i*95+44,320,f"Q={V[3-i] if False else V[i]}",WHITE,15);arrow(d,(770+i*95+20,350),(770+i*95+70,350),GRN,4,10)
        lab(d,960,400,"best action everywhere: go right",GRN,17)
    tw(d,sc,t,5,"TWIST #1 — values flow back from the goal")
def d_eps(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L5B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,170,"true win rate of each machine",WHITE,16)
        hbars(d,790,190,[("machine 1",30),("machine 2",50),("machine 3",80)],100,w=240,col=[RED,GOLD,GRN],lw=95,fmt="{:g}%")
    if t>=ts[3]:
        lab(d,1000,330,"wins in 2000 pulls",WHITE,16)
        vbars(d,830,355,130,[("eps 0",595),("eps 0.1",1520)],1600,bw=90,gap=60,col=[RED,GRN],fmt="{:,}")
    tw(d,sc,t,5,"TWIST #2 — explore a little to find better")
def d_wk(d,t,sc):walk(d,sc,t,[(WK5,1,2)])
SCENES=[("title",mk_title("Reinforcement Learning","Q-learning · explore vs exploit"),""),("q",d_q,"Room 1 · Q-learning"),("eps",d_eps,"Room 2 · Explore or exploit"),("wk",d_wk,"Walkthrough · Q update"),("end",mk_end("RL basics — complete",["reward","Q table","discount","epsilon"],"next: Bayesian methods"),"")]
