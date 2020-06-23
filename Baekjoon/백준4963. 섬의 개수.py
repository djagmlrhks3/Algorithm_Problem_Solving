import sys
sys.stdin = open('4963백준. 섬의 개수.txt','r')
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,1,-1,-1,0,1]
T = int(input())
for tc in range(T):
    w, h = map(int,input().split())
    matrix = []
    for i in range(h):
        matrix.append(list(map(int,input().split())))
    visited = list()
    queue = list()
    count = 0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] and (i,j) not in visited:
                queue.append((i,j))
                while len(queue):
                    start = queue.pop(0)
                    visited.append(start)
                    x = start[0]
                    y = start[1]
                    for z in range(8):
                        nx = x + dx[z]
                        ny = y + dy[z]
                        if 0<= nx < h and 0<= ny <w and matrix[nx][ny] and (nx,ny) not in visited:
                            queue.append((nx,ny))
                count += 1
    print(count)