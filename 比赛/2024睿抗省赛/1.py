n, w = map(int, input().split())
wendu = list(map(int, input().split()))
w = w % 7
ans1 = 0
ans2 = 0
for i in range(n):
    if wendu[i] >= 35 and w != 4:
        ans1 += 1
    if wendu[i] >= 35 and w == 4:
        ans2 += 1
    w = (w + 1) % 7
print(ans1, ans2)
