import sys
sys.stdin = open('백준15656. N과 M (7).txt')

def recursive(used, res):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for idx in range(N):
        if used[idx] <= M:
            used[idx] += 1
            recursive(used, res + [numbers[idx]])
            used[idx] -= 1

N, M = map(int, input().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

recursive([0] * N, [])