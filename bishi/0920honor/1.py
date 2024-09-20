from collections import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def solve():
    n = sint()
    nums = lint()
    cnt = Counter(nums)
    ans = 0
    for c in cnt:
        if c * 2 in cnt:
            ans += cnt[c]
    print(ans)
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        solve()

