import sys
sys.stdin = open('백준1189. 컴백홈.txt', 'r')

def backtracking(r, c, d):
    global answer, K
    # K거리로 집에 도착하면 +1
    if r == 0 and c == C - 1 and d == K:
        answer += 1
        return

    # 거리가 K보다 길면 return
    if d > K:
        return

    for i in range(4):
        nr, nc = r + dir[i][0], c + dir[i][1]
        # MAP을 벗어나면 return
        if 0 <= nr < R and 0 <= nc < C:
            if MAP[nr][nc] != 'T' and not visited[nr][nc]:
                visited[nr][nc] = 1
                backtracking(nr, nc, d + 1)
                visited[nr][nc] = 0

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
R, C, K = map(int, input().split())
MAP = [sys.stdin.readline().rstrip() for _ in range(R)]
answer = 0
visited = [[0] * C for _ in range(R)]
visited[R - 1][0] = 1
backtracking(R - 1, 0, 1)
print(answer)