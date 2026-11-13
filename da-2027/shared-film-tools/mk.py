import sys, os, json
FD=sys.argv[1];CMD=sys.argv[2]
base=os.path.abspath(FD);os.chdir(base)
for p in ("/home/claude/films","/home/claude/film",base):
    sys.path.insert(0,p)
if CMD=="audio":
    import tts, script
    V={"N":("en-gb+m7",148,38),"R":("en-us+m3",160,62),"S":("en-us+f3",156,58)}
    os.makedirs("wav",exist_ok=True);meta={}
    for sc,lines in script.SCENES.items():
        L=[]
        for i,(sp,tx) in enumerate(lines):
            tts.voice(*V[sp]);p=f"wav/{sc}_{i}.wav";d=tts.say(tx,p);L.append((sp,tx,p,d))
        meta[sc]=L
    json.dump(meta,open("meta.json","w"));tot=0
    for sc,L in meta.items():
        d=0.7+sum(x[3]+0.35 for x in L)+1.0;tot+=d;print(sc,round(d,1))
    print("total",round(tot/60,2),"min")
else:
    import film, scenes
    film.SCENES=scenes.SCENES
    if CMD=="test":
        os.makedirs("tst",exist_ok=True)
        for key,fn,ch in scenes.SCENES:
            sc=film.Sc(key)
            for fr in (0.3,0.62,0.93):film.frame(sc,sc.dur*fr,fn,ch).save(f"tst/{key}_{int(fr*100)}.png")
        from PIL import Image
        keys=[s[0] for s in scenes.SCENES]
        for gi in range(0,len(keys),5):
            g=keys[gi:gi+5];S=Image.new("RGB",(3*640,len(g)*360))
            for r,k in enumerate(g):
                for c,f in enumerate((30,62,93)):S.paste(Image.open(f"tst/{k}_{f}.png").resize((640,360)),(c*640,r*360))
            S.save(f"sheet{gi//5}.png")
    elif CMD=="render":
        for key in sys.argv[3:]:
            rc=film.render(key,f"sc_{key}.tmp.mp4")
            if rc==0:os.rename(f"sc_{key}.tmp.mp4",f"sc_{key}.mp4")
    elif CMD=="mix":
        import numpy as np, wave
        SR=22050;order=[s[0] for s in scenes.SCENES];scs=[film.Sc(k) for k in order]
        tot=sum(int(s.dur*30)/30 for s in scs);N=int(tot*SR)+SR;voice=np.zeros(N,dtype=np.float32);off=0.0
        for s in scs:
            for i,(sp,tx,p,du) in enumerate(s.L):
                w=wave.open(p);a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
                st=int((off+s.ts[i])*SR);voice[st:st+len(a)]+=a*0.9
            off+=int(s.dur*30)/30
        t=np.arange(N)/SR;chords=[(220,261.6,329.6),(174.6,220,261.6),(261.6,329.6,392),(196,246.9,293.7)];mus=np.zeros(N,dtype=np.float32)
        for i,f in enumerate(chords*int(tot/32+2)):
            a=int(i*8*SR);b=min(N,int((i+1)*8*SR))
            if a>=N:break
            tt=t[a:b]-t[a];env=np.minimum(1,np.minimum(tt/1.5,(8-tt)/1.5))
            for fr in f:mus[a:b]+=(np.sin(2*np.pi*fr*tt)+0.4*np.sin(2*np.pi*2*fr*tt+tt))*env*0.018
        fade=np.clip(np.minimum(t/2,(tot-t)/3),0,1);mix=np.clip(voice+mus*fade,-1,1)
        with wave.open("mix.wav","wb") as w:
            w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype(np.int16).tobytes())
        open("list.txt","w").write("".join(f"file sc_{k}.mp4\n" for k in order));print(round(tot,1))
