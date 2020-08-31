import sys
sys.stdin = open('1226. 미로1.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    stack = [(x, y)]
    visited = [(x, y)]
    while stack:
        x, y = stack.pop(-1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and (nx, ny) not in visited:
                if matrix[nx][ny] == '0':
                    stack.append((nx, ny))
                    visited.append((nx, ny))
                if matrix[nx][ny] == '3':
                    return True
for tc in range(10):
    n = input()
    matrix = [ input() for _ in range(16)]
    res = 1 if dfs(1, 1) else 0
    print('#{} {}'.format(tc+1, res))