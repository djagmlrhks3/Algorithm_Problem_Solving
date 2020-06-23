import sys
sys.stdin = open('백준1697. 숨바꼭질.txt','r')

route = list()
for i in range(0, 100001):  # 동생보다 한 칸 전까지 움직일 수 있는 모든경우 리스트만들기
    empty = list()
    if 0 <= i - 1 <= 100000:
        empty.append(i - 1)
    if 0 <= i + 1 <= 100000:
        empty.append(i + 1)
    if 0 <= i * 2 <= 100000:
        empty.append(i * 2)
    route.append(empty)
N, K = map(int,input().split())
if N < K:   #동생이 더 뒤에있을 때
    queue = list()
    queue.append(N)
    visited = [0] * 100001   #동생의 위치까지 visited 만들기
    visited[N] = 1          #본인의 위치 1
    while len(queue):
        N = queue.pop(0)
        for i in route[N]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[N] + 1
            if i == K:
                queue.clear()
    print(visited[K]-1)
else:   #동생보다 뒤에있거나 같을 때는 차이만 출력하면 된다.
    print(N-K)
"""
종호형 코드
X, K = map(int, input().split())

visited = [0]*100001
Q = [(X,0)]
visited[X] = 1
ans = 0
if X == K:
    print(ans)
else:
    while Q:
        temp = Q.pop(0)
        t = [temp[0]+1,temp[0]-1,temp[0]*2]
        if K in t:
            ans = temp[1]+1
            break
        for i in t:
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = 1
                Q.append((i,temp[1]+1))
    print(ans)

"""