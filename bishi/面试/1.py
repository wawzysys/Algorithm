def check(x):
    tep = x * x  # 正确计算 x 的平方
    tep = str(tep)  # 将平方结果转换为字符串
    x = str(x)  # 将 x 转换为字符串
    tep = list(tep)  # 不必要的转换，因为字符串可以直接迭代
    x = list(x)  # 这里应该是 x = list(x)，你原本的写法有误
    for i, j in zip(x[::-1], tep[::-1]):  # 检查每一个字符，但是这样只检查到最短的长度
        if i != j:
            return False
    return True

def check2(x):
    square = str(x * x)  # 计算平方并转换为字符串
    x_str = str(x)  # 将 x 转换为字符串
    # 直接检查 x_str 是否出现在 square 的末尾
    return square.endswith(x_str)


# print(check(5)) 
print(check(7))
    