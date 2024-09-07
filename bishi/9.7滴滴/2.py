def solve():
    m, n = map(int, input().split())
    print(m, n)
    # a = [float('inf')] * n
    # s = 0
    
    # for i in range(m):
    #     pre = 0
    #     cur_values = list(map(int, input().split())) 
    #     for j in range(n):
    #         cur = cur_values[j]
    #         a[j] = min(a[j], cur - pre)
    #         pre = cur
    #         if i == m - 1:
    #             s += a[j]
    
    # print(s)

solve()
