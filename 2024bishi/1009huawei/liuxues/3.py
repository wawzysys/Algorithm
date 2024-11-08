n, m = map(int, input().split())
a = input().split()
b = input().split()
ws = {}
from collections import *
ww = defaultdict(int)
dd = defaultdict(set)
for p in b:
    w = 0
    for c in p:
        d = int(c,16)
        w |= 1<<d
    ww[w] +=1
    for i in range(16):
        if w&(1<<i):
            dd[i].add(w)
res = []
for h in a:
    s = 0
    for c in h:
        d = int(c,16)
        s |= 1<<d
    has_AF = False
    for c in h:
        if c in 'ABCDEF':
            has_AF = True
            break
    if not has_AF:
        res.append(0)
        continue
    ls = int(h[-1],16)
    total = 0
    for w in dd[ls]:
        if s & w == w:
            total += ww[w]
    res.append(total)
print(' '.join(map(str,res)))
