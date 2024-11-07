s1 = input()
s2 = input()
group = {}
g1 = {'w','i','r','e','@','c','o','m'}
g2 = {'h','f','v','#','g','b','t','s'}
for c in g1:
    group[c] = 0
for c in g2:
    group[c] = 1
n, m = len(s1), len(s2)
prev = list(range(m+1))
curr = [0]*(m+1)
for j in range(m+1):
    prev[j] = j*3
for i in range(1, n+1):
    curr[0] = i*3
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            curr[j] = prev[j-1]
        else:
            g1_val = group.get(s1[i-1], 2)
            g2_val = group.get(s2[j-1], 2)
            if g1_val == g2_val:
                rc = 1
            elif g1_val !=2 and g2_val !=2:
                rc = 2
            else:
                rc = 3
            curr[j] = min(prev[j] +3, curr[j-1]+3, prev[j-1]+rc)
    prev, curr = curr, prev
print(prev[m])
