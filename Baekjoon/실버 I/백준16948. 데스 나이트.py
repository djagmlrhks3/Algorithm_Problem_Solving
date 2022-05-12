import sys
from collections import deque
sys.stdin = open('백준16948. 데스 나이트.txt', 'r')
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
queue = deque([(r1, c1, 0)])
visited = [[0] * N for _ in range(N)]
visited[r1][c1] = 1

while queue:
    r, c, t = queue.popleft()
    if r == r2 and c == c2:
        print(t)
        break
    for idx in range(6):
        nr = r+d[idx][0]
        nc = c+d[idx][1]
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                queue.append((nr, nc, t+1))
                visited[nr][nc] = 1
else:
    print(-1)