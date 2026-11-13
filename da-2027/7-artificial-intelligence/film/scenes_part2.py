from gcommon import *
import codes
P={"A":(1000,210),"B":(900,300),"C":(1100,300),"D":(850,390),"E":(950,390),"F":(1050,390),"G":(1150,390)}
E=[("A","B"),("A","C"),("B","D"),("B","E"),("C","F"),("C","G")]
def d_id(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.AA)],30,150,690,17,22)
    if t>=ts[2]:
        for a,b in E:d.line([P[a],P[b]],fill=GRY,width=2)
        for n,(x,y) in P.items():
            c=GOLD if n=="G" else TEAL;d.ellipse((x-20,y-20,x+20,y+20),fill=(20,24,50),outline=c,width=3);ctext(d,(x,y),n,F(17,True),c)
    if t>=ts[3]:
        for i,(l,c) in enumerate([("limit 0: 1 node",TEAL),("limit 1: 3 nodes",TEAL),("limit 2: 7 nodes → found G",GOLD)]):ctext(d,(1000,450+i*28),l,F(16,True),c)
    tw(d,sc,t,5,"TWIST #1 — DFS memory, BFS answer")
def d_cond(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.AB)],30,150,690,15,19)
    def tri(x0,y0,ed,title,res):
        ctext(d,(x0+90,y0-30),title,F(16),WHITE)
        pos={"A":(x0,y0+60),"B":(x0+90,y0+10),"C":(x0+180,y0+60)}
        pos={"A":(x0,y0),"B":(x0+90,y0+60),"C":(x0+180,y0)} if title.startswith("collider") else {"A":(x0,y0+50),"B":(x0+90,y0+50),"C":(x0+180,y0+50)}
        for a,b in ed:d.line([pos[a],pos[b]],fill=GOLD,width=3)
        for n,(x,y) in pos.items():d.ellipse((x-18,y-18,x+18,y+18),fill=(20,24,50),outline=TEAL,width=3);ctext(d,(x,y),n,F(16,True),TEAL)
        for i,r in enumerate(res):ctext(d,(x0+90,y0+120+i*26),r,F(15,True),GRN if "True" in r.split("=")[-1] else RED)
    if t>=ts[3]:tri(790,200,[("A","B"),("B","C")],"chain A→B→C",["A⊥C : False","A⊥C | B : True"])
    if t>=ts[5]:tri(790,400,[("A","B"),("C","B")],"collider A→B←C",["A⊥C : True","A⊥C | B : False"])
    tw(d,sc,t,6,"TWIST #2 — observing B blocks a chain, opens a collider")
def d_wk(d,t,sc):walk(d,sc,t,[(codes.WA2,1,2)])
SCENES=[("title",mk_title("The Thinking Machine, part 2","iterative deepening · d-separation"),""),("id",d_id,"Room 1 · Iterative deepening"),("cond",d_cond,"Room 2 · Conditional independence"),("wk",d_wk,"Walkthrough · depth budget"),("end",mk_end("AI part 2 — complete",["iterative deepening","chains","colliders","explaining away"],"next: relational algebra"),"")]
