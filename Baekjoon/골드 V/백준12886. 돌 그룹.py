import sys
from collections import deque
sys.stdin = open('백준12886. 돌 그룹.txt', 'r')
numbers = list(map(int, input().split()))
A = max(numbers)
C = min(numbers)
B = sum(numbers) - A - C
queue = deque([(A, B, C)])
visited = [[False] * 1501 for _ in range(1501)]
visited[A][B] = True
def check(A, B, C):
    a, c = max(A, B, C), min(A, B, C)
    b = A+B+C-(a+c)
    if not visited[a][b]:
        visited[a][b] = True
        queue.append((a, b, c))
        return True
    return False

while queue:
    a, b, c = queue.popleft()
    if a == b == c:
        print(1)
        break
    temp_a1, temp_b1, temp_c1 = a-b, b+b, c
    temp_a2, temp_b2, temp_c2 = a-c, b, c+c
    temp_a3, temp_b3, temp_c3 = a, b-c, c+c
    if temp_a1 > 0:
        check(temp_a1, temp_b1, temp_c1)
    if temp_a2 > 0:
        check(temp_a2, temp_b2, temp_c2)
    if temp_b3 > 0:
        check(temp_a3, temp_b3, temp_c3)
else:
    print(0)
