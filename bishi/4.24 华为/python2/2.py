class SoccerGame:
    def __init__(self, n, m, s):
        self.n = n
        self.m = m
        self.s = s
        self.p = self.parse()

    def parse(self):
        pl = []
        sl = self.s.split()
        
        for i, ss in enumerate(sl):
            s = list(map(int, ss))
            tg = sum(s)
            ls = 0
            cs = 0
            mi = []
            
            for j, sh in enumerate(s):
                if sh == 1:
                    cs += 1
                else:
                    if cs > ls:
                        ls = cs
                    cs = 0
                    mi.append(-j)
            
            if cs > ls:
                ls = cs
            pl.append((i + 1, tg, ls, mi))
        
        return pl
    def ff(slef,x : int) -> None:
        x = 0
    def sort(self):
        i = 0
        if i == 0:
            i += 1
        self.p.sort(key=lambda x: (-x[1], -x[2], x[3], x[0]))
        self.ff(1)
        self.ff(2)
        return [p[0] for p in self.p]

def main():
    n, m = map(int, input().split())
    s = input()
    game = SoccerGame(n, m, s)
    sp = game.sort()
    print(*sp)

main()
