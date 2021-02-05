import sys
from itertools import combinations
from copy import deepcopy
sys.stdin = open('백준18428. 감시 피하기.txt', 'r')

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def check(r, c, dir, classroom):
    global N
    for n in range(1, N): # 최대 N-1까지의 시야를 가질 수 있다. (가중치 부여)
        nr = r + (d[dir][0] * n)
        nc = c + (d[dir][1] * n)
        if 0 <= nr < N and 0 <= nc < N:
            if classroom[nr][nc] == "S":
                return False
            if classroom[nr][nc] == "O":
                return True
        else:
            break
    return True

def make_wall(li, classroom):
    for w in li:
        r, c = w
        classroom[r][c] = 'O'
    for t in teachers: # 모든 선생님들에 대해서
        for i in range(4): # 4방향을 탐색
            if not check(t[0], t[1], i, classroom):
                return False
    return True

N = int(input())
classroom = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
candidates = []
teachers = []

for r in range(N):
    for c in range(N):
        if classroom[r][c] == 'X':
            candidates.append((r, c))
            classroom[r][c] = ''
        elif classroom[r][c] == 'T':
            teachers.append((r, c))

for li in combinations(candidates, 3):
    if make_wall(li, deepcopy(classroom)):
        print("YES")
        break
else:
    print("NO")