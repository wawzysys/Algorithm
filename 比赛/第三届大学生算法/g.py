x, y, z = map(int, input().split())
def f(x):
    return x * (x + 1) // 2

print(f(x)*f(y)*f(z) % 998244353)