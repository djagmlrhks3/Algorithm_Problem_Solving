import sys
sys.stdin = open('백준2178. 미로 탐색.txt','r')

dx = [0,0,-1,1]
dy = [-1,1,0,0]
N,M = map(int,input().split())
miro = [ list(map(int,input())) for _ in range(N) ]
visited = [[0]*M for _ in range(N)]

x = y = 0
visited[x][y] = 1
queue = list()
queue.append((x,y))
while len(queue):
    start = queue.pop(0)
    x = start[0]
    y = start[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < M and miro[nx][ny] and not visited[nx][ny]:
            queue.append((nx,ny))
            visited[nx][ny] = visited[x][y] + 1
        if nx == N-1 and ny == M-1:
            queue.clear()
            break
print(visited[N-1][M-1])
