
# vowels = set("aeiouAEIOU")
# t = int(input())
# s = input()
# n = len(s)
# ans = 0
# num = 0
# l = 0
# for r in range(n):
#     if s[r] not in vowels:
#         num += 1
    
#     while num > t:
#         if s[l] not in vowels:
#             num -= 1
#         l += 1
#     if num == t:
#         if l < r and l < n and r < n and s[l] in vowels and s[r] in vowels :
#             ans = max(ans, r - l + 1)

# print(ans)


from re import L
vowels = set("aeiouAEIOU")
t = int(input())
s = input()
n = len(s)
ans = 0
num = 0
l = 0
for r in range(n):
    if s[r] not in vowels:
        num += 1
    
    while num > t:
        if s[l] not in vowels:
            num -= 1
        l += 1
    if num == t:
        if l <= r and l < n and r < n and s[l] in vowels and s[r]in vowels:
            ans = max(ans,r - l + 1)

print(ans)
