sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def main():
    T = sint()
    for _ in range(T):
        n, m = mint()
        total = 0
        D = []
        Y = []
        for i in range(n+m+1):
            x, y = mint()
            Y.append(y)
            D.append((x - y, i))
            total += y
        D_sorted = sorted(D, reverse=True)
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + D_sorted[i][0]
        ranks = [0]*(n+m+1)
        for idx, (_, i) in enumerate(D_sorted):
            ranks[i] = idx
        res = []
        for i in range(n+m+1):
            sy = total - Y[i]
            if ranks[i] < n:
                if n < len(D_sorted):
                    sx = P[n] - D[i][0] + D_sorted[n][0]
                else:
                    sx = P[n] - D[i][0]
            else:
                sx = P[n]
            res.append(str(sy + sx))
        print(' '.join(res))
main()
