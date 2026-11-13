M1='''
xs = [1, 2, 3, 4, 5]                      # hours studied
ys = [2.1, 3.9, 6.2, 7.8, 10.1]           # marks / 10
n = len(xs)
mx, my = sum(xs) / n, sum(ys) / n         # means
w = sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / sum((x-mx)**2 for x in xs)
b = my - w * mx                           # line passes through the means
pred = [w * x + b for x in xs]
sse = sum((y - p)**2 for y, p in zip(ys, pred))   # squared errors
sst = sum((y - my)**2 for y in ys)        # spread around the mean
print(round(w, 3), round(b, 3), round(1 - sse / sst, 4))  # slope, bias, R2
# UPDATE: R2 near 1 = line explains the data
'''
M2='''
xs = [1, 2, 3, 4, 5]
ys = [2.1, 3.9, 6.2, 7.8, 10.1]
w, b, lr = 0.0, 0.0, 0.02                 # start anywhere; lr = step size
for epoch in range(3000):                 # UPDATE: more epochs = closer
    gw = gb = 0
    for x, y in zip(xs, ys):
        err = (w * x + b) - y             # prediction - truth
        gw += err * x                     # slope of the loss wrt w
        gb += err                         # slope of the loss wrt b
    w -= lr * gw / len(xs)                # step downhill
    b -= lr * gb / len(xs)
print(round(w, 3), round(b, 3))
'''
M3='''
TP, FP, FN, TN = 40, 10, 20, 930          # confusion matrix, 1000 cases
acc = (TP + TN) / 1000                    # overall correct
prec = TP / (TP + FP)                     # of predicted +, how many right
rec = TP / (TP + FN)                      # of real +, how many found
f1 = 2 * prec * rec / (prec + rec)        # balance of the two
print(acc, round(prec, 3), round(rec, 3), round(f1, 3))
print("always say no:", (FP + TN) / 1000) # accuracy of a useless model
import math
sigmoid = lambda z: 1 / (1 + math.exp(-z))   # logistic regression output
print(round(sigmoid(0), 2), round(sigmoid(2), 3), round(sigmoid(-2), 3))
'''
M4='''
import math
def H(counts):                            # entropy of class counts
    n = sum(counts)
    return -sum(c / n * math.log2(c / n) for c in counts if c)
parent = H([9, 5])                        # 9 yes, 5 no
split = {"sunny": [2, 3], "overcast": [4, 0], "rain": [3, 2]}
child = sum(sum(c) / 14 * H(c) for c in split.values())
print(round(parent, 3), round(child, 3), round(parent - child, 3))
gini = lambda c: 1 - sum((x / sum(c))**2 for x in c)
print(round(gini([9, 5]), 3))             # gini of the parent
# gain = parent entropy - weighted child entropy; pick the biggest
'''
M5='''
w, b = (0.5, 0.5), -1.0                   # hyperplane  0.5x + 0.5y - 1 = 0
pts = [((2, 2), 1), ((3, 3), 1), ((0, 0), -1), ((-1, -1), -1)]
for (x, y), label in pts:
    f = w[0] * x + w[1] * y + b           # signed score
    hinge = max(0, 1 - label * f)         # 0 = safely outside the margin
    print((x, y), label, f, hinge)
print("margin width", round(2 / (w[0]**2 + w[1]**2) ** 0.5, 3))
# only points with label*f = 1 (support vectors) fix the line
phi = lambda x: (x, x * x)                # kernel idea: add a new feature
print([(x, x * x > 4) for x in (-3, -1, 0, 1, 3)])  # outer = True
'''
M6='''
import math, random
random.seed(3)
sg = lambda z: 1 / (1 + math.exp(-z))
H = 4                                     # hidden units
W1 = [[random.uniform(-1, 1) for _ in range(3)] for _ in range(H)]
W2 = [random.uniform(-1, 1) for _ in range(H + 1)]
data = [((0,0),0), ((0,1),1), ((1,0),1), ((1,1),0)]   # XOR
def fwd(x):
    h = [sg(w[0]*x[0] + w[1]*x[1] + w[2]) for w in W1]
    return h, sg(sum(W2[i]*h[i] for i in range(H)) + W2[H])
for epoch in range(8000):                 # UPDATE: more epochs, better fit
    for x, y in data:
        h, p = fwd(x)
        d2 = (p - y) * p * (1 - p)        # output error signal
        for i in range(H):
            d1 = d2 * W2[i] * h[i] * (1 - h[i])   # pushed back (backprop)
            W2[i] -= 0.5 * d2 * h[i]
            W1[i][0] -= 0.5 * d1 * x[0]
            W1[i][1] -= 0.5 * d1 * x[1]
            W1[i][2] -= 0.5 * d1
        W2[H] -= 0.5 * d2
print([round(fwd(x)[1]) for x, y in data])
'''
M7='''
xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [1.2, 3.1, 2.0, 4.9, 3.3, 6.4, 5.0, 7.9]
def knn(train, x, k):                     # average of k nearest y
    near = sorted(train, key=lambda p: abs(p[0] - x))[:k]
    return sum(p[1] for p in near) / k
data = list(zip(xs, ys))
for k in (1, 3, 5):
    tr = sum((knn(data, x, k) - y)**2 for x, y in data) / 8  # train error
    cv = 0
    for i in range(8):                    # leave-one-out cross-validation
        rest = data[:i] + data[i+1:]      # hide point i
        cv += (knn(rest, xs[i], k) - ys[i])**2
    print(k, round(tr, 3), round(cv / 8, 3))
# k=1 memorises: train error 0 but validation error is not
'''
M8='''
pts = [(1,1),(1.5,2),(3,4),(5,7),(3.5,5),(4.5,5),(3.5,4.5)]
cent = [(1, 1), (5, 7)]                   # starting centroids
for step in range(5):                     # UPDATE: stop when labels stop changing
    groups = [[], []]
    for p in pts:                         # assign to the nearest centroid
        d = [(p[0]-c[0])**2 + (p[1]-c[1])**2 for c in cent]
        groups[d.index(min(d))].append(p)
    cent = [(sum(p[0] for p in g)/len(g), sum(p[1] for p in g)/len(g))
            for g in groups]              # move centroid to the mean
print([(round(a, 2), round(b, 2)) for a, b in cent])
print([len(g) for g in groups])
'''
M8B='''
x = [2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]
y = [2.4,0.7,2.9,2.2,3.0,2.7,1.6,1.1,1.6,0.9]
n = len(x)
mx, my = sum(x)/n, sum(y)/n
a = sum((p-mx)**2 for p in x) / (n-1)     # var x
c = sum((q-my)**2 for q in y) / (n-1)     # var y
b = sum((p-mx)*(q-my) for p, q in zip(x, y)) / (n-1)  # covariance
tr, det = a + c, a * c - b * b
l1 = tr/2 + (tr*tr/4 - det) ** 0.5        # eigenvalues of the 2x2
l2 = tr/2 - (tr*tr/4 - det) ** 0.5        # covariance matrix
print(round(l1, 3), round(l2, 3), round(l1 / (l1 + l2), 3))
# PC1 keeps l1/(l1+l2) of the variance
'''
M9='''
import heapq, random
random.seed(1)
data = [(random.random(), random.random()) for _ in range(10000)]
q = (0.5, 0.5)
dist = lambda p: (p[0]-q[0])**2 + (p[1]-q[1])**2
ops = len(data)                           # 1 distance per point: O(n d)
near = heapq.nsmallest(3, data, key=dist) # top-3 in O(n log k)
print(ops, near == sorted(data, key=dist)[:3])
print("k-means per round: n*k*d =", 10000 * 3 * 2)
print("sort for a tree split: n log2 n =", round(10000 * 13.29))
# no training needed for KNN, but every query pays O(n)
'''
WM1='''
w, b = 0.5, 0.0                # weights start anywhere
x, y = 1.0, 1.0                # one training example
lr = 0.5                       # learning rate
for step in range(3):
    z = w * x + b              # forward: the prediction score
    err = z - y                # how wrong are we?
    gw = err * x               # slope of the loss wrt w
    w = w - lr * gw            # step AGAINST the slope
    print(step + 1, round(z, 3), round(w, 3))
'''
WM2='''
pts = [1, 2, 9, 10]            # 1-D data, want 2 clusters
c1, c2 = 1, 10                 # starting centroids
g1 = []
g2 = []
for p in pts:                  # ASSIGN each point to nearest centroid
    if abs(p - c1) <= abs(p - c2):
        g1.append(p)
    else:
        g2.append(p)
c1 = sum(g1) / len(g1)         # UPDATE: centroid = mean of group
c2 = sum(g2) / len(g2)
print(g1, g2, c1, c2)
'''
