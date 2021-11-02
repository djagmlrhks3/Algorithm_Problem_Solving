import sys
sys.stdin = open('백준9465. 스티커.txt', 'r')
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(max(int(input()) for _ in range(2)))
    else:
        sticker = [list(map(int, input().split())) for _ in range(2)]
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]
        for c in range(2, n):
            sticker[0][c] += max(sticker[1][c-1], sticker[1][c-2])
            sticker[1][c] += max(sticker[0][c-1], sticker[0][c-2])
        print(max(sticker[0][-1], sticker[1][-1]))