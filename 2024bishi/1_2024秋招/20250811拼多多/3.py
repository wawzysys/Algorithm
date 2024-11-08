def solve(n, flowers):
    a = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = 1 if flowers[i - 1] == 1 else -1
        s[i] = s[i - 1] + a[i]
    v = 0
    vv = 0
    kk = 0
    k = 0
    for i in range(1, n + 1):
        kk = max(kk, s[i] - v)
        v = min(v, s[i])
        k = min(k, s[i] - vv)
        vv = max(vv, s[i])
    y = s[n] - k * 2
    x = s[n] - kk * 2
    res = 0
    
    if x >= 0:
        res = (x - y) // 2 + 1
    elif y <= 0:
        res = (x - y) // 2 + 1
    else:
        z = max(abs(x), abs(y))
        if y % 2 == 1:
            res = (z + 1) // 2
        else:
            res = z // 2 + 1
    return res
n = int(input())
flowers = list(map(int, input().split()))
print(solve(n, flowers))


# def solve_optimized(n, flowers):
#     count0 = [0] * (n + 1)
#     count1 = [0] * (n + 1)
#     for i in range(1, n + 1):
#         count0[i] = count0[i - 1] + (1 if flowers[i - 1] == 0 else 0)
#         count1[i] = count1[i - 1] + (1 if flowers[i - 1] == 1 else 0)
    
#     initial_diff = abs(count0[n] - count1[n])
    
#     beauties = set()
#     beauties.add(initial_diff)  
#     for l in range(1, n + 1):
#         for r in range(l, n + 1):
#             a = count0[r] - count0[l - 1]
#             b = count1[r] - count1[l - 1]
#             c = abs((count0[n] - a + b) - (count1[n] - b + a))
#             beauties.add(c)
    
#     return len(beauties)

# n = int(input())
# flowers = list(map(int, input().split()))
# print(solve_optimized(n, flowers))

# def solve(n, flowers):
#     count0 = [0] * (n + 1)
#     count1 = [0] * (n + 1)
#     for i in range(1, n + 1):
#         count0[i] = count0[i - 1] + (1 if flowers[i - 1] == 0 else 0)
#         count1[i] = count1[i - 1] + (1 if flowers[i - 1] == 1 else 0)
    
#     a = count0[n]
#     b = count1[n]
#     c = abs(a - b)
    
#     beauties = set()
#     beauties.add(c)  
    
#     for l in range(1, n + 1):
#         for r in range(l, n + 1):
#             d = count0[r] - count0[l - 1]
#             e = count1[r] - count1[l - 1]
#             f = a - d + e
#             g = b - e + d
#             h = abs(f - g)
#             beauties.add(h)
    
#     return len(beauties)
# n = int(input())
# flowers = list(map(int, input().split()))
# print(solve(n, flowers))
