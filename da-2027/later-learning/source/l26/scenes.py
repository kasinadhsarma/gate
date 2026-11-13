from lhelp import *
import codes,math
def d_mdp(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L26A)],30,150,690,15,20)
    if t>=ts[2]:
        X=[820,1000,1180]
        for i in range(2):arrow(d,(X[i]+24,260),(X[i+1]-24,260),GRN,4,12)
        for i,n in enumerate(["s0","s1","end"]):node(d,X[i],260,n,GOLD if i==2 else TEAL,26,16)
        lab(d,910,235,"go: +1",GRN,14);lab(d,1090,235,"go: +10",GRN,14)
    cards(d,t,ts,[(3,"V(s1) after sweep 1","10.0",GOLD),(3,"V(s0) after sweep 2","10.0",GOLD),(4,"policy","go, go",GRN)],770,330,470,44,10,16)
    tw(d,sc,t,5,'TWIST #1 — a long plan as repeated one-step lookups')
def d_pg(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L26B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"true win rates",WHITE,15);hbars(d,790,200,[("arm 0",0.3),("arm 1",0.7)],1,w=240,col=[RED,GRN],lw=80)
    if t>=ts[3]:
        lab(d,1000,320,"learned P(pick arm 1)",WHITE,15);hbars(d,790,345,[("start",0.5),("after",0.97)],1,w=240,col=[GRY,GRN],lw=80)
    tw(d,sc,t,5,'TWIST #2 — make rewarded actions more likely')
def d_wk(d,t,sc):walk(d,sc,t,[(WK26,1,2)])
SCENES=[("title",mk_title('RL: Decision Making','MDPs · value iteration · policy gradients'),""),("mdp",d_mdp,'Room 1 · MDPs'),("pg",d_pg,'Room 2 · Policy gradients'),("wk",d_wk,'Walkthrough · Bellman backup'),("end",mk_end('RL decisions — complete',['MDP', 'Bellman', 'value iteration', 'policy gradient'],'next: advanced linear algebra'),"")]
