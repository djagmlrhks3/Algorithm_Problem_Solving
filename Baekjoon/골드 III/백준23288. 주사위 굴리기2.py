import sys
from collections import deque
sys.stdin = open('백준23288. 주사위 굴리기2.txt', 'r')
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
d = [0, 1, 2, 3]

# bfs탐색
def bfs(r, c, n):
    cnt = 1
    queue = deque([(r, c)])
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dir[i][0], c + dir[i][1]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and board[nr][nc] == n:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                    cnt += 1
    return cnt

def rotate(c):
    #시계
    if c:
        return (idx+1) % 4
    # 반시계
    else:
        return (idx-1) % 4

def check(idx):
    if idx == 0 and r-1 < 0:
        idx = 2
    elif idx == 1 and c+1 > M-1:
        idx = 3
    elif idx == 2 and r+1 > N-1:
        idx = 0
    elif idx == 3 and c-1 < 0:
        idx = 1
    return idx

def move(idx):
    global r, c
    #상
    if d[idx] == 0:
        r -= 1
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    # 우
    elif d[idx] == 1:
        c += 1
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    # 하
    elif d[idx] == 2:
        r += 1
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    # 좌
    elif d[idx] == 3:
        c -= 1
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]

dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
N, M, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r, c, idx = 0, 0, 1
answer = 0
while K:
    # 방향설정
    idx = check(idx)
    # 이동
    move(idx)
    # 점수내기
    answer += bfs(r, c, board[r][c]) * board[r][c]
    # 회전
    if dice[3][1] > board[r][c]:
        idx = rotate(True)
    elif dice[3][1] < board[r][c]:
        idx = rotate(False)
    K -= 1

print(answer)