N = 10**6 + 10
def check(num, n, r, d, s, t) -> bool:
    sub = [0] * (N + 1)
    for i in range(num):
        sub[s[i]] += d[i]
        sub[t[i] + 1] -= d[i]
        need = [0] * (N + 1)
    for i in range(1, n + 1):
        need[i] = need[i - 1] + sub[i]
        if need[i] > r[i]:
            return True
    return False
r = [0] * (N)
d = [0] * (N)
s = [0] * (N)
t = [0] * (N)
if __name__ == '__main__':
    print(1)
    n, m = map(int, input().split())
    temp_r = list(map(int, input().split()))
    for i in range(1, n + 1):
        r[i] = temp_r[i - 1]
    for i in range(m):
        d[i], s[i], t[i] = map(int, input().split())
    print(check(m, n, r, d, s, t))
