import sys
sys.stdin = open('백준2294. 동전 2.txt', 'r')
n, k = map(int, input().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
DP = [int(1e9)] * (k+1)
DP[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        DP[i] = min(DP[i-coin]+1, DP[i])
print(DP[-1]) if DP[-1] != int(1e9) else print(-1)