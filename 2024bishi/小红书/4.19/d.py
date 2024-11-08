# 导入所需的库
import sys

def main():
    # 读取n，并转换为整数
    n = int(input())
    a = list(map(int, input().split()))
    
    sum_a = sum(a)  # 计算列表a的和
    b = sorted(a, reverse=True)  # 对a进行降序排序，存储到b
    s = n * b[0] - sum_a  # 计算目标和与当前和的差值
    
    for i in range(n):
        if a[i] == b[0]:
            print(sum_a)
            continue
        if n == 2:
            print("-1")
            continue
        
        a[i] += 1
        diff = b[0] - a[i]
        cur = s - (b[0] - a[i] + 1)
        ans = sum_a + 1
        
        if diff <= cur:
            ans += 2 * diff
            print(ans)
        else:
            ans += 2 * cur
            a[i] += cur
            l, r = 1, 1e9
            while l <= r:
                mid = (l + r) // 2
                t = mid // (n - 1)
                if mid % (n - 1):
                    t += 1
                if a[i] + mid < t + b[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            ans += 2 * int(l)
            print(ans)

if __name__ == "__main__":
    main()
