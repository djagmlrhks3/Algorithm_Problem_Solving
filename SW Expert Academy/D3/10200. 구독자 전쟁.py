import sys
sys.stdin = open('10200. 구독자 전쟁.txt', 'r')

T = int(input())
for tc in range(T):
    N, A, B = map(int, input().split())
    maximum = 0
    minimum = 0
    if A >= B:
        maximum = B
    if A <= B:
        maximum = A
    if A + B >= N:
        minimum = A + B - N
    print('#{} {} {}'.format(tc+1, maximum, minimum))