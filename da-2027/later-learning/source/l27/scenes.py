from lhelp import *
import codes,math
def d_vs(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L27A)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"polynomial 5 + 3x + 4x²  =  [5, 3, 4]",WHITE,16)
        mat(d,800,215,[[0,1,0],[0,0,2],[0,0,0]],50,34,GOLD,18);lab(d,985,250,"×",WHITE,22);mat(d,1010,215,[[5],[3],[4]],50,34,TEAL,18)
    if t>=ts[3]:lab(d,1000,350,"= [3, 8, 0]   i.e.  3 + 8x",GRN,20)
    cards(d,t,ts,[(4,"rank + nullity","2 + 2 = 4 columns",GOLD),(4,"eigenvalues M and P⁻¹MP","2, 3  and  2, 3",GOLD)],770,400,470,44,10,16)
    tw(d,sc,t,5,'TWIST #1 — anything you can add and scale is a vector')
def d_ip(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L27B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"Q · Qᵀ",WHITE,16);mat(d,860,205,[[1,0,0],[0,1,0],[0,0,1]],60,40,GRN,22);lab(d,1000,350,"identity → orthonormal",GRN,17)
    cards(d,t,ts,[(3,"rank over the reals","3",TEAL),(3,"rank over GF(2)  (mod 2)","2",RED)],770,400,470,44,10,16)
    tw(d,sc,t,5,'TWIST #2 — orthogonalise, and mind the field')
def d_wk(d,t,sc):walk(d,sc,t,[(WK27,1,2)])
SCENES=[("title",mk_title('Advanced Linear Algebra 1','vector spaces · linear maps · Gram-Schmidt'),""),("vs",d_vs,'Room 1 · Vector spaces and maps'),("ip",d_ip,'Room 2 · Inner products and fields'),("wk",d_wk,'Walkthrough · Gram-Schmidt step'),("end",mk_end('Advanced linear algebra 1 — complete',['polynomial space', 'rank-nullity', 'Gram-Schmidt', 'fields'],'next: decompositions'),"")]
