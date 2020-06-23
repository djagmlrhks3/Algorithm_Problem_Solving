import sys
sys.stdin = open('3314. 보충학습과 평균.txt','r')

T = int(input())
for tc in range(T):
    scores = list(map(int,input().split()))
    for i in range(len(scores)):
        if scores[i] < 40:
            scores[i] = 40
    print('#{} {}'.format(tc+1,int(sum(scores)/5)))