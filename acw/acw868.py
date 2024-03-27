def prime(n): #筛合数的倍数
	st = [False] * (n + 10) #是否被筛掉
	prime = []
	for i in range(2,n + 1):
		if not st[i]: #没有被筛过 -> 质数
			prime.append(i)
		j = i * 2
		while j <= n:
			st[j] = True
			j += i
	return prime
def prime_1(n): #筛合数的倍数
	st = [False] * (n + 10)
	prime = []
	for i in range(2, n + 1):
		if not st[i]:
			prime.append(i)
			j = i * 2
			while j <= n:
				st[j] = True
				j += i
	return prime
def prime_2(n):
	st = [False] * (n + 10)
	prime = []
	for i in range(2, n + 1):
		if not st[i]:
			prime.append(i)
		for j in prime:
			if j * i > n:
				break
			st[j * i] = True
			if i % j == 0:
				break
	return prime

n = int(input())
pr = prime_2(n)
print(len(pr))