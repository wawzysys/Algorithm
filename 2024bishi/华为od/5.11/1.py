import sys


class Rect:
    def __init__(self):
        self.minRow = sys.maxsize
        self.maxRow = -sys.maxsize
        self.minCol = sys.maxsize
        self.maxCol = -sys.maxsize

    def setRow(self, row):
        self.minRow = min(self.minRow, row)
        self.maxRow = max(self.maxRow, row)

    def setCol(self, col):
        self.minCol = min(self.minCol, col)
        self.maxCol = max(self.maxCol, col)


# 输入获取
m, n = map(int, input().split())

rects = {}

for i in range(m):
    nums = list(map(int, input().split()))
    for j in range(n):
        num = nums[j]

        if num > 0:
            rects.setdefault(num, Rect())
            rects[num].setRow(i)
            rects[num].setCol(j)

maxArea = 0
for num in rects:
    rect = rects[num]

    maxArea = max(maxArea, (rect.maxRow - rect.minRow + 1) * (rect.maxCol - rect.minCol + 1))

print(maxArea)