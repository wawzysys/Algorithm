#判断是否是凸多边形
#叉乘
#相邻三个点的向量叉乘，如果叉乘结果的符号不一致，则不是凸多边形

from typing import List

class Solution:
    def is_convex(self, points: List[List[int]]) -> bool:
        n = len(points)
        if n < 3:
            return False 

        last_sign = 0

        for i in range(n):
            dx1 = points[(i+1) % n][0] - points[i][0]
            dy1 = points[(i+1) % n][1] - points[i][1]
            dx2 = points[(i+2) % n][0] - points[(i+1) % n][0]
            dy2 = points[(i+2) % n][1] - points[(i+1) % n][1]

            cross_product = dx1 * dy2 - dy1 * dx2
            
            # 检查叉积符号
            if cross_product != 0:
                if last_sign == 0:
                    last_sign = cross_product
                elif last_sign * cross_product < 0:
                    return False

        return True
from typing import List

class Solution:
    def is_convex(self, points: List[List[int]]) -> bool:
        prev = 0
        n = len(points)
        
        for i in range(n):
            x1 = points[i][0] - points[(i + 1) % n][0]
            y1 = points[i][1] - points[(i + 1) % n][1]
            x2 = points[i][0] - points[(i + 2) % n][0]
            y2 = points[i][1] - points[(i + 2) % n][1]
            
            cur = x1 * y2 - x2 * y1
            
            if cur != 0:  # 如果两向量不共线
                if cur * prev < 0:  # 如果当前向量的转向与前一个向量的转向不一致
                    return False
                prev = cur
                
        return True

# 使用示例
sol = Solution()
points = [[0, 0], [0, 1], [1, 1], [1, 0]]
print(sol.is_convex(points))  # 应该返回 True

# 使用示例
a = Solution()
p = [[0, 0], [0, 1], [1, 1], [1, 0]]
p1 = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]
print(a.is_convex(p1))  # 应该返回 True
