import sys
sys.stdin = open('1251. 하나로.txt', 'r')
import heapq
# INF = float('inf')
# def prim(start):
#     total = 0
#
#     key[start] = 0
#     heapq.heappush(pq, (key[start], 0))
#     while pq:
#         dist, u = heapq.heappop(pq)
#         if visit[u]:continue
#         visit[u] = 1
#         total += distance[PI[u]][u] * tax_rate
#
#         for v in range(N):
#             if visit[v] == 0 and key[v] > distance[u][v]:
#                 key[v] = distance[u][v]
#                 PI[v] = u
#                 heapq.heappush(pq, (key[v], v))
#     return total
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     key = [INF] * N
#     visit = [0] * N
#     PI = list(range(N))
#     pq = []
#     xarr = list(map(int, input().split()))
#     yarr = list(map(int, input().split()))
#     tax_rate = float(input())
#     distance = [[0] * N for _ in range(N)]
#     for i in range(N-1):
#         for j in range(i+1, N):
#             distance[j][i] = distance[i][j] = (xarr[i] - xarr[j]) ** 2 + (yarr[i] - yarr[j]) ** 2
#     print('#{} {}'.format(tc+1, round(prim(0))))


# 나중에 결과값을 계산할 때 다시 제곱을 해주므로 ^(0.5)는 생략
def distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


T = int(input())
for tc in range(T):
    N = int(input())
    adj = {i: [] for i in range(N)}  # 인접리스트 생성
    x = list(map(int, input().split()))  # x좌표
    y = list(map(int, input().split()))  # y좌표
    E = float(input())
    # 모든 섬들이 연결되어있으므로 각 연결마다 거리계산
    for i in range(N):
        for j in range(i + 1, N):
            dist = distance(x[i], y[i], x[j], y[j])
            adj[i].append((j, dist))
            adj[j].append((i, dist))
    # cost 무한대로 초기설정 (첫번째 부터 시작할 것이므로 첫번째 값은 0)
    cost = [0] + [float('inf')] * (N - 1)
    # mst 초기설정 : mst로 형성되면 True
    mst = [False] * N
    # 우선순위큐 priority queue
    pq = []
    # 첫번째 섬부터시작, 다리길이
    heapq.heappush(pq, (0, 0))
    # 결과값을 담을 변수
    answer = 0
    while pq:
        # 다리길이, 현재 섬
        nowbridge, nowisland = heapq.heappop(pq)

        # mst에 연결(연결되어있으면 continue로 skip)
        if mst[nowisland]: continue
        mst[nowisland] = True
        # mst로 형성된 nowisland의 cost를 미리 계산
        answer += cost[nowisland]
        # 현재섬에서 인접한 섬 탐색
        for island, bridge in adj[nowisland]:
            # 인접했지만 mst로 형성되지 않은 섬 & 비용이 더 적은 다리가 있으면 값 갱신
            if not mst[island] and cost[island] > bridge:
                cost[island] = bridge
                heapq.heappush(pq, (cost[island], island))
    print('#{} {}'.format(tc + 1, round((answer * E))))

