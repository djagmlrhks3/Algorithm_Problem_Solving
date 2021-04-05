import sys
from collections import deque
sys.stdin = open('백준14395. 4연산.txt', 'r')
s, t = map(int, input().split())
if s == t:
    print(0)
elif t == 0:
    print('-')
else:
    visited = [s**2, s*2, 1]
    candidates = []
    queue = deque([(s**2, '*'), (s*2, '+'), (1, '/')])
    while queue:
        num, order = queue.popleft()
        if num == t:
            candidates.append(order)
            continue
        if num > t:
            continue
        if num * num not in visited:
            queue.append((num ** 2, order + '*'))
            visited.append(num ** 2)
        if num + num not in visited:
            queue.append((num*2, order+'+'))
            visited.append(num*2)

    candidates.sort()
    print(candidates[0]) if candidates else print(-1)