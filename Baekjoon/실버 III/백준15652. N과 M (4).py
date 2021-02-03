import sys
sys.stdin = open('백준15652. N과 M (4).txt', 'r')

def recursive(start, used, res):
    global M
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for idx in range(start, N):
        if used[idx] < M:
            used[idx] += 1
            recursive(idx, used, res + [numbers[idx]])
            used[idx] -= 1

N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
recursive(0, [0]*N, [])