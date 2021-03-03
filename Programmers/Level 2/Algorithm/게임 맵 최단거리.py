from collections import deque
def solution(maps):
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if nr == n-1 and nc == m-1: return visited[r][c] + 1
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc]:
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))