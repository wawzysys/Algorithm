from datetime import datetime, timedelta

T = int(input())
for _ in range(T):
    data = input().split()
    m = int(data[0])
    times = []
    for i in range(m):
        h = int(data[1 + 2 * i])
        mi = int(data[1 + 2 * i + 1])
        der = datetime(2000, 1, 1, h, mi)
        times.append(der)
    print(times)

    count_valid_times = sum(1 for t in times if datetime(2000, 1, 1, 8, 0) <= t <= datetime(2000, 1, 1, 18, 0))

    if count_valid_times < 2:
        print('Absent')
        continue

    times.sort()
    a = times[0]
    b = times[-1]

    c = b - a

    d = datetime(2000, 1, 1, 12, 0)
    e = datetime(2000, 1, 1, 14, 0)

    f = max(a, d)
    g = min(b, e)
    if f < g:
        ll = g - f
    else:
        ll = timedelta(0)

    ii = c - ll

    sc = datetime(2000, 1, 1, 8, 0)
    if a > sc:
        la = a - sc
    else:
        la = timedelta(0)

    sch = datetime(2000, 1, 1, 18, 0)
    if b < sch:
        ed = sch - b
    else:
        ed = timedelta(0)

    td = la + ed

    fc = ii - td

    res = int(fc.total_seconds() // 60)
    print(res)
