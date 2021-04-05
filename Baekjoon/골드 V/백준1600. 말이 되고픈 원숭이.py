import sys
from collections import deque
sys.stdin = open('백준1600. 말이 되고픈 원숭이.txt', 'r')

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
hd = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
      (1, -2), (2, -1), (2, 1), (1, 2)]

def check(nr, nc, k):
    if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][k] and maps[nr][nc] == 0:
        return True
    return False

def bfs():
    queue = deque([(0, 0, 0)])
    while queue:
        r, c, k = queue.popleft()
        if r == H-1 and c == W-1:
            return visited[r][c][k]-1
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if check(nr, nc, k):
                queue.append((nr, nc, k))
                visited[nr][nc][k] = visited[r][c][k] + 1
        if k < K:
            for idx in range(8):
                nr = r + hd[idx][0]
                nc = c + hd[idx][1]
                if check(nr, nc, k+1):
                    queue.append((nr, nc, k+1))
                    visited[nr][nc][k+1] = visited[r][c][k] + 1
    return -1

K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1

print(bfs())