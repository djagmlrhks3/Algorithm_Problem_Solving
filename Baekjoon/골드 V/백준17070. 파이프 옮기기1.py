import sys
sys.stdin = open('백준17070. 파이프 옮기기1.txt', 'r')

"""
가로 0
세로 1
대각선 2
"""
def move(dir, r, c):
    global N, answer
    if r == N-1 and c == N-1:
        answer += 1
        return
    if dir == 0 or dir == 2:      #가로
        if c+1 < N and not matrix[r][c+1]:
            move(0, r, c+1)
    if dir == 1 or dir == 2:   #세로
        if r+1 < N and not matrix[r+1][c]:
            move(1, r+1, c)
    if c+1 < N and r+1 < N:
        if matrix[r+1][c] + matrix[r][c+1] + matrix[r+1][c+1] == 0:
            move(2, r+1, c+1)

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
move(0, 0, 1)
print(answer)
