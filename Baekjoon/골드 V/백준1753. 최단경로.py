import sys, heapq
sys.stdin = open('백준1753. 최단경로.txt', 'r')

V, E = map(int, input().split())
start = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, c = map(int, sys.stdin.readline().split())
    edges[s].append((c, e))

dist = [int(1e9)] * (V+1)
dist[start] = 0
heap = [(0, start)]
while heap:
    c, n = heapq.heappop(heap)
    for cost, node in edges[n]:
        temp = c + cost
        if temp < dist[node]:
            dist[node] = temp
            heapq.heappush(heap, (temp, node))

for n in range(1, V+1):
    print(dist[n]) if dist[n] != int(1e9) else print("INF")