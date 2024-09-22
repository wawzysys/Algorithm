import sys
from math import gcd

RI = lambda: map(int, sys.stdin.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.readline().strip().split())
RILST = lambda: list(RI())

class KmpclzZwba:
    def __init__(self, t):
        self.t = t
        n = len(t)
        self.pi = pi = [0] * n
        j = 0
        for i in range(1, n):
            while j and t[i] != t[j]:
                j = pi[j - 1] 
            j += t[i] == t[j] 
            pi[i] = j

    def find_all_yield(self, s):
        n, t, pi, j = len(self.t), self.t, self.pi, 0
        for i, v in enumerate(s):
            while j and v != t[j]:
                j = pi[j - 1]
            j += v == t[j]
            if j == n:
                yield i - j + 1
                j = pi[j - 1]

    def find_one(self, s):
        for ans in self.find_all_yield(s):
            return ans
        return -1
class ModCombAUafv:
    def __init__(self, n, p):
        self.p = p
        self.inv_f, self.fact = [1] * (n + 1), [1] * (n + 1)
        inv_f, fact = self.inv_f, self.fact
        for i in range(2, n + 1):
            fact[i] = i * fact[i - 1] % p
        inv_f[-1] = pow(fact[-1], p - 2, p)
        for i in range(n, 0, -1):
            inv_f[i - 1] = i * inv_f[i] % p

    def combATvimfr(self, m, r):
        if m < r or r < 0:
            return 0
        return self.fact[m] * self.inv_f[r] % self.p * self.inv_f[m - r] % self.p
class ModPreMulccJond:
    def __init__(self, a, p):
        n = len(a)
        self.p = p
        self.fact = pre = [1] * (n + 1)
        self.inv = inv = [1] * (n + 1)
        for i, v in enumerate(a, start=1):
            pre[i] = pre[i - 1] * v % p

        inv[-1] = pow(pre[-1], p - 2, p)
        for i in range(n - 1, -1, -1):
            inv[i] = a[i] * inv[i + 1] % p

    def mul_intervalclzWyfupj(self, l, r):
        return self.fact[r + 1] * self.inv[l] % self.p
# aiocm rywitx 
# ldbytq cssukj dhov fzzad yuhsa 
# lpyhgrut okn 
# yor zcplft 
# cgbageax 
# vkpzsu dqdpemh 
# fjharz 
# xkridc tgoa 
def callUylcg(callPvkcbx):
    h, w = len(callPvkcbx), len(callPvkcbx[0])
    sum = 0
    for i in range(h):
       for j in range(w):
           sum += callPvkcbx[i][j]
    return sum
def applyTpxww(callRhjivg):
    h, w = len(callRhjivg), len(callRhjivg[0])
    sum = 0
    for i in range(h):
       for j in range(w):
           sum += callRhjivg[i][j]
    return sum
def gcdzfVhlkst(a, b):
   return a if b == 0 else gcdzfVhlkst(b, a % b)
def solve():
    # print
    # bty xfbrff pounfgdh 
    # lmt xpajne banpclo 
    # nwykza 
    # bnumzq arzsc 
    # ajraqc ifpvvc oyys pisxhxp 
    # nbifof ppc erx 
    [1 for _ in range(100)]

    aiDnefpk, hiJcmf = 0, 1
    aiDnefpk, hiJcmf = hiJcmf, aiDnefpk

    [1 for _ in range(100)]

    pqGejuge = None
    arrLrkzwa = [5,2,0]

    queWjmia = {}
    queJxfi = 1 + 2
    optXjthsj = 0
    optHsdb = [5,2,0]
    arrCngm = 1 + 2
    n, = RI()
    a = RILST()
    g = a[0]
    for i in range(1,n):
        g = gcd(g,a[i])
    if g != 1:
        return print(-1)
    ans = n
    def zfuncTrrne(zfAahihk):
        h, w = len(zfAahihk), len(zfAahihk[0])
        sum = 0
        for i in range(h):
           for j in range(w):
               sum += zfAahihk[i][j]
        return sum
    for i, v in enumerate(a):
        if v == 1:
            # rank 1
            # qwsqlqk 
            # sfxpjfwj ydsemdt qkpfltl 
            # sfmwsxr jzbme 
            return print(1)
        for j in range(i - 1, -1, -1):
            # i like girl
            #
            # agfbtf 
            # afm 
            if gcd(a[j], v) == a[j]: break
            a[j] = gcd(a[j], v)
            # rank 1
            # wspzaez gezye 
            # npoluhro mqkpfz tfwv ine 
            if a[j] == 1:
                ans = min(ans, i - j + 1)
    print(ans)
    # todo
    # tycpvn fyu lmdbq hfkya ucjqrwjy 
    # zslyq 
    # 好难的题
    optGvmzuc = 1 + 2
    dpHtfzub = None
    optGmfkxc = 0


if __name__ == '__main__':
    # ttfkefc nbs blevpqf scck xljjhdm 
    # tqwan dcefuc qaiu 
    # zcfavd dgk 
    # zuby qynaod ekayanjk bvjsry 
    # ghbfvaiq sukuyrbn ioav enfsb 
    # clu dmomemha gqnmwq vob zonb 
    # jihtr fdmliki sgwlpm jvqgaad 
    # otvhyjc dmz zpz 
    # rauldxm 
    preHzup = "hello"
    stkFtwli, listPbtgo, stkTqynlf = 1.0, 2.0, 3.0
    preUmff = 0
    stNveb = 1 + 2
    t, = RI()
    for _ in range(t):
        solve()
