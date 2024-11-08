
n = int(input())
g = []
for _ in range(2):
    r = list(map(int, input().split()))
    g.append(r)
from math import inf


dpMax = [[[-inf] * 2 for _ in range(4)] for _ in range(n)]
dpMin = [[[inf] * 2 for _ in range(4)] for _ in range(n)]

dpMax[n - 1][3][1] = g[0][n - 1] + g[1][n - 1]
dpMax[n - 1][2][1] = g[1][n - 1]

dpMin[n - 1][3][1] = g[0][n - 1] + g[1][n - 1]
dpMin[n - 1][2][1] = g[1][n - 1]


for i in range(n - 2, -1, -1):
    for j in range(3, -1, -1):
        for k in (0, 1):
            if j & (1 << k) != 0:
                dpMin[i][j][k] = min(dpMin[i][j][k], dpMax[i + 1][(1 << k)][k] + g[k][i]) 
                dpMax[i][j][k] = max(dpMax[i][j][k], dpMin[i + 1][(1 << k)][k] + g[k][i])
                if j - (1 << k) == 0:
                    tk = 1 - k
                    dpMin[i][j][k] = min(dpMin[i][j][k], dpMax[i][3][tk] + g[k][i])
                    dpMax[i][j][k] = max(dpMax[i][j][k], dpMin[i][3][tk] + g[k][i])
print (dpMin[0][1][0])