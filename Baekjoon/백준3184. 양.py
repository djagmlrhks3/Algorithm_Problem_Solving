import sys
sys.stdin = open('백준3184. 양.txt','r')

from _collections import deque
"""
v : 늑대
o : 양
. : 필드
# : 울타리
"""
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(r, c):
    global r_wolf, r_sheep
    visited = [[False]*C for _ in range(R)]
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and fields[i][j] != '#':
                sheep = 1 if fields[i][j] == 'o' else 0
                wolf = 1 if fields[i][j] == 'v' else 0
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    start = queue.popleft()
                    x, y = start[0], start[1]
                    for z in range(4):
                        nx = x + dx[z]
                        ny = y + dy[z]
                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                            if fields[nx][ny] == '.':
                                queue.append((nx, ny))
                            elif fields[nx][ny] == 'v':
                                queue.append((nx, ny))
                                wolf += 1
                            elif fields[nx][ny] == 'o':
                                queue.append((nx, ny))
                                sheep += 1
                            visited[nx][ny] = True
                if wolf >= sheep:r_wolf += wolf
                else:r_sheep += sheep

R, C = map(int,input().split())
fields = [input() for _ in range(R)]
r_wolf = 0
r_sheep = 0

bfs(R, C)
print(r_sheep, r_wolf)
