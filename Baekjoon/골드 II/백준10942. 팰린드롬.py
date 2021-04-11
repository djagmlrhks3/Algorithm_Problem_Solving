import sys
sys.stdin = open('백준10942. 팰린드롬.txt', 'r')
N = int(input())
boards = list(map(int, sys.stdin.readline().split()))
DP = [[0] * N for _ in range(N)]
for i in range(N): # 길이 - 1
    DP[i][i] = 1
for i in range(N-1): # 길이 - 2
    if boards[i] == boards[i+1]:
        DP[i][i+1] = 1
for l in range(2, N): # 길이 - 3이상
    for i in range(N-l):
        if boards[i] == boards[i+l] and DP[i+1][i+l-1] == 1: # 첫번째 == 마지막 and DP[첫번째+1][마지막-1] 팰린드롬 여부
            DP[i][i+l] = 1

for _ in range(int(input())):
    s, e = map(int, sys.stdin.readline().split())
    print(DP[s-1][e-1])