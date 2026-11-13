from lhelp import *
import codes,math
def d_gnn(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L21A)],30,150,690,15,20)
    P={0:(900,260),1:(800,340),2:(1000,340),3:(1100,260)}
    if t>=ts[2]:
        for a,b in [(0,1),(0,2),(2,3)]:edge(d,P[a],P[b])
        L1={0:.5,1:.5,2:.25,3:0.0};L2={0:.438,1:.5,2:.25,3:.125};V={0:1.0,1:0.0,2:0.0,3:0.0}
        cur=V if t<ts[3] else (L1 if t<ts[3]+7 else L2)
        for n,(x,y) in P.items():node(d,x,y,str(n),GOLD if cur[n]>0 else TEAL,22,17);lab(d,x,y+38,f"{cur[n]:g}",WHITE,15)
        lab(d,1000,420,"start" if t<ts[3] else ("after layer 1" if t<ts[3]+7 else "after layer 2"),GRN,18)
    tw(d,sc,t,5,'TWIST #1 — repeated neighbour averaging')
def d_sym(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L21B)],30,150,690,15,20)
    import math as m
    if t>=ts[2]:
        pts=[(0,0),(3,0),(3,4)];s=26
        def draw(ox,oy,th,col,name):
            q=[(ox+s*(x*m.cos(th)-y*m.sin(th)),oy-s*(x*m.sin(th)+y*m.cos(th))) for x,y in pts]
            d.polygon(q,outline=col,width=4)
            for p in q:d.ellipse((p[0]-6,p[1]-6,p[0]+6,p[1]+6),fill=col)
            lab(d,ox+40,oy+25,name,col,14)
        draw(800,380,0,TEAL,"original")
        if t>=ts[2]+3:draw(1060,380,0.7,GOLD,"rotated")
        lab(d,1000,210,"distances: 3, 5, 4   |   3, 5, 4",GRN,18)
    if t>=ts[3]:lab(d,1000,470,"permute inputs → outputs permute: True",GRN,17)
    tw(d,sc,t,5,'TWIST #2 — build the symmetry in')
def d_wk(d,t,sc):walk(d,sc,t,[(WK21,1,2)])
SCENES=[("title",mk_title('Geometric Deep Learning','graph networks · symmetry'),""),("gnn",d_gnn,'Room 1 · Graph networks'),("sym",d_sym,'Room 2 · Equivariance'),("wk",d_wk,'Walkthrough · message passing'),("end",mk_end('Geometric deep learning — complete',['message passing', 'hops', 'rotation', 'permutation'],'next: optimization and overfitting'),"")]
