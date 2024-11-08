import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0]*(self.size + 2)
    
    def update(self, index, value=1):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        res = 0
        while index >0:
            res += self.tree[index]
            index -= index & -index
        return res

def main():
    T = sint()
    for _ in range(T):
        n = sint()
        a = lint()
        max_a = max(a) if a else 0
        ft = FenwickTree(max_a)
        freq = [0]*(max_a +2)
        ability =0
        max_ability =0
        for i in range(n):
            current = a[i]
            if i ==0:
                pass
            else:
                C_less = ft.query(current -1)
                C_equal = freq[current]
                C_greater = i - (C_less + C_equal)
                delta = C_less - C_greater
                ability += delta
                if ability > max_ability:
                    max_ability = ability
            ft.update(current)
            freq[current] +=1
        print(max_ability, ability)
main()