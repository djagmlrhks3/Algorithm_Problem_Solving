import sys
from collections import deque
sys.stdin = open('백준21756. 지우개.txt', 'r')

N = int(input())
queue = deque([i for i in range(1, N+1)])
while len(queue) > 1:
    for i in range(len(queue)):
        if not i%2:
            queue.popleft()
        else:
            queue.append(queue.popleft())
print(queue[0])
