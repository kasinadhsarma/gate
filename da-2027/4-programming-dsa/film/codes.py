P1='''
a = [1, 2]
b = a                      # b is another NAME for the same list
b.append(3)
print(a, a is b)           # change through b shows up in a
c = a[:]                   # slice = a real copy
print(c is a, c == a)      # different object, equal value
def add(x, bag=[]):        # TWIST: default list is made ONCE
    bag.append(x)
    return bag
print(add(1), add(2))      # same bag is reused
# UPDATE: use bag=None, then create a new list inside
'''
P2='''
src = "x = 2 + 3"
code = compile(src, "<demo>", "exec")  # step 1: source -> bytecode
print(code.co_consts)       # constants the VM will load
print(code.co_names)        # names it will store
ns = {}
exec(code, ns)              # step 2: the virtual machine runs it
print(ns["x"])
# UPDATE: 2 + 3 was folded to 5 before running
'''
D1='''
from collections import deque
data = list(range(1000))
def list_find(v):                  # list: look at items one by one
    steps = 0
    for item in data:
        steps += 1
        if item == v: break
    return steps
s = set(data)                      # set: hash jumps to the slot
print(list_find(999), 999 in s)    # 1000 steps vs one hash lookup
q = deque()
q.append("a"); q.append("b")       # queue: first in, first out
st = []
st.append("a"); st.append("b")     # stack: last in, first out
print(q.popleft(), st.pop())
# UPDATE: pick the structure that matches the access pattern
'''
S1='''
def bsearch(a, t):
    lo, hi, steps = 0, len(a) - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2       # look at the middle
        steps += 1
        if a[mid] == t: return mid, steps
        if a[mid] < t: lo = mid + 1    # throw away the left half
        else: hi = mid - 1             # throw away the right half
    return -1, steps
a = list(range(0, 2000, 2))        # 1000 sorted numbers
print(bsearch(a, 1998))            # worst end of the list
print(bsearch(a, 7))               # absent value
print(len(a).bit_length())         # about log2(n) steps
# UPDATE: data must be sorted first
'''
S2='''
def msort(a):
    if len(a) <= 1: return a, 0
    mid = len(a) // 2
    L, c1 = msort(a[:mid])         # divide
    R, c2 = msort(a[mid:])
    out, i, j, c = [], 0, 0, 0
    while i < len(L) and j < len(R):   # combine: merge two sorted lists
        c += 1
        if L[i] <= R[j]: out.append(L[i]); i += 1
        else: out.append(R[j]); j += 1
    out += L[i:] + R[j:]
    return out, c1 + c2 + c
r, c = msort([5, 2, 9, 1, 7, 3, 8, 4])
print(r, c)
print(msort(list(range(1024, 0, -1)))[1])  # n log n scale
# UPDATE: recurrence T(n) = 2T(n/2) + n
'''
G1='''
from collections import deque
import heapq
g = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": ["F"], "E": ["F"], "F": []}
def bfs(s):                        # queue -> fewest edges
    dist, q = {s: 0}, deque([s])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
def dfs(u, seen):                  # recursion -> go deep first
    seen.append(u)
    for v in g[u]:
        if v not in seen: dfs(v, seen)
    return seen
print(bfs("A"))
print(dfs("A", []))
# UPDATE: BFS = queue, DFS = recursion
'''
G2='''
import heapq
w = {"A": [("B", 4), ("C", 1)], "C": [("B", 2), ("D", 7)], "B": [("D", 1)], "D": []}
best, pq = {"A": 0}, [(0, "A")]
while pq:                          # Dijkstra: always expand the cheapest
    d, u = heapq.heappop(pq)
    if d > best[u]: continue
    for v, c in w[u]:
        if d + c < best.get(v, 99):
            best[v] = d + c
            heapq.heappush(pq, (d + c, v))
print(best)
# UPDATE: negative edge weights break Dijkstra
'''
WD1='''
a = [2, 5, 8, 12, 16, 23, 38]
t = 23
lo, hi = 0, 6
mid = (lo + hi) // 2
print(mid, a[mid])
lo = mid + 1
mid = (lo + hi) // 2
print(mid, a[mid])
'''
