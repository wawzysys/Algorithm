def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(2024 * 1024 // (gcd(2024, 1024)))  # 1048576