import sys
sys.stdin = open('백준9095. 1, 2, 3 더하기.txt', 'r')
from collections import deque

T = int(input())
for tc in range(T):
    n = int(input())
    queue = deque([[1], [2], [3]])
    answer = 0
    while queue:
        num = queue.popleft()
        if sum(num) == n: answer += 1; continue

        for number in range(1, 4):
            if sum(num) + number == n:
                answer += 1
                continue
            elif sum(num) + number > n:
                break
            else:
                queue.append(num + [number])
    print(answer)