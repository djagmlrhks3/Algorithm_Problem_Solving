import sys
sys.stdin = open('5250. 최소 비용.txt', 'r')

# from _collections import deque
# direction = [(0,1), (1,0)]
# def bfs(i, j):
#     global result, N
#     queue = deque()
#     visited = []
#
#     queue.append((i,j))
#     while queue:
#         i, j = queue.popleft()
#         visited.append((i, j))
#         for d in direction:
#             ni = i + d[0]
#             nj = j + d[1]
#             if ni < N and nj < N and (ni, nj) not in visited:


T = int(input())
for tc in range(T):
    N = int(input())
    graph = [ list(map(int, input().split())) for _ in range(N) ]
    result = 0
    INF = float('inf')
    dist = [INF] * N
    selected = []

    dist[0] = 0
    cnt = 0
    while cnt < N:
        mini = INF
        start = -1
        for i in range(N):
            if dist[i] < mini and not selected[i]:
                mini = dist[i]
                start = i
        selected[i] = True
        cnt += 1
        for j in graph[i]:
            if not j and