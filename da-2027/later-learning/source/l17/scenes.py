from lhelp import *
import codes
def d_flow(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L17A)],30,150,690,13,17)
    P={"S":(810,310),"A":(1000,230),"B":(1000,400),"T":(1190,310)}
    if t>=ts[2]:
        E=[("S","A",3),("S","B",2),("A","B",1),("A","T",2),("B","T",3)]
        for a,b,c in E:edge(d,P[a],P[b],GRY,3,f"cap {c}",WHITE)
        if t>=ts[2]+4:
            for a,b in [("S","A"),("A","T")]:d.line([P[a],P[b]],fill=GOLD,width=7)
            lab(d,1000,185,"bottleneck path pushed",GOLD,14)
        for n,(x,y) in P.items():node(d,x,y,n,TEAL,20,17)
    if t>=ts[3]:lab(d,1000,480,"reverse edges let us undo a choice",WHITE,15)
    if t>=ts[4]:lab(d,1000,520,"max flow = 5 = min cut",GRN,20)
    tw(d,sc,t,5,"TWIST #1 — no augmenting path left → flow is maximal")
def d_scc(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L17B),(4,L17C)],30,150,690,12,16)
    P={0:(840,260),1:(900,350),2:(780,350),3:(1120,260),4:(1180,350),5:(1060,350)}
    if t>=ts[2]:
        E=[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)]
        for a,b in E:arrow(d,P[a],P[b],GRN if a<3 else PUR,3,10)
        arrow(d,P[2],P[3],GRY,3,10)
        for n,(x,y) in P.items():node(d,x,y,str(n),GRN if n<3 else PUR,18,16)
        if t>=ts[2]+8:lab(d,840,400,"component 1",GRN,15);lab(d,1120,400,"component 2",PUR,15)
    if t>=ts[4]:
        d.line([P[2],P[3]],fill=RED,width=7);lab(d,950,250,"bridge (2,3)",RED,16)
    tw(d,sc,t,5,"TWIST #2 — a DFS pass or two finds every weak point")
def d_wk(d,t,sc):walk(d,sc,t,[(WK17,1,2)])
SCENES=[("title",mk_title("Network Flow and Connectivity","Edmonds-Karp · SCC · bridges"),""),("flow",d_flow,"Room 1 · Max flow"),("scc",d_scc,"Room 2 · SCC and bridges"),("wk",d_wk,"Walkthrough · bottleneck"),("end",mk_end("Advanced graphs 2 — complete",["augmenting path","max-flow = min-cut","Kosaraju","Tarjan"],"next: advanced DP and strings"),"")]
