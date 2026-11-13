from lhelp import *
import codes,math
def d_cause(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L24A)],30,150,690,15,20)
    P={"Z":(900,230),"X":(800,340),"Y":(1000,340)}
    if t>=ts[2]:
        for a,b in [("Z","X"),("Z","Y"),("X","Y")]:arrow(d,P[a],P[b],GRY,3,12)
        for n,(x,y) in P.items():node(d,x,y,n,GOLD if n=="Z" else TEAL,24,18)
        lab(d,1000,190,"Z = severity (hidden)",GOLD,14);lab(d,800,385,"X treatment",TEAL,14);lab(d,1000,385,"Y outcome",TEAL,14)
    cards(d,t,ts,[(2,"naive difference","-2.1",RED),(3,"adjusted for severity","+1.0",GRN)],770,430,470,40,8,16)
    tw(d,sc,t,5,'TWIST #1 — compare like with like, or randomise')
def d_game(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L24B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"prisoner's dilemma (row, column)",WHITE,15)
        pay={(0,0):"3,3",(0,1):"0,5",(1,0):"5,0",(1,1):"1,1"};nm=["C","D"]
        for r in range(2):
            lab(d,800,235+r*80,nm[r],GOLD,18)
            for c in range(2):
                nash=(r,c)==(1,1)
                cell(d,830+c*130,205+r*80,120,70,pay[(r,c)],GRN if (nash and t>=ts[2]+4) else TEAL,fs=20)
        for c in range(2):lab(d,890+c*130,190,nm[c],GOLD,18)
        if t>=ts[2]+4:lab(d,1000,385,"Nash equilibrium: (D, D)",GRN,18)
    if t>=ts[3]:lab(d,1000,440,"matching pennies: both settle near 0.5",GOLD,17)
    tw(d,sc,t,5,'TWIST #2 — best choices depend on the others')
def d_wk(d,t,sc):walk(d,sc,t,[(WK24,1,2)])
SCENES=[("title",mk_title('Causality and Game Theory','confounders · adjustment · Nash equilibrium'),""),("cause",d_cause,'Room 1 · Causality'),("game",d_game,'Room 2 · Game theory'),("wk",d_wk,'Walkthrough · naive comparison'),("end",mk_end('Causality and games — complete',['confounder', 'adjustment', 'Nash', 'mixed strategy'],'next: state space models, boosting, kernels'),"")]
