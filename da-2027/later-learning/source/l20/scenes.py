from lhelp import *
import codes,math
def d_diff(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L20A)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,172,"signal kept  →  noisy value  →  recovered",WHITE,15)
        cards(d,t,ts,[(2,"step 1  (0.90 signal)","1.52  →  2.0",TEAL),(2,"step 2  (0.60)","0.82  →  2.0",TEAL),(3,"step 3  (0.30)","1.66  →  2.0",GOLD),(3,"step 4  (0.05)","-1.79  →  2.0",GOLD)],770,195)
    if t>=ts[4]:lab(d,1000,470,"generate: pure noise → remove noise, step by step",GRN,16)
    tw(d,sc,t,5,'TWIST #1 — many small denoising steps')
def d_ae(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L20B)],30,150,690,15,20)
    if t>=ts[2]:
        a=Ax(790,200,300,240,(-2.5,2.5),(-5,5));a.axes(d,(-2,0,2),(-4,0,4))
        for x in [-2,-1,-0.5,0.5,1,2]:a.dot(d,x,2*x,TEAL,6)
        lab(d,940,185,"data on a line",WHITE,14)
    if t>=ts[3]:
        lab(d,1140,215,"reconstruction error",WHITE,14);vbars(d,1100,235,150,[("before",8.438),("after",0.0)],9,bw=50,gap=20,col=[RED,GRN],fmt="{:g}")
    tw(d,sc,t,5,'TWIST #2 — a bottleneck forces structure')
def d_gan(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L20C)],30,150,690,15,20)
    if t>=ts[2]:
        import math as m
        def pdf(x,mu):return m.exp(-(x-mu)**2/2)/m.sqrt(2*m.pi)
        a=Ax(790,200,440,200,(-3,6),(0,1.05));a.axes(d,(-2,0,2,4,6),(0,0.5,1));lab(d,1000,182,"best discriminator D*(x)",WHITE,15)
        d.line([a.P(-3,0.5),a.P(6,0.5)],fill=TEAL,width=4)
        if t>=ts[3]:a.curve(d,lambda x:pdf(x,0)/(pdf(x,0)+pdf(x,3)),GOLD,4)
        lab(d,1160,a.py(0.5)-14,"fake = real: 0.5",TEAL,14,"rm")
    if t>=ts[4]:lab(d,1000,450,"flow:  p(x) = p(z) / |slope|",WHITE,16);lab(d,1000,485,"0.176 = 0.176",GOLD,22)
    tw(d,sc,t,5,'TWIST #3 — competition, or invertible steps')
def d_wk(d,t,sc):walk(d,sc,t,[(WK20,1,2)])
SCENES=[("title",mk_title('Generative Models','diffusion · autoencoders · GANs · flows'),""),("diff",d_diff,'Room 1 · Diffusion'),("ae",d_ae,'Room 2 · Autoencoders'),("gan",d_gan,'Room 3 · GANs and flows'),("wk",d_wk,'Walkthrough · one diffusion step'),("end",mk_end('Generative models — complete',['diffusion', 'autoencoder', 'GAN', 'flow'],'next: geometric deep learning'),"")]
