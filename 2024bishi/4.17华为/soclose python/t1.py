def solve():
    n = int(input())  
    stack = []
    C = list(input().split())
    for _ in range(n):
        c = C[_] 
        if len(stack) > 1 and stack[-1] == c and stack[-2] == c:
            stack.pop()
            stack.pop()
        else:
            stack.append(c)

    print(' '.join(stack))

if __name__ == "__main__":
    solve()
