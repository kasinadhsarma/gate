from viz import *
def bx(d,x,y,w,h,col,txt,fs=18):
    rbox(d,(x,y,x+w,y+h),(20,24,50),col,10,2);ctext(d,(x+w//2,y+h//2),txt,F(fs,True),col)
def mk_title(name,sub):
    def d_title(d,t,sc):
        for i in range(14):
            x=90+i*85;y=(t*70+i*97)%820-60;rbox(d,(x,y,x+30,y+44),tuple(int(c*0.55) for c in [GOLD,TEAL,PUR,RED][i%4]),None,4)
        ctext(d,(W//2,240),"OPERATION  GATE",F(84),GOLD);ctext(d,(W//2,340),name,F(46))
        if t>1.6:ctext(d,(W//2,420),sub,F(26,False),(170,180,215))
        if t>3:ctext(d,(W//2,490),"GATE DA 2027  ·  Ramu & Somu",F(24),TEAL)
    return d_title
def mk_end(head,chips,foot):
    def d_end(d,t,sc):
        ctext(d,(W//2,230),head,F(50),GOLD)
        for i,x in enumerate(chips):
            if t>1+i*.4:
                cx=210+(i%4)*270;cy=320+(i//4)*60;c=[TEAL,GRN,PUR,GOLD][i%4];rbox(d,(cx-125,cy-22,cx+125,cy+22),(20,24,50),c,10,2);ctext(d,(cx,cy),x,F(17),c)
        if t>6:ctext(d,(W//2,470),foot,F(28),WHITE)
    return d_end
def tw(d,sc,t,i,txt):banner(d,sc.ts[i],t,txt,GOLD,115)
