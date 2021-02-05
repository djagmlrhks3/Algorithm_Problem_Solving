import sys
sys.stdin = open('백준14499. 주사위 굴리기.txt', 'r')

dice_n = [0] * 7
# 동서북남
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def move(r, c):
    global directions
    for dir in directions:
        nr = r + d[dir-1][0]
        nc = c + d[dir-1][1]
        if 0 <= nr < N and 0 <= nc < M:
            if dir == 1: # 동
                dice_n[1], dice_n[4], dice_n[6], dice_n[3] = dice_n[3], dice_n[1], dice_n[4], dice_n[6]
            elif dir == 2: # 서
                dice_n[1], dice_n[4], dice_n[6], dice_n[3] = dice_n[4], dice_n[6], dice_n[3], dice_n[1]
            elif dir == 3: # 북
                dice_n[1], dice_n[2], dice_n[5], dice_n[6] = dice_n[5], dice_n[1], dice_n[6], dice_n[2]
            else: # 남
                dice_n[1], dice_n[2], dice_n[5], dice_n[6] = dice_n[2], dice_n[6], dice_n[1], dice_n[5]
            print(dice_n[1])
            if matrix[nr][nc]: # 지도의 숫자가 0이 아닌 경우
                dice_n[6] = matrix[nr][nc]
                matrix[nr][nc] = 0
            else:              # 지도의 숫자가 0인 경우
                matrix[nr][nc] = dice_n[6]
            r, c = nr, nc

N, M, x, y, K = map(int, input().split())
matrix = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    matrix.append(line)
directions = list(map(int, sys.stdin.readline().split()))

move(x, y)