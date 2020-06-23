import sys
sys.stdin=open('백준2636. 치즈.txt','r')
sys.setrecursionlimit(100000)

def dfs(r,c): # 현재 공기의 상태를 바꿔주는 dfs
    global cheese, R, C, visit
    visit[r][c] = 1
    cheese[r][c] = -1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C  and visit[nr][nc] == 0 and cheese[nr][nc] == 0:
            # cheese[nr][nc] = -1
            dfs(nr,nc)
def change(r,c): # 공기와 접촉한 치즈를 녹이는 dfs
    global cheese, R, C, num_of_cheese, visit
    # 한 번 이라도 치즈를 녹이면 true
    # 못녹이면 false
    is_find = False
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and visit[nr][nc] == 0:
            if cheese[nr][nc] == -1:
                if change(nr,nc):
                    is_find = True
            elif cheese[nr][nc] == 1:   #치즈라면, 바꿔주고, 주변 공기 상태 확인
                # num_of_cheese += 1
                is_find = True
                num_of_cheese += 1
                cheese[nr][nc] = -1
                dfs(nr, nc)
    return is_find
dr = [-1,1,0,0]
dc = [0,0,-1,1]
R,C = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(R)]
visit = [[0]*C for _ in range(R)]
dfs(0,0) # 초기 외부공기 설정
#외부 공기 먼저 찾고, 외부 공기랑 맞닫는 면 찾기
cnt = 0
last = 0
while True:
    num_of_cheese = 0
    visit = [[0] * C for _ in range(R)]
    is_find = change(0,0)
    if is_find:
        cnt += 1
        last = num_of_cheese
    else:
        break
print(cnt)
print(last)