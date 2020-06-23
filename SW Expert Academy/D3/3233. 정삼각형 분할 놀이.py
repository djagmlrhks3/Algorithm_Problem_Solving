import sys
sys.stdin = open('3233. 정삼각형 분할 놀이.txt','r')

T = int(input())
for tc in range(T):
    A, B = map(int,input().split())
    result = 0
    for i in range(1,A//B+1):
        result += 2*i-1
    print('#{} {}'.format(tc+1,result))