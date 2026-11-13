A1='''
from collections import deque
import heapq
g = {"S": [("A", 1), ("B", 4)], "A": [("G", 6)], "B": [("G", 1)], "G": []}
def bfs(s, t):                     # fewest edges, ignores cost
    q = deque([(s, [s], 0)])
    while q:
        u, path, c = q.popleft()
        if u == t: return path, c
        for v, w in g[u]: q.append((v, path + [v], c + w))
def ucs(s, t):                     # cheapest total cost
    pq = [(0, s, [s])]
    while pq:
        c, u, path = heapq.heappop(pq)
        if u == t: return path, c
        for v, w in g[u]: heapq.heappush(pq, (c + w, v, path + [v]))
print(bfs("S", "G"))
print(ucs("S", "G"))
# UPDATE: b^d nodes at depth d: b=10, d=5 -> 100000
print(10 ** 5)
'''
A2='''
import heapq
W = ["....#..", ".##.#..", "...#...", ".#...#.", "...#..."]   # # = wall
def astar(h):
    st, go = (0, 0), (4, 6)
    pq, best, n = [(h(st), 0, st)], {st: 0}, 0
    while pq:
        f, g, u = heapq.heappop(pq)
        if g > best[u]: continue
        n += 1                              # nodes expanded
        if u == go: return g, n
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            v = (u[0] + dx, u[1] + dy)
            if 0 <= v[0] < 5 and 0 <= v[1] < 7 and W[v[0]][v[1]] != "#":
                if g + 1 < best.get(v, 99):
                    best[v] = g + 1
                    heapq.heappush(pq, (g + 1 + h(v), g + 1, v))
man = lambda p: abs(p[0] - 4) + abs(p[1] - 6)   # never overestimates
print("UCS", astar(lambda p: 0))
print("A* ", astar(man))
# UPDATE: A* expands fewer nodes, same cost
'''
A2B='''
import heapq
g = {"S": [("A", 1), ("B", 2)], "A": [("G", 5)], "B": [("G", 2)], "G": []}
def astar(h):
    pq = [(h["S"], 0, "S")]
    while pq:
        f, c, u = heapq.heappop(pq)
        if u == "G": return c
        for v, w in g[u]: heapq.heappush(pq, (c + w + h[v], c + w, v))
print(astar({"S": 0, "A": 0, "B": 0, "G": 0}))    # admissible
print(astar({"S": 0, "A": 0, "B": 10, "G": 0}))   # B really costs 2
# UPDATE: overestimating h can hide the best path
'''
A3='''
leaves = [3, 5, 6, 9, 1, 2, 0, -1]      # depth 3, branching 2
cnt = [0, 0]
def mm(i, d, mx):                       # plain minimax
    if d == 3: cnt[0] += 1; return leaves[i]
    vals = [mm(2*i + k, d + 1, not mx) for k in (0, 1)]
    return max(vals) if mx else min(vals)
def ab(i, d, mx, a, b):                 # alpha-beta: skip hopeless branches
    if d == 3: cnt[1] += 1; return leaves[i]
    best = -99 if mx else 99
    for k in (0, 1):
        v = ab(2*i + k, d + 1, not mx, a, b)
        if mx: best = max(best, v); a = max(a, v)
        else: best = min(best, v); b = min(b, v)
        if a >= b: break                # prune
    return best
print(mm(0, 0, True), ab(0, 0, True, -99, 99))
print("leaves looked at:", cnt)
# UPDATE: best move ordering gives O(b^(d/2))
'''
A4='''
from itertools import product
def entails(kb, q):               # KB entails q if q holds in every model of KB
    for P, Q in product([False, True], repeat=2):
        if kb(P, Q) and not q(P, Q): return False
    return True
imp = lambda a, b: (not a) or b   # a -> b
kb = lambda P, Q: imp(P, Q) and P
print(entails(kb, lambda P, Q: Q))          # modus ponens
print(entails(lambda P, Q: imp(P, Q), lambda P, Q: Q))   # without P?
print(imp(False, True), imp(False, False))  # false implies anything
# UPDATE: n symbols means 2**n models to check
'''
A5='''
people = ["ann", "bob", "cy"]
loves = {("ann", "bob"), ("bob", "cy"), ("cy", "ann")}
L = lambda x, y: (x, y) in loves
every_loves_someone = all(any(L(x, y) for y in people) for x in people)
someone_loved_by_all = any(all(L(x, y) for x in people) for y in people)
print(every_loves_someone, someone_loved_by_all)   # forall-exists vs exists-forall
def unify(a, b):                  # lower-case = variable
    if a == b: return {}
    if a.islower(): return {a: b}
    if b.islower(): return {b: a}
    return None
print(unify("x", "ann"), unify("ann", "bob"))
# UPDATE: quantifier order changes the meaning
'''
A6='''
import random
random.seed(1)
PB, PE = 0.001, 0.002
PA = {(1,1): .95, (1,0): .94, (0,1): .29, (0,0): .001}
PJ, PM = {1: .9, 0: .05}, {1: .7, 0: .01}
def joint(b, e, a, j, m):
    p = (PB if b else 1-PB) * (PE if e else 1-PE)
    p *= PA[(b,e)] if a else 1 - PA[(b,e)]
    p *= (PJ[a] if j else 1-PJ[a]) * (PM[a] if m else 1-PM[a])
    return p
num = sum(joint(1,e,a,1,1) for e in (0,1) for a in (0,1))
den = sum(joint(b,e,a,1,1) for b in (0,1) for e in (0,1) for a in (0,1))
print(round(num / den, 3))        # exact: sum out e and a
w1 = w0 = 0.0                     # likelihood weighting: fix J=M=1
for _ in range(100000):
    b = random.random() < PB; e = random.random() < PE
    a = random.random() < PA[(b, e)]
    wt = PJ[a] * PM[a]            # weight = how well evidence fits
    if b: w1 += wt
    w0 += wt
print(round(w1 / w0, 2))
# UPDATE: more samples, estimate closer to exact
'''
WA1='''
leaves = [3, 5, 2, 9]
a, b = -99, 99
v1 = min(leaves[0], leaves[1])
a = max(a, v1)
v2 = leaves[2]
print(a, v2)
'''
