import sys
sys.stdin = open('2806. N-Queen.txt','r')

def recursive(r):
    global N, answer
    if r == N:
        answer += 1
        return
    for c in range(N):
        if h[c] and right[r+c] and left[r-c+N-1]:
            h[c] = right[r+c] = left[r-c+N-1] = False
            recursive(r+1)
            h[c] = right[r+c] = left[r-c+N-1] = True


T = int(input())
for tc in range(T):
    N = int(input())
    answer = 0
    h = [True] * N
    left = [True] * (2 * N - 1)
    right = [True] * (2 * N - 1)
    recursive(0)
    print('#{} {}'.format(tc+1, answer))