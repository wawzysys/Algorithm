#E题
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n ,m, L = map(int, input().split())
    kb = input().strip()
    tgt = input().strip()
    kb_pos = {c: i for i, c in enumerate(kb)}
    dists = [abs(kb_pos[tgt[i]] - kb_pos[tgt[i+1]]) for i in range(m-1)]
    max_mv = L
    prefix_len = 0
    for dist in dists:
        if dist <= max_mv:
            prefix_len += 1
            max_mv -= dist
        else:
            break
    print(min(m, prefix_len + 1))

if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()
