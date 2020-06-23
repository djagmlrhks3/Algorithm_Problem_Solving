import sys
sys.stdin = open('4871. 그래프 경로.txt','r')
"""
강사님 코드에 v값에 start를 주고 완전탐색 시작(DFS)
탐색 후 pop해줄 때 해당 값이 end와 같으면 True
길이가 0이 될 떄 까지(즉, 노드간 간선이 없는 경우) end값을 찾지 못하면 False
"""
def CRTESTACK() :  return([])                #stack을 생성해주는 함수
def PUSH(stack,item) :  stack.append(item)   #stack에 item을 추가해주는 함수
def ISEMPTY(stack) :    return len(stack)==0 #길이가 0인지 확인해주는 함수
def POP(stack) :        return stack.pop(-1) if len(stack) else None #길이가 0이 아니면 stack에서 마지막 것을 빼주는 함수

def DFS(G, v):              # visit:PUSH시점과 연관, LtoR
    visited = [False]*(V+1) #노드들의 숫자가 1부터 시작이므로 +1 만큼의 길이로 리스트를 생성(False : 초기값/ 아직 지나간 곳 없음)
    stack0 = CRTESTACK()
    visited[v] = True               #v는 지나간 곳이기 때문에 True로 바꿔줌
    flag = False
    while True :
        w = 0               #인접한 노드가 있을 경우 1을 주었기 때문에 0으로 초기화 시킴 (그리고 앞에서부터 진행하기 때문에 내림차순임!).
        #시작 지점을 위한 코딩
        for i in range(1,V+1):
            if not visited[i] and G[v][i] :    #visited가 False이고 G[v][i]의 값이 0이 아닌경우(인접한 경우) = 방문을 안했고 인접했는지 묻는 부분
                PUSH(stack0,v);     # (*)      #그러면 stack0에 해당 노드를 푸쉬해!!!
                w = i;                         #그리고 그 노드를 w
                break   # (*)
        #방문을 했으면 방문한 노드를 stack에 쌓는 코딩
        while w :
            visited[w] = True           # (*) visit위치
            PUSH(stack0,w)              # (*)
            v = w

            #v의 인접점w(not visited) 찾기
            w = 0
            for i in range(1,V+1):
                if not visited[i] and G[v][i]:
                    w = i;
                    break

        if ISEMPTY(stack0) : break
        if stack0[0] == start and stack0[-1] == end:
            flag = True
            break
        v = POP(stack0)                 # (*)
    if flag:
        print('#{} {}'.format(tc + 1, 1))
    else:
        print('#{} {}'.format(tc + 1, 0))

T = int(input())
for tc in range(T):
    V, E = map(int,input().split())
    edges = list()
    for _ in range(E):
        u, v = map(int,input().split())
        edges.append(u)
        edges.append(v)
    start, end = map(int,input().split())
    #노드와 서로 연결된 엣지들에 대한 설정
    G = [[0]*(V+1) for _ in range(V+1)]
    for i in range(0,len(edges),2) :
        u = edges[i];
        v = edges[i+1]
        G[u][v] = 1                 #나와연결된 노드들은 상대방도 연결되어 있으므로 x,y좌표를 바꾼 값도 같이 1이되도록 설정
        #
    DFS(G,start)


# import sys
# # sys.stdin = open('4871. 그래프 경로.txt','r')
# #
# # T = int(input())
# # for tc in range(T):
# #     V, E = map(int,input().split())   #V는 노드 E는 간선의 수
# #     visited = [False]*(V+1)
# #     G = [[0]*(V+1) for _ in range(V+1)]
# #     for i in range(E):
# #         node1, node2 = map(int,input().split())
# #         G[node1][node2] = G[node2][node1] = 1
# #     start, end = map(int,input().split())

# #DFS(G,start)
# #DFS_recur(G,1)

# def CRTESTACK() :  return([])
# def PUSH(stack,item) :  stack.append(item)
# def ISEMPTY(stack) :    return len(stack)==0
# def POP(stack) :        return stack.pop(-1) if len(stack) else None
# def PEEK(stack) :       return stack[-1] if len(stack) else None

# V = 7       # 1~7
# def DFS(G, v):            # visit:POP시점과 연관, RtoL
#     visited = [False]*(V+1)         #초기값 +1 개수만큼 False 반환
#     stack0 = CRTESTACK()            #stack0라는 리스트 생성
#     PUSH(stack0,v)                # (*) #1(시작)값을 stack0에 넣음
#     while not ISEMPTY(stack0):    # 1을 넣은 뒤로 stack0가 0이 아닐때까지 반복
#         v = POP(stack0)           # (*)
#         if not visited[v]:
#             visited[v] = True       # (*) visit위치
#             print("-", v, end="")
#             for i in range(1,V+1):
#                 if not visited[i] and G[v][i]:
#                     PUSH(stack0,i)     # (*)

# # def DFS(G, v):              # visit:PUSH시점과 연관, LtoR
# #     visited = [False]*(V+1)
# #     stack0 = CRTESTACK()
# #     print("-", v, end="")
# #     visited[v] = True               # (*) visit위치
# #     while True :
# #         w = 0
# #         for i in range(1,V+1):
# #             if not visited[i] and G[v][i] :
# #                 PUSH(stack0,v);     # (*)
# #                 w = i;
# #                 break   # (*)
# #         while w :
# #             print("-", w, end="")
# #             visited[w] = True           # (*) visit위치
# #             PUSH(stack0,w)              # (*)
# #             v = w
# #
# #             #v의 인접점w(not visited) 찾기
# #             w = 0
# #             for i in range(1,V+1):
# #                 if not visited[i] and G[v][i]:
# #                     w = i;
# #                     break
# #
# #         if ISEMPTY(stack0) : break
# #         v = POP(stack0)                 # (*)
# #
# #     print("")

# visited = [False]*(V+1)                 #루트 파악을 위해 +1만큼의 False를 담은 리스트 생성
# def DFS_recur(G,v) :
#     visited[v] = True                   # (*) visit위치 / v(v=1)가 시작위치이므로 True 값을 줌
#     print("-%d"%(v), end="")              # 루트를 출력하므로 첫번째 1을 프린트
#     for i in range(1,V+1):                # 1부터 시작하여 V+1까지 반복
#         if not visited[i] and G[v][i] :   # visited[i]번째를 방문하지 않았고 G[v][i]값이 1이면 / 방문하지 않았으며 라인이 있을 때
#           DFS_recur(G,i)                  # DFS recur 함수 실행 (재귀함수)
# #
# #
# G = [[0]*(V+1) for _ in range(V+1)]         #인덱스가 0 부터 시작하므로 +1만큼의 2차배열 만들기
# edges = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]   #연결되어있는 노드 (전,후)
# for i in range(0,len(edges),2) :            #u가 mother v가 sun
#     u = edges[i];
#     v = edges[i+1]
#     G[u][v] = G[v][u] = 1                   #어짜피 앞뒤 같은 연결이므로 1씩 추가

# DFS(G,1)
# DFS_recur(G,1)

# '''
# 1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7

# -1-2-4-6-5-7-3
# '''
# # def makeGraph(V, E):
# #     # 정점 번호를 key값, set()를 value값으로 갖는 기본 그래프
# #     # ex) {1:set(), 2:set(), 3:set()}
# #     graph = {key+1:set() for key in range(V)}
# #
# #     # 정점(V)에 연결된 다음 노드(E) 입력, 그래프 수정
# #     # ex) {1:{3, 4, 6}, 2:{3}, 3:set()}
# #     for _ in range(E):
# #         key, val = map(int, input().split())
# #         graph[key].add(val)
# #     return graph
# #
# #
# # def DFS(graph, V, E):
# #     visited = []
# #     stack = []
# #
# #     stack.append(V)
# #
# #     is_path = 0
# #     while stack:
# #         node = stack.pop()
# #         if node == E:
# #             is_path = 1
# #             break
# #
# #         if node not in visited:
# #             visited.append(node)
# #             stack.extend(graph[node])
# #     return is_path
# #
# #
# # T = int(input())
# #
# # for test_case in range(1, T+1):
# #     # V: 정점 E: 간선을 입력
# #     V, E = map(int, input().split())
# #     # 간선(E) 수 만큼 반복하며 딕셔너리형 그래프 만듬
# #     myGraph = makeGraph(V, E)
# #
# #     # 확인할 경로의 시작 정점과 끝 정점 입력
# #     cV, cE = map(int, input().split())
# #     # 깊이우선탐색으로 경로 확인
# #     ans = DFS(myGraph, cV, cE)
# #
# #     print('#{} {}'.format(test_case, ans))