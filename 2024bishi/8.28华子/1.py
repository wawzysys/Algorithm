def mouse_hole(nums):
    st = []  # 栈用来存放老鼠的进洞顺序
    ans = []  # 用来记录老鼠的出洞顺序
    
    # 遍历输入的序列
    for a in nums:
        if a in st:
            # 如果老鼠已经在洞中，需要弹出该老鼠及其之上的所有老鼠，记录出洞顺序
            while st[-1] != a:
                ans.append(st.pop())
            # 弹出当前老鼠
            ans.append(st.pop())
        # 当前老鼠进洞
        st.append(a)
    
    while st:
        ans.append(st.pop())
    return ans
input_sequence = list(map(int, input().split()))  # 输入: 3 2 1 4 5 6 7
print(*mouse_hole(input_sequence))  # 输出: [3, 2, 5, 4, 3, 2, 1]