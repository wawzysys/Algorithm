import os
from random import randint, uniform
import subprocess

T = 10 # 样例组数

# 生成随机数据的函数
def generate_date():
     A = [0] * 1010
     for t in range(1, T + 1):
          # 数据的文件名
          filename = f"in_{t}.txt"
          with open(filename, "w") as file:
               n = randint(1, 1000)
            #    k = randint(1, n)
               file.write(str(n)+  "\n")
               for i in range(n):
                    A[i] = randint(0, 10000)
               nums = " ".join(map(str, A[:n]))
               file.write(nums + "\n")
     print(f'generate_ok:......{T}')

# 调用py程序函数
def run(process_name):
     for t in range(1, T + 1):
          # 文件名
          out_filename = f"{process_name}_out_{t}.txt"
          in_filename = f"in_{t}.txt"
          subprocess.run(['python', process_name],
                         stdin = open(in_filename, "r"),
                         stdout = open(out_filename, "w"))
     print(f'run_{process_name}_ok:......{T}')

# 对比txt文件是否相同的函数
def diff(file1, file2):
     for t in range(1, T + 1):
          f1 = f"{file1}_out_{t}.txt"
          f2 = f"{file2}_out_{t}.txt"
          with open(f1, "r") as s, open(f2, "r") as ss:
               lines1 = s.readlines()
               lines2 = ss.readlines()
               if len(lines1) != len(lines2):
                    print(f'{t}:lines error')
                    continue
               ok = 1
               for line1,line2 in zip(lines1, lines2):
                    if line1 != line2:
                         print(f'{t}:exist error')
                         ok = 0
                         break
               if ok: print(f'{t}:ok')
if __name__ == "__main__":
    # 生成输入文件
    generate_date()

    # 调用正解
    file_true = r'E:\0Code\Algorithm\bishi\京东8.24\3_1.py'
    run(file_true)

    # 调用测试程序
    file_my = r'E:\0Code\Algorithm\bishi\京东8.24\3_4.py'
    run(file_my)

    # 调用对比程序
    diff(file_true, file_my)
