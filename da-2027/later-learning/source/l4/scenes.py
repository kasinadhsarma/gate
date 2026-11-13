from lhelp import *
import codes
def d_ret(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L4A)],30,150,690,15,20)
    docs=["refund within 30 days","shipping takes 5 days","password reset 1 hour"];sc_=[0.0,0.15,0.0]
    if t>=ts[2]:
        lab(d,1000,170,"question: how long does shipping take",GOLD,15)
        for i,dc in enumerate(docs):cell(d,780,195+i*60,300,40,dc,GRY,fs=15)
    if t>=ts[3]:
        for i,v in enumerate(sc_):
            c=GOLD if v>0 else GRY;rbox(d,(1100,200+i*60,1100+max(4,int(v*900)),224+i*60),c,None,4);lab(d,1100+max(4,int(v*900))+8,212+i*60,f"{v:.2f}",WHITE,15,"lm")
    if t>=ts[4]:lab(d,1000,400,"best match: shipping",GRN,22)
    tw(d,sc,t,5,"TWIST #1 — embeddings: nearest vector wins")
def d_rag(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(3,L4B)],30,150,690,16,21)
    if t>=ts[2]:
        for i,(n,c) in enumerate([("question",TEAL),("retrieve",PUR),("prompt",GOLD),("model",GRN),("answer",RED)]):
            if t>=ts[2]+i*1.2:cell(d,770+(i%3)*160,190+(i//3)*70,140,44,n,c,fs=16)
    if t>=ts[3]:
        lab(d,1000,360,"chunks (overlap = 2)",WHITE,16)
        cell(d,790,380,400,36,"one two three four five six",TEAL,fs=15)
        cell(d,850,426,400,36,"five six seven eight nine ten",GRN,fs=15)
    tw(d,sc,t,5,"TWIST #2 — retrieval = facts, generation = language")
def d_wk(d,t,sc):walk(d,sc,t,[(WK4,1,2)])
SCENES=[("title",mk_title("NLP and Retrieval","vector search · RAG"),""),("ret",d_ret,"Room 1 · Search"),("rag",d_rag,"Room 2 · RAG"),("wk",d_wk,"Walkthrough · overlap"),("end",mk_end("NLP and retrieval — complete",["tf-idf","cosine","chunking","grounded prompt"],"next: reinforcement learning"),"")]
