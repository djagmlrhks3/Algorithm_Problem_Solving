import sys
from collections import deque

def bfs(r, c):
    global answer
    queue = deque([(r, c)])
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    while queue:
        i, j = queue.popleft()
        for idx in range(8):
            ni = i+d[idx][0]
            nj = j+d[idx][1]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if board[ni][nj]:
                    answer = max(answer, visited[i][j])
                    return
                else:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

sys.stdin = open('백준17086. 아기 상어 2.txt', 'r')
d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark = deque([])
answer = 0
for r in range(N):
    for c in range(M):
        if not board[r][c]:
            shark.append((r, c))
while shark:
    r, c = shark.popleft()
    bfs(r, c)
print(answer)