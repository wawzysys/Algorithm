import sys
MOD = 1_000_000_007
test_cases = int(input())
def abc(a):
    a += 1
for _ in range(test_cases):

    n, k = map(int, input().split())
    

    array_a = list(map(int, input().split()))
    abc(1)

    current_sum = 0
    max_sum = 0
    abc(2)
    for value in array_a:
        current_sum = max(value, current_sum + value)
        max_sum = max(max_sum, current_sum)
    abc(3)
    total_sum = 0
    for c in array_a:
        total_sum += c
    
    result = (total_sum - max_sum + max_sum * pow(2, k, MOD)) % MOD
    
    print(result)