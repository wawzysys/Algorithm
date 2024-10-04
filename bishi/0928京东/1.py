import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    import sys
    Q,*rest = map(int, sys.stdin.read().split())
    L=-10**18
    U=10**18
    for i in range(0,2*Q,2):
        M,D=rest[i],rest[i+1]
        L=max(L, M-D)
        U=min(U, M+D)
    print(U if L<=U else -1)
    
if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()