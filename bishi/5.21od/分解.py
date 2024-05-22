def solve(n):
    def g(x):
        if x < 3:
            return -1
        i = 3
        while i * i <= x:
            if n % i == 0:
                return i
            i += 2
        return x

    if n == 1:
        return "N"
    if n % 2 != 0:
        return f"{n}={n // 2}+{n // 2 + 1}"
    x = n // 2
    while x % 2 == 0:
        x //= 2
    l_even = n // x * 2
    s_even = x // 2 - (l_even // 2 - 1)
    l_odd = g(x)
    s_odd = n // l_odd - (l_odd - 1) // 2
    l, s = None, None
    if s_odd >= 1 and s_even >= 1:
        if l_even < l_odd:
            l, s = l_even, s_even
        else:
            l, s = l_odd, s_odd
    elif s_even >= 1:
        l, s = l_even, s_even
    elif s_odd >= 1:
        l, s = l_odd, s_odd
    else:
        return "N"
    return f"{n}={'+'.join(map(str, range(s, s + l)))}"

n = int(input())
print(solve(n))
