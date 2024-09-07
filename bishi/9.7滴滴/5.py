
points = {'H': 1, 'S': 2, 'D': 3, 'C': 4}
cards = input().strip()
k = int(input().strip())
w = [points[card] for card in cards]
n = len(w)
if k >= n:
    return sum(w)

max_score = sum(w[:k])
current_score = max_score
for i in range(1, k + 1):
    current_score = current_score - w[k - i] + w[-i]
    max_score = max(max_score, current_score)
print(max_score)
