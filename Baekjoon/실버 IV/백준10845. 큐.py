import sys
from collections import deque
sys.stdin = open('백준10845. 큐.txt', 'r')

def pick(order, idx):
    if queue:
        if order == 'print':
            print(queue[idx])
        else:
            print(queue.popleft())
    else:
        print(-1)

N = int(input())
queue = deque([])
for _ in range(N):
    order, *num = sys.stdin.readline().split()
    if order == 'push':
        queue.append(num[0])
    elif order == 'front':
        pick('print', 0)
    elif order == 'back':
        pick('print', -1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(0) if queue else print(1)
    elif order == 'pop':
        pick('pop', 0)