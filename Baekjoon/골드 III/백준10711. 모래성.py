import sys
from collections import deque
sys.stdin = open('백준10711. 모래성.txt', 'r')

d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
H, W = map(int, input().split())
sands = [list(map(str, ''.join(sys.stdin.readline().rstrip()))) for _ in range(H)]

def crush(r, c):
    global is_crush
    for idx in range(8):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if 0 <= nr < H and 0 <= nc < W and sands[nr][nc] != '.':
            sands[nr][nc] = int(sands[nr][nc]) - 1
            if sands[nr][nc] == 0:
                queue.append((nr, nc))
                is_crush = True

answer = 0
queue = deque([])
for r in range(H):
    for c in range(W):
        if sands[r][c] == '.':
            queue.append((r, c))
while queue:
    is_crush = False
    for _ in range(len(queue)):
        r, c = queue.popleft()
        crush(r, c)
    if is_crush:
        answer += 1
print(answer)