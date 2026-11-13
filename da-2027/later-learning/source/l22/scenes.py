from lhelp import *
import codes,math
def d_opt(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L22A)],30,150,690,15,20)
    if t>=ts[2]:
        a=Ax(790,200,260,230,(-2.3,2.3),(-4,6));a.axes(d,(-2,0,2),(-4,0,4));a.curve(d,lambda x:x**4-3*x**2+x,TEAL,4);lab(d,920,182,"two valleys",WHITE,14)
        if t>=ts[4]:a.dot(d,-1.301,-3.514,GRN,8);a.dot(d,1.131,-1.07,GOLD,8)
        cards(d,t,ts,[(2,"plain GD, 60 steps","0.323",GOLD),(2,"with momentum","0.0255",GRN),(3,"learning rate too big","5e12",RED)],1070,200,180,44,10,13)
    tw(d,sc,t,5,'TWIST #1 — start point and step size decide the ending')
def d_over(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L22B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"error by polynomial degree",WHITE,15)
        lab(d,880,200,"train",TEAL,13);vbars(d,790,215,150,[("1",.203),("3",.009),("9",0.0)],0.25,bw=40,gap=20,col=TEAL,fs=13,fmt="{:g}")
        lab(d,1130,200,"test",RED,13);vbars(d,1040,215,150,[("1",.207),("3",.02),("9",.027)],0.25,bw=40,gap=20,col=RED,fs=13,fmt="{:g}")
        lab(d,1000,420,"degree 9: train 0, test worse than degree 3",GOLD,16)
    tw(d,sc,t,5,'TWIST #2 — predict new data, not old data')
def d_wk(d,t,sc):walk(d,sc,t,[(WK22,1,2)])
SCENES=[("title",mk_title('Optimization and Overfitting','loss landscapes · momentum · generalisation'),""),("opt",d_opt,'Room 1 · Loss landscapes'),("over",d_over,'Room 2 · Overfitting'),("wk",d_wk,'Walkthrough · gradient step'),("end",mk_end('Optimization — complete',['valleys', 'momentum', 'overfitting', 'double descent'],'next: Bayesian methods and uncertainty'),"")]
