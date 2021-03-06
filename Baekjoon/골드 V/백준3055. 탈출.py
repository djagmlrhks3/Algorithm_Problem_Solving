import sys
from collections import deque
sys.stdin = open('백준3055. 탈출.txt', 'r')

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C = map(int, input().split())
maps = [list(' '.join(map(str, sys.stdin.readline().split()))) for _ in range(R)]

def move_water():
    global R, C
    for _ in range(len(queue_water)):
        r, c = queue_water.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < R and 0 <= nc < C:
                if maps[nr][nc] == '.':
                    maps[nr][nc] = '*'
                    queue_water.append((nr, nc))
                    visited[nr][nc] = 1

def move_pet(cnt):
    global answer
    for _ in range(len(queue_pet)):
        m, r, c = queue_pet.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if maps[nr][nc] == '.':
                    queue_pet.append((cnt+1, nr, nc))
                    maps[nr][nc], maps[r][c] = 'S', '.'
                    visited[nr][nc] = 1
                if maps[nr][nc] == 'D':
                    answer = cnt+1

queue_pet = deque([])
queue_water = deque([])
visited = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if maps[r][c] == 'S':
            queue_pet.append((0, r, c))
            visited[r][c] = 1
        if maps[r][c] == '*':
            queue_water.append((r, c))
            visited[r][c] = 1

answer = 'KAKTUS'
cnt = 0
while queue_pet:
    move_water()
    move_pet(cnt)
    cnt += 1
    if answer != 'KAKTUS': break
print(answer)