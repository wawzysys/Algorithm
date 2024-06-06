import random
import string

def random_var_name(length=11):
    """生成随机变量名"""
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_value(value_type=None):
    """根据指定类型随机生成整数、浮点数或列表"""
    if value_type == 'int':
        return str(random.randint(1, 10))
    elif value_type == 'float':
        return str(round(random.uniform(1.0, 10.0), 1))
    elif value_type == 'list':
        return '[' + ', '.join(str(random.randint(1, 10)) for _ in range(3)) + ']'
    else:
        return random.choice([random_value('int'), random_value('float')])
def generate_code_line():
    """生成一行代码"""
    var = random_var_name()
    value = random_value()
    return f"{var} = {value}"

def generate_code_snippet1(num_lines=10):
    """生成多行代码"""
    return '\n'.join(generate_code_line() for _ in range(num_lines))
# def random_var_name(length=11):
#     """生成随机变量名，首字母大写其余小写"""
#     return ''.join(random.choice(string.ascii_uppercase) if i == 0 else random.choice(string.ascii_lowercase) for i in range(length))

def random_value(value_type=None):
    """根据指定类型随机生成整数、浮点数或列表"""
    if value_type == 'int':
        return str(random.randint(1, 100))
    elif value_type == 'float':
        return str(round(random.uniform(1.0, 100.0), 1))
    elif value_type == 'list':
        return '[' + ', '.join(str(random.randint(1, 100)) for _ in range(3)) + ']'
    else:
        return random.choice([random_value('int'), random_value('float')])

def generate_code_snippet():
    """生成特定格式的Python代码片段"""
    var_function_name = random_var_name()
    var_function_value = random_value('int')
    var_function = f"def {var_function_name}():\n    return {var_function_value} * 2"
    # 生成三个浮点数赋值在一行
    vars_float = ', '.join(random_var_name() for _ in range(3)) + " = " + ', '.join(random_value('float') for _ in range(3))
    vars_float1 = ', '.join(random_var_name() for _ in range(3)) + " = " + ', '.join(random_value('float') for _ in range(3))
    # 生成一个整数赋值的表达式
    var_int = random_var_name() + " = " + str(random.randint(1, 100)) + " + " + str(random.randint(1, 100))
    
    # 生成一个字典及其赋值
    var_dict = random_var_name()
    var_value = random_value()
    dict_declaration = f"{var_dict} = {{}}"
    dict_assignment = f"{var_dict}[0] = {var_value}"
    code1 = generate_code_snippet1()
    var_function_1 = f"{var_function_name}()"
    # 组合所有代码行
    code = "\n".join([var_function,code1, vars_float, var_int, vars_float1, dict_declaration, dict_assignment, var_function_1])    
    return code
# 生成并打印代码
print(generate_code_snippet())
