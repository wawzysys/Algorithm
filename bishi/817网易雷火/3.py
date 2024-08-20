import sys

sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().strip()
from collections import *

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
m, n, l = mint()
task_series = [lint() for _ in range(m)]
done = lint()
updates = [lint() for _ in range(l)]


def solve():
    task_dict = {series[0]: series[2:] for series in task_series}
    pre = {}
    for i in task_dict:
        pre[i] = 1

    completed_set = set(done)
    curs = {}
    for sid, tasks in task_dict.items():
        for task in tasks:
            if task in completed_set:
                continue
            else:
                curs[sid] = task
                break
    for update in updates:
        op, sid, task_id, new_task_id = update
        if op == 0:
            if sid in task_dict:
                if task_id in task_dict[sid]:
                    task_dict[sid].remove(task_id)
                if curs.get(sid) == task_id:
                    if not task_dict[sid]:
                        curs.pop(sid, None)
                    else:
                        for task in task_dict[sid]:
                            if task not in completed_set:
                                curs[sid] = task
                                break
        elif op == 1:
            if sid in task_dict:
                idx = task_dict[sid].index(task_id) if task_id != 0 else -1
                task_dict[sid].insert(idx + 1, new_task_id)
                print(sid, idx)
                if sid not in curs:
                    if idx + 1 == len(task_dict[sid]) - 1:
                        curs[sid] = new_task_id
        print(task_dict)

        print(curs)
    for sid in sorted(task_dict.keys()):
        tasks = task_dict[sid]
        if sid in curs:
            current_task = curs[sid]
            start_idx = tasks.index(current_task)
            series_tasks = tasks[start_idx:]
            if series_tasks:
                series_tasks.sort()
                print(*series_tasks)


solve()
