def solve(N, a):
    a.sort()
    cur = 0

    for pi, xi, di in a:
        if cur < xi:
            vi = xi
        else:
            offset = (cur - xi) % di
            if offset == 0:
                vi = cur
            else:
                vi = cur + di - offset

        cur = vi + 1

    return cur - 1


N = int(input())
num = []
for _ in range(N):
    a, b, c = map(int, input().split())
    num.append((a, b, c))
print(solve(N, num))
