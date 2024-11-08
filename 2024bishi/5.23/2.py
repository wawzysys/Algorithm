def f9_10(n):
    n = list(str(n))
    ans = 0
    for c in n:
        ans = ans * 9 + int(c)
    return ans
def f10_9(decimal_number):
    if decimal_number == 0:
        return "0"
    base9_number = ""
    negative = decimal_number < 0
    if negative:
        decimal_number = -decimal_number
    while decimal_number > 0:
        remainder = decimal_number % 9
        base9_number = str(remainder) + base9_number
        decimal_number = decimal_number // 9
    if negative:
        base9_number = "-" + base9_number
    return base9_number
n = int(input())
m = int(input())

n_10 = f9_10(n)
m_10 = f9_10(m)

ans_10 = n_10 * m_10
ans_9 = f10_9(ans_10)
print(ans_9)