# 思路 切割出来 num1 num2 然后进行斐波那契
def F(x):
    n = len(x)
    max_len1 = n - 2 
    for len1 in range(1, max_len1 + 1):
        if x[0] == '0' and len1 > 1:
            continue
        num1_str = x[:len1]
        num1 = int(num1_str)
        max_len2 = n - len1 - 1
        for len2 in range(1, max_len2 + 1):
            if x[len1] == '0' and len2 > 1:
                continue
            num2_str = x[len1:len1+len2]
            num2 = int(num2_str)
            sequence = [num1, num2]
            idx = len1 + len2
            while idx < n:
                num3 = num1 + num2
                num3_str = str(num3)
                num3_len = len(num3_str)
                if idx + num3_len > n or x[idx:idx+num3_len] != num3_str:
                    break
                sequence.append(num3)
                idx += num3_len
                num1, num2 = num2, num3
            if idx == n and len(sequence) >= 3:
                return sequence
    return []
x = input()
print(x)
print(F(x))