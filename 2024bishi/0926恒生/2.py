def max_matrix_sum(n, m, matrix):
    original_sum = 0
    sum_row = [0] * n
    row_max = [0] * n
    sum_col = [0] * m
    column_max = [0] * m
    for i in range(n):
        for j in range(m):
            val = matrix[i][j]
            original_sum += val
            sum_row[i] += val
            if val > row_max[i]:
                row_max[i] = val
            sum_col[j] += val
            if val > column_max[j]:
                column_max[j] = val

    max_sum = float('-inf')
    for i in range(n):
        for j in range(m):
            col_max_after = max(column_max[j], row_max[i])
            
            final_sum = (
                original_sum
                - sum_row[i]
                - sum_col[j]
                + matrix[i][j]
                + row_max[i] * (m - 1)
                + col_max_after * n
            )
            
            if final_sum > max_sum:
                max_sum = final_sum

    return max_sum

if __name__ == "__main__":
    import sys

    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        n, m = map(int, sys.stdin.readline().split())
        matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    else:
        tokens = []
        for line in input_lines:
            tokens.extend(line.strip().split())
        n, m = map(int, tokens[:2])
        matrix = []
        idx = 2
        for _ in range(n):
            row = list(map(int, tokens[idx:idx + m]))
            matrix.append(row)
            idx += m
    result = max_matrix_sum(n, m, matrix)
    print(result)
