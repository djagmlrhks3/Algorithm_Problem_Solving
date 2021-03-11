import sys
from collections import deque
sys.stdin = open('백준1449. 수리공 항승.txt', 'r')

N, L = map(int, input().split())
leak = list(map(int, sys.stdin.readline().split()))
leak.sort()
queue = deque(leak)
answer = 0
while queue:
    start = queue.popleft() - 0.5
    end = start + L
    answer += 1
    while queue and queue[0] + 0.5 <= end:
        queue.popleft()
print(answer)
