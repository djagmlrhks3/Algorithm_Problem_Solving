import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('백준11724. 연결 요소의 개수.txt', 'r')

def dfs(node):
    global cnt
    group[node] = cnt
    for next_node in edge[node]:
        if not group[next_node]:
            dfs(next_node)

N, M = map(int, input().split())
edge = {i:[] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)
group = [0] * (N+1)
cnt = 0
for node in range(1, N+1):
    if not group[node]:
        cnt += 1
        dfs(node)
print(len(set(group))-1)