def solve(nums : list) -> int:
    nums.sort()
    ans = sum(nums[1:-1]) // 3
    return ans

print(solve([1, 2, 3, 4, 5]))