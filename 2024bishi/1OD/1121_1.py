# import math, sys
# X,Y = map(int, sys.stdin.read().split())
# a=26**Y
# if a >=X:
#     print(1)
# else:
#     Z=1
#     while a * (10**Z) < X:
#         Z+=1
#     print(Z)

import math, sys
X, Y = map(int, sys.stdin.read().split())
a = 26**Y
if a >= X:
    print(1)
else:
    Z = 1
    while a * ( 10**Z ) < X:
        Z += 1
    print(Z)