# E:\0Code\Algorithm\acw\137\3218.py 2024-03-29 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
y = sint()
dd = sint()
ans = 0
i = 1
d = y * 10000 + 101
while i < dd:
    d = int(d) + 1
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = d % 100
    month = (d // 100) % 100
    year = d // 10000
    if is_leap(year):
        days[2] = 29
    if day > days[month]:
        day = 1
        month += 1
    if month > 12:
        year += 1
        month = 1
    d = year * 10000 + month * 100 + day
    i += 1
print(d // 100 % 100)
print(d % 100)