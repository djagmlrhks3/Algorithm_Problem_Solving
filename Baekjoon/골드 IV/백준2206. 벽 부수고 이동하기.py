import sys
from collections import deque
sys.stdin = open('2206. 벽 부수고 이동하기.txt', 'r')

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0, 1)])
    visited[0][0][1] = 1
    while queue:
        r, c, used = queue.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c][used]
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 1 and used == 1: # 벽이고 아직 뚫지 않았다면
                    visited[nr][nc][0] = visited[r][c][1] + 1
                    queue.append((nr, nc, 0))
                elif matrix[nr][nc] == 0 and visited[nr][nc][used] == 0: # 이동 가능한 칸이며 아직 지나가지 않았다면
                    visited[nr][nc][used] = visited[r][c][used] + 1
                    queue.append((nr, nc, used))
    return -1

N, M = map(int, input().split())
matrix = [list(map(int, ''.join(sys.stdin.readline().rstrip()))) for _ in range(N)]
print(bfs())
