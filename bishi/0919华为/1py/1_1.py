import sys
import re
class so():
    
    def main(self):
        import sys

        first_line = sys.stdin.readline()
        while first_line.strip() == '':
            first_line = sys.stdin.readline()
        n, m = map(int, first_line.strip().split())
        expressions = []
        for _ in range(n):
            line = sys.stdin.readline()
            while line.strip() == '':
                line = sys.stdin.readline()
            expressions.append(line.strip())

        # 读取m行的键值对
        data = {}
        for _ in range(m):
            line = sys.stdin.readline()
            while line.strip() == '':
                line = sys.stdin.readline()
            key, value = line.strip().split()
            data[key] = value

        pattern = re.compile(r"(\w+)\s*=\s*'([^']*)'")

        for expr in expressions:
            expr_replaced = expr.replace('AND', 'and').replace('OR', 'or')

            expr_replaced = pattern.sub(r"data['\1'] == '\2'", expr_replaced)

            try:
                result = eval(expr_replaced, {"data": data})
                print(0 if result else 1)
            except Exception as e:
                print(1)

a = so()
a.main()
