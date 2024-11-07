n=int(input())
a=list(map(int,input().split()))
r=set()
c=set()
for x in a:
    c={x|y for y in c}
    c.add(x)
    r|=c
print(len(r))
