import sys
sys.stdin = open('백준16194. 카드 구매하기 2.txt', 'r')

N = int(input())
costs = list(map(int, sys.stdin.readline().split()))

DP = [[0] * (N+1) for _ in range(N)]

for c in range(1, N+1):
    DP[0][c] = costs[0] * c

for r in range(1, N):
    for c in range(1, N+1):
        if r+1 <= c:
            DP[r][c] = min(DP[r][c-(r+1)]+costs[r], DP[r-1][c])
        else:
            DP[r][c] = DP[r-1][c]
print(DP[-1][-1])