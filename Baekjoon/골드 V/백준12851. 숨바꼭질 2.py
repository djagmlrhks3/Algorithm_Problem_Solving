import sys
from collections import deque
sys.stdin = open('백준12851. 숨바꼭질 2.txt', 'r')

def bfs(n, k):
    global time, ways
    if n == k:
        return 0, 1
    if n > k:
        return n-k, 1

    visited, ways = [int(1e9)] * 100001, [0] * 100001

    queue = deque([n])
    visited[n], ways[n] = 0, 1

    flag = True
    time, cnt = 0, 0

    while queue and flag:
        for _ in range(len(queue)):
            l = queue.popleft()
            for temp in [l-1, l+1, l*2]:
                if 0 <= temp < 100001 and time+1 <= visited[temp]:
                    ways[temp] += 1
                    visited[temp] = time+1
                    if temp == k:
                        flag = False
                    if flag:
                        queue.append(temp)
        time += 1
    return visited[k], ways[k]

N, K = map(int, sys.stdin.readline().split())

time, cnt = bfs(N, K)
print(time)
print(cnt)