import math
n, m = map(int, input().split())
k = math.ceil(n * 1.0 / m)
matrix = [[0 for _ in range(k)] for _ in range(m)]
step = 1
x, y = 0, 0
while step <= n:
    while y < k and matrix[x][y] == 0 and step <= n:
        matrix[x][y] = step
        step += 1
        y += 1
    y -= 1
    x += 1

    while x < m and matrix[x][y] == 0 and step <= n:
        matrix[x][y] = step
        step += 1
        x += 1
    x -= 1
    y -= 1

    while y >= 0 and matrix[x][y] == 0 and step <= n:
        matrix[x][y] = step
        step += 1
        y -= 1
    y += 1
    x -= 1

    while x >= 0 and matrix[x][y] == 0 and step <= n:
        matrix[x][y] = step
        step += 1
        x -= 1
    x += 1
    y += 1

for i in range(m):
    for j in range(k):
        if matrix[i][j] == 0:
            print("*", end="")
        else:
            print(matrix[i][j], end="")
        if j < k - 1:
            print(" ", end="")
    print("")
