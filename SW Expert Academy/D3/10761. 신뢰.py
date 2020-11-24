import sys
sys.stdin = open('10761. 신뢰.txt', 'r')

T = int(input())
for tc in range(T):
    A, B = 0, 0
    res = 0
    N, *args = list(input().split())
    for n in range(int(N)):
        if args[n*2] == 'A':
            A = int(args[n*2 + 1]) - A
        else:
            B = int(args[n*2 + 1]) - B
        if n % 2:
            res += max(A, B)
    print(res)

