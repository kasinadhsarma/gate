import math, numpy as np
from film import *
class Ax:
    def __init__(s,x0,y0,w,h,xr,yr):s.x0,s.y0,s.w,s.h,s.xr,s.yr=x0,y0,w,h,xr,yr
    def px(s,x):return s.x0+(x-s.xr[0])/(s.xr[1]-s.xr[0])*s.w
    def py(s,y):return s.y0+s.h-(y-s.yr[0])/(s.yr[1]-s.yr[0])*s.h
    def P(s,x,y):return (s.px(x),s.py(y))
    def axes(s,d,xt=(),yt=(),col=(110,120,160),grid=True,labels=True):
        if s.xr[0]<=0<=s.xr[1]:d.line([(s.px(0),s.y0),(s.px(0),s.y0+s.h)],fill=col,width=2)
        if s.yr[0]<=0<=s.yr[1]:d.line([(s.x0,s.py(0)),(s.x0+s.w,s.py(0))],fill=col,width=2)
        for v in xt:
            if grid:d.line([(s.px(v),s.y0),(s.px(v),s.y0+s.h)],fill=(40,46,80),width=1)
            if labels:ctext(d,(s.px(v),s.py(0 if s.yr[0]<=0<=s.yr[1] else s.yr[0])+14),f"{v:g}",F(13),(150,160,200))
        for v in yt:
            if grid:d.line([(s.x0,s.py(v)),(s.x0+s.w,s.py(v))],fill=(40,46,80),width=1)
            if labels:ctext(d,(s.px(0 if s.xr[0]<=0<=s.xr[1] else s.xr[0])-14,s.py(v)),f"{v:g}",F(13),(150,160,200))
    def curve(s,d,f,col,wd=4,xr=None,n=240,ylim=None):
        a,b=xr or s.xr;pts=[]
        for i in range(n+1):
            x=a+(b-a)*i/n
            try:y=f(x)
            except Exception:continue
            if y!=y:continue
            lo,hi=ylim or (s.yr[0]-0.0*(s.yr[1]-s.yr[0]),s.yr[1])
            if y<lo or y>hi:
                if len(pts)>1:d.line(pts,fill=col,width=wd)
                pts=[];continue
            pts.append(s.P(x,y))
        if len(pts)>1:d.line(pts,fill=col,width=wd)
    def dot(s,d,x,y,col,r=7):
        X,Y=s.P(x,y);d.ellipse((X-r,Y-r,X+r,Y+r),fill=col,outline=WHITE,width=2)
def arrow(d,p,q,col,w=4,head=14):
    d.line([p,q],fill=col,width=w);a=math.atan2(q[1]-p[1],q[0]-p[0])
    d.polygon([q,(q[0]-head*math.cos(a-0.4),q[1]-head*math.sin(a-0.4)),(q[0]-head*math.cos(a+0.4),q[1]-head*math.sin(a+0.4))],fill=col)
def mat(d,x,y,M,cw=62,ch=40,col=WHITE,fs=24,cols=None):
    r,c=len(M),len(M[0]);w=c*cw;h=r*ch
    d.line([(x+6,y),(x,y),(x,y+h),(x+6,y+h)],fill=(190,200,230),width=3)
    d.line([(x+w-6,y),(x+w,y),(x+w,y+h),(x+w-6,y+h)],fill=(190,200,230),width=3)
    for i in range(r):
        for j in range(c):
            v=M[i][j];t=(f"{v:g}" if not isinstance(v,str) else v)
            ctext(d,(x+j*cw+cw/2,y+i*ch+ch/2),t,F(fs,True,True),(cols[i][j] if cols else col))
    return w
import sys
sys.path.insert(0,"/home/claude/film")
import pyviz
def _fit(d,lines,w,fs,lh):
    while fs>11 and (len(lines)*lh>330 or max(len(l) for l in lines)*F(fs,False,True).getlength("M")>w-26):
        fs-=1;lh=max(16,min(lh,fs+6))
    return fs,lh
def panel2(d,sc,t,blocks,x=30,y=150,w=650,fs=15,lh=20):
    k=None
    for i,(li,code) in enumerate(blocks):
        if t>=sc.ts[li]:k=i
    if k is None:return None
    li,code=blocks[k];lines=code.strip("\n").split("\n")
    fs,lh=_fit(d,lines,w,fs,lh);h=len(lines)*lh+16
    rbox(d,(x,y,x+w,y+h),(16,20,44),(90,100,150),10,2)
    for j,l in enumerate(lines):pyviz.code_line(d,x+12,y+8+j*lh,l,F(fs,False,True))
    out=pyviz.runcode(code)
    if t>=sc.ts[li]+1.6:
        oy=y+h+8;oh=len(out)*lh+12
        rbox(d,(x,oy,x+w,oy+oh),(40,36,14),(200,150,60),8,2)
        for j,l in enumerate(out):d.text((x+12,oy+6+j*lh),(l if len(l)<70 else l[:68]+"…"),font=F(fs,True,True),fill=(255,225,140))
    return k
import io as _io
class _Stop(Exception):pass
def trace(code,maxsteps=500):
    code=code.strip("\n");steps=[];buf=_io.StringIO();g={"__name__":"walk"}
    def fmt(v):
        if isinstance(v,float):return f"{v:.5g}"
        if isinstance(v,(list,tuple)):return "["+", ".join(fmt(q) for q in v)+"]"
        return repr(v)
    def tr(frame,event,arg):
        if frame.f_code.co_filename!="<walk>":return None
        if event=="line":
            loc={k:fmt(v) for k,v in frame.f_locals.items() if not k.startswith("__") and not callable(v)}
            steps.append((frame.f_lineno,loc,buf.getvalue()))
            if len(steps)>=maxsteps:raise _Stop()
        return tr
    import contextlib
    with contextlib.redirect_stdout(buf):
        sys.settrace(tr)
        try:exec(compile(code,"<walk>","exec"),g)
        except _Stop:pass
        finally:sys.settrace(None)
    steps.append((0,steps[-1][1] if steps else {},buf.getvalue()))
    return steps
_TC={}
def walk(d,sc,t,segs,x=24,y=150,w=770,fs=18,lh=24):
    """segs: list of (code, first_line_idx, last_line_idx). Shows traced execution advancing over the narration of those lines."""
    cur=None
    for si,(code,a,b) in enumerate(segs):
        if t>=sc.ts[a]:cur=si
    if cur is None:return
    code,a,b=segs[cur];t0=sc.ts[a];t1=sc.ts[b]+sc.L[b][3]
    if code not in _TC:_TC[code]=trace(code)
    st=_TC[code];p=clamp((t-t0)/(t1-t0));k=min(len(st)-1,int(ease(p)*len(st)))
    ln,loc,out=st[k];lines=code.strip("\n").split("\n");fs,lh=_fit(d,lines,w,fs,lh);h=len(lines)*lh+16
    rbox(d,(x,y,x+w,y+h),(16,20,44),(90,100,150),10,2)
    if ln>0:d.rectangle((x+4,y+8+(ln-1)*lh-1,x+w-4,y+8+ln*lh-1),fill=(70,60,20))
    for j,l in enumerate(lines):pyviz.code_line(d,x+12,y+8+j*lh,l,F(fs,False,True))
    if ln>0:ctext(d,(x+w-8,y+8+(ln-1)*lh+lh/2),"◀ running",F(14),GOLD,"rm")
    prev=st[k-1][1] if k>0 else {}
    vx=x+w+16;rbox(d,(vx,y,1250,y+34+max(1,len(loc))*30),(20,24,50),TEAL,10,2);ctext(d,(vx+14,y+17),"variables",F(16),TEAL,"lm")
    for j,(n,v) in enumerate(loc.items()):
        ch=prev.get(n)!=v;ctext(d,(vx+14,y+48+j*30),f"{n} = {v}",F(18,True,True),GOLD if ch else WHITE,"lm")
    oy=y+h+10;ol=[q for q in out.rstrip("\n").split("\n") if q][-3:]
    rbox(d,(x,oy,x+w,oy+len(ol)*lh+14 if ol else oy+lh+14),(40,36,14),(200,150,60),8,2)
    ctext(d,(x+10,oy+12),"output" if not ol else "",F(14),(200,150,60),"lm")
    for j,l in enumerate(ol):d.text((x+12,oy+7+j*lh),l[:60],font=F(fs,True,True),fill=(255,225,140))
