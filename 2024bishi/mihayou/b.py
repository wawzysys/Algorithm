s = input()
n = len(s)

yuanyin = [0] * n
fu = [0] * n
y = "aeiou"

for i, c in enumerate(s):
	if c in y:
		yuanyin[i] += 1
	else:
		fu[i] += 1

for i in range(1, n):
	yuanyin[i] += yuanyin[i - 1]
	fu[i] += fu[i - 1]
	
ans = 0

for i in range(0, n - 1):
	lasty = yuanyin[n - 1] - yuanyin[i]
	lastf = fu[n - 1] - fu[i]
	if abs(yuanyin[i] - fu[i]) == abs(lasty - lastf):
		ans += 1
print(ans)