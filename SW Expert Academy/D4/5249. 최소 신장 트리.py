import sys
sys.stdin = open('5249. 최소 신장 트리.txt', 'r')

import heapq # heapq 라이브러리 사용
T = int(input())
for tc in range(T):
    V, E = map(int,input().split())
    adj = {i : [] for i in range(V+1)}
    for _ in range(E):
        n1, n2, w = map(int,input().split()) #무방향 그래프
        adj[n1].append([n2, w])
        adj[n2].append([n1, w])
    INF = float('inf')
    key = [INF] * (V+1)
    mst = [False] * (V+1)
    pq = []
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    result = 0
    while pq:
        k, node = heapq.heappop(pq)
        if mst[node]:continue
        mst[node] = True
        result += k
        for dest, wt in adj[node]:
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq, (key[dest],dest))
    print('#{} {}'.format(tc+1, result))
