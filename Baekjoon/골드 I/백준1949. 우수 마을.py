import sys
sys.stdin = open('백준1949. 우수 마을.txt', 'r')
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
people = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
DP = [[0, 0] for _ in range(n + 1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

check = [True] * (n+1)

def dfs(n):
    check[n] = False
    DP[n][0] = people[n]
    DP[n][1] = 0
    for i in graph[n]:
        if check[i]:
            dfs(i)
            DP[n][0] += DP[i][1]
            DP[n][1] += max(DP[i][0], DP[i][1])

dfs(1)
print(max(DP[1][0], DP[1][1]))
