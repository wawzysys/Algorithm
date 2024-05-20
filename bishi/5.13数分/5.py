
s = input()
def sp(s):
    d = dict()
    a = list(s.split(";"))
    for tep in a:
        a, b = tep.split(":")
        b = int(b)
        d[a] = b
    return d
print(sp(s))
            
    
    