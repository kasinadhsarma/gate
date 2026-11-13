from lhelp import *
import codes
def d_etl(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L8A)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,880,170,"raw feed (4 rows)",WHITE,15)
        for i,r in enumerate(["01-01 p1","01-01 p2","01-02 p1","01-02 p1"]):cell(d,780,190+i*40,200,34,r,RED if i==3 else TEAL,fs=14)
    if t>=ts[3]:
        arrow(d,(990,260),(1040,260),GOLD,4,12);lab(d,1140,170,"fact table (3 rows)",WHITE,15)
        for i,r in enumerate(["01-01 p1","01-01 p2","01-02 p1"]):cell(d,1050,190+i*40,180,34,r,GRN,fs=14)
    if t>=ts[4]:hbars(d,800,380,[("p1",50),("p2",20)],60,w=240,col=[TEAL,PUR],lw=60)
    tw(d,sc,t,5,"TWIST #1 — idempotent loads recover from failures")
def d_scale(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L8B)],30,150,690,16,21)
    if t>=ts[2]:
        lab(d,960,170,"users per shard (1000 users)",WHITE,16);vbars(d,790,195,130,[("s0",249),("s1",251),("s2",249),("s3",251)],260,bw=60,gap=30,col=[TEAL,PUR,GRN,GOLD])
    if t>=ts[3]:
        lab(d,1000,390,"rows processed tonight",WHITE,16);hbars(d,790,410,[("all rows",1000),("new only",10)],1000,w=260,col=[RED,GRN],lw=90)
    tw(d,sc,t,5,"TWIST #2 — shard, partition, process only what is new")
def d_wk(d,t,sc):walk(d,sc,t,[(WK8,1,2)])
SCENES=[("title",mk_title("Data Engineering","pipelines · warehouses · SQL at scale"),""),("etl",d_etl,"Room 1 · Pipeline"),("scale",d_scale,"Room 2 · Scale"),("wk",d_wk,"Walkthrough · idempotent"),("end",mk_end("Data engineering — complete",["ETL","idempotent","shards","watermark"],"next: system design"),"")]
