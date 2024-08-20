from collections import defaultdict

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(list)
    
    for i in range(n):
        cnt[a[i]].append(i + 1)
    
    q = int(input())
    
    while q > 0:
        q -= 1
        x, y = map(int, input().split())
        if x in cnt:
            cnt[y].extend(cnt[x])
            del cnt[x]
    
    result = [0] * (n + 1)
    for x, idx in cnt.items():
        for i in idx:
            result[i] = x
    
    print(" ".join(map(str, result[1:])))
    
main()
