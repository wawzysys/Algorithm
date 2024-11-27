def count_valid_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if (i ^ n) < n:
            count += 1
    return count

print(count_valid_numbers(2024))