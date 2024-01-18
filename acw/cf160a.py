n =  int(input())
for _ in range(n):
	s = input()
	if len(s) == 1:
		print(-1)
	else:
		flag = 0
		for i in range(1,len(s)):
			a = s[:i]
			b = s[i:]
			if b[0] == "0":
				continue
			a = int(a)
			b = int(b)
			if a < b:
				flag = 1
				print(a,b)
				break
		if flag == 0:
			print(-1)
