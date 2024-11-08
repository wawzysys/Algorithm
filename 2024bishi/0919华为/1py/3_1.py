import sys

def main():
    import sys
    data = sys.stdin.read().split()
    ptr = 0
    N, M, C = int(data[ptr]), int(data[ptr+1]), int(data[ptr+2])
    ptr += 3

    gr = [[] for _ in range(N)]
    for _ in range(N * M):
        if ptr + 2 >= len(data):
            break  
        a = int(data[ptr])
        b = int(data[ptr+1])
        c = int(data[ptr+2])
        if 0 <= a < N:
            gr[a].append((b, c))
        ptr += 3

    INF = -1 << 60
    fg = [[INF] * (C + 1) for _ in range(N)]

    for g in range(N):
        dp = [INF] * (C + 1)
        dp[0] = 0
        for b, c in gr[g]:
            for s in range(C, b - 1, -1):
                if dp[s - b] != INF:
                    dp[s] = max(dp[s], dp[s - b] + c)
        for s in range(1, C + 1):
            fg[g][s] = dp[s]

    dp_total = [INF] * (C + 1)
    dp_total[0] = 0

    for g in range(N):
        new_dp = [INF] * (C + 1)
        for c1 in range(C + 1):
            if dp_total[c1] == INF:
                continue
            for s in range(1, C - c1 + 1):
                if fg[g][s] != INF:
                    new_dp[c1 + s] = max(new_dp[c1 + s], dp_total[c1] + fg[g][s])
        dp_total = new_dp

    max_download = max(dp_total)
    if max_download == INF:
        print(-1)
    else:
        print(max_download)

if __name__ == "__main__":
    main()
