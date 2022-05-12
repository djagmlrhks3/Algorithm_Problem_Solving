import sys
from collections import deque
sys.stdin = open('백준2638. 치즈.txt', 'r')

def air():
    queue = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = -1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+d[i][0], c+d[i][1]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and cheeze[nr][nc] <= 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                    cheeze[nr][nc] = -1

def melt():
    global last
    candidates = []
    for r in range(N):
        for c in range(M):
            if cheeze[r][c] == 1:
                cnt = 0
                for i in range(4):
                    nr, nc = r+d[i][0], c+d[i][1]
                    if 0 <= nr < N and 0 <= nc < M and cheeze[nr][nc] == -1:
                        cnt += 1
                if cnt >= 2:
                    candidates.append((r, c))
    while candidates:
        r, c = candidates.pop()
        cheeze[r][c] = 0
        last -= 1

N, M = map(int, input().split())
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cheeze = []
last, answer = 0, 0
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    last += sum(row)
    cheeze.append(row)

while last:
    air()
    melt()
    answer += 1
print(answer)