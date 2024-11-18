import sys, bisect
n = int(input())
arr = sorted(list(map(int, input().split())))
N=int(input())
idx = bisect.bisect_left(arr,N)
cnt =n - idx
l=0
r=idx-1
while l < r:
    if arr[l] + arr[r] >=N:
        cnt +=1
        l +=1
        r -=1
    else:
        l +=1
print(cnt)


