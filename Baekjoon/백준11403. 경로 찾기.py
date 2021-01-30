import sys
sys.stdin = open('백준11403. 경로 찾기.txt', 'r')
N = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

adj = {i:[] for i in range(N)}

for r in range(N):
    for c in range(N):
        if matrix[r][c]:
            adj[r].append(c)

for s in range(N):
    stack = [s]
    visited = []
    while stack:
        node = stack.pop()
        for e in adj[node]:
            if e not in visited:
                matrix[s][e] = 1
                stack.append(e)
                visited.append(e)

for row in matrix:
    print(' '.join(map(str, row)))