from gcommon import *
import codes
def d_ll(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DS1)],30,150,690,17,22)
    if t>=ts[2]:
        for i,v in enumerate([1,2,3]):
            x=790+i*140;bx(d,x,230,110,54,TEAL,f"{v} | •",20)
            if i<2:d.line([(x+110,257),(x+140,257)],fill=WHITE,width=3);d.polygon([(x+140,257),(x+130,251),(x+130,263)],fill=WHITE)
        ctext(d,(1000,200),"head → value + pointer",F(17),WHITE)
    if t>=ts[3]:
        for i,v in enumerate([3,2,1]):
            x=790+i*140;bx(d,x,360,110,54,GOLD,f"{v} | •",20)
        ctext(d,(1000,440),"after reverse: every pointer flipped",F(17),GOLD)
    tw(d,sc,t,4,"TWIST #1 — fast to change, slow to look up")
def d_bst(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DS2)],30,150,690,15,19)
    N={50:(1000,200),30:(900,270),70:(1100,270),20:(850,340),40:(950,340),60:(1050,340),80:(1150,340)}
    E=[(50,30),(50,70),(30,20),(30,40),(70,60),(70,80)]
    if t>=ts[2]:
        for a,b in E:d.line([N[a],N[b]],fill=GRY,width=2)
        for v,(x,y) in N.items():d.ellipse((x-20,y-20,x+20,y+20),fill=(20,24,50),outline=TEAL,width=3);ctext(d,(x,y),str(v),F(15,True),TEAL)
        ctext(d,(1000,172),"balanced: height 3",F(16),WHITE)
    if t>=ts[4]:
        for i in range(7):
            x=800+i*65;y=410+i*14;d.ellipse((x-14,y-14,x+14,y+14),outline=RED,width=3)
            if i:d.line([(x-65+10,y-14+4),(x-10,y-4)],fill=RED,width=2)
        ctext(d,(1000,525),"sorted input: height 7 (a chain)",F(16),RED)
    tw(d,sc,t,5,"TWIST #2 — search cost = height: log n or n")
def d_ht(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.DS3)],30,150,690,17,22)
    if t>=ts[2]:
        for i in range(5):
            y=200+i*55;bx(d,790,y,60,44,TEAL,str(i),20)
        ctext(d,(820,180),"slot",F(14),WHITE)
    if t>=ts[3]:
        for j,v in enumerate([12,22,7,17,27]):bx(d,870+j*70,310,60,44,GOLD,str(v),20)
        bx(d,870,420,60,44,TEAL,"3",20);ctext(d,(1090,285),"collision: all land in slot 2",F(15),RED)
    if t>=ts[4]:ctext(d,(1010,520),"load factor = 6/5 = 1.2",F(18,True),GRN)
    tw(d,sc,t,5,"TWIST #3 — a bad hash makes lookup O(n)")
def d_sorts(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(2,codes.DS4),(4,codes.DS5)],30,150,690,15,19)
    if k==0:
        for i,(l,v,c) in enumerate([("insertion, sorted: 0 shifts",0,GRN),("insertion, reversed: 15 shifts",15,RED),("selection: ≤ 5 swaps",5,TEAL)]):
            y=200+i*70;d.rectangle((780,y,780+max(4,v*24),y+34),fill=c);ctext(d,(780,y+52),l,F(16),WHITE,"lm")
    else:
        a=ease((t-ts[4])/2)
        for i,(l,v,c) in enumerate([("quick sort, random: 1 707",1707,TEAL),("quick sort, sorted: 19 900",19900,RED)]):
            y=220+i*90;d.rectangle((780,y,780+max(4,int(440*v/19900*a)),y+40),fill=c);ctext(d,(780,y+60),l,F(17),WHITE,"lm")
    tw(d,sc,t,5,"TWIST #4 — quick sort: n log n average, n² worst")
def d_wk(d,t,sc):walk(d,sc,t,[(codes.WS1,1,3)])
SCENES=[("title",mk_title("The Data Structure Workshop","linked lists · trees · hashing · sorting"),""),("ll",d_ll,"Room 1 · Linked lists"),("bst",d_bst,"Room 2 · Binary search trees"),("ht",d_ht,"Room 3 · Hash tables"),("sorts",d_sorts,"Room 4 · Sorting"),("wk",d_wk,"Walkthrough · insertion sort"),("end",mk_end("Data structures — complete",["linked lists","BST height","hash chaining","insertion sort","selection sort","quick sort"],"next: statistics"),"")]
