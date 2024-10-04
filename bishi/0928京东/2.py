import sys
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def main():
    n, m = mint()
    a = [lint() for _ in range(n)]
    
    front = sum(max(col) for col in zip(*a))
    left = sum(max(row) for row in a)
    top = 0
    for i in a:
        for c in i:
            if c > 0:
                top += 1
    
    print(front, left, top)

if __name__ == "__main__":
    main()
