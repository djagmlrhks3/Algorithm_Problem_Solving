import sys
from collections import deque
sys.stdin = open('백준1005. ACM Craft.txt', 'r')

def topological_sort():
    global N, W
    DP = time[:]
    queue = deque()
    for i in range(1, N+1):
        if not indegree[i]:
            queue.append(i)
    while queue:
        for _ in range(len(queue)):
            now = queue.popleft()
            for n in graph[now]:
                indegree[n] -= 1
                DP[n] = max(DP[n], DP[now] + time[n])
                if not indegree[n]:
                    queue.append(n)
    return DP[W]

for _ in range(int(input())):
    N, K = map(int, input().split())
    indegree = [0] * (N+1)

    graph = [[] for _ in range(N+1)]
    time = [0] + list(map(int, sys.stdin.readline().split()))
    for _ in range(K):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        indegree[e] += 1
    W = int(input())
    print(topological_sort())