import random
import string


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
    return '\n'.join(generate_code_line() for _ in range(num_lines))
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
def generate_random_code(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def add_random_comments_to_code(file_path, output_path, comment_length=10, comment_symbol='#'):
    """
    在代码文件的每一行前后以及文件的开头和结尾添加随机乱码注释，并保存到新文件。
    :param file_path: str, 源代码文件的路径。
    :param output_path: str, 输出文件的路径。
    :param comment_length: int, 乱码注释的长度。
    :param comment_symbol: str, 用于注释的符号，默认为Python的注释符号。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(output_path, 'w', encoding='utf-8') as file:
            # 添加文件开头的随机注释
            header_comment = f"{comment_symbol} Made by 777\n{comment_symbol} {generate_random_code(comment_length)}\n"
            file.write(header_comment)
            for line in lines:
                # 为每一行生成一个随机注释，并在行前后都添加
                if line == "def solve():\n":
                    print("yes")
                    post_comment = generate_code_snippet()
                    print(type(post_comment))
                    new_line = line + post_comment
                    file.write(new_line)       
                else:
                    pre_comment = f"{comment_symbol} {generate_random_code(comment_length)}\n"
                    post_comment = f" {comment_symbol} {generate_random_code(comment_length)}\n"
                    new_line = pre_comment + line.rstrip('\n') + post_comment
                    file.write(new_line)                
            # 添加文件结尾的随机注释
            footer_comment = f"{comment_symbol} {generate_random_code(comment_length)}\n{comment_symbol} Made by 777\n"
            file.write(footer_comment)

        print(f"随机注释已添加完成。输出文件保存在：{output_path}")
    except Exception as e:
        print(f"发生错误：{e}")
# 使用示例
source_path = r'E:\0Code\Algorithm\model\test1.py'  # 要读取的源代码文件路径
# source_path = input
output_path = r'E:\0Code\Algorithm\model\test2.py'  # 输出文件的路径
add_random_comments_to_code(source_path, output_path)
