#华为手撕
def quicksort(A, start, end):
    # 基本情况：如果分区大小为1或0个元素，则无需操作
    if start >= end:
        return
    
    # 初始化当前分区的指针
    left, right = start, end
    # 选择中间元素作为基准点
    pivot = A[start + (end - start) // 2]

    # 围绕基准点分区数组
    while left <= right:
        # 向右移动左指针，直到找到一个大于基准点的元素
        while left <= right and A[left] < pivot:
            left += 1
        # 向左移动右指针，直到找到一个小于基准点的元素
        while left <= right and A[right] > pivot:
            right -= 1
        # 当左指针仍然在右指针左侧时，交换元素
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    # 对基准左侧的元素进行递归排序
    quicksort(A, start, right)
    # 对基准右侧的元素进行递归排序
    quicksort(A, left, end)

def main():
    # 输入数组长度
    length = int(input())
    # 输入数组元素
    nums = [int(i) for i in input().split()]
    # 对整个数组进行快速排序
    quicksort(nums, 0, length - 1)
    # 输出排序后的数组，每个元素后面跟一个空格
    for j in nums:
        print(j, end=' ')

# 调用main函数开始执行
main()
