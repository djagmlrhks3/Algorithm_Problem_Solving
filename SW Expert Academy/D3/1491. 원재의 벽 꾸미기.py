import sys
sys.stdin = open('1491. 원재의 벽 꾸미기.txt','r')

T = int(input())
for tc in range(T):
    N, A, B = map(int,input().split())
    n = int(N**(0.5))
    minimum = 1000000000
    MA = 1
    if n**2 == N:
        print('#{} {}'.format(tc+1,0))
    else:
        center = int(N**(0.5))
        for r in range(center,N+1):
            for c in range(center,1,-1):
                    area = r*c
                    if area <= N:
                        test = A * abs(r-c) + B * (N-(r*c))
                        if area >= MA and test < minimum:
                            MA = area
                            minimum = test

        print('#{} {}'.format(tc+1,minimum))
