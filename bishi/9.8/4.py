import sys
from math import gcd
def fn(a, b, c, d):
    e = len(a)
    f = len(a[0])
    p = [[0] * (f + 1) for _ in range(e + 1)]
    
    for i in range(e):
        for j in range(f):
            m = gcd(a[i][j], b)
            m = 1 if m > 1 else 0
            p[i + 1][j + 1] = p[i + 1][j] + p[i][j + 1] - p[i][j] + m
    
    r = 0
    for x in range(e - c + 1):
        for y in range(f - d + 1):
            n = p[x + c][y + d] - p[x][y + d] - p[x + c][y] + p[x][y]
            if n == c * d:
                r += 1
    return r
def main():
    t = int(input())  
    for _ in range(t):
        k, l, q = map(int, input().split())     
        a = []
        for i in range(k):
            row = list(map(int, input().split()))
            a.append(row)
        for _ in range(q):
            h1, w1, v = map(int, input().split())
            result = fn(a, v, h1, w1)
            print(result)
main()