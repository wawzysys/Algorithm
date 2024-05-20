alist=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18','a19','a20','a21','a22','a23','a24','a25','a26','a27','a28','a29','a0','a30','a31']
conut={}
def chars(s):
    if s in alist:
        return conut[s]
    else:
        return int(s)
while True:
    try:
        s=input().split()
        if s[0]=='MOV':
            if s[2] not in alist:
                conut[s[1]]=int(s[2])
            else:
                conut[s[1]]=conut[s[2]]
        if s[0]=='ADD':
            conut[s[1]]=chars(s[2])+chars(s[3])
        if s[0]=='SUB':
            conut[s[1]]=chars(s[2])-chars(s[3])
        if s[0]=='NUL':
            conut[s[1]]=chars(s[2])*chars(s[3])
        if s[0]=='DIV':
            conut[s[1]]=int(chars(s[2])/chars(s[3]))
        if s[0]=='PRINT':
            print (chars(s[1]))
            
    except:
        break