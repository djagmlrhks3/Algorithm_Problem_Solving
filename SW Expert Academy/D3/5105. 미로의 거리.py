import sys
sys.stdin = open('5105. 미로의 거리.txt','r')
# sys.stdin = open('미로의거리_input2.txt','r')
dx = [0,0,-1,1]
dy = [-1,1,0,0]
T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [ list(map(int,input())) for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start = (i,j)
            if matrix[i][j] == 3:
                end = (i,j)
#     visited = list()
#     queue = list()
#     queue.append(start)
#     flag = False
#     count = end = 0
#     while len(queue):
#         start = queue.pop(0)
#         x = start[0]
#         y = start[1]
#         visited.append((x,y))
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<= nx < N and 0<= ny < N and (nx,ny) not in visited:
#                 if not matrix[nx][ny]:
#                     queue.append((nx, ny))
#                 if matrix[nx][ny] == 3:
#                     flag = True
#                     queue.clear()
#                     break
#         else:
#             if len(queue) and end not in queue:
#                 count += 1
#                 end = queue[-1]
#     print('#{} {}'.format(tc+1,count)) if flag else print('#{} {}'.format(tc+1,0))
    visited = [[0]*N for _ in range(N)]
    queue = list()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    flag = False
    while len(queue):
        start = queue.pop(0)
        x = start[0]
        y = start[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < N:
                if not matrix[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                if matrix[nx][ny] == 3:
                    flag = True
                    visited[nx][ny] = visited[x][y] + 1
                    queue.clear()
                    break

    print('#{} {}'.format(tc+1,visited[end[0]][end[1]]-2)) if flag else print('#{} {}'.format(tc+1,0))
