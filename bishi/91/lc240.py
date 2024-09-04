m, n, target = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
def solve():
    i, j = 0, n - 1  # 从右上角开始
    while i < m and j >= 0:  # 还有剩余元素
        if matrix[i][j] == target:
            print("TRUE")
            return True  
        if matrix[i][j] < target:
            i += 1  
        else:
            j -= 1  
    print("FALSE")
    return False
solve()