import sys
sys.stdin = open('백준11404. 플로이드.txt', 'r')

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

matrix = [[int(1e9)] * n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if r == c:
            matrix[r][c] = 0

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    if matrix[s-1][e-1] > c:
        matrix[s-1][e-1] = c

for k in range(n):
    for r in range(n):
        for c in range(n):
            matrix[r][c] = min(matrix[r][c], matrix[r][k] + matrix[k][c])

for r in range(n):
    for c in range(n):
        if matrix[r][c] == int(1e9):
            print(0, end=" ")
        else:
            print(matrix[r][c], end=" ")
    print()