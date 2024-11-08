import sys

def main():
    n, q = map(int, input().split())
    s = input()
    abc = [0] * (n + 1)
    for i in range(1, n + 1):
        abc[i] = abc[i - 1] + (1 if s[i - 1] == '0' else 0)
    result = []
    for _ in range(q):
        l, r, k = map(int, input().split())
        cnt0 = abc[r] - abc[l - 1]
        if k <= cnt0:
            result.append('0')
        else:
            result.append('1')
    print(''.join(result))

main()
