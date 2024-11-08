# 定义一个函数来计算组合数 C(n, k) % mod

# 牛牛班级内有",个男同学和m个女同学:
# 现在老师想要组成一个包含k个同学的合唱队,
# 并且合唱队内至少需要包含3个男生和2个女牛牛牛想请你帮他计算出一共有多少种不同的方案组成合唱队,因为答案很大,
# 所以需要模上1000000007后输出.注意:两种不同的方案被认为不同当且仅当包含不同的个体时
mod = 1000000007
def factorial_mod(n, mod):
    """计算 n! 对 mod 取模的结果"""
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % mod
    return result
def inverse_mod(x, mod):
    """计算 x 在 mod 下的逆元，这里使用费马小定理，因为 mod 是质数"""
    return pow(x, mod - 2, mod)
def comb_mod(n, k, mod):
    """计算组合数 C(n, k) 对 mod 取模的结果"""
    if k > n or k < 0:
        return 0
    numerator = factorial_mod(n, mod)
    denominator = (factorial_mod(k, mod) * factorial_mod(n - k, mod)) % mod
    return (numerator * inverse_mod(denominator, mod)) % mod
n, m, k = map(int, input().split())
res = 0
for i in range(2, m + 1):
    if k - i >= 3:
        res += comb_mod(m, i, mod) * comb_mod(n, k - i, mod) 
print(res)
#n! / (n - k) ! / k !