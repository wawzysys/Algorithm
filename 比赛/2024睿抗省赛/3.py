# wm....mw
# .w..ww..
# ..wm.wwm
# w.w....w
# .m.c.m..
# w.....w.
def f():
    n, m = map(int, input().split())
    pre_grid = [list(input()) for _ in range(n)]
    pre_coid = [pre_grid[i].copy() for i in range(n)]
    for i in range(n):
        for j in range(m):
            if pre_coid[i][j] == 'w':
                pre_coid[i][j] = 'c'
    for i in range(n):
        for j in range(m):
            if pre_grid[i][j] == 'm':
                for x in range(max(0, i - 1), min(i + 2, n)):
                    for y in range(max(0, j - 1), min(j + 2, m)):
                        if pre_coid[x][y] == 'c':
                            pre_coid[x][y] = 'w'
    er_x = -1
    er_y = -1
    for i in range(n):
        for j in range(m):
            if pre_grid[i][j] != pre_coid[i][j]:
                er_x = i
                er_y = j
                break
    print(er_x, er_y)
    if er_x == -1:
        print("Too cold!")
        return
    ans = []
    def check(x, y):
        if pre_grid[x][y] != '.':
            return False
        for i in range(max(0, x - 1), min(x + 2, n)):
            for j in range(max(0, y - 1), min(y + 2, m)):
                if pre_grid[i][j] == 'c' and (i != er_x and j != er_y):
                    return False
        return True
    ans = []
    for i in range(max(er_x - 1, 0), min(er_x + 2, n)):
        for j in range(max(er_y - 1, 0), min(er_y + 2, m)):
            if check(i, j):
                ans.append([i, j])
    ans.sort()
    for i, j in ans:
        print(i + 1, j + 1)



    # for i in range(n):
    #     print(*pre_grid[i])
    # print()
    # for i in range(n):
    #     print(*pre_coid[i])
f()