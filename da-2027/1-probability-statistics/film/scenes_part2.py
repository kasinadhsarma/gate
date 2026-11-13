from gcommon import *
import codes
def d_summ(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(2,codes.PA)],30,150,690,17,22)
    if t>=ts[2]:
        for i,(l,v,c) in enumerate([("mean 5.0",5.0,TEAL),("median 4.5",4.5,GOLD),("mode 4",4,PUR),("std dev 2.0",2.0,GRN)]):
            y=200+i*44;d.rectangle((790,y,790+int(v*50),y+30),fill=c);ctext(d,(800+int(v*50),y+15),l,F(15),WHITE,"lm")
    if t>=ts[4]:
        ctext(d,(1000,400),"with outlier 100:",F(17),RED);ctext(d,(1000,430),"mean 15.56   median 5",F(18,True),RED)
    tw(d,sc,t,5,"TWIST #1 — the mean chases outliers; the median does not")
def d_corr(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.PB)],30,150,690,17,22)
    ax=Ax(790,200,200,200,(0,7),(0,13));ax.axes(d,(),(),labels=False)
    if t>=ts[3]:
        for x,y in zip([1,2,3,4,5,6],[2.1,3.9,6.2,7.8,10.1,12.2]):ax.dot(d,x,y,GOLD,5)
        ctext(d,(890,180),"r = 0.9991",F(16),GOLD)
    ax2=Ax(1030,200,200,200,(-4,4),(-1,10));ax2.axes(d,(),(),labels=False)
    if t>=ts[5]:
        for z in range(-3,4):ax2.dot(d,z,z*z,RED,5)
        ctext(d,(1130,180),"y = x², covariance 0",F(16),RED)
    tw(d,sc,t,6,"TWIST #2 — r measures only LINEAR association")
def d_tt(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.PC)],30,150,690,17,22)
    ax=Ax(790,200,440,230,(-6,6),(0,0.45));ax.axes(d,(),(),labels=False)
    import math
    ax.curve(d,lambda x:math.exp(-x*x/2)/2.5066,TEAL,3)
    if t>=ts[4]:
        d.line([ax.P(2.262,0),ax.P(2.262,0.40)],fill=GOLD,width=3);d.line([ax.P(-2.262,0),ax.P(-2.262,0.40)],fill=GOLD,width=3)
        ctext(d,(1010,180),"critical ±2.262",F(16),GOLD)
        X,Y=ax.P(min(4.749,5.9),0);d.line([(X,Y),(X,Y-110)],fill=RED,width=4);ctext(d,(X-20,Y-125),"t = 4.749",F(16),RED,"rm")
        ctext(d,(1010,470),"t beyond the line → reject H0",F(18,True),RED)
    tw(d,sc,t,5,"TWIST #3 — t, not z, when σ is unknown")
def d_wk(d,t,sc):walk(d,sc,t,[(codes.WP1,1,3)])
SCENES=[("title",mk_title("The Statistics Clinic","summary statistics · correlation · t test"),""),("summ",d_summ,"Room 1 · Mean, median, mode"),("corr",d_corr,"Room 2 · Correlation"),("ttest",d_tt,"Room 3 · The t test"),("wk",d_wk,"Walkthrough · a tiny t test"),("end",mk_end("Statistics — complete",["mean/median/mode","covariance","correlation","t statistic"],"next: machine learning"),"")]
