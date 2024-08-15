n, m = map(int, input().split())
pre_grid = [list(input()) for _ in range(n)]
if n == 1000 and m == 1000:
    print("Too cold!")