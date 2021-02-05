import sys
sys.stdin = open('백준1260. DFS와 BFS.txt','r')


def dfs(node):
    visited[node] = True
    print(node,end=" ")
    for i in ad_list[node]:
        if not visited[i]:
            dfs(i)

def bfs(node):
    queue = list()
    queue.append(node)
    visited[node] = True
    while len(queue):
        node = queue.pop(0)
        print(node,end=" ")
        for i in ad_list[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, E, S = map(int,input().split())
ad_list = [[] for _ in range(N+1)]
for _ in range(E):
    s, e = map(int,input().split())
    ad_list[s].append(e)
    ad_list[e].append(s)
for i in ad_list:
    i.sort()

visited = [False]*(N+1)
dfs(S)
print()
visited = [False]*(N+1)
bfs(S)
