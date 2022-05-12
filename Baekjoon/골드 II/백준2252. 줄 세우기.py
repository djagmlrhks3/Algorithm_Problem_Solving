import sys
from collections import deque
sys.stdin = open('백준2252. 줄 세우기.txt', 'r')

def topological_sort():
    res = []
    queue = deque()
    for i  in range(1, N+1):
        if not indegree[i]:
            queue.append(i)
    while queue:
        now = queue.popleft()
        res.append(now)
        for n in turn[now]:
            indegree[n] -= 1
            if not indegree[n]:
                queue.append(n)
    return ' '.join(map(str, res))

N, M = map(int, input().split())
indegree = [0] * (N+1)
turn = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    turn[s].append(e)
    indegree[e] += 1
print(topological_sort())