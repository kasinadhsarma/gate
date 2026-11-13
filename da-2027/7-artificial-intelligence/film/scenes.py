from viz import *
import codes
def bx(d,x,y,w,h,col,txt,fs=18):
    rbox(d,(x,y,x+w,y+h),(20,24,50),col,10,2);ctext(d,(x+w//2,y+h//2),txt,F(fs,True),col)
def d_title(d,t,sc):
    for i in range(14):
        x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
    ctext(d,(W//2,240),"OPERATION  GATE",F(84),GOLD);ctext(d,(W//2,340),"The Thinking Machine",F(50))
    if t>1.6:ctext(d,(W//2,420),"Artificial Intelligence · search · logic · uncertainty",F(26,False),(170,180,215))
    if t>3:ctext(d,(W//2,490),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
def d_unin(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.A1)],30,150,690,16,20)
    P={"S":(830,300),"A":(980,220),"B":(980,380),"G":(1130,300)}
    if t>=ts[3]:
        for a,b,c in(("S","A",1),("A","G",6),("S","B",4),("B","G",1)):
            d.line([P[a],P[b]],fill=GRY,width=3);ctext(d,((P[a][0]+P[b][0])//2,(P[a][1]+P[b][1])//2-14),str(c),F(16,True),WHITE)
        for n,(x,y) in P.items():
            d.ellipse((x-22,y-22,x+22,y+22),fill=(20,24,50),outline=TEAL,width=3);ctext(d,(x,y),n,F(20,True),TEAL)
    if t>=ts[4]:
        ctext(d,(980,170),"BFS: S-A-G cost 7",F(17),RED);ctext(d,(980,450),"UCS: S-B-G cost 5",F(17),GRN)
    banner(d,ts[5],t,"TWIST #1 — nodes grow like b^d",GOLD,115)
MZ=["....#..",".##.#..","...#...",".#...#.","...#..."]
def d_inf(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.A2),(4,codes.A2B)],30,150,690,15,19)
    if t>=ts[3]:
        for r,row in enumerate(MZ):
            for c,ch in enumerate(row):
                x=800+c*50;y=190+r*50;d.rectangle((x,y,x+44,y+44),fill=(70,80,130) if ch=="#" else (24,30,60),outline=GRY)
        ctext(d,(825,215),"S",F(20,True),GOLD);ctext(d,(1075,415),"G",F(20,True),GRN)
        ctext(d,(1000,462),"UCS 23 nodes · A* 19 nodes",F(16),WHITE)
    if t>=ts[4]:ctext(d,(1000,495),"h admissible → 4    h too big → 6",F(16),RED)
    banner(d,ts[5],t,"TWIST #2 — overestimating h hides the best path",GOLD,115)
def d_adv(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.A3)],30,150,690,15,19)
    leaves=[3,5,6,9,1,2,0,-1]
    if t>=ts[2]:
        pos={}
        for i,v in enumerate(leaves):pos[(3,i)]=(800+i*58,430)
        for lv in(2,1,0):
            for i in range(2**lv):
                a=pos[(lv+1,2*i)];b=pos[(lv+1,2*i+1)];pos[(lv,i)]=((a[0]+b[0])//2,430-(3-lv)*80)
        for (lv,i),p in pos.items():
            if lv<3:
                for k2 in(0,1):d.line([p,pos[(lv+1,2*i+k2)]],fill=GRY,width=2)
        for (lv,i),p in pos.items():
            if lv==3:
                dead=i in(5,6,7) and t>=ts[4];col=(90,90,100) if dead else TEAL
                d.rectangle((p[0]-20,p[1]-16,p[0]+20,p[1]+16),outline=col,width=2);ctext(d,p,str(leaves[i]),F(16,True),col)
            else:
                col=GOLD if lv%2==0 else PUR;d.ellipse((p[0]-16,p[1]-16,p[0]+16,p[1]+16),outline=col,width=2);ctext(d,p,"MAX" if lv%2==0 else "min",F(11,True),col)
        ctext(d,(1000,176),"root = 5   leaves seen: 8 vs 5",F(16),WHITE)
    banner(d,ts[5],t,"TWIST #3 — pruning keeps the answer, saves the work",GOLD,115)
def d_prop(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.A4)],30,150,690,17,22)
    if t>=ts[2]:
        ctext(d,(1000,185),"P   Q   P→Q   KB(P→Q ∧ P)",F(17,True,True),WHITE)
        for i,(p,q) in enumerate([(0,0),(0,1),(1,0),(1,1)]):
            imp=(not p) or q;kb=imp and p
            ctext(d,(1000,225+i*40),f"{p}   {q}    {int(imp)}         {int(kb)}",F(18,True,True),GRN if kb else GRY)
        if t>=ts[3]:ctext(d,(1000,415),"only model with KB true: Q = 1 → entailed",F(16),GOLD)
    if t>=ts[4]:ctext(d,(1000,455),"false premise → implication true",F(16),RED)
    banner(d,ts[5],t,"TWIST #4 — checking 2^n models; resolution is practical",GOLD,115)
def d_pred(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.A5)],30,150,690,17,22)
    P={"ann":(900,260),"bob":(1100,260),"cy":(1000,420)}
    if t>=ts[2]:
        for a,b in(("ann","bob"),("bob","cy"),("cy","ann")):
            (x1,y1),(x2,y2)=P[a],P[b];d.line([(x1,y1),(x2,y2)],fill=GOLD,width=3)
        for n,(x,y) in P.items():d.ellipse((x-34,y-24,x+34,y+24),fill=(20,24,50),outline=TEAL,width=3);ctext(d,(x,y),n,F(18,True),TEAL)
        ctext(d,(1000,200),"loves(ann,bob) · loves(bob,cy) · loves(cy,ann)",F(15),WHITE)
    if t>=ts[3]:
        ctext(d,(1000,480),"∀x ∃y loves(x,y) = True",F(18,True),GRN);ctext(d,(1000,510),"∃y ∀x loves(x,y) = False",F(18,True),RED)
    banner(d,ts[5],t,"TWIST #5 — quantifier order changes the meaning",GOLD,115)
def d_unc(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(4,codes.A6)],30,150,690,15,19)
    P={"Burglary":(840,230),"Earthquake":(1080,230),"Alarm":(960,330),"John":(860,430),"Mary":(1080,430)}
    if t>=ts[2]:
        for a,b in(("Burglary","Alarm"),("Earthquake","Alarm"),("Alarm","John"),("Alarm","Mary")):d.line([P[a],P[b]],fill=GRY,width=3)
        for n,(x,y) in P.items():
            c=GRN if n in("John","Mary") and t>=ts[3] else TEAL
            d.ellipse((x-52,y-24,x+52,y+24),fill=(20,24,50),outline=c,width=3);ctext(d,(x,y),n,F(16,True),c)
        ctext(d,(840,190),"P=.001",F(14),WHITE);ctext(d,(1080,190),"P=.002",F(14),WHITE)
    if t>=ts[4]:ctext(d,(1000,495),"P(B | J,M) = 0.284 exact · ≈0.28 sampled",F(17,True),GOLD)
    banner(d,ts[6],t,"TWIST #6 — rare cause: only 28% even after two calls",GOLD,115)
def d_wk(d,t,sc):walk(d,sc,t,[(codes.WA1,1,3)])
def d_end(d,t,sc):
    ctext(d,(W//2,230),"The Thinking Machine — awake",F(52),GOLD)
    for i,x in enumerate(["uninformed search","A* & heuristics","minimax / alpha-beta","propositional logic","predicate logic","Bayesian networks","sampling"]):
        if t>1+i*.4:
            cx=210+(i%4)*270;cy=320+(i//4)*60;rbox(d,(cx-125,cy-22,cx+125,cy+22),(20,24,50),[TEAL,GRN,PUR,GOLD][i%4],10,2);ctext(d,(cx,cy),x,F(17),[TEAL,GRN,PUR,GOLD][i%4])
    if t>6:ctext(d,(W//2,470),"Operation Gate · all seven films complete",F(30),WHITE)
SCENES=[("title",d_title,""),("unin",d_unin,"Room 1 · Uninformed search"),("inf",d_inf,"Room 2 · Informed search"),("adv",d_adv,"Room 3 · Adversarial search"),("prop",d_prop,"Room 4 · Propositional logic"),("pred",d_pred,"Room 5 · Predicate logic"),("unc",d_unc,"Room 6 · Reasoning under uncertainty"),("wk",d_wk,"Walkthrough · alpha-beta pruning"),("end",d_end,"")]
