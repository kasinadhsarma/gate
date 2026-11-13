from lhelp import *
import codes
def d_bp(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L2C)],30,150,690,16,21)
    if t>=ts[2]:
        a=Ax(790,185,430,290,(0,2.6),(0,22));a.axes(d,(0,1,2),(0,10,20));a.curve(d,lambda w:4.667*(w-2)**2,TEAL,4)
        lab(d,1000,165,"loss as w changes",WHITE,16)
        pts=[(0,ts[2]+1),(1.867,ts[4]),(1.991,ts[4]+3),(2.0,ts[4]+6)]
        for w,tt in pts:
            if t>=tt:a.dot(d,w,4.667*(w-2)**2,GOLD if w>1.9 else RED)
        if t>=ts[3]:lab(d,1000,500,"slope says: move w right",GRN,16)
    tw(d,sc,t,5,"TWIST #1 — backprop = chain rule, backwards")
def d_cnn(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L2A)],30,150,690,16,21)
    img=[[0,0,9,9]]*4;cs=44;x0,y0=780,200
    if t>=ts[2]:
        lab(d,x0+2*cs,180,"image",WHITE,16)
        for r in range(4):
            for c in range(4):
                v=img[r][c];d.rectangle((x0+c*cs,y0+r*cs,x0+c*cs+cs,y0+r*cs+cs),fill=(15,15,30) if v==0 else (240,220,120),outline=GRY)
    if t>=ts[3]:
        k=int(((t-ts[3])*1.2)%3);d.rectangle((x0+k*cs,y0,x0+k*cs+2*cs,y0+2*cs),outline=GOLD,width=4)
        lab(d,x0+2*cs,y0+4*cs+20,"filter [-1 +1] slides",GOLD,15)
    if t>=ts[4]:
        ox=1040;lab(d,ox+66,180,"output",WHITE,16)
        for r in range(3):
            for c in range(3):cell(d,ox+c*44,y0+r*44,44,44,"18" if c==1 else "0",GOLD if c==1 else GRY,fs=17)
    tw(d,sc,t,5,"TWIST #2 — shared weights, same filter everywhere")
def d_rnn(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L2B)],30,150,690,16,21)
    if t>=ts[3]:
        lab(d,1000,170,"memory h after each step",WHITE,16)
        vbars(d,800,195,150,[("step 1",.462),("step 2",.354),("step 3",.276),("step 4",.217)],0.5,bw=60,gap=26,col=TEAL,fmt="{:.3f}")
    if t>=ts[4]:
        lab(d,1000,380,"gradient after n steps",WHITE,16)
        vbars(d,800,405,100,[("5",0.768**5),("10",0.768**10),("20",0.768**20)],0.3,bw=70,gap=40,col=RED,fmt="{:.4f}")
    tw(d,sc,t,5,"TWIST #3 — vanishing gradients; LSTM/attention fix it")
def d_wk(d,t,sc):walk(d,sc,t,[(WK2,1,2)])
SCENES=[("title",mk_title("Deep Learning","backprop · CNN · RNN"),""),("bp",d_bp,"Room 1 · Backpropagation"),("cnn",d_cnn,"Room 2 · CNN"),("rnn",d_rnn,"Room 3 · RNN"),("wk",d_wk,"Walkthrough · convolution"),("end",mk_end("Deep learning — complete",["chain rule","shared filter","hidden state","vanishing gradient"],"next: transformers and LLMs"),"")]
