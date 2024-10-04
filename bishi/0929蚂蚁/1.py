sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

q = sint()
for _ in range(q):
    n,k = mint()
    s = input()
    t = input()
    d = {}
    for i in range(n):
        c = i % k
        if c not in d:
            d[c] = [[],[]]
        d[c][0].append(s[i])
        d[c][1].append(t[i])
    ok = True
    for v in d.values():
        if sorted(v[0]) != sorted(v[1]):
            ok = False
            break
    print("Yes" if ok else "No")
