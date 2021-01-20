import sys
sys.stdin = open('백준2447. 별 찍기 - 10.txt', 'r')


def recursive(r, c, interval, length):
    global N
    if r < 1 or c < 1: return # (1, 1) 보다 더 적은 시작점이면 return
    for nr in range(r, N, length): # 출발지점으로부터 length 만큼 떨어진 지점(행, 열)도 변경 가능한지 판단
        for nc in range(c, N, length):
            if 0 <= nr < N and 0 <= nc < N: # NxN 범위 내에 들어오는지 판단
                for i in range(nr, nr + interval): # (nr, nc)를 출발점으로하여 interval 범위만큼을 공백으로 처리
                    for j in range(nc, nc + interval):
                        stars[i][j] = ''
    recursive(r//3, c//3, interval//3, length//3)

N = int(input())
stars = [['*' for _ in range(N)] for _ in range(N)]

recursive(N//3, N//3, N//3, N)

for i in stars:
    string = ''
    for se in i:
        string += '*' if se == '*' else ' '
    print(string)
