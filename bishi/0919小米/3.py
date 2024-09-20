def canMakeSorted(a, b, order):
    n = len(a)
    if order == "asc":
        prev = float('-inf')
        for i in range(n):
            val1, val2 = a[i], b[i]
            canPickVal1 = val1 >= prev
            canPickVal2 = val2 >= prev
            if not canPickVal1 and not canPickVal2:
                return False
            if canPickVal1 and canPickVal2:
                prev = min(val1, val2)
            elif canPickVal1:
                prev = val1
            else:
                prev = val2
        return True
    else:  # "desc"
        prev = float('inf')
        for i in range(n):
            val1, val2 = a[i], b[i]
            canPickVal1 = val1 <= prev
            canPickVal2 = val2 <= prev
            if not canPickVal1 and not canPickVal2:
                return False
            if canPickVal1 and canPickVal2:
                prev = max(val1, val2)
            elif canPickVal1:
                prev = val1
            else:
                prev = val2
        return True

def solve(a, b):
    return (canMakeSorted(a, b, "asc") or
            canMakeSorted(a, b, "desc") or
            canMakeSorted(b, a, "asc") or
            canMakeSorted(b, a, "desc"))

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if solve(a, b):
        print("YES")
    else:
        print("NO")
