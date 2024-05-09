def is_lucky_number(number):
    num_str = list(str(number))
    for i in range(len(num_str) - 1, -1, -2):  # 从右往左遍历奇数位
        digit = int(num_str[i]) * 7  # 进行变换
        while digit > 9:
            digit_sum = sum(int(d) for d in str(digit))
            digit = digit_sum
        num_str[i] = str(digit)
    # 计算变换结果的和
    transformed_sum = sum(int(d) for d in num_str)
    # 判断变换结果的和是否为 8 的倍数
    if transformed_sum % 8 == 0:
        return True
    else:
        return False

N = int(input())

for _ in range(N):
    num = int(input())
    if is_lucky_number(num):
        print('T')
    else:
        print('F')
