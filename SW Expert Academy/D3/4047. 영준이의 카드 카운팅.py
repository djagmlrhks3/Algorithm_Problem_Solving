import sys
sys.stdin = open('4047. 영준이의 카드 카운팅.txt','r')
"""
카드무늬 S, D, H, C
01 ~ 13
"""
T = int(input())
for tc in range(T):
    input_data = input()
    cards = list()
    counts = [13]*4
    turn = ['S','D','H','C']
    for i in range(0,len(input_data)-2,3):
        card = input_data[i:i+3]
        cards.append(card)
    flag = True
    for i in cards:
        if cards.count(i) > 1:
            flag = False
            break
        else:
            counts[turn.index(i[0])] -= 1
    if flag:
        print('#{} {} {} {} {}'.format(tc+1,counts[0],counts[1],counts[2],counts[3]))
    else:
        print('#{} {}'.format(tc + 1,'ERROR'))