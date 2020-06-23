import sys
sys.stdin = open("4861. 회문.txt","r")

T = int(input())
for tc in range(T):
    #글자판 길이 : N / 찾고자하는 회문길이 : M
    N, M = map(int,input().split())
    matrix = list()
    for i in range(N):
        matrix.append(input())

    for i in matrix:
        for j in range(N-M+1):
            empty = ''
            for z in range(j,j+M):
                empty += i[z]
            if empty == empty[::-1]:
                print('#{} {}'.format(tc+1,empty))

    for i in range(N):
        for j in range(N-M+1):
            empty = ''
            for z in range(j,j+M):
                empty += matrix[z][i]
            if empty == empty[::-1]:
                print('#{} {}'.format(tc+1,empty))


