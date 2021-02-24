import sys
sys.stdin = open('백준4963. 섬의 개수.txt','r')

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,1,-1,-1,0,1]

def dfs(r, c):
    if visited[r][c]: return
    visited[r][c] = island
    for idx in range(8):
        nr = r + dx[idx]
        nc = c + dy[idx]
        if 0 <= nr < h and 0 <= nc < w and matrix[nr][nc]:
            dfs(nr, nc)

while True:
    w, h = map(int, input().split())
    if not w + h: break
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    island = 0
    for r in range(h):
        for c in range(w):
            if matrix[r][c] and not visited[r][c]:
                island += 1
                dfs(r, c)
    print(island)


