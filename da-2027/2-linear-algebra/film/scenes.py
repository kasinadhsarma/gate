from viz import *
import codes
import numpy as np
def T(sc,t,k):return t>=sc.ts[k]
def title(sub,t,col=GOLD):
    ctext(ImageDraw.Draw(BG),(0,0),"",F(1)) if False else None
def head(d,txt,col=WHITE):ctext(d,(W//2,165),txt,F(30),col)
def d_title(d,t,sc):
    for i in range(14):
        x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
    ctext(d,(W//2,240),"OPERATION  GATE",F(84),GOLD);ctext(d,(W//2,340),"The Tower of Vectors",F(50))
    if t>1.6:ctext(d,(W//2,420),"Linear Algebra · nine floors · nine twists",F(26,False),(170,180,215))
    if t>3:ctext(d,(W//2,490),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
def d_vs(d,t,sc):
    ts=sc.ts;ax=Ax(60,170,520,360,(-3,3),(-3,3))
    ax.axes(d,range(-3,4),range(-3,4),labels=False)
    if t>=ts[4]:
        ax.curve(d,lambda x:-x,TEAL,5);ctext(d,(ax.px(1.4),ax.py(-0.9)),"x+y=0 : subspace",F(17),TEAL)
        ax.curve(d,lambda x:x+1,RED,5);ctext(d,(ax.px(-2.3),ax.py(-0.9)),"y=x+1 : no origin",F(17),RED)
    if t>=ts[5]:
        arrow(d,ax.P(0,0),ax.P(1,0),GOLD);arrow(d,ax.P(0,0),ax.P(1,1),GRN);ctext(d,(ax.px(1.1),ax.py(-.3)),"e1",F(16),GOLD);ctext(d,(ax.px(1.3),ax.py(1.1)),"v",F(16),GRN)
    ctext(d,(320,152),"the room (a plane through the origin)",F(18,False),(170,180,215))
    if t>=ts[7]:
        rbox(d,(650,170,1250,330),(20,24,50),TEAL,12,2)
        ctext(d,(950,200),"basis of R²:  (1,0) , (1,1)  → dim 2",F(22,True,True),TEAL)
        ctext(d,(950,245),"(1,2) and (2,4): same line",F(22,True,True),RED)
        ctext(d,(950,290),"dependent → dim of span = 1",F(22,True,True),RED)
    if t>=ts[8]:
        for i,(a,b) in enumerate([("2x2 matrices","dim 4"),("symmetric 2x2","dim 3"),("poly deg ≤ 2","dim 3")]):
            x=650+i*200;rbox(d,(x,370,x+185,470),(20,24,50),GOLD,10,2);ctext(d,(x+92,400),a,F(16),WHITE);ctext(d,(x+92,440),b,F(26),GOLD)
    banner(d,ts[8],t,"TWIST #1 — matrices and polynomials are vectors too",GOLD,115)
def d_mt(d,t,sc):
    ts=sc.ts;types=[("symmetric","A = Aᵀ  → real λ",TEAL,[[2,1],[1,3]]),("orthogonal","QᵀQ = I  → keeps length",GRN,[["c","-s"],["s","c"]]),("triangular","λ on the diagonal",PUR,[[2,5],[0,3]]),("idempotent","A² = A  (projection)",GOLD,[[1,0],[0,0]])]
    for i,(nm,pr,c,M) in enumerate(types):
        if t>=ts[[2,3,3,6][i]]:
            x=60+(i%2)*300;y=160+(i//2)*190
            rbox(d,(x,y,x+280,y+170),(20,24,50),c,12,2);ctext(d,(x+140,y+22),nm,F(20),c);mat(d,x+90,y+45,M,50,34,WHITE,20);ctext(d,(x+140,y+148),pr,F(15,False),(190,200,230))
    if t>=ts[5]:
        rbox(d,(680,160,1250,330),(20,24,50),RED,12,2)
        for j,l in enumerate(["det(AB) = det A · det B","(AB)ᵀ = BᵀAᵀ   order flips","tr(A) = sum of diagonal","det = volume scale"]):ctext(d,(700,190+j*36),l,F(20,True,True),WHITE,"lm")
    if t>=ts[7]:
        ang=min(1,(t-ts[7])/2.5)*math.pi/2;cx,cy=900,440
        d.line([(cx-120,cy),(cx+120,cy)],fill=GRY,width=2);d.line([(cx,cy-120),(cx,cy+90)],fill=GRY,width=2)
        arrow(d,(cx,cy),(cx+90,cy),GRY,3);arrow(d,(cx,cy),(cx+90*math.cos(ang),cy-90*math.sin(ang)),RED,5)
        ctext(d,(1130,420),"rotate 90°:",F(18),RED);ctext(d,(1130,450),"[[0,-1],[1,0]]",F(18,True,True),WHITE);ctext(d,(1130,480),"λ = ± i  (no real λ)",F(18),RED)
    banner(d,ts[7],t,"TWIST #2 — a rotation has no real direction it keeps",GOLD,115)
def d_ls(d,t,sc):
    ts=sc.ts
    if t>=ts[3]:
        for j,l in enumerate(["x +  y +  z =  6","     2y + 5z = -4","2x + 5y -  z = 27"]):ctext(d,(70,200+j*42),l,F(26,True,True),WHITE,"lm")
    if t>=ts[3]+3:
        ctext(d,(70,350),"↓ eliminate (staircase)",F(18),(170,180,215),"lm")
        for j,l in enumerate(["x + y + z =  6","    2y +5z = -4","     -10.5z =  21"]):ctext(d,(70,390+j*36),l,F(24,True,True),TEAL,"lm")
    if t>=ts[3]+6:
        ctext(d,(520,230),"z = -2",F(34,True,True),GOLD,"lm");ctext(d,(520,285),"y =  3",F(34,True,True),GOLD,"lm");ctext(d,(520,340),"x =  5",F(34,True,True),GOLD,"lm")
    if t>=ts[5]:
        for j,l in enumerate(["5+3-2 = 6 ✓","6-10 = -4 ✓","10+15+2 = 27 ✓"]):ctext(d,(520,410+j*34),l,F(22,True,True),GRN,"lm")
    if t>=ts[6]:
        rbox(d,(790,160,1250,345),(20,24,50),TEAL,12,2)
        for j,(l,c) in enumerate([("rank A ≠ rank [A|b]  → none",RED),("rank = n               → unique",GRN),("rank < n               → infinite",GOLD)]):ctext(d,(810,195+j*50),l,F(20,True,True),c,"lm")
    if t>=ts[7]:
        ax=Ax(800,365,200,110,(0,4),(0,4));ax.axes(d,(),(),grid=False,labels=False)
        ax.curve(d,lambda x:2-x,GOLD,4,ylim=(0,4));ctext(d,(900,495),"x+y=2 (twice) : ∞",F(15),GOLD)
        ax2=Ax(1030,365,200,110,(0,4),(0,4));ax2.axes(d,(),(),grid=False,labels=False)
        ax2.curve(d,lambda x:2-x,GOLD,4,ylim=(0,4));ax2.curve(d,lambda x:5-x,RED,4,ylim=(0,4));ctext(d,(1130,495),"...=5 : none",F(15),RED)
    banner(d,ts[7],t,"TWIST #3 — change one number and ∞ solutions become none",GOLD,115)
def d_rn(d,t,sc):
    ts=sc.ts;M=[[1,2,3],[2,4,6],[1,0,1]]
    cols=[[WHITE]*3,[RED]*3,[WHITE]*3] if t>=ts[2] else None
    ctext(d,(190,175),"A",F(26),GOLD);mat(d,100,195,M,70,44,WHITE,26,cols)
    if t>=ts[2]:ctext(d,(330,255),"← 2 × row 1",F(18),RED,"lm");ctext(d,(190,355),"rank = 2",F(30),GOLD)
    if t>=ts[3]:
        rbox(d,(60,400,520,500),(20,24,50),TEAL,12,2);ctext(d,(290,430),"rank + nullity = columns",F(22),TEAL);ctext(d,(290,472),"2 + 1 = 3",F(30,True,True),WHITE)
    if t>=ts[5]:
        ctext(d,(660,175),"null space (line)",F(24),PUR)
        ax=Ax(600,195,300,300,(-2,2),(-2,2));ax.axes(d,(-1,0,1),(-1,0,1),labels=False)
        a=ease((t-ts[5])/2);arrow(d,ax.P(0,0),ax.P(-1.5*a,-1.5*a),PUR,5);arrow(d,ax.P(0,0),ax.P(1.5*a,1.5*a),PUR,5)
        ctext(d,(1070,230),"(-1, -1, 1)",F(28,True,True),PUR);ctext(d,(1070,275),"A · v = (0,0,0)",F(24,True,True),WHITE)
        ctext(d,(1070,320),"x+2y+3z = 0",F(20,True,True),(190,200,230));ctext(d,(1070,350),"x + z = 0",F(20,True,True),(190,200,230))
    if t>=ts[6]:ctext(d,(1070,420),"row rank = column rank",F(22),GOLD)
    banner(d,ts[7],t,"TWIST #4 — a wide matrix always hides a vanishing vector",GOLD,115)
def d_ev(d,t,sc):
    ts=sc.ts;ax=Ax(60,170,480,360,(-3,6),(-5,6));ax.axes(d,range(-3,7,2),range(-4,7,2),labels=False)
    A=np.array([[4,1],[2,3.]])
    if t>=ts[2]:
        k=ease((t-ts[2])/3)
        for ang in range(0,360,40):
            v=np.array([math.cos(math.radians(ang)),math.sin(math.radians(ang))])*1.3
            w=(1-k)*v+k*(A@v);arrow(d,ax.P(0,0),ax.P(*w),(90,100,140),2,8)
    if t>=ts[3]:
        arrow(d,ax.P(0,0),ax.P(1,1),GOLD,5);arrow(d,ax.P(0,0),ax.P(5,5),GOLD,3);ctext(d,(ax.px(4.4),ax.py(5.7)),"λ=5",F(18),GOLD)
        arrow(d,ax.P(0,0),ax.P(1,-2),TEAL,5);arrow(d,ax.P(0,0),ax.P(2,-4),TEAL,3);ctext(d,(ax.px(2.8),ax.py(-4.2)),"λ=2",F(18),TEAL)
    ctext(d,(780,170),"A = [[4,1],[2,3]]",F(24,True,True),WHITE)
    if t>=ts[3]:
        ctext(d,(620,215),"A(1,1) = (5,5)  = 5·(1,1)",F(20,True,True),GOLD,"lm");ctext(d,(620,250),"A(1,-2) = (2,-4) = 2·(1,-2)",F(20,True,True),TEAL,"lm")
    if t>=ts[5]:
        rbox(d,(610,290,1250,400),(20,24,50),GRN,12,2)
        ctext(d,(630,320),"5 + 2 = 7  = trace  (4+3)",F(22,True,True),GRN,"lm");ctext(d,(630,365),"5 × 2 = 10 = det  (12-2)",F(22,True,True),GRN,"lm")
    if t>=ts[6]:ctext(d,(930,435),"A = P D P⁻¹   →   Aⁿ = P Dⁿ P⁻¹",F(24,True,True),PUR)
    if t>=ts[7]:
        ctext(d,(930,480),"A⁵ = [[2094,1031],[2062,1063]]",F(20,True,True),WHITE);ctext(d,(930,515),"trace 3157 = 5⁵ + 2⁵ = 3125 + 32",F(20,True,True),GOLD)
    banner(d,ts[7],t,"TWIST #5 — the 5th power came free from the eigenvalues",GOLD,115)
def d_qf(d,t,sc):
    ts=sc.ts
    def bowl(x0,fn,c,title,sub):
        ax=Ax(x0,200,230,200,(-1.5,1.5),(-1.5,1.5))
        for r in (0.3,0.6,0.9,1.2):
            pts=[]
            for k in range(0,361,6):
                th=math.radians(k);v=np.array([math.cos(th),math.sin(th)])
                q=fn(v);s=r/math.sqrt(abs(q)) if abs(q)>0.05 else None
                if s is not None and abs(s)<1.5:pts.append(ax.P(v[0]*s,v[1]*s))
            if len(pts)>2:d.line(pts,fill=c,width=2)
        ctext(d,(x0+115,170),title,F(18),c);ctext(d,(x0+115,420),sub,F(14,False),(190,200,230))
    if t>=ts[3]:
        bowl(60,lambda v:2*v[0]**2+2*v[0]*v[1]*2/2*1+2*v[1]**2,GRN,"pos. definite","A=[[2,1],[1,2]]  λ=3,1")
        bowl(330,lambda v:v[0]**2+4*v[0]*v[1]+v[1]**2,RED,"indefinite","A=[[1,2],[2,1]]  λ=3,-1")
    if t>=ts[2]:
        for j,(l,c) in enumerate([("λ all > 0 : bowl (min)",GRN),("λ all < 0 : hill (max)",TEAL),("mixed signs : saddle",RED),("some λ = 0 : semi-definite",GOLD)]):ctext(d,(640,200+j*42),l,F(21,True,True),c,"lm")
    if t>=ts[5]:
        ctext(d,(640,400),"xᵀAx at (1,-1):",F(20),WHITE,"lm");ctext(d,(640,440),"1 - 4 + 1 = -2  < 0",F(30,True,True),RED,"lm")
    banner(d,ts[6],t,"TWIST #6 — positive diagonal, yet negative form",GOLD,115)
def d_lu(d,t,sc):
    ts=sc.ts
    ctext(d,(60,215),"A",F(24),GOLD,"lm");mat(d,100,200,[[2,1,1],[4,3,3],[8,7,9]],56,38,WHITE,22)
    if t>=ts[2]:
        ctext(d,(300,215),"=",F(30),WHITE);ctext(d,(350,185),"L",F(24),TEAL);mat(d,330,200,[[1,0,0],["2",1,0],["4","3",1]],56,38,TEAL,22,[[TEAL]*3,[GOLD,TEAL,TEAL],[GOLD,GOLD,TEAL]])
        ctext(d,(540,215),"×",F(30),WHITE);ctext(d,(620,185),"U",F(24),PUR);mat(d,560,200,[[2,1,1],[0,1,1],[0,0,2]],56,38,PUR,22)
    if t>=ts[2]+2:
        for j,l in enumerate(["R2 ← R2 - 2·R1","R3 ← R3 - 4·R1","R3 ← R3 - 3·R2"]):ctext(d,(60,350+j*34),l,F(21,True,True),(190,200,230),"lm")
        ctext(d,(60,465),"multipliers 2, 4, 3 go into L",F(20),GOLD,"lm")
    if t>=ts[3]:
        rbox(d,(480,340,1250,490),(20,24,50),GRN,12,2)
        ctext(d,(500,370),"check row 3:  4·(2,1,1) + 3·(0,1,1) + 1·(0,0,2)",F(19,True,True),WHITE,"lm")
        ctext(d,(500,410),"= (8, 4+3, 4+3+2) = (8, 7, 9)  ✓",F(21,True,True),GRN,"lm")
        ctext(d,(500,455),"det A = 2·1·2 = 4   (diagonal of U)",F(21,True,True),GOLD,"lm")
    if t>=ts[7]:
        ctext(d,(900,525),"zero pivot?  →  P A = L U  (swap rows)",F(22,True,True),RED)
    banner(d,ts[7],t,"TWIST #7 — a zero pivot forces a row swap",GOLD,115)
def d_svd(d,t,sc):
    ts=sc.ts;B=np.array([[3,2,2],[2,3,-2.]])
    ctext(d,(60,190),"A",F(24),GOLD,"lm");mat(d,100,172,[[3,2,2],[2,3,-2]],60,40,WHITE,24)
    ctext(d,(330,190),"=  U  Σ  Vᵀ",F(28,True,True),PUR,"lm")
    if t>=ts[3]:
        ctext(d,(60,285),"A·Aᵀ = [[17,8],[8,17]]",F(22,True,True),WHITE,"lm");ctext(d,(60,325),"eigenvalues 25 and 9",F(22,True,True),TEAL,"lm")
    if t>=ts[5]:
        for i,(s,c) in enumerate([(5,GOLD),(3,TEAL)]):
            h=s*26*ease((t-ts[5])/1.5);x=140+i*110;d.rectangle((x,520-h,x+70,520),fill=c);ctext(d,(x+35,500-h-14),f"σ{i+1}={s}",F(20),c)
        ctext(d,(250,545),"singular values",F(16,False),(170,180,215))
        ctext(d,(560,300),"Σ entries²  = 9+4+4+4+9+4 = 34",F(21,True,True),WHITE,"lm");ctext(d,(560,340),"σ1² + σ2²   = 25 + 9     = 34",F(21,True,True),GOLD,"lm")
    if t>=ts[6]:
        rbox(d,(560,390,1250,480),(20,24,50),GRN,12,2);ctext(d,(905,420),"keep σ1 only  →  best rank-1 copy",F(23),GRN);ctext(d,(905,460),"image compression · PCA",F(20,False),(190,200,230))
    banner(d,ts[7],t,"TWIST #8 — dropping small σ is provably the best simplification",GOLD,115)
def d_py(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(2,codes.LA1),(5,codes.LA2)],30,150,680,17,22)
    if k==0:
        ctext(d,(960,175),"staircase → back-substitute",F(20),TEAL)
        for j,(l,c) in enumerate([("x + y + z = 6",WHITE),("2y + 5z = -4",WHITE),("-10.5z = 21",TEAL)]):ctext(d,(780,225+j*40),l,F(22,True,True),c,"lm")
        if t>=ts[3]:
            for j,(l,c) in enumerate([("z = -2",GOLD),("y = 3",GOLD),("x = 5",GOLD)]):ctext(d,(780,365+j*42),l,F(30,True,True),c,"lm")
    if k==1:
        A=[[4,1],[2,3]];v=[1,0];lams=[]
        for _ in range(20):
            w=[A[0][0]*v[0]+A[0][1]*v[1],A[1][0]*v[0]+A[1][1]*v[1]];b=max(abs(w[0]),abs(w[1]));lams.append(b);v=[w[0]/b,w[1]/b]
        ax=Ax(760,200,460,260,(0,20),(0,6));ax.axes(d,range(0,21,5),(0,2,4,6),labels=True)
        n=int(clamp((t-ts[5])/6)*20)
        pts=[ax.P(i+1,l) for i,l in enumerate(lams[:max(n,1)])]
        if len(pts)>1:d.line(pts,fill=GOLD,width=4)
        for p in pts:d.ellipse((p[0]-4,p[1]-4,p[0]+4,p[1]+4),fill=GOLD)
        d.line([ax.P(0,5),ax.P(20,5)],fill=GRN,width=2);ctext(d,(1000,175),"scale factor → eigenvalue 5",F(20),GOLD)
    banner(d,ts[7],t,"PYTHON TWIST — never test floats with ==",GOLD,115)
def d_dsa(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(2,codes.LA3),(5,codes.LA4)],30,150,680,17,22)
    if k==0:
        ctext(d,(960,175),"work = n³  (log scale bars)",F(20),TEAL)
        for i,(n,o) in enumerate([(2,8),(4,64),(8,512),(16,4096)]):
            h=math.log2(o)*17*ease((t-ts[2]-.5*i)/1.2);x=760+i*115;d.rectangle((x,500-h,x+80,500),fill=[TEAL,GRN,PUR,GOLD][i])
            ctext(d,(x+40,515),f"n={n}",F(16),WHITE);ctext(d,(x+40,490-h),str(o),F(18,True,True),WHITE)
    if k==1:
        ctext(d,(960,175),"100 right-hand sides, n = 1000",F(20),TEAL)
        a=ease((t-ts[5])/2);d.rectangle((760,230,760+int(460*a),290),fill=RED);ctext(d,(990,260),"redo elimination: 3.3×10¹⁰",F(20),WHITE)
        d.rectangle((760,330,760+int(6*a),390),fill=GRN);ctext(d,(990,420),"LU: 4.3×10⁸   (≈ 77× cheaper)",F(20),GRN)
    banner(d,ts[6],t,"DSA TWIST — choose the algorithm by what you need",GOLD,115)
def d_wk(d,t,sc):
    walk(d,sc,t,[(codes.W_LA1,2,7),(codes.W_LA2,8,10)])
def d_end(d,t,sc):
    ctext(d,(W//2,230),"The Tower of Vectors — climbed",F(52),GOLD)
    for i,x in enumerate(["vector spaces","matrix types","linear systems","rank & nullity","eigenvalues","quadratic forms","LU","SVD"]):
        if t>1+i*.4:
            cx=240+(i%4)*270;cy=320+(i//4)*60;rbox(d,(cx-110,cy-22,cx+110,cy+22),(20,24,50),[TEAL,GRN,PUR,GOLD][i%4],10,2);ctext(d,(cx,cy),x,F(20),[TEAL,GRN,PUR,GOLD][i%4])
    if t>6:ctext(d,(W//2,470),"next film: Calculus & Optimization",F(30),WHITE)
SCENES=[("title",d_title,""),("vs",d_vs,"Floor 1 · Vector spaces"),("mt",d_mt,"Floor 2 · Matrix types"),("ls",d_ls,"Floor 3 · Linear systems"),("rn",d_rn,"Floor 4 · Rank and nullity"),("ev",d_ev,"Floor 5 · Eigenvalues and eigenvectors"),("qf",d_qf,"Floor 6 · Quadratic forms"),("lu",d_lu,"Floor 7 · LU decomposition"),("svd",d_svd,"Floor 8 · SVD"),("wk",d_wk,"Walkthrough · how the code thinks"),("py",d_py,"Lab 1 · Python for linear algebra"),("dsa",d_dsa,"Lab 2 · Complexity (DSA)"),("end",d_end,"")]
