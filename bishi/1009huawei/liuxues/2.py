n = int(input())
seq=list(map(int, input().split()))
end=[0]*65536
total=0
for s in seq:
    if s>0 and end[s-1]>0:
        end[s-1]-=1
    else:
        total+=1
    end[s]+=1
print(total)
