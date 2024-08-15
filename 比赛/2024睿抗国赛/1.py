import re
def fisbig(c: str) -> bool:
    return 'A' <= c <= 'Z'

def fissmall(c: str) -> bool:
    return 'a' <= c <= 'z'

def isdigit(c: str) -> bool:
    return '0' <= c <= '9'
def get_score(k: str) -> int:
    a = any(fisbig(c) for c in k)
    b = any(fissmall(c) for c in k)
    c = any(isdigit(c) for c in k)
    
    if a and b and c:
        return 5
    elif (a and c) or (b and c):
        return 3
    elif a and b:
        return 1
    else:
        return 0
def f(code: str):
    pp = r'\b[A-Za-z0-9]+\b'
    kk = re.findall(pp, code)
    
    aa = 0
    ll = 0
    
    for k in kk:
        score = get_score(k)
        aa += score
        ll += len(k)
    
    return aa, ll, len(kk)

code = ""
while True:
    try:
        line = input().strip()
        if not line:
            break
        code += " " + line
    except EOFError:
        break

aa, ll, num = f(code)
print(aa)
print(f"{ll} {num}")