n = int(input())
num = list(range(n + 1)) + [0]
l = n 
r = n + 1
ss = 0
ans = 0
def f(l, r):
    for i in range(l, r + 1):
        if i == r:
            print(i)
        else:
            print(i,end='+')
while r >= 1:
    r -= 1
    ss += num[r]
    while ss > n:
        ss -= num[l]
        l -= 1
    if ss == n and r != 0:
        ans += 1
        print(f"{n}=",end='')
        f(r, l)
print(f"Result:{ans}")