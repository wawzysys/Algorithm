from math import factorial
#组合数
def solve(k, m, n):
    if k < m + n:
        print(0)
        return 
    paths = factorial(m + n) // (factorial(m) * factorial(n))
    #c(m+n,m)
    print(paths)

k = int(input())
m = int(input())
n = int(input())
solve(k, m, n)