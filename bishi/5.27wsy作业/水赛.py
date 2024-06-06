#10
# def fun(a, *, b):
#     print(b)
# fun(1, 2, 3, 4)
# 11
str = "hello world"
suffix = 'python'
print(str.endswith(suffix))
#13
lists = [1, 1, 2, 3, 4, 5]
lists.pop(1)#?
lists.extend([7, 8, 9])
print(lists)
#14
def fn():
    t = []
    i = 1
    while i < 4:
        t.append(lambda x : print(i * x, end = ','))
        i += 1
    return t
for f in fn():
    f(3)
#15
def dec (f):
    n = 3
    def wrapper (*args, **kw) :
        return f(*args, **kw) * n
    return wrapper
@dec
def foo (n) :
    return n * 2
print(foo(2))

#16
class Foo:
    def __init__(self):
        pass

    def __getitem__(self, pos):
        return list(range(0, 30, 10))[pos]

foo = Foo()
for i in foo:
    print(i)
# print(len(f))
#17
def func(a, i, j):
    if i < j:
        func(a, i + 1, j - 1)
        a[i], a[j] = a[j], a[i]

def main():
    a = [10, 6, 23, -90, 0, 3]
    func(a, 0, len(a) - 2)
    for i in range(6):
        print(a[i])

main()

#19
lis = [1,2,3,4,5,6,]
print(lis[-1:1:-1])
#21
n1 = [1, 2, 5, 3, 5]
n1.append(4)
n1.insert(0, 7)#
n1.sort()
print(n1)
#22
str1 = ''
str2 = ' '
if not str1:
    print(0)
#23
one = (1,2)
two = ("aa", "bb")
print(one+two)
#24
tmp = dict.fromkeys(['a', ''], 42)
print(tmp)

#35
def func(lst):
    return [i for i in lst if isinstance(i, int)]

mixed_list = [1, 'a', 2, 'b', 3, 'c']
filtered_list = func(mixed_list)
print(filtered_list)

#36
def some_func(a, b, *args, **kwargs):
    return a + b

print(some_func(1, 2, 3, 4, x=5, y=6))
# 定义函数 some_func：

# a 和 b 是位置参数。
# *args 用于捕获所有额外的未命名位置参数。
# **kwargs 用于捕获所有额外的关键字参数。

def outer_function(x):
    def inner_function(y):
        return x * y
    return inner_function

double = outer_function(2)
triple = outer_function(3)

print(double(50))
print(triple(50))
# 创建 double 和 triple 函数：

# python
# 复制代码
# double = outer_function(2)
# triple = outer_function(3)
# double 是 outer_function 调用时 x 为 2 时返回的 inner_function，因此 double(y) 的行为是 2 * y。
# triple 是 outer_function 调用时 x 为 3 时返回的 inner_function，因此 triple(y) 的行为是 3 * y。

img1 = [12, 34, 56]
img2 = [1, 2, 4, 5]

def test():
    global img1
    img1 = img2
    print(img1)

test()
print(img1)
