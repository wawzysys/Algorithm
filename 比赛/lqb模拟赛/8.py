target = "LANQIAO"
s = input().strip()

i, j = 0, 0
while j < len(s):
    if target[i] == s[j]:
        i += 1
    j += 1
    if i == len(target):
        print("YES")
        break
else:
    print("NO")