import sys
from collections import deque
sys.stdin = open('백준2583. 영역 구하기.txt', 'r')
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j):
    area = 1
    queue = deque([(i, j)])
    visited[i][j] = 1
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < M and 0 <= nc < N:
                if not matrix[nr][nc] and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                    area += 1
    return area

M, N, K = map(int, input().split())
matrix = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for r in range(M-y2, M-y1):
        for c in range(x1, x2):
            matrix[r][c] = 1

width = []
visited = [[0] * N for _ in range(M)]
for r in range(M):
    for c in range(N):
        if not visited[r][c] and not matrix[r][c]:
            width.append(bfs(r, c))
width.sort()
print(len(width))
print(' '.join(map(str, width)))