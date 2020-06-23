import sys
sys.stdin = open('5251. 최소 이동 거리.txt', 'r')

T = int(input())
for tc in range(T):
    N, E = map(int, input().split())
    adj = {i : [] for i in range(N+1)}
    for _ in range(E):
        s, e, w = map(int,input().split())
        adj[s].append([e,w])

    INF = float('inf')
    distance = [INF] * (N+1) #비용(거리)를 무한으로 설정
    selected = [False] * (N+1) #선택할 때마다(지나갈 때마다) True로 변환
    distance[0] = 0 #처음시작할 정점을 0으로 지정
    cnt = 0 #모든 정점을 지나가면 종료시키기 위한 변수

    while cnt < N:
        mini = INF #최소값을 찾기위해 가장 큰 값을 초기설정
        u = -1 #정점을 찾기위한 변수
        for i in range(N+1):
            if not selected[i] and distance[i] < mini: #지나가지않은정점 & 비용이 더 적은 값이 나오면
                mini = distance[i] #최소값 갱신
                u = i #최소값을 가진 정점 최신화
        selected[u] = True #최소값을 가진 정점에대해 지나갔음을 표시
        cnt += 1 #정점을 지나쳤으니 +1
        for end, cost in adj[u]:
            if distance[end] > distance[u] + cost: #end정점이 가지고 있는 비용보다 지금까지 지나온 비용이 더 적은 경우
                distance[end] = distance[u] + cost #갱신
    print('#{} {}'.format(tc+1, distance[-1]))
