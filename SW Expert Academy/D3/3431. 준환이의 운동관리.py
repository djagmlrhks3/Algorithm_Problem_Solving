import sys
sys.stdin = open('3431. 준환이의 운동관리.txt','r')

T = int(input())
for tc in range(T):
    L, U, X = map(int,input().split())
    if X > U:
        print('#{} {}'.format(tc+1,-1))
    elif X < L:
        print('#{} {}'.format(tc+1,L-X))
    elif L <= X <= U:
        print('#{} {}'.format(tc+1,0))