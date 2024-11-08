# 1
有一组正整数(大于0)序列，请问有多少对数字满足:其中一个数字是另外一个数字的2倍
输入描述
输入一个数字T，表示有T组测试数据;每个测试数据输入一个数字n(1< n <100),表示有多少数字;然后再输入数字，空格隔开;
输出描述
对于每组测试数据，输出满足条件的组数。
输入
2
6
1 3 5 7 9 11
7
6 2 4 3 33 10 1
输出:
0
3

# 代码
```python
from collections import *
sint = lambda: int(input())
lint = lambda: list(map(int, input().split()))
def solve():
    n = sint()
    nums = lint()
    cnt = Counter(nums)
    ans = 0
    for c in cnt:
        if c * 2 in cnt:
            ans += cnt[c]
    print(ans)
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        solve()


```
# 2
现从德国引进一台高精度机器，用于加工一批零件。每个零件加工完可获得一定的报酬，但是零件加工有以下要求:
(1)每个零件加工的起始与结束时间是固定的，必须从某一时刻开始到某一时刻结束，一次性连续加工完。
(2)零件间的加工时间要求可能有冲突，但机器只有一台，在某个时刻，只能加工一个零件。一个零件开始时间和另一个零件结束时间相同不算冲突。
请合理安排从而保证最大加工报酬。
输入描述
```
零件的数量
零件一编号 零件一的加工报酬 零件一加工起始时间 零件一加工结束时间
零件二编号 零件二的加工报酬 零件二加工起始时间 零件二加工结束时间
零件三编号 零件三的加工报酬 零件三加工起始时间 零件三加工结束时间
......
零件N编号 零件N的加工报酬 零件N加工起始时间 零件N加工结束时间
```
输出描述

最大加工报酬
示例 
输入
5
1 10 1 2
2 15 5 6
3 20 4 6
4 15 1 5
5 20 4 6
输出：
30
描述：
可以安排{1,3}或者{1,5}或者{4、2}
```
```

# 3
随着移动互联网的发展，人们的出行方式也变得越来越方便，相信很多人都用过手机打车软件，请你设计一个简单的订单调度系统，当用户打车时能够计算出最快接到乘客的司机。
乘客叫车时，系统获取出当前区域内司机情况如下
1.乘客到各个司机的路程长度分别是D1、D2...DN，单位是米。
2.这些路程中可能存在拥堵路段，各司机路程中的拥堵长度分别是C1C2..CN，如果到某司机的路段不存在拥堵，则值为0。
3.路程中还可能存在红绿灯路口，各司机路程经过的红绿灯的个数分别是L1、L2.LN，如果无红绿灯则为0，假设每个红绿灯路口碰到红灯的概率都为50%，每个红灯要等待15秒。
4.所有司机在正常路段的行驶速度是10m/s，在拥堵路段的行驶速度是2m/s。
5.各个司机评分级别分别是L1、L2、..LN，评分等级反映服务质量，是1-10的整数。
调度系统需综合考虑接载速度和服务质量，假设通过以上数据计算得到最快接载司机是M司机，其用时为T，单位是秒，如果在[T,T+60)时间范围内存在评分级别更高的司机，则安排该时间范围内评分更高的司机接载。
输入包括4行数据，格式说明如下:
第1行是乘客到各司机的路程长度，都是整数，用英文半角逗号分隔。第1个整数表示1号司机的距离，第2个整数表示2号司机的距离，以此类推。第2行是各司机路程中的拥堵路段长度，都是整数，用英文半角逗号分隔。与第一行对应，按照司机编号排列。第3行是各司机路程中红绿灯路口的个数，都是整数，用英文半角逗号分隔。与第一行对应，按照司机编号排列。第4行是各司机的评分等级，共有10级，分别用整数1到10表示，数字越大表示
级别越高，服务质量越好。与第一行对应，按照司机编号排列。
输出描述
输出系统所计算出的接单的司机编号(司机编号从1开始)及其接载所用时长(单位是秒)，用逗号分隔。例如:4,398。
补充说明
题目保证所有用例输入文件中数据都合法，且接载时间计算结果都只需要整数结果，不需要考虑小数情况。

输入
1530,1760,2300,1990
240,320,0,0
2,1,0,0
8,10,10,9

输出
3,230
```python
import sys
import re
lint = lambda: list(map(int, input().split(",")))

class Driver:
    def __init__(self, index, D, C, L, S):
        self.index = index  
        self.D = D          
        self.C = C          
        self.L = L          
        self.S = S          
        self.T = self.compute_time()  

    def compute_time(self):
        dis = self.D - self.C
        times = dis // 10  
        ji = self.C // 2         
        wait_time = (self.L * 15) // 2        
        return times + ji + wait_time
def f(ds):
    min_driver = ds[0]
    for d in ds:
        if d.T < min_driver.T:
            min_driver = d
        elif d.T == min_driver.T and d.S > min_driver.S:
            min_driver = d
    return min_driver
def main():
    D = lint()
    C = lint()
    L = lint()
    S = lint()
    N = len(D)
    ds = []
    for i in range(N):
        ds.append(Driver(i+1, D[i], C[i], L[i], S[i]))
    se = f(ds)
    while True:
        found = False
        current_T = se.T
        current_S = se.S
        bh = None
        for d in ds:
            if d.S > current_S and current_T <= d.T < current_T + 60:
                if bh is None:
                    bh = d
                else:
                    if d.S > bh.S:
                        bh = d
                    elif d.S == bh.S and d.T < bh.T:
                        bh = d

        if bh:
            se = bh
            found = True
        else:
            break

    print(f"{se.index},{se.T}")

main()

```