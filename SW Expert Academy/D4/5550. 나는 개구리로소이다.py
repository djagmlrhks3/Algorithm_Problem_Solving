import sys
sys.stdin = open('5550. 나는 개구리로소이다.txt','r')
"""
croak
"""
T = int(input())
for tc in range(T):
    frogs = list()
    count = 0
    life = 0
    unit = ['c','r','o','a','k'] #개구리가 몇 마리 있는지 확인하기 위해
    input_data = input()
    """
    입력받은 데이터에대해 문자하나씩 추출하여
    'croak'순서가 되도록 코딩
    """
    for i in input_data:
        flag = False
        if i == 'c':
            frogs.append(['c'])
            count += 1             #'c'는 울음소리의 첫 번째 이므로 새로운 개구리 탄생을 의미 +1
            if life >= 1:
                count -= 1         #만약 이전에 생성이 완료 된 개구리가 있으면 그 녀석을 사용하면 되니까 -= 1
                life -= 1
        elif i == 'r':
            for i in frogs:
                if i[-1] == 'c':
                    i.append('r')
                    flag = True
                    break
            if not flag:
                break
        elif i == 'o':
            for i in frogs:
                if i[-1] == 'r':
                    i.append('o')
                    flag = True
                    break
            if not flag:
                break
        elif i == 'a':
            for i in frogs:
                if i[-1] == 'o':
                    i.append('a')
                    flag = True
                    break
            if not flag:
                break
        elif i == 'k':
            for i in frogs:
                if i[-1] == 'a':
                    i.append('k')
                    life += 1
                    flag = True
                    break
            if not flag:
                break
    if len(frogs) - frogs.count(unit) or not flag:
        print('#{} {}'.format(tc+1,-1))
    else:
        print('#{} {}'.format(tc+1,count))
