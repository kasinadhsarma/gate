from viz import *
import codes
def card(d,box,col,lines,fs=19,gap=34,mono=True):
    rbox(d,box,(20,24,50),col,12,2)
    for j,(l,c) in enumerate(lines):ctext(d,(box[0]+18,box[1]+26+j*gap),l,F(fs,True,mono),c,"lm")
def table(d,x,y,head,rows,cw=90,rh=30,col=TEAL,hl=None,fs=17):
    n=len(head);rbox(d,(x,y,x+cw*n,y+rh*(len(rows)+1)),(20,24,50),col,8,2)
    d.rectangle((x+2,y+2,x+cw*n-2,y+rh),fill=tuple(int(c*0.45) for c in col))
    for j,h in enumerate(head):ctext(d,(x+j*cw+cw/2,y+rh/2),h,F(fs,True),WHITE)
    for i,r in enumerate(rows):
        if hl and i in hl:d.rectangle((x+2,y+rh*(i+1)+1,x+cw*n-2,y+rh*(i+2)-1),fill=(70,60,20))
        for j,v in enumerate(r):ctext(d,(x+j*cw+cw/2,y+rh*(i+1)+rh/2),str(v),F(fs,False,True),WHITE)
def d_title(d,t,sc):
    for i in range(14):
        x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
    ctext(d,(W//2,240),"OPERATION  GATE",F(84),GOLD);ctext(d,(W//2,340),"The Vault of Tables",F(50))
    if t>1.6:ctext(d,(W//2,420),"DBMS & Data Warehousing · seven vaults · seven twists",F(26,False),(170,180,215))
    if t>3:ctext(d,(W//2,490),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
def d_er(d,t,sc):
    ts=sc.ts
    if t>=ts[2]:
        for x,y,w,nm,c in((60,200,200,"STUDENT",TEAL),(520,200,200,"COURSE",GRN)):rbox(d,(x,y,x+w,y+60),(20,24,50),c,6,3);ctext(d,(x+w/2,y+30),nm,F(24),c)
        ctext(d,(160,285),"(sid) name, dept",F(16,False),(190,200,230));ctext(d,(620,285),"(cid) title, credits",F(16,False),(190,200,230))
    if t>=ts[3]:
        pts=[(340,230),(400,200),(460,230),(400,260)];d.polygon(pts,outline=GOLD,fill=(40,34,10));d.line([(400,200),(400,260)],fill=GOLD,width=0)
        ctext(d,(400,230),"enrols",F(15),GOLD);d.line([(260,230),(340,230)],fill=WHITE,width=2);d.line([(460,230),(520,230)],fill=WHITE,width=2)
        ctext(d,(295,215),"M",F(18),GOLD);ctext(d,(490,215),"N",F(18),GOLD)
        for i,(a,b) in enumerate([("1 : 1","passport"),("1 : N","dept → emp"),("M : N","student ↔ course")]):
            rbox(d,(790+i*0,190+i*55,1230,235+i*55),(20,24,50),TEAL,8,2);ctext(d,(810,212+i*55),a,F(20,True,True),GOLD,"lm");ctext(d,(930,212+i*55),b,F(18),WHITE,"lm")
    if t>=ts[5]:
        table(d,60,360,["sid","name"],[(1,"Asha"),(2,"Ben")],110,30,TEAL);table(d,330,360,["sid","cid","grade"],[(1,"C1","A"),(1,"C2","B"),(2,"C1","B")],85,30,GOLD);table(d,640,360,["cid","title"],[("C1","DBMS"),("C2","ML")],110,30,GRN)
        ctext(d,(500,345),"Enrolment (the new table)",F(16),GOLD)
    if t>=ts[6]:
        for i,(a,c) in enumerate([("superkey",GRY),("candidate key",TEAL),("primary key",GOLD),("foreign key",RED)]):
            rbox(d,(900+(i%2)*170,400+(i//2)*50,1060+(i%2)*170,442+(i//2)*50),(20,24,50),c if c!=GRY else (120,130,170),8,2);ctext(d,(980+(i%2)*170,421+(i//2)*50),a,F(16),WHITE)
    banner(d,ts[7],t,"TWIST #1 — many-to-many needs a third table",GOLD,115)
def d_sql(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DB1),(7,codes.DB2)],30,150,690,17,22)
    if t>=ts[3]:
        table(d,760,165,["name","dept","sal"],[("Asha","CS",50),("Ben","CS",70),("Cara","EE",60),("Dev","EE","NULL"),("Esh","ME",40)],110,30,TEAL,hl=[3] if t>=ts[5] else None)
    if t>=ts[5]:
        ctext(d,(925,385),"group → having count(*) > 1",F(17),GOLD);table(d,760,400,["dept","n","n_sal","avg"],[("CS",2,2,60.0),("EE",2,1,60.0)],82,28,GOLD,fs=16)
    if t>=ts[6] and t<ts[7]:
        for i,(a,c) in enumerate([("INNER: matches only",TEAL),("LEFT: all left + NULL",GRN),("subquery: query in query",PUR)]):rbox(d,(760,490+i*0,1240,530),(20,24,50),c,8,2) if False else None
    banner(d,ts[8],t,"TWIST #2 — NULL is unknown: use IS NULL; WHERE ≠ HAVING",GOLD,115)
def d_ic(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DB3)],30,150,690,17,22)
    if t>=ts[2]:
        for i,(a,b,c) in enumerate([("NOT NULL","value must exist",TEAL),("UNIQUE","no duplicates",GRN),("PRIMARY KEY","unique + not null",GOLD),("CHECK","condition holds",PUR),("FOREIGN KEY","must match a parent",RED)]):
            y=170+i*50;rbox(d,(770,y,1240,y+42),(20,24,50),c,8,2);ctext(d,(785,y+21),a,F(18,True,True),c,"lm");ctext(d,(960,y+21),b,F(16,False),WHITE,"lm")
    if t>=ts[6]:
        for i,(a,b) in enumerate([("RESTRICT","block the delete"),("SET NULL","blank the child"),("CASCADE","delete children too")]):
            rbox(d,(770+i*160,440,925+i*160,490),(20,24,50),GOLD,8,2);ctext(d,(847+i*160,458),a,F(15),GOLD);ctext(d,(847+i*160,478),b,F(12,False),WHITE)
    banner(d,ts[7],t,"TWIST #3 — UNIQUE may hold many NULLs; a primary key never",GOLD,115)
def d_norm(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DB4),(7,codes.DB5)],30,150,690,17,22)
    if k==0:
        for j,(l,c) in enumerate([("A → B",TEAL),("B → C",GRN),("CD → E",PUR)]):ctext(d,(790,185+j*38),l,F(24,True,True),c,"lm")
        if t>=ts[3]+2:ctext(d,(790,320),"A⁺ = {A, B, C}",F(24,True,True),GOLD,"lm")
        if t>=ts[4]:ctext(d,(790,365),"(AD)⁺ = {A,B,C,D,E}  → key",F(22,True,True),GOLD,"lm")
        if t>=ts[6]:
            for i,(a,c) in enumerate([("1NF atomic",TEAL),("2NF no partial",GRN),("3NF no transitive",PUR),("BCNF det = superkey",GOLD)]):rbox(d,(790,415+i*0,1230,415),(0,0,0),c,0,0) if False else ctext(d,(790+ (i%2)*230,430+(i//2)*40),a,F(16),c,"lm")
    if k==1:
        ctext(d,(790,185),"R(A,B,C): AB → C , C → B",F(21,True,True),WHITE,"lm");ctext(d,(790,235),"keys: AB and AC",F(24,True,True),GOLD,"lm")
        card(d,(780,285,1240,400),RED,[("C → B : C not a superkey",RED),("→ violates BCNF",RED),("B is prime → passes 3NF",GRN)],18,36)
    banner(d,ts[8],t,"TWIST #4 — 3NF is looser than BCNF",GOLD,115)
def d_idx(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DB6)],30,150,690,17,22)
    if t>=ts[2]:
        for i,(a,b,c) in enumerate([("full scan","n",RED),("binary search","log₂ n",GOLD),("B+ tree","log₁₀₀ n",GRN)]):
            y=170+i*60;rbox(d,(770,y,1240,y+50),(20,24,50),c,8,2);ctext(d,(790,y+25),a,F(18),WHITE,"lm");ctext(d,(1220,y+25),b,F(22,True,True),c,"rm")
    if t>=ts[4]:
        ctext(d,(1005,375),"B+ tree, fan-out 100, 1M rows",F(17),WHITE)
        rbox(d,(960,390,1050,420),(20,24,50),GOLD,6,2);ctext(d,(1005,405),"root",F(14),GOLD)
        for i in range(3):
            x=840+i*165;d.line([(1005,420),(x+45,450)],fill=GRY,width=2);rbox(d,(x,450,x+90,480),(20,24,50),TEAL,6,2);ctext(d,(x+45,465),"node",F(14),TEAL)
        ctext(d,(1005,505),"height 3 → 3 disk reads (not 1,000,000)",F(16),GRN)
    banner(d,ts[8],t,"TWIST #5 — low-cardinality or LIKE '%son' defeats an index",GOLD,115)
def d_pre(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DB7)],30,150,690,17,22)
    data=[10,20,30,40,100]
    if t>=ts[3]:
        ax=Ax(770,190,470,150,(0,6),(0,1.1))
        ctext(d,(1005,170),"min-max scaled",F(18),TEAL)
        for i,v in enumerate(data):
            h=150*(v-10)/90*ease((t-ts[3])/1.5);d.rectangle((790+i*90,340-h,850+i*90,340),fill=GOLD if i==4 else TEAL);ctext(d,(820+i*90,355),str(v),F(15),WHITE)
        ctext(d,(1005,385),"outlier 100 squeezes the rest to the bottom",F(16),RED)
    if t>=ts[6]:
        for i,(a,b) in enumerate([("equal width","same range"),("equal depth","same count"),("smoothing","bin mean")]):
            rbox(d,(770+i*160,420,925+i*160,480),(20,24,50),PUR,8,2);ctext(d,(847+i*160,440),a,F(16),PUR);ctext(d,(847+i*160,464),b,F(13,False),WHITE)
    banner(d,ts[7],t,"TWIST #6 — one outlier ruins min-max scaling",GOLD,115)
def d_dw(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(6,codes.DB8)],30,150,690,17,22) if t>=ts[6] else None
    if t>=ts[3] and t<ts[6]:
        cx,cy=340,340
        rbox(d,(cx-90,cy-45,cx+90,cy+45),(20,24,50),GOLD,10,3);ctext(d,(cx,cy-12),"FACT sales",F(22),GOLD);ctext(d,(cx,cy+16),"amount, qty",F(16,False),WHITE)
        for i,(nm,x,y) in enumerate([("time",cx,cy-125),("product",cx-210,cy),("store",cx+210,cy),("customer",cx,cy+125)]):
            c=[TEAL,GRN,PUR,RED][i];rbox(d,(x-65,y-26,x+65,y+26),(20,24,50),c,8,2);ctext(d,(x,y),nm,F(20),c)
        for a,b in(((340,295),(340,241)),((250,340),(210+0,340)),((430,340),(470,340)),((340,385),(340,439))):d.line([a,b],fill=GRY,width=3)
    if t>=ts[5]:
        for i,(a,b) in enumerate([("roll-up","day → month"),("drill-down","month → day"),("slice","fix 1 dimension"),("dice","pick a sub-cube"),("pivot","rotate the view")]):
            rbox(d,(780,170+i*52,1240,214+i*52),(20,24,50),TEAL,8,2);ctext(d,(795,192+i*52),a,F(18,True),TEAL,"lm");ctext(d,(970,192+i*52),b,F(16,False),WHITE,"lm")
    if t>=ts[6]:ctext(d,(1000,470),"2ⁿ aggregates  (n = 3 → 8)",F(24,True,True),GOLD)
    banner(d,ts[7],t,"TWIST #7 — each extra dimension doubles the cube",GOLD,115)
def d_dsa(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DB9)],30,150,690,17,22)
    if t>=ts[2]:
        ctext(d,(1000,175),"comparisons (|R|=1000, |S|=100)",F(18),WHITE)
        a=ease((t-ts[3])/2)
        d.rectangle((770,215,770+int(440*a),270),fill=RED);ctext(d,(780,242),"nested loops: n·m = 100 000",F(19),WHITE,"lm")
        d.rectangle((770,300,770+max(3,int(440*0.011*a)),355),fill=GRN);ctext(d,(1000,385),"hash join: n + m = 1 100",F(20,True),GRN)
    banner(d,ts[7],t,"DSA TWIST — one hash table powers joins, indexes, dedup",GOLD,115)
def d_wk(d,t,sc):
    walk(d,sc,t,[(codes.WD1,1,4),(codes.WD2,5,8)])
def d_end(d,t,sc):
    ctext(d,(W//2,230),"The Vault of Tables — open",F(52),GOLD)
    for i,x in enumerate(["ER model","SQL","constraints","normal forms","indexing","preprocessing","warehouse"]):
        if t>1+i*.4:
            cx=210+(i%4)*270;cy=320+(i//4)*60;rbox(d,(cx-110,cy-22,cx+110,cy+22),(20,24,50),[TEAL,GRN,PUR,GOLD][i%4],10,2);ctext(d,(cx,cy),x,F(19),[TEAL,GRN,PUR,GOLD][i%4])
    if t>6:ctext(d,(W//2,470),"next film: Machine Learning",F(30),WHITE)
SCENES=[("title",d_title,""),("er",d_er,"Vault 1 · ER and relational models"),("sql",d_sql,"Vault 2 · SQL"),("ic",d_ic,"Vault 3 · Integrity constraints"),("norm",d_norm,"Vault 4 · Normalization"),("idx",d_idx,"Vault 5 · Indexing"),("pre",d_pre,"Vault 6 · Data preprocessing"),("dw",d_dw,"Vault 7 · Data warehouse modelling"),("dsa",d_dsa,"Lab · Complexity of joins (DSA)"),("wk",d_wk,"Walkthrough · how the code thinks"),("end",d_end,"")]
