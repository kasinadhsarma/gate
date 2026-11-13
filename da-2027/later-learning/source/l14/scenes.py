from lhelp import *
import codes
def d_fen(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L14A),(4,L14B)],30,150,690,15,20)
    if ts[2]<=t<ts[4]:
        v=[3,1,4,1,5,9,2,6];T=[3,4,4,9,5,14,2,31]
        lab(d,1000,172,"Fenwick tree: T[i] covers a block ending at i",WHITE,15)
        for i in range(8):
            cell(d,775+i*56,195,52,38,str(v[i]),TEAL,fs=16);lab(d,775+i*56+26,248,str(i+1),GRY,13)
            cell(d,775+i*56,265,52,38,str(T[i]),GOLD if i in (3,7) else PUR,fs=16)
        lab(d,780,320,"item",TEAL,13,"lm");lab(d,780,340,"T[i]",PUR,13,"lm")
        lab(d,1000,380,"i += i & -i   (update)      i -= i & -i   (query)",WHITE,15)
        if t>=ts[2]+8:lab(d,1000,430,"sum(5) - sum(2) = 10   →   after +10: 20",GRN,17)
    if t>=ts[4]:
        a=[5,2,8,1,9,3,7,4];lab(d,1000,172,"segment tree of minimums",WHITE,15)
        lv=[[1],[1,3],[2,1,3,4],a]
        for L,row in enumerate(lv):
            n=len(row);cw=432//8*(8//n)
            for i,x in enumerate(row):
                cx=785+(i*cw)+(cw-46)//2;hi=(L==3 and 1<=i<=3 and t>=ts[4]+3)
                cell(d,cx,195+L*58,46,38,str(x),GOLD if hi else (TEAL if L==3 else PUR),fs=16)
        if t>=ts[4]+3:lab(d,1000,440,"min of a[1:4] = 1     min of a[4:8] = 3",GRN,17)
    tw(d,sc,t,5,"TWIST #1 — small cost per update, log n per query")
def d_dsu(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L14C),(4,L14D)],30,150,690,14,19)
    if t<ts[4] and t>=ts[2]:
        X=[800+i*80 for i in range(6)];Y=260;lab(d,1000,180,"parent pointers",WHITE,15)
        pr={1:0,2:0,4:3}
        for c,p in pr.items():
            if t>=ts[2]+3+c*0.8:arrow(d,(X[c],Y-18),(X[p]+(10 if p<c else -10),Y-18-(30+(c-p)*8)),GRN,3,10) if False else d.line([(X[c],Y-18),(X[c],Y-50-abs(c-p)*10),(X[p],Y-50-abs(c-p)*10),(X[p],Y-18)],fill=GRN,width=3)
        for i in range(6):node(d,X[i],Y,str(i),GOLD if i in (0,3,5) else TEAL)
        if t>=ts[2]+9:
            lab(d,X[1],Y+55,"group {0,1,2}",GRN,14);lab(d,X[4],Y+55,"group {3,4}",PUR,14);lab(d,X[5],Y+55,"{5}",GRY,14)
            lab(d,1000,400,"3 groups; find(0) == find(2)",GOLD,17)
    if t>=ts[4]:
        lab(d,1000,175,"trie: car, card, care, dog",WHITE,15)
        P={"root":(900,215),"c":(840,265),"a":(840,315),"r":(840,365),"d1":(790,420),"e":(890,420),"d2":(980,265),"o":(980,315),"g":(980,365)}
        E=[("root","c"),("c","a"),("a","r"),("r","d1"),("r","e"),("root","d2"),("d2","o"),("o","g")]
        for a,b in E:edge(d,P[a],P[b])
        for k,(x,y) in P.items():
            end=k in("r","d1","e","g");node(d,x,y,"" if k=="root" else k[0],GOLD if end else TEAL,14,14,w=4 if end else 2)
        if t>=ts[4]+5:lab(d,1100,300,"prefix car →",WHITE,15,"lm");lab(d,1100,330,"car, card, care",GRN,16,"lm")
    tw(d,sc,t,5,"TWIST #2 — near-constant connectivity; prefix search by length")
def d_wk(d,t,sc):walk(d,sc,t,[(WK14,1,2)])
SCENES=[("title",mk_title("Range Queries, DSU, Tries","Fenwick · segment tree · union-find · trie"),""),("fen",d_fen,"Room 1 · Range queries"),("dsu",d_dsu,"Room 2 · Union-find and trie"),("wk",d_wk,"Walkthrough · path compression"),("end",mk_end("Advanced structures 1 — complete",["Fenwick","segment tree","union-find","trie"],"next: balanced trees"),"")]
