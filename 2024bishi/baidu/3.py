
from collections import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
	n = sint()
	cnt = defaultdict(list)
	mm = 10 ** 10
	ans = [""]
	for i in range(n):
		name, num = input().split()
		num = int(num)
		if name not in cnt:
			cnt[name] = [num, i]
		else:
			cnt[name] = [cnt[name][0] + num, i]
	cnt = sorted(cnt.items(), key = lambda x : (x[1][0],x[1][1]) )
	print(cnt[0][0])
	print(1000 + cnt[0][1][0])


if __name__ == '__main__':
    main();