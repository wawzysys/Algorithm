from typing import List
import math

class Solution:
    def MySort(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return arr
        mid = math.floor(len(arr) / 2)
        left, right = arr[:mid], arr[mid:]
        return self.merge(self.MySort(left), self.MySort(right))

    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
        return result

def main():
    solution = Solution()
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]  # 示例数组，可根据需要修改
    sorted_arr = solution.MySort(arr)
    print( sorted_arr)

if __name__ == "__main__":
    main()
