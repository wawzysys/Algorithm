def max_expos(n, k, nums):
    e = []
    for start, end in nums:
        e.append((start, 'start'))
        e.append((end + 1, 'end'))
    
    e.sort()
    
    a = 0
    b = 0
    c = 0
    
    for day, event_type in e:
        if event_type == 'start':
            a += 1
        else:
            a -= 1
        if a > 0 and b != day:
            c += min(a, k)
            b = day
    
    return c

# 测试样例
n, k = map(int, input().split())
nums = [tuple(map(int, input().split())) for _ in range(n)]
print(max_expos(n, k, nums))  # 应输出 4
