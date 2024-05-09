# E:\0Code\Algorithm\acw\1229.py 2024-03-29 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
a = input().split('/')
# print(a)
start = '19600101'
end = '20591231'
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
ans = set()
def check(year : str, month : str, day : str) -> bool:
    # ss = year + month.zfill(2) + day.zfill(2)  # Ensure month and day are two digits
    ss = year + month + day
    if ss < start or ss > end:
        return False
    if int(month) > 12 or int(month) <= 0:
        return False
    days= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(int(year)):
        days[2] = 29
    if int(day) > days[int(month)] or int(day) <= 0:  
        return False
    return True
def date(a : str, b : str, c : str) -> None:
    for i in range(1, 3):
        for j in range(0, 10):
            year = str(i) + str(j) + str(a)
            # print(year)
            if check(year, b, c):              
                ans.add((year,b, c))
                # print(year,b, c)
date(a[0], a[1], a[2])
date(a[2], a[0], a[1])
date(a[2], a[1], a[0] )
for x in sorted(ans):
    print('-'.join(x))

