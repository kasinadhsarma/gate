import sys,os,re,io,contextlib,importlib,runpy,random
sys.path.insert(0,"/home/claude/films/L");sys.path.insert(0,"/home/claude/films")
import codes_L
def esc(s):
    for a,b in [("\\","\\textbackslash{}"),("&","\\&"),("%","\\%"),("$","\\$"),("#","\\#"),("_","\\_"),("{","\\{"),("}","\\}"),("~","\\textasciitilde{}"),("^","\\textasciicircum{}")]:s=s.replace(a,b)
    return s
def run(code):
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code,{"__name__":"__main__"})
    return buf.getvalue().rstrip()
out=[]
def film_meta(i):
    d=f"/home/claude/films/L/l{i}"
    sc=open(d+"/scenes.py").read()
    m=re.search(r"mk_title\((['\"])(.*?)\1,\s*(['\"])(.*?)\3\)",sc)
    title,sub=m.group(2),m.group(4)
    rooms=re.findall(r'\("(\w+)",d_\w+,(".*?"|\'.*?\')\)',sc)
    # map room key -> code names
    s2=sc.split("\ndef ")
    codes={}
    for blk in s2:
        mm=re.match(r"d_(\w+)\(",blk)
        if mm:codes[mm.group(1)]=re.findall(r"\b(L\d+[A-Z]\d*)\b",blk.split("\n")[1] if "\n" in blk else "")
    ns={};exec(open(d+"/script.py").read(),ns)
    return title,sub,codes,ns["SCENES"],sc
def chap_of(sc,key):
    m=re.search(r'\("%s",d_\w+,(?:"([^"]*)"|\'([^\']*)\')\)'%key,sc)
    return (m.group(1) or m.group(2)) if m else key
parts={"Part I - The first Later Learning topics (films 1-13)":range(1,14),"Part II - Advanced data structures and algorithms (films 14-19)":range(14,20),"Part III - Advanced machine learning (films 20-26)":range(20,27),"Part IV - Advanced linear algebra (films 27-29)":range(27,30),"Part V - Advanced probability, statistics and calculus (films 30-33)":range(30,34),"Part VI - LeetCode patterns (films 34-37)":range(34,38)}
T=r"""\documentclass[11pt,a4paper]{report}
\usepackage[margin=1.9cm]{geometry}
\usepackage{fontspec}
\setmainfont{DejaVu Sans}[Scale=0.92]
\setmonofont{DejaVu Sans Mono}[Scale=0.80]
\usepackage{fancyvrb,fvextra}
\usepackage[dvipsnames]{xcolor}
\usepackage{tcolorbox}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=NavyBlue}
\usepackage{titlesec}
\titleformat{\chapter}[display]{\bfseries\Large\color{NavyBlue}}{Film \thechapter}{4pt}{}
\titlespacing*{\chapter}{0pt}{-10pt}{14pt}
\setlength{\parindent}{0pt}\setlength{\parskip}{5pt}
\DefineVerbatimEnvironment{Code}{Verbatim}{fontsize=\scriptsize,frame=single,framerule=0.3pt,rulecolor=\color{gray},breaklines=true,breaksymbolleft={}}
\DefineVerbatimEnvironment{Out}{Verbatim}{fontsize=\scriptsize,frame=leftline,framerule=1.5pt,rulecolor=\color{OliveGreen},breaklines=true,xleftmargin=4pt}
\begin{document}
\begin{titlepage}\centering\vspace*{3cm}
{\Huge\bfseries Operation Gate}\\[10pt]{\LARGE Out-of-Syllabus Handbook}\\[24pt]
{\large Advanced topics for later learning, beyond GATE DA 2027}\\[40pt]
Every code block in this book was run, and every output shown is the real output.\\[8pt]
Each chapter matches one narrated film.
\end{titlepage}
\tableofcontents
"""
out.append(T)
for pname,rng in parts.items():
    out.append("\\part*{%s}\\addcontentsline{toc}{part}{%s}\n"%(esc(pname),esc(pname)))
    for i in rng:
        title,sub,codes,S,sc=film_meta(i)
        out.append("\\chapter{%s}\n\\textit{%s}\n"%(esc(title),esc(sub)))
        for key,cs in codes.items():
            if key=="wk" or not cs or key not in S:continue
            ch=chap_of(sc,key).replace("Room ","Room ")
            out.append("\\section*{%s}\n"%esc(ch))
            expl=[t for sp,t in S[key] if sp=="S" ]
            out.append(esc(" ".join(expl))+"\n")
            twist=[t for sp,t in S[key] if sp=="N"][-1]
            out.append("\\begin{tcolorbox}[colback=yellow!12,colframe=orange!70!black,boxrule=0.4pt,left=4pt,right=4pt,top=2pt,bottom=2pt]\\textbf{%s}\\end{tcolorbox}\n"%esc(twist))
            for cn in dict.fromkeys(cs):
                code=getattr(codes_L,cn).strip("\n")
                try:
                    random.seed(0);o=run(code)
                except Exception as e:
                    o="ERROR %s"%e;print("ERR",i,cn,e)
                out.append("\\begin{Code}\n%s\n\\end{Code}\n\\begin{Out}\n%s\n\\end{Out}\n"%(code,o))
out.append("\\end{document}\n")
open("/home/claude/films/handbook.tex","w").write("".join(out))
