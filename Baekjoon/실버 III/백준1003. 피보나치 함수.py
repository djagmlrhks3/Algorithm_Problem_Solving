import sys
sys.stdin = open('백준1003. 피보나치 함수.txt', 'r')

def fibo(num):
    global DP, N
    if num > N:return
    else:
        DP[num][0] = DP[num-1][0] + DP[num-2][0]
        DP[num][1] = DP[num-1][1] + DP[num-2][1]
        fibo(num+1)

T = int(input())
for _ in range(T):
    N = int(input())
    DP = [[1, 0], [0, 1]] + [[0, 0] for _ in range(N-1)]
    fibo(2)
    print(' '.join(map(str, DP[N])))

