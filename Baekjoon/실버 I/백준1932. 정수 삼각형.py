import sys
sys.stdin = open('백준1932. 정수 삼각형.txt', 'r')

N = int(input())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for row in range(1, N):
    for col in range(len(triangle[row])):
        if col == 0:
            triangle[row][col] += triangle[row-1][col]
        elif col == len(triangle[row])-1:
            triangle[row][col] += triangle[row-1][col-1]
        else:
            triangle[row][col] += max(triangle[row-1][col-1], triangle[row-1][col])

print(max(triangle[-1]))