import sys
sys.stdin = open('1233. 사칙연산 유효성 검사.txt','r')
for tc in range(10):
    N = int(input())
    basic = list()
    flag = True
    for n in range(N):
        basic.append(input().split())
    for i in range(N-1,-1,-1):
        if len(basic[i]) > 2 and basic[i][1].isnumeric():
            flag = False
            break
        elif len(basic[i]) == 2 and not basic[i][1].isnumeric():
            flag = False
            break
    result = 1 if flag else 0
    print('#{} {}'.format(tc+1,result))