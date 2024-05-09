def find_zeros_positions(n):
    positions = []
    zero_count = 0
    position = 0
    while n:
        if not n & 1:
            positions.append(position)
            zero_count += 1
        n >>= 1
        position += 1
    return zero_count, positions
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        c, pos = find_zeros_positions(x)
        x_length = x.bit_length()
        # print("{}:{}".format('x_length', x_length))
        for i in range(30):
            pos.append(x_length + i)
        # print(pos)
        ans = x
        # print(ans)
        j = 0
        n = n - 1
        while n:
            ans += (n & 1) * (1 << pos[j])
            n >>= 1
            j += 1
        return ans
# num = int(input())
# zeros_count, zeros_positions = find_zeros_positions(num)
# print("{}:{}".format(zeros_count, zeros_positions))
cl = Solution()
n = 3
x = 4
print(cl.minEnd(n, x))
n = 2
x =7
print(cl.minEnd(n, x))
# print(1 << 4)