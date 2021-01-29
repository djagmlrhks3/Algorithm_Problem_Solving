import sys
sys.stdin = open('백준5014. 스타트링크.txt', 'r')
from collections import deque

F, S, G, U, D = map(int, input().split())
check = [int(1e9)] * (F+1)
check[S] = 0
queue = deque([S])

while queue:
    now = queue.popleft()
    if 0 < now+U <= F and check[now+U] == int(1e9):
        check[now+U] = check[now]+1
        queue.append(now+U)
    if  0 < now-D <= F and check[now-D] == int(1e9):
        check[now-D] = check[now]+1
        queue.append(now-D)
    if G in queue:
        break
print("use the stairs") if check[G] == int(1e9) else print(check[G])

