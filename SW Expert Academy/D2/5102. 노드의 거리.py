import sys
sys.stdin = open('5102. 노드의 거리.txt','r')

# T = int(input())
# for tc in range(T):
#     V, E = map(int,input().split())
#     matrix = [ [0]*(V+1) for _ in range(V+1) ]
#     for e in range(E):
#         x, y = map(int,input().split())
#         matrix[x][y] = matrix[y][x] = 1
#     S, G = map(int,input().split())
#     visited = [0]*(V+1)
#     queue = list()
#     queue.append(S)
#     flag = False
#     end = count = 0
#     while len(queue):
#         start = queue.pop(0)
#         visited[start] = 1
#         for i in range(V+1):
#             if matrix[start][i] and not visited[i]:
#                 if i == G:
#                     queue.clear()
#                     flag = True
#                     break
#                 else:
#                     queue.append(i)
#         else:
#             if len(queue) and end not in queue:
#                 count += 1
#                 end = queue[-1]
#     print('#{} {}'.format(tc+1,count+1)) if flag else print('#{} {}'.format(tc+1,0))

T = int(input())
for tc in range(T):
    V, E = map(int,input().split())
    matrix = [ [0]*(V+1) for _ in range(V+1) ]
    for e in range(E):
        x, y = map(int,input().split())
        matrix[x][y] = matrix[y][x] = 1
    S, G = map(int,input().split())
    visited = [0]*(V+1)
    queue = list()
    queue.append(S)
    flag = False
    visited[S] = 1
    while len(queue):
        S = queue.pop(0)
        for i in range(V+1):
            if matrix[S][i] and not visited[i]:
                if i == G:
                    visited[i] = visited[S] + 1
                    queue.clear()
                    flag = True
                    break
                else:
                    queue.append(i)
                    visited[i] = visited[S] + 1
    print('#{} {}'.format(tc+1,visited[G]-1)) if flag else print('#{} {}'.format(tc+1,0))