import sys
sys.stdin = open('5432. 쇠막대기 자르기.txt','r')

T = int(input())
for tc in range(T):
    stick = input()
    basic=list()
    empty = list()
    for i in range(len(stick)):
        if stick[i] == '(':
            if len(empty):
                empty.append(stick[i])
                basic.append(0)
            else:
                empty.append(stick[i])
                basic.append(1)
        else:
            if len(empty) and stick[i-1] == '(':
                basic.pop(-1)
                basic.append(3)
                empty.pop(-1)
            else :
                basic.append(2)
                empty.clear()
    result = 0
    for i in basic:
        if i == 1 or i == 0:
            empty.append(i)
        elif i == 2:
            empty.pop(-1)
            result += 1
        elif i == 3 and len(empty):
            result += len(empty)
    print('#{} {}'.format(tc+1,result))

