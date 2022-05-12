import sys
sys.stdin = open('백준1495. 기타리스트.txt', 'r')

N, S, M = map(int, input().split())
V = [0] + list(map(int, sys.stdin.readline().split()))
DP = [[0] * (M+1) for _ in range(N+1)]
DP[0][S] = 1
for i in range(1, N+1): # 1 ~ N까지
    for m in range(M+1):
        if DP[i-1][m]:
            if m + V[i] <= M:
                DP[i][m+V[i]] = 1
            if m - V[i] >= 0:
                DP[i][m-V[i]] = 1

res = -1
for v in range(len(DP[-1])):
    if DP[-1][v]:
        res = v
print(res)
