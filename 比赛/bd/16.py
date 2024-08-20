import sys
from collections import deque

class Read:
    def __init__(self):
        self.st = sys.stdin

    def nextInt(self):
        return int(self.st.readline().strip())

def main():
    read = Read()
    n = read.nextInt()
    dp = [0] * (n + 1)
    ue = deque()
    dp[0] = 1  # 设置初始状态为1表示从0开始一步
    ue.append(0)

    while ue:
        current = ue.popleft()
        if current * 3 <= n and dp[current * 3] == 0:
            dp[current * 3] = dp[current] + 1
            ue.append(current * 3)
        if current + 1 <= n and dp[current + 1] == 0:
            dp[current + 1] = dp[current] + 1
            ue.append(current + 1)

    # 打印目标数n的最小操作次数减1（因为初始状态为1）
    print(dp[n] - 1)

if __name__ == "__main__":
    main()
