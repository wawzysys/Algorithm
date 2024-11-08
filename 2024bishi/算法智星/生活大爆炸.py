def get_winner(hand1, hand2):
    # 定义手势之间的胜负关系
    # 0 剪刀
    # 1 石头
    # 2 布
    # 3 蜥蜴
    # 4 斯波克
    rules = {
        (1, 0): 1,  # 石头 vs 剪刀
        (0, 2): 1,  # 剪刀 布 vs 
        (0, 3): 1,  # 剪刀 vs 蜥蜴人
        (4, 0): 1,  # 蜥蜴人 vs 斯波克
        (2, 1): 1,  # 布  vs 石头
        (1, 3): 1,
        (4, 1): 1,
        (3, 2): 1,
        (2, 4): 1,
        (3, 4): 1
    }
    if hand1 == hand2:
        return 0  
    elif (hand1, hand2) in rules:
        return 1  
    else:
        return 2  
def calculate_score(hand_a, hand_b, N):
    score_a = 0
    score_b = 0
    for i in range(N):
        result = get_winner(hand_a[i % len(hand_a)], hand_b[i % len(hand_b)])
        if result == 1:
            score_a += 1
        elif result == 2:
            score_b += 1
    return score_a, score_b
N, Na, Nb = map(int, input().split())
hand_a = list(map(int, input().split()))
hand_b = list(map(int, input().split()))
score_a, score_b = calculate_score(hand_a, hand_b, N)
print(score_a, score_b)
