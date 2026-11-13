from lhelp import *
import codes
def d_lif(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L13A)],30,150,690,15,20)
    V=[0.3,0.57,0.81,0.73,1.16,0.5,0.45,0.41]
    if t>=ts[3]:
        a=Ax(790,200,430,230,(0,8),(0,1.3));a.axes(d,(0,2,4,6,8),(0,1));lab(d,1000,180,"membrane voltage",WHITE,16)
        d.line([a.P(0,1.0),a.P(8,1.0)],fill=RED,width=2);lab(d,1225,a.py(1.0)-10,"threshold",RED,14,"rm")
        n=min(8,int((t-ts[3])/0.7))
        pts=[a.P(i+.5,V[i]) for i in range(n)]
        if len(pts)>1:d.line(pts,fill=TEAL,width=4)
        for i in range(n):a.dot(d,i+.5,V[i],GOLD if i==4 else TEAL,5)
    if t>=ts[4]:lab(d,1000,470,"spikes: 0 0 0 0 1 0 0 0",GOLD,20)
    tw(d,sc,t,5,"TWIST #1 — spikes only when the threshold is crossed")
def d_stdp(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L13B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,880,175,"pre fires 2 ms BEFORE post",GRN,15)
        cell(d,790,195,70,36,"pre",TEAL,fs=16);arrow(d,(860,213),(940,213),GRN,4,10);cell(d,945,195,70,36,"post",PUR,fs=16)
    if t>=ts[3]:
        vbars(d,1060,190,130,[("+2",0.567),("w",0.5),("-2",0.433)],0.6,bw=44,gap=10,col=[GRN,GRY,RED],fs=13,fmt="{:.3f}")
    if t>=ts[4]:
        lab(d,1000,400,"2% of neurons active",WHITE,16);cs=14
        for i in range(100):d.rectangle((790+(i%25)*cs*1.2,420+(i//25)*cs*1.2,790+(i%25)*cs*1.2+cs,420+(i//25)*cs*1.2+cs),fill=GOLD if i%50==7 or i%50==31 else (30,34,66))
        lab(d,1000,500,"only 20 of 1000 do work",GOLD,16)
    tw(d,sc,t,5,"TWIST #2 — timing is the signal; silence is free")
def d_wk(d,t,sc):walk(d,sc,t,[(WK13,1,2)])
SCENES=[("title",mk_title("Neuromorphic Computing","spiking neurons · STDP"),""),("lif",d_lif,"Room 1 · Spiking neuron"),("stdp",d_stdp,"Room 2 · Spike timing"),("wk",d_wk,"Walkthrough · charging a neuron"),("end",mk_end("Neuromorphic — complete",["spikes","leak","STDP","energy"],"next: advanced data structures"),"")]
