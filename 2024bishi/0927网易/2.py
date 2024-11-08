import sys
mint = lambda: map(int, sys.stdin.readline().split())
def main():
    n, m, q = mint()
    g = list(range(n))       
    shift_offsets = [0] * n        
    for _ in range(q):
        t, x, y = mint()
        if t == 1:
            x =  x - 1
            y =  y - 1
            g[x], g[y] = g[y], g[x]
        elif t == 2:
            x = x - 1
            y = y
            row = g[x]
            shift_offsets[row] = (shift_offsets[row] + y) % m
        elif t == 3:
            x = x - 1
            y = y
            row = g[x]
            s = shift_offsets[row]
            pos = (s + y - 1) % m + 1
            number = row * m + pos
            print(number)

main()
