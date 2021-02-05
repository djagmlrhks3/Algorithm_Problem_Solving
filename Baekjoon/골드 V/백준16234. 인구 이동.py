import sys
from collections import deque
sys.stdin = open('백준16234. 인구 이동.txt', 'r')

def union(g_country, g_people):
    for idx in range(len(g_country)):
        total = len(g_country[idx])
        for r, c in g_country[idx]:
            country[r][c] = int(g_people[idx] / total)

def find(g_country, g_people):
    queue = deque([])
    temp = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                temp.append((i, j))
                queue.append((i, j))
                cnt += country[i][j]
                while queue:
                    r, c = queue.popleft()
                    visited[r][c] = 1
                    for idx in range(4):
                        nr = r + d[idx][0]
                        nc = c + d[idx][1]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and (nr, nc) not in temp:
                            if L <= abs(country[r][c] - country[nr][nc]) <= R:
                                queue.append((nr, nc))
                                temp.append((nr, nc))
                                cnt += country[nr][nc]
                if len(temp) > 1:
                    g_country.append(temp)
                    g_people.append(cnt)
                temp = []
                cnt = 0

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, L, R = map(int, sys.stdin.readline().split())
country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

time = 0

while True:
    visited = [[0] * N for _ in range(N)]
    g_country = deque([])
    g_people = deque([])
    find(g_country, g_people)
    if not len(g_country): break
    union(g_country, g_people)
    time += 1
print(time)



