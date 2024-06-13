---
title: python
cover: 'https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240128010140.png'
tags: python
abbrlink: b9ebdeb8
date: 2024-01-28 00:59:10
---
```python
bisect_left:>=
bisect_right:>
```
## dict
```python
dict = defaultdict(list)
# 设置无限大
dict = defaultdict(inf) 
```
## SortedDict
```python
dict = defaultdict(SortedDict)
```
## any
```python
if any(1 in row for row in grid):
    return -1
# 检查列表中是否有真值
print(any([0, False, 5]))  # True，因为5是真值

# 空列表中没有真值
print(any([]))  # False

# 字典在使用any时会检查键而不是值
print(any({0: "False", 1: "True"}))  # True，因为有一个真键1

# 空字典
print(any({}))  # False

# 检查列表中是否存在大于5的元素
nums = [1, 4, 6, 8]
print(any(n > 5 for n in nums))  # True
```
## copy
```python
#二位数组
import copy
pre_grid = copy.deepcopy(grid)##pre_grid 和 grid两者独立
pre_grid = grid ##两者不独立
pre_grid = grid.copy() ##两者不独立
# 使用.copy()方法对列表进行浅复制（shallow copy）时，这个方法只会创建列表
# 本身的一个新的副本，但是不会对列表中的子列表（即列表中的列表）进行深度复制。
# 这意味着，如果原始列表中包含了其他列表（如二维数组或矩阵），那么新列表和原
# 始列表中的子列表仍然是相同的对象（即它们在内存中的地址是相同的）。
# 因此，当您修改grid中的任何元素时，pre_color中相应的子列表元素也会被修改，
# 因为它们实际上是指向同一块内存地址。

```
### 一维数组
```python
a_copy = a.copy()#两者独立 
a_copy = a[:]#两者独立 使用切片
a_copy = a#两者不独立
#对于一维数组（列表），可以使用 .copy() 方法或切片操作 [:] 来创建一个浅复制。
# 对于一维数组，这两种方法都能有效地复制数组，因为一维数组不包含嵌套的列表，
# 所以“浅复制”已经足够用于创建一个完全独立的副本
# 修改副本中的元素不会影响原始数组。
```
## 可变对象
 * 可变对象（如列表、字典、集合等）则表现出“按引用传递”的特性。
 * 因为函数接收的参数是对象的引用，所以如果你在函数内部修改了一个可变对象（例如，添加、删除或者修改列表中的元素），
 * 那么这些修改会反映到原始对象上，因为实际上你和函数内部操作的是同一个对象。
 
## 不可变对象
 * 不可变对象（如**整数、浮点数、字符串、元组**等）看起来像是“按值传递”，因为它们的值不能被修改。
 * 如果你在函数内部试图改变一个不可变对象的值，实际上会创建一个新的对象，并将其绑定到函数内部的局部变量名上，而原始对象不会受到影响。

## def 函数参数
在Python中，所有的***函数参数***传递都可以视为“按对象引用传递”（pass by object reference）。这意味着函数内部接收到的是实际参数对象的引用，而不是对象的副本。这种传递方式的效果取决于对象本身是可变的（mutable）还是不可变的（immutable）。
### 不可变
```python
area = 0
def fun(area):
    area += 1
fun(area)
print(area) 
# 0
#area 不可变 
#函数fun中的area是一个局部变量，它仅在函数作用域内有效。尽管它与全局变量area同名，但它实际上是一个完全不同的变量。在fun函数内部修改area时，实际上是在修改这个局部变量，而不是全局变量area。因此，全局变量area的值不会因为调用fun函数而改变。
```
### Python中函数参数如何按引用传递（对于可变对象而言）
```python
area[0] = 0
def fun(area):
    area[0] += 1
fun(area)
print(area[0]) 
# 1
```
### 不可变对象 + global
```python
area = 0
def fun():
    global area  # 指明我们打算修改的是全局变量area
    area += 1
fun()
print(area)  
# 结果将是1，因为fun函数被调用，全局变量area被修改

```
### global
 * 使用`global`关键字在函数内部**声明全局变量**。
 * 当在函数内部修改全局变量时，如果不使用`global`关键字，
 * `Python`将会创建一个新的局部变量，而不是修改外部的全局变量。
 * 通过使用`global`关键字，可以明确指示Python在函数内部对全局变量进行修改。
```python
x = 5
def func():
    global x  # 指明我们要修改的是全局变量x
    x = 10
func()
print(x)  # 输出将是10，因为全局变量x被修改了
```
### nonlocal
 * `nonlocal`关键字用于在嵌套函数中声明非局部变量（即不属于这个函数，但也不是全局的变量）。
 * 这通常用于在嵌套函数中修改封闭作用域（enclosing scope，即嵌套函数外部的另一个函数内部）的变量。

```python
def outer():
    x = 5
    def inner():
        nonlocal x  # 指明我们要修改的是封闭作用域中的变量x
        x = 10
    inner()
    print(x)  # 输出将是10，因为封闭作用域中的变量x被修改了
outer()

```
### 使用注意事项
`global`和`nonlocal`关键主要用于复杂的场景，比如需要在多层嵌套的函数中修改外部变量的值。然而，过度使用这些关键字可能会导致代码难以理解和维护，因此应该谨慎使用。
如果可以通过其他方式（如返回值、类属性等）来实现相同的功能，通常这些方式会更加清晰和优雅。

## 嵌套函数
在Python中，嵌套函数可以访问其外部函数（父函数）作用域内的所有变量，无论这些变量是可变的还是不可变的。这种特性是由于Python的作用域和闭包的概念所决定的。当你在一个函数内定义另一个函数时，内部的函数（嵌套函数）可以访问外部函数的局部变量。

### 访问不可变变量
嵌套函数可以读取外部函数中定义的不可变变量（如整数、字符串、元组等），但不能直接修改它们。如果尝试修改，Python会在嵌套函数的局部作用域内创建一个同名的新变量，而不是修改外部函数的变量。这是因为不可变变量不能被更改，只能被替换。

示例：
```python
Copy code
def outer():
    x = 3  # 不可变变量
    def inner():
        print(x)  # 可以访问外部函数的变量x
    inner()

outer()
```
### 修改可变变量
对于可变变量（如列表、字典等），嵌套函数可以修改这些变量的内容，因为可变变量允许原地修改。

```python
Copy code
def outer():
    lst = [1, 2, 3]  # 可变变量
    def inner():
        lst.append(4)  # 修改外部函数的变量lst
    inner()
    print(lst)

outer()
```
### 使用nonlocal关键字
如果需要在嵌套函数中修改外部函数的不可变变量，可以使用nonlocal关键字。这样做可以明确地告诉Python解释器你打算修改的是嵌套作用域中的变量，而不是创建一个新的局部变量。
```python
python
Copy code
def outer():
    x = 3
    def inner():
        nonlocal x
        x = 5  # 修改的是外部函数的变量x
    inner()
    print(x)  # 输出5

outer()
```
在这个示例中，nonlocal关键字使得inner函数能够修改外部函数outer中定义的不可变变量x的值。
总结来说，嵌套函数能够访问父函数中定义的所有变量，无论它们是可变的还是不可变的。但要修改不可变变量，需要使用nonlocal关键字。

### 总结
修改不可变复杂一点......
修改可变，不用加入函数参数直接改！
```python
my_list = [1, 2, 3]

def modify_list():
    my_list.append(4)

modify_list()
print(my_list)  # 输出 [1, 2, 3, 4]

```

## 排序
### `lambda`
在python种,`lambda`函数后面可以跟一个列表或任何其他类型的表达式。`lambda`函数是一个简单的匿名函数，可以接受任何任何数量的参数，但只有一个表达式，这个表达式的就算结果就是函数的返回值。
例如：
* 排序字典的时候，lambda接受两个参数 `item = [k, v]`,然后返回一个参数`item[1]`
```python
sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
```
* 按值排序索引的时候,接受一个参数，返回一个列表里面两个参数
    * 这里的 lambda 函数对于每个元素 x（在这个上下文中，x 是 lst 中的一个元素，即一个索引）返回一个由两个元素组成的列表：nums[x] 和 x。
    * 这个返回的列表用作排序的键：
      * 第一个元素 nums[x] 是主要的排序依据。
      * 第二个元素 x 作为次要排序依据，确保在 nums[x] 相同的情况下，索引较小的元素排在前面。
```python
sort_lst = sorted(lst, key=lambda x: [nums[x], x])
```

```python
my_dict = {'b': 1, 'a': 2, 'c': 3}
sorted_dict = dict(sorted(my_dict.items()))

my_dict = {'b': 1, 'a': 2, 'c': 3}
sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

```
```python
#升序
sorted_index = sorted(range(len(nums)), key = nums.__getitem__)
#升序
sorted_index = [i for i, _ in sorted(enumerate(nums), key=lambda x: x[1])]
#升序
nums_index = [[num, i] for  i, num in enumerate(nums)]
sorted_index = [i for num, i in sorted(nums_index, key = lambda x : x[0])]

#根据列表nums中的值和索引对一个索引列表lst进行排序。
#根据nums中的值降序排序，如果有值相同，则根据索引降序排序。
n = len(nums)
lst = list(range(n)) #创建一个从0到n-1的索引列表，这个列表将被排序。
lst.sort(key=lambda x: [-nums[x], -x])
#对lst进行就地排序（即排序后的结果直接修改lst）
#对于lst中的每一个元素x（这里的x是一个索引），lambda函数返回一个由两部分组成的列表[-nums[x], -x]。
#第一关键字 -nums[x]
#第二关键字 -x


#升序
n = len(nums)
lst = list(range(n))
sort_lst = sorted(lst, key = lambda x: nums[x])
#sorted() 函数返回一个新列表，这个列表是按照 key 参数指定的方法排序的 lst 的副本。
sort_lst = sorted(lst, key = lambda x: [nums[x], x])
```
* `sort_lst = sorted(lst, key=lambda x: nums[x]):`
这个表达式根据 `nums` 中每个索引 x 对应的值对 `lst` 进行排序。如果 nums 中存在相同的值，那么它们对应的索引在 `sort_lst` 中的相对顺序将按照它们在原列表 `lst` 中的顺序，也就是说，排序是稳定的。
* `sort_lst = sorted(lst, key=lambda x: [nums[x], x]):`
这个表达式在排序时考虑了两个因素：首先是 nums 中每个索引 x 对应的值，其次是索引 `x` 本身。这意味着，如果 `nums` 中有两个或多个相同的值，它们将进一步按照它们的索引进行排序。这种方法确保了即使在 `nums` 中的值相等时，排序结果也是确定的，因为索引值是唯一的。
## accumulate
内置前缀和
```python
import itertools 
import operator
data = [1, 2, 3, 4, 5]
# 计算前缀和
print(list(itertools.accumulate(data)))
print(list(accumulate(data)))
# 计算到当前位置累积相乘得结果
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(itertools.accumulate(data, operator.mul, initial=2)))
# 计算到当前位置的最大值并且输出
print(list(itertools.accumulate(data, max)))
```
## enumerate
在Python中，enumerate 是一个内置函数，用于将一个可迭代的（比如列表、元组、字符串等）组合成一个索引序列，通常用于在for循环中获取每个元素的索引和值。这样可以在遍历时同时获得每个元素的索引位置和对应的值
```python
for index, value in enumerate(iterable, start=0):
    print(index, value)
#这里的 iterable 是你想要遍历的可迭代对象，start 是一个可选参数，表示索引的起始值，默认为0。
# 下面是一个具体的例子：

my_list = ['apple', 'banana', 'cherry']

# 使用enumerate遍历列表
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")


Index: 0, Value: apple
Index: 1, Value: banana
Index: 2, Value: cherry

```
使用 enumerate 可以使代码更加清晰和简洁，特别是当你需要索引和值时。

### 图论
#### 邻接表
```python
g = defaultdict(list)
while x, y in deges:
    g[x].append(y)
    g[y].adppen(x)

while x, y, d in deges():
    g[x].append((y, d))
    g[y].append((x, d))
```
#### 并查集
```python
# 数组
p = list(range(n))

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]
def merge(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        p[px] = p[py]

# 增加联通分量的大小，联通分量的数量

p = list(range(n))  # 父节点数组
size = [1] * n  # 连通分量大小数组，初始时每个连通分量大小为1
num_components = n  # 初始时每个节点自成一个连通分量，所以总数为n

def find(x):
    if x != p[x]:
        p[x] = find(p[x])  # 路径压缩
    return p[x]

def merge(x, y):
    px = find(x)
    py = find(y)
    if px != py:  # 只有当两个节点属于不同的连通分量时，才进行合并
        global num_components
        if size[px] < size[py]:  # 将较小的连通分量合并到较大的连通分量
            p[px] = py  # 更新父节点
            size[py] += size[px]  # 更新连通分量的大小
        else:
            p[py] = px
            size[px] += size[py]
        num_components -= 1  # 减少连通分量的总数

```
```python
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1]*n
        self.part = n

    def find(self, x):
        if x != self.root[x]:
            # 在查询的时候合并到顺带直接根节点
            root_x = self.find(self.root[x])
            self.root[x] = root_x
            return root_x
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] >= self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        # 将非根节点的秩赋0
        self.size[root_x] = 0
        self.part -= 1
        return

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_root_part(self):
        # 获取每个根节点对应的组
        part = defaultdict(list)
        n = len(self.root)
        for i in range(n):
            part[self.find(i)].append(i)
        return part

    def get_root_size(self):
        # 获取每个根节点对应的组大小
        size = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            size[self.find(i)] = self.size[self.find(i)]
        return size
```
## 数论
```python
def quick_pow(a, b, mod):#快速幂
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res
def inverse(a, mod): #求逆元
    return quick_pow(a, mod - 2, mod)
```
```python
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
```
```python
def sieve(n):
    primes = []
    st = [0] * (n + 1)
    for i in range(2, n + 1):
        if not st[i]:
            primes.append(i)
        for j in range(i * i, n + 1, i):
            st[j] = 1
    return primes

```
```python
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i <=n // i:
        if n % i == 0:
            return False
        i += 1
    return True
```

用Python编码更简单：

```
n = int(input()) 
s = 1 
ans = 0
for i in range(1,n+1,1):    
    s *= i
    ans += s 
print(ans)
```

## C.2 构造随机数和随机字符串

用Python构造测试数据，比c++简单得多。它能直接产生极大的数字，方便地产生随机字符等。下
（1）导入库

```python
import random
```

可以写成：

```python
from random import *
```

此时后面的代码能够简单一点，例如把`random.randint`直接写为`randint`
（2）在指定范围内生成一个很大的随机整数：

```python
print (random.randint(-9999999999999999,9999999999999999))
```

输出示例：428893995939258
（3）在指定范围内（0到100000）生成一个随机偶数：

```python
print (random.randrange(0, 100001, 2))
```

输出示例：14908
（4）生成一个0到1之间的随机浮点数：

```python
print (random.random())
```

输出示例：0.2856636141181378
（5）在指定范围内（1到20）生成一个随机浮点数：

```python
print (random.uniform(1, 20))
```

输出示例：9.81984258258233
（6）在指定字符中生成一个随机字符：

```python
print (random.choice('abcdefghijklmnopqrst@#$%^&*()'))
```

输出示例：d
（7）在指定字符中生成指定数量的随机字符：

```python
print (random.sample('zyxwvutsrqponmlkjihgfedcba',5))
```

输出示例：[‘z’, ‘u’, ‘x’, ‘w’, ‘j’]
（8）导入库

```python
import string
```

若写成`from string import *`，下面的`string.ascii_letters`改为`ascii_letters`
（9）用a-z、A-Z、0-9生成指定数量的随机字符串：

```python
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print (ran_str)
```

输出示例：iCTm6yxN
（10）从多个字符中选取指定数量的字符组成新字符串：

```python
print (''.join(random.sample(['m','l','k','j','i','h','g','d'], 5)))
```

输出示例：mjlhd
（11）打乱数组的顺序：

```
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]   
random.shuffle(items)
for i in range(0,len(items),1):      #逐个打印
   print (items[i]," ",end='')
```

输出示例：1 0 8 3 5 7 9 4 6 2
```python
import os
from random import randint, uniform
import subprocess

T = 10 # 样例组数

# 生成随机数据的函数
def generate_date():
     A = [0] * 1010
     for t in range(1, T + 1):
          # 数据的文件名
          filename = f"in_{t}.txt"
          with open(filename, "w") as file:
               n = randint(1, 1000)
               k = randint(1, n)
               file.write(str(n)+ " " + str(k) + "\n")
               for i in range(n):
                    A[i] = randint(0, 100)
               nums = " ".join(map(str, A[:n]))
               file.write(nums + "\n")
     print(f'generate_ok:......{T}')

# 调用py程序函数
def run(process_name):
     for t in range(1, T + 1):
          # 文件名
          out_filename = f"{process_name}_out_{t}.txt"
          in_filename = f"in_{t}.txt"
          subprocess.run(['python', f'{process_name}.py'],
                         stdin = open(in_filename, "r"),
                         stdout = open(out_filename, "w"))
     print(f'run_{process_name}_ok:......{T}')

# 对比txt文件是否相同的函数
def diff(file1, file2):
     for t in range(1, T + 1):
          f1 = f"{file1}_out_{t}.txt"
          f2 = f"{file2}_out_{t}.txt"
          with open(f1, "r") as s, open(f2, "r") as ss:
               lines1 = s.readlines()
               lines2 = ss.readlines()
               if len(lines1) != len(lines2):
                    print(f'{t}:lines error')
                    continue
               ok = 1
               for line1,line2 in zip(lines1, lines2):
                    if line1 != line2:
                         print(f'{t}:exist error')
                         ok = 0
                         break
               if ok: print(f'{t}:ok')

if __name__ == "__main__":
    # 生成输入文件
    generate_date()

    # 调用正解
    file_true = "True"
    run(file_true)

    # 调用测试程序
    file_my = "A"
    run(file_my)

    # 调用对比程序
    diff(file_true, file_my)
```