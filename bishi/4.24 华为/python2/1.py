class BinarySearch:
    def __init__(self, arr):
        self.arr = sorted(arr)

    def search(self, x):
        def find(l, r):
            if l > r:
                return False
            mid = (l + r) // 2
            if x == self.arr[mid]:
                return True
            elif x > self.arr[mid]:
                print("R", end="")
                return find(mid + 1, r)
            else:
                print("L", end="")
                return find(l, mid - 1)

        return find(0, len(self.arr) - 1)

def solve():
    arr = list(map(int, input().split()))
    x = int(input())
    bs = BinarySearch(arr)
    print("S", end="")
    ans = bs.search(x)
    if ans:
        print("Y")
    else:
        print("N")

if __name__ == '__main__':
    solve()
