import sys
sys.setrecursionlimit(1000000)
n, q = map(int, input().split())
g = [input() for _  in range(n)]
qs = input().split()
from functools import lru_cache
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
res = []
for s in qs:
    m = len(s)
    found = False
    @lru_cache(None)
    def dfs(x,y,p,mask):
        if p == m:
            return True
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and g[nx][ny]==s[p]:
                pos = nx*n + ny
                if not mask & (1<<pos):
                    if dfs(nx,ny,p+1, mask | (1<<pos)):
                        return True
        return False
    for i in range(n):
        for j in range(n):
            if g[i][j]==s[0]:
                pos = i*n + j
                if dfs(i,j,1,1<<pos):
                    found = True
                    break
        if found:
            break
    res.append("Yes" if found else "No")
    dfs.cache_clear()
print(' '.join(res))
