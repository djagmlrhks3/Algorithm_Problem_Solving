import sys
from itertools import combinations
from copy import deepcopy
sys.stdin = open('백준14502. 연구소.txt', 'r')

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
"""
0은 빈 칸, 1은 벽, 2는 바이러스
"""
def calculate(matrix):
    global N, M, answer
    cnt = 0
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 0:
                cnt += 1
    answer = max(answer, cnt)

def dfs(matrix):
    stack = deepcopy(viruses)
    while stack:
        vi = stack.pop()
        for idx in range(4):
            nr = vi[0] + d[idx][0]
            nc = vi[1] + d[idx][1]
            if 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 0:
                    matrix[nr][nc] = 2
                    stack.append((nr, nc))
    calculate(matrix)

def test(wall, matrix):
    for w in wall:
        matrix[w[0]][w[1]] = 1
    dfs(matrix)


N, M = map(int, sys.stdin.readline().split())

walls = []
viruses = []
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

for r in range(N):
    for c in range(M):
        if matrix[r][c] == 0:
            walls.append((r, c))
        elif matrix[r][c] == 2:
            viruses.append((r, c))

for wall in combinations(walls, 3):
    test(wall, deepcopy(matrix))
print(answer)

"""
DFS(재귀)를 사용한 코드
"""

# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
# N, M = map(int, input().split())
# matrix = []
# temp = [[0] * M for _ in range(N)]
#
# for _ in range(N):
#     matrix.append(list(map(int, input().split())))
#
# answer = 0
#
# def virus(r, c):
#     for idx in range(4):
#         nr = r + d[idx][0]
#         nc = c + d[idx][1]
#         if 0 <= nr < N and 0 <= nc < M:
#             if not temp[nr][nc]:
#                 temp[nr][nc] = 2
#                 virus(nr, nc)
#
# def calculate():
#     cnt = 0
#     for r in range(N):
#         for c in range(M):
#             if temp[r][c] == 0:
#                 cnt += 1
#     return cnt
#
#
#
# def dfs(count):
#     global answer
#     if count == 3:
#         for r in range(N):
#             for c in range(M):
#                 temp[r][c] = matrix[r][c]
#         for r in range(N):
#             for c in range(M):
#                 if temp[r][c] == 2:
#                     virus(r, c)
#         answer = max(answer, calculate())
#         return
#
#     for r in range(N):
#         for c in range(M):
#             if not matrix[r][c]:
#                 matrix[r][c] = 1
#                 count += 1
#                 dfs(count)
#                 matrix[r][c] = 0
#                 count -= 1
# dfs(0)
# print(answer)