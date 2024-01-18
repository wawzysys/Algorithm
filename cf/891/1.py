import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import *
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def bomb_bricks(n, m, k, bombs):
    matrix = [['*' for _ in range(m)] for _ in range(n)]
    cnt = [0  for _ in range(m)]
    for x, y in bombs:
    	if x > cnt[y - 1]:
    		cnt[y - 1] += 1
    for i in range(m):
    	for j in range(cnt[i]):
    		matrix[j][i] = '.'

    for row in matrix:
    	print(''.join(row))

def solve():
	n, m, k = mint()
	bombs = []
	for i in range(k):
		x, y = mint()
		bombs.append((x,y))
	bomb_bricks(n, m, k, bombs)



	






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()