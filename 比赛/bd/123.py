# strs = ['apple', 'orange', 'pear', 'watermelon']
# dicts = {}
# for i in range(len(strs)):
#     dicts[i] = strs[i]
# print(dicts)

def dec(f):
    n = 3
    def wrapper(*args, **kw):
        return f(*args, **kw) * n
    return wrapper

@dec
def foo(n):
    return n * 2

print(foo(3))
print(foo(2))