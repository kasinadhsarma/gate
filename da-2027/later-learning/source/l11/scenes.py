from lhelp import *
import codes
def d_xor(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L11A)],30,150,690,15,20)
    if t>=ts[2]:
        nums=[4,1,2,1,2];run=[4,5,7,6,4]
        for i,n in enumerate(nums):
            if t>=ts[2]+1+i*1.3:cell(d,770+i*60,190,52,40,str(n),TEAL,fs=18);lab(d,796+i*60,260,f"x={run[i]}",GOLD,15)
    if t>=ts[4]:
        lab(d,1000,320,"n & (n-1)",WHITE,16)
        for i,(a,b,r) in enumerate([("10000","01111","00000  power of 2"),("10010","10001","10000  not")]):
            lab(d,800,355+i*40,f"{a} & {b} = {r}",GRN if i==0 else RED,15,"lm")
    tw(d,sc,t,5,"TWIST #1 — XOR cancels, n & (n-1) clears a bit")
def d_arr(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L11B)],30,150,690,15,20)
    if t>=ts[2]:
        M=[[1,2,3],[4,5,6]];lab(d,830,175,"M",WHITE,16)
        for r in range(2):
            for c in range(3):cell(d,780+c*44,190+r*44,44,44,str(M[r][c]),GOLD if (r,c)==(1,2) else TEAL,fs=16)
        lab(d,1060,175,"transpose",WHITE,16)
        for r in range(3):
            for c in range(2):cell(d,1020+c*44,190+r*44,44,44,str(M[c][r]),PUR,fs=16)
    if t>=ts[3]:
        lab(d,1000,350,"cube[1][0][1] = 7",WHITE,16)
        for k in range(2):
            for r in range(2):
                for c in range(2):cell(d,800+k*130+c*40,370+r*40,40,40,"7" if (k,r,c)==(1,0,1) else "0",GOLD if (k,r,c)==(1,0,1) else GRY,fs=15)
    if t>=ts[4]:
        pre=[0,3,4,8,9,14]
        for i,v in enumerate(pre):cell(d,780+i*70,470,64,36,str(v),GRN if i in (1,4) else TEAL,fs=16)
        lab(d,1000,525,"pre[4] - pre[1] = 6",GOLD,16)
    tw(d,sc,t,5,"TWIST #2 — precompute once, query instantly")
def d_wk(d,t,sc):walk(d,sc,t,[(WK11,1,2)])
SCENES=[("title",mk_title("Bits, Arrays, Prefix Sums","XOR · 2D/3D arrays"),""),("xor",d_xor,"Room 1 · XOR"),("arr",d_arr,"Room 2 · Arrays"),("wk",d_wk,"Walkthrough · XOR"),("end",mk_end("Bits and arrays — complete",["XOR","power of two","2D / 3D","prefix sums"],"next: two sum and friends"),"")]
