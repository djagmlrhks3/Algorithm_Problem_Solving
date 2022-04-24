from collections import deque

R, C = map(int, input().split())
matrix = [input().rstrip() for _ in range(R)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0] * C for _ in range(R)]
queue = deque([])
for r in range(R):
	for c in range(C):
		if matrix[r][c] == "@":
			queue.append((r, c))
			visited[r][c] = 1
	
answer = -1
while queue:
	r, c = queue.popleft()
	for idx in range(4):
		nr, nc = r+d[idx][0], c+d[idx][1]
		if 0 <= nr < R and 0 <= nc < C:
			if matrix[nr][nc] == '.' and not visited[nr][nc]:
				queue.append((nr, nc))
				visited[nr][nc] = visited[r][c] + 1
			if matrix[nr][nc] == '&':
				answer = visited[r][c] - 1
				queue.clear()
print(answer)