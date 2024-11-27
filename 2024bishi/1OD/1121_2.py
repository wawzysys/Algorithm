class B:
    def __init__(self, expr):
        self.expr = expr
        self.max_depth = 0

    def f(self):
        stk = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in self.expr:
            if char in '({[':
                stk.append(char)
                if len(stk) > self.max_depth:
                    self.max_depth = len(stk)
            elif char in ')}]':
                if not stk or stk[-1] != pairs.get(char):
                    return 0
                stk.pop()
            else:
                return 0
        return self.max_depth if not stk else 0
s = input()
checker = B(s)
print(checker.f())