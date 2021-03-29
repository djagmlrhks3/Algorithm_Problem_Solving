import sys
sys.stdin = open('백준11052. 카드 구매하기.txt', 'r')

N = int(input())
value = list(map(int, sys.stdin.readline().split()))
DP = [[0] * (N+1) for _ in range(N)]

for c in range(1, N+1):
    DP[0][c] = c * value[0]

for r in range(1, N):
    for c in range(1, N+1):
        if r+1 <= c:
            DP[r][c] = max(DP[r][c-(r+1)] + value[r], DP[r-1][c])
        else:
            DP[r][c] = DP[r-1][c]

print(DP[-1][-1])