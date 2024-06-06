import random
import string

def random_var_name(length=6):
    """生成随机变量名"""
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_value():
    """随机生成整数、浮点数或列表"""
    switcher = random.randint(0, 2)
    if switcher == 0:
        # 生成整数
        return str(random.randint(0, 10))
    elif switcher == 1:
        # 生成浮点数
        return str(round(random.uniform(0.0, 10.0), 2))
    elif switcher == 2:
        # 生成列表
        return '[' + ','.join([str(random.randint(0, 10)) for _ in range(3)]) + ']'

def generate_code_line():
    """生成一行代码"""
    var = random_var_name()
    value = random_value()
    return f"{var} = {value}"

def generate_code_snippet(num_lines=10):
    """生成多行代码"""
    return '\n'.join(generate_code_line() for _ in range(num_lines))



# 生成并打印代码
code_snippet = generate_code_snippet(10)
print(code_snippet)
