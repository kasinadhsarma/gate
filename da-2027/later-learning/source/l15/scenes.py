from lhelp import *
import codes,hashlib
def d_bal(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L15A)],30,150,690,14,19)
    if t>=ts[2]:
        lab(d,880,175,"plain tree: a chain",RED,15)
        for i,k in enumerate([30,20,10]):node(d,800+i*10,215+i*50,str(k),RED)
        for i in range(2):edge(d,(800+i*10,215+i*50+17),(810+i*10,265+i*50-17),RED)
    if t>=ts[3]:
        lab(d,1100,175,"after rotate right",GRN,15)
        edge(d,(1100,215),(1060,270),GRN);edge(d,(1100,215),(1140,270),GRN)
        node(d,1100,215,"20",GRN);node(d,1060,270,"10",GRN);node(d,1140,270,"30",GRN)
    if t>=ts[4]:
        lab(d,1000,380,"1000 sorted keys",WHITE,16)
        hbars(d,800,400,[("plain",1000),("balanced",10)],1000,w=260,col=[RED,GRN],lw=90)
    tw(d,sc,t,5,"TWIST #1 — local rotations keep height ≈ log n")
def hh(w,i):return int(hashlib.md5(f"{i}{w}".encode()).hexdigest(),16)%64
def d_prob(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L15B),(4,L15C)],30,150,690,13,18)
    if ts[2]<=t<ts[4]:
        on=set()
        for w in ["apple","banana","cherry"]:on|={hh(w,i) for i in range(3)}
        ap={hh("apple",i) for i in range(3)};gr={hh("grape",i) for i in range(3)}
        lab(d,1000,175,"64 bits, 3 hashes per word",WHITE,15)
        for i in range(64):
            c=(GOLD if i in on else (30,34,66));x=800+(i%16)*26;y=200+(i//16)*26
            d.rectangle((x,y,x+22,y+22),fill=c,outline=GRY)
            if t>=ts[2]+4 and i in ap:d.rectangle((x,y,x+22,y+22),outline=GRN,width=3)
            if t>=ts[2]+8 and i in gr:d.rectangle((x,y,x+22,y+22),outline=RED,width=3)
        if t>=ts[2]+4:lab(d,1000,330,"apple: all 3 bits set → yes",GRN,16)
        if t>=ts[2]+8:lab(d,1000,360,"grape: some bit is 0 → no (always right)",RED,16)
    if t>=ts[4]:
        pts=[(2,3),(5,4),(9,6),(4,7),(8,1),(7,2)];a=Ax(800,200,420,260,(0,10),(0,8));a.axes(d,(0,5,10),(0,4,8))
        for p in pts:a.dot(d,p[0],p[1],TEAL,6)
        a.dot(d,9,2,GOLD,8);lab(d,a.px(9)+12,a.py(2)-12,"query",GOLD,14,"lm")
        if t>=ts[4]+6:a.dot(d,8,1,GRN,9);d.line([a.P(9,2),a.P(8,1)],fill=GRN,width=3);lab(d,1000,490,"nearest: (8, 1)",GRN,17)
    tw(d,sc,t,5,"TWIST #2 — trade exactness for space; skip regions")
def d_wk(d,t,sc):walk(d,sc,t,[(WK15,1,2)])
SCENES=[("title",mk_title("Balanced Trees, Bloom, k-d Trees","rotations · Bloom filter · nearest neighbour"),""),("bal",d_bal,"Room 1 · Balanced trees"),("prob",d_prob,"Room 2 · Bloom and k-d"),("wk",d_wk,"Walkthrough · balance check"),("end",mk_end("Advanced structures 2 — complete",["AVL rotation","B-tree idea","Bloom filter","k-d tree"],"next: shortest paths"),"")]
