import sys
sys.path.insert(0,'/home/claude/films');sys.path.insert(0,'/home/claude/films/L')
from gcommon import *
from codes_L import *
def hbars(d,x,y,items,maxv,w=300,col=TEAL,fs=16,gap=34,lw=130,fmt="{:g}"):
    for i,(l,v) in enumerate(items):
        yy=y+i*gap;c=col[i%len(col)] if isinstance(col,list) else col
        ctext(d,(x,yy+12),l,F(fs,True),WHITE,"lm");bw=max(3,int(w*v/maxv))
        rbox(d,(x+lw,yy,x+lw+bw,yy+24),c,None,4);ctext(d,(x+lw+bw+8,yy+12),fmt.format(v),F(fs-1,True),GOLD,"lm")
def vbars(d,x,y,h,items,maxv,bw=60,gap=26,col=TEAL,fs=16,fmt="{:g}"):
    for i,(l,v) in enumerate(items):
        c=col[i%len(col)] if isinstance(col,list) else col;bh=max(3,int(h*v/maxv));xx=x+i*(bw+gap)
        rbox(d,(xx,y+h-bh,xx+bw,y+h),c,None,5);ctext(d,(xx+bw//2,y+h-bh-14),fmt.format(v),F(fs-1,True),GOLD)
        ctext(d,(xx+bw//2,y+h+16),l,F(fs-1,True),WHITE)
def cell(d,x,y,w,h,txt,col=TEAL,fill=(20,24,50),fs=16,tc=None):
    d.rectangle((x,y,x+w,y+h),fill=fill,outline=col,width=2);ctext(d,(x+w//2,y+h//2),txt,F(fs,True),tc or col)
def lab(d,x,y,txt,col=WHITE,fs=16,a="mm"):ctext(d,(x,y),txt,F(fs,True),col,a)
def node(d,x,y,txt,col=TEAL,r=17,fs=15,fill=(20,24,50),w=3):
    d.ellipse((x-r,y-r,x+r,y+r),fill=fill,outline=col,width=w);ctext(d,(x,y),txt,F(fs,True),col)
def edge(d,p,q,col=GRY,w=3,label=None,lc=WHITE):
    d.line([p,q],fill=col,width=w)
    if label is not None:ctext(d,((p[0]+q[0])//2,(p[1]+q[1])//2-12),str(label),F(15,True),lc)
def cards(d,t,ts,items,x=770,y=190,w=470,h=44,gap=10,fs=17):
    for i,(li,l,v,c) in enumerate(items):
        if t>=ts[li]:
            yy=y+i*(h+gap);rbox(d,(x,yy,x+w,yy+h),(20,24,50),c,10,2)
            ctext(d,(x+14,yy+h//2),l,F(fs-2,True),WHITE,"lm");ctext(d,(x+w-14,yy+h//2),v,F(fs,True),c,"rm")
