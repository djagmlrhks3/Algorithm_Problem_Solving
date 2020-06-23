import sys
sys.stdin = open('3456. 직사각형 길이 찾기.txt','r')

T = int(input())
for tc in range(T):
    F, S, T = map(int,input().split())
    if F == S == T:
        print('#{} {}'.format(tc+1,F))
    elif F == S:
        print('#{} {}'.format(tc+1,T))
    elif S == T:
        print('#{} {}'.format(tc+1,F))
    elif F == T:
        print('#{} {}'.format(tc+1,S))