t = int(input())
from collections import *
dirs = defaultdict(list)
dirs["UP"] = [-1, 0]
dirs["DOWN"] = [1, 0]
dirs["RIGHT"] = [0, 1]
dirs["LEFT"] = [0, -1]
for _ in range(t):
    n = int(input())
    dir = input().split()
    begin_x, begin_y = 0, 0
    for c in dir:
        begin_x += dirs[c][0]
        if begin_x < 0:
            begin_x = 0
        if begin_x >= n:
            begin_x = n - 1
        begin_y += dirs[c][1]
        if begin_y < 0:
            begin_y = 0
        if begin_y >= n:
            begin_y = n - 1
    # print(begin_x, begin_y)
    print(begin_x * n + begin_y)
