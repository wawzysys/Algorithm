from collections import *
def incode(x):
	return (x // 3, x % 3)

def swap(list,a,b):
	list[a], list[b] = list[b], list[a]

end = '12345678x'

def bfs(start):
	q = deque()
	dir = [[1,0],[-1,0],[0,1],[0,-1]]
	dist = defaultdict(lambda : -1)
	cur_x, cur_y = incode(start.find('x'))
	q.append(start)
	dist[start] = 0
	while q:
		cur_str = q.popleft()

		distance = dist[cur_str]

		if cur_str == end:
			return distance
		index = cur_str.find('x')

		cur_x,cur_y = incode(index)
		
		cur_str = list(cur_str)
		for dx, dy in dir:
			x, y = cur_x + dx, cur_y + dy
			if 0 <= x < 3 and 0 <= y < 3:
				temp_index = x * 3 + y
				swap(cur_str, index, temp_index)
				cur = ''.join(cur_str)
				if dist[cur] == -1:
					dist[cur] = distance + 1
					q.append(cur)
				swap(cur_str, index, temp_index)
	return -1

start = ''.join(input().split())
print(bfs(start))
