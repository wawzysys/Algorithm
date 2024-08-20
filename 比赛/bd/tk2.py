from typing import List

class Solution:
    def getSolution(self, n: int) -> List[str]:
        self.strl = []
        self.hannoi(n, 'left', 'mid', 'right')
        return self.strl

    def hannoi(self, n, a, b, c):
        if n == 1:
            self.strl.append('move from %s to %s' % (a, c))
        else:
            self.hannoi(n-1, a, c, b)
            str2 = 'move from %s to %s' % (a, c)
            self.strl.append(str2)
            self.hannoi(n-1, b, a, c)

if __name__ == "__main__":
    solution = Solution()
    n = 3  # 设置汉诺塔的盘子数量
    result = solution.getSolution(n)
    print("移动步骤如下:")
    for step in result:
        print(step)
