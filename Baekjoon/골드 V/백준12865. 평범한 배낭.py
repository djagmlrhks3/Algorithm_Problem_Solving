import sys
sys.stdin = open('백준12865. 평범한 배낭.txt', 'r')
N, K = map(int, input().split())

cases = []
for _ in range(N):
    w, v = map(int, input().split())
    cases.append((w, v))

DP = [[0] * (K+1) for _ in range(N+1)]

for row in range(1, N+1):
    for col in range(1, K+1):
        if col >= cases[row-1][0]:
            DP[row][col] = max(DP[row-1][col], DP[row-1][col-cases[row-1][0]] + cases[row-1][1])
        else:
            DP[row][col] = DP[row-1][col]

print(max(DP[-1]))
