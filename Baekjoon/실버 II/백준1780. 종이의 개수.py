import sys
sys.stdin = open('백준1780. 종이의 개수.txt', 'r')

def check(i, j, size):
    global m_one, zero, one
    compare = paper[i][j]
    for r in range(i, i + size):
        for c in range(j, j + size):
            if paper[r][c] != compare:
                return False
    if paper[r][c] == 1:
        one += 1
    elif paper[r][c] == 0:
        zero += 1
    elif paper[r][c] == -1:
        m_one += 1

    for r in range(i, i + size):
        for c in range(j, j + size):
            paper[r][c] = 2
    return True

def recursive(r, c, size):
    global m_one, zero, one
    if size == 1:
        if paper[r][c] == 1:
            one += 1
        elif paper[r][c] == 0:
            zero += 1
        elif paper[r][c] == -1:
            m_one += 1
        return
    if 0 <= r < N and 0 <= c < N and paper[r][c] != 2:
        if not check(r, c, size):
            for i in range(3):
                for j in range(3):
                    recursive(r + size * i // 3, c + size * j // 3, size // 3)

N = int(input())
one, zero, m_one = 0, 0, 0
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
recursive(0, 0, N)

print(m_one)
print(zero)
print(one)