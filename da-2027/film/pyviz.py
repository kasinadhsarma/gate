import io, re, contextlib
from film import *
KW={"def","return","for","in","if","else","elif","while","break","continue","class","try","except","finally","as","lambda","yield","nonlocal","import","None","True","False","not","and","or","is","print"}
def runcode(code):
    buf=io.StringIO()
    g={}
    with contextlib.redirect_stdout(buf):
        try:exec(code,g)
        except Exception as e:print(f"{type(e).__name__}: {e}")
    return buf.getvalue().rstrip("\n").split("\n")
TOK=re.compile(r"(#.*$)|(\"[^\"]*\"|'[^']*')|(\b\d+\.?\d*\b)|([A-Za-z_]+)")
def code_line(d,x,y,line,font):
    pos=0;cx=x;cw=d.textlength("M",font=font)
    for m in TOK.finditer(line):
        if m.start()>pos:
            seg=line[pos:m.start()];d.text((cx,y),seg,font=font,fill=(210,220,250));cx+=cw*len(seg)
        tx=m.group(0)
        col=(120,200,120) if m.group(1) else (240,140,120) if m.group(2) else (255,205,90) if m.group(3) else ((110,170,255) if tx in KW else (210,220,250))
        d.text((cx,y),tx,font=font,fill=col);cx+=cw*len(tx);pos=m.end()
    if pos<len(line):d.text((cx,y),line[pos:],font=font,fill=(210,220,250))
def panel(d,sc,t,blocks,x=40,y=165,w=620):
    """blocks: list of (line_idx, code) ; shows the latest started block + its real output"""
    k=None
    for i,(li,code) in enumerate(blocks):
        if t>=sc.ts[li]:k=i
    if k is None:return None
    li,code=blocks[k];lines=code.strip("\n").split("\n");f=F(19,True,True)
    h=len(lines)*25+18
    rbox(d,(x,y,x+w,y+h),(16,20,44),(90,100,150),10,2)
    for j,l in enumerate(lines):code_line(d,x+14,y+9+j*25,l,F(19,False,True))
    out=runcode(code)
    if t>=sc.ts[li]+1.6:
        oy=y+h+10;oh=len(out)*25+14
        rbox(d,(x,oy,x+w,oy+oh),(40,36,14),(200,150,60),8,2)
        for j,l in enumerate(out):
            d.text((x+14,oy+7+j*25),(l if len(l)<58 else l[:56]+"…"),font=F(18 if len(l)<48 else 15,True,True),fill=(255,225,140))
    return k
