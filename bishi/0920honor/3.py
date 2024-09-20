import sys
import re
lint = lambda: list(map(int, input().split(",")))

class Driver:
    def __init__(self, index, D, C, L, S):
        self.index = index  
        self.D = D          
        self.C = C          
        self.L = L          
        self.S = S          
        self.T = self.compute_time()  

    def compute_time(self):
        dis = self.D - self.C
        times = dis // 10  
        ji = self.C // 2         
        wait_time = (self.L * 15) // 2        
        return times + ji + wait_time
def f(ds):
    min_driver = ds[0]
    for d in ds:
        if d.T < min_driver.T:
            min_driver = d
        elif d.T == min_driver.T and d.S > min_driver.S:
            min_driver = d
    return min_driver
def main():
    D = lint()
    C = lint()
    L = lint()
    S = lint()
    N = len(D)
    ds = []
    for i in range(N):
        ds.append(Driver(i+1, D[i], C[i], L[i], S[i]))
    se = f(ds)
    while True:
        found = False
        current_T = se.T
        current_S = se.S
        bh = None
        for d in ds:
            if d.S > current_S and current_T <= d.T < current_T + 60:
                if bh is None:
                    bh = d
                else:
                    if d.S > bh.S:
                        bh = d
                    elif d.S == bh.S and d.T < bh.T:
                        bh = d

        if bh:
            se = bh
            found = True
        else:
            break

    print(f"{se.index},{se.T}")

main()
