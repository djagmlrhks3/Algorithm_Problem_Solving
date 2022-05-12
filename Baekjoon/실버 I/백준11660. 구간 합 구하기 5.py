import sys
sys.stdin = open('백준11660. 구간 합 구하기 5.txt', 'r')
N, M = map(int, input().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1, N):
    matrix[0][i] += matrix[0][i-1]
    matrix[i][0] += matrix[i-1][0]
for r in range(1, N):
    for c in range(1, N):
        matrix[r][c] += (matrix[r-1][c] + matrix[r][c-1] - matrix[r-1][c-1])

for _ in range(M):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    if r1 == 1 and c1 == 1:
        print(matrix[r2-1][c2-1])
    elif r1 == 1:
        print(matrix[r2-1][c2-1]-matrix[r2-1][c1-2])
    elif c1 == 1:
        print(matrix[r2-1][c2-1]-matrix[r2-2][c1-1])
    else:
        print(matrix[r2-1][c2-1] - matrix[r2-1][c1-2] - matrix[r1-2][c2-1] + matrix[r1-2][c1-2])