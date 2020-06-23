import sys
sys.stdin=open('4615. 재미있는 오셀로 게임.txt','r')
"""
2는 흰색
1은 검은색
"""
T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    matrix = [ [0]*(N) for _ in range(N) ]
    matrix[(N//2)-1][(N//2)-1] = 2
    matrix[(N//2)-1][(N//2)] = 1
    matrix[(N//2)][(N//2)] = 2
    matrix[(N//2)][(N//2)-1] = 1
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    for m in range(M):
        y, x, c = map(int,input().split())
        matrix[x-1][y-1] = c
        for i in range(8):
            nx = x - 1 + dx[i]
            ny = y - 1 + dy[i]
            stack = list()
            flag = False
            for j in range(N):
                if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and matrix[nx][ny] != c and matrix[nx][ny] != 0:
                    stack.append((nx,ny))
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and matrix[nx][ny] == 0:
                        break
                    elif 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and matrix[nx][ny] == c:
                        flag = True
                        break
            if flag:
                for z in stack:
                    matrix[z[0]][z[1]] = c
    black = 0
    for i in matrix:
        black += i.count(1)
    print('#{} {} {}'.format(tc+1,black,16-black))
T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    matrix = [ [0]*(N) for _ in range(N) ]
    matrix[(N//2)-1][(N//2)-1] = 2
    matrix[(N//2)-1][(N//2)] = 1
    matrix[(N//2)][(N//2)] = 2
    matrix[(N//2)][(N//2)-1] = 1
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    for m in range(M):
        y, x, c = map(int,input().split())
        matrix[x-1][y-1] = c
        for i in range(8):
            nx = x - 1 + dx[i]
            ny = y - 1 + dy[i]
            stack = list()
            flag = False
            for j in range(N):
                if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and matrix[nx][ny] != c and matrix[nx][ny] != 0:
                    stack.append((nx,ny))
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and matrix[nx][ny] == c:
                        flag = True
                        break
            if flag:
                for z in stack:
                    matrix[z[0]][z[1]] = c
    black = 0
    white = 0
    for i in matrix:
        black += i.count(1)
        white += i.count(2)
    print('#{} {} {}'.format(tc+1,black,white))