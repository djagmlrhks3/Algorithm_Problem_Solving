import sys
sys.stdin = open('백준2167. 2차원 배열의 합.txt', 'r')

N, M = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

K = int(input())
answer = []
for r in range(N):
    for c in range(M):
        if r == 0 and c == 0:
            continue
        elif r == 0:
            matrix[r][c] += matrix[r][c-1]
        elif c == 0:
            matrix[r][c] += matrix[r-1][c]
        else:
            matrix[r][c] += matrix[r-1][c] + matrix[r][c-1] - matrix[r-1][c-1]

for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    if r1 == 1 and c1 == 1:
        print(matrix[r2-1][c2-1])
    elif r1 == 1:
        print(matrix[r2-1][c2-1] - matrix[r2-1][c1-2])
    elif c1 == 1:
        print(matrix[r2-1][c2-1] - matrix[r1-2][c2-1])
    else:
        print(matrix[r2-1][c2-1] - matrix[r2-1][c1-2] - matrix[r1-2][c2-1] + matrix[r1-2][c1-2])