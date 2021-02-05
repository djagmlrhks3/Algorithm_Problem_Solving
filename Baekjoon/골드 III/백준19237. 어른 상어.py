import sys
sys.stdin = open('백준19237. 어른 상어.txt', 'r')

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find(s):
    for r in range(N):
        for c in range(N):
            if tank[r][c][0] == s and tank[r][c][1] == k:
                turn = sharks_d[s][n_d[s]-1]
                same = ''
                possible = []
                for t in turn:
                    nr = r + d[t-1][0]
                    nc = c + d[t-1][1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if tank[nr][nc][0] == 0:
                            possible.append((s, nr, nc, t))
                        elif tank[nr][nc][0] == s and not same:
                            same = (s, nr, nc, t)
                if len(possible):
                    ready.append(possible[0])
                else:
                    ready.append(same)
                return

def delete():
    global N
    for r in range(N):
        for c in range(N):
            if tank[r][c][0]:
                if tank[r][c][1] == 1:
                    tank[r][c] = [0, 0]
                else:
                    tank[r][c][1] -= 1

def move(ready):
    for r in ready:
        if tank[r[1]][r[2]][0] and tank[r[1]][r[2]][0] < r[0]:
            survive[r[0]] = 0
            continue
        tank[r[1]][r[2]] = [r[0], k+1]
        n_d[r[0]] = r[3]

N, M, k = map(int, input().split())

tank = [[[0, 0] for _ in range(N)] for _ in range(N)]

for r in range(N):
    temp = list(map(int, input().split()))
    for c in range(len(temp)):
        if temp[c]:
            tank[r][c] = [temp[c], k]

n_d = [0] + list(map(int, input().split())) # 상어 현재 방향

sharks_d = {} # 상어 우선순위 방향
for m in range(M):
    before = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
    sharks_d[m+1] = before


survive = [0] + [1] * (M) # 상어 생존 여부
time = 0 # 걸린 시간

while True:
    ready = []
    for s in range(1, 1+M):
        if survive[s]:
            find(s)
    move(ready)
    delete()

    time += 1
    if sum(survive) == 1:
        break
    if time > 1000:
        break

print(-1 if time > 1000 else time)

