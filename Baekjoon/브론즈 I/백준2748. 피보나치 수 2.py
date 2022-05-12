import sys
sys.stdin = open('백준2748. 피보나치 수 2.txt', 'r')
n = int(input())
DP = [0, 1] + [0] * (n-1)
for i in range(2, n+1):
    DP[i] = DP[i-1] + DP[i-2]
print(DP[-1])