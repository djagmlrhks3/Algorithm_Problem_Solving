import sys
sys.stdin = open('1249. 보급로.txt','r')

from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(input())
for tc in range(T):
    N = int(input())
    #input값이 문자열이므로 숫자형으로 분리
    warmap = [list(map(int,''.join(input()))) for _ in range(N)]
    #Dijkstra 알고리즘 구현위해 visited setting
    INF = float('inf')
    visited = [[INF]*N for _ in range(N)]
    #시작점 (0, 0)방문표시 및 enqueue
    visited[0][0] = 0
    queue = deque([(0,0)])
    while queue:
        start = queue.popleft()
        x, y = start[0], start[1]
        #상하좌우 탐색
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 <= nx < N and 0 <= ny < N:
                #Dijkstra 알고리즘 핵심부분(중요) : 가중치 비교
                if visited[nx][ny] > visited[x][y] + warmap[x][y]:
                    visited[nx][ny] = visited[x][y] + warmap[x][y]
                    queue.append((nx,ny))
    print('#{} {}'.format(tc+1,visited[N-1][N-1]))