import sys
sys.stdin = open('백준2580. 스도쿠.txt', 'r')

def check(r, c):
    global matrix, cols
    exist = set()
    for num in matrix[r]:
        if num: exist.add(num)
    for idx in range(9):
        if matrix[idx][c]: exist.add(matrix[idx][c])

    sr, sc = r//3*3, c//3*3
    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if matrix[i][j]: exist.add(matrix[i][j])
    return list(all - exist)

def res():
    for row in matrix:
        print(' '.join(map(str, row)))

def solve(r, c):
    if c == 9: r += 1; c = 0
    if r > 8 or c > 8:
        res()
        exit()
    if not matrix[r][c]:
        candidates = check(r, c)
        for num in candidates:
            matrix[r][c] = num
            solve(r, c+1)
            matrix[r][c] = 0
    else:
        solve(r, c+1)

matrix = [list(map(int, input().split())) for _ in range(9)]
all = set(i for i in range(1, 10))
solve(0, 0)
