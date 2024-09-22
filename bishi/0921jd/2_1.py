import sys
import bisect

def main():
    import sys, bisect
    input = sys.stdin.read().split()
    n = int(input[0])
    cars = []
    for i in range(n):
        x = int(input[1 + 2 * i])
        v = int(input[1 + 2 * i + 1])
        cars.append((x, v))
    
    cars.sort(key=lambda car: car[0])
    
    speeds = [v for _, v in cars]
    
    dp = []
    for v in speeds:
        idx = bisect.bisect_right(dp, v)
        if idx == len(dp):
            dp.append(v)
        else:
            dp[idx] = v
    
    L = len(dp)
    print(n - L)

if __name__ == "__main__":
    main()
