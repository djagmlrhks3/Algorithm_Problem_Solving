import sys
sys.stdin = open('백준1926. 그림.txt','r')

dx = [0,0,-1,1]
dy = [-1,1,0,0]
n, m = map(int,input().split())
picture = [ list(map(int,input().split())) for _ in range(n) ]
visited = [[0]*m for _ in range(n)]
result = list()
for i in range(n):
    for j in range(m):
        stack = list()
        if picture[i][j] and not visited[i][j]:
            count = 1
            visited[i][j] = 1
            stack.append((i, j))
            while len(stack):
                start = stack.pop(0)
                x = start[0]
                y = start[1]
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if 0 <= nx < n and 0 <= ny < m:
                        if not visited[nx][ny] and picture[nx][ny]:
                            stack.append((nx,ny))
                            visited[nx][ny] = 1
                            count += 1
            result.append(count)

if len(result):
    print(len(result));print(max(result))
else:
    print(0);print(0)
