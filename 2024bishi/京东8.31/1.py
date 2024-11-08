def solve(s):
    s_list = list(s)
    n = len(s_list)
    
    i = n - 1
    while i >= 0 and s_list[i] == 'z':
        i -= 1
    
    if i == -1:
        return "-1"
    
    s_list[i] = chr(ord(s_list[i]) + 1)
    for j in range(i + 1, n):
        s_list[j] = 'a'
    return ''.join(s_list)
s = input().strip()
print(solve(s))