n, m = map(int, input().split())
Gi = [float(input()) for _ in range(n)]
Gi.sort()
def is_possible(k):
    count = 1
    last_angle = Gi[0]
    for i in range(1, n):
        diff = Gi[i] - last_angle
        if diff < 0:
            diff += 360
        if diff >= k - 1e-8:
            count += 1
            last_angle = Gi[i]
            if count == m:
                return True
    diff = (Gi[0] + 360) - last_angle
    if diff >= k - 1e-8:
        count += 1
        if count >= m:
            return True
    return count >= m

L = 0.0
R = 180.0
epsilon = 1e-5
while R - L > epsilon:
    mid = (L + R) / 2
    if is_possible(mid):
        L = mid
    else:
        R = mid

k_best = L
a = m
k = k_best
tep_k = -1
cha = 1e9
for i in range(n):
    for j in range(n):
        if abs(Gi[j] - Gi[i] - k_best) < cha:
            cha = abs(Gi[j] - Gi[i] - k_best)
            k = Gi[j] - Gi[i]
    
D = (180 * a + k - 180) / (360 * m) + 0.5
if k == 0:
    k = 180
print(f"{k:.5f}")
print(f"{a}")
