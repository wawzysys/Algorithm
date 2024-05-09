# T3

## 题面

多多最近在研究一种数组$a=[a1,a2,a3…,an]$，该数组由$n$个元素构成，每个元素是一个**正整数**。
对于这个数组，可以将其拆分为多个子数组，每次拆分是将数组a中连续的元素拆到一个子数组中，而且一个元素只能拆到一个子数组中。例如:数组$a=[4,1,5]$，拆分为多个了数组后只画能会有以下4种情况:

① 拆分为3个子数组:[4]、[1]、[5]

② 拆分为2个子数组:[4]、[1,5]

③ 拆分为2个子数组:[4,1]、[5]

④ 拆分为1个子数组:[4,1.5]
拆分后的多个子数组如果满足:子数组内元素的和是相等的。则这种拆分叫做**完美拆分**。换分话说，对于上述数组$ a= [4.1.5]$，只有③,④两种情况是满足**完美拆分**的:第③中情况了数组中元素的和都相等，都是5;第④种情况了数组的和是10.
在满足**完美拆分**的情况下，我们把该情况下元素个数最多的子数组挑选出来，把这个子数组元素的数量记为该拆分的**厚度**。
现在多多想知道，**厚度**最小的那一种情况，如果有多个，取子数组元素和最小的情情况。种完美拆分情况下，厚度最小且子数组和最小的情况叫做:完美厚度拆
例如:上述数组 $a=[4.1,5]$，

第③种情况中，$[4,1]$这个子数组在所有子数组中元素最多，厚度为2。

第④种情况下，[4,1.5]这个子数组在所有子数组中元素最多，厚度为3。

所以完美厚度拆分的厚度是3，子数组的和是5.

输入

```
3
3
4 1 5
4
1 1 1 1
2 
1 2

```

输出

```
2 5
1 1
2 3
```

说明

## 思路 

枚举第一个长度，然后模拟。

## 代码

```c++
#include <iostream>
#include <vector>
#include <climits> // For INT_MAX

using namespace std;

int main() {
    int t, n;
    cin >> t;

    while (t--) {
        cin >> n;
        vector<int> a(n + 1); 
        int k = 0;
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
            k += a[i];
        }

        int min1 = INT_MAX, sum = 0;
        for (int i = 1; i * i <= k; i++) {
            if (k % i == 0) {
                int ans = 0, cnt = 0, max1 = 0;
                for (int j = 1; j <= n; j++) {
                    cnt += a[j];
                    ans++;
                    if (cnt == k / i) {
                        max1 = max(max1, ans);
                        ans = 0;
                        cnt = 0;
                    }
                }
                if (cnt == 0 && max1 <= min1) {
                    sum = k / i;
                    min1 = max1;
                }
                ans = 0, cnt = 0, max1 = 0;
                for (int j = 1; j <= n; j++) {
                    cnt += a[j];
                    ans++;
                    if (cnt == i) {
                        max1 = max(max1, ans);
                        cnt = 0;
                        ans = 0;
                    }
                }
                if (cnt == 0 && max1 < min1) {
                    sum = i;
                    min1 = max1;
                }
            }
        }

        cout << min1 << " " << sum << endl;
    }

    return 0;
}

#include <iostream>
#include <vector>
#include <climits> // For INT_MAX

using namespace std;

int main() {
    int t, n;
    cin >> t;

    while (t--) {
        cin >> n;
        vector<int> a(n + 1); 
        int k = 0;
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
            k += a[i];
        }

        int min1 = INT_MAX, sum = 0;
        for (int i = 1; i * i <= k; i++) {
            if (k % i == 0) {
                int ans = 0, cnt = 0, max1 = 0;
                for (int j = 1; j <= n; j++) {
                    cnt += a[j];
                    ans++;
                    if (cnt == k / i) {
                        max1 = max(max1, ans);
                        ans = 0;
                        cnt = 0;
                    }
                }
                if (cnt == 0 && max1 <= min1) {
                    sum = k / i;
                    min1 = max1;
                }
                ans = 0, cnt = 0, max1 = 0;
                for (int j = 1; j <= n; j++) {
                    cnt += a[j];
                    ans++;
                    if (cnt == i) {
                        max1 = max(max1, ans);
                        cnt = 0;
                        ans = 0;
                    }
                }
                if (cnt == 0 && max1 < min1) {
                    sum = i;
                    min1 = max1;
                }
            }
        }

        cout << min1 << " " << sum << endl;
    }

    return 0;
}

```

# T4

## 题面

你有一块长方形的巧克力，这块巧克力共有n*m小块。你想吃k小块巧克力，因此你也许需要掰开这块巧克力。

在每一次操作中你可以把任意一块矩形形状的巧克力掰成两块矩形形状的巧克力。你只能沿着巧克力小块之间的分割线掰开巧克力——可以沿着水平方向或是竖直方向掰开。掰开巧克力的花费等于分割线长度的平方。

例如，如果你有一块2:*3的巧克力，那么你可以沿着水平方向掰从而得到两块1:*3的巧克力，这次操作的花费即为3^2=9。

或者你也可以沿着竖直方向掰从而得到一块2*1的巧克力和一块2*2的巧克力，这次操作的花费即为2^2=4。

对于每一个给出的n，m和k，计算出最小花费。你可以用多块巧克力凑出k小块巧克力。剩余的巧克力可以不是完整的一块。

输入格式：

输入数据的第一行包括1个整数$t(1<=t<=40910)$，表示数据组数。

接下来的t行每一行都包含3个整数$n，m和k(1<=n,m<=30,1<=k<=min(n*m,50))$，其意义见上文。

输出格式：

输出t行，分别表示每一组数据的最小花费。

说明：

在样例一的第1行这组数据情况下一共需要进行2次操作： 1.把2:2的巧克力掰成两块2:*1的巧克力，花费为2^2=4； *

*2.把2:1的巧克力掰成两块1*:1的巧克力，花费为1:2=1。

在样例一的第2行这组数据情况下操作步骤同上。

```
给你价格数组costs和金币量coins。
```

输出描述

```
请你计算并返回用 coins 金币能够买到最多的英雄列表。
```

输入

```
4
2 2 1
2 2 3
2 2 2
2 2 4
```

输出

```
5
5
4
0
```



## 思路

记忆化搜索//dp

`dp[n][n][p]`表示从n：m的巧克力中切出大小为p的最小话费。

## 代码

```c++
#include<cstdio>
#include<iostream>
#include<climits>
#include<algorithm>
#include<cmath>
using namespace std;
int s[55][55][55];
int inf=0x3f3f3f3f;
int f(int n,int m,int p){
	if(n*m==p || p==0){
		return 0;
	}
	if(n>m){
		swap(n,m);
	}
	if(s[n][m][p]>0){
		return s[n][m][p];
	}
	int smin=inf;
	for(int i=1;i<=n/2;i++){
		for(int j=0;j<=p;j++){
			int ans=m*m+f(i,m,j)+f(n-i,m,p-j);
			smin=min(ans,smin);
		}
	}
	for(int i=1;i<=m/2;i++){
		for(int j=0;j<=p;j++){
			int ans=n*n+f(i,n,j)+f(m-i,n,p-j);
			smin=min(smin,ans);
		}
	}
	return s[n][m][p]=smin;
}
int main(){
	int T,n,m,p;
	scanf("%d",&T);
	while(T--){
		scanf("%d %d %d",&n,&m,&p);
		printf("%d\n",f(n,m,p));
	}
return 0;
}
```

```python
换成dp写法：
N  = 31 
dp = [[inf for _ in range(N)] for _ in range(N)]
for i in range(31):
    for j in range(31):
        if i * j > 50:
            continue
        dp[i][j][i * j] = 0
for n in range(31):
    for m in range(31):
        ss = min(n * m, 50)
        for p in range(1, ss + 1):
			for i in range(1, n // 2 + 1):
                for j in range(min(i * m, p) + 1):
                    dp[n][m][p] = min(dp[n][m][p], dp[i][m][j] + dp[n - i][m][p - j] + m * m)
            for i in raneg(1, m // 2 + 1):
                for j in range(min(i * n, p) + 1):
                    dp[n][m][p] = min(dp[n][m][p], dp[n][i][j] + dp[n][m - i][p - j] + n * n)
                    
```



# T3

## 

卡车运货详细眉述有一批货物要运输，己知卡车的载重量为 w ，其中集袈 0 (1<=i<=n) 的重虽为 w[i], n 为集装箱个数，在不考虑集装箱体积的前提下，尽虽多的将集装箱放到卡车上，使集装箱的重量之和正好等于 W ，当总重虽相同时，要求选取的集装箱个数尽可能少，适给出最优的集装箱选择方案。

```cpp
输入描述卡车重量W，和集装箱重量c

```

示例

```
输入: 10, [5, 2, 6, 4, 3]
输出: [0, 0, 1, 1, 0]
说明：
方案一： 1, 1, 0, 0,  1  // 5 + 2 + 3 = 10 需要三个
方案二： 0, 0, 1, 1, 0 // 需要二个集装箱
方案二的集装箱数量最，故方案二是最优方案
```

## 思路

我们用 $dp[i][j]$ 表示前 $i$ 个集装箱中可以凑成重量为 $j$ 所需要的最少集装箱数量。$dp$ 之前先将序列从小到大排序，假设当前枚举到 $w[i]$，那么转移方程为 $dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - w[i]] + 1)$。然后从后往前枚举 $w[i]$，如果当前重量不小于 $w[i]$ 的话就可以选这个集装箱。

## 代码

```python
class Solution:
    def trunkLoad(self, w, c):
        inf = float('inf')
        n = len(c)
        a = [(0, 0)] * (n + 1)
        for i in range(n):
            a[i + 1] = (c[i], i + 1)
        a.sort()

        dp = [[INF] * (w + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(w + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
                if j - a[i][0] >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - a[i][0]] + 1)

        vis = [0] * (n + 1)
        now = w
        for i in range(n, 0, -1):
            if now - a[i][0] >= 0 and dp[i - 1][now - a[i][0]] != INF:
                vis[a[i][1]] = 1
                now -= a[i][0]

        ans = []
        for i in range(1, n + 1):
            ans.append(vis[i])
        
        return ans

```

