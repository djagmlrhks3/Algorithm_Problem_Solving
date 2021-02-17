import sys
sys.stdin = open('백준15657. N과 M (8).txt', 'r')

def recursive(start, used, res):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for idx in range(start, N):
        if used[idx] < M:
            used[idx] += 1
            recursive(start, used, res + [numbers[idx]])
            start += 1
            used[idx] -= 1

N, M = map(int, input().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
recursive(0, [0]*N, [])

