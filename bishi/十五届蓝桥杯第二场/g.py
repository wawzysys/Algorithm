# G题
# n = int(input())
# warriors = list(map(int, input().split()))
# strongest_teams = []
# for state in range(1 << n):  
#     current_team = []
#     for i in range(n):
#         if state & (1 << i):  
#             current_team.append(warriors[i])
#     strongest_teams.append(current_team)
# ans = 1
# for team in strongest_teams:
#     if len(team) > ans :
#         if len(team) == 2 and 2 > ans:
#             ans = 2
#             continue            
#         if team[0] > max(team[1:len(team) - 1]) and team[-1] > max(team[1:len(team) - 1]): 
#             ans = len(team)
# print(ans)

def strongest_team(n, strengths):
    # 初始化开始和结束指针
    start = 0
    max_length = 0
    
    # 遍历数组
    for end in range(n):
        # 计算当前子序列的力量范围
        min_strength = strengths[start]
        max_strength = strengths[end]
        
        # 判断当前子序列是否满足条件
        if max_strength > min(strengths[start:end]):
            # 更新最大长度
            max_length = max(max_length, end - start + 1)
        else:
            # 移动开始指针直到满足条件
            while start <= end and max_strength <= min_strength:
                start += 1
                if start <= end:
                    min_strength = min(min_strength, strengths[start])
    
    return max_length

# 读取输入
n = int(input())
strengths = list(map(int, input().split()))

# 计算最强小队的成员数量
result = strongest_team(n, strengths)
print(result)
