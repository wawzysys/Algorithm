
def main():
    T = int(input())
    for j in range(T):
        s = input()
        n = len(s)
        ans = 0
        for i in range(n):
            if i % 2 == 0 and s[i] == 'B':
                ans += 1
            if i % 2 == 1 and s[i] == 'A':
                ans += 1
        ans = min(ans, n - ans)
        print(ans)



if __name__ == '__main__':
    main();