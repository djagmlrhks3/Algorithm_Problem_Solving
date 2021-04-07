import sys
sys.stdin = open('백준11058. 크리보드.txt', 'r')

N = int(input())
DP = [i for i in range(N+1)]
for i in range(7, N+1):
    DP[i] = max(DP[i-3]*2, DP[i-4]*3, DP[i-5]*4)
print(DP[N])