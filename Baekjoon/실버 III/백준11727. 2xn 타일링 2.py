import sys
sys.stdin = open('백준11727. 2xn 타일링 2.txt', 'r')

n = int(input())
DP = [0] * (n+2)

DP[1], DP[2] = 1, 3
for idx in range(3, n+1):
    DP[idx] = DP[idx-1] + 2 * DP[idx-2]
print(DP[n] % 10007)