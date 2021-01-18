import sys
from copy import deepcopy
sys.stdin = open('백준19236. 청소년 상어.txt', 'r')

dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
tank = []
answer = 0

def move_fish(copy_tank, num, shark_r, shark_c):
    for r in range(4):
        for c in range(4):
            if copy_tank[r][c][0] == num:
                while True:
                    nr = r + dir[copy_tank[r][c][1]][0]
                    nc = c + dir[copy_tank[r][c][1]][1]
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        if not(nr == shark_r and nc == shark_c):
                            copy_tank[r][c], copy_tank[nr][nc] = copy_tank[nr][nc], copy_tank[r][c]
                            return
                    copy_tank[r][c][1] = (copy_tank[r][c][1]+1) % 8

def recursive(tank, shark_r, shark_c, eat):
    global answer
    copy_tank = deepcopy(tank)
    eat += copy_tank[shark_r][shark_c][0]
    copy_tank[shark_r][shark_c][0] = 0
    for num in range(1, 17):
        move_fish(copy_tank, num, shark_r, shark_c)

    if answer < eat:
        answer = max(answer, eat)

    for m in range(1, 4):
        n_shark_r = shark_r + (dir[copy_tank[shark_r][shark_c][1]][0] * m)
        n_shark_c = shark_c + (dir[copy_tank[shark_r][shark_c][1]][1] * m)
        if 0 <= n_shark_r < 4 and 0 <= n_shark_c < 4 and copy_tank[n_shark_r][n_shark_c][0]:
            recursive(copy_tank, n_shark_r, n_shark_c, eat)

for r in range(4):
    n1, d1, n2, d2, n3, d3, n4, d4 = map(int, input().split())
    before = [[n1, d1-1], [n2, d2-1], [n3, d3-1], [n4, d4-1]]
    tank.append(before)

recursive(tank, 0, 0, 0)
print(answer)