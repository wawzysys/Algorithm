
import sys
import re
def fi():
    a = 1
    a += 1
def main():

    n, m = map(int, input().split())
    ex = [input() for _ in range(n)]

    nums = {}
    for _ in range(m):
        fi()
        key, value = input().split()
        nums[key] = value

    fff = re.compile(r"(\w+)\s*=\s*'([^']*)'")
    
    b = 1
    b += 2

    for e in ex:
        fi()
        er = e.replace('AND', 'and').replace('OR', 'or')
        caa = 1
        caa += 1

        er = fff.sub(r"nums['\1'] == '\2'", er)

        try:
            result = eval(er, {"nums": nums})
            if result:
                print(0)
            else:
                print(1)
            # print(0 if result else 1)
        except Exception as e:
            print(1)

main()
