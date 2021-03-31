import sys
sys.stdin = open('백준13398. 연속합 2.txt', 'r')

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

DP = [[0, 0] for _ in range(n)]
DP[0] = [arr[0], -int(1e9)]
for i in range(1, n):
    DP[i][0] = max(DP[i-1][0]+arr[i], arr[i])
    DP[i][1] = max(DP[i-1][0], DP[i-1][1]+arr[i])

answer = -int(1e9)
for idx in range(n):
    answer = max(answer, max(DP[idx]))
print(answer)