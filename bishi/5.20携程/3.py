
def solve(x, p):
    # 提取奇数位数字组成新数
    odd = [digit for digit in str(x) if int(digit) % 2 != 0]
    if not odd:
        new_number = 0
    else:
        new_number = int(''.join(odd))
    
    # 计算新数对p取模的结果
    result = new_number % p
    return result

# 读取输入
x = int(input().strip())
p = int(input().strip())

# 计算并输出结果
print(solve(x, p))