# def solve(nums):
#     mm = max(nums)
#     ops = [float('inf')] * (mm + 1)
#     ops[0] = 0 
#     for i in range(1, mm + 1):
#         if i >= 1:
#             ops[i] = min(ops[i], ops[i - 1] + 1)
#         if i % 2 == 0:
#             ops[i] = min(ops[i], ops[i // 2] + 1)
#     ans = 0
#     for num in nums:
#         ans = max(ans, ops[num])
    
#     return ans
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = [0] + list(map(int, input().split()))
#     print(sum(max(a[i] - a[i-1], 0) for i in range(1, len(a))))
#     # result = solve(b)
#     # print(result)


ops = [1, 2, 3, 1, 2]

max_prefix = 0
total_ops = 0
for i in range(len(ops)):
    if ops[i] > max_prefix:
        total_ops += ops[i] - max_prefix
    max_prefix = ops[i]
print(total_ops)