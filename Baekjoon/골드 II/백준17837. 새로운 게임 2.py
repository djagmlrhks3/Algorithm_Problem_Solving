import sys
sys.stdin = open('백준17837. 새로운 게임 2.txt', 'r')
dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
N, K = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def is_finish(nr, nc):
    if len(location[nr][nc]) >= 4:
        print(answer)
        exit()

def white_red(r, c, nr, nc, num, color):
    for idx in range(len(location[r][c])):
        if location[r][c][idx] == num:
            if color == "white": location[nr][nc] += location[r][c][idx:]
            else: location[nr][nc] += location[r][c][idx:][::-1]
            location[r][c] = location[r][c][:idx]
            break
    is_finish(nr, nc) # 4개의 말이 쌓였는지 확인
    for horse in location[nr][nc]:
        horses[horse][0], horses[horse][1] = nr, nc

def blue(r, c, d, num):
    if d % 2: d += 1
    else: d -= 1
    horses[num][2] = d
    nr = r + dir[d][0]
    nc = c + dir[d][1]
    if 0 <= nr < N and 0 <= nc < N:
        if not matrix[nr][nc]: white_red(r, c, nr, nc, num, "white") # 흰색
        elif matrix[nr][nc] == 1: white_red(r, c, nr, nc, num, "red") # 빨간색

def solve(num):
    r, c, d = horses[num]
    nr = r + dir[d][0]
    nc = c + dir[d][1]
    if 0 <= nr < N and 0 <= nc < N:
        if not matrix[nr][nc]: # 흰색
            white_red(r, c, nr, nc, num, "white")
        elif matrix[nr][nc] == 1: # 빨간색
            white_red(r, c, nr, nc, num, "red")
        else: # 파란색
            blue(r, c, d, num)
    else:
        blue(r, c, d, num)

location = [[[] for _ in range(N)] for _ in range(N)]
horses = dict()
for idx in range(K):
    r, c, d = map(int, input().split())
    location[r-1][c-1].append(idx)
    horses[idx] = [r-1, c-1, d]

answer = 1
while answer < 1000:
    for num in range(K):
        solve(num)
    answer += 1
print(-1)


