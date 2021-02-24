import sys
from collections import deque
sys.stdin = open('백준2644. 촌수 계산.txt', 'r')

n = int(input())
man1, man2 = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]
parents = [0] + [i for i in range(1, n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

distance = [0] * (n+1)
queue = deque([man1])
distance[man1] = 0
while queue:
    node = queue.popleft()
    if node == man2: break
    for next in relation[node]:
        if not distance[next]:
            distance[next] = distance[node] + 1
            queue.append(next)
print(distance[man2]) if distance[man2] else print(-1)
