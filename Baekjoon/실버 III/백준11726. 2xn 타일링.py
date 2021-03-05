import sys
sys.stdin = open('백준11726. 2xn 타일링.txt', 'r')

n = int(input())

DP = [0] * (n + 1)
DP[0] = DP[1] = 1

for idx in range(2, n+1):
    DP[idx] = DP[idx-1] + DP[idx-2]
print(DP[n] % 10007)