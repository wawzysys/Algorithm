---
title: sort
tags: sort
abbrlink: 5124f222
date: 2024-03-30 00:50:49
---
给定一个整数 $N$，请你求出所有分母小于或等于 $N$，大小在 $[0,1]$ 范围内的**最简分数**，并按从小到大顺序依次输出。

例如，当 $N = 5$ 时，所有满足条件的分数按顺序依次为：

$\frac{0}{1},\frac{1}{5},\frac{1}{4},\frac{1}{3},\frac{2}{5},\frac{1}{2},\frac{3}{5},\frac{2}{3},\frac{3}{4},\frac{4}{5},\frac{1}{1}$

#### 输入格式

共一行，包含一个整数 $N$。

#### 输出格式

按照从小到大的顺序，输出所有满足条件的分数。

每个分数占一行，格式为 $a/b$，其中 $a$ 为分子， $b$ 为分母。

#### 数据范围

$1 \le N \le 160$

#### 输入样例：

```
5
```

#### 输出样例：

```
0/1
1/5
1/4
1/3
2/5
1/2
3/5
2/3
3/4
4/5
1/1
```
```python
# E:\0Code\Algorithm\acw\1360.py 2024-03-30 by wz
from functools import cmp_to_key
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n = sint()
a = set()
def cmp(x,y):
    return x[0]*y[1] - x[1]*y[0]
    #返回 < 0  排序结果 x y
    #返回 > 0  排序结果 y x
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i <= j:
            a.add((i, j))       
b = set()
for (i, j) in a:
    b.add((i // gcd(i,j), j // gcd(i, j)))
a = list(b)

a = sorted(a, key = cmp_to_key(cmp))
print("0/1")
for (i, j) in a:
    print(str(i) + "/" + str(j))
```