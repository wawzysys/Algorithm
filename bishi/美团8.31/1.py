
import sys
input=lambda:sys.stdin.readline().strip()
def solve(n, k, positions):
    positions.sort()
    low, high = 1, k
    
    def check(mid):
        a = []
        b = []
        ans = 0
        for c in positions:
            a.append([c, c + mid - 1])
        for l, r in a:
            if not b or l > b[-1][1]:
                b.append([l, r])
            else:
                b[-1][1] = max(b[-1][1], r)
        
        for l, r in b:
            ans += r - l + 1
        return ans >= k
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid  
        else:
            low = mid + 1  
    
    return low
n, k = map(int, input().split())
positions = list(map(int, input().split()))
print(solve(n, k, positions))
