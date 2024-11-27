import os

def remove_comments(input_file, output_file):
    """
    Read a Python file and remove all comments after # symbol
    Args:
        input_file (str): Path to input Python file
        output_file (str): Path to output Python file
    """
    # Convert path to proper format using os.path
    input_file = os.path.normpath(input_file)
    output_file = os.path.normpath(output_file)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Process each line
        processed_lines = []
        for line in lines:
            # Find position of # that isn't inside a string
            hash_pos = -1
            in_string = False
            string_char = None
            
            for i, char in enumerate(line):
                # Handle string boundaries
                if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):
                    if not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char:
                        in_string = False
                # Find # that's not in a string
                elif char == '#' and not in_string:
                    hash_pos = i
                    break
            
            # Remove comment if found, otherwise keep whole line
            if hash_pos != -1:
                processed_line = line[:hash_pos].rstrip() + '\n'
                # Don't keep empty lines
                if processed_line.strip():
                    processed_lines.append(processed_line)
            else:
                processed_lines.append(line)
        
        # Write processed lines to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)
            
        print(f"Successfully processed {input_file}")
        print(f"Output written to {output_file}")
            
    except FileNotFoundError:
        print(f"Error: Could not find the input file: {input_file}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    # Use raw string for Windows paths to handle backslashes correctly
    input_path = r"E:\0Code\Algorithm\比赛\亚太杯\4.py"
    output_path = r"E:\0Code\Algorithm\比赛\亚太杯\d.py"
    
    # Alternative: use forward slashes which work on both Windows and Unix
    # input_path = "E:/0Code/Algorithm/比赛/亚太杯/2.py"
    # output_path = "E:/0Code/Algorithm/比赛/亚太杯/b.py"
    
    remove_comments(input_path, output_path)
    
