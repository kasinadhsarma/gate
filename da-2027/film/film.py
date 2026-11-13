import json, math, random, sys, subprocess, os
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720; FPS=30
FD="/usr/share/fonts/truetype/dejavu/"
_f={}
def F(sz,b=True,mono=False):
    k=(sz,b,mono)
    if k not in _f:
        n="DejaVuSansMono-Bold.ttf" if mono and b else "DejaVuSansMono.ttf" if mono else "DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"
        _f[k]=ImageFont.truetype(FD+n,sz)
    return _f[k]
META=json.load(open("meta.json"))
COL={"N":(180,190,220),"R":(110,170,255),"S":(255,170,90)}
NAME={"N":"Narrator","R":"Ramu","S":"Somu"}
GOLD=(255,205,70);TEAL=(70,210,190);RED=(245,90,90);GRN=(110,220,130);PUR=(170,130,255);GRY=(70,78,105);WHITE=(240,244,255)
def ease(x):
    x=max(0,min(1,x));return x*x*(3-2*x)
def clamp(x,a=0,b=1):return max(a,min(b,x))
BG=Image.new("RGB",(W,H))
_d=ImageDraw.Draw(BG)
for y in range(H):
    k=y/H;_d.line([(0,y),(W,y)],fill=(int(10+14*k),int(14+8*k),int(36+30*k)))
rnd=random.Random(5)
for _ in range(90):
    x,y=rnd.randint(0,W),rnd.randint(0,H);c=rnd.randint(60,130);_d.point((x,y),fill=(c,c,c+30))

def ctext(d,xy,s,font,fill=WHITE,anchor="mm"):d.text(xy,s,font=font,fill=fill,anchor=anchor)
def rbox(d,box,fill,outline=None,r=10,w=2):d.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=w)
def wrap(s,font,maxw,d):
    out=[];cur=""
    for wd in s.split():
        t=(cur+" "+wd).strip()
        if d.textlength(t,font=font)<=maxw:cur=t
        else:out.append(cur);cur=wd
    out.append(cur);return out
def banner(d,t0,t,text,col=GOLD,y=108):
    a=ease((t-t0)/0.5)
    if a<=0:return
    f=F(30);wd=d.textlength(text,font=f)+60;x0=W//2-wd/2;yy=y-(1-a)*20
    rbox(d,(x0,yy-26,x0+wd,yy+26),(30,24,10),col,12,3);ctext(d,(W//2,yy),text,f,col)
def avatar(d,x,y,col,name,active,t):
    b=-8*abs(math.sin(t*9)) if active else 0
    if active:d.ellipse((x-52,y-52+b,x+52,y+52+b),fill=tuple(int(c*0.35) for c in col))
    d.ellipse((x-38,y-38+b,x+38,y+38+b),fill=col,outline=WHITE,width=3)
    for dx in(-14,14):
        d.ellipse((x+dx-9,y-14+b,x+dx+9,y+4+b),fill=WHITE,outline=(30,30,60),width=2);d.ellipse((x+dx-3,y-8+b,x+dx+3,y-2+b),fill=(20,20,40))
    if active:d.ellipse((x-10,y+14+b,x+10,y+26+b),fill=(60,20,30))
    else:d.arc((x-14,y+8+b,x+14,y+26+b),20,160,fill=(30,30,60),width=3)
    ctext(d,(x,y+60),name,F(18),WHITE)

class Sc:
    def __init__(s,key):
        s.key=key;L=META[key];s.L=L;s.ts=[];t=0.7
        for sp,tx,p,du in L:s.ts.append(t);t+=du+0.35
        s.dur=t+0.65
    def cur(s,t):
        c=-1
        for i,(sp,tx,p,du) in enumerate(s.L):
            if s.ts[i]<=t<s.ts[i]+du+0.25:c=i
        return c

def frame(sc,t,draw_fn,chapter):
    im=BG.copy();d=ImageDraw.Draw(im)
    c=sc.cur(t)
    if chapter:
        ctext(d,(34,34),chapter,F(22),(150,160,200),"lm")
    draw_fn(d,t,sc)
    # avatars + caption
    spk=sc.L[c][0] if c>=0 else None
    avatar(d,80,628,COL["R"],"Ramu",spk=="R",t);avatar(d,190,628,COL["S"],"Somu",spk=="S",t)
    if c>=0:
        sp,tx=sc.L[c][0],sc.L[c][1]
        f=F(25,False);ls=wrap(tx,f,900,d);h=len(ls)*32+34;y0=H-18-h
        rbox(d,(262,y0,1262,H-18),(14,18,40),COL[sp],12,2)
        d.text((278,y0+8),NAME[sp],font=F(16),fill=COL[sp])
        for i,l in enumerate(ls):d.text((278,y0+30+i*32),l,font=f,fill=WHITE)
    return im
# ---------------------------------------------------------------- scenes
def d_title(d,t,sc):
    for i in range(14):
        x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
    a=ease(t/1.5)
    ctext(d,(W//2,250),"OPERATION  GATE",F(84),GOLD)
    ctext(d,(W//2,350),"The Night Library",F(50),WHITE)
    if t>1.6:ctext(d,(W//2,430),"a mathematics, data structures and algorithms film in twelve twists",F(26,False),(170,180,215))
    if t>3.2:ctext(d,(W//2,500),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
def d_s1(d,t,sc):
    ts=sc.ts;n=28;x0=70;w=36;gap=4
    rr=random.Random(3)
    cols=[tuple(rr.randint(70,200) for _ in range(3)) for _ in range(n)]
    for r in range(2):
        y=250+r*0
    pr=clamp((t-ts[1])/(ts[4]+2.2-ts[1]));pr=ease(pr) if t>ts[3] else pr
    idx=int(clamp((t-ts[1])/(ts[4]+2.0-ts[1]))**1.0*(n-1)) if t>ts[1] else -1
    for i in range(n):
        x=x0+i*(w+gap);last=(i==n-1);h=150 if last else 120+(i*37)%40
        col=GOLD if last and t>ts[0]+3 else cols[i]
        if i==idx:col=tuple(min(255,c+70) for c in col)
        rbox(d,(x,390-h,x+w,390),col,WHITE if i==idx else None,5,3)
    if idx>=0:
        x=x0+idx*(w+gap)+w/2;d.polygon([(x,410),(x-12,436),(x+12,436)],fill=TEAL)
        ctext(d,(x,452),"Ramu",F(16),TEAL)
    ctext(d,(W//2,190),"1,000,000 shelves  ·  one missing book",F(30),WHITE)
    ctext(d,(x0+(n-1)*(w+gap)+w/2-30,412),"the Golden Algorithm",F(16),GOLD)
    if t>ts[1]:
        k=int(1_000_000*clamp((t-ts[1])/(ts[4]+2.0-ts[1]))**2.2)
        ctext(d,(W//2,505),f"shelves checked: {k:,}",F(40),TEAL)
    if t>ts[2]+3.5:ctext(d,(W//2,556),"linear search:  Θ(n)   ·   1 shelf/sec  =  11.6 days",F(28),RED)
    banner(d,ts[4],t,"TWIST #6 — it was on the LAST shelf",GOLD,115)
def bs_steps(a,tg):
    lo,hi=0,len(a)-1;S=[]
    while lo<=hi:
        m=(lo+hi)//2;S.append((lo,hi,m))
        if a[m]==tg:break
        if a[m]<tg:lo=m+1
        else:hi=m-1
    return S
A32=[3*i+2 for i in range(32)];TG=A32[22];BSS=bs_steps(A32,TG)
def d_s2(d,t,sc):
    ts=sc.ts;ctext(d,(W//2,180),f"sorted shelves — find {TG}",F(32),WHITE)
    step=int(clamp((t-ts[1])/ (ts[4]-ts[1]),0,0.999)*len(BSS)) if t>=ts[1] else -1
    lo,hi,m=(BSS[step] if step>=0 else (0,31,-1))
    w=34
    for i in range(32):
        x=36+i*(w+3);dead=(step>=0 and (i<lo or i>hi));col=(40,46,70) if dead else (70,90,150)
        if i==m:col=GOLD
        rbox(d,(x,250,x+w,320),col,None,5);ctext(d,(x+w/2,285),str(A32[i]),F(12),(15,15,30) if i==m else (200,205,230))
        if i==m:d.polygon([(x+w/2,332),(x+w/2-9,350),(x+w/2+9,350)],fill=GOLD);ctext(d,(x+w/2,368),"mid",F(14),GOLD)
        if i==lo and step>=0:ctext(d,(x+w/2,236),"lo",F(14),TEAL)
        if i==hi and step>=0:ctext(d,(x+w/2,236),"hi",F(14),PUR)
    if step>=0:ctext(d,(W//2,430),f"question {step+1}: is {A32[m]} {'the one!' if A32[m]==TG else ('too small → keep the right half' if A32[m]<TG else 'too big → keep the left half')}",F(28),TEAL)
    if t>ts[4]:ctext(d,(W//2,500),"1,048,576 shelves  →  only 20 questions",F(34),GOLD);ctext(d,(W//2,548),"binary search:  Θ(log n)",F(28),GRN)
    banner(d,ts[5],t,"TWIST #7 — it only works while the order holds",PUR,115)
import random as _r
_rr=_r.Random(11);ARR=list(range(1,17));_rr.shuffle(ARR)
def msort_states(a):
    st=[(a[:],16)];w=1;cur=a[:]
    ws=[16,8,4,2,1]
    S=[(a[:],x) for x in ws]
    w=1
    while w<len(cur):
        nxt=[]
        for i in range(0,len(cur),2*w):nxt+=sorted(cur[i:i+2*w])
        cur=nxt;S.append((cur[:],2*w if 2*w<16 else 16));w*=2
    return S
MS=msort_states(ARR)
def d_s3(d,t,sc):
    ts=sc.ts
    if t<ts[2]:
        ctext(d,(W//2,190),"the Shuffler strikes!",F(34),RED);arr=ARR;grp=1;shake=6*math.sin(t*40)
        gi=None
    else:
        ctext(d,(W//2,190),"divide, conquer, combine",F(34),WHITE)
        k=int(clamp((t-ts[2])/(ts[6]-ts[2]),0,0.999)*len(MS));arr,grp=MS[k];shake=0
    n=16;bw=50;x0=(W-(n*bw+ (n//grp-1)*0))//2
    gap=10 if t>=ts[2] else 0
    for i,v in enumerate(arr):
        g=i//grp if grp else 0
        x=x0+i*bw+g*gap-(n//grp)*gap//2+int(shake*(1 if i%2 else -1))
        h=v*13;col=tuple(int(c) for c in (70+v*8,140,255-v*9))
        rbox(d,(x,520-h,x+bw-6,520),col,None,4);ctext(d,(x+bw/2-3,508),str(v),F(15),(10,10,30))
    if t>=ts[2]:
        lab="split until single books" if k<5 else "merge: always take the smaller front book"
        ctext(d,(W//2,560),lab,F(26),TEAL)
    if t>ts[5]:
        rbox(d,(150,225,1130,300),(20,24,50),GOLD,12);ctext(d,(W//2,250),"bubble sort ≈ 5×10¹¹ comparisons    merge sort ≈ 2×10⁷",F(28),GOLD)
        ctext(d,(W//2,282),"n per level  ×  log n levels  =  Θ(n log n)",F(22,False),WHITE)
    banner(d,ts[6],t,"TWIST #8 — no comparison sort beats n log n",TEAL,128)
def d_s4(d,t,sc):
    ts=sc.ts
    def hx(k):return (3*k)%10
    ev=[(1,ts[2]),(4,ts[2]+1.1),(5,ts[2]+2.2),(6,ts[2]+3.3),(14,ts[3]+0.8),(15,ts[4]+3.0)]
    table={}
    sw=84;x0=(W-10*sw)//2;y0=340
    ctext(d,(W//2,190),"hash:  h(k) = 3k mod 10     linear probing",F(32),WHITE)
    cur=None;msg=""
    for k,tt in ev:
        if t<tt:continue
        home=hx(k);slot=home;probes=[home]
        while slot in table:slot=(slot+1)%10;probes.append(slot)
        el=t-tt;stepd=0.8
        npro=min(len(probes),int(el/stepd)+1)
        if el>=stepd*len(probes):
            table[slot]=k
        else:
            cur=(k,probes,npro)
    for i in range(10):
        x=x0+i*sw;rbox(d,(x,y0,x+sw-8,y0+90),(26,32,66),(90,100,150),8,2);ctext(d,(x+sw/2-4,y0+112),str(i),F(18),(150,160,200))
        if i in table:rbox(d,(x+6,y0+10,x+sw-14,y0+80),TEAL,None,8);ctext(d,(x+sw/2-4,y0+45),str(table[i]),F(30),(10,20,30))
    if cur:
        k,pr,npro=cur
        for j in range(npro):
            s=pr[j];x=x0+s*sw;busy=(j<len(pr)-1)
            rbox(d,(x,y0,x+sw-8,y0+90),(70,26,34) if busy else (24,70,50),RED if busy else GRN,8,4)
        s=pr[npro-1];x=x0+s*sw
        ctext(d,(x+sw/2-4,y0-50),f"key {k}",F(30),GOLD);d.polygon([(x+sw/2-4,y0-22),(x+sw/2-14,y0-6),(x+sw/2+6,y0-6)],fill=GOLD)
        ctext(d,(W//2,520),(f"{k} → home slot {pr[0]}" if npro==1 else f"slot {pr[npro-2]} is busy → probe slot {pr[npro-1]}"),F(28),TEAL if npro==len(pr) else RED)
    if t>ts[5]:
        ctext(d,(W//2,570),"expected probes ≈ 1 / (1 − α)  →  α = 0.9  gives 10",F(28),GOLD)
    banner(d,ts[5],t,"TWIST #9 — the fuller the table, the slower it gets",RED,115)
def d_s5(d,t,sc):
    ts=sc.ts
    code=["def append_to_lst(val, lst=[]):","    lst.append(val)","    return lst","","print(append_to_lst(1))","print(append_to_lst(2))","print(append_to_lst(3, []))"]
    rbox(d,(60,200,640,480),(18,22,46),(90,100,150),12,2)
    for i,l in enumerate(code):d.text((84,216+i*34),l,font=F(22,False,True),fill=(210,220,250))
    # ghost
    gx,gy=900,300;bob=8*math.sin(t*2.5)
    d.pieslice((gx-70,gy-70+bob,gx+70,gy+70+bob),180,360,fill=(230,235,255));d.rectangle((gx-70,gy+bob,gx+70,gy+80+bob),fill=(230,235,255))
    for i in range(4):d.ellipse((gx-70+i*35,gy+62+bob,gx-35+i*35,gy+98+bob),fill=(230,235,255))
    for dx in(-22,22):d.ellipse((gx+dx-8,gy-20+bob,gx+dx+8,gy+6+bob),fill=(20,20,50))
    ctext(d,(gx,gy-110+bob),"the shared default list",F(20),(200,210,240))
    c1=t>ts[3]+0.5;c2=t>ts[3]+2.0;c3=t>ts[3]+3.5
    lst="[]" if not c1 else ("[1]" if not c2 else "[1, 2]")
    rbox(d,(780,390,1020,445),(30,40,80),PUR,10,3);ctext(d,(900,418),"lst = "+lst,F(28,True,True),WHITE)
    outs=[("[1]",c1),("[1, 2]",c2),("[3]",c3)]
    for i,(o,sh) in enumerate(outs):
        if sh:ctext(d,(1150,260+i*44),">>> "+o,F(28,True,True),GRN if i<2 else TEAL,"lm") if False else d.text((690,490+i*0),"",font=F(10))
    y=500
    for i,(o,sh) in enumerate(outs):
        if sh:
            d.text((90+i*200,y),o,font=F(34,True,True),fill=RED if i==1 else GRN)
    if c3:rbox(d,(1050,390,1230,445),(24,70,50),GRN,10,3);ctext(d,(1140,418),"fresh [3]",F(24,True,True),GRN)
    if c2:ctext(d,(W//2,552),"call 2 did not start from empty — the ghost remembered",F(24),RED)
    banner(d,ts[4],t,"TWIST #10 — mutable defaults remember",PUR,125)
G6={0:(220,360),1:(380,260),2:(380,470),3:(580,250),4:(580,480),5:(780,360),6:(780,540)}
E6=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5),(4,6)]
DIST={0:0,1:1,2:1,3:2,4:2,5:3,6:3}
LC=[GOLD,TEAL,GRN,PUR]
def d_s6(d,t,sc):
    ts=sc.ts
    ctext(d,(W//2,180),"the city map",F(30),WHITE)
    for a,b in E6:d.line([G6[a],G6[b]],fill=(90,100,150),width=4)
    dfs_start=ts[4];order=[0,1,3,5,4,2]
    lev=int(clamp((t-ts[1])/1.7,0,10)) if t>=ts[1] and t<dfs_start else (4 if t>=dfs_start else -1)
    onpath=[];back=False
    if t>=dfs_start:
        k=int((t-dfs_start)/0.9);onpath=order[:min(len(order),k+1)]
        back=k>=len(order)
    for n,(x,y) in G6.items():
        col=(50,58,95)
        if lev>=0 and DIST[n]<=lev-1 or (t>=ts[1] and t<dfs_start and DIST[n]<=lev):col=LC[DIST[n]]
        if t>=dfs_start:col=PUR if n in onpath else (50,58,95)
        d.ellipse((x-26,y-26,x+26,y+26),fill=col,outline=WHITE,width=3)
        ctext(d,(x,y),"L" if n==0 else str(n),F(22),(10,10,30))
        if t<dfs_start and t>=ts[1] and DIST[n]<=lev:ctext(d,(x,y+44),f"dist {DIST[n]}",F(16),col)
    if t<dfs_start and t>=ts[1]:
        q={0:["L"],1:["1","2"],2:["3","4"],3:["5","6"]}.get(min(lev,3),["L"])
        ctext(d,(990,300),"queue →",F(22),(170,180,215));
        for i,s in enumerate(q):rbox(d,(1060+i*52,278,1106+i*52,322),LC[min(lev,3)],None,6);ctext(d,(1083+i*52,300),s,F(22),(10,10,30))
        ctext(d,(1030,380),"BFS = a ripple\nfewest roads first",F(24),TEAL)
    if t>=dfs_start:
        ctext(d,(1030,300),"DFS dives deep:\n L → 1 → 3 → 5 → 4 → 2",F(24),PUR)
        if back:
            d.line([G6[2],G6[0]],fill=RED,width=8);ctext(d,(1000,440),"road 2 → L leads back\nto an OPEN junction!",F(22),RED)
    banner(d,ts[5],t,"TWIST #11 — a back edge means a cycle",RED,115)
G7={0:(520,300),1:(980,300),2:(520,470),3:(760,470),4:(760,250),5:(300,380)}
E7=[(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
TOP=[4,5,2,0,3,1]
def d_s7(d,t,sc):
    ts=sc.ts;ctext(d,(W//2,180),"morning routine: arrows mean 'must happen before'",F(28),WHITE)
    k=int(clamp((t-ts[2]-1.0)/1.4,0,6)) if t>=ts[2]+1.0 else 0
    gone=TOP[:k]
    for a,b in E7:
        (x1,y1),(x2,y2)=G7[a],G7[b];col=(50,56,88) if a in gone else (130,145,200)
        d.line([(x1,y1),(x2,y2)],fill=col,width=4)
        ang=math.atan2(y2-y1,x2-x1);ex,ey=x2-30*math.cos(ang),y2-30*math.sin(ang)
        d.polygon([(ex+12*math.cos(ang),ey+12*math.sin(ang)),(ex-8*math.sin(ang),ey+8*math.cos(ang)),(ex+8*math.sin(ang),ey-8*math.cos(ang))],fill=col)
    ind={n:sum(1 for a,b in E7 if b==n and a not in gone) for n in G7}
    for n,(x,y) in G7.items():
        col=(45,52,85) if n in gone else (GRN if ind[n]==0 else (80,100,170))
        d.ellipse((x-27,y-27,x+27,y+27),fill=col,outline=WHITE,width=3);ctext(d,(x,y),str(n),F(24),(10,10,30) if n not in gone else (110,120,150))
        if n not in gone:ctext(d,(x,y-44),f"in:{ind[n]}",F(16),GRN if ind[n]==0 else (170,180,215))
    ctext(d,(W//2,590-52),"order:  "+"  ".join(str(x) for x in gone),F(34,True,True),GOLD)
    banner(d,ts[3],t,"TWIST #12 — leftovers = a hidden cycle",PUR,128)
def mtree():
    nodes=[];cnt=[0]
    def build(n,dep):
        node={"n":n,"d":dep,"i":len(nodes),"c":[]};nodes.append(node)
        if n>0:
            node["c"]=[build(n-1,dep+1),build(n-2,dep+1)]
        return node
    r=build(4,0);leaf=[0]
    def pos(nd):
        if not nd["c"]:nd["x"]=leaf[0];leaf[0]+=1
        else:
            for c in nd["c"]:pos(c)
            nd["x"]=sum(c["x"] for c in nd["c"])/2
    pos(r);return nodes
MT=mtree();MCOL={4:GOLD,3:TEAL,2:GRN,1:PUR}
def d_s8(d,t,sc):
    ts=sc.ts;ctext(d,(W//2,170),"mystery(4)",F(30,True,True),WHITE)
    k=int(clamp((t-ts[1]-0.2)/0.38,0,15)) if t>=ts[1]+0.2 else 0
    k=min(k,len(MT));seen=set();memo=t>ts[3]
    nl=len([x for x in MT]);sp=70;x0=(W-14*sp)//2
    for nd in MT[:k]:
        x=x0+nd["x"]*sp;y=215+nd["d"]*72
        for c in nd["c"]:
            if c["i"]<k:d.line([(x,y),(x0+c["x"]*sp,215+c["d"]*72)],fill=(90,100,150),width=3)
    for nd in MT[:k]:
        x=x0+nd["x"]*sp;y=215+nd["d"]*72;n=nd["n"];key=n if n>0 else 0
        col=MCOL.get(n,(120,125,150))
        dup=(key in seen) if memo else False;seen.add(key)
        if memo and dup:col=(45,50,75)
        d.ellipse((x-24,y-24,x+24,y+24),fill=col,outline=WHITE if not dup else (80,90,120),width=2)
        ctext(d,(x,y),str(n) if n>0 else "b",F(20),(10,10,30) if not dup else (110,120,150))
    ctext(d,(W//2,566),f"calls so far: {k}" if not memo else "memo: 15 calls → 5 distinct problems (n = 4, 3, 2, 1, base)",F(26),GOLD if not memo else GRN)
    if t>ts[3]:ctext(d,(W//2,640-8),"",F(10))
    banner(d,ts[4],t,"FINAL TWIST — easy problems, asked too many times",GOLD,115)
def d_end(d,t,sc):
    ts=sc.ts;ctext(d,(W//2,150),"the toolbox",F(40),GOLD)
    cards=[("linear search","Θ(n)",RED),("binary search","Θ(log n)",GRN),("merge sort","Θ(n log n)",TEAL),("hash lookup","Θ(1) avg",PUR),("Euclid GCD","Θ(log n)",GOLD),("sieve","Θ(n log log n)",GRN),("fast power","Θ(log e)",TEAL),("BFS / DFS","Θ(V+E)",PUR)]
    for i,(a,b,c) in enumerate(cards):
        al=ease((t-ts[1]-i*0.45)/0.5) if t>ts[1] else 0
        if al<=0:continue
        x=70+(i%4)*285;y=210+(i//4)*125-(1-al)*30
        rbox(d,(x,y,x+265,y+105),(20,26,56),c,14,3);ctext(d,(x+132,y+34),a,F(20),WHITE);ctext(d,(x+132,y+74),b,F(26),c)
    if t>ts[2]:ctext(d,(W//2,490),"GATE DA 2027  ·  Google prep",F(34),WHITE)
    if t>ts[3]:ctext(d,(W//2,540),"github.com/kasinadhsarma/gate  →  da-2027/",F(24,False),TEAL)

def show(d,t,ts,k,xy,text,font,col=WHITE,anchor="lm"):
    if t>=ts[k]:ctext(d,xy,text,font,col,anchor)
def d_m1(d,t,sc):
    ts=sc.ts;ctext(d,(W//2,170),"17 sweets, 5 friends",F(30),WHITE)
    for i in range(17):
        g,pos=(i//3,i%3) if i<15 else (5,i-15)
        x=110+g*115+(pos*30 if g<5 else 0);y=260+(pos*34 if g<5 else 0)
        if g==5:x=700+pos*34+0;y=300
        col=[TEAL,GRN,PUR,GOLD,(255,140,200)][g] if g<5 else RED
        if g<5:d.ellipse((110+g*115,260+pos*38,110+g*115+30,290+pos*38),fill=col)
        else:d.ellipse((700+pos*38,300,730+pos*38,330),fill=col)
    for g in range(5):ctext(d,(125+g*115,390),f"friend {g+1}",F(15),(170,180,215))
    ctext(d,(715,360),"left over",F(16),RED)
    L=[("17 / 5  =  3.4",2),("17 // 5  =  3   (quotient)",2),("17 % 5  =  2   (remainder)",2),("a = b·q + r :   17 = 5·3 + 2",3)]
    for j,(tx,k) in enumerate(L):
        if t>=ts[k]+j*1.6-(0 if k==2 else 0)*0:ctext(d,(110,455+j*34),tx,F(26,True,True),[TEAL,GRN,RED,GOLD][j],"lm")
    if t>=ts[5]:
        rbox(d,(760,420,1240,545),(20,24,50),RED,12,2)
        ctext(d,(1000,448),"negatives (floor goes DOWN)",F(20),RED)
        ctext(d,(1000,485),"-17 // 5  =  -4",F(28,True,True),WHITE);ctext(d,(1000,520),"-17 %  5  =   3",F(28,True,True),WHITE)
    banner(d,ts[6],t,"TWIST #1 — floor means down, not toward zero",GOLD,115)
def d_m2(d,t,sc):
    ts=sc.ts;ctext(d,(W//2,170),"two ropes: 48 m and 18 m",F(30),WHITE)
    u=8;x0,y0=90,230
    d.rectangle((x0,y0,x0+48*u,y0+18*u),fill=(30,36,70),outline=WHITE,width=2)
    if t>=ts[1]:
        a=ease((t-ts[1])/2)
        for i in range(8):
            for j in range(3):
                if (i*3+j)/24<=a:rbox(d,(x0+i*6*u+2,y0+j*6*u+2,x0+(i+1)*6*u-2,y0+(j+1)*6*u-2),(70,120,200),None,4)
        ctext(d,(x0+24*u,y0+18*u+26),"tiles of 6 × 6 fit exactly:  GCD = HCF = 6",F(22),GOLD)
    steps=[(48,18),(18,12),(12,6),(6,0)]
    for j,(a,b) in enumerate(steps):
        if t>=ts[2]+j*2.2:
            ctext(d,(560+0,470+j*0),"",F(10))
            ctext(d,(x0+j*215,475),f"({a}, {b})",F(30,True,True),TEAL if b else GOLD,"lm")
            if j<3:ctext(d,(x0+j*215+150,475),"→",F(30),(150,160,200),"lm")
    if t>=ts[2]:ctext(d,(x0,520),"(a, b)  →  (b, a mod b)   until b = 0",F(22),(170,180,215),"lm")
    if t>=ts[5]:
        rbox(d,(770,215,1240,385),(20,24,50),GOLD,12,2)
        ctext(d,(1005,245),"LCM  (buses meet again)",F(22),GOLD)
        ctext(d,(1005,290),"gcd × lcm = a × b",F(28,True,True),WHITE)
        ctext(d,(1005,335),"lcm = 48·18 / 6 = 144",F(26,True,True),GRN)
    banner(d,ts[6],t,"TWIST #2 — one GCD gives the LCM for free",PUR,115)
PR=[2,3,5,7]
def d_m3(d,t,sc):
    ts=sc.ts;ctext(d,(330,170),"sieve of Eratosthenes (1 to 50)",F(26),WHITE)
    pr=[n for n in range(2,51) if all(n%p for p in range(2,int(n**.5)+1))]
    start=ts[3]+0.5;k=int(clamp((t-start)/2.2,0,4)) if t>=start else 0;cut=set()
    for p in PR[:k]:cut|={m for m in range(2*p,51,p)}
    for n in range(1,51):
        r,c=(n-1)//10,(n-1)%10;x=70+c*58;y=215+r*58
        col=(50,56,90);tc=WHITE
        if n==1:col=(35,40,60);tc=(110,120,150)
        elif n in cut:col=(40,30,40);tc=(120,80,90)
        elif k>=4 and n in pr:col=GRN;tc=(10,20,20)
        rbox(d,(x,y,x+50,y+50),col,None,6);ctext(d,(x+25,y+25),str(n),F(20),tc)
    if t>=ts[1]:ctext(d,(330,520),"is n prime?  test divisors only up to √n",F(22),TEAL)
    if t>=ts[4]:
        ctext(d,(930,230),"modular arithmetic = a clock",F(22),GOLD)
        ctext(d,(930,275),"(7·8) mod 5  =  1",F(26,True,True),WHITE);ctext(d,(930,315),"((7 mod 5)·(8 mod 5)) mod 5 = 1",F(18,True,True),(170,180,215))
    if t>=ts[5]:
        ctext(d,(930,385),"fast power: 3^13",F(22),GOLD)
        ctext(d,(930,425),"13 → 6 → 3 → 1 → 0",F(26,True,True),TEAL);ctext(d,(930,465),"3^13 = 1,594,323  in ~log₂13 steps",F(18),WHITE)
    banner(d,ts[6],t,"TWIST #3 — cross out multiples, primes remain",GRN,115)
import math as _m
def d_m4(d,t,sc):
    ts=sc.ts
    L=[("5 choose 2 = 10   (order ignored)",1,TEAL),("5 × 4 = 20   (order matters)",1,GRN),("P(sum of two dice = 7) = 6/36 = 1/6",2,PUR),("E[die] = 3.5 ,   E[X+Y] = E[X]+E[Y]",2,GOLD)]
    for j,(tx,k,c) in enumerate(L):
        if t>=ts[k]+j%2*1.6:ctext(d,(70,200+j*40),tx,F(22,True,True),c,"lm")
    if t>=ts[4]:
        ctext(d,(W//2+170,170),"1000 people tested",F(24),WHITE)
        cols,rows=40,25;sz=13
        for i in range(1000):
            r,c=i//cols,i%cols;x=690-120+c*sz;y=190+r*sz
            sick=i<10;flag_h=(10<=i<99);pos=sick and i<9
            col=(60,68,100)
            if t>=ts[4]+1:
                if sick:col=RED
                if i<9 and t>=ts[4]+2:col=(255,120,40)
                if flag_h and t>=ts[4]+3:col=GOLD
            d.rectangle((x,y,x+sz-4,y+sz-4),fill=col)
        if t>=ts[4]+1:ctext(d,(70,340),"red = sick (10)   gold = healthy but flagged (≈89)",F(18),(210,220,250),"lm")
    if t>=ts[5]:
        rbox(d,(60,380,590,500),(20,24,50),GOLD,12,2)
        ctext(d,(325,408),"P(sick | positive)",F(22),GOLD);ctext(d,(325,448),"= 9 / (9 + 89) ≈ 9.2 %",F(30,True,True),WHITE)
        ctext(d,(325,482),"Bayes: posterior = likelihood × prior / evidence",F(16),(170,180,215))
    banner(d,ts[6],t,"TWIST #4 — a positive test can still mean healthy",RED,115)
def bday(n):
    r=1.0
    for i in range(n):r*=(365-i)/365
    return 1-r
def d_m5(d,t,sc):
    ts=sc.ts
    x0,y0,wd,ht=620,200,560,300
    d.line([(x0,y0),(x0,y0+ht),(x0+wd,y0+ht)],fill=(150,160,200),width=2)
    ctext(d,(x0+wd/2,y0-26),"birthday paradox: P(two people share a birthday)",F(20),WHITE)
    a=ease((t-ts[3])/3) if t>=ts[3] else 0
    pts=[(x0+n/60*wd,y0+ht-bday(n)*ht) for n in range(0,61)]
    m=int(len(pts)*a)
    if m>1:d.line(pts[:m],fill=TEAL,width=4)
    for fr,lab in ((0.5,"50%"),(1.0,"100%")):
        yy=y0+ht-fr*ht;d.line([(x0,yy),(x0+wd,yy)],fill=(70,80,110),width=1);ctext(d,(x0-10,yy),lab,F(14),(170,180,215),"rm")
    if a>=0.45:
        px,py=pts[23];d.ellipse((px-8,py-8,px+8,py+8),fill=GOLD);ctext(d,(px+14,py+18),"n = 23 → 50.7%",F(20),GOLD,"lm")
    ctext(d,(x0+wd/2,y0+ht+26),"people (n)",F(14),(170,180,215))
    items=[("Euclid GCD","a loop",1),("sieve","an array",1),("fast power","divide and conquer",1),("hash table","probability",1),("random pivot","expected n log n",4)]
    for j,(a_,b_,k) in enumerate(items):
        if t>=ts[k]+j*0.9 if k==1 else t>=ts[k]:
            rbox(d,(60,200+j*62,560,250+j*62),(20,26,56),[TEAL,GRN,PUR,GOLD,RED][j],10,2)
            ctext(d,(80,225+j*62),a_,F(22),WHITE,"lm");ctext(d,(540,225+j*62),b_,F(20,False),[TEAL,GRN,PUR,GOLD,RED][j],"rm")
    if t>=ts[3]+3.5:ctext(d,(x0+wd/2,540),"300 keys, 10,000 slots → collision 98.9%",F(22),RED)
    banner(d,ts[5],t,"TWIST #5 — collisions arrive early",GOLD,115)

def d_mb(d,t,sc):
    ts=sc.ts;ctext(d,(W//2,165),"45 in base 2",F(28),WHITE)
    bits=[0,0,1,0,1,1,0,1];wts=[128,64,32,16,8,4,2,1]
    for i,(b,w) in enumerate(zip(bits,wts)):
        x=250+i*98;lit=b and t>=ts[2]+0.6*i*0.4
        rbox(d,(x,200,x+88,262),TEAL if lit else (40,46,78),(150,160,200),8,2)
        ctext(d,(x+44,231),str(b) if t>=ts[2] else "",F(30,True,True),(10,20,30) if lit else (120,130,160))
        ctext(d,(x+44,282),str(w),F(16),(170,180,215))
    if t>=ts[2]+2.5:ctext(d,(W//2,312),"32 + 8 + 4 + 1 = 45",F(22),GOLD)
    if t>=ts[3]:
        ctext(d,(90,345),"n    n//2   n%2",F(18,True,True),(170,180,215),"lm")
        rows=[(45,22,1),(22,11,0),(11,5,1),(5,2,1),(2,1,0),(1,0,1)]
        for j,(a,b,c) in enumerate(rows):
            if t>=ts[3]+0.5+j*0.9:ctext(d,(90,375+j*27),f"{a:<4} {b:<5} {c}",F(20,True,True),[TEAL,GRN][j%2],"lm")
        if t>=ts[3]+6:ctext(d,(90,540-6),"read up: 101101",F(20,True,True),GOLD,"lm")
    if t>=ts[5]:
        ctext(d,(560,345),"group bits in fours",F(20),GOLD,"lm")
        ctext(d,(560,385),"1011  0111",F(30,True,True),WHITE,"lm");ctext(d,(560,428),"  B     7   = 183",F(26,True,True),TEAL,"lm")
        ctext(d,(560,470),"13 = 1101₂ = 15₈ = D₁₆",F(20,True,True),GRN,"lm")
    if t>=ts[6]:
        ctext(d,(900,345),"binary add:  1101 + 1 = 1110",F(18,True,True),PUR,"lm")
        ctext(d,(900,385),"two's complement of 5:",F(18),GOLD,"lm");ctext(d,(900,420),"00000101 → flip → 11111010",F(16,True,True),WHITE,"lm");ctext(d,(900,450),"+1 → 11111011  (= −5)",F(18,True,True),RED,"lm")
    banner(d,ts[7],t,"BONUS TWIST — 0.1 has no finite binary form",RED,115)
SCENES=[("title",d_title,""),("m1",d_m1,"Basement · Arithmetic"),("mb",d_mb,"Basement · Number Bases"),("m2",d_m2,"Basement · GCD, HCF, LCM"),("m3",d_m3,"Basement · Primes and Modular Arithmetic"),("m4",d_m4,"Basement · Counting and Probability"),("m5",d_m5,"Basement · Math inside DSA"),("s1",d_s1,"Chapter 1 · Linear Search"),("s2",d_s2,"Chapter 2 · Binary Search"),("s3",d_s3,"Chapter 3 · Merge Sort"),("s4",d_s4,"Chapter 4 · Hashing"),("s5",d_s5,"Chapter 5 · Python Memory"),("s6",d_s6,"Chapter 6 · Graphs: BFS and DFS"),("s7",d_s7,"Chapter 7 · Topological Sort"),("s8",d_s8,"Finale · Recursion and Memoisation"),("end",d_end,"")]
def render(key,out):
    sc=Sc(key);fn=[x for x in SCENES if x[0]==key][0]
    n=int(sc.dur*FPS)
    p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-vf","fade=t=in:st=0:d=0.4,fade=t=out:st=%.2f:d=0.4"%(sc.dur-0.4),"-c:v","libx264","-crf","20","-preset","veryfast","-pix_fmt","yuv420p",out],stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(frame(sc,i/FPS,fn[1],fn[2]).tobytes())
    p.stdin.close();p.wait();return p.returncode
if __name__=="__main__":
    if sys.argv[1]=="test":
        os.makedirs("tst",exist_ok=True)
        for key,fn_,ch in SCENES:
            sc=Sc(key)
            for fr in (0.35,0.62,0.92):
                frame(sc,sc.dur*fr,fn_,ch).save(f"tst/{key}_{int(fr*100)}.png")
    else:
        key=sys.argv[1];tmp=f"sc_{key}.tmp.mp4";rc=render(key,tmp)
        if rc==0:os.rename(tmp,f"sc_{key}.mp4")
