import sys
from collections import deque
sys.stdin = open('백준2163. 초콜릿 자르기.txt', 'r')

N, M = map(int, input().split())
queue = deque([(N, M)])
if N == 1 and M == 1:
    print(1)
else:
    answer = 0
    while queue:
        r, c = queue.popleft()
        if r == 1 and c == 1: continue
        r, c = max(r, c), min(r, c)
        if r % 2:
            queue.append((r // 2, c))
            queue.append(((r // 2) + 1, c))
        else:
            queue.append((r // 2, c))
            queue.append((r // 2, c))
        answer += 1
    print(answer)