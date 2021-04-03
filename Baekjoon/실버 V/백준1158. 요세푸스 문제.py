import sys
from collections import deque
sys.stdin = open('백준1158. 요세푸스 문제.txt', 'r')
N, K = map(int, input().split())
answer = []
queue = deque([i for i in range(1, N+1)])

while queue:
    queue.rotate(-K+1)
    answer.append(queue.popleft())
print('<'+', '.join(map(str, answer))+'>')