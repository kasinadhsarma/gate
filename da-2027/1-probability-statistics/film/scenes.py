from viz import *
import codes, random
from math import comb, exp, factorial, sqrt, pi
def hist(d,x0,y0,w,h,vals,col,maxv=None,labels=None,lab_every=1):
    n=len(vals);mv=maxv or max(vals);bw=w/n
    for i,v in enumerate(vals):
        hh=h*v/mv;d.rectangle((x0+i*bw+2,y0+h-hh,x0+(i+1)*bw-2,y0+h),fill=col)
        if labels and i%lab_every==0:ctext(d,(x0+i*bw+bw/2,y0+h+12),str(labels[i]),F(13),(170,180,215))
def card(d,box,col,lines,fs=19,gap=34,mono=True):
    rbox(d,box,(20,24,50),col,12,2)
    for j,(l,c) in enumerate(lines):ctext(d,(box[0]+18,box[1]+26+j*gap),l,F(fs,True,mono),c,"lm")
def d_title(d,t,sc):
    for i in range(14):
        x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
    ctext(d,(W//2,240),"OPERATION  GATE",F(84),GOLD);ctext(d,(W//2,340),"The Casino of Chance",F(50))
    if t>1.6:ctext(d,(W//2,420),"Probability & Statistics · nine tables · nine twists",F(26,False),(170,180,215))
    if t>3:ctext(d,(W//2,490),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
def d_cnt(d,t,sc):
    ts=sc.ts
    if t>=ts[3]:
        card(d,(40,160,420,300),TEAL,[("C(5,2) = 10",WHITE),("C(10,2) = 45 handshakes",WHITE),("order matters → P(n,k)",GOLD)])
    if t>=ts[5]:
        word="MISSISSIPPI";col={"M":GOLD,"I":TEAL,"S":RED,"P":PUR}
        for i,c in enumerate(word):
            x=40+i*37;rbox(d,(x,330,x+33,375),tuple(int(v*0.5) for v in col[c]),col[c],6,2);ctext(d,(x+16,352),c,F(22),WHITE)
        ctext(d,(40,405),"11! / (4!·4!·2!) = 34650",F(24,True,True),GOLD,"lm");ctext(d,(40,440),"(M×1, I×4, S×4, P×2)",F(16,False),(170,180,215),"lm")
    if t>=ts[6]:
        card(d,(40,470,420,530),GRN,[("10 sweets, 3 kids: C(12,2) = 66",GRN)],17)
    if t>=ts[7]:
        ax=Ax(500,190,700,300,(0,60),(0,1));ax.axes(d,range(0,61,10),(0,.25,.5,.75,1),labels=True)
        def pb(n):
            p=1
            for i in range(n):p*=(365-i)/365
            return 1-p
        ax.curve(d,lambda x:pb(int(x)),GOLD,5,n=60);ax.dot(d,23,pb(23),RED,9);ctext(d,(ax.px(23)+110,ax.py(pb(23))+20),"23 people → 50.7%",F(20),RED)
        ctext(d,(850,170),"shared birthday vs group size",F(20),WHITE)
    banner(d,ts[7],t,"TWIST #1 — 23 people, already a 50.7% shared birthday",GOLD,115)
def d_ax(d,t,sc):
    ts=sc.ts
    card(d,(40,160,420,280),TEAL,[("P(A) ≥ 0",WHITE),("P(Ω) = 1",WHITE),("disjoint: P(A∪B)=P(A)+P(B)",GOLD)],17)
    if t>=ts[3]:
        d.ellipse((470,170,640,340),outline=TEAL,width=4);d.ellipse((560,170,730,340),outline=GOLD,width=4);ctext(d,(520,255),"A",F(26),TEAL);ctext(d,(680,255),"B",F(26),GOLD);ctext(d,(600,255),"A∩B",F(16),RED)
        ctext(d,(600,365),"P(A∪B)=P(A)+P(B)-P(A∩B)",F(18,True,True),WHITE)
    if t>=ts[5]:
        for a in range(6):
            for b in range(6):
                x=790+b*34;y=170+a*34;hit=a+b==5;rbox(d,(x,y,x+31,y+31),(120,90,20) if hit else (30,36,70),GOLD if hit else None,4,2)
        ctext(d,(895,390),"sum = 7 : 6 of 36 = 1/6",F(20,True,True),GOLD)
    if t>=ts[6]:
        card(d,(40,400,700,490),GRN,[("P(no six, 4 rolls) = (5/6)⁴ = 0.4823",WHITE),("P(at least one six) = 1 - 0.4823 = 0.5177",GRN)],19)
    banner(d,ts[7],t,"TWIST #2 — disjoint events are the most dependent of all",GOLD,115)
def d_bay(d,t,sc):
    ts=sc.ts
    if t>=ts[2]:
        card(d,(40,160,520,230),TEAL,[("P(A|B) = P(A∩B) / P(B)",WHITE)],22)
    if t>=ts[3]:
        card(d,(40,245,520,315),PUR,[("P(A|B) = P(B|A)·P(A) / P(B)",WHITE)],22)
    if t>=ts[8]:
        ctext(d,(900,170),"10 000 people",F(22),WHITE)
        a=ease((t-ts[8])/2)
        d.rectangle((600,200,600+int(600*0.01*a)+3,260),fill=RED);ctext(d,(620,290),"100 sick → 99 flagged",F(18),RED,"lm")
        d.rectangle((600,330,1200,380),outline=GRY,width=2);d.rectangle((600,330,600+int(600*0.0495*a),380),fill=GOLD);ctext(d,(620,410),"9 900 healthy → 495 flagged",F(18),GOLD,"lm")
        d.rectangle((600,200,1200,260),outline=GRY,width=2)
        ctext(d,(900,470),"99 / (99+495) = 1/6 ≈ 16.7%",F(30,True,True),GRN)
    elif t>=ts[6]:
        card(d,(560,170,1240,330),GOLD,[("prevalence 1%",WHITE),("sensitivity 99%",WHITE),("false positive 5%",WHITE),("P(sick | +) = 0.0099/(0.0099+0.0495)",GRN)],18)
    banner(d,ts[9],t,"TWIST #3 — the base rate beats the test accuracy",GOLD,115)
def d_rv(d,t,sc):
    ts=sc.ts
    if t>=ts[2]:card(d,(40,160,400,290),TEAL,[("fair die: E = 3.5",WHITE),("Var = 35/12 = 2.917",WHITE),("E = long-run average",GOLD)],18)
    if t>=ts[3]:
        v=[comb(10,k)/1024 for k in range(11)];hist(d,40,330,380,150,v,TEAL,maxv=.3,labels=range(11));ctext(d,(230,320),"Binomial(10, ½): P(5)=0.246",F(16),TEAL)
    if t>=ts[4]:
        v=[exp(-3)*3**k/factorial(k) for k in range(10)];hist(d,450,330,380,150,v,GRN,maxv=.3,labels=range(10));ctext(d,(640,320),"Poisson(3): P(0)=0.0498",F(16),GRN)
    if t>=ts[6]:
        ax=Ax(870,190,370,250,(-3.5,3.5),(0,.45));pdf=lambda x:exp(-x*x/2)/sqrt(2*pi)
        for lim,c in((1.96,(60,90,60)),(1,(90,120,60))):
            xs=[-lim+2*lim*i/40 for i in range(41)];d.polygon([ax.P(x,pdf(x)) for x in xs]+[ax.P(lim,0),ax.P(-lim,0)],fill=c)
        ax.curve(d,pdf,GOLD,4);ax.axes(d,(-2,0,2),(),labels=True,grid=False);ctext(d,(1055,170),"68% · 95% (±1.96) · 99.7%",F(17),GOLD)
    banner(d,ts[7],t,"TWIST #4 — the exponential never remembers the past",GOLD,115)
def means(seed,n):
    r=random.Random(seed);return [sum(r.randint(1,6) for _ in range(30))/30 for _ in range(n)]
def d_clt(d,t,sc):
    ts=sc.ts
    if t>=ts[3]:
        hist(d,40,200,260,200,[1]*6,TEAL,maxv=1.3,labels=range(1,7));ctext(d,(170,175),"one die: flat",F(20),TEAL)
        m=means(11,3000);bins=[0]*20
        for x in m:bins[min(19,max(0,int((x-2.5)/2*20)))]+=1
        hist(d,380,200,560,200,bins,GOLD,maxv=max(bins)*1.05);ctext(d,(660,175),"mean of 30 dice, 3000 times: bell",F(20),GOLD)
        for k in range(0,20,5):ctext(d,(380+k*28+14,420),f"{2.5+k*0.1:.1f}",F(13),(170,180,215))
    if t>=ts[3]+2:card(d,(960,200,1250,330),GRN,[("μ = 3.5",WHITE),("σ/√n = 1.708/√30",WHITE),("     = 0.312",GOLD)],17)
    if t>=ts[5]:ctext(d,(640,490),"4× the data  →  ½ the noise  (SE = σ/√n)",F(24,True,True),WHITE)
    banner(d,ts[6],t,"TWIST #5 — even a coin flip becomes a bell",GOLD,115)
def d_ci(d,t,sc):
    ts=sc.ts;r=random.Random(7);ax=Ax(40,190,560,300,(40,60),(0,22))
    ax.axes(d,(),(),labels=False);d.line([ax.P(50,0),ax.P(50,22)],fill=GRN,width=3);ctext(d,(ax.px(50),175),"true mean 50",F(17),GRN)
    miss=0
    if t>=ts[2]:
        n=int(clamp((t-ts[2])/6)*20)
        for i in range(20):
            xb=sum(r.gauss(50,10) for _ in range(25))/25;lo,hi=xb-1.96*2,xb+1.96*2;bad=not(lo<=50<=hi)
            if i<n:
                if bad:miss+=1
                y=ax.py(i+1);d.line([(ax.px(lo),y),(ax.px(hi),y)],fill=RED if bad else TEAL,width=4);d.ellipse((ax.px(xb)-4,y-4,ax.px(xb)+4,y+4),fill=WHITE)
        ctext(d,(320,515),f"{n-miss} of {n} intervals catch the true mean",F(18),WHITE)
    if t>=ts[3]:card(d,(650,190,1250,300),TEAL,[("z: 52 ± 1.96·(10/√25)",WHITE),("= (48.08 , 55.92)",GOLD)],20)
    if t>=ts[5]:card(d,(650,320,1250,440),PUR,[("t(15)=2.131: 20 ± 2.131·(4/√16)",WHITE),("= (17.87 , 22.13)",GOLD),("heavier tails → wider",GRN)],19)
    banner(d,ts[6],t,"TWIST #6 — halve the width, pay 4× the data",GOLD,115)
def d_ht(d,t,sc):
    ts=sc.ts
    if t>=ts[3]:
        ax=Ax(40,190,380,200,(-4,4),(0,.45));pdf=lambda x:exp(-x*x/2)/sqrt(2*pi)
        for a,b in((-4,-1.96),(1.96,4)):
            xs=[a+(b-a)*i/20 for i in range(21)];d.polygon([ax.P(x,pdf(x)) for x in xs]+[ax.P(b,0),ax.P(a,0)],fill=(130,50,50))
        ax.curve(d,pdf,TEAL,4);ax.axes(d,(-2,0,2),(),labels=True,grid=False);ax.dot(d,2,pdf(2),GOLD,8);ctext(d,(230,175),"z = 2 → in the reject zone",F(17),GOLD)
        card(d,(450,190,830,290),TEAL,[("z = (105-100)/(15/6) = 2",WHITE),("p = 0.0455 < 0.05 → REJECT",RED)],18)
    if t>=ts[4]:card(d,(450,305,830,405),PUR,[("t = (54-50)/(6/3) = 2, df 8",WHITE),("p = 0.0805, crit 2.306 → KEEP",GRN)],18)
    if t>=ts[7]:card(d,(450,420,830,520),GOLD,[("χ² = 42/10 = 4.2, df 5",WHITE),("crit 11.07, p 0.52 → fair die",GRN)],18)
    if t>=ts[7]:
        for j,(l,p,c) in enumerate([("z",.0455,RED),("t",.0805,PUR),("χ²",.52,GOLD)]):
            y=210+j*70;d.rectangle((900,y,900+int(300*p/.55),y+36),fill=c);ctext(d,(890,y+18),l,F(20),WHITE,"rm");ctext(d,(900+int(300*p/.55)+8,y+18),f"{p}",F(16),WHITE,"lm")
        d.line([(900+int(300*.05/.55),195),(900+int(300*.05/.55),400)],fill=GRN,width=3);ctext(d,(990,175),"α = 0.05",F(16),GRN)
    banner(d,ts[9],t,"TWIST #7 — failing to reject ≠ proving true",GOLD,115)
def d_py(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(2,codes.P1),(5,codes.P2),(6,codes.P3)],30,150,680,17,22)
    if k==0:
        ctext(d,(970,180),"Monte Carlo vs formula",F(22),GOLD)
        d.rectangle((760,220,760+int(440*.507),270),fill=TEAL);ctext(d,(770,245),"formula 0.507",F(20),(10,10,30),"lm")
        a=ease((t-ts[3])/1.5) if t>=ts[3] else 0
        d.rectangle((760,300,760+int(440*.511*a),350),fill=GOLD);ctext(d,(770,325),"20 000 trials: 0.511",F(20),(10,10,30),"lm")
    if k==1:
        ctext(d,(970,175),"Pascal's triangle = nCk",F(22),GOLD)
        for i in range(7):
            for j in range(i+1):ctext(d,(970+(j-i/2)*56,225+i*40),str(comb(i,j)),F(22,True,True),[TEAL,GRN,PUR,GOLD][i%4])
    if k==2:
        m=means(1,5000);bins=[0]*20
        for x in m:bins[min(19,max(0,int((x-2.5)/2*20)))]+=1
        hist(d,730,230,490,230,bins,GOLD,maxv=max(bins)*1.05);ctext(d,(975,190),"5000 means of 30 dice",F(20),GOLD)
    banner(d,ts[7],t,"PYTHON TWIST — seed the random generator when testing",GOLD,115)
def d_dsa(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(2,codes.P4),(5,codes.P5)],30,150,680,17,22)
    if k==0:
        ctext(d,(970,175),"stream → keep k=3 slots",F(22),GOLD)
        for i in range(12):
            x=730+i*42;d.rectangle((x,230,x+36,266),outline=GRY,width=2);ctext(d,(x+18,248),str(i),F(14),(150,160,200))
        for j,c in enumerate([TEAL,GRN,PUR]):
            rbox(d,(800+j*120,340,900+j*120,390),(20,24,50),c,8,2);ctext(d,(850+j*120,365),f"slot {j}",F(18),c)
        ctext(d,(975,430),"replace with probability k/i",F(20),WHITE);ctext(d,(975,470),"O(n) time · O(k) memory",F(20,True,True),GOLD)
    if k==1:
        ctext(d,(970,175),"expected work per round",F(22),GOLD)
        w=480
        for i in range(6):
            v=w/(2**i);d.rectangle((730,215+i*45,730+int(v*ease((t-ts[5]-i*.4)/1)),215+i*45+32),fill=[TEAL,GRN,PUR,GOLD,RED,TEAL][i]);ctext(d,(1235,231+i*45),f"n/{2**i}",F(16),WHITE,"rm")
        ctext(d,(975,500),"n + n/2 + n/4 + … ≈ 2n  →  O(n)",F(22,True,True),GOLD)
    banner(d,ts[6],t,"DSA TWIST — random pivot makes the n² case vanishingly rare",GOLD,115)
def d_wk(d,t,sc):
    walk(d,sc,t,[(codes.W_P1,1,4),(codes.W_P2,5,8)])
def d_end(d,t,sc):
    ctext(d,(W//2,230),"The Casino of Chance — closed",F(52),GOLD)
    for i,x in enumerate(["counting","axioms","Bayes","distributions","CLT","intervals","tests","Python","DSA"]):
        if t>1+i*.35:
            cx=190+(i%5)*225;cy=320+(i//5)*60;rbox(d,(cx-95,cy-22,cx+95,cy+22),(20,24,50),[TEAL,GRN,PUR,GOLD][i%4],10,2);ctext(d,(cx,cy),x,F(19),[TEAL,GRN,PUR,GOLD][i%4])
    if t>6:ctext(d,(W//2,470),"all three films done — now solve the PYQs",F(30),WHITE)
SCENES=[("title",d_title,""),("cnt",d_cnt,"Table 1 · Counting"),("ax",d_ax,"Table 2 · Axioms"),("bay",d_bay,"Table 3 · Conditional and Bayes"),("rv",d_rv,"Table 4 · Random variables and distributions"),("clt",d_clt,"Table 5 · Central Limit Theorem"),("ci",d_ci,"Table 6 · Confidence intervals"),("ht",d_ht,"Table 7 · Hypothesis tests (z, t, χ²)"),("wk",d_wk,"Walkthrough · how the code thinks"),("py",d_py,"Lab 1 · Python for probability"),("dsa",d_dsa,"Lab 2 · Randomized algorithms (DSA)"),("end",d_end,"")]
