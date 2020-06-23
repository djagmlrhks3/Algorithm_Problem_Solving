import sys
sys.stdin = open('백준10026. 적록색약.txt','r')

sys.setrecursionlimit(100000)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def X(x,y,color):
    visited[x][y] = True
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and color == matrix[nx][ny]:
                X(nx,ny,color)

def O(x,y,color):
    visited[x][y] = True
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if color == 'B':
                if matrix[nx][ny] == color:
                    O(nx,ny,color)
            else:
                if matrix[nx][ny] == 'R' or matrix[nx][ny] == 'G':
                    O(nx,ny,color)

N = int(input())
matrix = [ input() for _ in range(N) ]
visited = [ [False]*N for _ in range(N) ]
count_X = count_O = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            X(i,j,matrix[i][j])
            count_X += 1
visited = [ [False]*N for _ in range(N) ]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            O(i,j,matrix[i][j])
            count_O += 1
print(count_X,end=" ");print(count_O)