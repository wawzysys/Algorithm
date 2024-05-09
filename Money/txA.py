
lint = lambda: list(map(int, input().split()))
def is_sortable(lists):
    # 找到潜在的断裂点
    ans = []
    for lst in lists:
        for i in range(1, len(lst)):
            if lst[i - 1] >= lst[i]:
                ans += 1
        if ans <= 1:         
            ans.append(True)
        else:
            ans.append(False)
    return ans

