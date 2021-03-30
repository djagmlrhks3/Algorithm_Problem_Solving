import sys
sys.stdin = open('백준15988. 1, 2, 3 더하기 3.txt', 'r')

DP = [0] * 1000001
DP[1], DP[2], DP[3] = 1, 2, 4
for idx in range(4, 1000001):
    DP[idx] = DP[idx - 1] % 1000000009 + DP[idx - 2] % 1000000009 + DP[idx - 3] % 1000000009
for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    print(DP[n]%1000000009)