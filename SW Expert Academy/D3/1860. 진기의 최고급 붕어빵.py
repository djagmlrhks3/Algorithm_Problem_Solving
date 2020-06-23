"""
0초부터
M초의시간을들여
K개의 붕어빵을만듦
초단위로 언제도착하는지 N명
M초로 시간이 나눠지면 K개 붕어빵 +

"""
import sys
sys.stdin=open('1860. 진기의 최고급 붕어빵.txt','r')

T = int(input())
for tc in range(T):
    N,M,K = map(int,input().split())
    customer = list(map(int,input().split()))
    customer.sort()
    fish = [K] * ((11111//M)+1)
    flag = True
    # print(fish)
    for i in customer:
        if i<M:
            flag = False
            break
        else:
            if fish[(i//M)-1]:
                fish[(i // M)-1] -= 1
            else:
                if sum(fish[:i//M]):
                    for j in range((i//M)-1):
                        if fish[j]:
                            fish[j] -= 1
                            break
                else:
                    flag = False
                    break

    if flag:
        print('#{} {}'.format(tc+1,'Possible'))
    else:
        print('#{} {}'.format(tc+1,'Impossible'))
