import sys
sys.stdin = open('5521. 상원이의 생일파티.txt', 'r')

from collections import deque

def bfs(n):
    #방문여부 확인하는 리스트
    visited = [0]*(N+1)
    visited[1] = 1
    #queue(deque사용)
    queue = deque()
    queue.append(n)
    while queue:
        #queue에서 하나씩 빼서 해당값에 인접한 값 파악 
        man = queue.popleft()
        for i in friends[man]:
            #인접하면서 방문하지 않아야 함
            if not visited[i]:
                #가지치기 : 친구의 친구까지(상원=1 / 이후 단계마다 + 1이므로 3까지가 친구의친구
                if visited[man]+1 < 4:
                    queue.append(i)
                    #이전의 값 + 1로 visited값 최신화
                    visited[i] = visited[man] + 1
                #만약 친구의 친구의 친구가 나타나면 break
                else:
                    queue.clear()
                    break
    #친구의친구 수를 출력
    result = 0
    for num in visited:
        if num > 1:result+=1
    print('#{} {}'.format(tc+1, result))
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    #인접리스트
    friends = [[] for _ in range(N+1)]
    #무방향그래프
    for m in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    #상원이는 1번
    bfs(1)