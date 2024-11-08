class Solution:
    def maxArea(self, height) -> int:
        ans = left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)
            if height[left] < height[right]:
                # height[left] 与右边的任意线段都无法组成一个比 ans 更大的面积
                left += 1
            else:
                # height[right] 与左边的任意线段都无法组成一个比 ans 更大的面积
                right -= 1
        return ans
    
a = Solution()

heights = [1, 2]

ans = a.maxArea(heights)
print(ans)
