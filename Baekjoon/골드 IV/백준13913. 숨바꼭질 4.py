import sys
from collections import deque
sys.stdin = open('백준13913. 숨바꼭질 4.txt', 'r')

N, K = map(int, input().split())
queue = deque([(N, str(N))])
visited = [0] * 100001
visited[N] = 1

while queue:
    x, h = queue.popleft()
    if x == K:
        res = h.split(',')
        print(len(res)-1)
        print(' '.join(map(str, res)))
        break
    # x-1
    if x-1 >= 0 and not visited[x-1]:
        queue.append((x-1, h + ',' + str(x-1)))
        visited[x-1] = 1
    # x+1
    if x+1 < 100001 and not visited[x+1]:
        queue.append((x+1, h + ',' + str(x+1)))
        visited[x+1] = 1
    # x*2
    if x*2 < 100001 and not visited[x*2]:
        queue.append((x*2, h + ',' + str(x*2)))
        visited[x*2] = 1