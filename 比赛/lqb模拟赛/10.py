class Position:
    def __init__(self, r=0, c=0, direction=0):
        self.r = r  # 行坐标
        self.c = c  # 列坐标
        self.direction = direction  # 0:北, 1:东, 2:南, 3:西
    
    def __eq__(self, other):
        return self.r == other.r and self.c == other.c
    
    def __hash__(self):
        return hash((self.r, self.c))

def move(pos, action):
    new_pos = Position(pos.r, pos.c, pos.direction)
    
    if action == 'L':
        new_pos.direction = (pos.direction - 1) % 4
    elif action == 'R':
        new_pos.direction = (pos.direction + 1) % 4
    
    # 根据最终朝向移动
    if new_pos.direction == 0:  # 北
        new_pos.r -= 1
    elif new_pos.direction == 1:  # 东
        new_pos.c += 1
    elif new_pos.direction == 2:  # 南
        new_pos.r += 1
    else:  # 西
        new_pos.c -= 1
    
    return new_pos

def solve(n, path):
    # 存储所有可能的终点位置
    final_positions = set()
    
    # 计算原始路径的终点
    original_pos = Position()
    positions = [original_pos]
    
    # 记录原始路径上的所有位置
    for action in path:
        original_pos = move(original_pos, action)
        positions.append(original_pos)
    
    # 对每一步尝试改变动作
    for i in range(n):
        pos = positions[i]  # 获取改变前的位置
        
        # 尝试三种可能的动作
        for new_action in ['F', 'L', 'R']:
            if new_action == path[i]:
                continue
                
            # 从改变点开始重新计算路径
            current_pos = move(pos, new_action)
            
            # 继续执行剩余的原始路径
            for j in range(i + 1, n):
                current_pos = move(current_pos, path[j])
            
            # 记录终点位置
            final_positions.add((current_pos.r, current_pos.c))
    
    return len(final_positions)

# 读取输入并解决问题
def main():
    n = int(input())
    path = input().strip()
    result = solve(n, path)
    print(result)

if __name__ == "__main__":
    main()
    
