import sys
sys.stdin = open('백준1149. RGB거리.txt', 'r')

N = int(input())
RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(RGB)
for row in range(1, len(RGB)):
    for col in range(3):
        if col == 0:
            RGB[row][col] += min(RGB[row-1][1], RGB[row-1][2])
        elif col == 1:
            RGB[row][col] += min(RGB[row-1][0], RGB[row-1][2])
        else:
            RGB[row][col] += min(RGB[row-1][0], RGB[row-1][1])

print(min(RGB[-1]))