import math

MOD = 10**9 + 7

def fact(x):
    return math.factorial(x) % MOD

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 解析输入
    if len(data) < 4:
        # 假设输入只有三行：n, m, q 和 q 个 d_i
        n, m, q = map(int, data[:3])
        ds = list(map(int, data[3:]))
    else:
        # 如果有四个参数：n, m, q, t 和 q 个 d_i
        n, m, q, t = map(int, data[:4])
        ds = list(map(int, data[4:]))
    
    total_tickets = m * n
    total_players = q + 1
    
    if total_tickets >= total_players:
        res = fact(total_players)
    else:
        res = (total_tickets * fact(q)) % MOD
    
    print(res)

# 示例测试
if __name__ == "__main__":
    solve()
