sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

n = sint()
elements = lint()
kk = sint()

m = [0] * (kk + 1)
res  = 0

for el in elements:
    re = el % kk
    m[re] = m[re] + 1
    res = max(res, m[re])

elements.sort()

for el in elements:
    if m[el % kk] == res:
        print(el)
        break