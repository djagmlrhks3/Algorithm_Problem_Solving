import sys
sys.stdin = open('백준1987. 알파벳.txt')
sys.setrecursionlimit(10**6)
R, C = map(int, input().split())
board = [sys.stdin.readline().rstrip() for _ in range(R)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(r, c, cnt):
    global answer
    if cnt == 26:
        answer = 26
        return
    else:
        answer = max(answer, cnt)
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if 0 <= nr < R and 0 <= nc < C:
            temp = ord(board[nr][nc])-ord('A')
            if not check[temp]:
                check[temp] = 1
                dfs(nr, nc, cnt+1)
                check[temp] = 0

check = [0] * 26
check[ord(board[0][0])-ord('A')] = 1
answer = 0
dfs(0, 0, 1)
print(answer)