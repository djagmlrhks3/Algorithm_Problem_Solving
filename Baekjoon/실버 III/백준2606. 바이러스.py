import sys
sys.stdin = open('백준2606. 바이러스.txt','r')

N = int(input())
V = int(input())
matrix = [ [0] * (N+1) for _ in range(N+1) ]
for v in range(V):
    x, y = map(int,input().split())
    matrix[x][y] = matrix[y][x] = 1

visited = [0] * (N+1)
stack = [1]
while len(stack):
    start = stack.pop(-1)
    visited[start] = 1
    for i in range(N+1):
        if matrix[start][i] and visited[i] == 0:
            stack.append(i)
print(sum(visited)-1)
