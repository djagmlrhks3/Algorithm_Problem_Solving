import sys
sys.stdin = open('백준9328. 열쇠.txt', 'r')
from collections import deque

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def unlock():
    for r in range(h+2):
        for c in range(w+2):
            if maps[r][c].lower() in keys:
                maps[r][c] = '.'
    keys.clear()

def bfs():
    global answer
    queue = deque([(0, 0)])
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = 1
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < h+2 and 0 <= nc < w+2 and not visited[nr][nc]:
                if maps[nr][nc] == '*':
                    continue
                if ord('A') <= ord(maps[nr][nc]) <= ord('Z'):
                    continue
                if maps[nr][nc] == '$':
                    answer += 1
                if ord('a') <= ord(maps[nr][nc]) <= ord('z'):
                    keys.append(maps[nr][nc])
                queue.append((nr, nc))
                maps[nr][nc] = '.'
                visited[nr][nc] = 1

for _ in range(int(input())):
    h, w = map(int, input().split())

    maps = [['.'] * (w+2)]
    for _ in range(h):
        row = sys.stdin.readline().rstrip()
        row = '.' + row + '.'
        maps.append(list(''.join(row)))
    maps.append(['.'] * (w+2))

    keys = deque(list(''.join(sys.stdin.readline().rstrip())))
    answer = 0
    while keys:
        if keys[0] == '0': keys.clear()
        if keys:
            unlock()
        bfs()
    print(answer)