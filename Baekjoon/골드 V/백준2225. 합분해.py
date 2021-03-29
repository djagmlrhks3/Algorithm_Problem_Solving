import sys
sys.stdin = open('백준2225. 합분해.txt', 'r')
N, K = map(int, input().split())
DP = [[1] * N] + [[0] * N for _ in range(K-1)]
for r in range(1, K):
    DP[r][0] = r+1

for r in range(1, K):
    for c in range(1, N):
        DP[r][c] = DP[r-1][c] + DP[r][c-1]

print(DP[K-1][N-1] % 1000000000)