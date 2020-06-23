import sys
sys.stdin = open('백준1012. 유기농 배추.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())
def dfs():
    global result
    visited = []
    for i in range(N):
        for j in range(M):
            if fields[i][j] and (i, j) not in visited:
                stack = [(i,j)]
                result += 1
                while stack:
                    visited.append((i,j))
                    y, x = stack.pop(0)
                    for z in range(4):
                        ny = y+dx[z]
                        nx = x+dy[z]
                        if 0<= nx < M and 0<= ny < N:
                            if (ny, nx) not in visited and fields[ny][nx]:
                                stack.append((ny,nx))
                                visited.append((ny, nx))

for tc in range(T):
    """
    M : 가로길이
    N : 세로길이
    K : 배추개수
    """
    M, N, K = map(int,input().split())
    fields = [[0]*M for _ in range(N)]

    for k in range(K):
        s, e = map(int, input().split())
        fields[e][s] = 1

    result = 0
    dfs()
    print(result)
    # for i in fields:
    #     print(i)
    # print()
