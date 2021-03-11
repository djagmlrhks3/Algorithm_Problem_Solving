import sys
sys.stdin = open('백준2740. 행렬 곱셈.txt', 'r')

N, M = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

res = [[0] * K for _ in range(N)]
for r in range(N):
    for c in range(K):
        temp = 0
        for idx in range(M):
            temp += A[r][idx] * B[idx][c]
        res[r][c] = temp

for row in res:
    print(' '.join(list(map(str, row))))