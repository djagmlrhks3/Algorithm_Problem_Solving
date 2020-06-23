import sys
sys.stdin = open('6057. 그래프의 삼각형.txt','r')

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    matrix = [[0]*(N+1) for _ in range(N+1)]
    for m in range(M):
        x, y = map(int,input().split())
        matrix[x][y] = matrix[y][x] = 1
    count = 0
    result = list()
    candidate= list()
    for i in range(1,N+1):
        for j in range(i,N+1):
            if matrix[i][j] and i<j:
                for z in range(j,N+1):
                    if matrix[j][z] and matrix[z][i]:
                        count += 1

    print('#{} {}'.format(tc+1,count))