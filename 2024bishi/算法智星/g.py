def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input().strip()
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        ans = n % 2
        for i in range(26):
            ans = max(ans, cnt[i] * 2 - n)
        print(ans)

if __name__ == "__main__":
    main()
