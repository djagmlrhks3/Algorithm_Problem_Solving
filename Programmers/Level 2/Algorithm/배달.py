from collections import deque
def solution(N, road, K):
    answer = 0
    dist = [0] + [int(1e9)] * (N-1)
    maps = [[int(1e9)] * N for _ in range(N)]
    for s, e, t in road:
        maps[s-1][e-1] = min(maps[s-1][e-1], t)
        maps[e-1][s-1] = min(maps[e-1][s-1], t)

    queue = deque([(0, 0)])
    while queue:
        node, v = queue.popleft()
        for next_node in range(N):
            if dist[next_node] > v + maps[node][next_node]:
                dist[next_node] = v + maps[node][next_node]
                queue.append((next_node, dist[next_node]))

    for num in dist:
        if num <= K:
            answer += 1
    return answer

solution(6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)