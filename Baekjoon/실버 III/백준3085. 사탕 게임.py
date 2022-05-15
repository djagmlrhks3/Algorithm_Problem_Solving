import sys
sys.stdin = open('백준3085. 사탕 게임.txt', 'r')
N = int(input())
d = [(0, 1), (1, 0)]
board = [list(''.join(sys.stdin.readline().rstrip())) for _ in range(N)]

def count(r, c):
    global answer
    cnt = 1
    for i in range(N-1):
        if board[r][i] == board[r][i+1]:
            cnt += 1
            answer = max(answer, cnt)
        else:
            cnt = 1
    cnt = 1
    for i in range(N-1):
        if board[i][c] == board[i+1][c]:
            cnt += 1
            answer = max(answer, cnt)
        else:
            cnt = 1

answer = 1
for r in range(N):
    for c in range(N):
        count(r, c)
        nr, nc = r+1, c+1
        if nr < N and board[r][c] != board[nr][c]:
            board[r][c], board[nr][c] = board[nr][c], board[r][c]
            count(nr, c)
            count(r, c)
            board[r][c], board[nr][c] = board[nr][c], board[r][c]
        if nc < N and board[r][c] != board[r][nc]:
            board[r][c], board[r][nc] = board[r][nc], board[r][c]
            count(r, nc)
            count(r, c)
            board[r][c], board[r][nc] = board[r][nc], board[r][c]
print(answer)