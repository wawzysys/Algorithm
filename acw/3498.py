# E:\0Code\Algorithm\acw\3498.py 2024-03-29 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
while True:
    try:
        a = input()
        b = input()
    except:
        break
    if a > b:
        a, b = b, a
    year1 = int(a[:4])
    month1 = int(a[4:6])
    day1 = int(a[6:])
    year2 = int(b[:4])
    month2 = int(b[4:6])
    day2 = int(b[6:])
    for i in range(1, month1):
        if is_leap_year(year1) and i == 2:
            day1 += 1
        day1 += days[i]
    for i in range(1, month2):
        if is_leap_year(year2) and i == 2:
            day2 += 1
        day2 += days[i]
    for i in range(year1, year2):
        if is_leap_year(i):
            day2 += 1
        day2 += 365
    print(day2 - day1 + 1)