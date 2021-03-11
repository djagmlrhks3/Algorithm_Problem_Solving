import sys
sys.stdin = open('백준2630. 색종이 만들기.txt', 'r')

def check(r, c, N):
    global white, blue
    compare = paper[r][c]
    for i in range(r, r+N):
        for j in range(c, c+N):
            if paper[i][j] != compare:
                return False
    if compare == 1: blue += 1
    else: white += 1

    for i in range(r, r+N):
        for j in range(c, c+N):
            paper[i][j] = 2
    return True

def recursive(r, c, size):
    global blue, white
    if 0 <= r < N and 0<= c < N and paper[r][c] != 2:
        if size == 1:
            if paper[r][c] == 1: blue += 1
            elif paper[r][c] == 0: white += 1
            return
        if not check(r, c, size):
            recursive(r, c, size//2)
            recursive(r, c + size//2, size//2)
            recursive(r + size//2, c, size//2)
            recursive(r + size//2, c + size//2, size//2)
    return

N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white, blue = 0, 0
recursive(0, 0, N)
print(white)
print(blue)
