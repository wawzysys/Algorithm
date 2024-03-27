def Multiplicative_inverse(a: int, b: int, p: int) -> int:
    return a*pow(b, p-2, p)%p

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc
global a
a = 0

dic = {}
@bootstrap
def dfs(n):
    global a
    a += 1
    if n in dic:
        yield  dic[n]
    if n == 0:
        yield 0

    min_count = float('inf')
    i = 1
    while i*i <= n:
        t = ( yield dfs(n - i*i)) + 1
        min_count = min(min_count, t)
        i += 1
    dic[n] = min_count
    yield min_count

# 使用记忆化搜索所需的最少平方数
min_squares_dfs = dfs(9999)
print(min_squares_dfs)
print(a)
