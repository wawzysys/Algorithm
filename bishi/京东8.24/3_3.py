from collections import deque
ans_len = 2
ans_l = 0
n = int(input())
arr = list(map(int, input().split()))
def check(k):
    global ans_len, ans_l
    max_values = []
    min_values = []
    second_min_values = []
    max_deque = deque()
    min_deque = deque()
    if k < 3:
        return True
    for i in range(n):
        while max_deque and arr[max_deque[-1]] < arr[i]:
            max_deque.pop()
        max_deque.append(i)
        if max_deque[0] <= i - k:
            max_deque.popleft()
        
        while min_deque and arr[min_deque[-1]] > arr[i]:
            last = min_deque.pop()
        min_deque.append(i)
        if min_deque[0] <= i - k:
            min_deque.popleft()

        if i >= k - 1:
            max_values.append(arr[max_deque[0]])
            min_values.append(arr[min_deque[0]])
            min_val = arr[min_deque[0]]
            second_min = arr[last]
            if len(min_deque) > 1:
                second_min = arr[min_deque[1]]
            second_min_values.append(second_min)
            if max_values[-1] < min_values[-1] + second_min_values[-1]:
                if k > ans_len:
                    ans_len = k
                    ans_l = i - k + 1
                return True
    return False
l = 1 
r = n
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        l = mid + 1
    else:
        r = mid - 1
if r == 2:
    print("1 2")
else:
    print(ans_l + 1, ans_l + ans_len)