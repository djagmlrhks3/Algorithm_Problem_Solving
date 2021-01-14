import sys
sys.stdin = open('백준16236. 아기 상어.txt', 'r')

from collections import deque
N = int(input())
tank = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

now = 2 # 현재 상어 크기
upgrade = 0 # 상어가 진화하기 위해 먹은 개수
answer = 0 # 이동 거리
shark_r, shark_c = 0, 0 # 현재 아기상어 위치
sharks = [] # 먹이를 담을 배열

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find(x, y):
    global now
    queue = deque([(x, y)])
    possible = []
    visit[x][y] = 0
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < N and 0 <= nc < N:
                if tank[nr][nc] <= now and visit[nr][nc] == -1:
                    queue.append((nr, nc))
                    visit[nr][nc] = visit[r][c] + 1
                    if tank[nr][nc] and tank[nr][nc] < now:
                        possible.append((nr, nc, visit[r][c] + 1))
    return possible

for r in range(N):
    for c in range(N):
        if 1 <= tank[r][c] <= 6:
            sharks.append((r, c, tank[r][c]))
        if tank[r][c] == 9:
            shark_r, shark_c = r, c

while True:
    visit = [[-1] * N for _ in range(N)]
    candidates = sorted(find(shark_r, shark_c), key=lambda x:[-x[2], -x[0], -x[1]])
    if candidates:
        target = candidates.pop()
        tank[shark_r][shark_c] = 0
        shark_r, shark_c = target[0], target[1]
        answer += target[2]
        upgrade += 1
        if upgrade == now:
            now += 1
            upgrade = 0
    else:
        break
print(answer)
