from math import factorial

# 计算第n个Catalan数
def catalanr(n):
    return factorial(2*n) // (factorial(n+1) * factorial(n))

# 计算n=时的Catalan数
s = str(catalanr(10))
print(len(s))