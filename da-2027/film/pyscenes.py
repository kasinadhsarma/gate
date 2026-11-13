from pyviz import *
def tag(d,x,y,name,col):
    rbox(d,(x,y,x+54,y+34),col,None,17);ctext(d,(x+27,y+17),name,F(20),(10,10,30))
def obj(d,x,y,w,items,col=(60,70,120)):
    rbox(d,(x,y,x+w,y+48),col,WHITE,8,2)
    for i,it in enumerate(items):ctext(d,(x+22+i*40,y+24),str(it),F(22,True,True),WHITE)
CODE1=["""
x = 7
y = 3.5
s = "gate"
ok = True
n = None
print(type(x), type(y), type(s))
""","""
a = [1, 2]
b = a
c = [1, 2]
b.append(3)
print(a, c, a is b, a == c, a is c)
"""]
def d_p1(d,t,sc):
    ts=sc.ts;ctext(d,(W//2,128),"",F(10))
    k=panel(d,sc,t,[(2,CODE1[0]),(3,CODE1[1])])
    if k==0 or k is None:
        for i,(n,v,c) in enumerate([("x","7  int",TEAL),("y","3.5  float",GRN),("s","'gate'  str",PUR),("ok","True  bool",GOLD),("n","None  NoneType",RED)]):
            if t>=ts[2]+0.8+i*0.8:tag(d,720,190+i*62,n,c);d.line([(776,207+i*62),(850,207+i*62)],fill=c,width=3);rbox(d,(850,190+i*62,1180,226+i*62),(24,30,64),c,8,2);ctext(d,(865,208+i*62),v,F(20,True,True),WHITE,"lm")
        if t>=ts[2]:ctext(d,(950,160),"name tags  →  objects with a type",F(20),(170,180,215))
    else:
        ctext(d,(950,160),"two tags, ONE list object",F(22),GOLD)
        tag(d,720,230,"a",TEAL);tag(d,720,300,"b",GRN);tag(d,720,430,"c",PUR)
        obj(d,880,255,200,[1,2,3] if t>=ts[3]+1.6 else [1,2],(70,50,120))
        d.line([(774,247),(880,275)],fill=TEAL,width=3);d.line([(774,317),(880,290)],fill=GRN,width=3)
        obj(d,880,425,160,[1,2]);d.line([(774,447),(880,449)],fill=PUR,width=3)
        if t>=ts[5]:ctext(d,(950,520),"immutable: int str tuple     mutable: list dict set",F(18),GOLD)
    banner(d,ts[6],t,"PYTHON TWIST #1 — a name is a label, not a box",GOLD,115)
CODE2=["""
nums = [5, 2, 9]
nums.append(1)
nums.sort()
print(nums, nums[1:3], nums[::-1])
""","""
t = (3, 4)
x, y = t
print(x + y)
t[0] = 1
""","""
d = {}
for w in "to be or not to be".split():
    d[w] = d.get(w, 0) + 1
print(d)
""","""
s = {1, 2, 2, 3}
print(s, 2 in s, s | {9}, s & {2, 3, 4})
"""]
def d_p2(d,t,sc):
    ts=sc.ts;k=panel(d,sc,t,[(1,CODE2[0]),(2,CODE2[1]),(3,CODE2[2]),(4,CODE2[3])])
    rows=[("list","[ ]","yes","yes","O(n)"),("tuple","( )","no","yes","O(n)"),("dict","{k:v}","yes","unique keys","O(1) avg"),("set","{ }","yes","no","O(1) avg")]
    ctext(d,(950,165),"which container?",F(22),WHITE)
    hdr=["type","literal","mutable","duplicates","find x"];xs=[700,775,855,950,1130]
    for h,x in zip(hdr,xs):ctext(d,(x,205),h,F(15),(170,180,215),"lm")
    for i,r in enumerate(rows):
        y=235+i*70;act=(k==i)
        rbox(d,(690,y,1235,y+56),(40,50,100) if act else (22,28,58),[TEAL,GRN,PUR,GOLD][i] if act else (70,80,120),10,3 if act else 1)
        for v,x in zip(r,xs):ctext(d,(x,y+28),v,F(18,True,True),WHITE,"lm")
    ctext(d,(950,540),"dicts keep insertion order (Python 3.7+)",F(16),(170,180,215))
    banner(d,ts[5],t,"PYTHON TWIST #2 — choose by the question you will ask",PUR,115)
CODE3=["""
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i, end=" ")
""","""
n = 29
for d in range(2, int(n**0.5) + 1):
    if n % d == 0:
        print("composite")
        break
else:
    print("prime")
""","""
x, steps = 100, 0
while x > 1:
    x //= 2
    steps += 1
print(steps)
""","""
print([i * i for i in range(6) if i % 2 == 0])
print(list(zip("ab", [1, 2])))
"""]
def d_p3(d,t,sc):
    ts=sc.ts;k=panel(d,sc,t,[(1,CODE3[0]),(2,CODE3[1]),(3,CODE3[2]),(4,CODE3[3])])
    ctext(d,(950,160),["for + continue","for … else","while: halve until 1","comprehension"][k] if k is not None else "",F(22),GOLD)
    if k==0:
        for i in range(1,6):
            x=720+(i-1)*95;skip=i%2==0
            rbox(d,(x,230,x+80,300),(50,30,40) if skip else (30,90,80),RED if skip else GRN,10,3);ctext(d,(x+40,265),str(i),F(30,True,True),WHITE)
            ctext(d,(x+40,325),"continue" if skip else "print",F(16),RED if skip else GRN)
    if k==1:
        ds=list(range(2,6));a=int(clamp((t-ts[2]-1.0)/0.7,0,4))
        for i,dv in enumerate(ds):
            x=720+i*95;on=i<a
            rbox(d,(x,230,x+80,300),(30,50,90) if on else (24,28,56),TEAL if on else (70,80,120),10,2);ctext(d,(x+40,258),f"29%{dv}",F(16),WHITE);ctext(d,(x+40,282),str(29%dv),F(20,True,True),TEAL)
        if a>=4:ctext(d,(950,360),"no break  →  else runs  →  prime",F(24),GRN)
    if k==2:
        seq=[100,50,25,12,6,3,1];a=int(clamp((t-ts[3]-1.0)/0.7,0,7))
        for i in range(a):
            x=700+i*78;rbox(d,(x,240,x+68,290),(40,60,110),PUR,8,2);ctext(d,(x+34,265),str(seq[i]),F(22,True,True),WHITE)
            if i:ctext(d,(x-5,265),"",F(10))
        if a>=7:ctext(d,(950,350),"6 halvings  =  ⌊log₂100⌋ = 6",F(24),GOLD)
    if k==3:
        for i in range(0,6):
            x=720+i*85;ev=i%2==0
            rbox(d,(x,230,x+72,290),(30,90,80) if ev else (40,30,50),GRN if ev else (90,80,110),8,2);ctext(d,(x+36,260),str(i),F(24,True,True),WHITE)
            if ev:ctext(d,(x+36,320),str(i*i),F(24,True,True),GOLD)
        ctext(d,(950,375),"keep even i  →  square it",F(20),(170,180,215))
    banner(d,ts[5],t,"PYTHON TWIST #3 — the else belongs to the loop",TEAL,115)
CODE4=["""
def area(w, h=2):
    return w * h
def total(*args, **kw):
    return sum(args), kw
print(area(5), area(5, 3), total(1, 2, 3, unit="cm"))
""","""
x = 10
def f():
    x = 5
    return x
print(f(), x)
""","""
def counter():
    c = 0
    def inc():
        nonlocal c
        c += 1
        return c
    return inc
k = counter()
k(); k()
print(k(), counter()())
""","""
words = ["bb", "a", "ccc"]
print(sorted(words, key=lambda s: len(s)))
"""]
def d_p4(d,t,sc):
    ts=sc.ts;k=panel(d,sc,t,[(1,CODE4[0]),(2,CODE4[1]),(3,CODE4[2]),(4,CODE4[3])])
    if k==1:
        names=[("Built-in",(60,60,100)),("Global  x = 10",(50,70,120)),("Enclosing",(40,90,110)),("Local  x = 5",(30,120,100))]
        ctext(d,(950,160),"L E G B : where does a name live?",F(22),GOLD)
        for i,(n,c) in enumerate(names):
            a=ease((t-ts[2]-0.5-i*0.5)/0.5)
            if a>0:rbox(d,(700+i*28,195+i*28,1225-i*28,540-i*28),c,WHITE,12,2);d.text((712+i*28,200+i*28),n,font=F(16),fill=WHITE)
    if k==2:
        ctext(d,(950,160),"closure: inc remembers c",F(22),GOLD)
        n=int(clamp((t-ts[3]-2.0)/1.0,0,3))
        rbox(d,(720,230,1180,420),(30,40,80),TEAL,12,2);ctext(d,(750,250),"counter()  frame",F(16),TEAL,"lm")
        rbox(d,(760,290,900,350),(20,26,56),GOLD,8,2);ctext(d,(830,320),f"c = {n}",F(28,True,True),GOLD)
        rbox(d,(960,290,1140,350),(20,26,56),PUR,8,2);ctext(d,(1050,320),"inc()",F(26,True,True),PUR)
        d.line([(960,320),(900,320)],fill=PUR,width=3)
        if n>=3:ctext(d,(950,470),"a new counter() makes a NEW c  →  1",F(20),GRN)
    if k==0:
        ctext(d,(950,160),"parameter kinds",F(22),GOLD)
        for i,(a,b,c) in enumerate([("w","positional, required",TEAL),("h=2","default value",GRN),("*args","extra positionals → tuple",PUR),("**kw","extra keywords → dict",GOLD)]):
            if t>=ts[1]+0.6+i*1.2:rbox(d,(710,200+i*80,1225,258+i*80),(24,30,64),c,10,2);ctext(d,(730,229+i*80),a,F(22,True,True),c,"lm");ctext(d,(1210,229+i*80),b,F(18,False),WHITE,"rm")
    if k==3:
        ctext(d,(950,160),"key=lambda s: len(s)",F(22),GOLD)
        for i,(w,l) in enumerate([("bb",2),("a",1),("ccc",3)]):
            rbox(d,(740+i*150,230,880+i*150,290),(40,60,110),PUR,8,2);ctext(d,(810+i*150,255),w,F(24,True,True),WHITE);ctext(d,(810+i*150,320),f"len={l}",F(16),GOLD)
    banner(d,ts[5],t,"PYTHON TWIST #4 — functions are objects too",PUR,115)
CODE5=["""
class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
    def pop(self):
        return self.items.pop()
s = Stack()
s.push(1); s.push(2)
print(s.pop(), len(s.items))
""","""
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("oops:", e)
finally:
    print("cleanup always runs")
""","""
def squares(n):
    for i in range(n):
        yield i * i
print(list(squares(4)))
print(sum(i * i for i in range(10**6)))
"""]
def d_p5(d,t,sc):
    ts=sc.ts;k=panel(d,sc,t,[(1,CODE5[0]),(2,CODE5[1]),(3,CODE5[2])])
    if k==0:
        ctext(d,(950,160),"Stack object:  self.items",F(22),GOLD)
        rbox(d,(780,200,1120,520),(22,28,58),TEAL,12,2)
        ph=int(clamp((t-ts[1]-4.0)/1.4,0,3))
        for i,v in enumerate(([1,2][:min(2,ph)]) if ph<3 else [1]):rbox(d,(820,440-i*70,1080,500-i*70),(70,90,160),WHITE,8,2);ctext(d,(950,470-i*70),f"{v}",F(28,True,True),WHITE)
        if ph>=1:ctext(d,(1160,470),"push 1",F(16),GRN,"lm")
        if ph>=2:ctext(d,(1160,400),"push 2",F(16),GRN,"lm")
        if ph>=3:ctext(d,(950,230),"pop → 2  (last in, first out)",F(20),RED)
    if k==1:
        ctext(d,(950,160),"error handling flow",F(22),GOLD)
        a=int(clamp((t-ts[2]-1.5)/1.6,0,4))
        for i,(n,c) in enumerate([("try: risky code",TEAL),("error raised",RED),("except: handle it",GOLD),("finally: ALWAYS",GRN)]):
            on=i<a
            rbox(d,(740,200+i*80,1190,258+i*80),(30,40,80) if on else (22,26,50),c if on else (70,80,120),10,3 if on else 1);ctext(d,(965,229+i*80),n,F(22,True,True),WHITE if on else (110,120,150))
    if k==2:
        ctext(d,(950,160),"yield: one value at a time",F(22),GOLD)
        n=int(clamp((t-ts[3]-1.5)/0.9,0,4))
        for i in range(4):
            on=i<n;rbox(d,(720+i*115,210,820+i*115,270),(30,90,80) if on else (24,28,56),GRN if on else (70,80,120),8,2);ctext(d,(770+i*115,240),str(i*i) if on else "?",F(26,True,True),WHITE)
        rbox(d,(720,330,1180,390),(50,30,40),RED,10,2);ctext(d,(950,360),"list of 10^6 squares: 8,000,056 bytes",F(20),WHITE)
        rbox(d,(720,410,1180,470),(24,70,50),GRN,10,2);ctext(d,(950,440),"generator object: 200 bytes",F(20),WHITE)
    banner(d,ts[4],t,"PYTHON TWIST #5 — be lazy, compute on demand",GRN,115)
