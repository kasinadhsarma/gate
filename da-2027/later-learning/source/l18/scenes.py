from lhelp import *
import codes
def d_dpa(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L18A),(4,L18B)],30,150,690,14,19)
    if ts[2]<=t<ts[4]:
        lab(d,1000,175,"mask = set of visited cities",WHITE,15)
        for i in range(4):cell(d,820+i*80,200,70,44,f"city {i}",GOLD if i in(0,1,3) else GRY,fs=15);lab(d,855+i*80,265,"1" if i in(0,1,3) else "0",GOLD if i in(0,1,3) else GRY,18)
        lab(d,1000,320,"mask 1011  →  {0, 1, 3}",WHITE,17)
        if t>=ts[2]+6:lab(d,1000,400,"best tour cost = 80",GRN,24)
    if t>=ts[4]:
        lab(d,1000,185,"orders of multiplication",WHITE,15)
        hbars(d,800,210,[("(AB)C",4500),("A(BC)",27000)],27000,w=240,col=[GRN,RED],lw=80,fmt="{:,}")
        if t>=ts[4]+4:lab(d,1000,320,"best = 4,500 operations",GRN,20)
    tw(d,sc,t,5,"TWIST #1 — compact state, reuse sub-answers")
def d_dpb(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L18C),(4,L18D)],30,150,690,15,20)
    if t<ts[4] and t>=ts[2]:
        P={1:(1000,215),2:(920,290),3:(1080,290),4:(870,365),5:(970,365)}
        for a,b in [(1,2),(1,3),(2,4),(2,5)]:edge(d,P[a],P[b])
        V={1:"3,3",2:"1,2",3:"1,0",4:"1,0",5:"1,0"}
        for n,(x,y) in P.items():
            node(d,x,y,str(n),TEAL,17);lab(d,x+34,y,"("+V[n]+")",GOLD,14,"lm")
        lab(d,1000,430,"(take, skip) per node",WHITE,15)
        if t>=ts[2]+8:lab(d,1000,470,"best independent set = 3",GRN,18)
    if t>=ts[4]:
        lab(d,1000,215,"numbers 1..50 without a digit 4",WHITE,16)
        lab(d,1000,270,"digit DP  →  36",GRN,24);lab(d,1000,320,"brute force  →  36",GOLD,24)
        lab(d,1000,380,"state = (position, still tight?)",WHITE,16)
    tw(d,sc,t,5,"TWIST #2 — the structure defines the state")
def d_str(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L18E),(4,L18F)],30,150,690,13,17)
    text="abababcababab"
    if t<ts[4] and t>=ts[2]:
        lab(d,1000,175,"text: abababcababab    pattern: abab",WHITE,15)
        for i,ch in enumerate(text):cell(d,790+i*34,200,30,34,ch,TEAL,fs=16)
        for k,p in enumerate([0,2,7,9]):
            if t>=ts[2]+8+k*1.3:
                for j in range(4):d.rectangle((790+(p+j)*34,200,790+(p+j)*34+30,234),outline=GOLD,width=3)
                lab(d,790+p*34+60,252+k*0,f"{p}",GOLD,15)
        lab(d,1000,330,"failure table of ababaca",WHITE,15)
        for i,v in enumerate([0,0,1,2,3,0,1]):cell(d,820+i*50,350,44,34,str(v),PUR,fs=16)
    if t>=ts[4]:
        lab(d,1000,185,"Z array of  aabcaab",WHITE,16)
        for i,(ch,v) in enumerate(zip("aabcaab",[0,1,0,0,3,1,0])):cell(d,820+i*50,210,44,34,ch,TEAL,fs=16);cell(d,820+i*50,250,44,34,str(v),GOLD if v==3 else PUR,fs=16)
        lab(d,1000,330,"rolling hash: drop one letter, add one letter",WHITE,15);lab(d,1000,365,"matches at 0, 2, 7, 9",GRN,18)
    tw(d,sc,t,5,"TWIST #3 — reuse what earlier comparisons told you")
def d_wk(d,t,sc):walk(d,sc,t,[(WK18,1,2)])
SCENES=[("title",mk_title("Advanced DP and String Matching","bitmask · matrix chain · tree/digit DP · KMP"),""),("dpa",d_dpa,"Room 1 · DP part 1"),("dpb",d_dpb,"Room 2 · DP part 2"),("str",d_str,"Room 3 · String matching"),("wk",d_wk,"Walkthrough · failure table"),("end",mk_end("Advanced DP and strings — complete",["bitmask","matrix chain","tree/digit DP","KMP / Z"],"next: number theory"),"")]
