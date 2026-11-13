from lhelp import *
import codes
P={"A":(810,300),"B":(1000,230),"C":(1000,400),"D":(1190,300)}
def d_sp(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L16A),(4,L16B)],30,150,690,14,19)
    if t>=ts[2]:
        neg=t>=ts[4];W=[("A","B",4),("A","C",1),("C","B",-2 if neg else 2),("C","D",7),("B","D",1)]
        for a,b,w in W:edge(d,P[a],P[b],RED if w<0 else GRY,3,w,RED if w<0 else WHITE)
        for n,(x,y) in P.items():node(d,x,y,n,TEAL,20,17)
        D1={"A":0,"C":1,"B":3,"D":4};D2={"A":0,"C":1,"B":-1,"D":0}
        for n,(x,y) in P.items():
            if t>=ts[2]+2.5:lab(d,x,y+36,f"d={(D2 if neg and t>=ts[4]+4 else D1)[n]}",GOLD,15)
        lab(d,1000,500,"Bellman-Ford with the -2 edge" if neg else "Dijkstra from A",GRN,16)
    tw(d,sc,t,5,"TWIST #1 — Dijkstra needs no negative edges")
def d_mst(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L16C),(4,L16D)],30,150,690,14,19)
    if t>=ts[2]:
        W=[("A","B",1),("A","C",3),("B","C",2),("C","D",4)];keep={("A","B"),("B","C"),("C","D")}
        for i,(a,b,w) in enumerate(W):
            on=t>=ts[2]+2+i*1.5;ok=(a,b) in keep
            edge(d,P[a],P[b],(GOLD if ok else (90,50,50)) if on else GRY,6 if (on and ok) else 3,w)
        for n,(x,y) in P.items():node(d,x,y,n,TEAL,20,17)
        if t>=ts[2]+8:lab(d,1000,450,"MST cost = 1 + 2 + 4 = 7",GOLD,18)
    if t>=ts[4]:
        for i,n in enumerate(["shirt","pants","tie","shoes","jacket"]):
            if t>=ts[4]+1+i*1.0:cell(d,780+i*92,490,86,36,n,GRN,fs=14)
    tw(d,sc,t,5,"TWIST #2 — greedy edges; count dependencies")
def d_wk(d,t,sc):walk(d,sc,t,[(WK16,1,2)])
SCENES=[("title",mk_title("Shortest Paths, MST, Ordering","Dijkstra · Bellman-Ford · Kruskal · topological sort"),""),("sp",d_sp,"Room 1 · Shortest paths"),("mst",d_mst,"Room 2 · MST and ordering"),("wk",d_wk,"Walkthrough · relaxation"),("end",mk_end("Advanced graphs 1 — complete",["Dijkstra","Bellman-Ford","Kruskal","Kahn"],"next: flow and connectivity"),"")]
