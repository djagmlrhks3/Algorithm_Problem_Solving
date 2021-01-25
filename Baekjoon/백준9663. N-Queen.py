import sys
sys.stdin = open('백준9663. N-Queen.txt', 'r')

def nqueen(r):
    global answer, N
    if r == N:
        answer += 1
        return
    for c in range(N):
        if not (v[c] or r_d[r+c] or l_d[r-c+N-1]):
            v[c] = r_d[r+c] = l_d[r-c+N-1] = 1
            nqueen(r+1)
            v[c] = r_d[r+c] = l_d[r-c+N-1] = 0

N = int(input())
v, r_d, l_d = [0] * N, [0] * (2*N-1), [0] * (2*N-1)
answer = 0
nqueen(0)
print(answer)