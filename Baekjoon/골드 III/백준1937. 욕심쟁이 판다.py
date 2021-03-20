import sys, heapq
sys.stdin = open('백준1937. 욕심쟁이 판다.txt', 'r')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n = int(input())
ground = [[0] * n for _ in range(n)]
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
heap = []

for r in range(n):
    for c in range(n):
        heapq.heappush(heap, (matrix[r][c], r, c))

answer = 0
while heap:
    bamboo, r, c = heapq.heappop(heap)
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if 0 <= nr < n and 0 <= nc < n:
            if matrix[r][c] > matrix[nr][nc]:
                ground[r][c] = max(ground[r][c], ground[nr][nc])
    ground[r][c] += 1
    answer = max(answer, ground[r][c])

print(answer)

# DFS
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# def dfs(x, y):
#     if dp[x][y]: return dp[x][y]
#     dp[x][y] = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if s[x][y] < s[nx][ny]:
#                 dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
#     return dp[x][y]
# n = int(input())
# s = [list(map(int, input().split())) for i in range(n)]
# dp = [[0] * n for i in range(n)]
# result = 0
# for i in range(n):
#     for j in range(n):
#         result = max(result, dfs(i, j))
# print(result)