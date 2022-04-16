import sys
from collections import deque
sys.stdin = open('백준2573. 빙산.txt', 'r')

def check():
    global cnt
    visited = [[0] * M for _ in range(N)]
    iceberg = 0
    queue = deque([])
    for i in range(N):
        for j in range(M):
            if matrix[i][j] and not visited[i][j]:
                iceberg += 1
                queue.append((i, j))
                while queue:
                    r, c = queue.popleft()
                    for idx in range(4):
                        nr, nc = r+d[idx][0], c+d[idx][1]
                        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc]:
                            if not visited[nr][nc]:
                                queue.append((nr, nc))
                                visited[nr][nc] = 1
    cnt = iceberg

def melt():
    candidates = []
    for r in range(N):
        for c in range(M):
            if matrix[r][c]:
                sea = 0
                for idx in range(4):
                    nr, nc = r + d[idx][0], c + d[idx][1]
                    if 0 <= nr < N and 0 <= nc < M and not matrix[nr][nc]:
                        sea += 1
                candidates.append((r, c, sea))
    if candidates:
        while candidates:
            r, c, s = candidates.pop()
            matrix[r][c] -= s
            if matrix[r][c] < 0:
                matrix[r][c] = 0
        return True
    return False

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
matrix = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
cnt, time = 0, 0

while cnt < 2:
    if melt():
        check()
        time += 1
    else:
        time = 0
        break
print(time)