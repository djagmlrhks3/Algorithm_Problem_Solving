import sys
sys.stdin = open('백준10844. 쉬운 계단 수.txt', 'r')

N = int(input())
dp = [0] * 10
copy_dp = [1] * 10
for _ in range(N-1):
    dp[0] = copy_dp[1]
    dp[-1] = copy_dp[-2]
    for idx in range(1, 9):
        dp[idx] = copy_dp[idx-1] + copy_dp[idx+1]
    copy_dp = dp[:]
print(sum(copy_dp[1:]))