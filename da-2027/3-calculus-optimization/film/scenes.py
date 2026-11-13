from viz import *
import codes
def reveal(f,xr,a):return lambda x:f(x)
def grow(ax,d,f,col,t,t0,dur,wd=4,**k):
    a=clamp((t-t0)/dur)
    if a<=0:return
    x0,x1=k.pop('xr',ax.xr);ax.curve(d,f,col,wd,xr=(x0,x0+(x1-x0)*a),**k)
def d_title(d,t,sc):
    for i in range(14):
        x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
    ctext(d,(W//2,240),"OPERATION  GATE",F(84),GOLD);ctext(d,(W//2,340),"The Hill of Change",F(50))
    if t>1.6:ctext(d,(W//2,420),"Calculus & Optimization · five hills · five twists",F(26,False),(170,180,215))
    if t>3:ctext(d,(W//2,490),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
def d_fn(d,t,sc):
    ts=sc.ts;ax=Ax(60,175,560,350,(-0.5,4.5),(-2,4));ax.axes(d,range(0,5),range(-2,5),labels=True)
    f=lambda x:x*x-4*x+3
    grow(ax,d,f,TEAL,t,ts[3],3)
    if t>=ts[3]+3:
        ax.dot(d,1,0,GOLD);ax.dot(d,3,0,GOLD);ax.dot(d,2,-1,RED)
        ctext(d,(ax.px(2)+60,ax.py(-1)+4),"min (2, -1)",F(18),RED);ctext(d,(ax.px(1)-10,ax.py(0)-18),"1",F(18),GOLD);ctext(d,(ax.px(3)+10,ax.py(0)-18),"3",F(18),GOLD)
    if t>=ts[5]:
        rbox(d,(660,175,1250,345),(20,24,50),GRN,12,2)
        for j,(l,c) in enumerate([("x² - 4x + 3",WHITE),("= (x - 2)² - 1",GRN),("square ≥ 0  →  min = -1",GOLD)]):ctext(d,(690,210+j*45),l,F(24,True,True),c,"lm")
    if t>=ts[6]:
        for i,(a,b) in enumerate([("domain","allowed inputs"),("range","outputs"),("even","mirror y-axis"),("odd","flip origin")]):
            x=660+i*148;y=370;rbox(d,(x,y,x+140,y+58),(20,24,50),TEAL,10,2);ctext(d,(x+70,y+18),a,F(18),TEAL);ctext(d,(x+70,y+42),b,F(13,False),(190,200,230))
    if t>=ts[7]:
        cx,cy=900,475;d.ellipse((cx-50,cy-50,cx+50,cy+50),outline=RED,width=4);d.line([(cx+30,cy-70),(cx+30,cy+70)],fill=GOLD,width=2)
        ctext(d,(cx+200,cy),"x²+y²=1 : two y for one x",F(17),RED)
    banner(d,ts[7],t,"TWIST #1 — a circle is not a function",GOLD,115)
def d_lim(d,t,sc):
    ts=sc.ts
    ax=Ax(60,175,380,260,(-1,3),(0,4));ax.axes(d,range(0,4),range(0,5),labels=False)
    ax.curve(d,lambda x:x+1,TEAL,4);X,Y=ax.P(1,2);d.ellipse((X-8,Y-8,X+8,Y+8),fill=(10,14,36),outline=GOLD,width=3)
    ctext(d,(250,162),"(x²-1)/(x-1)",F(20),TEAL)
    if t>=ts[3]:
        a=(t-ts[3])*.35%1
        for s in(-1,1):ax.dot(d,1+s*(1-a)*1.2,2+s*(1-a)*1.2,RED if s<0 else GRN,6)
        ctext(d,(250,470),"limit = 2 (hole at 1)",F(20),GOLD)
    ax2=Ax(480,175,330,260,(-3,3),(-2,2));ax2.axes(d,(),(),labels=False)
    if t>=ts[5]:
        ax2.curve(d,lambda x:-1,RED,5,xr=(-3,-0.05));ax2.curve(d,lambda x:1,GRN,5,xr=(0.05,3))
        ctext(d,(645,162),"|x|/x",F(20),WHITE);ctext(d,(645,470),"left -1, right +1: no limit",F(18),RED)
    if t>=ts[6]:
        rbox(d,(850,175,1250,330),(20,24,50),GOLD,12,2)
        ctext(d,(870,215),"lim sin x / x  = 1",F(24,True,True),WHITE,"lm");ctext(d,(870,265),"(1+1/n)ⁿ → e ≈ 2.718",F(24,True,True),GOLD,"lm");ctext(d,(870,305),"x→0",F(14),(150,160,200),"lm")
    if t>=ts[7]:
        ax3=Ax(850,360,400,150,(0.02,1),(-1.3,1.3));
        ax3.curve(d,lambda x:math.sin(1/x),RED,2,n=900);d.line([(850,435),(1250,435)],fill=GRY,width=1);ctext(d,(1050,525),"sin(1/x) as x→0: wiggles forever",F(16),RED)
    banner(d,ts[7],t,"TWIST #2 — bounded, yet the limit does not exist",GOLD,115)
def d_cd(d,t,sc):
    ts=sc.ts;ax=Ax(60,175,380,250,(-2,2),(-0.5,2.5));ax.axes(d,(-1,0,1),(1,2),labels=False)
    ax.curve(d,abs,TEAL,5);ctext(d,(250,162),"|x| : continuous, not differentiable",F(18),TEAL)
    if t>=ts[4]:
        ax.curve(d,lambda x:-x,RED,2,xr=(-2,0));ax.curve(d,lambda x:x,GRN,2,xr=(0,2))
        ctext(d,(ax.px(-1.4),ax.py(1.9)),"slope -1",F(18),RED);ctext(d,(ax.px(1.4),ax.py(1.9)),"slope +1",F(18),GRN)
    ax2=Ax(520,175,340,250,(-0.3,2.3),(-0.5,5));ax2.axes(d,(1,2),(2,4),labels=False)
    if t>=ts[5]:
        ax2.curve(d,lambda x:x*x,PUR,5,xr=(0,2.2))
        ax2.curve(d,lambda x:2*x,GRY,3,xr=(0,2));d.line([ax2.P(0,0),ax2.P(2,4)],fill=GOLD,width=3)
        a=ease((t-ts[5])/2);ax2.dot(d,0,0,GOLD,6);ax2.dot(d,2,4,GOLD,6)
        ax2.curve(d,lambda x:2*(x-1)+1,GRN,3,xr=(0.3,1.7));ax2.dot(d,1,1,GRN)
        ctext(d,(690,162),"MVT: chord slope 2 = f'(1) = 2",F(18),GOLD)
    if t>=ts[6]:
        ax3=Ax(920,175,330,250,(0,3),(-0.5,3));ax3.axes(d,(),(),labels=False)
        f=lambda x:1+x*(3-x)*0.9*0+ (x*(3-x))/1.5*(1) ;ax3.curve(d,lambda x:x*(3-x)/1.5+0.3,TEAL,5)
        ax3.dot(d,1.5,1.5*1.5/1.5+0.3,GOLD);ctext(d,(1085,162),"Rolle: ends equal → slope 0",F(18),TEAL)
    if t>=ts[8]:
        rbox(d,(300,470,980,520),(20,24,50),GOLD,12,2);ctext(d,(640,495),"differentiable  IMPLIES  continuous      (not the reverse)",F(24,True,True),GOLD)
    banner(d,ts[8],t,"TWIST #3 — the corner of |x| breaks the converse",GOLD,115)
def d_tay(d,t,sc):
    ts=sc.ts;ax=Ax(60,175,560,330,(-3,3),(-1,8));ax.axes(d,range(-3,4),range(0,8,2),labels=False)
    ex=lambda x:math.exp(x)
    ax.curve(d,ex,WHITE,5)
    P=[lambda x:1,lambda x:1+x,lambda x:1+x+x*x/2,lambda x:1+x+x*x/2+x**3/6,lambda x:1+x+x*x/2+x**3/6+x**4/24]
    cols=[GRY,RED,GOLD,TEAL,GRN]
    if t>=ts[3]:
        k=int(min(4,(t-ts[3])/2.2))
        for i in range(k+1):ax.curve(d,P[i],cols[i],3,ylim=(-1,8))
        ctext(d,(340,165),f"e^x  vs  Taylor degree {k}",F(20),cols[k])
    if t>=ts[5]:
        rbox(d,(650,175,1250,325),(20,24,50),TEAL,12,2)
        for j,(n,v) in enumerate([("1","1"),("2","2"),("3","2.5"),("4","2.667"),("5","2.708"),("6","2.717")]):
            ctext(d,(670+(j%3)*195,205+(j//3)*50),f"{n} terms: {v}",F(18,True,True),GOLD if j<5 else GRN,"lm")
        ctext(d,(670,300),"e = 2.71828…",F(20,True,True),WHITE,"lm")
    if t>=ts[6]:
        rbox(d,(650,345,1250,480),(20,24,50),PUR,12,2)
        ctext(d,(670,372),"sin x ≈ x - x³/6",F(21,True,True),WHITE,"lm")
        ctext(d,(670,410),"x=0.5: 0.47917  vs  true 0.47943",F(19,True,True),PUR,"lm");ctext(d,(670,446),"error 0.00026 = x⁵/120",F(21,True,True),GOLD,"lm")
    banner(d,ts[7],t,"TWIST #4 — the first dropped term is the error",GOLD,115)
def d_opt(d,t,sc):
    ts=sc.ts;f=lambda x:x**3-6*x*x+9*x+1
    ax=Ax(60,175,520,330,(-0.3,4.3),(-1,7));ax.axes(d,range(0,5),range(0,8,2),labels=True)
    grow(ax,d,f,TEAL,t,ts[3],3)
    if t>=ts[4]:
        ax.dot(d,1,5,GOLD);ax.dot(d,3,1,RED);ctext(d,(ax.px(1)-10,ax.py(5)-22),"max 5",F(17),GOLD);ctext(d,(ax.px(3)+10,ax.py(1)+22),"min 1",F(17),RED)
        ctext(d,(330,162),"f = x³ - 6x² + 9x + 1  ,  f' = 3(x-1)(x-3)",F(17,True,True),WHITE)
    if t>=ts[6]:
        for x,y,c in((0,1,RED),(4,5,GOLD)):ax.dot(d,x,y,c,9)
        rbox(d,(620,175,1250,300),(20,24,50),GOLD,12,2)
        for j,l in enumerate(["f(0)=1  f(1)=5  f(3)=1  f(4)=5","global max 5 at x=1 and x=4","global min 1 at x=0 and x=3"]):ctext(d,(640,205+j*36),l,F(20,True,True),[WHITE,GOLD,RED][j],"lm")
    if t>=ts[7]:
        rbox(d,(620,320,1250,420),(20,24,50),GRN,12,2)
        ctext(d,(640,348),"box: V(x) = x(12-2x)²",F(20,True,True),WHITE,"lm");ctext(d,(640,385),"V' = (12-2x)(12-6x)=0 → x=2, V=128",F(20,True,True),GRN,"lm")
    if t>=ts[9]:
        rbox(d,(620,440,1250,510),(20,24,50),PUR,12,2)
        ctext(d,(640,462),"Newton √2:  x → (x + 2/x)/2",F(19,True,True),WHITE,"lm");ctext(d,(640,494),"1 → 1.5 → 1.41667 → 1.41422",F(19,True,True),PUR,"lm")
    banner(d,ts[10],t,"TWIST #5 — max and min each happen twice: compare the ends!",GOLD,115)
def d_py(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(2,codes.C1),(5,codes.C4)],30,150,680,17,22)
    if k==0:
        ax=Ax(720,190,500,300,(0.8,2.1),(-0.5,3));ax.axes(d,(1,1.5,2),(0,1,2),labels=True);ax.curve(d,lambda x:x*x-2,TEAL,4)
        x=1.0;n=int(clamp((t-ts[2]-1)/4)*3)
        for i in range(n):
            y=x*x-2;nx=x-y/(2*x);d.line([ax.P(x,0),ax.P(x,y)],fill=GRY,width=2);d.line([ax.P(x,y),ax.P(nx,0)],fill=GOLD,width=3);ax.dot(d,nx,0,GOLD,6);x=nx
        ctext(d,(970,165),"Newton: tangent → zero → repeat",F(20),GOLD)
    if k==1:
        f=lambda x:x**3-6*x*x+9*x+1;ax=Ax(720,190,500,300,(1.8,3.6),(0.5,3));ax.axes(d,(2,3),(1,2),labels=True);ax.curve(d,f,TEAL,4)
        x=2.5;path=[x]
        for _ in range(60):x-=0.05*(3*x*x-12*x+9);path.append(x)
        n=int(clamp((t-ts[5])/6)*60)
        for j in range(0,n,3):ax.dot(d,path[j],f(path[j]),GOLD,5)
        ctext(d,(970,165),"gradient descent walks downhill",F(20),GOLD)
    banner(d,ts[7],t,"PYTHON TWIST — learning rate too big = blow-up",GOLD,115)
def d_dsa(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(2,codes.C2),(6,codes.C3)],30,150,680,17,22)
    if k==0:
        ctext(d,(970,175),"each step halves the interval",F(20),TEAL)
        lo,hi=1.0,2.0;n=int(clamp((t-ts[2]-1)/5)*9)
        for i in range(10):
            y=215+i*30
            if i<=n:
                x0=720+(lo-1)*500;x1=720+(hi-1)*500;d.rectangle((x0,y,x1,y+18),fill=[TEAL,GRN,PUR,GOLD][i%4]);ctext(d,(1235,y+9),f"{i}",F(14),GRY,"rm")
            mid=(lo+hi)/2
            if mid*mid-2<0:lo=mid
            else:hi=mid
        d.line([(720+(2**.5-1)*500,205),(720+(2**.5-1)*500,520)],fill=RED,width=2);ctext(d,(720+(2**.5-1)*500,535),"√2",F(18),RED)
    if k==1:
        f=lambda x:(x-2)**2-1;ax=Ax(720,190,500,300,(0,5),(-1.5,5));ax.axes(d,range(0,6),(0,2,4),labels=True);ax.curve(d,f,TEAL,4)
        lo,hi=0.0,5.0
        for i in range(int(clamp((t-ts[6])/5)*6)):
            a=lo+(hi-lo)/3;b=hi-(hi-lo)/3
            d.line([ax.P(lo,-1.3-i*0.0),ax.P(hi,-1.3)],fill=[GOLD,GRN,PUR,RED,TEAL,WHITE][i%6],width=3)
            if f(a)<f(b):hi=b
            else:lo=a
        ctext(d,(970,165),"ternary search: one valley",F(20),GOLD)
    banner(d,ts[7],t,"DSA TWIST — 20 halvings ≈ 1 part in a million",GOLD,115)
def d_wk(d,t,sc):
    walk(d,sc,t,[(codes.W_C1,1,5),(codes.W_C2,6,9)])
def d_end(d,t,sc):
    ctext(d,(W//2,230),"The Hill of Change — climbed",F(52),GOLD)
    for i,x in enumerate(["functions","limits","continuity","Taylor series","optimization"]):
        if t>1+i*.5:
            cx=210+i*215;cy=330;rbox(d,(cx-100,cy-24,cx+100,cy+24),(20,24,50),[TEAL,GRN,PUR,GOLD,RED][i],10,2);ctext(d,(cx,cy),x,F(15),[TEAL,GRN,PUR,GOLD,RED][i])
    if t>6:ctext(d,(W//2,450),"next film: Probability & Statistics",F(30),WHITE)
SCENES=[("title",d_title,""),("fn",d_fn,"Hill 1 · Functions"),("lim",d_lim,"Hill 2 · Limits"),("cd",d_cd,"Hill 3 · Continuity and differentiability"),("tay",d_tay,"Hill 4 · Taylor series"),("opt",d_opt,"Hill 5 · Optimization"),("wk",d_wk,"Walkthrough · how the code thinks"),("py",d_py,"Lab 1 · Python for calculus"),("dsa",d_dsa,"Lab 2 · Complexity (DSA)"),("end",d_end,"")]
