from collections import Counter

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n, k = mint()
    a = lint()
    mp = Counter(a)
    mp = dict(sorted(mp.items(), key=lambda x: -x[1]))
    ans, last, cnt = 0, n, 0 
    for v, c in mp.items():
        if last + cnt * c >= k:
            ans = max(v, ans)
        last, cnt = last - c, cnt + 1
    print(ans)
t = sint()
for _ in range(t):
	solve()	
