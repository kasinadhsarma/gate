from viz import *
import codes
def bx(d,x,y,w,h,col,txt,fs=18):
    rbox(d,(x,y,x+w,y+h),(20,24,50),col,10,2);ctext(d,(x+w//2,y+h//2),txt,F(fs,True),col)
def d_title(d,t,sc):
    for i in range(14):
        x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
    ctext(d,(W//2,240),"OPERATION  GATE",F(84),GOLD);ctext(d,(W//2,340),"The Code Workshop",F(50))
    if t>1.6:ctext(d,(W//2,420),"Python · data structures · algorithms",F(26,False),(170,180,215))
    if t>3:ctext(d,(W//2,490),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
def d_py(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.P1)],30,150,690,17,22)
    if t>=ts[2]:
        bx(d,800,200,90,40,GOLD,"a");bx(d,800,270,90,40,TEAL,"b");bx(d,1060,225,150,60,PUR,"[1,2,3]",20)
        d.line([(890,220),(1060,245)],fill=WHITE,width=3);d.line([(890,290),(1060,265)],fill=WHITE,width=3)
        ctext(d,(1000,330),"two names, one object",F(17),WHITE)
    if t>=ts[3]:
        bx(d,800,390,90,40,GOLD,"c");bx(d,1060,380,150,50,GRN,"[1,2,3]",20);d.line([(890,410),(1060,405)],fill=WHITE,width=3);ctext(d,(1000,450),"copy: new object",F(17),WHITE)
    if t>=ts[5]:ctext(d,(1000,500),"bag=[] is created once",F(17),RED)
    banner(d,ts[6],t,"TWIST #1 — mutable default arguments are shared",GOLD,115)
def d_arch(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.P2)],30,150,690,17,22)
    if t>=ts[2]:
        for i,(l,c) in enumerate([("source .py",GOLD),("compiler",TEAL),("bytecode",PUR),("virtual machine",GRN)]):
            y=175+i*70;bx(d,820,y,260,46,c,l,18)
            if i<3:d.polygon([(950,y+50),(940,y+62),(960,y+62)],fill=WHITE)
    if t>=ts[4]:bx(d,1100,200,130,70,RED,"refcount\n→ free at 0",14)
    banner(d,ts[5],t,"TWIST #2 — choose the right big O before micro-tricks",GOLD,115)
def d_learn(d,t,sc):
    ts=sc.ts
    labs=[("1 READ",GOLD),("2 PREDICT",TEAL),("3 RUN",PUR),("4 CHANGE",GRN)]
    pos=[(300,230),(700,230),(700,420),(300,420)]
    if t>=ts[2]:
        for a,b in [(0,1),(1,2),(2,3),(3,0)]:
            (x1,y1),(x2,y2)=pos[a],pos[b];d.line([(x1+120,y1+35),(x2+120,y2+35)],fill=GRY,width=3)
        for (l,c),(x,y) in zip(labs,pos):bx(d,x,y,240,70,c,l,26)
        ctext(d,(640,345),"prediction = learning",F(22),WHITE)
    if t>=ts[3]:ctext(d,(1110,230),"trace small inputs\nask: cost if n doubles?",F(17),TEAL)
    if t>=ts[4]:ctext(d,(1110,420),"rebuild from\nblank file",F(17),GOLD)
    banner(d,ts[5],t,"TWIST #3 — recognising is not the same as producing",GOLD,115)
def d_ds(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.D1)],30,150,690,17,22)
    if t>=ts[2]:
        a=ease((t-ts[3])/2)
        for i,(l,v,c) in enumerate([("list scan: 1000 steps",1000,RED),("set lookup: 1 step",8,GRN)]):
            y=200+i*70;d.rectangle((770,y,770+max(6,int(450*v/1000*a)),y+36),fill=c);ctext(d,(780,y+52),l,F(17),WHITE,"lm")
    if t>=ts[4]:
        bx(d,800,380,170,60,GOLD,"stack LIFO",18);bx(d,1010,380,200,60,TEAL,"queue FIFO",18)
    banner(d,ts[5],t,"TWIST #4 — list.pop(0) is O(n); use a deque",GOLD,115)
def d_srch(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.S1)],30,150,690,17,22)
    if t>=ts[2]:
        for i in range(11):
            w=int(440*(0.5**i)) if i<10 else 6;y=200+i*26
            if t>=ts[2]+i*.4 or t>=ts[3]:d.rectangle((780,y,780+max(w,6),y+18),fill=[TEAL,GOLD][i%2]);ctext(d,(790+max(w,6),y+9),f"{1000>>i}",F(13),WHITE,"lm")
        ctext(d,(1000,176),"items left after each step",F(16),WHITE)
    banner(d,ts[5],t,"TWIST #5 — binary search needs sorted data",GOLD,115)
def d_srt(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.S2)],30,150,690,17,22)
    if t>=ts[2]:
        for lv in range(4):
            n=2**lv;w=440//n
            for j in range(n):d.rectangle((780+j*w+2,200+lv*50,780+(j+1)*w-2,236+lv*50),outline=[GOLD,TEAL,PUR,GRN][lv],width=2)
            ctext(d,(1235,218+lv*50),f"{n} × {8//n}",F(14),WHITE,"rm")
        ctext(d,(1000,176),"log n levels, n work each",F(16),WHITE)
    banner(d,ts[5],t,"TWIST #6 — merge sort always n log n; quick sort worst n²",GOLD,115)
POS={"A":(830,260),"B":(960,200),"C":(960,320),"D":(1090,200),"E":(1090,320),"F":(1200,260)}
EDG=[("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","F"),("E","F")]
def d_gr(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.G1),(4,codes.G2)],30,150,690,16,20)
    if t>=ts[2]:
        for a,b in EDG:d.line([POS[a],POS[b]],fill=GRY,width=3)
        lev={"A":0,"B":1,"C":1,"D":2,"E":2,"F":3}
        for n,(x,y) in POS.items():
            c=[GOLD,TEAL,PUR,GRN][lev[n]] if t>=ts[3] else TEAL
            d.ellipse((x-20,y-20,x+20,y+20),fill=(20,24,50),outline=c,width=3);ctext(d,(x,y),n,F(18,True),c)
        if t>=ts[3]:ctext(d,(1020,420),"BFS levels: 0 1 1 2 2 3",F(16),WHITE)
    if t>=ts[4]:ctext(d,(1020,455),"Dijkstra: A→D = 4 (via C, B)",F(16),GOLD)
    if t>=ts[5]:ctext(d,(1020,490),"BFS/DFS: V+E   Dijkstra: E log V",F(16),TEAL)
    banner(d,ts[6],t,"TWIST #7 — Dijkstra fails on negative weights",GOLD,115)
def d_wk(d,t,sc):walk(d,sc,t,[(codes.WD1,1,3)])
def d_end(d,t,sc):
    ctext(d,(W//2,230),"The Code Workshop — open",F(52),GOLD)
    for i,x in enumerate(["Python model","bytecode & VM","how to learn","data structures","search & sort","divide & conquer","graphs"]):
        if t>1+i*.4:
            cx=210+(i%4)*270;cy=320+(i//4)*60;rbox(d,(cx-110,cy-22,cx+110,cy+22),(20,24,50),[TEAL,GRN,PUR,GOLD][i%4],10,2);ctext(d,(cx,cy),x,F(18),[TEAL,GRN,PUR,GOLD][i%4])
    if t>6:ctext(d,(W//2,470),"next film: Artificial Intelligence",F(30),WHITE)
SCENES=[("title",d_title,""),("py",d_py,"Room 1 · How Python thinks"),("arch",d_arch,"Room 2 · Architecture under the hood"),("learn",d_learn,"Room 3 · Learning method"),("ds",d_ds,"Room 4 · Data structures"),("srch",d_srch,"Room 5 · Searching"),("srt",d_srt,"Room 6 · Sorting & divide and conquer"),("gr",d_gr,"Room 7 · Graph algorithms"),("wk",d_wk,"Walkthrough · binary search"),("end",d_end,"")]
