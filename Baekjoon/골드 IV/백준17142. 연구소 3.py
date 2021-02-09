import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
sys.stdin = open('백준17142. 연구소 3.txt', 'r')


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(virus, not_activate, matrix, empty):
    global answer
    for r, c in virus:
        matrix[r][c] = 0
    queue = deque(virus)
    time = 0
    while queue:
        if not empty: break
        if time >= answer: break
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < N and 0 <= nc  < N:
                if not matrix[nr][nc] and (nr, nc) not in virus:
                    matrix[nr][nc] = matrix[r][c] + 1
                    time = matrix[r][c] + 1
                    queue.append((nr, nc))
                    empty -= 1
                if matrix[nr][nc] == 2 and (nr, nc) in not_activate:
                    if empty:
                        matrix[nr][nc] = matrix[r][c] + 1
                        time = matrix[r][c] + 1
                        queue.append((nr, nc))
                    else:
                        matrix[nr][nc] = matrix[r][c]

    if not empty:
        answer = min(answer, time)

N, M = map(int, input().split())
empty = 0
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

virus= []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 2:
            virus.append((r, c))
        elif not matrix[r][c]:
            empty += 1

answer = int(1e9)
for li in combinations(virus, M):
    bfs(li, list(set(virus) - set(li)), deepcopy(matrix), empty)

print(answer) if answer != int(1e9) else print(-1)