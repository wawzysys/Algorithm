t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == 1:
        print(0, end = ' ')
    if n == 2:
        print(m, end = ' ')
    if n > 2:
        print(2 * m, end = ' ')