import sys
sys.stdin = open('백준17140. 이차원 배열과 연산.txt', 'r')

r, c, k = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

def calculate(matrix, dir):
    new_matrix, length = [], 0
    for row in matrix:
        num_cnt, new_row = [], []
        for num in set(row):
            if num == 0: continue
            cnt = row.count(num)
            num_cnt.append((num, cnt))
        num_cnt = sorted(num_cnt, key=lambda x:[x[1], x[0]])
        for num, cnt in num_cnt:
            new_row += [num, cnt]
        new_matrix.append(new_row)
        length = max(length, len(new_row))

    for row in new_matrix:
        row += [0] * (length - len(row))
        if len(row) > 100: row = row[:100]

    return list(zip(*new_matrix)) if dir == 'C' else new_matrix

time = 0
while True:
    if time > 100: time = -1; break
    if 0 <= r-1 < len(matrix) and 0 <= c-1 < len(matrix[0]) and matrix[r-1][c-1] == k: break
    if len(matrix) >= len(matrix[0]):
        matrix = calculate(matrix, 'R')
    else:
        matrix = calculate(list(zip(*matrix)), 'C')
    time += 1
print(time)