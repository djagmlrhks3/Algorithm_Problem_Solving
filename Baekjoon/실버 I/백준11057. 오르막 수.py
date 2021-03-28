import sys
sys.stdin = open('백준11057. 오르막 수.txt', 'r')

N = int(input())
DP = [1] * 10

for _ in range(N-1):
    for idx in range(1,  10):
        DP[idx] += DP[idx-1]
print(sum(DP)%10007)