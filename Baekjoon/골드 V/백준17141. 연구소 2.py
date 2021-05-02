import sys, copy
from itertools import combinations
from collections import deque

sys.stdin = open('백준17141. 연구소 2.txt', 'r')
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(li):
    temp = 0
    copy_maps = copy.deepcopy(maps)
    copy_visited = copy.deepcopy(visited)
    for r, c in li:
        copy_visited[r][c] = 1
    queue = deque(li)
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + d[i][0]
            nc = c + d[i][1]
            if 0 <= nr < N and 0 <= nc < N:
                if not copy_visited[nr][nc] and copy_maps[nr][nc] != 1:
                    queue.append((nr, nc))
                    copy_visited[nr][nc] = copy_visited[r][c] + 1
                    temp = copy_visited[nr][nc]
    for r in range(N):
        for c in range(N):
            if copy_visited[r][c] == 0:
                return False
    return temp - 1

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
candidates = []
for r in range(N):
    for c in range(N):
        if maps[r][c] == 2:
            candidates.append((r, c))
        if maps[r][c] == 1:
            visited[r][c] = 1
answer = int(1e9)
for li in combinations(candidates, M):
    temp = bfs(li)
    if temp == False:
        continue
    elif temp == -1:
        answer = 0
    else:
        answer = min(answer, temp)
print(-1) if answer == int(1e9) else print(answer)