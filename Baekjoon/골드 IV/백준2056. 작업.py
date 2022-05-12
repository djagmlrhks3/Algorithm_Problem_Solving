import sys
from collections import deque
sys.stdin = open('백준2056. 작업.txt', 'r')

def topological_sort():
    global N
    DP = time[:]
    queue = deque()
    for i in range(1, N+1):
        if not indegree[i]:
            queue.append(i)
    while queue:
        now = queue.popleft()
        for n in graph[now]:
            indegree[n] -= 1
            DP[n] = max(DP[n], time[n]+DP[now])
            if not indegree[n]:
                queue.append(n)
    return max(DP)

N = int(input())
indegree = [0] * (N+1)
time = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    t, c, *li = map(int, input().split())
    for n in li:
        graph[n].append(i)
    indegree[i] += c
    time[i] = t
print(topological_sort())