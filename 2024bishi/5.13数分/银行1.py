class Solution:
    def countOne(self, numbers: List[int]) -> int:
        def int_count_one(n):
            bin_n = bin(n)
            num = str(bin_n).count("1")
            return num
        
        def count(n):
            ans = 0
            while n > 1:
                n = int_count_one(n)
                ans += 1
            return ans
        
        ans = 0
        for c in numbers:
            ans += count(c)
        return ans

# 创建Solution的实例
sol = Solution()
print(sol.countOne([9, 2]))  # 输出结果
print(sol.countOne([1, 3, 5]))
