from collections import *
inf = 10**9
class Solution:
    def maxPointsInsideSquare(self, points, s: str) -> int:
        dict = defaultdict(list)
        for c, [x, y] in zip(s, points):
            dict[c].append(max(abs(x), abs(y)))
        up = inf
        print(dict)
        de = []
        for c in dict:
            dict[c].sort()
            if len(dict[c]) > 1:
                if  dict[c][0] == dict[c][1]:
                    de.append(c)
                
                up = min(up, dict[c][1])
        for c in  de:
            del dict[c]
        ans = 0
        for c in dict:
            if dict[c][0] < up:
                ans += 1
        return ans


# p = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]
# s ="abdca"
# p = [[1,1],[-2,-2],[-2,2]]
# s = "abb"
p = [[1,1],[-1,-1],[2,-2]]
s = "ccd"
sc = Solution()
print(sc.maxPointsInsideSquare(p,s))