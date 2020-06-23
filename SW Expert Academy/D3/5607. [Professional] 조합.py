import sys
sys.stdin = open('5607. [Professional] 조합.txt','r')

T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    p = 1234567891


    def mul(a, b):
        if b == 0:
            return 1
        elif b == 1:
            return a
        elif b % 2 > 0:
            return mul(a, b - 1) * a
        else:
            d = mul(a, b // 2)
            d %= p
            return d ** 2 % p
    A = 1
    B = 1
    for i in range(1, n + 1):
        A *= i
        A %= p
    for i in range(1, k + 1):
        B *= i
        B %= p
    for i in range(1, n - k + 1):
        B *= i
        B %= p

    B = mul(B, (p - 2) % p)
    print('#{} {}'.format(tc+1,(A * B) % p))