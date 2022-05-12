import sys
from collections import deque
sys.stdin = open('백준14567. 선수과목 (Prerequisite).txt', 'r')

def topological_sort():
    global N
    queue = deque()
    for i in range(N):
        if not indegree[i]:
            queue.append(i)
            res[i] = 1
    while queue:
        now = queue.popleft()
        for n in turn[now]:
            indegree[n] -= 1
            if not indegree[n]:
                res[n] = res[now] + 1
                queue.append(n)

N, M = map(int, input().split())
indegree = [0] * N
turn = [[] for _ in range(N)]
res = [0] * N
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    turn[s-1].append(e-1)
    indegree[e-1] += 1

topological_sort()
print(' '.join(map(str, res)))