from collections import Counter
def isNStraightHand(hand, groupSize) -> bool:
    n = len(hand)
    if n % groupSize:
        return False
    cnt = Counter(hand)
    hand = sorted(set(hand), reverse=True)
    for _ in range(n // groupSize):
        k, c = hand[-1], cnt[hand[-1]]
        for i in range(k, k + groupSize):
            if cnt[i] < c:
                return False
            cnt[i] -= c 
        while hand and not cnt[hand[-1]]:
            hand.pop()
    return True
    
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3

print(isNStraightHand(hand, groupSize)) 