import sys
sys.stdin = open('6109. 추억의 2048게임.txt','r')

T = int(input())
for tc in range(T):
    N, S = input().split()
    N = int(N)
    basic = list()
    for i in range(N):
        basic.append(list(map(int,input().split())))
    for j in range(N):
        stack = list()
        for i in range(N):
            now = basic[i][j]
            if not now:
                stack.append(i)
            else:
                flag = True
                while flag:
                    for z in range(i+1,N):
                        if now == basic[z][j]:
                            basic[i][j] *= 2
                            basic[z][j] = 0
                            flag = False
                            break
                        elif basic[z][j] and now != basic[z][j]:
                            flag = False
                            break
                        elif basic[z][j] == 0:
                            continue
                    else:
                        flag = False
                        break


    for i in basic:
        print(i)
    # print(stack)