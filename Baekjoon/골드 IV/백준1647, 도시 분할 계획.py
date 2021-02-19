import sys
sys.stdin = open('백준1647. 도시 분할 계획.txt', 'r')

def find_parents(parents, x):
    if parents[x] != x:
        return find_parents(parents, parents[x])
    return parents[x]

def union_parent(parents, A, B):
    a = find_parents(parents, A)
    b = find_parents(parents, B)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M = map(int, input().split())
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((C, A, B))

roads = sorted(roads)
cost = 0
parents = [i for i in range(N+1)]
for c, a, b in roads:
    if find_parents(parents, a) != find_parents(parents, b):
        union_parent(parents, a, b)
        cost += c
        last = c
print(cost - last)

