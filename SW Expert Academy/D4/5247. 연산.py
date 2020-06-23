import sys
sys.stdin = open('5247. 연산.txt', 'r')
"""
+1, -1, *2, -10
"""
from collections import deque
def solution(num):
    global result, M
    queue = deque([(num, 0)])
    visited = [0]*1000001
    visited[num] = 1
    flag = True
    while queue:
        now = queue.popleft()
        number = now[0]
        count = now[1]
        if number+1 <= 1000000 and not visited[number+1]: # +1
            if number+1 == M:
                result = count+1
                queue.clear()
                break
            visited[number+1] = 1
            queue.append((number+1, count+1))
        if 0 < number-1 and not visited[number-1]: # -1
            if number-1 == M:
                result = count+1
                queue.clear()
                break
            visited[number-1] = 1
            queue.append((number-1, count+1))
        if number*2 <= 1000000 and number*2 and not visited[number*2]: # *2
            if number*2 == M:
                result = count + 1
                queue.clear()
                break
            visited[number*2] = 1
            queue.append((number*2, count+1))
        if 0 < number-10 and not visited[number-10]: # -10
            if number-10 == M:
                result = count + 1
                queue.clear()
                break
            visited[number-10] = 1
            queue.append((number-10, count+1))
T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    result = 0
    solution(N)
    print('#{} {}'.format(tc+1, result))
