
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy = energy[::-1]
        sum = [[0, -inf] for _ in range(k)]
        ans = -inf
        for i, num in enumerate(energy):
            sum[i % k][0] += num
            sum[i % k][1] = max(sum[i % k][1], sum[i % k][0])
            ans = max(ans, sum[i % k][1])
        return ans
