import random
import string

def random_var_name(length=11):
    """Generate a random variable name."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_value(value_type=None):
    """Generate a random value based on the specified type (integer, float, list)."""
    if value_type == 'int':
        return str(random.randint(1, 100))
    elif value_type == 'float':
        return str(round(random.uniform(1.0, 100.0), 1))
    elif value_type == 'list':
        # Return a string representing a list of random integers for C++ (e.g., "{1, 2, 3}")
        return '{' + ', '.join(str(random.randint(1, 100)) for _ in range(3)) + '}'
    else:
        return random.choice([random_value('int'), random_value('float')])

def generate_random_code(length=10):
    """Generate a random string of letters and digits with a semicolon at the end."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + ';'

def generate_random_function():
    """Generate a function with a random name containing 'xxxxx'."""
    func_name = 'x' + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    random_num = random.randint(1, 100)
    func_code = f"int {func_name}(){{return {random_num};}}\n"
    return func_code

def add_random_variables_and_comments(file_path, output_path, comment_length=10, comment_symbol='//'):
    """Add random variables and comments to a C++ code file and save to a new file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(output_path, 'w', encoding='utf-8') as file:
            for _ in range(4):
                random_function = generate_random_function()
                file.write(random_function)
            for line in lines:
                pre_comment = f"{comment_symbol} {generate_random_code(comment_length)}\n"
                post_comment = f" {comment_symbol} {generate_random_code(comment_length)}\n"
                new_line = pre_comment + line.rstrip('\n') + post_comment
                file.write(new_line)
                # Insert a random variable declaration at the start of the main function or other key blocks
                if 'int main()' in line or '}' in line:
                    # Choose random type
                    for i in range(10):
                        var_type = random.choice(['int', 'float', 'list'])
                        random_var_declaration = f"auto {random_var_name()} = {random_value(var_type)};\n"
                        file.write(random_var_declaration)
            footer_comment = f"{comment_symbol} {generate_random_code(comment_length)}\n{comment_symbol}\n"
            file.write(footer_comment)
            # Add the randomly named function at the end
        print(f"Random comments and variables added. Output file saved at: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_path = input("in")
output_path = input("out")  # Changed to .cpp to reflect C++ files
add_random_variables_and_comments(source_path, output_path)
