from gcommon import *
import codes
def d_hc(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(4,codes.MA)],30,150,690,15,19)
    pts=[1,2,3,5,7,8,9]
    if t>=ts[2]:
        for p in pts:
            x=790+p*45;d.ellipse((x-9,430-9,x+9,430+9),fill=TEAL);ctext(d,(x,455),str(p),F(13),WHITE)
        ctext(d,(1000,175),"merge closest clusters → dendrogram",F(16),WHITE)
    if t>=ts[3]:
        ctext(d,(900,215),"single: closest pair",F(15),GOLD);ctext(d,(1130,215),"complete: farthest pair",F(15),PUR)
    if t>=ts[4]:
        ctext(d,(900,255),"merges at 2, 2",F(18,True),GOLD);ctext(d,(1130,255),"merges at 4, 8",F(18,True),PUR)
    tw(d,sc,t,5,"TWIST #1 — single linkage chains; complete stays compact")
def d_lda(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.MB)],30,150,690,15,19)
    ax=Ax(780,190,320,300,(0,10),(0,9));ax.axes(d,(),(),labels=False)
    for p in [(1,2),(2,3),(3,3),(2,1)]:ax.dot(d,p[0],p[1],TEAL,6)
    for p in [(6,5),(7,7),(8,6),(7,4)]:ax.dot(d,p[0],p[1],GOLD,6)
    if t>=ts[4]:
        ax.curve(d,lambda x:x*0.111/1.194*0+ (0.111/1.194)*x+0.2,WHITE,2) if False else None
        ctext(d,(1180,260),"w = (1.194, 0.111)",F(15),GRN);ctext(d,(1180,300),"means project to\n2.64 and 8.97",F(15),WHITE)
    tw(d,sc,t,5,"TWIST #2 — LDA uses labels; PCA ignores them")
def d_mlr(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.MC)],30,150,690,15,19)
    if t>=ts[2]:
        bx(d,800,200,420,60,TEAL,"y = w0 + w1·x1 + w2·x2",22)
        bx(d,800,290,420,60,GOLD,"XᵀX · w = Xᵀy",24)
    if t>=ts[3]:bx(d,800,380,420,60,GRN,"w = [-1.0, 2.0, 1.0]",24)
    tw(d,sc,t,4,"TWIST #3 — correlated features make XᵀX unstable")
SCENES=[("title",mk_title("The Learning Machine, part 2","hierarchical clustering · LDA · multiple regression"),""),("hc",d_hc,"Room 1 · Hierarchical clustering"),("lda",d_lda,"Room 2 · Linear discriminant analysis"),("mlr",d_mlr,"Room 3 · Multiple regression"),("end",mk_end("ML part 2 — complete",["linkage","dendrogram","Fisher LDA","normal equations"],"next: artificial intelligence"),"")]
