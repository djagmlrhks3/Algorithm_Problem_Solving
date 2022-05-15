import sys
sys.stdin = open('백준2669. 직사각형 네개의 합집합의 면적 구하기.txt', 'r')

# Case 1
candidates = set()
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(100-y2, 100-y1):
        for c in range(x1, x2):
            candidates.add((r, c))
print(len(candidates))

# Case 2
candidates = []
answer = 0
w, h = 0, 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    candidates.append((x1, y1, x2, y2))
    w = max(w, x1, x2)
    h = max(h, y1, y2)
board = [[0] * w for _ in range(h)]
for x1, y1, x2, y2 in candidates:
    for r in range(h-y2, h-y1):
        for c in range(x1, x2):
            board[r][c] = 1
for r in range(h):
    for c in range(w):
        if board[r][c]:
            answer += 1
print(answer)