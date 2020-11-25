import sys
sys.stdin = open('10726. 이진수 표현.txt')

def check():
    global N, M
    for i in range(N):
        if not M % 2:
            return False
        M //= 2
    else:
        return True

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    res = 'ON' if check() else 'OFF'
    print('#{} {}'.format(tc+1, res))

