import sys
sys.stdin = open('백준15486. 퇴사 2.txt', 'r')
N = int(input())
time, cost = [], []
DP = [0] * (N+1)
for i in range(N):
    t, c = map(int, sys.stdin.readline().split())
    time.append(t)
    cost.append(c)

for i in range(N):
    if i + time[i] <= N:
        DP[i+time[i]] = max(DP[i+time[i]], DP[i]+cost[i])
    DP[i+1] = max(DP[i+1], DP[i])
print(max(DP))