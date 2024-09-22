n, m = map(int, input().split())
Gi = [int(float(input()) * 1e5 + 0.5) for _ in range(n)]
Gi.sort()

def is_possible(k):
    count = 1
    last_angle = Gi[0]
    for i in range(1, n):
        diff = Gi[i] - last_angle
        if diff >= k:
            count += 1
            last_angle = Gi[i]
            if count == m:
                return True
    diff = Gi[0] + 36000000 - last_angle
    if diff >= k:
        count += 1
        if count >= m:
            return True
    return count >= m

L = 0
R = 18000000
while L < R:
    mid = (L + R + 1) // 2
    if is_possible(mid):
        L = mid
    else:
        R = mid - 1

k_best = L
k = k_best / 1e5
a = m

D = (180 * a + k - 180) / (360 * m) + 0.5

print(f"{k:.5f}")
print(f"{a}")
