import sys
d=map(int,sys.stdin.read().split())
n,m=next(d),next(d)
a=[0]*(m+2)
for _ in range(n):
    L,R=next(d),next(d)
    a[L]+=1
    a[R+1]-=1
s=mx=0
for i in range(1,m+1):
    s+=a[i]
    if s>mx: mx=s
print(mx)
