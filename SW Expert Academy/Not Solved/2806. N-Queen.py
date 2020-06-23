import sys
sys.stdin = open('2806. N-Queen.txt','r')

def chk(n,i,y):
    global count
    if n == N:
        count += 1
        return
    else:
        for j in range(y,N):
            if not matrix[n][j]:
                chk(n,i,j+1)
                matrix[n][j] = 1
                for z in range(8):
                    ni = i + dx[z]
                    nj = j + dy[z]
                    for l in range(N):
                        if 0 <= ni <= N-1 and 0 <= nj <= N-1 :
                            matrix[ni][nj] = 1
                            ni += dx[z]
                            nj += dy[z]
                        else:
                            break
                chk(n+1,i+1,0)
        else:
            return

dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,-1,1,1,-1]
T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    count = 0
    for j in range(N):
        matrix[0][j] = 1
        for n in range(8):
            ni = dx[n]
            nj = j + dy[n]
            for z in range(N):
                if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:
                    matrix[ni][nj] = 1
                    ni += dx[n]
                    nj += dy[n]
        chk(1,1,0)

    print('#{} {}'.format(tc+1,count))


