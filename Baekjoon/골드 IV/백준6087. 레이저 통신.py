import sys
from collections import deque

sys.stdin = open('백준6087. 레이저 통신.txt', 'r')
d = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def bfs(i, j):
    global W, H
    queue = deque([])
    visited = [[int(1e9)] * W for _ in range(H)]
    visited[i][j] = 0
    for idx in range(4):
        r = i + d[idx][0]
        c = j + d[idx][1]
        if 0 <= r < H and 0 <= c < W and maps[r][c] == '.':
            queue.append((r, c, idx, 0))
            visited[r][c] = 0

    res = int(1e9)
    while queue:
        r, c, dir, cnt = queue.popleft()
        if maps[r][c] == 'C':
            res = min(res, cnt)
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < H and 0 <= nc < W:
                if maps[nr][nc] != '*':
                    if idx == dir and cnt <= visited[nr][nc]:
                        queue.append((nr, nc, dir, cnt))
                        visited[nr][nc] = min(visited[nr][nc], cnt)
                    elif idx != dir and cnt + 1 <= visited[nr][nc]:
                        queue.append((nr, nc, idx, cnt + 1))
                        visited[nr][nc] = min(visited[nr][nc], cnt + 1)
    return res


W, H = map(int, input().split())
maps = [''.join(map(str, sys.stdin.readline().rstrip())) for _ in range(H)]
points = []
is_Find = False
for r in range(H):
    if is_Find: break
    for c in range(W):
        if maps[r][c] == 'C':
            print(bfs(r, c))
            is_Find = True
            break