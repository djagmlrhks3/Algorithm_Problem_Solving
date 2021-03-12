import sys
sys.stdin = open('백준1956. 운동.txt', 'r')

V, E = map(int, sys.stdin.readline().split())
matrix = [[int(1e9)] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a-1][b-1] = c

for k in range(V):
    for n1 in range(V):
        for n2 in range(V):
            matrix[n1][n2] = min(matrix[n1][n2], matrix[n1][k] + matrix[k][n2])

answer = int(1e9)
for i in range(V):
    answer = min(answer, matrix[i][i])

print(-1) if answer == int(1e9) else print(answer)