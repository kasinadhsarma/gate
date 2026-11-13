DB1='''
import sqlite3
db = sqlite3.connect(":memory:")          # a throw-away database
db.executescript("""
create table emp(name, dept, sal);
insert into emp values ('Asha','CS',50), ('Ben','CS',70),
  ('Cara','EE',60), ('Dev','EE',NULL), ('Esh','ME',40);""")
q = """select dept, count(*), count(sal), avg(sal)
       from emp group by dept
       having count(*) > 1"""             # HAVING filters GROUPS
print(db.execute(q).fetchall())
# count(*) counts rows; count(sal) skips NULL; avg skips NULL
'''
DB2='''
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""create table emp(name, sal);
insert into emp values ('Asha',50), ('Dev',NULL);""")
print(db.execute("select count(*) from emp where sal = NULL").fetchone())
print(db.execute("select count(*) from emp where sal is NULL").fetchone())
# NULL = NULL is never true -> always write IS NULL
'''
DB3='''
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("pragma foreign_keys = on")    # sqlite needs this switch
db.executescript("""
create table dept(id integer primary key, name text unique);
create table emp(id integer primary key, d integer
  references dept(id) on delete cascade);
insert into dept values (1, 'CS');
insert into emp values (10, 1);""")
try:
    db.execute("insert into emp values (11, 99)")   # dept 99 missing
except Exception as e:
    print(e)                              # foreign key protects links
db.execute("delete from dept where id = 1")         # parent deleted
print(db.execute("select count(*) from emp").fetchone())  # child gone
'''
DB4='''
def closure(attrs, fds):                  # attribute closure X+
    result = set(attrs)
    changed = True
    while changed:                        # repeat until nothing grows
        changed = False
        for lhs, rhs in fds:
            if set(lhs) <= result and not set(rhs) <= result:
                result |= set(rhs)        # lhs known -> rhs known
                changed = True
    return "".join(sorted(result))
fds = [("A","B"), ("B","C"), ("CD","E")]  # A->B, B->C, CD->E
print(closure("A", fds), closure("AD", fds))
# closure(X) = ALL attributes  =>  X is a superkey
'''
DB5='''
from itertools import combinations
def closure(attrs, fds):
    r = set(attrs)
    while True:
        n = len(r)
        for l, h in fds:
            if set(l) <= r: r |= set(h)
        if len(r) == n: return r
fds = [("AB","C"), ("C","B")]             # AB->C, C->B
cols, keys = "ABC", []
for size in range(1, 4):                  # smallest subsets first
    for s in combinations(cols, size):
        if closure(s, fds) == set(cols) and not any(
                set(k) <= set(s) for k in keys):
            keys.append("".join(s))       # minimal superkey
print(keys)   # C->B: C is not a key -> violates BCNF
'''
DB6='''
import sqlite3, math
db = sqlite3.connect(":memory:")
db.execute("create table t(id integer, x integer)")
db.executemany("insert into t values (?,?)", [(i, i % 50) for i in range(1000)])
plan = lambda: [r[3] for r in db.execute(
    "explain query plan select * from t where x = 7")]
print(plan())                             # before: full scan
db.execute("create index ix on t(x)")     # UPDATE: index the column you filter
print(plan())                             # after: index search
n = 1_000_000
print(n, math.ceil(math.log2(n)), math.ceil(math.log(n, 100)))
# scan n | binary search log2 n | B+ tree (fan-out 100) height
'''
DB7='''
data = [10, 20, 30, 40, 100]
lo, hi = min(data), max(data)
minmax = [round((x - lo) / (hi - lo), 3) for x in data]  # -> [0,1]
mu = sum(data) / len(data)
sd = (sum((x - mu)**2 for x in data) / len(data)) ** 0.5
z = [round((x - mu) / sd, 3) for x in data]   # mean 0, sd 1
print(minmax)
print(z)
# UPDATE: outlier 100 squashes min-max; z-score also moves
'''
DB8='''
from itertools import combinations
dims = ["time", "product", "store"]
groups = []
for r in range(len(dims) + 1):            # every subset of dimensions
    for g in combinations(dims, r):
        groups.append(g)
print(len(groups), "group-bys for", len(dims), "dimensions")
print(groups[0], groups[1], groups[-1])
# CUBE = 2^n aggregates : roll-up goes DOWN the list
'''
DB9='''
R = [(i, i % 100) for i in range(1000)]
S = [(j, j * 2) for j in range(100)]
def nested(R, S):                         # compare every pair
    ops, out = 0, []
    for r in R:
        for s in S:
            ops += 1
            if r[1] == s[0]: out.append((r[0], s[1]))
    return ops, len(out)
def hashjoin(R, S):                       # build a dict, then probe
    table = {s[0]: s[1] for s in S}       # build: len(S) steps
    out = [(r[0], table[r[1]]) for r in R if r[1] in table]  # probe
    return len(S) + len(R), len(out)
print(nested(R, S), hashjoin(R, S))
'''
WD1='''
fds = [("A","B"), ("B","C")]
result = {"A"}                 # start with X = A
changed = True
while changed:                 # keep going until nothing is added
    changed = False
    for lhs, rhs in fds:
        if set(lhs) <= result and not set(rhs) <= result:
            result |= set(rhs) # we know lhs, so we know rhs
            changed = True
print(sorted(result))
'''
WD2='''
R = [("r1", 2), ("r2", 3), ("r3", 2)]    # (id, join key)
S = [(2, "x"), (3, "y")]                 # (join key, value)
table = {}
for k, v in S:                 # BUILD: put S into a dict
    table[k] = v
out = []
for rid, key in R:             # PROBE: look each R row up, O(1)
    if key in table:
        out.append((rid, table[key]))
print(out)
'''
