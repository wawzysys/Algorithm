def min_operations_to_alternate(string):
    # Initial count of operations needed
    operations = 0
    # Loop through the string to find consecutive same letters
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            operations += 1  # Increment if two adjacent characters are the same
    print(operations)

# Test the function with an example string
n = int(input())
for i in range(n):
    example_string = input()
    min_operations_to_alternate(example_string)
