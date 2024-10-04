import sys
import heapq
sint = lambda: int(sys.stdin.readline())
mint = lambda: map(int, sys.stdin.readline().split())
lint = lambda: list(map(int, sys.stdin.readline().split()))

class Node:
    def __init__(self, x, y, danger):
        self.x = x
        self.y = y
        self.danger = danger

    def __lt__(self, other):
        return self.danger > other.danger

def main():
    M, N = mint()
    a1, a2 = mint()
    b1, b2 = mint()
    
    g = []
    d = [[-1 for _ in range(N)] for _ in range(M)]
    inf = []
    
    for i in range(M):
        row = list(mint())
        g.append(row)
        for j in range(N):
            if g[i][j] == 2 or g[i][j] == 3:
                d[i][j] = 0
                inf.append((i, j))
    
    day = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while inf:
        day += 1
        D = [[0 for _ in range(N)] for _ in range(M)]
        q = []
        
        for x, y in inf:
            if g[x][y] == 2:
                danger = a2
            else:
                danger = a1
            heapq.heappush(q, Node(x, y, danger))
            D[x][y] = danger
        
        while q:
            node = heapq.heappop(q)
            x, y, danger = node.x, node.y, node.danger
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < M and 0 <= ny < N and g[nx][ny] != 1:
                    nd = danger - 1
                    if nd > 0 and D[nx][ny] < nd:
                        D[nx][ny] = nd
                        heapq.heappush(q, Node(nx, ny, nd))
        
        newInf = []
        for i in range(M):
            for j in range(N):
                if (g[i][j] == 4 or g[i][j] == 5) and d[i][j] == -1:
                    th = b2 if g[i][j] == 4 else b1
                    if D[i][j] >= th:
                        d[i][j] = day
                        newInf.append((i, j))
        
        for x, y in newInf:
            if g[x][y] == 4:
                g[x][y] = 2
            elif g[x][y] == 5:
                g[x][y] = 3
        
        inf = newInf
    
    for i in range(M):
        row_output = []
        for j in range(N):
            if g[i][j] == 0 or g[i][j] == 1:
                res = -1
            else:
                res = d[i][j]
            row_output.append(str(res))
        print(' '.join(row_output))

main()
