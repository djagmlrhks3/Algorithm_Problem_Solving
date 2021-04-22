import sys
from collections import deque
sys.stdin = open('백준2637. 장난감조립.txt', 'r')

def topological_sort():
    queue = deque()
    for i in range(1, N+1):
        if not indegree[i]:
            queue.append(i)
            check[i][i] = 1
    while queue:
        now = queue.popleft()
        for n, c in graph[now]:
            indegree[n] -= 1
            for key in check[n].keys():
                check[n][key] += (check[now][key] * c)
            if not indegree[n]:
                queue.append(n)
    return check[n]

N = int(input())
M = int(input())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    e, s, c = map(int, sys.stdin.readline().split())
    indegree[e] += 1
    graph[s].append((e, c))

cnt = dict()
first = []
for i in range(1, N+1):
    if not indegree[i]:
        first.append(i)
check = [{t:0 for t in first} for i in range(N+1)]

for key, value in topological_sort().items():
    print(key, value)