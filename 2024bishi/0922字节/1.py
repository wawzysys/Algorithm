n, k = map(int, input().split())
s = input().strip()
f = [0] * n
sum_f = 0

# Initialize flip flags
for i in range(n):
    if s[i] == '1':
        f[i] = 1
        sum_f += 1

# Adjust flips if sum_f > k
if sum_f > k:
    for i in range(n - 1, -1, -1):
        if f[i] == 1:
            f[i] = 0
            sum_f -= 1
            if sum_f == k:
                break

# Adjust parity if necessary
if (k - sum_f) % 2 == 1:
    f[-1] = 1 - f[-1]
    sum_f += 1 if f[-1] == 1 else -1

# Remaining flips
rem = k - sum_f
if rem < 0 or rem % 2 != 0:
    pass  # Remaining flips are adjusted through even flips

# Apply flips to get the result
result = []
for i in range(n):
    s_i = int(s[i])
    s_i_prime = s_i ^ f[i]
    result.append(str(s_i_prime))

print(''.join(result))
