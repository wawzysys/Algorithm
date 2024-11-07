MOD = 10**9 + 7

def modinv(a):
    return pow(a, MOD - 2, MOD)

n, m, q, t = map(int, input().split())
d = list(map(int, input().split()))

s1 = 0  # Number of Type A players (x >= t)
s2 = 0  # Number of Type B players (x < t)
for x in d:
    if x >= t:
        s1 += 1
    else:
        s2 += 1

if n >= t:
    player_type = 'A'
else:
    player_type = 'B'

max_n = 2 * (q + 1)
factorial = [1] * (max_n + 1)
inv_factorial = [1] * (max_n + 1)

for i in range(1, max_n + 1):
    factorial[i] = factorial[i - 1] * i % MOD
inv_factorial[max_n] = modinv(factorial[max_n])
for i in range(max_n, 0, -1):
    inv_factorial[i - 1] = inv_factorial[i] * i % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD

ans = 0
for p in range(0, q + 1):
    for a in range(0, min(p, s1) + 1):
        b = p - a
        if b < 0 or b > s2:
            continue
        # Tickets consumed before Mi Xiaoyou's turn
        t1 = min(a, m)
        t2 = max(0, a - m) + b
        r1 = m - t1  # Remaining Tier 1 tickets
        r2 = m - t2  # Remaining Tier 2 tickets
        can_get_ticket = False
        if player_type == 'A':
            if r1 > 0:
                can_get_ticket = True
            elif r2 > 0:
                can_get_ticket = True
        else:  # Type B
            if r2 > 0:
                can_get_ticket = True
        if can_get_ticket:
            ways = comb(s1, a) * comb(s2, b) % MOD
            ways = ways * factorial[a + b] % MOD
            ways = ways * factorial[q - (a + b)] % MOD
            ans = (ans + ways) % MOD

print(ans)
