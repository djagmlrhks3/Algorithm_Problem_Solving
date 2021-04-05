import sys
from collections import deque
from itertools import permutations
sys.stdin = open('백준4991. 로봇 청소기.txt', 'r')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j):
    visited = [[0] * w for _ in range(h)]
    visited[i][j] = 1
    queue = deque([(i, j)])
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                if maps[nr][nc] != 'x':
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    return visited


while True:
    w, h = map(int, input().split())
    if w + h:
        maps = [list(''.join(map(str, sys.stdin.readline().rstrip()))) for _ in range(h)]
        dusts = []
        cr, cc = 0, 0
        for r in range(h):
            for c in range(w):
                if maps[r][c] == 'o':
                    cr, cc = r, c
                elif maps[r][c] == '*':
                    dusts.append((r, c))

        cleaner = [0] * len(dusts)
        visited = bfs(cr, cc)
        is_possible = True
        for idx, rc in enumerate(dusts):
            temp = visited[rc[0]][rc[1]]
            if not temp:
                print(-1)
                is_possible = False
                break
            cleaner[idx] += temp - 1

        if is_possible:
            dists = [[0] * (len(dusts)) for _ in range(len(dusts))]
            for i in range(len(dusts) - 1):
                visited = bfs(dusts[i][0], dusts[i][1])
                for j in range(i + 1, len(dusts)):
                    dists[i][j] = visited[dusts[j][0]][dusts[j][1]] - 1
                    dists[j][i] = dists[i][j]
            answer = int(1e9)
            for li in permutations(range(len(dists))):
                temp = cleaner[li[0]]
                start = li[0]
                for idx in range(1, len(li)):
                    end = li[idx]
                    temp += dists[start][end]
                    start = end
                answer = min(answer, temp)
            print(answer)
    else:
        break