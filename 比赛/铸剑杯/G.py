def get_knight_moves(x, y, k):
   moves = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
   valid = []
   for dx, dy in moves:
       new_x, new_y = x + dx, y + dy
       if 0 <= new_x < k and 0 <= new_y < k:
           valid.append((new_x, new_y))
   return valid

def count_safe_positions(k):
   if k == 1:
       return 0
   total = k * k * (k * k - 1) // 2
   attacks = 0
   
   for i in range(k):
       for j in range(k):
           valid_moves = get_knight_moves(i, j, k)
           attacks += len(valid_moves)
           
   return total - attacks // 2

n = int(input())
result = []

for k in range(1, n + 1):
   result.append(count_safe_positions(k))
   
for count in result:
   print(count)