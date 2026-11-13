from lhelp import *
import codes
def lcs_tab(a,b):
    t=[[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            t[i][j]=t[i-1][j-1]+1 if a[i-1]==b[j-1] else max(t[i-1][j],t[i][j-1])
    return t
def d_dp(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L1A)],30,150,690,15,19)
    if t>=ts[2]:
        lab(d,1000,165,"calls for fib(30)",WHITE,17)
        hbars(d,780,185,[("plain",1600000),("cached",31)],1600000,w=260,col=[RED,GRN],fmt="{:,}",lw=80)
    if t>=ts[4]:
        a,b="AGGTAB","GXTXAYB";T=lcs_tab(a,b);x0,y0,c=780,262,32
        lab(d,1000,248,"LCS table",WHITE,17)
        for j,ch in enumerate(b):lab(d,x0+(j+2)*c+c//2-c//2+0,y0+c//2,ch,GOLD,16)
        for i,ch in enumerate(a):lab(d,x0+c//2,y0+(i+1)*c+c//2,ch,GOLD,16)
        for i in range(1,7):
            for j in range(1,8):
                k=(i*7+j)/49
                if t>=ts[4]+0.5+k*5:cell(d,x0+j*c+c//2,y0+i*c,c,c,str(T[i][j]),TEAL if T[i][j]<4 else GOLD,fs=14)
    tw(d,sc,t,5,"TWIST #1 — DP = recursion + a table of answers")
def d_gr(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L1B1),(4,L1B2)],30,150,690,15,19)
    jobs=sorted([(1,4),(3,5),(0,6),(5,7),(8,9),(5,9)],key=lambda j:j[1]);pick={(1,4),(5,7),(8,9)}
    if t>=ts[2]:
        lab(d,1000,165,"jobs sorted by finish",WHITE,16)
        for i,(s,e) in enumerate(jobs):
            on=t>=ts[2]+1+i*.6;c=(GOLD if (s,e) in pick else GRY) if on else (60,66,100)
            rbox(d,(780+s*50,180+i*20,780+e*50,196+i*20),c,None,3)
    if t>=ts[3]:
        lab(d,1000,318,"make 11 with 1,5,6,9",WHITE,16)
        for i,(v,c) in enumerate([(9,RED),(1,RED),(1,RED)]):cell(d,780+i*44,330,40,32,str(v),c,fs=15)
        lab(d,945,346,"greedy: 3",RED,15,"lm")
        for i,(v,c) in enumerate([(6,GRN),(5,GRN)]):cell(d,1060+i*44,330,40,32,str(v),c,fs=15)
        lab(d,1150,346,"best: 2",GRN,15,"lm")
    if t>=ts[4]:
        sol=None
        def q(n,row=0,cols=()):
            if row==n:return cols
            for c in range(n):
                if all(c!=k and abs(c-k)!=row-r for r,k in enumerate(cols)):
                    r=q(n,row+1,cols+(c,))
                    if r:return r
        sol=q(6);cs=24;x0,y0=880,392
        lab(d,1000,378,"6 queens: 4 solutions",WHITE,16)
        for r in range(6):
            for c in range(6):d.rectangle((x0+c*cs,y0+r*cs,x0+c*cs+cs,y0+r*cs+cs),fill=(30,34,66) if (r+c)%2 else (20,24,50),outline=GRY)
        for r,c in enumerate(sol):
            if t>=ts[4]+0.8+r*0.7:ctext(d,(x0+c*cs+cs//2,y0+r*cs+cs//2),"Q",F(20,True),GOLD)
    tw(d,sc,t,5,"TWIST #2 — greedy needs a proof; DP is the fallback")
def d_wk(d,t,sc):walk(d,sc,t,[(WK1,1,2)])
SCENES=[("title",mk_title("Advanced DSA","dynamic programming · greedy · backtracking"),""),("dp",d_dp,"Room 1 · Dynamic programming"),("gr",d_gr,"Room 2 · Greedy and backtracking"),("wk",d_wk,"Walkthrough · memo"),("end",mk_end("Advanced DSA — complete",["memoisation","LCS table","greedy proof","backtracking"],"next: deep learning"),"")]
