小红定义一个字符矩阵的权值为:该矩阵有多少2“2的矩形区域满足:区域中同时出现了"red"这三种字符。现在小红想知道，所有n行m列的、仅由小写字母组成矩阵，它们的权值之和等于多少?由于答案过大，请对10°+7取模。

输入描述
两个正整数几，m，用空格隔开l≤n,m≤10^9
输出描述
一个整数，代码所有几行m列的、仅由小写字母组成矩阵的权值之和。由于答案过大，请对10^9+ 7取模。

示例1:
输入：
2 3
输出:
794976

说明
2行3列的字母矩阵共有26^6种。其中所有矩阵的权值之和为105456.

思路：
要解决这个问题，我们需要计算所有 `n` 行 `m` 列的仅由小写字母组成的矩阵的权值之和。权值的定义是矩阵中包含 "r"、"e"、"d" 这三种字符的 2x2 子矩阵的数量。

### 分析步骤

1. **计算每个 2x2 子矩阵满足条件的概率：**
   - 一个 2x2 子矩阵有 4 个位置，每个位置可以是 26 个小写字母中的一个。
   - 我们需要确保在这 4 个位置中至少包含 "r"、"e"、"d" 这三个字符。
   - 使用容斥原理，满足条件的数量为：
     \[
     26^4 - 3 \times 25^4 + 3 \times 24^4 - 23^4 = 588
     \]

2. **总的 2x2 子矩阵数量：**
   - 对于 `n` 行 `m` 列的矩阵，总共有 `(n-1) \times (m-1)` 个 2x2 子矩阵。

3. **计算所有矩阵的权值之和：**
   - 每个 2x2 子矩阵满足条件的情况有 `588` 种。
   - 剩下的 `n*m - 4` 个位置可以是任意字母，所以总的组合数为 \(26^{n \times m - 4}\)。
   - 因此，总权值之和为：
     \[
     588 \times (n-1) \times (m-1) \times 26^{n \times m - 4} \mod (10^9 + 7)
     \]
   - 由于 `n` 和 `m` 可能很大（最多 \(10^9\)），需要使用快速幂算法，并利用费马小定理来处理指数部分的模运算。

### 实现代码

以下是使用 Python 实现的代码：

```python
MOD = 10**9 + 7
PHI = MOD - 1  # 因为 MOD 是质数

def compute_weight_sum(n, m):
    if n < 2 or m < 2:
        return 0

    term1 = (n - 1) % MOD
    term2 = (m - 1) % MOD

    # Compute (n * m) mod (MOD-1)
    nm_mod = (n % PHI) * (m % PHI) % PHI
    x = (nm_mod - 4) % PHI

    power = pow(26, x, MOD)

    result = 588 * term1 % MOD
    result = result * term2 % MOD
    result = result * power % MOD

    return result

# 读取输入
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n, m = map(int, input().split())
    print(compute_weight_sum(n, m))
```

### 代码说明

1. **输入读取：**
   - 从标准输入读取两个整数 `n` 和 `m`。

2. **边界条件处理：**
   - 如果 `n` 或 `m` 小于 2，则没有 2x2 子矩阵，直接返回 `0`。

3. **计算各个部分：**
   - 计算 `(n-1)` 和 `(m-1)` 对 `MOD` 取模。
   - 计算指数部分 `x = (n * m - 4) mod (MOD-1)`。
   - 使用 Python 内置的 `pow` 函数高效地计算 \(26^x \mod MOD\)。

4. **最终结果：**
   - 将所有部分相乘，并对 `MOD` 取模，得到最终结果。

### 示例验证

以示例输入 `2 3`：

- `(n-1) = 1`
- `(m-1) = 2`
- `x = (2 * 3 - 4) mod 10^9+6 = 2`
- `26^2 = 676`
- 最终结果 `588 * 1 * 2 * 676 mod 10^9+7 = 794976`

这与示例输出一致。