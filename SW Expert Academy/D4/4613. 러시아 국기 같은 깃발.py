import sys
sys.stdin = open('4613. 러시아 국기 같은 깃발.txt','r')


def chk(n,change,color):
    global minimum
    if n == N:
        if change < minimum and color == 'red':
            minimum = change
            return
        else:
            return
    if color == 'white':
        chk(n+1,change+matrix_c[n][1]+matrix_c[n][2],'white')
        chk(n+1,change+matrix_c[n][0]+matrix_c[n][2],'blue')
    elif color == 'blue':
        chk(n+1,change+matrix_c[n][0]+matrix_c[n][2],'blue')
        chk(n+1,change+matrix_c[n][0]+matrix_c[n][1],'red')
    elif color == 'red':
        chk(n+1,change+matrix_c[n][0]+matrix_c[n][1],'red')

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    matrix_c = list()
    for i in range(N):
        colors = [0] * 3
        input_data = input()
        colors[0] += input_data.count('W')
        colors[1] += input_data.count('B')
        colors[2] += input_data.count('R')
        matrix_c.append(colors)
    change = 0
    minimum = 10000000
    chk(1,matrix_c[0][1]+matrix_c[0][2],'white')
    print('#{} {}'.format(tc+1,minimum))




    # print(matrix_c)
    # flag = 'red'
    # for i in range(N-1,-1,-1):
    #     if flag == 'red':
    #         if matrix_c[i][2] > matrix_c[i][1]:
    #             change += matrix_c[i][0] + matrix_c[i][1]
    #         else:
    #             change += matrix_c[i][0] + matrix_c[i][2]
    #             flag = 'blue'
    #     if flag == 'blue':
    #         if matrix_c[i][1] > matrix_c[i][0]:
    #             change += matrix_c[i][0] + matrix_c[i][2]
    #         else:
    #             change += matrix_c[i][1] + matrix_c[i][2]
    #             flag = 'white'
    #     if flag == 'white':
    #         change += matrix_c[i][1] + matrix_c[i][2]
    # print(change)
