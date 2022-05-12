import sys
sys.stdin = open('백준16967. 배열 복원하기.txt', 'r')

H, W, X, Y = map(int, input().split())
A = [[0] * W for _ in range(H)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(X+H)]

for r in range(H):
    for c in range(W):
        if r >= X and c >= Y:
            A[r][c] = B[r][c] - A[r-X][c-Y]
        else:
            A[r][c] = B[r][c]
for i in A:
    print(' '.join(map(str, i)))