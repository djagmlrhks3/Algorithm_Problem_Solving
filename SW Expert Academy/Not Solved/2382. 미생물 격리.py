import sys
sys.stdin = open('2382. 미생물 격리.txt', 'r')



def check(groups):
    for i in range(len(groups)):
        same = []
        cell = groups.popleft()
        for j in groups:
            if cell[0] == j[0] and cell[1] == j[1]:


from _collections import deque

directions = [None, (-1,0), (1,0), (-1,0), (0,1)]
T = int(input())
for tc in range(T):
    """
    N : 셀의개수
    M : 격리시간
    K : 군집의 개수
    """
    #1시간마다 이동
    #약품이 칠해진 곳에 도착, 미생물의 절반이 죽고 이동방향이 반대 (홀수면 /2 버림)
    #1마리면 0이되니까 사라짐
    #군집이 모이면 미생물수는 + 방향은 많은 수에 따름(합쳐질 때 미생물 수가 같은경우는X)
    N, M, K = map(int ,input().split())

    groups = deque()
    for k in range(K):
        y, x, num, direction = map(int, input().split())
        matrix[y][x] = num
    #막힌 부분 : 돌리고나서 계산...
    for m in range(M):
        matrix = [[0]*N for _ in range(N)]
        for k in range(K):
            cell = groups.popleft()
            
            i, j, value, d = cell[0], cell[1], cell[2], cell[3]
            ni = i + directions[d][0]
            nj = j + directions[d][1]
            if 0 < ni < N and 0 < nj < N:
                matrix[ni][nj] = value
                deque.append((ni, nj, value, d))
            elif value == 1:
                continue
            else:
                deque.append((ni, nj, value//2, ))
        check(groups)
    #행렬을 ㅍ현

    #미생물의 수를 출력