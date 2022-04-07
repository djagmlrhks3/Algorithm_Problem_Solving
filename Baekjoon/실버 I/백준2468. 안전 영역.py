import sys
sys.stdin = open('백준2468. 안전 영역.txt', 'r')

def check():
    global answer
    visited = [[0] * n for _ in range(n)]
    stack = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                stack.append((i, j))
                while stack:
                    r, c = stack.pop()
                    for idx in range(4):
                        nr, nc = r+d[idx][0], c+d[idx][1]
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                            if  arr[nr][nc]:
                                stack.append((nr, nc))
                                visited[nr][nc] = 1
    answer = max(cnt, answer)

def rain():
    zero = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c]:
                arr[r][c] -= 1
            else:
                zero += 1
    if zero == n ** 2:
        return True
    return False

n = int(input())
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 1

while True:
    if rain(): break
    check()
print(answer)