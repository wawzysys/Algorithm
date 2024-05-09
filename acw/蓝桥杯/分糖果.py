ans = 0
def dfs(x, n, m):
	global ans
	if x == 7:
		if n == 0 and m == 0:
			ans += 1
		return 
	t = 7 - x
	if n + m < 2 * t or n + m > 5 * t:
		return
	for i in range(n + 1):
		for j in range(m + 1):
			if 2 <= i + j <= 5:
				dfs(x + 1, n - i, m - j)
dfs(0, 9, 16)
print(ans)

