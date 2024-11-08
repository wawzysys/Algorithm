# 1
### 问题描述

小美有三个水桶，容量分别为 \(a\)、\(b\)、\(c\)，现在有 \(n\) 单位的水需要搬运。每次搬水时小美可以选择容量最大的桶进行搬运。请计算小美最少需要几次才能将 \(n\) 单位的水全部搬运完。

### 输入描述

- 输入四个整数 \( a, b, c, n \)，分别表示三个桶的容量以及需要搬运的水的总量。

### 输出描述

- 输出一个整数，表示小美最少需要几次搬运才能将所有的水搬运完。



### 示例 1

输入
```
5 3 4 10
```
输出
```
2
```
解释  
小美每次选择容量最大的桶进行搬运：
1. 第一次使用容量为 5 的桶，搬 5 单位水，剩下 5 单位水。
2. 第二次再次使用容量为 5 的桶（同样选最大的桶），搬 5 单位水，剩下 0 单位水。

总共 2 次搬运完成任务。

### 示例 2

输入
```
7 2 5 15
```

输出
```
3
```





### 思路
签到题选择最大的桶运水就可。
```python
a, b, c, n = map(int, input().split())
mm = max(a, b, c)
print((n + a - 1) // mm)
```


# 2
### 问题描述

小红 (R)、小蓝 (B) 和小绿 (G) 正在一个字符串上玩捉迷藏。三人的位置分别用对应的字母 \( R \)、\( B \)、\( G \) 表示，其他位置是空地 (\*) 或障碍 (\#)。

- 寻找方可以每秒移动一个位置，躲藏方不能移动。
- 双方均不能移动到障碍物 (\#) 上。
- 当寻找方移动到躲藏方的位置时，躲藏方被认为被找到。
- 当一个人作为寻找方，另外两个人作为躲藏方时，只要寻找方找到一个躲藏方，即认为游戏胜利。

请计算当三个人分别作为寻找方时，能够使游戏胜利所需的最少时间。

### 输入描述

- 输入一个字符串 \( s \)，仅由字符 "\*#RGB" 组成，长度在 \( 3 \leq |s| \leq 10^5 \) 之间，且保证 "RGB" 各只出现一次。

### 输出描述

- 输出三个整数，分别代表小红、小蓝和小绿作为寻找方时，能够获胜的最少时间。如果无法获胜，则输出 -1。



### 示例 1

输入
```
R***B*G
```

输出
```
4 3 3
```

### 示例 2

输入
```
R****B***#G
```

输出
```
5 5 -1
```

### 思路

1. 首先识别三个玩家的位置（R、B、G）以及所有障碍的位置（#）。
2. 使用广度优先搜索（BFS）计算从每个玩家的位置到其他两位玩家的最短路径，同时避开障碍物。
3. 对于每个人作为寻找方，找到其中一位躲藏方的最小步数。
4. 输出三种情况下的最短步数，若无法找到任意一位躲藏方，则输出 -1。
   
```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        int n = s.length();
        int[] component = new int[n];
        int comp_id = 0;

        int[] positions = { -1, -1, -1 };
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'R' || c == 'B' || c == 'G') {
                positions["RBG".indexOf(c)] = i;
            }
            if (c == '#') {
                component[i] = -1;
            } else {
                if (i > 0 && component[i - 1] != -1) {
                    component[i] = component[i - 1];
                } else {
                    component[i] = comp_id++;
                }
            }
        }

        StringBuilder results = new StringBuilder();
        String[] seekers = { "R", "B", "G" };
        for (String seeker : seekers) {
            int a = "RBG".indexOf(seeker);
            int b = positions[a];
            int c = component[b];
            int minTime = Integer.MAX_VALUE;
            boolean found = false;
            for (int i = 0; i < positions.length; i++) {
                if (i != a) {
                    int hide = positions[i];
                    if (hide != -1 && component[hide] == c) {
                        int time = Math.abs(b - hide);
                        if (time < minTime) {
                            minTime = time;
                            found = true;
                        }
                    }
                }
            }
            if (found) {
                results.append(minTime).append(" ");
            } else {
                results.append("-1 ");
            }
        }

        System.out.println(results.toString().trim());
        scanner.close();
    }
}

```

# 3
小美有 a个红砖、6个蓝砖和c个绿砖。每x个红砖可以合成1个蓝砖，每y个蓝砖可以合成1个绿砖。砖块只能正向合成，不能反向分解。
一套砖块包含1个红砖、1个蓝砖和1个绿砖。请计算小美最多可以收集多少套砖块。

输入描述
每个测试文件均包含多组测试数据。第一行输入一个整数 T(1 ≤T ≤10^9)代表数据组数，每组测试数据描述如下:
在一行上输入五个整数a, b, c, x,y (0 < a, b,c ≤ 10^9,1 ≤ x,y≤ 10^9).分别表示红砖、蓝砖、绿砖的数量及合成的比例。
1输出描述
对于每一组测试数据，在一行上输出一个整数，代表小美最多可以收集到的砖块套数。

### 示例1
输入
2
1 2 3 4 2
10 2 1 4 2

输出
1
2
对于第一组测试数据，无法进行合成转换，故只能收集初始的一套。
对于第二组测试数据，可以把 8个红砖转为 2个蓝砖把2个蓝砖转化为1个绿砖。这样每种的砖块数量分别为[2, 2 ,2]刚好凑成2 套.

### 思路
由题意得具有单调性，二分求最大值。
check定义：mid使我们要check的值，check(mid)返回是否满足条件。
l_min = max(0, mid - c)：计算蓝砖转绿砖的最小次数 l_min，确保绿砖数量足够。
k_min = max(0, mid + y * l_min - b)：计算红砖转蓝砖的最小次数 k_min，确保蓝砖数量足够。
最大转换次数计算：
k_max = (a - mid) // x：计算最多能进行红砖转蓝砖的次数 k_max，即红砖足够时的最大次数。
如果 k_min <= k_max，说明在当前的 mid 情况下可以满足需求。

代码
```python

T = int(input())
for _ in range(T):
    a, b, c, x, y = map(int, input().split())
    left, right = 0, a + b + c
    def check(x):
        l_min = max(0, x - c)
        k_min = max(0, x + y * l_min - b)
        k_max = (a - x) // x
        return k_min <= k_max
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    print(left)



```

# 4
### 问题描述

小美有一个长度为 \( n \) 的数组 \( [a_1, a_2, \ldots, a_n] \)。她定义一个数组是“好”的，当且仅当数组中所有数的最小公倍数（LCM）不在数组中。例如：

- 数组 \( [1, 2, 3, 4] \) 是一个好数组，因为所有元素的 LCM 是 12，而 12 不在数组中。
- 数组 \( [2, 6, 3] \) 不是好数组，因为所有元素的 LCM 是 6，而 6 存在于数组中。

小美希望从数组 \( a \) 中选择一个子序列，使得该子序列是一个好数组，并且她想知道该子序列的最大长度。数组 \( b \) 是数组 \( a \) 的子序列，如果 \( b \) 可以通过删除 \( a \) 中的若干（可能为零或全部）元素得到。

### 输入描述

- 第一行输入一个整数 \( t \) ，表示测试用例的数量。
- 每个测试用例包含两行：
  - 第一行输入一个整数 \( n \) ，表示数组的长度。
  - 第二行输入 \( n \) 个整数，表示数组 \( a \) 的元素。

### 输出描述

- 对于每个测试用例，输出子序列的最大长度，使得子序列是好数组。

### 示例

#### 示例 1

输入
```
2
3
1 3 2
5
1 2 3 12 4
```

输出
```
3
4
```

### 解释
- 第一个测试用例中，数组 `[1, 3, 2]` 是一个好数组，因此最大长度为 3。
- 第二个测试用例中，从 `[1, 2, 3, 12, 4]` 中可以选择 `[1, 2, 3, 4]` 作为子序列，这是一个好数组，最大长度为 4。

### 思路：
本题思维较大。
最大元素与最小公倍数的关系：
- 当且仅当数组中所有元素都能整除最大元素时，数组的最小公倍数等于最大元素。
- 如果最大元素不能被所有元素整除，则最小公倍数大于最大元素。

算法步骤：
步骤 1：计算数组的最大元素 max_element。
步骤 2：检查数组中的每个元素是否都整除 max_element。
如果所有元素都整除 max_element，则最小公倍数等于 max_element。
如果 max_element 存在于数组中，我们需要删除它的所有出现次数，并更新数组。
重复上述步骤，直到最小公倍数不在数组中或数组为空。
如果有任何元素不能整除 max_element，则最小公倍数大于 max_element，不在数组中，我们可以选择所有元素。
实现细节：
使用map来记录数组中每个元素的出现次数，方便删除元素。
在每次迭代中，更新数组并重新计算最大元素。

```python
import sys
import math
from collections import Counter
def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        counts = Counter(arr)
        answer = n
        while True:
            nums = list(counts.keys())
            max_e = max(nums)
            ok = True
            for num in nums:
                if max_e % num != 0:
                    ok = False
                    break
            if ok:
                if counts[max_e] > 0:
                    answer -= counts[max_e]
                    del counts[max_e]
                    if not counts:
                        break
                else:
                    break
            else:
                break
        print(answer)
main()

```

# 5
### 问题描述

小美正在一张有向但不一定连通的图上玩游戏。图包含若干个点，每个点的权值为 \( q_i \)。当小美从节点 \( i \) 移动到节点 \( \text{Next}_i \) 时，游戏规则如下：

- 如果 \( a_{\text{Next}} > a_i \)，小美的金币将增加 \( x \)。
- 如果 \( a_{\text{Next}} \le a_i \)，小美的金币将增加 \( y \)。

小美会提出 \( q \) 次询问，每个询问从某个点 \( u \) 出发，移动不超过 \( k \) 步，求最多能获得多少金币。

### 输入描述

- 第一行输入四个整数 \( n, q, x, y \) 代表图上点的数量、询问的次数、规则中金币的增加量。
  - \( 1 \le n, q \le 2 \times 10^5 \)
  - \(-10^6 \le x, y \le 10^6 \)
  
- 第二行输入 \( n \) 个整数 \( \text{Next}_1, \text{Next}_2, \ldots, \text{Next}_n \) 表示第 \( i \) 个节点下一步的位置。
  - \( 1 \le \text{Next}_i \le n \)

- 第三行输入 \( n \) 个整数 \( a_1, a_2, \ldots, a_n \) 表示第 \( i \) 个节点的权值。
  - \( 1 \le a_i < 10^6 \)

- 接下来的 \( q \) 行，每行输入两个整数 \( u, k \) 表示一次询问的起始点和步数限制。
  - \( 1 \le u \le n \)
  - \( 1 \le k \le 10^9 \)

### 输出描述
对于每一次询问，在一行上输出一个整数，代表最多能获得的金币数量。
### 示例1
输入:
4 5 -2 3
2 3 4 1
5 10 3 2
1 1
1 2
1 4
2 4
2 7
输出:
0
1
4
6
8
说明:
对于第一次询问，走一步会扣除2金币，但是可以选择站在原地不走;
对于第二次询问，走一步时金币数量减至-2走两步金币数量变更为-2+3=1

### 示例2
输入:
4 4 2 -1
2 3 1 4
1 2 3 1000000
1 3
3 3
2 3
4 1000000
输出:
4
3
2
0

### 思路
