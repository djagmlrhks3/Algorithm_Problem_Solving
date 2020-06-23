import sys
sys.stdin = open('3376. 파도반 수열.txt','r')

T = int(input())
for tc in range(T):
    padoban = [1, 1, 1, 2]
    N = int(input())
    if N > 4:
        for i in range(N-4):
            a = padoban[-3]
            b = padoban[-2]
            padoban.append(a + b)
        print('#{} {}'.format(tc + 1, padoban[N - 1]))
    else:
        print('#{} {}'.format(tc + 1, padoban[N - 1]))
