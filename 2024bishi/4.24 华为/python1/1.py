def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
def f(x):
    x += 1
def solve():
    a = list(map(int, input().split()))
    a.sort()
    x = int(input())
    
    def find(l, r):
        while l <= r:
            mid = (l + r) // 2
            if x == a[mid]:
                return True
            elif x > a[mid]:
                print("R", end="")
                l = mid + 1
            else:
                print("L", end="")
                r = mid - 1
        return False
    
    print("S", end="")
    ans = find(0, len(a) - 1)
    print("Y" if ans else "N")


if __name__ == '__main__':
    i = 0
    if i == 0:
        j = 1
        if j == 1:
            f(j)
        solve()
