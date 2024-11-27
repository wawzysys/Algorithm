# 读取输入
n = int(input())
a = list(map(int, input().split()))

# 初始化 min_even 为一个很大的偶数
min_even = 1000001

# 遍历数组
for i in range(n):
    if a[i] % 2 == 0 and a[i] < min_even:
        min_even = a[i]

# 输出结果
print(min_even)