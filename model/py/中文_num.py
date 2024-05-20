num = {"一":1, "二":2, "三":3, "四":4, "五":5, "六":6, "七":7, "八":8, "九":9,"零":0}
d = {"十":10, "百":100, "千":1000, "万":10000, "亿":100000000}
s = input()
print(s)
tep = 0
for c in s:
    if c in num:
        tep += num[c]
    if c in d:
        cur = tep % d[c]
        tep = tep - cur + d[c] * cur
print(tep)



