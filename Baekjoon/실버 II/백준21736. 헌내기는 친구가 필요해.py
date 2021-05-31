import sys
from collections import deque
sys.stdin = open('백준21736. 헌내기는 친구가 필요해.txt', 'r')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())

campus = [sys.stdin.readline().rstrip() for _ in range(N)]
sr, sc = 0, 0
for r in range(N):
    for c in range(M):
        if campus[r][c] == 'I':
            sr, sc = r, c

visited = [[0] * M for _ in range(N)]
visited[sr][sc] = 1
queue = deque([(sr, sc)])
res = 0
while queue:
    r, c = queue.popleft()
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if campus[nr][nc] == 'O':
                queue.append((nr, nc))
            elif campus[nr][nc] == 'P':
                queue.append((nr, nc))
                res += 1
            visited[nr][nc] = 1
print(res) if res else print('TT')