import sys
from collections import deque
sys.stdin = open('백준18352. 특정 거리의 도시 찾기.txt', 'r')

N, M, K, X = map(int, sys.stdin.readline().split())

connect = {i:[] for i in range(1, N+1)}

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    connect[start].append(end)

queue = deque([X])

visited = [-1] * (N+1)
visited[X] = 0

while queue:
    start = queue.popleft()
    for node in connect[start]:
        if visited[node] == -1:
            visited[node] = visited[start] + 1
            queue.append(node)

if visited.count(K):
    for idx in range(len(visited)):
        if visited[idx] == K:
            print(idx)
else:
    print(-1)