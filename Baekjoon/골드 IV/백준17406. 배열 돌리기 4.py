import sys
from itertools import permutations
from copy import deepcopy
sys.stdin = open('백준17406. 배열 돌리기 4.txt', 'r')

def rotate(cases, copy_matrix):
    global answer
    for case in cases:
        r, c, s = case
        r -= 1
        c -= 1
        print(r, c, s)
        for inner in range(s, 0, -1):
            top_right = copy_matrix[r-inner][c+inner]
            bottom_left = copy_matrix[r+inner][c-inner]
            bottom_right = copy_matrix[r+inner][c+inner]
            for idx in range(c+inner, c-inner, -1):
                copy_matrix[r-inner][idx] = copy_matrix[r-inner][idx-1]
            for idx in range(r+inner, r-inner, -1):
                copy_matrix[idx][c+inner] = copy_matrix[idx-1][c+inner]
            for idx in range(c-inner, c+inner):
                copy_matrix[r+inner][idx] = copy_matrix[r+inner][idx+1]
            for idx in range(r-inner, r+inner):
                copy_matrix[idx][c-inner] = copy_matrix[idx+1][c-inner]
            copy_matrix[r-inner+1][c+inner] = top_right
            copy_matrix[r+inner][c+inner-1] = bottom_right
            copy_matrix[r+inner-1][c-inner] = bottom_left

    for row in copy_matrix:
        answer = min(answer, sum(row))

N, M, K = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotates = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
answer = 0xfffffffffffff

for cases in permutations(rotates, K):
    rotate(cases, deepcopy(matrix))
print(answer)