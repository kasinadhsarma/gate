LA1='''
def solve(A, b):               # solve A x = b
    n = len(A)
    for i in range(n):         # pivot row i
        for r in range(i + 1, n):      # rows below the pivot
            m = A[r][i] / A[i][i]      # multiplier to kill A[r][i]
            for c in range(i, n):
                A[r][c] -= m * A[i][c] # row r = row r - m*row i
            b[r] -= m * b[i]           # same on the right side
    x = [0] * n
    for i in range(n - 1, -1, -1):     # back-substitute: bottom row up
        s = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - s) / A[i][i]    # solve for x[i]
    return x
# UPDATE: a zero pivot A[i][i] needs a row swap first
print(solve([[1,1,1],[0,2,5],[2,5,-1]], [6,-4,27]))
'''
LA2='''
A = [[4, 1], [2, 3]]
v = [1, 0]                     # any starting vector
for _ in range(20):            # UPDATE: more rounds = more exact
    w = [A[0][0]*v[0] + A[0][1]*v[1],
         A[1][0]*v[0] + A[1][1]*v[1]]   # w = A times v
    big = max(abs(w[0]), abs(w[1]))     # biggest entry
    lam = big                  # this scale factor -> eigenvalue
    v = [w[0] / big, w[1] / big]        # shrink so it never explodes
print(round(lam, 4), [round(x, 3) for x in v])
'''
LA3='''
def matmul_count(n):
    ops = 0
    for i in range(n):         # loop 1: n times
        for j in range(n):     # loop 2: n times
            for k in range(n): # loop 3: n times
                ops += 1       # one multiply-add
    return ops                 # n * n * n = n^3
for n in (2, 4, 8, 16):        # UPDATE: try other sizes
    print(n, matmul_count(n))
'''
LA4='''
n = 1000
gauss = n**3 // 3              # eliminate once: about n^3/3
tri = n**2                     # triangular solve: n^2
print("factor once:", gauss)
print("each new b :", tri)
print("100 right sides, LU :", gauss + 100*tri)   # factor ONCE
print("100 right sides, redo:", 100*gauss)        # factor EVERY time
# UPDATE: change 100 to see LU win by more
'''
C1='''
def newton(f, df, x):          # f = curve, df = its slope
    for i in range(6):         # UPDATE: more steps, more digits
        x = x - f(x) / df(x)   # slide down the tangent to zero
        print(i + 1, round(x, 7))
# solve x*x - 2 = 0, start the guess at 1.0
newton(lambda x: x*x - 2, lambda x: 2*x, 1.0)
'''
C2='''
def bisect(f, lo, hi, eps=1e-6):   # f(lo)<0 and f(hi)>0
    steps = 0
    while hi - lo > eps:       # stop when the gap is tiny
        mid = (lo + hi) / 2    # look at the middle
        if f(mid) < 0:
            lo = mid           # root is in the upper half
        else:
            hi = mid           # root is in the lower half
        steps += 1             # each step halves the gap
    return round(lo, 5), steps
print(bisect(lambda x: x*x - 2, 1, 2))
'''
C3='''
def ternary(f, lo, hi):        # f has ONE valley
    for _ in range(60):
        a = lo + (hi - lo) / 3     # left third point
        b = hi - (hi - lo) / 3     # right third point
        if f(a) < f(b):
            hi = b             # valley is not right of b
        else:
            lo = a             # valley is not left of a
    return round(lo, 4)
print(ternary(lambda x: (x - 2)**2 - 1, 0, 5))
'''
C4='''
f = lambda x: x**3 - 6*x*x + 9*x + 1   # the curve
df = lambda x: 3*x*x - 12*x + 9        # its slope
x, lr = 2.5, 0.05              # start point, learning rate
for i in range(60):
    x -= lr * df(x)            # step AGAINST the slope = downhill
# UPDATE: lr too big = jumps past; too small = slow
print(round(x, 4), round(f(x), 4))
'''
P1='''
import random
random.seed(7)                 # same result every run
def same_birthday(n):
    days = [random.randrange(365) for _ in range(n)]  # n random days
    return len(set(days)) < n  # a repeat means fewer distinct days
trials = 20000                 # UPDATE: more trials, closer to truth
hits = sum(same_birthday(23) for _ in range(trials))
print(hits / trials)           # hits / trials = probability
'''
P2='''
def C(n, k):                   # n choose k
    row = [1] + [0] * k        # row[j] = ways to choose j
    for i in range(1, n + 1):  # add items one at a time
        for j in range(min(i, k), 0, -1):  # go BACKWARDS
            row[j] += row[j - 1]  # skip item + take item
    return row[k]
print(C(5, 2), C(10, 2), C(12, 2), C(30, 15))
'''
P3='''
import random
random.seed(1)
means = []
for _ in range(5000):          # 5000 experiments
    rolls = [random.randint(1, 6) for _ in range(30)]  # 30 dice
    means.append(sum(rolls) / 30)       # keep each average
mu = sum(means) / 5000         # mean of the averages
sd = (sum((m - mu)**2 for m in means) / 5000) ** 0.5
# UPDATE: change 30 to see the spread shrink as 1/sqrt(n)
print(round(mu, 3), round(sd, 3))
'''
P4='''
import random
random.seed(3)
def reservoir(stream, k):      # keep k random items
    keep = []
    for i, x in enumerate(stream):
        if i < k:
            keep.append(x)     # first k go straight in
        else:
            j = random.randint(0, i)   # random slot 0..i
            if j < k:          # chance is k/(i+1)
                keep[j] = x    # replace an old item
    return keep
print(reservoir(range(1000000), 3))
'''
P5='''
import random
random.seed(5)
def quickselect(a, k):         # k-th smallest, no full sort
    p = random.choice(a)       # random pivot
    lo = [x for x in a if x < p]   # smaller than pivot
    hi = [x for x in a if x > p]   # bigger than pivot
    eq = len(a) - len(lo) - len(hi)
    if k < len(lo): return quickselect(lo, k)  # answer is left
    if k < len(lo) + eq: return p              # pivot is it
    return quickselect(hi, k - len(lo) - eq)   # answer is right
a = random.sample(range(10**6), 10001)
print(quickselect(a, 5000) == sorted(a)[5000])
'''
W_LA1='''
A = [[1, 1], [2, -1]]          # x + y = 3 ; 2x - y = 0
b = [3, 0]                     # right-hand side
m = A[1][0] / A[0][0]          # multiplier: 2 / 1 = 2
for c in range(2):
    A[1][c] = A[1][c] - m * A[0][c]  # row2 = row2 - m*row1
b[1] = b[1] - m * b[0]         # same on the right side
y = b[1] / A[1][1]             # last row: -3y = -6
x = (b[0] - A[0][1] * y) / A[0][0]   # put y back into row 1
print(x, y)
'''
W_LA2='''
A = [[4, 1], [2, 3]]
v = [1, 0]                     # starting vector
for rnd in range(4):
    w = [A[0][0]*v[0] + A[0][1]*v[1],
         A[1][0]*v[0] + A[1][1]*v[1]]   # w = A times v
    big = max(w)               # biggest entry -> eigenvalue
    v = [w[0] / big, w[1] / big]        # shrink; keep direction
    print(round(big, 3), [round(q, 3) for q in v])
'''
W_C1='''
x = 1.0                        # first guess for sqrt(2)
for i in range(3):
    fx = x * x - 2             # height of the curve at x
    slope = 2 * x              # slope of the curve at x
    x = x - fx / slope         # jump to where the tangent hits 0
    print(i + 1, round(x, 5))
'''
W_C2='''
lo, hi = 1.0, 2.0              # root is between 1 and 2
for i in range(5):
    mid = (lo + hi) / 2        # test the middle
    if mid * mid < 2:
        lo = mid               # too small: move low end up
    else:
        hi = mid               # too big: move high end down
    print(lo, hi)              # the gap halves each time
'''
W_P1='''
row = [1, 0, 0]                # ways to choose 0, 1, 2 items
for i in range(1, 5):          # add item i (4 items total)
    for j in range(min(i, 2), 0, -1):  # backwards, so no reuse
        row[j] += row[j - 1]   # not take + take the new item
    print(i, row)
'''
W_P2='''
stream = [10, 20, 30, 40, 50, 60]
draws = {3: 1, 4: 4, 5: 0}     # pretend random draws
k = 3                          # slots to keep
keep = []
for i, x in enumerate(stream):
    if i < k:
        keep.append(x)         # first k always enter
    else:
        j = draws[i]           # random slot 0..i
        if j < k:
            keep[j] = x        # replace slot j
    print(i, keep)
'''
