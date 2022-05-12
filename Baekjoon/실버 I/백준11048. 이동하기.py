import sys
sys.stdin = open('백준11048. 이동하기.txt', 'r')

N, M = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

DP = [[0] * M for _ in range(N)]
DP[0][0] = maps[0][0]
for r in range(1, N):
    DP[r][0] = maps[r][0] + DP[r-1][0]
for c in range(1, M):
    DP[0][c] = maps[0][c] + DP[0][c-1]
for r in range(1, N):
    for c in range(1, M):
        DP[r][c] = maps[r][c] + max(DP[r-1][c-1], DP[r-1][c], DP[r][c-1])
print(DP[-1][-1])