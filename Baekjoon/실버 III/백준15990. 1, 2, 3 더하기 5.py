import sys
sys.stdin = open('백준15990. 1, 2, 3 더하기 5.txt', 'r')

DP = [[0] * 3 for _ in range(100001)]
DP[1][0] = DP[2][1] = 1
DP[3] = [1, 1, 1]

for i in range(4, 100001):
    DP[i][0] = (DP[i-1][1] + DP[i-1][2]) % 1000000009
    DP[i][1] = (DP[i-2][0] + DP[i-2][2]) % 1000000009
    DP[i][2] = (DP[i-3][0] + DP[i-3][1]) % 1000000009

for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    print(sum(DP[n]) % 1000000009)