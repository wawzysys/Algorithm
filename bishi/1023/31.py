sint = lambda:int(input())
mint = lambda:map(int,input().split())
lint = lambda:list(map(int,input().split()))
def f():
    n_d =lint()
    if len(n_d)<2:
        print("-1")
        return
    n,d=n_d[:2]
    nums=[]
    while len(nums)<n:
        nums +=lint()
    nums.sort()
    ans=[0]*(n+1)
    res=[0]*(n+1)
    op=2
    for i in range(2,n+1):
        j=i-1
        t=i-2
        tmp=1 if(nums[j]-nums[t]<=d) else 0
        op +=1
        if ans[t]+tmp>ans[j]:
            ans[i]=ans[t]+tmp
            res[i]=res[t]+(nums[j]-nums[t])
            op+=2
        elif ans[t]+tmp<ans[j]:
            ans[i]=ans[j]
            res[i] = res[j]
            op+=3
        else:
            ans[i]=ans[j]
            op+=4
            if tmp==1:
                a=res[j]
                b=res[t]+(nums[j]-nums[t])
                res[i]=min(a,b)
                op +=7
            else:
                res[i]=res[j]
                op+=6
    if ans[n]==0:
        print("-1")
    else:
        print(res[n])
f()