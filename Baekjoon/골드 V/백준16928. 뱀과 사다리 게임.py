import sys
from collections import deque
sys.stdin = open('백준16928. 뱀과 사다리 게임.txt', 'r')

visited, maps = [0] * 101, [0] * 101
visited[1] = 1
N, M = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]
for _ in range(N):
    s, e = map(int, input().split())
    maps[s] = e
for _ in range(M):
    s, e = map(int, input().split())
    maps[s] = e

queue = deque([1])
while queue:
    now = queue.popleft()
    for d in dice:
        next = now + d
        if next > 100: continue
        if not visited[next]:
            if maps[next]:
                next2 = maps[next]
                if not visited[next2]:
                    visited[next] = visited[now]+1
                    visited[next2] = visited[now]+1
                    queue.append(next2)
            else:
                visited[next] = visited[now]+1
                queue.append(next)
        if queue[-1] == 100:
            queue.clear()
            print(visited[now])