import sys, heapq
sys.stdin = open('백준1261. 알고스팟.txt', 'r')
M, N = map(int, input().split())

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
maps = [list(map(int, ' '.join(sys.stdin.readline().split()))) for _ in range(N)]
heap = []
heapq.heappush(heap, (0, 0, 0))
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
while heap:
    w, r, c = heapq.heappop(heap)
    if r == N-1 and c == M-1:
        print(w)
        break
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if 0 <= nr < N and 0 <= nc < M:
            if maps[nr][nc] and not visited[nr][nc]:
                heapq.heappush(heap, (w+1, nr, nc))
                visited[nr][nc] = 1
            elif not maps[nr][nc] and not visited[nr][nc]:
                heapq.heappush(heap, (w, nr, nc))
                visited[nr][nc] = 1