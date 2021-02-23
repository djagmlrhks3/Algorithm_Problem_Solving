import sys, heapq
sys.stdin = open('백준1197. 최소 스패닝 트리.txt', 'r')

def find_parent(node):
    if node != parent[node]:
        return find_parent(parent[node])
    return parent[node]

def union_parent(n1, n2):
    n1 = find_parent(n1)
    n2 = find_parent(n2)
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2

V, E = map(int, input().split())
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(edges, (C, A-1, B-1))

parent = [i for i in range(V)]
answer = 0

while edges:
    C, A, B = heapq.heappop(edges)
    if find_parent(A) != find_parent(B):
        union_parent(A, B)
        answer += C

print(answer)
