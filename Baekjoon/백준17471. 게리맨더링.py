import sys
from itertools import combinations
from collections import deque
sys.stdin = open('백준17471. 게리맨더링.txt', 'r')

def calculate(li, res):
    global answer
    groupA, groupB = 0, 0
    for p in li:
        groupA += people[p]
    for p in res:
        groupB += people[p]
    answer = min(answer, abs(groupA-groupB))

def bfs(li):
    global N
    queue = deque([li[0]])
    visited = [li[0]]
    while queue:
        start = queue.pop()
        for next in relationship[start]:
            if next not in li: continue
            if next not in visited:
                queue.append(next)
                visited.append(next)
    if set(visited) & set(li) == set(li):
        return True
    else:
        return False

def check(li):
    global N
    res = list(set(i for i in range(N)) - set(li))
    if len(li) == 1:
        if bfs(res):
            calculate(li, res)
    else:
        if bfs(li) and bfs(res):
            calculate(li, res)

N = int(input())
people = list(map(int, sys.stdin.readline().split()))
answer = 1000
relationship = {i:[] for i in range(N)}

for idx in range(N):
    S, *args = map(int, sys.stdin.readline().split())
    for E in args:
        relationship[idx].append(E-1)

for k in range(1, N//2+1):
    for i in combinations([i for i in range(N)], k):
        check(i)

print(answer if answer < 1000 else -1)