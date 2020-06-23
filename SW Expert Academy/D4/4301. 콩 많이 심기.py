import sys
sys.stdin = open('4301. 콩 많이 심기.txt','r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    matrix = [ [0] * N for _ in range(M) ]
    dx = [0,2,0,-2]
    dy = [2,0,-2,0]
    for i in range(M):
        for j in range(N):
            if not matrix[i][j]:
                for z in range(4):
                    if 0<= i + dx[z] < M and 0<= j + dy[z] < N:
                        matrix[i + dx[z]][j + dy[z]] = 1
    total = 0
    for i in matrix:
        total += sum(i)
    print('#{} {}'.format(tc+1,M*N-total))