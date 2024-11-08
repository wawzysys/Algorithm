# E:\0Code\Algorithm\bishi\wangyi\1_1.py 2024-08-17 by 777
import sys

input = lambda: sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))


def solve():
    M = sint()
    for _ in range(M):
        N = sint()
        events = []
        for __ in range(N):
            time, k, t = input().split()
            k, t = int(k), int(t)
            hh, mm = map(int, time.split(':'))
            a = hh * 60 + mm
            b = a + t
            events.append((a, k))
            events.append((b, -k))
        chafen = [0] * 1440
        for event_time, change in events:
            if 0 <= event_time < 1440:
                chafen[event_time] += change
        mm = 0
        cur = 0
        for minute in range(1440):
            cur += chafen[minute]
            if cur > mm:
                mm = cur
        print(mm)


solve()
