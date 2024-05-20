from itertools import permutations
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i <=n // i:
        if n % i == 0:
            return False
        i += 1
    return True
a = list(input())
def solve(a):
    for perm in permutations(a):
        if perm[0] != '0':
            n = int(''.join(perm))
            if is_prime(n):
                print(n)
                return
    print(-1)

solve(a)

