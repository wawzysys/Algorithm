# 假设city.csv文件内容如下:
# 巴哈马,巴林,孟加拉国,巴巴多斯
# 白俄罗斯,比利时,伯利兹
# 以下代码的输出结果是()
# f=open("city.csv","r")
# ls =f.read().split(",")
# f.close()
# print(ls)
# lis = [1, 3, 2]
# a = id(lis)
# lis = sorted(lis)
# b = id(lis)
# print(a == b)

# lis = [1, 3, 2]
# a = id(lis)
# lis += [4, 5]
# b = id(lis)
# print(a == b)

# def outer_function(x):
#     def inner_function(y):
#         return x * y
#     return inner_function

# result = outer_function(10)(5)
# print(result)


# def mysort(ss, flag):
#     if flag:
#         return sorted(ss, reverse=True)
#     else:
#         return sorted(ss, reverse=False)

# ss = [11, 22, 6, 21]
# print(mysort(ss, 2))  # flag 为 True，降序排序
# print(mysort(ss, 0)) # flag 为 False，升序排序


# def outer(fn):
#     print('outer')
#     def inner():
#         print('inner')
#         return fn()
#     return inner

# @outer
# def fun():
#     print('fun')

# # fun()
# name = "1"

# def f1():
#     print(name)

# def f2():
#     name = "2"

# f1()
# f2()
# f1()
# strs = 'abcd12efgqweqw'
# print(strs.upper().title())


# names = ["tom", "jerry", "tiger", "dragon"]
# lists = []
# for name in names:
#     if name.count('a') >= 1:
#         lists.append(name)
# print(lists)

# lis = [1, 2, 3, 4, 5, 6]
# print(lis[-1:1:-1])
# dicts ={}
# dicts[(1,'')]=({3,(4,5)})
# print(dicts)


# def f(x):
#     if x == 0:
#         return 1
#     elif x == 1:
#         return 1
#     else:
#         return x * f(x - 2)

# print(f(5))

# tmp = [1, 2, 3, 4, 5, 6]
# print(tmp[6::-2])

# one = (1, 2)
# two = ('aaa','bbb')
# print(one + two)


# tmp = dict.fromkeys(['a', ''], 42)
# print(tmp)


def some_func(a, b, *args, **kwargs):
    return a + b
print(some_func(1,2,3,4,x=5,y=6))

def foo(a, b=[]):
    b.append(a)
    return b
print(foo(11))
print(foo(22))
print(foo(33))

def outer_function(x):
    def inner_function(y):
        return x * y
    return inner_function

double = outer_function(2)
triple = outer_function(3)

print(double(50))  # Output: 100
print(triple(50))  # Output: 150

random(1,3)