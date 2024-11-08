

# 小红的密码

时间限制： 5000 MS
内存限制: 589824 KB
题目描述:
小红书最近更新了密码策略，小红需要更新她的密码。她的旧密码足一个 $n$ 位的数字序列 $P$ ，她想要生成一个新密码 $Q$ ，按照小红书最新的密码策略，新密码需要满足以下条件:

- 长度和原来的密码长度一致,且每一位都由 $[0,9]$ 的数字之一组成。
- 至少包含一个数字比旧密码中的最大数字大。
- 至少包含一个数字比旧密码中的最小数字小。

请计算小红可以生成的新密码数量。由于结果可能很大，请对 $10^9+7$ 取模后再输出。

输入描述
每个测试文件均包含多组测试数据。第一行输入一个整数 $T(1 \leq T \leq 1000)$ 代表数据组数，每组测试数据描述如下:
第一行输入一个整数 $n\left(1 \leq n \leq 2 \times 10^5\right)$ 表示原来的密码长度。
第二行输入一个长度为 $n$ ，且仅由数字字符构成的字符串 $s$ 表示原来的密码。
除此之外，保证所有的 n 之和不超过 $2 \times 10^5$ 。

输出描述
对于每一组测试数据，在一行上输出一个整数，代表新密码的方案总数。由于答案可能很大，请将答案对 $\left(10^9+7\right)$ 取模后输出。

输入：

```
2
2
12
2
00
```

输出：

```
14
0
```

说明：对于第一组样例符合条件的密码 03,04,05,06,07,08,09,30,40,50,60,70,80,90, 共 14个。

```python
T = int(input())
mod = 10 ** 9 + 7

for _ in range(T):
    n = int(input())
    s = input().strip()
    digits = [int(c) for c in s]
    minP = min(digits)
    maxP = max(digits)
    total_sequences = pow(10, n, mod)
    if maxP == 9:
        D = total_sequences
    else:
        D = pow(maxP + 1, n, mod)
    if minP == 0:
        E = total_sequences
    else:
        E = pow(10 - minP, n, mod)
    D_intersect_E = pow(maxP - minP + 1, n, mod)
    temp = (D + E - D_intersect_E) % mod
    answer = (total_sequences - temp + mod) % mod
    print(answer)
```






# 三角形问题

时间限制： 3000 MS
内存限制: 589824 KB
题目描述：
小歪最近对勾股数很感兴棷，他知道小红书上面有非常多的总结攻略，于是他进行了搜索学习，即一个三元组 $(a, b, c)$ 满足其是勾股数当且仅当 $a^2+b^2=c^2$ 。
现在，小歪想要找到三数之和大于等于 $k$ 的最小的一组勾股数，即找到最小的三元组 $\left(a_0, b_0, c_0\right)$ 使得 $k \leq a_0+b_0+c_0$

输入描述
第一行输入一个整数 $\mathrm{q}\left(1 \leq \mathrm{q} \leq 10^5\right)$ 代表询问数量，对于每一个询问:
在一行上输入一个整数 $k\left(1 \leq k \leq 10^4\right)$ ，代表询问的数字。

输出描述
对于每一个询问，在一行上从小到大依次输出三个整数，代表大于等于 $k$ 的最小的一组勾股数。如果有多个三元组满足条件，输出字典序最小的三元组。


示例：

输入：

```
2
12
33
```

输出：

```
3 4 5
9 12 15
```

```python
from math import gcd
import bisect

S = 100000
ts = []
for m in range(2, int((S//2)**0.5)+1):
    for n in range(1, m):
        if (m - n) % 2 == 1 and gcd(m, n) == 1:
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            s = a + b + c
            if s > S:
                continue
            p = sorted([a, b, c])
            k = 1
            while True:
                a_k = p[0]*k
                b_k = p[1]*k
                c_k = p[2]*k
                s_k = a_k + b_k + c_k
                if s_k > S:
                    break
                ts.append((s_k, a_k, b_k, c_k))
                k += 1

ts.sort()
ss = [t[0] for t in ts]
q = int(input())
for _ in range(q):
    k = int(input())
    idx = bisect.bisect_left(ss, k)
    print(ts[idx][1], ts[idx][2], ts[idx][3])
```







# 商店购物

时间限制： 3000 MS
内存限制: 786432 KB
题目描述：
在小红书电商平台上，用户经常可以看到各种商品搭配优惠券的促销活动。每件商品都标注了价格和相应的优惠券，使用这些优惠券可以让商品的价格降低。某些情况下，为了使用某个商品的优惠券，用户还必须使用其他商品的优惠券，形成了一个特定的购买顺序和依赖关系。
现在商店有 n 件商品，每件商品仅可购买一次。每件商品价格为 $c_i$ ，第 i 件物品使用专属优惠券购买可以降价 $d_i$ ，对于商品编号 $\mathrm{i} \geq 2$ 的商品，使用第 i 个商品优惠券还必须使用优惠券购买编号为 $x_i$ 商品（当然，你也可以选择不使用优惠直接购买）。你有 b 元，请问你最多可以买多少件商品。

输入描述
第一行两个整数 $n ， b\left(1 \leq n \leq 5000,1 \leq b \leq 10^9\right)$ ，表示有 $n$ 件商品，现在你有 $b$ 元用于购买商品。
接下来 $n$ 行，每 i 行两个整数 $\mathrm{c}_{\mathrm{i}}, \mathrm{d}_{\mathrm{i}}\left(1 \leq \mathrm{d}_{\mathrm{i}} \leq \mathrm{c}_{\mathrm{i}} \leq 100000\right)$ 。
如果 $i \geq 2$ 额外增加一个整数 $x_i\left(1 \leq x_i<i\right)$ 。

输出描述
输出一行，请问你最多可以买多少件商品。






示例：

输入：

```
6 16
10 9
10 5 1
12 2 1
20 18 3
10 2 3
2 1 5
```

输出：

```
4
```

说明：

其中一个合法的购买方案为:
1.购买第一件商品，花费 $10-9=1$ ；
2.购买第三件商品，降价，需要搭配购买第一件商品 (已购买)，花费 $12-2=10$ ；
3.购买第四件商品，降价，需要搭配购买第三件商品 (已购买)，花费 $20-18=2$ ；
4.购买第六件商品，不降价，花费 2 ；

总花费为 $1+10+2+2=15$ 。

```
def shop(n, b, lst):
    from heapq import heappush, heappop
    import sys

    ind = [0] * n
    adj = [[] for _ in range(n)]
    c = []
    d = []

    for i in range(n):
        if i == 0:
            a, e = lst[i]
            c.append(a)
            d.append(a - e)
        else:
            a, e, x = lst[i]
            x -= 1
            c.append(a)
            d.append(a - e)
            ind[i] += 1
            adj[x].append(i)

    from collections import deque
    q = deque()
    q.append(0)
    topo = []

    while q:
        node = q.popleft()
        topo.append(node)
        for nb in adj[node]:
            ind[nb] -= 1
            if ind[nb] == 0:
                q.append(nb)

    if len(topo) != n:
        return 0

    dp = [sys.maxsize] * n
    dp[0] = d[0]
    mx = 0

    for node in topo:
        if dp[node] > b:
            continue
        mx += 1
        for nb in adj[node]:
            dp[nb] = min(dp[nb], dp[node] + d[nb])

    return mx

n, b = map(int, input().split())
lst = []
for i in range(n):
    if i == 0:
        a, e = map(int, input().split())
        lst.append((a, e))
    else:
        a, e, x = map(int, input().split())
        lst.append((a, e, x))

print(shop(n, b, lst))

```



