import ctypes, espeakng_loader, wave, numpy as np
lib=ctypes.CDLL(espeakng_loader.get_library_path())
lib.espeak_Initialize.restype=ctypes.c_int
sr=lib.espeak_Initialize(1,0,espeakng_loader.get_data_path().encode(),0)
buf=[]
CB=ctypes.CFUNCTYPE(ctypes.c_int,ctypes.POINTER(ctypes.c_short),ctypes.c_int,ctypes.c_void_p)
def cb(w,n,ev):
    if w and n>0: buf.append(np.ctypeslib.as_array(w,shape=(n,)).copy())
    return 0
cbf=CB(cb); lib.espeak_SetSynthCallback(cbf)
def voice(name,rate=150,pitch=50):
    lib.espeak_SetVoiceByName(name.encode())
    lib.espeak_SetParameter(1,rate,0); lib.espeak_SetParameter(3,pitch,0)
def say(text,path):
    buf.clear()
    t=text.encode()
    lib.espeak_Synth(t,len(t)+1,0,0,0,1,None,None); lib.espeak_Synchronize()
    a=np.concatenate(buf) if buf else np.zeros(100,dtype=np.int16)
    with wave.open(path,'wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(a.tobytes())
    return len(a)/sr
if __name__=="__main__":
    voice("en-us",150,50);print(sr,say("Hello Ramu. Why does binary search need a sorted array?","t.wav"))
