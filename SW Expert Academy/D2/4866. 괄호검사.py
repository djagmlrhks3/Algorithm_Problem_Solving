import sys
sys.stdin = open('4866. 괄호 검사.txt','r')

T = int(input())
for tc in range(T):
    input_data = input()
    n = len(input_data)
    chk_list_left = ['(','{']
    chk_list_right = [')','}']

    chk = list()
    NOK_flag = False

    for i in input_data:
        if i in chk_list_left:
            chk.append(i)
        if i in chk_list_right:
            if len(chk) != 0:
                if chk_list_left.index(chk[-1]) == chk_list_right.index(i):
                    chk.pop(-1)
                else:
                    NOK_flag = True
                    break
            else:
                NOK_flag = True

    print('#{} {}'.format(tc + 1, 1 if not NOK_flag and len(chk) == 0 else 0))