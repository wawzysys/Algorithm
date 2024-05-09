class Solution:
    def getmethod(self, head : ListNode, colors : str) - > int:
        mod = 10 ** 9 + 7
        ListNode temp = head
        i, j, sum = 0, 0, 0
        arr = [0 for _ in range(100005)]
        while(temp != None):
            ft = temp.val
            if colors[i] =='R':
                sum += ft
                sum %= 2
            else:
                j += 1
                arr[j] = ft
            temp = temp.next
            i += 1
        ans = [[0, 0] for _ in range(100005)]
        ans[0][0] = 1
        ans[0][1] = 0
        for x in range(1, j + 1):
            if arr[x] % 2 ==  1:
                ans[x][0] = (ans[x - 1][1] + ans[x - 1][0]) % mod
                ans[x][1] = (ans[x - 1][1] + ans[x - 1][0]) % mod
            else:
                ans[x][0] = (2 * ans[x - 1][0]) % mod
                ans[x][1] = (2 * ans[x - 1][1]) % mod
        return ans[j][sum % 2]