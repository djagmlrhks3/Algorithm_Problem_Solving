import sys
sys.stdin = open('백준17404. RGB거리 2.txt', 'r')

N = int(input())
RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 1001 * 1000
for i in range(3):
    DP = [[1001] * 3 for _ in range(len(RGB))]
    DP[0][i] = RGB[0][i]
    for r in range(1, len(RGB)):
        DP[r][0] = RGB[r][0] + min(DP[r-1][1], DP[r-1][2])
        DP[r][1] = RGB[r][1] + min(DP[r-1][0], DP[r-1][2])
        DP[r][2] = RGB[r][2] + min(DP[r-1][0], DP[r-1][1])
    for j in range(3):
        if i != j:
            answer = min(DP[-1][j], answer)

print(answer)