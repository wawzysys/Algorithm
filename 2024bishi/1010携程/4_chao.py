import sys

data = sys.stdin.read().split()

idx = 0
n = int(data[idx])
q = int(data[idx+1])
idx += 2

a = [0] + [int(x) for x in data[idx:idx + n]]

size = 4 * n + 4
tree = [[0,0,0] for _ in range(size)]

def push_up(i):
    left = tree[2 * i]
    right = tree[2 * i + 1]
    tree[i][2] = left[2] + right[2]
    for op in range(2):
        if left[2] % 2 == 1:
            if op == 0:
                tree[i][op] = left[0] & right[0]
            else:
                tree[i][op] = left[1] | right[1]
        else:
            if op == 0:
                tree[i][op] = left[0] | right[0]
            else:
                tree[i][op] = left[1] & right[1]
def build(i,l,r):
    if l == r:
        tree[i][0] = tree[i][1] = a[l]
        tree[i][2] = 1
        return
    m = (l+r)//2
    build(2*i,l,m)
    build(2*i+1,m+1,r)
    push_up(i)
def query(i,l,r,x,y):
    if x <= l and r <= y:
        return tree[i][:]
    m = (l+r)//2
    if y <= m:
        return query(2*i,l,m,x,y)
    elif x > m:
        return query(2*i+1,m+1,r,x,y)
    else:
        left = query(2*i,l,m,x,y)
        right = query(2*i+1,m+1,r,x,y)
        res_len = left[2] + right[2]
        res0 = res1 = 0
        if left[2] % 2 == 1:
            res0 = left[0] & right[0]
        else:
            res0 = left[0] | right[0]
        if left[2] % 2 == 1:
            res1 = left[1] | right[1]
        else:
            res1 = left[1] & right[1]
        return [res0,res1,res_len]

build(1,1,n)
output = []
for _ in range(q):
    if idx + 3 > len(data):
        parts = sys.stdin.readline().split()
        if not parts:
            sys.stdin.readline().split()
        op, l, r = map(int, parts)
    else:
        op = int(data[idx])
        l = int(data[idx+1])
        r = int(data[idx+2])
        idx += 3
    res = query(1,1,n,l,r)
    output.append(str(res[op-1]))
print('\n'.join(output))

