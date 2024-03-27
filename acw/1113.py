from collections import *
m, n = map(int, input().split())
grid = [list(input()) for i in range(n)]
st = [[0 for i in range(m)] for j in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()

def bfs(x, y):
	q.append([x, y])
	st[x][y] = 1
	count = 1
	while q:
		x, y = q.popleft()
		for k in range(4):
			xx = x + dx[k]
			yy = y + dy[k]
			if 0<=xx<n and 0<=yy<m and grid[xx][yy]=='.' and st[xx][yy]==0:
				q.append([xx, yy])
				st[xx][yy] = st[x][y] + 1
				count += 1
	return count

for i in range(n):
	for j in range(m):
		if grid[i][j] == '@':
			print(bfs(i, j))
			print(st)
			break
