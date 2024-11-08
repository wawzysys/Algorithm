import sys
import math

def f(x):
    fa = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            fa[d] = fa.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        fa[x] = fa.get(x, 0) + 1
    return fa

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split())) 
    fa = f(x)
    req = fa.copy()
    current = {p:0 for p in fa}
    segments = 1
    for num in a:
        for p in fa:
            count =0
            temp = num
            while temp % p ==0:
                count +=1
                temp//=p
            current[p] += count
        dis = True
        for p in fa:
            if current[p] < req[p]:
                dis = False
                break
        if dis:
            segments +=1
            current = {}
            for p in fa:
                count =0
                temp = num
                while temp % p ==0:
                    count +=1
                    temp//=p
                current[p] = count
    print(segments)

main()
