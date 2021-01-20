import sys
from collections import deque
sys.stdin = open('백준18405. 경쟁적 전염.txt', 'r')

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread(candidates):
    global N
    for i in range(1, len(candidates)):
        for _ in range(len(candidates[i])):
            r, c = candidates[i].popleft()
            for idx in range(4):
                nr = r + d[idx][0]
                nc = c + d[idx][1]
                if 0 <= nr < N and 0 <= nc < N:
                    if not matrix[nr][nc]:
                        matrix[nr][nc] = i
                        candidates[i].append((nr, nc))

N, K = map(int, input().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

S, X, Y = map(int, sys.stdin.readline().split())

candidates = [deque([]) for _ in range(K+1)]


for r in range(N):
    for c in range(N):
        if matrix[r][c]:
            candidates[matrix[r][c]].append((r, c))
time = 0
while time < S:
    spread(candidates)
    time += 1

print(matrix[X-1][Y-1])

"""
시간초과 - 모든 바이러스 번호에 대해서 matrix를 탐색하는 과정을 거쳤기 때문!

import sys

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread(n):
    global N
    virus = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == n:
                virus.append((i, j))

    while virus:
        r, c = virus.pop()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < N and 0 <= nc < N:
                if not matrix[nr][nc]:
                    matrix[nr][nc] = n

N, K = map(int, input().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

S, X, Y = map(int, sys.stdin.readline().split())

time = 0

while time < S:
    for i in range(1, K+1):
        spread(i)
    time += 1

print(matrix[X-1][Y-1])
"""