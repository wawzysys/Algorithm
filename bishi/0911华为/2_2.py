class solution:
    def f(self, n, boxes):
        bb = []
        for a, b, c in boxes:
            bb.append((a, b, c))
        bb.sort(key=lambda x: (-x[0], -x[1], -x[2]))
        dp = [0] * n
        for i in range(n):
            dp[i] = bb[i][2]  
        for i in range(n):
            for j in range(i):
                if bb[j][0] > bb[i][0]:
                    if bb[j][1] > bb[i][1]: 
                        if bb[j][2] > bb[i][2]:
                            dp[i] = max(dp[i], dp[j] + bb[i][2])
        
        return max(dp)

n = int(input())
boxes = []
for _ in range(n):
    a, b, c = map(int, input().split())
    boxes.append((a, b, c))
bb = solution()
print(bb.f(n, boxes))
