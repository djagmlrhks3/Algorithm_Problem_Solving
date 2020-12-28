import sys
sys.stdin = open('10965. 제곱수 만들기.txt', 'r')

prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)
answer = []
T = int(input())
for tc in range(T):
    A = int(input())
    res = 1
    if A**0.5 != int(A**0.5):
        for p in prime:
            cnt = 0
            while not A % p:
                A //= p
                cnt += 1
            if cnt % 2:
                res *= p
            if A == 1 or p > A:
                break
        if A > 1:
            res *= A
    answer.append('#{} {}'.format(tc+1, res))
for ans in answer:
    print(ans)

    # for i in range(2, A+1):
    #     cnt = 0
    #     if not A%i:
    #         while True:
    #             if not A%i:
    #                 cnt += 1
    #                 A //= i
    #             else:
    #                 break
    #         if cnt % 2:
    #             res *= i
    #     if A == 1:
    #         break
    # print('#{} {}'.format(tc+1, res))