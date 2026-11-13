from viz import *
import codes, random
def card(d,box,col,lines,fs=19,gap=34,mono=True):
    rbox(d,box,(20,24,50),col,12,2)
    for j,(l,c) in enumerate(lines):ctext(d,(box[0]+18,box[1]+26+j*gap),l,F(fs,True,mono),c,"lm")
def d_title(d,t,sc):
    for i in range(14):
        x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
    ctext(d,(W//2,240),"OPERATION  GATE",F(84),GOLD);ctext(d,(W//2,340),"The Learning Machine",F(50))
    if t>1.6:ctext(d,(W//2,420),"Machine Learning · seven rooms · seven twists",F(26,False),(170,180,215))
    if t>3:ctext(d,(W//2,490),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
XS=[1,2,3,4,5];YS=[2.1,3.9,6.2,7.8,10.1]
def d_reg(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.M1),(6,codes.M2)],30,150,690,17,22)
    ax=Ax(760,190,470,300,(0,6),(0,12));ax.axes(d,range(0,7),(0,4,8,12),labels=True)
    if t>=ts[3]:
        for x,y in zip(XS,YS):ax.dot(d,x,y,GOLD,6)
        w,b=1.99,0.05
        if k==1:
            a=ease((t-ts[6])/4);w,b=1.99*a,0.05*a
        ax.curve(d,lambda x:w*x+b,TEAL,4)
        if k==0 and t>=ts[3]+3:
            for x,y in zip(XS,YS):d.line([ax.P(x,y),ax.P(x,1.99*x+.05)],fill=RED,width=2)
        ctext(d,(995,170),"y = 1.99x + 0.05    R² = 0.9973",F(18,True,True),TEAL)
    if t>=ts[7]:card(d,(770,505,1240,555),PUR,[("ridge: Σw²   lasso: Σ|w| → zeros",WHITE)],16)
    banner(d,ts[8],t,"TWIST #1 — more features always raise training R², even noise",GOLD,115)
def d_cls(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(4,codes.M3)],30,150,690,17,22)
    if t>=ts[2]:
        ax=Ax(770,180,300,180,(-6,6),(0,1.05));ax.axes(d,(-4,0,4),(0,.5,1),labels=True);ax.curve(d,lambda z:1/(1+math.exp(-z)),TEAL,4);ctext(d,(920,165),"sigmoid(z) = 1/(1+e⁻ᶻ)",F(16),TEAL)
    if t>=ts[4]:
        for (i,j,v,c) in((0,0,"TP 40",GRN),(0,1,"FN 20",RED),(1,0,"FP 10",RED),(1,1,"TN 930",GRN)):
            x=1100+j*70-35;y=215+i*60;rbox(d,(x,y,x+66,y+52),(20,24,50),c,6,2);ctext(d,(x+33,y+26),v,F(14,True),c)
        ctext(d,(1135,190),"pred +   pred −",F(12),(170,180,215))
    if t>=ts[6]:
        for i,(a,v,c) in enumerate([("accuracy",.97,TEAL),("precision",.8,GOLD),("recall",.667,PUR),("F1",.727,GRN)]):
            y=400+i*36;d.rectangle((900,y,900+int(330*v),y+26),fill=c);ctext(d,(890,y+13),a,F(16),WHITE,"rm");ctext(d,(900+int(330*v)+6,y+13),f"{v}",F(15),WHITE,"lm")
    banner(d,ts[7],t,"TWIST #2 — 'always say no' scores 0.94 accuracy",GOLD,115)
def d_tree(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(4,codes.M4)],30,150,690,17,22)
    if t>=ts[2]:
        ax=Ax(770,190,220,150,(0,1),(0,1.05));ax.axes(d,(0,.5,1),(0,1),labels=True);ax.curve(d,lambda p:-(p*math.log2(p)+(1-p)*math.log2(1-p)) if 0<p<1 else 0,TEAL,4,n=100);ctext(d,(880,172),"entropy H(p)",F(16),TEAL)
    if t>=ts[3]:
        rbox(d,(1020,190,1230,240),(20,24,50),GOLD,8,2);ctext(d,(1125,208),"Outlook",F(18),GOLD);ctext(d,(1125,228),"9 yes · 5 no",F(13,False),WHITE)
        for i,(nm,c,col) in enumerate([("Sunny","2 y / 3 n",RED),("Overcast","4 y / 0 n",GRN),("Rain","3 y / 2 n",RED)]):
            x=770+i*155;d.line([(1125,240),(x+65,300)],fill=GRY,width=2);rbox(d,(x,300,x+130,350),(20,24,50),col,8,2);ctext(d,(x+65,318),nm,F(16),col);ctext(d,(x+65,338),c,F(13,False),WHITE)
    if t>=ts[4]:card(d,(770,380,1240,470),GRN,[("H(parent) = 0.940",WHITE),("weighted H(children) = 0.694",WHITE),("gain = 0.247",GOLD)],17,28)
    banner(d,ts[7],t,"TWIST #3 — info gain loves ID columns; gain ratio fixes it",GOLD,115)
def d_svm(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.M5)],30,150,690,17,22)
    ax=Ax(770,180,300,300,(-2,4.5),(-2,4.5));ax.axes(d,(0,2,4),(0,2,4),labels=False)
    if t>=ts[2]:
        ax.curve(d,lambda x:2-x,GOLD,4);ax.curve(d,lambda x:4-x,(120,100,40),2);ax.curve(d,lambda x:-x,(120,100,40),2)
        for p,c in(((2,2),GRN),((3,3),GRN),((0,0),RED),((-1,-1),RED)):ax.dot(d,p[0],p[1],c,7)
    if t>=ts[5]:
        for p in((2,2),(0,0)):X,Y=ax.P(*p);d.ellipse((X-15,Y-15,X+15,Y+15),outline=WHITE,width=3)
        ctext(d,(920,168),"margin 2.828 · support vectors circled",F(15),WHITE)
    if t>=ts[6]:
        ax2=Ax(1100,230,140,150,(-4,4),(0,16));ax2.curve(d,lambda x:x*x,PUR,3);ax2.axes(d,(),(),grid=False,labels=False)
        d.line([ax2.P(-4,4),ax2.P(4,4)],fill=GOLD,width=2)
        for x in(-3,-1,0,1,3):ax2.dot(d,x,x*x,GRN if abs(x)>2 else RED,5)
        ctext(d,(1170,205),"add x²",F(15),PUR)
    banner(d,ts[7],t,"TWIST #4 — delete non-support vectors: the line never moves",GOLD,115)
def d_nn(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(5,codes.M6)],30,150,690,15,19)
    if t>=ts[3]:
        L=[(790,[250,360]),(940,[200,280,360,440]),(1090,[320])]
        for (x,ys) in L:
            for y in ys:d.ellipse((x-16,y-16,x+16,y+16),outline=TEAL,width=3)
        for a in L[0][1]:
            for b in L[1][1]:d.line([(790+16,a),(940-16,b)],fill=(60,70,120),width=1)
        for b in L[1][1]:d.line([(940+16,b),(1090-16,320)],fill=(60,70,120),width=1)
        for x,l in((790,"inputs"),(940,"4 hidden"),(1090,"output")):ctext(d,(x,490),l,F(15),WHITE)
    if t>=ts[4]:
        ax=Ax(1130,190,110,110,(-0.3,1.3),(-0.3,1.3))
        for (x,y),c in(((0,0),RED),((1,1),RED),((0,1),GRN),((1,0),GRN)):ax.dot(d,x,y,c,7)
        ctext(d,(1185,172),"XOR",F(15),GOLD)
    banner(d,ts[8],t,"TWIST #5 — without activations, deep = one line",GOLD,115)
def d_ev(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(4,codes.M7)],30,150,690,17,22)
    if t>=ts[3]:
        ax=Ax(770,190,460,230,(0,10),(0,10));ax.axes(d,(),(),labels=False)
        ax.curve(d,lambda x:9*math.exp(-x/2.2)+0.3,TEAL,4);ax.curve(d,lambda x:9*math.exp(-x/2.2)+0.5+0.09*(x**2)/1.3,RED,4)
        ctext(d,(1000,172),"error vs model complexity",F(17),WHITE);ctext(d,(850,440),"high bias",F(16),GOLD);ctext(d,(1160,440),"high variance",F(16),GOLD)
        ctext(d,(900,300),"training",F(15),TEAL);ctext(d,(1140,230),"validation",F(15),RED)
    if t>=ts[6]:
        for i in range(4):
            for j in range(4):d.rectangle((790+j*55,470+i*0,840+j*55,490),fill=RED if j==i%4 and False else (70,80,130))
        d.rectangle((790+55*3,470,840+55*3,490),fill=RED);ctext(d,(1000,510),"k-fold: each part is the test set once",F(15),WHITE)
    banner(d,ts[7],t,"TWIST #6 — pick the smallest validation error, not training",GOLD,115)
def d_un(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.M8),(6,codes.M8B)],30,150,690,16,21)
    if k==0:
        ax=Ax(780,190,440,300,(0,6),(0,8));ax.axes(d,(),(),labels=False)
        pts=[(1,1),(1.5,2),(3,4),(5,7),(3.5,5),(4.5,5),(3.5,4.5)]
        for i,p in enumerate(pts):ax.dot(d,p[0],p[1],TEAL if i<2 else GOLD,6)
        ax.dot(d,1.25,1.5,WHITE,10);ax.dot(d,3.9,5.1,WHITE,10);ctext(d,(1000,172),"two clusters, centres ○",F(16),WHITE)
    if k==1:
        xs=[2.5,.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1];ys=[2.4,.7,2.9,2.2,3.0,2.7,1.6,1.1,1.6,.9]
        ax=Ax(780,190,440,300,(-0.5,4),(-0.5,4));ax.axes(d,(),(),labels=False)
        for x,y in zip(xs,ys):ax.dot(d,x,y,TEAL,6)
        ax.curve(d,lambda x:0.0+0.84*x+0.1 if False else 0.9*(x-1.81)+1.91,GOLD,3);ctext(d,(1000,172),"PC1 keeps 96.3% of the variance",F(16),GOLD)
    banner(d,ts[7],t,"TWIST #7 — K-means needs good starts; PCA = SVD of centred data",GOLD,115)
def d_dsa(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.M9)],30,150,690,17,22)
    if t>=ts[2]:
        a=ease((t-ts[3])/2)
        for i,(l,v,c) in enumerate([("KNN query: n = 10 000",10000,TEAL),("k-means round: nkd = 60 000",60000,GOLD),("tree split: n log n = 132 900",132900,PUR)]):
            y=200+i*80;d.rectangle((770,y,770+int(450*v/132900*a)+3,y+36),fill=c);ctext(d,(780,y+60),l,F(17),WHITE,"lm")
    banner(d,ts[7],t,"DSA TWIST — a size-k heap turns n log n into n log k",GOLD,115)
def d_wk(d,t,sc):walk(d,sc,t,[(codes.WM1,1,5),(codes.WM2,6,9)])
def d_end(d,t,sc):
    ctext(d,(W//2,230),"The Learning Machine — trained",F(52),GOLD)
    for i,x in enumerate(["regression","classification","trees","SVM","neural nets","evaluation","clustering & PCA"]):
        if t>1+i*.4:
            cx=210+(i%4)*270;cy=320+(i//4)*60;rbox(d,(cx-110,cy-22,cx+110,cy+22),(20,24,50),[TEAL,GRN,PUR,GOLD][i%4],10,2);ctext(d,(cx,cy),x,F(18),[TEAL,GRN,PUR,GOLD][i%4])
    if t>6:ctext(d,(W//2,470),"next film: Artificial Intelligence",F(30),WHITE)
SCENES=[("title",d_title,""),("reg",d_reg,"Room 1 · Regression"),("cls",d_cls,"Room 2 · Classification"),("tree",d_tree,"Room 3 · Decision trees"),("svm",d_svm,"Room 4 · Support vector machines"),("nn",d_nn,"Room 5 · Neural networks"),("ev",d_ev,"Room 6 · Model evaluation"),("un",d_un,"Room 7 · Clustering and PCA"),("dsa",d_dsa,"Lab · Complexity of learning (DSA)"),("wk",d_wk,"Walkthrough · how the code thinks"),("end",d_end,"")]
