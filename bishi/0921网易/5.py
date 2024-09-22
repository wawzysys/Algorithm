n, m = map(int, input().split())
grid = [input() for _ in range(n)]

a = all(row == row[::-1] for row in grid)

b = grid == grid[::-1]

print('YES' if a else 'NO')
print('YES' if b else 'NO')
