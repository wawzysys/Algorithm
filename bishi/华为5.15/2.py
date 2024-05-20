def f(pattern: str) -> str:
    def pr(p: str) -> str:
        i = 0
        result = ''
        while i < len(p):
            if p[i] == 'N':
                result += 'b'
                i += 1
            elif p[i] == 'A':
                result += 'a'
                i += 1
            elif p[i].isdigit():
                j = i
                while j < len(p) and p[j].isdigit():
                    j += 1
                count = int(p[i:j])
                if p[j] == '(':
                    depth = 1
                    k = j + 1
                    while k < len(p) and depth > 0:
                        if p[k] == '(':
                            depth += 1
                        elif p[k] == ')':
                            depth -= 1
                        k += 1
                    subpattern = pr(p[j + 1:k - 1])
                    result += subpattern * count
                    i = k
            else:
                i += 1
        return result
    return pr(pattern)
pa = input()
pa = f(pa)
s = input()
tep = ""
for c in s:
    if c.isdigit():
        tep += "b"
    else:
        tep += "a"

n = len(tep)
n2 = len(pa)
base = 131
mod = 10 ** 9 + 7
h = [0] * (n + 1)
p = [1] * (n + 1)
if n2 > n:
    print("!")
for i in range(1, n + 1):
    p[i] = p[i - 1] * base % mod
    h[i] = h[i - 1] * base + ord(tep[i - 1])
    h[i] %= mod
h1 = [0] * (n2 + 1)
for i in range(1, n2 + 1):
    h1[i] = h1[i - 1] * base + ord(pa[i - 1])
    h1[i] %= mod
def get_hash(l, r):
    res = h[r] - h[l - 1] * p[r - l + 1]
    return res % mod
flag = False
for i in range(1, n):
    j = i + n2 - 1
    if j > n:
        break
    if get_hash(i, j) == h1[n2]:
        flag = True
        print(s[i - 1: j])
        break
if not flag:
    print("!")