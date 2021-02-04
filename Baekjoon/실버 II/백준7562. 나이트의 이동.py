import sys
sys.stdin = open('백준7562. 나이트의 이동.txt', 'r')
from collections import deque

d = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
      (1, -2), (2, -1), (2, 1), (1, 2)]
T = int(input())
for _ in range(T):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    queue = deque([(sr, sc)])
    matrix[sr][sc] = 0

    while queue:
        r, c = queue.popleft()
        if r == er and c == ec:
            print(matrix[r][c])
            break
        for idx in range(8):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < N and 0 <= nc < N:
                if not matrix[nr][nc]:
                    matrix[nr][nc] = matrix[r][c] + 1
                    queue.append((nr, nc))