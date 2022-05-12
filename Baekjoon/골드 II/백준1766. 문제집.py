import sys, heapq
sys.stdin = open('백준1766. 문제집.txt', 'r')

N, M = map(int, input().split())

indegree = [0] * (N+1)
turn = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    turn[s].append(e)
    indegree[e] += 1

def topological_sort():
    result = []
    heap = []
    for i in range(1, N+1):
        if not indegree[i]:
            heapq.heappush(heap, i)
    while heap:
        now = heapq.heappop(heap)
        result.append(now)
        for n in turn[now]:
            indegree[n] -= 1
            if not indegree[n]:
                heapq.heappush(heap, n)
    return ' '.join(map(str, result))

print(topological_sort())
