import sys
from collections import deque
sys.stdin = open('백준1516. 게임 개발.txt', 'r')

def topological_sort():
    queue = deque()
    for i in range(1, N+1):
        if not indegree[i]:
            queue.append(i)
            DP[i] = time[i]
    while queue:
        now = queue.popleft()
        for n in turn[now]:
            indegree[n] -= 1
            DP[n] = max(DP[n], time[n] + DP[now])
            if not indegree[n]:
                queue.append(n)

    return DP[1:]
N = int(input())
indegree = [0] * (N+1)
turn = [[] for _ in range(N+1)]
time = [0]
DP = [0] * (N+1)
for i in range(1, N+1):
    t, *li = map(int, sys.stdin.readline().split())
    time.append(t)
    for s in li[:-1]:
        turn[s].append(i)
        indegree[i] += 1

for ans in topological_sort():
    print(ans)