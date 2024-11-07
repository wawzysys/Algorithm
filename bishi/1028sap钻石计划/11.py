import sys
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
T = int(input())
for _ in range(T):
    N = sint()
    x = lint()
    y = lint()
    
    if all(x1 == x[0] for x1 in x):
        print('undefined')
        continue
    
    points = sorted(zip(x, y), key=lambda p: (p[0], p[1]))
    x_sorted = [p[0] for p in points]
    y_sorted = [p[1] for p in points]
    
    y_min = y_sorted[0]
    x_min = x_sorted[0]
    max_s = float('-inf')
    
    for i in range(1, N):
        x_i, y_i = x_sorted[i], y_sorted[i]
        if x_i != x_min:
            s = (y_i - y_min) / (x_i - x_min)
            if s > max_s:
                max_s = s
        if y_i < y_min:
            y_min = y_i
            x_min = x_i
    
    y_max = y_sorted[-1]
    x_max = x_sorted[-1]
    for i in range(N - 2, -1, -1):
        x_i, y_i = x_sorted[i], y_sorted[i]
        if x_i != x_max:
            s = (y_i - y_max) / (x_i - x_max)
            if s > max_s:
                max_s = s
        if y_i > y_max:
            y_max = y_i
            x_max = x_i
    
    print(f"{max_s:.2f}")
