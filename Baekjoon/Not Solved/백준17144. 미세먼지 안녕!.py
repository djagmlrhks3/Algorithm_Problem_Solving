import sys
sys.stdin = open('백준17144. 미세먼지 안녕!.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dust():
    global R, C
    empty_matrix = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if matrix[i][j]:
                cnt = 0
                for z in range(4):
                    ni = i + dx[z]
                    nj = j + dy[z]
                    if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] != -1:
                        cnt += 1
                        empty_matrix[ni][nj] += int(matrix[i][j]/5)
                empty_matrix[i][j] += matrix[i][j] - int(matrix[i][j]/5) * cnt
    return empty_matrix



def blow(li):
    empty_matrix = [[0] * (C+2) for _ in range(R+2)]
    r1 = li[0]
    r2 = li[1]
    #r1오른쪽
    for i in range(1, C):
        if matrix[r1][i]:
            empty_matrix[r1+1][i+2] = matrix[r1][i]
    #r2오른쪽
    for i in range(1, C):
        if matrix[r2][i]:
            empty_matrix[r2+1][i+2] = matrix[r2][i]
    #r1왼쪽
    for i in range(C-1, 0, -1):
        if matrix[0][i]:
            empty_matrix[1][i] = matrix[0][i]
    #r2왼쪽
    for i in range(C-1, 0, -1):
        if matrix[R-1][i]:
            empty_matrix[R][i] = matrix[R-1][i]
    #r1위쪽
    for i in range(r2+1, 0, -1):
        if i-1 == 0:break
        else:
            empty_matrix[i-2][C] = matrix[i][C-1]
    #r2위쪽
    for i in range(r1+1, 0, -1):
        if matrix[i-1][0] == -1:break
        else:
            empty_matrix[i-2][1] = matrix[i][0]

    #r1아래쪽
    for i in range(r1-1, R):
        if matrix[i+1][0] == -1:break
        else:
            empty_matrix[i+2][1] = matrix[i][0]
    #r2아래쪽
    for i in range(r2-1, R):
        if i+1 == R:break
        else:
            empty_matrix[i+2][C] = matrix[i][C-1]
    for i in empty_matrix:
        print(i)
    return empty_matrix
R, C, T = map(int, input().split())

matrix = [list(map(int,input().split())) for _ in range(R)]
clear = []
for i in range(R):
    if matrix[i][0] == -1:
        clear = [i, i+1]
        break

for t in range(T):
    matrix = dust()
    matrix = blow(clear)
result = 0
for r in matrix:
    result += sum(r)
print(result+2)
# for i in matrix:
#     print(i)