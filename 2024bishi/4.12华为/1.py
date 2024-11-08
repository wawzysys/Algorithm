def f(n):
    count = 0
    for i in range(1, n +1):
        if '4' in str(i):
            count += 1
    return count
n = int(input())
print(n - f(n))
