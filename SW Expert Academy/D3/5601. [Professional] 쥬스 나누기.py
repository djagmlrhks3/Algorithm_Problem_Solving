import sys
sys.stdin = open('5601. [Professional] 쥬스 나누기.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    print('#{}'.format(tc+1),end=" ")
    for i in range(N):
        print('1/{}'.format(N),end=" ")
    print()