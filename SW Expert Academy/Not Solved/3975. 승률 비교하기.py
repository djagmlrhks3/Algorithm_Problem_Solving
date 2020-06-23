import sys
sys.stdin = open('3975. 승률 비교하기.txt','r')

T = int(input())
for tc in range(T):
    A, B, C, D = map(int,input().split())
    alice = A/B
    bob = C/D
    if alice>bob:
        print('#{} {}'.format(tc+1,'ALICE'))
    elif alice<bob:
        print('#{} {}'.format(tc + 1, 'BOB'))
    elif alice==bob:
        print('#{} {}'.format(tc + 1, 'DRAW'))