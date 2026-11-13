from lhelp import *
import codes
def d_att(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L3A)],30,150,690,15,20)
    if t>=ts[2]:
        for i,(n,c) in enumerate([("word 1",TEAL),("word 2",PUR),("word 3",GRN)]):cell(d,790+i*130,190,110,40,n,c,fs=16)
        lab(d,1000,260,"query: what am I looking for?",GOLD,15)
    if t>=ts[3]:
        lab(d,1000,300,"attention weights",WHITE,16)
        hbars(d,800,320,[("word 1",.412),("word 2",.203),("word 3",.384)],0.5,w=240,col=[TEAL,PUR,GRN],lw=80,fmt="{:.3f}")
    if t>=ts[4]:
        lab(d,1000,450,"output = weighted mix of values",WHITE,16);lab(d,1000,485,"[7.2, 2.8]",GOLD,28)
    tw(d,sc,t,5,"TWIST #1 — weighted average of values")
def d_temp(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L3B)],30,150,690,15,20)
    if t>=ts[3]:
        G=[("T=1",[.659,.242,.099]),("T=0.2",[.993,.007,0]),("T=3",[.445,.319,.236])]
        for i,(n,v) in enumerate(G):
            x=770+i*160;lab(d,x+60,170,n,GOLD,16)
            vbars(d,x,195,150,[("cat",v[0]),("dog",v[1]),("car",v[2])],1,bw=36,gap=10,col=[TEAL,PUR,RED],fs=12,fmt="{:.2f}")
    if t>=ts[4]:
        lab(d,1000,440,"4096 wide x 32 layers",WHITE,17);lab(d,1000,475,"~6 billion weights",GOLD,24)
    tw(d,sc,t,5,"TWIST #2 — temperature shapes the next-token choice")
def d_wk(d,t,sc):walk(d,sc,t,[(WK3,1,2)])
SCENES=[("title",mk_title("Transformers and LLMs","attention · temperature · size"),""),("att",d_att,"Room 1 · Attention"),("temp",d_temp,"Room 2 · Next token"),("wk",d_wk,"Walkthrough · softmax"),("end",mk_end("Transformers — complete",["query/key/value","softmax","temperature","stacked blocks"],"next: NLP and retrieval"),"")]
