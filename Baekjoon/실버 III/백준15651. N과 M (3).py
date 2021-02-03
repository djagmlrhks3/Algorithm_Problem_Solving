import sys
sys.stdin = open('백준15651. N과 M (3).txt', 'r')

def recursive(n, used, res):
    global M
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for idx in range(N):
        if used[idx] <= M:
            used[idx] += 1
            recursive(n+1, used, res + [numbers[idx]])
            used[idx] -= 1

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
recursive(0, [0]*N, [])
