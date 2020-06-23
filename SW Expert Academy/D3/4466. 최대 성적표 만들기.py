import sys
sys.stdin = open('4466. 최대 성적표 만들기.txt','r')

T = int(input())
for tc in range(T):
    N, K = map(int,input().split())
    scores = list(map(int,input().split()))
    scores.sort()

    result = sum(scores[-K:])
    print('#{} {}'.format(tc+1,result))
