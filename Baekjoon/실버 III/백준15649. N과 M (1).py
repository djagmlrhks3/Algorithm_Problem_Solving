import sys
sys.stdin = open('백준15649. N과 M (1).txt', 'r')

def recursive(n, used, res):
    global M
    if n == M:
        print(' '.join(map(str, res)))
    for idx in range(N):
        if not used[idx]:
            used[idx] = 1
            recursive(n+1, used, res + [numbers[idx]])
            used[idx] = 0

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
used = [0] * N
recursive(0, used[:], [])