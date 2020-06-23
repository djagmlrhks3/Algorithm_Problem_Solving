import sys
sys.stdin = open('1873. 상호의 배틀필드.txt','r')
"""

문자	의미
.	평지(전차가 들어갈 수 있다.)   0   
*	벽돌로 만들어진 벽            1
#	강철로 만들어진 벽            2
-	물(전차는 들어갈 수 없다.)    3
^	위쪽을 바라보는 전차(아래는 평지이다.)     4
v	아래쪽을 바라보는 전차(아래는 평지이다.)   5
<	왼쪽을 바라보는 전차(아래는 평지이다.)     6
>	오른쪽을 바라보는 전차(아래는 평지이다.)   7
다음 표는 사용자가 넣을 수 있는 입력의 종류를 나타낸다.
 
문자	동작

"""
setting = [0,'.',1,'*',2,'#',3,'-',4,'^',5,'v',6,'<',7,'>']

T = int(input())
for tc in range(T):
    H, W = map(int,input().split())
    matrix = [ [0] * W for _ in range(H) ]
    for h in range(H):
        input_data = input()
        for i in range(len(input_data)):
            matrix[h][i] = setting[setting.index(input_data[i])-1]
            if matrix[h][i] >= 4:
                juncha_i = h
                juncha_j = i
    N = int(input())
    play = input()
    for p in play:
        if p == 'U':
            matrix[juncha_i][juncha_j] = 4
            if 0 <= juncha_i - 1 and matrix[juncha_i - 1][juncha_j] == 0:
                matrix[juncha_i - 1][juncha_j] = 4
                matrix[juncha_i][juncha_j] = 0
                juncha_i -= 1
        elif p == 'D':
            matrix[juncha_i][juncha_j] = 5
            if juncha_i + 1 <= H - 1 and matrix[juncha_i + 1][juncha_j] == 0:
                matrix[juncha_i + 1][juncha_j] = 5
                matrix[juncha_i][juncha_j] = 0
                juncha_i += 1
        elif p == 'L':
            matrix[juncha_i][juncha_j] = 6
            if 0 <= juncha_j - 1 and matrix[juncha_i][juncha_j - 1] == 0:
                matrix[juncha_i][juncha_j - 1] = 6
                matrix[juncha_i][juncha_j] = 0
                juncha_j -= 1
        elif p == 'R':
            matrix[juncha_i][juncha_j] = 7
            if juncha_j + 1 <= W - 1 and matrix[juncha_i][juncha_j + 1] == 0:
                matrix[juncha_i][juncha_j + 1] = 7
                matrix[juncha_i][juncha_j] = 0
                juncha_j += 1
        elif p == 'S':
            x , y = juncha_i, juncha_j
            if matrix[juncha_i][juncha_j] == 4:
                for i in range(H):
                    x -= 1
                    if 0 <= x and matrix[x][y] == 1:
                        matrix[x][y] = 0
                        break
                    elif 0<= x and matrix[x][y] == 2:
                        break
                    elif 0<= x:
                        continue
                    else:
                        continue
            elif matrix[juncha_i][juncha_j] == 5:
                for i in range(H):
                    x += 1
                    if x <= H-1 and matrix[x][y] == 1:
                        matrix[x][y] = 0
                        break
                    elif x <= H-1 and matrix[x][y] == 2:
                        break
                    elif x <= H-1:
                        continue
                    else:
                        break
            elif matrix[juncha_i][juncha_j] == 6:
                for i in range(H):
                    y -= 1
                    if 0 <= y and matrix[x][y] == 1:
                        matrix[x][y] = 0
                        break
                    elif 0 <= y and matrix[x][y] == 2:
                        break
                    elif 0 <= y:
                        continue
                    else:
                        break
            elif matrix[juncha_i][juncha_j] == 7:
                for i in range(H):
                    y += 1
                    if y <= W-1 and matrix[x][y] == 1:
                        matrix[x][y] = 0
                        break
                    elif y <= W-1 and matrix[x][y] == 2:
                        break
                    elif y <= W-1:
                        continue
                    else:
                        break
    print('#{}'.format(tc+1),end=" ")
    for i in matrix:
        for j in i:
            print(setting[setting.index(j)+1],end="")
        print()
"""
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
"""
