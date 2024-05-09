# E:\0Code\Algorithm\acw\137\2867.py 2024-03-29 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
d1 = sint()
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
def check_1(str : str) -> bool:
    return str == str[:: - 1]
ans = 0
d = d1 + 1
while ans < 1:
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
    d = str(year) + str(month).zfill(2) + str(day).zfill(2)
    if check_1(d):
        print(d)
        ans += 1
    d = int(d) + 1
ans = 0
d = d1 + 1
while ans < 1:
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
    d = str(year) + str(month).zfill(2) + str(day).zfill(2)
    if check_1(d) and d[0] == d[2] and d[1] == d[3] and d[0] != d[1]: 
        ans += 1
        print(d)
    d = int(d) + 1