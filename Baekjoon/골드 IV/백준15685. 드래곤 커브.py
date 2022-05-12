import sys
sys.stdin = open('백준15685. 드래곤 커브.txt', 'r')

di = [(0, 1), (-1, 0), (0, -1), (1, 0)]

N = int(input())
maps = [[0] * 101 for _ in range(101)]
for n in range(N):
    c, r, d, g = map(int, sys.stdin.readline().split())
    maps[r][c] = 1
    move = [d]
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1]+1) % 4)
        move += temp
    for idx in move:
        nr = r+di[idx][0]
        nc = c+di[idx][1]
        maps[nr][nc] = 1
        r, c = nr, nc

cnt = 0
for r in range(100):
    for c in range(100):
        if maps[r][c] and maps[r+1][c] and maps[r+1][c+1] and maps[r][c+1]:
            cnt += 1
print(cnt)