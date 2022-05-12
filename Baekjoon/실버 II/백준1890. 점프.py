import sys
sys.stdin = open('백준1890. 점프.txt', 'r')
sys.setrecursionlimit(10**6)

def dfs(r, c):
    if r == N-1 and c == N-1:
        return 1
    if DP[r][c] != -1:
        return DP[r][c]
    DP[r][c] = 0
    if r+maps[r][c] < N:
        DP[r][c] += dfs(r+maps[r][c], c)
    if c+maps[r][c] < N:
        DP[r][c] += dfs(r, c+maps[r][c])
    return DP[r][c]

N = int(input())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [[-1] * N for _ in range(N)]

print(dfs(0, 0))