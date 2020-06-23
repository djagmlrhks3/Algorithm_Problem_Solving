import sys
sys.stdin = open('백준7576. 토마토.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
from _collections import deque
def bfs(tomato):
    while tomato:
        i, j = tomato.popleft()
        for z in range(4):
            ni = i+dx[z]
            nj = j+dy[z]
            if 0<= ni < y and 0<= nj < x:
                if not visited[ni][nj] and fields[ni][nj]==0:
                    visited[ni][nj] = visited[i][j] + 1
                    tomato.append((ni,nj))
x, y = map(int, input().split())

fields = [list(map(int, input().split())) for _ in range(y)]

visited = [[0]*x for _ in range(y)]
tomato = deque()
for i in range(y):
    for j in range(x):
        if fields[i][j]==1:
            tomato.append((i,j))
            visited[i][j] = 1
        elif fields[i][j]==-1:
            visited[i][j] = -1
bfs(tomato)

result = 0
flag = False

for li in visited:
    if 0 in li:
        flag = True
        break
    result = max(result, max(li))
print(-1) if flag else print(result-1)