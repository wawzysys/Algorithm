import decimal
from decimal import Decimal, getcontext
getcontext().prec = 50
def solve(a, b, c):
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)).sqrt() 
    nums = [a, b, c]
    nums.sort()
    if nums[-1] ** 2 > nums[0] ** 2 + nums[1] ** 2:
        nums = [nums[-1]]

    x = Decimal('-inf')
    
    for d in nums:
        h = (2 * area) / d
        x = max(x, (d * h) / (d + h))
    
    print(x)
a, b, c = map(Decimal, input().split())
solve(a, b, c)
