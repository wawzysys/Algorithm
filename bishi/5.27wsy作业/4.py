def gcd(a, b):
    # 如果两个数相等，返回其中一个
    if a == b:
        return a
    # 如果a大于b，递归调用gcd(a-b, b)
    elif a > b:
        return gcd(a - b, b)
    # 如果b大于a，递归调用gcd(a, b-a)
    else:
        return gcd(a, b - a)

