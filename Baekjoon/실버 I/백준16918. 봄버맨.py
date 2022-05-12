import sys
sys.stdin = open('백준16918. 봄버맨.txt', 'r')

def pop():
    global N
    candidate = []
    for r in range(R):
        for c in range(C):
            if maps[r][c] == 2:
                candidate.append((r, c))
                for i in range(4):
                    nr, nc = r+d[i][0], c+d[i][1]
                    if 0 <= nr < R and 0 <= nc < C:
                        candidate.append((nr, nc))
    while candidate:
        r, c = candidate.pop()
        maps[r][c] = 0
    N -= 1

def add():
    global N
    for r in range(R):
        for c in range(C):
            maps[r][c] = maps[r][c] + 1
    N -= 1

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
R, C, N = map(int, input().split())

maps = [[0] * C for _ in range(R)]

for r in range(R):
    row = sys.stdin.readline().rstrip()
    for c in range(C):
        if row[c] == 'O':
            maps[r][c] = 1

N -= 1
while N > 0:
    add()
    if not N: break
    pop()
    if not N: break

answer = []
for r in range(R):
    row = ''
    for c in range(C):
        if maps[r][c]:
            row += 'O'
        else:
            row += '.'
    answer.append(row)

for i in answer:
    print(i)