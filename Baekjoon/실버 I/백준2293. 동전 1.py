import sys
sys.stdin = open('백준2293. 동전 1.txt', 'r')
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1] + [0] * (k)

for coin in coins:
    for v in range(1, k+1):
        if v >= coin:
            dp[v] += dp[v-coin]
print(dp[k])