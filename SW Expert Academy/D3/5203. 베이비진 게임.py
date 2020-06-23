import sys
sys.stdin = open('5203. 베이비진 게임.txt','r')
"""
draw 0
p1 1
p2 2
p1부터 시작

input이 6개(p1 3개 / p2 3개)이상일 때부터 baby-gin 점검
run : check 함수를 통해서 연속하는 3개의 값이 존재하는지 확인
triplet : count함수를 이용해서 숫자 3이 있는지 확인 
"""
def check(li):
    for i in range(1,9):
        if li[i-1]>=1 and li[i]>=1 and li[i+1]>=1:
            return True
    return False

T = int(input())
for tc in range(T):
    game = list(map(int,input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    for i in range(len(game)):
        if i&1:
            p2[game[i]] += 1
        else:
            p1[game[i]] += 1
        if i >= 5:
            if p2.count(3) or check(p2):
                print('#{} {}'.format(tc+1,2))
                break
            if p1.count(3) or check(p1):
                print('#{} {}'.format(tc + 1, 1))
                break
    else:
        print('#{} {}'.format(tc+1, 0))