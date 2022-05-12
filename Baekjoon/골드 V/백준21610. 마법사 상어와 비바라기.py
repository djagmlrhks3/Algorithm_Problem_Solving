from collections import deque
import sys
sys.stdin = open('백준21610. 마법사 상어와 비바라기.txt', 'r')

def move(dir, s):
    global clouds
    check = [[False] * N for _ in range(N)]
    move_clouds = []
    for i in range(len(clouds)):
        cr, cc = clouds[i][0], clouds[i][1]
        nr = (N + cr + (d[dir][0]) * s) % N
        nc = (N + cc + (d[dir][1]) * s) % N
        basket[nr][nc] += 1
        move_clouds.append((nr, nc))
        check[nr][nc] = True
    for r, c in move_clouds:
        if check[r][c]:
            for i in (2, 4, 6, 8):
                nr = r + d[i][0]
                nc = c + d[i][1]
                if 0 <= nr < N and 0 <= nc < N:
                    if basket[nr][nc]:
                        basket[r][c] += 1
    make(check)

def make(check):
    global clouds
    clouds.clear()
    for r in range(N):
        for c in range(N):
            if basket[r][c] >= 2 and not check[r][c]:
                clouds.append((r, c))
                basket[r][c] -= 2

d = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1),
     (0, 1), (1, 1), (1, 0), (1, -1)]

N, M = map(int, input().split())

clouds = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])
basket = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(M):
    dir, s = map(int, sys.stdin.readline().split())
    move(dir, s)

answer = 0
for row in basket:
    answer += sum(row)
print(answer)