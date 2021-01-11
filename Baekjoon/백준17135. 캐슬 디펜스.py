import sys
from copy import deepcopy
from itertools import combinations
from collections import deque
sys.stdin = open('백준17135. 캐슬 디펜스.txt', 'r')

def check(target):
    global inf
    res = []
    for t in target:
        if t not in res and t != [0, inf]:
            res.append(t)
    return len(res)

def move(rc, target):
    global N, M
    for _ in range(len(rc)):
        enemy = rc.popleft()
        if enemy in target: continue
        if enemy[0]+1 < N:
            enemy[0] += 1
            rc.append(enemy)
    return rc

def find(li, rc):
    global answer, N, D, inf
    kill = 0
    while len(rc):
        target = [[0, inf] for _ in range(3)]
        dist = [inf] * 3
        for _ in range(len(rc)):
            enemy = rc.popleft()
            for idx in range(3):
                distance = abs(enemy[0]-N) + abs(enemy[1]-li[idx])
                if distance < dist[idx] and distance <= D:
                    dist[idx] = distance
                    target[idx][0], target[idx][1] = enemy[0], enemy[1]
                elif distance == dist[idx] and enemy[1] < target[idx][1]:
                    target[idx][0], target[idx][1] = enemy[0], enemy[1]
            rc.append(enemy)
        rc = move(rc, target)
        kill += check(target)
    answer = max(answer, kill)

N, M, D = map(int, input().split())
rc = []
answer = 0
inf = 0xfffff
for r in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for c in range(M):
        if row[c]:
            rc.append([r, c])

rc = sorted(rc, key=lambda x:[-x[0], x[1]])
for li in combinations([i for i in range(M)], 3):
    find(li, deque(deepcopy(rc)))
print(answer)

# def NOE():
#     for i in range(n):
#         for j in range(m):
#             if Map[i][j] == 1:
#                 q.append((i, j))
#
#
# def Attack(q):
#     global k
#     target = [(0, Max), (0, Max), (0, Max)]
#     Dist = [Max, Max, Max]
#     while q:
#         x, y = q.popleft()
#         for i in range(3):
#             z = abs(n - x) + abs(S[i] - y)
#             if Dist[i] > z:
#                 Dist[i] = z
#                 target[i] = (x, y)
#             elif Dist[i] == z and y < target[i][1]:
#                 target[i] = (x, y)
#     for t, (x, y) in enumerate(target):
#         if Map[x][y] == 1:
#             if Dist[t] <= d:
#                 Map[x][y] = 0
#                 k += 1
#
#
# from itertools import combinations
# from copy import deepcopy
# from collections import deque
#
# Max = float('inf')
# n, m, d = map(int, input().split())
# D = [[*map(int, input().split())] for _ in range(n)]
# Castle = [i for i in range(m)]
# Archer = combinations(Castle, 3)
# ans = 0
# q = deque()
# for S in Archer:
#     Map = deepcopy(D)
#     k = 0
#     while 1:
#         NOE()
#         if len(q) == 0: break
#         Attack(q)
#         Map = [[0] * m] + Map[:n - 1]
#     ans = max(ans, k)
# print(ans)
