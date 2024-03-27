s=input()
n=len(s)
a=[0]*(n+1)
a[1:n+1]=list(s)
y={'a','e','i','o','u'}
t=[0]*(n+1)
h=0
for i in range(1,n+1):
    if a[i] in y:
        t[i]=t[i-1]+1
    else:
        t[i]=t[i-1]
for i in range(1,n):
    if (t[i]-(i-t[i]))==((t[n]-t[i])-(n-i-(t[n]-t[i]))) or (t[i]-(i-t[i]))==-((t[n]-t[i])-(n-i-(t[n]-t[i]))):
        h+=1
        # print(a[i])
print(h)