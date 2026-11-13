import itertools, random, math
print("== 2024 ==")
# Q30 quicksort last pivot on sorted array, count real swaps
def qs(a,lo,hi,c):
    if lo<hi:
        p=a[hi];i=lo-1
        for j in range(lo,hi):
            if a[j]<=p:
                i+=1
                if i!=j: a[i],a[j]=a[j],a[i];c[0]+=1
        if i+1!=hi: a[i+1],a[hi]=a[hi],a[i+1];c[0]+=1
        qs(a,lo,i,c);qs(a,i+2,hi,c)
a=[60,70,80,90,100];c=[0];qs(a,0,4,c);print("Q30 real swaps",c[0],a)
# Q32 deque
from collections import deque
D=deque();D.appendleft(10);D.append(32);a=D.popleft();D.append(28);D.append(17);a=D.popleft();a=D.pop();print("Q32",a)
# Q38
def count(cd,i):
    if i not in cd.keys(): return 1
    ans=1
    for j in cd[i]: ans+=count(cd,j)
    return ans
print("Q38",count({0:[1,2],1:[3,4,5],2:[6,7,8]},0))
# Q39
def computeS(X):
    S=[1]*len(X)
    for i in range(1,len(X)):
        if X[i-1]<=X[i]: S[i]+=S[i-1]
    return S
print("Q39",computeS([6,3,5,4,10]))
# Q41
def fun(D,s1,s2):
    if s1<s2:
        D[s1],D[s2]=D[s2],D[s1];fun(D,s1+1,s2-1)
L=[1,2,3,4,5];fun(L,0,4);print("Q41",L);L=[1,2,3,4,5,6];fun(L,1,4);print("Q41b",L)
# Q45 passes
def bubble_pass(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:a[i],a[i+1]=a[i+1],a[i]
def sel_pass(a,k):
    m=min(range(k,len(a)),key=lambda i:a[i]);a[k],a[m]=a[m],a[k]
def ins_pass(a,k):
    key=a[k];j=k-1
    while j>=0 and a[j]>key:a[j+1]=a[j];j-=1
    a[j+1]=key
b=[4,3,2,1,5];bubble_pass(b);print("bubble1",b);bubble_pass(b);print("bubble2",b)
s=[4,3,2,1,5];sel_pass(s,0);print("sel1",s);sel_pass(s,1);print("sel2",s)
i=[4,3,2,1,5];ins_pass(i,1);print("ins1",i);ins_pass(i,2);print("ins2",i)
# Q52 brute force binary trees (each node: 0,1,2 children, shapes by structure)
def trees(n):
    if n==0: yield None;return
    for l in range(n):
        for L in trees(l):
            for R in trees(n-1-l): yield (L,R)
def stats(t):
    if t is None: return -1,0,0,0  # height, internal, leaves, nodes
    hl,il,ll,nl=stats(t[0]);hr,ir,lr,nr=stats(t[1])
    h=max(hl,hr)+1;n=nl+nr+1
    if t[0] is None and t[1] is None: return h,0,1,1
    return h,il+ir+1,ll+lr,n
ok={k:True for k in "ABCD"}
for n in range(1,10):
    for t in trees(n):
        H,I,L,N=stats(t)
        ok['A']&= L<=I+1; ok['B']&= H+1<=N<=2**(H+1)-1; ok['C']&= H<=I<=2**H-1; ok['D']&= H<=L<=2**(H-1)
print("Q52",ok)
# Q14 DFS undirected check with shortest-dist definition
def check(n,edges,order_seed):
    adj={i:[] for i in range(n)}
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    rnd=random.Random(order_seed)
    for i in adj: rnd.shuffle(adj[i])
    # BFS dist
    from collections import deque
    d=[None]*n;d[0]=0;q=deque([0])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if d[y] is None:d[y]=d[x]+1;q.append(y)
    if None in d:return None
    state=[0]*n;explored=set();res=[]
    def dfs(u):
        state[u]=1
        for v in adj[u]:
            e=frozenset((u,v))
            if e in explored: continue
            explored.add(e)
            if d[u]<d[v]:
                res.append('tree' if state[v]==0 else ('back' if state[v]==1 else 'other'))
            if state[v]==0: dfs(v)
        state[u]=2
    dfs(0);return res
cnt={}
rnd=random.Random(1)
for trial in range(4000):
    n=rnd.randint(4,8);E=set()
    for _ in range(rnd.randint(n,2*n)):
        u,v=rnd.sample(range(n),2);E.add((min(u,v),max(u,v)))
    r=check(n,sorted(E),trial)
    if r:
        for x in r:cnt[x]=cnt.get(x,0)+1
print("Q14 shortest-dist reading: classification counts of edges with d[u]<d[v] explored first from u:",cnt)
# explicit counterexample
edges=[(0,1),(0,2),(1,3),(3,4),(4,2),(2,3)]  # s=0,w=1,u=2,v=3,y=4
adj={0:[1,2],1:[0,3],3:[1,4,2],4:[3,2],2:[4,0,3]}
print("counterexample listed")
# discovery-time reading: d[u]<d[v] => tree always? test
def check2(n,edges,seed):
    adj={i:[] for i in range(n)};
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    r=random.Random(seed)
    for i in adj:r.shuffle(adj[i])
    disc=[None]*n;state=[0]*n;explored=set();t=[0];res=[]
    def dfs(u):
        t[0]+=1;disc[u]=t[0];state[u]=1
        for v in adj[u]:
            e=frozenset((u,v))
            if e in explored:continue
            explored.add(e)
            kind='tree' if state[v]==0 else 'back'
            res.append((u,v,kind))
            if state[v]==0:dfs(v)
        state[u]=2
    dfs(0);return [(u,v,k,disc[u],disc[v]) for u,v,k in res]
bad=0;tot=0
rnd=random.Random(2)
for trial in range(3000):
    n=rnd.randint(4,8);E=set()
    for _ in range(rnd.randint(n,2*n)):
        u,v=rnd.sample(range(n),2);E.add((min(u,v),max(u,v)))
    for (u,v,k,du,dv) in check2(n,sorted(E),trial):
        if du<dv:
            tot+=1;bad+= (k!='tree')
print("Q14 discovery-time reading: edges with disc[u]<disc[v] first explored from u:",tot,"non-tree:",bad)
print("== 2025 ==")
# Q18
T=[None]*10
for k in [1,4,5,6,14,15]:
    h=3*k%10
    while T[h] is not None:h=(h+1)%10
    T[h]=k
print("Q18",T)
# Q29
def inv_swaps(a):
    c=0;a=a[:]
    for k in range(1,len(a)):
        j=k
        while j>0 and a[j-1]>a[j]:a[j-1],a[j]=a[j],a[j-1];c+=1;j-=1
    return c
for x in (10,12,14,16):print("Q29 x=",x,inv_swaps([1,3,5,7,9,11,x,15,13]))
# Q47
A={"this","that"};B={"that","other"};C={"other","this"}
it=0
while "other" in C:
    it+=1
    if "this" in A:A,B,C=A-B,B-C,C-A
    if "that" in B:A,B,C=C|A,A|B,B|C
    print("iter",it,sorted(A),sorted(B),sorted(C))
    if it>6:break
print("Q47 contain 'this':",[n for n,S in zip("ABC",(A,B,C)) if "this" in S])
# Q63
def f(a,b):
    if a==0:return b
    if a%2==1:return 2*f((a-1)//2,b)
    return b+f((a-1)//2,b)
print("Q63",f(15,10))
# Q64
S=[];x=0;flag=0;total=0;S.append(x)
while S:
    if flag==0:
        x+=1;S.append(x)
    if x==8:flag=1
    if flag==1:
        x=S.pop()
        if x%2==1:S.pop()
        total+=x
print("Q64",total)
# Q65
sys_rec=__import__('sys');sys_rec.setrecursionlimit(10000)
order=[];seen=set()
def dfs(i):
    seen.add(i);order.append(i)
    for j in (i+2,i+1):
        if j<=100 and j not in seen:dfs(j)
dfs(0);print("Q65",len(order)-order.index(50)-1,order[:5],order[50:55])
# Q58 shortest-path logic: check which pairs would shorten
print("== 2026 ==")
def append_to_lst(val,lst=[]):
    lst.append(val);return lst
print("Q16",append_to_lst(1),append_to_lst(2),append_to_lst(3,[]))
def mystery(n):
    global calls;calls+=1
    return 1 if n<=0 else mystery(n-1)+mystery(n-2)
calls=0;mystery(4);print("Q39 calls",calls)
P=[1,2,3,5,4]
def bubble_cmp(a,early):
    a=a[:];c=0
    for p in range(len(a)-1):
        sw=False
        for i in range(len(a)-1-p):
            c+=1
            if a[i]>a[i+1]:a[i],a[i+1]=a[i+1],a[i];sw=True
        if early and not sw:break
    return c
def ins_cmp(a):
    a=a[:];c=0;sw=0
    for k in range(1,len(a)):
        j=k
        while j>0:
            c+=1
            if a[j-1]>a[j]:a[j-1],a[j]=a[j],a[j-1];sw+=1;j-=1
            else:break
    return c,sw
print("Q49 bubble no-early",bubble_cmp(P,False),"bubble early",bubble_cmp(P,True),"insertion (cmp,swaps)",ins_cmp(P))
def outer():
    x=[]
    def inner(val):
        x.append(val);return x
    return inner
f1=outer();f2=outer();print("Q50",f1(10),f1(20),f2(30),f1(40))
def fn(L,i=0):
    if i>=len(L)-1:return 0
    if L[i]>L[i+1]:
        L[i+1],L[i]=L[i],L[i+1];return 1+fn(L,i+1)
    else:return fn(L,i+1)
data=[5,3,4,1,2];count=0
for _ in range(len(data)):count+=fn(data)
print("Q58",count,data)
print("Q31",math.floor(math.log2(1000))+1)
# Q25 tree rebuild
pre="PQSERFG";ino="SQEPFRG"
def build(pre,ino):
    if not pre:return None
    r=pre[0];k=ino.index(r)
    return (r,build(pre[1:1+k],ino[:k]),build(pre[1+k:],ino[k+1:]))
t=build(pre,ino);print("Q25 tree",t)
def post(t):return "" if t is None else post(t[1])+post(t[2])+t[0]
print("post",post(t))
# Q15 recurrences ok
# Q31 variant
print("log2 1000",math.log2(1000))
