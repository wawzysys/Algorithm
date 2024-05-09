class Solution:
    def combination(self, n, k):
        # 计算组合数 C(n, k)
        numerator = 1
        denominator = 1
        for i in range(k):
            numerator *= (n - i)
            denominator *= (i + 1)
        return numerator // denominator

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # 计算组合数 C(m+n, n)
        total_combinations = self.combination(zero + one, one)
        m = limit + 1
        x_0 = 0
        x_1 = 0
        if one < m and zero < m:
            return total_combinations
        if zero >= m:
            zero_1 = zero - limit
            x_0 = self.combination(zero_1 + one, one)
            if one < m:
                return total_combinations - x_0
            if one >= m:
                one_1 = one - limit
                x_1 = self.combination(zero + one_1, zero)
                return total_combinations - x_1 - x_0 + self.combination(zero_1 + one_1, zero_1)
        if one >= m:
            one_1 = one - limit
            x_1 = self.combination(zero + one_1, zero)
            if zero < m:
                return total_combinations - x_1
            if zero >= m:
                zero_1 = zero - limit
                x_0 = self.combination(zero_1 + one, one)
                return total_combinations - x_0 - x_1 + self.combination(zero_1 + one_1, zero_1)


