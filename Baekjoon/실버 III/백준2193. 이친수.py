import sys
sys.stdin = open('백준2193. 이친수.txt', 'r')

N = int(input())
DP = [1, 1] + [0] * (N-2)
for idx in range(2, N):
    DP[idx] = DP[idx-1] + DP[idx-2]
print(DP[-1])