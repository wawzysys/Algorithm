n = int(input())
from collections import *
for _ in range(n):
	s = input()
	# print(s,end=' ')
	num = defaultdict(int)
	for x in s:
		num[x] += 1
	num0 = num['0']
	num1 = num['1']
	if len(s) == 1:
		print(1)
		continue
	if num0  == num1:
		print(0)
		continue
	ans  = 0
	res  = 0
	if num0 > num1:
		for i in range(len(s)):
			if s[i] == '0':
				ans += 1
			if ans >  num1 and s[i] == '0':
				print(len(s) - i )
				break
	if num1 > num0:
		for i in range(len(s)):
			if s[i] == '1':
				ans += 1
			if ans > num0 and s[i] == '1':
				print(len(s) - i )
				break
	# print(res)