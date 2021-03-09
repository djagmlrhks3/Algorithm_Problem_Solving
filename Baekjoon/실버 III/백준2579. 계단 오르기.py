import sys
sys.stdin = open('백준2579. 계단 오르기.txt', 'r')

n = int(input())
stairs = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(n)]

if n == 1:
    print(stairs[-1])
else:
    DP = [0] * (n+1)
    DP[1], DP[2] = stairs[1], stairs[1] + stairs[2]
    for idx in range(3, n+1):
        DP[idx] = max(stairs[idx]+stairs[idx-1]+DP[idx-3], stairs[idx]+DP[idx-2])
    print(DP[-1])