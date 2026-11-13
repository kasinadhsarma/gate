from gcommon import *
import codes
def d_ra(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.RA)],30,150,690,13,17)
    if t>=ts[2]:
        for i,(l,c,s) in enumerate([("σ  select rows",TEAL,"σ dept=cs (S)"),("π  project columns",GOLD,"π name (S)"),("JOIN",PUR,"S JOIN E")]):
            bx(d,790,200+i*60,200,46,c,l,16);ctext(d,(1010,223+i*60),s,F(16,True,True),c,"lm")
    if t>=ts[4]:bx(d,790,400,200,46,GRN,"÷  division",16);ctext(d,(1010,423),"E ÷ {db, ml} → s1, s3",F(16,True,True),GRN,"lm")
    if t>=ts[6]:ctext(d,(1000,480),"SQL: GROUP BY … HAVING COUNT(DISTINCT)=2",F(14),WHITE)
    tw(d,sc,t,7,"TWIST #1 — division = the 'for all' of algebra")
def d_bag(d,t,sc):
    ts=sc.ts;k=panel2(d,sc,t,[(3,codes.RB)],30,150,690,17,22)
    if t>=ts[2]:
        ctext(d,(900,230),"SQL (bag)",F(18,True),GOLD);ctext(d,(900,265),"cs, cs, ee",F(20),WHITE)
        ctext(d,(1130,230),"algebra (set)",F(18,True),TEAL);ctext(d,(1130,265),"cs, ee",F(20),WHITE)
    if t>=ts[3]:ctext(d,(1010,350),"SELECT DISTINCT matches π",F(20,True),GRN)
    tw(d,sc,t,4,"TWIST #2 — algebra uses sets, SQL uses bags")
SCENES=[("title",mk_title("The Vault of Tables, part 2","relational algebra"),""),("ra",d_ra,"Room 1 · Relational algebra"),("bag",d_bag,"Room 2 · Sets versus bags"),("end",mk_end("Relational algebra — complete",["select σ","project π","join","division ÷"],"Operation Gate · every topic covered"),"")]
