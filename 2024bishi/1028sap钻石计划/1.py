sint = lambda: int(input())
lint = lambda: list(map(int, input().split()))
def solve():
    n = sint()
    x = lint()
    y = lint()
    if all(x1 == x[0] for x1 in x):
        print("undefined")
        return 
    m = float('-inf')
    for i in range(n):
        for j in range(n):
            xi, yi = x[i], y[i]
            xj, yj = x[j], y[j]
            if xi != xj:
                k = (yj - yi) / (xj - xi)
                if k > m:
                    m = k
    print(f"{m:.2f}")
    
t = sint()
for _ in range(t):
    solve()