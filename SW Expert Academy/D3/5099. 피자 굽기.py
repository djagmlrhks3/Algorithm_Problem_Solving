import sys
sys.stdin = open('5099. 피자 굽기.txt','r')

# T = int(input())
# for tc in range(T):
#     N, M = map(int,input().split())
#     pizza = list(map(int,input().split()))
#     fan = pizza[:N]
#     fan_idx = [ i for i in range(N) ]
#     idx = N-1
#     circle = 0
#     while fan.count(0) != N-1:
#         if circle == N:
#             circle = 0
#         if fan[circle]//2:
#             fan[circle] = fan[circle]//2
#             circle += 1
#         else:
#             if M-1 > idx:
#                 idx += 1
#                 fan_idx[circle] = idx
#                 fan[circle] = pizza[idx]
#                 circle += 1
#             else:
#                 fan[circle] = 0
#                 fan_idx[circle] = 0
#                 circle += 1
#
#     for i in fan_idx:
#         if i:
#             break
#     print('#{} {}'.format(tc + 1, i + 1))

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    pizza = list(map(int,input().split()))
    fan = [i for i in range(N) ]
    rest = [ i for i in range(N,M) ]
    while pizza.count(0) != M-1:
        idx = fan.pop(0)
        if pizza[idx]//2:
            pizza[idx] = pizza[idx]//2
            fan.append(idx)
        else:
            if len(rest):
                pizza[idx] = 0
                fan.append(rest.pop(0))
            else:
                pizza[idx] = 0

    for i in range(len(pizza)):
        if pizza[i]:
            print('#{} {}'.format(tc+1,i+1))
            break