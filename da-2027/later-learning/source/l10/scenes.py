from lhelp import *
import codes
def d_inj(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L10A)],30,150,690,16,21)
    if t>=ts[2]:
        cell(d,770,190,220,44,"review: IGNORE ALL RULES",RED,fs=14);arrow(d,(990,212),(1040,212),GOLD,4,10);cell(d,1045,190,190,44,"model",TEAL,fs=16)
    if t>=ts[3]:
        cell(d,770,270,460,44,"<data> ...untrusted text... </data>",GOLD,fs=16);lab(d,1000,335,"treat as text, never as instructions",WHITE,15)
    if t>=ts[4]:
        lab(d,1000,380,"tool allow-list",WHITE,16)
        cell(d,780,400,200,40,"summarise  ✔",GRN,fs=16);cell(d,1010,400,220,40,"send_email  ✘",RED,fs=16)
    tw(d,sc,t,5,"TWIST #1 — limit what the model may do")
def d_leak(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L10B)],30,150,690,16,21)
    if t>=ts[2]:lab(d,1000,170,"confidence on seen vs unseen data",WHITE,16);vbars(d,850,195,170,[("seen",0.99),("unseen",0.70)],1.0,bw=90,gap=70,col=[RED,TEAL],fmt="{:.2f}")
    if t>=ts[3]:lab(d,1000,430,"gap = 0.29  →  leaks membership",GOLD,19)
    if t>=ts[4]:lab(d,1000,475,"regularise · limit outputs · DP · rate-limit",GRN,16)
    tw(d,sc,t,5,"TWIST #2 — overconfidence is a privacy leak")
def d_wk(d,t,sc):walk(d,sc,t,[(WK10,1,2)])
SCENES=[("title",mk_title("Security of ML Systems","prompt injection · leakage · theft"),""),("inj",d_inj,"Room 1 · Prompt injection"),("leak",d_leak,"Room 2 · Leakage"),("wk",d_wk,"Walkthrough · allow-list"),("end",mk_end("ML security — complete",["data vs instructions","allow-list","membership leak","rate limits"],"next: bits and arrays"),"")]
