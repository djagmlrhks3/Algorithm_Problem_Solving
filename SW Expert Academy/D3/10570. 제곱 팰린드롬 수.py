import sys
sys.stdin = open('10570. 제곱 팰린드롬 수.txt', 'r')

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    # print((A**0.5))
    a = int(A**0.5) + 1 if A**0.5 > int(A**0.5) else int(A**0.5)
    b = int(B**0.5) if B**0.5 > int(B**0.5) else int(B**0.5)
    res = 0
    for i in range(a, b+1):
        if str(i) == str(i)[::-1]:
            if str(i**2) == str(i**2)[::-1]:
                res += 1
    print('#{} {}'.format(tc+1, res))