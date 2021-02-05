import sys
sys.stdin = open('백준14716. 현수막.txt', 'r')

dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, -1, 1, 1, -1]

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(M)]

visited = [[0]*N for _ in range(M)]
res = 0
stack = []
for m in range(M):
    for n in range(N):
        if not visited[m][n] and matrix[m][n]:
            res += 1
            stack.append((m, n))
            while stack:
                x, y = stack.pop(-1)
                visited[m][n] = 1
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < M and 0 <= ny < N:
                        if matrix[nx][ny] and not visited[nx][ny]:
                            stack.append((nx, ny))
                            visited[nx][ny] = 1
print(res)