import sys
sys.stdin = open('백준21608. 상어 초등학교.txt', 'r')

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def calculate():
    global N, answer
    for r in range(N):
        for c in range(N):
            score = 0
            for idx in range(4):
                nr = r + d[idx][0]
                nc = c + d[idx][1]
                if 0 <= nr < N and 0 <= nc < N:
                    if seats[nr][nc] in students[seats[r][c]]:
                        score += 1
            if score:
                answer += (10 ** (score-1))

N = int(input())
students = dict()
answer = 0
seats = [[0] * N for _ in range(N)]
for i in range(N*N):
    s, *li = sys.stdin.readline().split()
    students[s] = li

for k, v in students.items():
    max_friend, max_empty = 0, 0
    row, col = N+1, N+1
    for r in range(N):
        for c in range(N):
            if not seats[r][c]:
                friend, empty = 0, 0
                for idx in range(4):
                    nr = r + d[idx][0]
                    nc = c + d[idx][1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if not seats[nr][nc]:
                            empty += 1
                        elif seats[nr][nc] in v:
                            friend += 1
                if friend > max_friend:
                    row, col = r, c
                    max_friend, max_empty = friend, empty
                elif friend == max_friend:
                    if empty > max_empty:
                        row, col = r, c
                        max_friend, max_empty = friend, empty
                    elif empty == max_empty:
                        if r < row:
                            row, col = r, c
                            max_friend, max_empty = friend, empty
                        elif r == row and c < col:
                            col = c
                            max_friend, max_empty = friend, empty
    seats[row][col] = k

calculate()
print(answer)
