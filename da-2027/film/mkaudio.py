import tts, script, json, wave
V={"N":("en-gb+m7",148,38),"R":("en-us+m3",160,62),"S":("en-us+f3",156,58)}
meta={}
for sc,lines in script.SCENES.items():
    L=[]
    for i,(sp,tx) in enumerate(lines):
        tts.voice(*V[sp]); p=f"wav/{sc}_{i}.wav"; d=tts.say(tx,p); L.append((sp,tx,p,d))
    meta[sc]=L
json.dump(meta,open("meta.json","w"))
tot=0
for sc,L in meta.items():
    d=0.7+sum(x[3]+0.35 for x in L)+1.0; tot+=d; print(sc,round(d,1))
print("total",round(tot,1),"s",round(tot/60,2),"min")
