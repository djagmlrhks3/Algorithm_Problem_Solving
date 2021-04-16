# DFS + DP
import sys
sys.stdin = open('백준1520. 내리막 길.txt', 'r')
sys.setrecursionlimit(10**6)
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
M, N = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
DP = [[-1] * N for _ in range(M)]

def dfs(r, c):
    if r == M-1 and c == N-1:
        return 1
    if DP[r][c] != -1:
        return DP[r][c]
    DP[r][c] = 0
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if 0 <= nr < M and 0 <= nc < N and maps[r][c] > maps[nr][nc]:
            DP[r][c] += dfs(nr, nc)
    return DP[r][c]

print(dfs(0, 0))
