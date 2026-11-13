from lhelp import *
import codes,hashlib
def h(s):return int(hashlib.md5(s.encode()).hexdigest(),16)%10**6
def d_cache(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L9A)],30,150,690,16,21)
    if t>=ts[2]:lab(d,1000,190,"1,000,000 / 86,400 s",WHITE,17);lab(d,1000,225,"= 11.6 requests/second",GOLD,22);lab(d,1000,262,"peak: 3x to 10x",GRY,16)
    if t>=ts[4]:
        steps=[("put a,b",["a","b"]),("get a",["b","a"]),("put c",["a","c"])]
        for i,(n,sl) in enumerate(steps):
            if t>=ts[4]+i*2.2:
                y=320+i*60;lab(d,800,y+20,n,WHITE,16)
                for j,v in enumerate(sl):cell(d,880+j*70,y,60,40,v,GOLD if (i==2 and v=="c") else TEAL,fs=18)
        if t>=ts[4]+4.4:lab(d,1130,420,"b evicted",RED,16)
    tw(d,sc,t,5,"TWIST #1 — estimate first")
def d_ring(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L9B)],30,150,690,15,20)
    import math
    cx,cy,r=1000,350,120
    if t>=ts[2]:
        d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=GRY,width=2)
        cols={"A":TEAL,"B":PUR,"C":GRN,"D":GOLD};nodes=["A","B","C"]+(["D"] if t>=ts[3] else [])
        for n in nodes:
            for i in range(0,50,3):
                a=h(f"{n}{i}")/10**6*2*math.pi;d.ellipse((cx+r*math.cos(a)-6,cy+r*math.sin(a)-6,cx+r*math.cos(a)+6,cy+r*math.sin(a)+6),fill=cols[n])
        for n,c in cols.items():
            if n in nodes:lab(d,cx-50+"ABCD".index(n)*34,505,n,c,18)
    if t>=ts[3]+2:lab(d,cx,350,"24% of keys moved",GOLD,16)
    tw(d,sc,t,5,"TWIST #2 — move only what must move")
def d_wk(d,t,sc):walk(d,sc,t,[(WK9,1,2)])
SCENES=[("title",mk_title("System Design","capacity · caching · consistent hashing"),""),("cache",d_cache,"Room 1 · Cache"),("ring",d_ring,"Room 2 · Ring"),("wk",d_wk,"Walkthrough · LRU"),("end",mk_end("System design — complete",["estimates","LRU cache","hash ring","rebalancing"],"next: ML security"),"")]
