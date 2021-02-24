import sys
sys.stdin = open('백준1904. 01타일.txt', 'r')

N = int(input())
DP = [1, 1] + [0] *(N-1)
for idx in range(2, N+1):
    DP[idx] = (DP[idx-1] + DP[idx-2]) % 15746
print(DP[N])
