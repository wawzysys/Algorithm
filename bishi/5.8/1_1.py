# import sys
# from collections import defaultdict

# def mov(vars, var_name, value):
#     vars[var_name] = int(value)

# def add(vars, var_name, val1, val2):
#     vars[var_name] = get_value(vars, val1) + get_value(vars, val2)

# def sub(vars, var_name, val1, val2):
#     vars[var_name] = get_value(vars, val1) - get_value(vars, val2)

# def mul(vars, var_name, val1, val2):
#     vars[var_name] = get_value(vars, val1) * get_value(vars, val2)

# def div(vars, var_name, val1, val2):
#     vars[var_name] = get_value(vars, val1) // get_value(vars, val2)

# def get_value(vars, val):
#     return int(val) if val.isdigit() else vars[val]

# def solve() -> None:
#     vars = defaultdict(int)
#     operations = {
#         "MOV": mov,
#         "ADD": add,
#         "SUB": sub,
#         "MUL": mul,
#         "DIV": div,
#     }
#     while True:
#         try:
#             opts = list(input().split())
#             if opts[0] == "MOV":
#                 mov(vars, opts[1], opts[2])
#             if opts[0] == "ADD":
#                 add(vars, opts[1], opts[2], opts[3])
#             if opts[0] == "SUB":
#                 sub(vars, opts[1], opts[2], opts[3])
#             if opts[0] == "MUL":
#                 mul(vars, opts[1], opts[2], opts[3])
#             if opts[0] == "DIV":
#                 div(vars, opts[1], opts[2], opts[3])
#             if opts[0] == "PRINT":
#                 print(vars[opts[1]])
#         except:
#             break


# if __name__ == '__main__':
#     solve()
from collections import defaultdict
conut=defaultdict(int)
while True:
    try:
        s=input().split()
        if s[0]=='MOV':
            conut[s[1]] = int(s[2])
        if s[0]=='ADD':
            conut[s[1]]=conut[s[2]]+conut[s[3]]
        if s[0]=='SUB':
            conut[s[1]]=conut[s[2]]-conut[s[3]]
        if s[0]=='MUL':
            conut[s[1]]=conut[s[2]]*conut[s[3]]
        if s[0]=='DIV':
            conut[s[1]]=conut[s[2]]//conut[s[3]]
        if s[0]=='PRINT':
            print (conut[s[1]])
            
    except:
        break

import sys

from collections import *

def solve() -> None:
    vars = defaultdict(int)
    while True:
        try:
            opts = list(input().split())
            if opts[0] == "MOV":
                vars[opts[1]] = int(opts[2])
            elif opts[0] == "ADD":
                vars[opts[1]] = (int(opts[2]) if opts[2].isdigit() else vars[opts[2]]) + (int(opts[3]) if opts[3].isdigit() else vars[opts[3]])
            elif opts[0] == "SUB":
                vars[opts[1]] = (int(opts[2]) if opts[2].isdigit() else vars[opts[2]]) - (int(opts[3]) if opts[3].isdigit() else vars[opts[3]])
                
            elif opts[0] == "MUL":
                vars[opts[1]] = (int(opts[2]) if opts[2].isdigit() else vars[opts[2]]) * (int(opts[3]) if opts[3].isdigit() else vars[opts[3]])
            elif opts[0] == "DIV":
                vars[opts[1]] = (int(opts[2]) if opts[2].isdigit() else vars[opts[2]]) // (int(opts[3]) if opts[3].isdigit() else vars[opts[3]])
            else:
                print(vars[opts[1]])
        except:
            break
                
    

if __name__ == '__main__':
    solve()