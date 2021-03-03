import sys
sys.stdin = open('백준13023. ABCDE.txt', 'r')

def dfs(node, depth, visited):
    global flag
    if depth == 5:
        flag = True
        return
    for idx in relationship[node]:
        if not visited[idx]:
            visited[idx] = True
            dfs(idx, depth+1, visited)
            visited[idx] = False

N, M = map(int, input().split())
relationship = {i:[] for i in range(N)}
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    relationship[s].append(e)
    relationship[e].append(s)

flag = False
for node in range(N):
    if not flag:
        visited = [False] * N
        visited[node] = True
        dfs(node, 1, visited)
    else:
        break
print(1) if flag else print(0)
