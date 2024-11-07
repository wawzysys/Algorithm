n, m = map(int, input().split())
a = input().split()
b = input().split()
from collections import defaultdict
bit_count = defaultdict(int)
bit_sets = defaultdict(set)

for p in b:
    mask = 0
    for c in p:
        mask |= 1 << int(c, 16)
    bit_count[mask] += 1
    for i in range(16):
        if mask & (1 << i):
            bit_sets[i].add(mask)


res = []
for h in a:

    mask = 0
    has_AF = any(c in 'ABCDEF' for c in h) 
    if not has_AF:
        res.append(0)
        continue

    for c in h:
        mask |= 1 << int(c, 16)


    last_digit = int(h[-1], 16)
    total = sum(bit_count[w] for w in bit_sets[last_digit] if mask & w == w)

    res.append(total)
print(' '.join(map(str, res)))
