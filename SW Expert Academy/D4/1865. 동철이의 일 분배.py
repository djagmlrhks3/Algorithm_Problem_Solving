import sys
sys.stdin = open('1865. 동철이의 일 분배.txt','r')


def f(n,k,s):
    global maximum
    if maximum >= s:
        return
    if n == k and s > maximum:
        maximum = s
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                f(n + 1, k, s * (P[i][n]/100))
                used[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    P = list()
    for n in range(N):
        P.append(list(map(int,input().split())))
    used = [0] * N
    maximum = 0
    f(0,N,1)
    maximum *= 100
    print('#{} {:6f}'.format(tc+1,maximum))

