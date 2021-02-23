import sys
sys.stdin = open('백준9461. 파도반 수열.txt', 'r')

T = int(input())
DP = [0, 1, 1] + [0] * 98
for _ in range(T):
    N = int(input())
    for idx in range(N+1):
        if not DP[idx]:
            DP[idx] = DP[idx-2] + DP[idx-3]
    print(DP[N])
