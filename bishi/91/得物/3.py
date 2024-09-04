from math import factorial

def solve(k, m, n):

    if k < m + n:
        print(0)
        return 
    
    paths = factorial(m + n) // (factorial(m) * factorial(n))
    print(paths)

k = int(input())
m = int(input())
n = int(input())


solve(k, m, n)