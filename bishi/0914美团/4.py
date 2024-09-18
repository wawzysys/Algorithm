import sys
import math
from collections import Counter
def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        counts = Counter(arr)
        answer = n
        while True:
            nums = list(counts.keys())
            max_e = max(nums)
            ok = True
            for num in nums:
                if max_e % num != 0:
                    ok = False
                    break
            if ok:
                if counts[max_e] > 0:
                    answer -= counts[max_e]
                    del counts[max_e]
                    if not counts:
                        break
                else:
                    break
            else:
                break
        print(answer)
main()
