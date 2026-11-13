import numpy as np, wave, json
import film
SR=22050
order=["title","m1","mb","m2","m3","m4","m5","s1","s2","s3","s4","s5","s6","s7","s8","end"]
scs=[film.Sc(k) for k in order];tot=sum(int(s.dur*30)/30 for s in scs)
N=int(tot*SR)+SR
voice=np.zeros(N,dtype=np.float32);off=0.0
for s in scs:
    for i,(sp,tx,p,du) in enumerate(s.L):
        w=wave.open(p);a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
        st=int((off+s.ts[i])*SR);voice[st:st+len(a)]+=a*0.9
    off+=int(s.dur*30)/30
t=np.arange(N)/SR
chords=[(220,261.6,329.6),(174.6,220,261.6),(261.6,329.6,392),(196,246.9,293.7)]
mus=np.zeros(N,dtype=np.float32)
for i,f in enumerate(chords*int(tot/32+2)):
    a=int(i*8*SR);b=min(N,int((i+1)*8*SR))
    if a>=N:break
    tt=t[a:b]-t[a];env=np.minimum(1,np.minimum(tt/1.5,(8-tt)/1.5))
    for fr in f:mus[a:b]+=(np.sin(2*np.pi*fr*tt)+0.4*np.sin(2*np.pi*2*fr*tt+tt))*env*0.018
mus*=(0.8+0.2*np.sin(2*np.pi*0.15*t))
fade=np.minimum(1,np.minimum(t/2,(tot-t)/3));fade=np.clip(fade,0,1)
mix=np.clip(voice+mus*fade,-1,1)
with wave.open("mix.wav","wb") as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype(np.int16).tobytes())
print(round(tot,1))
