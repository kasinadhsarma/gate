from lhelp import *
import codes,math
def d_crit(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L33A)],30,150,690,15,20)
    a=Ax(790,200,440,220,(0,50),(0,700))
    if t>=ts[2]:
        a.axes(d,(0,25,50),(0,300,600));a.curve(d,lambda w:w*(50-w),TEAL,4);lab(d,1000,182,"area = w (50 − w)",WHITE,15)
    if t>=ts[3]:
        a.dot(d,25,625,GOLD,9);d.line([a.P(15,625),a.P(35,625)],fill=GOLD,width=3);lab(d,a.px(25),a.py(625)-18,"f' = 0, f'' = −2",GOLD,14)
    if t>=ts[4]:a.dot(d,0,0,RED,8);a.dot(d,50,0,RED,8)
    tw(d,sc,t,5,'TWIST #1 — reduce, differentiate, test, check ends')
def d_lag(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L33B)],30,150,690,15,20)
    cards(d,t,ts,[(2,"max of x·y with x + y = 10","x = y = 5,  product 25",GOLD),(2,"multiplier λ","5",TEAL),(3,"brute-force check","(25.0, 5.0)",GRN),(3,"closest point to the origin","(−1.2, 0.6),  d = 1.342",PUR)],770,200,470,48,12,16)
    tw(d,sc,t,5,'TWIST #2 — parallel gradients at the optimum')
def d_wk(d,t,sc):walk(d,sc,t,[(WK33,1,2)])
SCENES=[("title",mk_title('Calculus Optimization','critical points · second derivative · Lagrange'),""),("crit",d_crit,'Room 1 · Critical points'),("lag",d_lag,'Room 2 · Constraints'),("wk",d_wk,'Walkthrough · second derivative test'),("end",mk_end('Calculus optimization — complete',['objective', 'constraint', "f' = 0", 'Lagrange'],'next: LeetCode patterns'),"")]
