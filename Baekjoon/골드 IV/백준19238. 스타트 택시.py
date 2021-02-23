import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('백준19238. 스타트 택시.txt', 'r')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def pick(distance):
    man = -1
    now = int(1e9)
    for idx in range(M):
        if not done[idx]:
            r, c = customer[idx][0], customer[idx][1]
            if distance[r][c] < now:
                now = distance[r][c]
                man = idx
            elif distance[r][c] == now:
                if r < customer[man][0]:
                    man = idx
                elif r == customer[man][0]:
                    if c < customer[man][1]:
                        man = idx
    return man

def bfs(tr, tc):
    queue = deque([(tr, tc)])
    distance = deepcopy(origin)
    distance[tr][tc] = 1
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < N and 0 <= nc < N:
                if not distance[nr][nc]:
                    queue.append((nr, nc))
                    distance[nr][nc] = distance[r][c] + 1
    return distance

N, M, fuel = map(int, input().split())
origin = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
customer = []
tr, tc = map(int, input().split())
tr -= 1; tc -= 1

for _ in range(M):
    sr, sc, er, ec = map(int, input().split())
    customer.append((sr-1, sc-1, er-1, ec-1))

done = [False] * M
while done.count(True) < M:
    distance = bfs(tr, tc)
    man = pick(distance)
    dist_man = distance[customer[man][0]][customer[man][1]]
    if not dist_man or fuel < dist_man - 1:
        fuel = -1
        break
    fuel -= (dist_man - 1)

    distance = bfs(customer[man][0], customer[man][1])
    dist_goal = distance[customer[man][2]][customer[man][3]]
    if not dist_goal or fuel < dist_goal - 1:
        fuel = -1
        break
    fuel += dist_goal - 1

    done[man] = True
    tr, tc = customer[man][2], customer[man][3]
print(fuel)

