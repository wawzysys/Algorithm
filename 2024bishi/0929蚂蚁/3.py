sint = lambda: int(input())
mint = lambda: map(int, input().split())
for _ in range(sint()):
    n,m = mint()
    lst = [tuple(map(int, input().split())) for _ in range(n+m+1)]
    idx = list(range(n+m+1))
    x_sorted = sorted(idx, key=lambda i: -lst[i][0])
    x_sel = set(x_sorted[:n])
    y_sorted = sorted([i for i in idx if i not in x_sel], key=lambda i: -lst[i][1])
    y_sel = set(y_sorted[:m])
    total = sum(lst[i][0] for i in x_sel) + sum(lst[i][1] for i in y_sel)
    x_extra = sorted([i for i in x_sorted[n:]], key=lambda i: -lst[i][0])
    y_extra = sorted([i for i in y_sorted[m:]], key=lambda i: -lst[i][1])
    res = []
    for i in range(n+m+1):
        if i not in x_sel and i not in y_sel:
            res.append(total)
            continue
        tmp = total
        if i in x_sel:
            tmp -= lst[i][0]
            if x_extra:
                new_x = x_extra[0]
                tmp += lst[new_x][0]
            else:
                new_x = None
            if new_x in y_sel:
                if y_extra:
                    new_y = y_extra[0]
                    tmp += lst[new_y][1]
                else:
                    tmp -= lst[new_x][1]
        elif i in y_sel:
            tmp -= lst[i][1]
            if y_extra:
                new_y = y_extra[0]
                tmp += lst[new_y][1]
            else:
                new_y = None
            if new_y in x_sel:
                if x_extra:
                    new_x = x_extra[0]
                    tmp += lst[new_x][0]
                else:
                    tmp -= lst[new_y][0]
        res.append(tmp)
    print(' '.join(map(str, res)))
