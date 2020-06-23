import sys
sys.stdin = open('3499. 퍼펙트 셔플.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    shuffle = list(input().split())
    order = [ i for i in range(N+1) ]
    if N%2:
        front = order[:N//2+1]
        back = order[N//2+1:]
        print('#{}'.format(tc+1),end=" ")
        for i in range(N):
            if i%2:
                print(shuffle[back.pop(0)], end=" ")
            else:
                print(shuffle[front.pop(0)],end=" ")
        print()
    else:
        front = order[:N // 2]
        back = order[N // 2:]
        print('#{}'.format(tc+1),end=" ")
        for i in range(N):
            if i%2:
                print(shuffle[back.pop(0)], end=" ")
            else:
                print(shuffle[front.pop(0)],end=" ")
        print()
