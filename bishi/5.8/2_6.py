alist=['capacity','write','read','query']
s1=input()
n=int(input())
c=[]
ca=[]#c中a的值
# c=[[1,2,6,1],[1,2,3,2],[1,2,2,4]]
# c.sort(key=lambda x: (-x[3],x[2]))
# c.pop()
def read(a):
    if a in ca:
        for i in c:
            i[2]+=1
        for i in c:
            if i[0]==a:
                i[2]=0
                i[3]+=1
def write(a,b):
    if a in ca:
        read(a)
    else:
        if n==len(ca):
            c.sort(key=lambda x: (-x[3],x[2]))
            z=c.pop()
            ca.remove(z[0])
        for i in c:
            i[2]+=1
        e=[]
        e.append(a)#localcekk
        e.append(b)#neigh
        e.append(0)#时间
        e.append(0)#次数
        c.append(e)
        ca.append(a)
def query(a):
    if a in ca:
        for i in c:
             if i[0]==a:
                    print(i[1])
    else:
        print(-1)
while True:
    try:
        s=input()
        # print(s)
        if s=='write:':
            x=int(input())
            # print(x)
            for _ in range(x):
                a, b=map(int,input().split())
                # print(a, b)
                write(a,b)
        if s=='read:':
            x=int(input())
            read(x)
            # print(x)
        if s=='query:':
            x=int(input())
            query(x)
    except:
        break
