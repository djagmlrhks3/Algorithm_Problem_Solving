import sys
from collections import deque
sys.stdin = open('백준15558. 점프 게임.txt', 'r')
N, k = map(int, input().split())
lines = [sys.stdin.readline().rstrip() for _ in range(2)]
queue = deque([(0, 0)])
visited = [[0]*N for _ in range(2)]
time = -1
flag = False
while queue:
    for _ in range(len(queue)):
        d, idx = queue.popleft()
        if idx+1 >= N or idx+k >= N:
            flag = True
            break
        if int(lines[d][idx+1]) and not visited[d][idx+1]:
            queue.append((d, idx+1))
            visited[d][idx+1] = 1
        if idx-1 > time+1 and int(lines[d][idx-1]) and not visited[d][idx-1]:
            queue.append((d, idx-1))
            visited[d][idx-1] = 1
        if int(lines[(d+1)%2][idx+k]) and not visited[0][idx+k]:
            queue.append(((d+1)%2, idx+k))
            visited[(d+1)%2][idx+k] = 1
    time += 1
print(1) if flag else print(0)