def is_prime(n):
    """判断一个数是否为素数"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(num):
    """生成小于等于 num 的所有素数"""
    return [i for i in range(2, num + 1) if is_prime(i)]

def count_prime_combinations(num):
    """计算三元组的组合数量"""
    primes = generate_primes(num)
    unique_combinations = set()

    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                if p1 + p2 + p3 == num:
                    # 将三个数排序以避免重复
                    combination = tuple(sorted((p1, p2, p3)))
                    unique_combinations.add(combination)

    return len(unique_combinations)

def main():
    num = int(input())  # 输入三位数
    result = count_prime_combinations(num)
    print(result)

if __name__ == "__main__":
    main()
