def f(n, k, x, prices):
    di = [(price, abs(price - x)) for price in prices]
    
    di.sort(key=lambda item: (item[1], item[0]))
    
    cl = [di[i][0] for i in range(k)]
    
    cl.sort()
    
    return cl
n, k, x = map(int, input().split())
prices = list(map(int, input().split()))
result = f(n, k, x, prices)
print(" ".join(map(str, result)))