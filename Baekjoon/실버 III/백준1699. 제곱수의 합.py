import sys
sys.stdin = open('백준1699. 제곱수의 합.txt', 'r')

N = int(input())
DP = [i for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i):
        if j ** 2 == i:
            DP[i] = 1
            break
        if j ** 2 > i:
            break
        DP[i] = min(DP[i-j**2]+1, DP[i])
print(DP[N])