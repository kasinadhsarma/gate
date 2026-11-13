from lhelp import *
import codes,math
def d_ssm(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L25A)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"output after each input",WHITE,15);vbars(d,790,200,120,[("1",.5),("2",.4),("3",.32),("4",1.256),("5",1.005)],1.3,bw=50,gap=22,col=TEAL,fs=13,fmt="{:g}")
    if t>=ts[3]:lab(d,1000,375,"recurrence == convolution: True",GRN,17)
    if t>=ts[4]:hbars(d,790,415,[("SSM",1000),("attention",1000000)],1000000,w=240,col=[GRN,RED],lw=90,fmt="{:,}")
    tw(d,sc,t,5,'TWIST #1 — a recurrence with linear cost')
def d_boost(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L25B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"mean squared error after each round",WHITE,15)
        vbars(d,800,200,170,[("1",1.142),("2",.32),("3",.115),("4",.039)],1.2,bw=70,gap=30,col=[RED,GOLD,GOLD,GRN],fmt="{:g}")
    tw(d,sc,t,5,'TWIST #2 — each weak model fixes the last')
def d_kern(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L25C)],30,150,690,15,20)
    if t>=ts[2]:
        a=Ax(800,200,240,240,(-2,2),(-2,2));a.axes(d,(-1,1),(-1,1))
        for (x,y),c in [((1,1),GRN),((-1,-1),GRN),((1,-1),RED),((-1,1),RED)]:a.dot(d,x,y,c,9)
        lab(d,920,182,"XOR: no line separates",WHITE,14)
    cards(d,t,ts,[(2,"feature map dot","25.0",GOLD),(2,"kernel formula","25",GOLD),(3,"kernel perceptron on XOR","1, 1, -1, -1",GRN)],1060,210,190,50,10,13)
    tw(d,sc,t,5,'TWIST #3 — curved boundary for the price of a dot product')
def d_wk(d,t,sc):walk(d,sc,t,[(WK25,1,2)])
SCENES=[("title",mk_title('SSMs, Boosting and Kernels','Mamba idea · gradient boosting · kernel trick'),""),("ssm",d_ssm,'Room 1 · State space models'),("boost",d_boost,'Room 2 · Gradient boosting'),("kern",d_kern,'Room 3 · Kernels and SVMs'),("wk",d_wk,'Walkthrough · fading memory'),("end",mk_end('SSMs, boosting, kernels — complete',['state space', 'Mamba idea', 'boosting', 'kernel trick'],'next: reinforcement learning, decisions'),"")]
