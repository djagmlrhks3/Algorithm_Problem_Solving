import sys
sys.stdin = open('백준 15665. N과 M (11).txt', 'r')

def recursive(used, res):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    check = 0
    for idx in range(N):
        if used[idx] < M and check != numbers[idx]:
            used[idx] += 1
            recursive(used, res + [numbers[idx]])
            check = numbers[idx]
            used[idx] -= 1

N, M = map(int, input().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
recursive([0] * N, [])
