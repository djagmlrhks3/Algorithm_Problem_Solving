import sys
from collections import deque
sys.stdin = open('백준4179. 불!.txt', 'r')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
R, C = map(int, input().split())
maps = [list(''.join(sys.stdin.readline().rstrip())) for _ in range(R)]
answer = 0
def fire():
    for _ in range(len(fire_queue)):
        r, c = fire_queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if maps[nr][nc] != '#':
                    maps[nr][nc] = 'F'
                    visited[nr][nc] = 1
                    fire_queue.append((nr, nc))

def man():
    global answer, flag
    for _ in range(len(man_queue)):
        r, c, s = man_queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < R and 0 <= nc < C:
                if maps[nr][nc] == '.':
                    maps[nr][nc] = 'J'
                    visited[nr][nc] = 1
                    man_queue.append((nr, nc, s+1))
            else:
                answer = s+1

flag = True
man_queue = deque([])
fire_queue = deque([])
visited = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if maps[r][c] == 'F':
            fire_queue.append((r, c))
            visited[r][c] = 1
        elif maps[r][c] == 'J':
            man_queue.append((r, c, 0))
            visited[r][c] = 1

while man_queue:
    fire()
    man()
    if answer > 0: break
print(answer if answer else "IMPOSSIBLE")