from lhelp import *
import codes,math
def d_ncon(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L29A)],30,150,690,15,20)
    cards(d,t,ts,[(2,"CG after step 1","[0.25, 0.5]",TEAL),(2,"CG after step 2","[0.0909, 0.6364]",GOLD),(2,"direct solver","[0.0909, 0.6364]",GRN),(3,"condition number, Hilbert 6x6","1.5e7",RED)],770,200,470,48,12,16)
    tw(d,sc,t,5,'TWIST #1 — iterate cheaply; watch conditioning')
def d_tens(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L29B)],30,150,690,15,20)
    cards(d,t,ts,[(2,"outer product rank","1",TEAL),(3,"det before / after row swap","-2  /  2",GOLD),(4,"Lie bracket [X, Y]","[[0,-1],[-1,0]]",PUR),(5,"Hessian eigenvalues","0.793, 2.207  → minimum",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,6,'TWIST #2 — structure, brackets and minima')
def d_wk(d,t,sc):walk(d,sc,t,[(WK29,1,2)])
SCENES=[("title",mk_title('Advanced Linear Algebra 3','numerical methods · tensors · Lie brackets'),""),("ncon",d_ncon,'Room 1 · Numerical methods'),("tens",d_tens,'Room 2 · Tensors and forms'),("wk",d_wk,'Walkthrough · CG step size'),("end",mk_end('Advanced linear algebra 3 — complete',['conjugate gradient', 'conditioning', 'tensors', 'Lie bracket'],'next: advanced probability and statistics'),"")]
