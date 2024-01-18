import sys
sys.setrecursionlimit(1000000)
input=lambda:sys.stdin.readline().strip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n = sint()
	a = lint()
	ss = sum(a)
	if ss %  2 == 1:
		print("NO")
	else:
		print("YES")
	
if __name__ == '__main__':
	t=sint()
	for _ in range(t):
	    solve()

	# solve()