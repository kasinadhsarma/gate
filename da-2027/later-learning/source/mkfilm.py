import os,textwrap
def make(dirn,title,sub,intro,rooms,wk,end_head,chips,nxt,wkcode,wkchap,endlines):
    os.makedirs(dirn,exist_ok=True)
    open(f"{dirn}/codes.py","w").write("from lhelp import *\n")
    S={"title":intro}
    for r in rooms:S[r["key"]]=r["lines"]
    S["wk"]=wk;S["end"]=endlines
    s='N,R,S="N","R","S"\nSCENES={\n'
    for k,v in S.items():
        s+=f'"{k}":[\n'+",\n".join(f"({sp},{tx!r})" for sp,tx in v)+"],\n"
    s+="}\n"
    open(f"{dirn}/script.py","w").write(s)
    c="from lhelp import *\nimport codes,math\n"
    for r in rooms:
        blocks=",".join(f"({i},{n})" for i,n in r["codes"])
        body=textwrap.indent(textwrap.dedent(r["vis"]).strip("\n"),"    ")
        c+=f"def d_{r['key']}(d,t,sc):\n    ts=sc.ts;panel2(d,sc,t,[{blocks}],30,150,690,{r.get('fs',15)},{r.get('lh',20)})\n{body}\n    tw(d,sc,t,{len(r['lines'])-1},{('TWIST #'+str(rooms.index(r)+1)+' — '+r['tw'])!r})\n"
    c+=f"def d_wk(d,t,sc):walk(d,sc,t,[({wkcode},1,2)])\n"
    sc=[f'("title",mk_title({title!r},{sub!r}),"")']
    for i,r in enumerate(rooms):sc.append(f'("{r["key"]}",d_{r["key"]},{r["chap"]!r})')
    sc.append(f'("wk",d_wk,{wkchap!r})')
    sc.append(f'("end",mk_end({end_head!r},{chips!r},{nxt!r}),"")')
    c+="SCENES=["+",".join(sc)+"]\n"
    open(f"{dirn}/scenes.py","w").write(c)
