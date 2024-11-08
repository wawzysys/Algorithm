def find_longest_triangle_interval(stick_lengths):
    n = len(stick_lengths)
    left, right = 0, 2  
    max_len = 0
    start_pos = 0
    while left < n - 2:
        while right < n and can_form_triangle(stick_lengths[left:right + 1]):
            right += 1

        if right - left > max_len:
            max_len = right - left
            start_pos = left

        left += 1
        right = left + 2  
    return [start_pos, start_pos + max_len - 1]

def can_form_triangle(arr):
    for i in range(len(arr) - 2):
        if arr[i] + arr[i + 1] <= arr[i + 2]:
            return False
    return True

# Example usage
if __name__ == "__main__":
    n = int(input())
    stick_lengths = list(map(int, input().split()))
    print(*find_longest_triangle_interval(stick_lengths))