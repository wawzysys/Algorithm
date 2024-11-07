s1=input()
s2=input()
g1={'w','i','r','e','@','c','o','m'}
g2={'h','f','v','#','g','b','t','s'}
m,n=len(s1),len(s2)
prev = list(range(n+1))
for i in range(1, m+1):
    curr = [i*3] + [0]*n
    for j in range(1, n+1):
        if s1[i-1]==s2[j-1]:
            cost=prev[j-1]
        else:
            if (s1[i-1] in g1 and s2[j-1] in g1) or (s1[i-1] in g2 and s2[j-1] in g2):
                rep=1
            elif (s1[i-1] in g1 and s2[j-1] in g2) or (s1[i-1] in g2 and s2[j-1] in g1):
                rep=2
            else:
                rep=3
            cost = min(prev[j-1]+rep, prev[j]+3, curr[j-1]+3)
        curr[j]=cost
    prev=curr
print(prev[n])
