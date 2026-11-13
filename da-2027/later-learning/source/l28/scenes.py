from lhelp import *
import codes,math
def d_svd(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L28A)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"singular values",WHITE,15);hbars(d,790,200,[("σ1",5),("σ2",3)],5,w=240,col=[GOLD,TEAL],lw=60)
    cards(d,t,ts,[(3,"rank-1 approximation error","3.0",RED),(3,"equals next singular value","3.0",GOLD)],770,320,470,44,10,16)
    tw(d,sc,t,5,'TWIST #1 — keep the big singular values')
def d_jordan(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L28B)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,175,"Jordan block J",WHITE,15);mat(d,900,200,[[2,1],[0,2]],60,40,GOLD,22)
    cards(d,t,ts,[(2,"eigenvectors","only 1",RED),(2,"J⁵ first row","[32, 80]",GOLD),(4,"eigenvalues of symmetric S","2.382, 4.618",GRN),(4,"Cholesky L·Lᵀ = S","True",GRN)],770,300,470,44,10,16)
    tw(d,sc,t,5,'TWIST #2 — symmetric matrices always diagonalise')
def d_wk(d,t,sc):walk(d,sc,t,[(WK28,1,2)])
SCENES=[("title",mk_title('Advanced Linear Algebra 2','SVD · Jordan form · spectral theorem'),""),("svd",d_svd,'Room 1 · SVD'),("jordan",d_jordan,'Room 2 · Canonical forms'),("wk",d_wk,'Walkthrough · energy share'),("end",mk_end('Advanced linear algebra 2 — complete',['SVD', 'low rank', 'Jordan form', 'spectral theorem'],'next: numerical methods and tensors'),"")]
