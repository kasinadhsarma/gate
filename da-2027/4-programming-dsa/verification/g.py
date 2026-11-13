from collections import deque, Counter
import heapq
def two_sum(a,t):
    seen={}
    for i,x in enumerate(a):
        if t-x in seen: return (seen[t-x],i)
        seen[x]=i
print(two_sum([2,7,11,15],9))
def two_ptr(a,t):
    i,j=0,len(a)-1
    while i<j:
        s=a[i]+a[j]
        if s==t:return (i,j)
        i,j=(i+1,j) if s<t else (i,j-1)
print(two_ptr([1,3,4,6,9],10))
def best_window(a,k):
    s=sum(a[:k]);b=s
    for i in range(k,len(a)):
        s+=a[i]-a[i-k];b=max(b,s)
    return b
print(best_window([2,1,5,1,3,2],3))
def longest_unique(s):
    last={};l=0;b=0
    for r,ch in enumerate(s):
        if ch in last and last[ch]>=l:l=last[ch]+1
        last[ch]=r;b=max(b,r-l+1)
    return b
print(longest_unique("abcabcbb"))
P=[0]
for x in [3,1,4,1,5,9]:P.append(P[-1]+x)
print(P, P[5]-P[2])
def min_speed(piles,h):
    lo,hi=1,max(piles)
    while lo<hi:
        m=(lo+hi)//2
        if sum(-(-p//m) for p in piles)<=h:hi=m
        else:lo=m+1
    return lo
print(min_speed([3,6,7,11],8))
def next_greater(a):
    r=[-1]*len(a);st=[]
    for i,x in enumerate(a):
        while st and a[st[-1]]<x:r[st.pop()]=x
        st.append(i)
    return r
print(next_greater([2,1,2,4,3]))
def islands(g):
    R,C=len(g),len(g[0]);seen=set();n=0
    for r in range(R):
        for c in range(C):
            if g[r][c]==1 and (r,c) not in seen:
                n+=1;q=deque([(r,c)]);seen.add((r,c))
                while q:
                    y,x=q.popleft()
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<R and 0<=nx<C and g[ny][nx]==1 and (ny,nx) not in seen:
                            seen.add((ny,nx));q.append((ny,nx))
    return n
print(islands([[1,1,0,0],[0,1,0,1],[1,0,0,1]]))
def topk(a,k):
    h=[]
    for x in a:
        heapq.heappush(h,x)
        if len(h)>k:heapq.heappop(h)
    return sorted(h,reverse=True)
print(topk([5,1,9,3,7,8],3))
def valid(s):
    st=[];m={')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in m:
            if not st or st.pop()!=m[ch]:return False
        else:st.append(ch)
    return not st
print(valid("{[()]}"),valid("([)]"))
def kadane(a):
    cur=best=a[0]
    for x in a[1:]:
        cur=max(x,cur+x);best=max(best,cur)
    return best
print(kadane([-2,1,-3,4,-1,2,1,-5,4]))
def fib_memo():
    memo={}
    def f(n):
        if n<2:return n
        if n not in memo:memo[n]=f(n-1)+f(n-2)
        return memo[n]
    return f
print(fib_memo()(50))
def merge_sort(a):
    if len(a)<=1:return a
    m=len(a)//2;L=merge_sort(a[:m]);R=merge_sort(a[m:]);o=[];i=j=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:o.append(L[i]);i+=1
        else:o.append(R[j]);j+=1
    return o+L[i:]+R[j:]
print(merge_sort([5,2,9,1,5,6]))
def binsearch(a,t):
    lo,hi=0,len(a)-1;c=0
    while lo<=hi:
        c+=1;m=(lo+hi)//2
        if a[m]==t:return m,c
        if a[m]<t:lo=m+1
        else:hi=m-1
    return -1,c
print(binsearch([1,3,5,7,9,11,13],11), binsearch(list(range(1000)),999))
def topo(n,edges):
    adj=[[] for _ in range(n)];ind=[0]*n
    for u,v in edges:adj[u].append(v);ind[v]+=1
    q=deque(i for i in range(n) if ind[i]==0);o=[]
    while q:
        u=q.popleft();o.append(u)
        for v in adj[u]:
            ind[v]-=1
            if ind[v]==0:q.append(v)
    return o if len(o)==n else None
print(topo(6,[(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]), topo(3,[(0,1),(1,2),(2,0)]))
