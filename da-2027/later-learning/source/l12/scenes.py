from lhelp import *
import codes
def d_tsum(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L12A)],30,150,690,13,17)
    if t>=ts[2]:
        for i,v in enumerate([2,7,11,15]):cell(d,780+i*64,190,58,40,str(v),GOLD if i<2 and t>=ts[2]+6 else TEAL,fs=18)
        lab(d,1000,260,"seen = {2:0}  →  7 needs 2  →  (0, 1)",WHITE,15)
    if t>=ts[3]:
        a=[-4,-1,-1,0,1,2]
        for i,v in enumerate(a):cell(d,780+i*64,330,58,40,str(v),TEAL,fs=18)
        step=int((t-ts[3])/2)%4;i,lo,hi=[(1,2,5),(1,3,5),(1,3,4),(2,3,5)][step]
        for idx,(n,c) in {i:("i",GOLD),lo:("lo",GRN),hi:("hi",RED)}.items():lab(d,780+idx*64+29,390,n,c,16)
        lab(d,1000,430,"i fixed, lo/hi move inward",WHITE,15)
    if t>=ts[4]:lab(d,1000,480,"[-1,-1,2]  [-1,0,1]",GOLD,20)
    tw(d,sc,t,5,"TWIST #1 — hash map = O(n); sort + pointers for 3-sum")
def d_pal(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L12B)],30,150,690,13,17)
    if t>=ts[2]:
        w="racecar";k=min(3,int((t-ts[2])/1.2))
        for i,ch in enumerate(w):cell(d,790+i*52,190,48,44,ch,GRN if (i<=k or i>=6-k) else TEAL,fs=20)
        lab(d,790+k*52+24,255,"i",GOLD,16);lab(d,790+(6-k)*52+24,255,"j",GOLD,16)
    if t>=ts[3]:
        a=[2,1,5,1,3,2]
        for i,v in enumerate(a):cell(d,790+i*52,320,48,40,str(v),GOLD if 2<=i<=4 else TEAL,fs=18)
        lab(d,1000,385,"window of 3: 5+1+3 = 9",WHITE,15)
    if t>=ts[4]:lab(d,1000,440,"sorted('listen') == sorted('silent')",GRN,16)
    tw(d,sc,t,5,"TWIST #2 — one pass instead of nested loops")
def d_wk(d,t,sc):walk(d,sc,t,[(WK12,1,2)])
SCENES=[("title",mk_title("Two Sum, Three Sum and Patterns","hashing · two pointers · sliding window"),""),("tsum",d_tsum,"Room 1 · Two/three sum"),("pal",d_pal,"Room 2 · Pointers and windows"),("wk",d_wk,"Walkthrough · two sum"),("end",mk_end("Problem patterns — complete",["hash map","two pointers","sliding window","anagram"],"last: neuromorphic"),"")]
