import sys
from collections import deque
sys.stdin = open('백준2589. 보물섬.txt', 'r')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
R, C = map(int, input().split())
maps = [sys.stdin.readline().rstrip() for _ in range(R)]

def bfs(i, j):
    visited = [[0] * C for _ in range(R)]
    queue = deque([(i, j)])
    visited[i][j] = 1
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < R and 0 <= nc < C:
                if maps[nr][nc] == 'L' and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
    return visited[r][c]

answer = 0
for r in range(R):
    for c in range(C):
        if maps[r][c] == 'L':
            answer = max(answer, bfs(r, c))
print(answer-1)