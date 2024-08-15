from collections import defaultdict

def fisbig(c: str) -> bool:
    return 'A' <= c <= 'Z'

def fissmall(c: str) -> bool:
    return 'a' <= c <= 'z'

def isdigit(c: str) -> bool:
    return '0' <= c <= '9'

def nottarget(c):
    return fisbig(c) or fissmall(c) or isdigit(c)

ss = 0
ll = 0
num = 0
idx = 0
b = defaultdict(int)

while True:
    try:
        s = input()
        if not s:  # 如果输入为空字符串，则退出循环
            break
        print(s)
        for c in s:
            if not nottarget(c):
                if len(b) == 3:
                    ss += 5
                elif len(b) == 2:
                    if 3 in b:
                        ss += 3
                    else:
                        ss += 1
                ll += idx
                if len(b) != 0:
                    num
                b.clear()  
                idx = 0
            else:
                if fisbig(c):
                    b[1] += 1
                elif fissmall(c):
                    b[2] += 1
                elif isdigit(c):
                    b[3] += 1
                idx += 1
    except EOFError:  # 捕获文件结束错误
        break

print(ss)
print(ll, num)