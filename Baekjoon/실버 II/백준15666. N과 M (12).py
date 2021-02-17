import sys
sys.stdin = open('백준15666. N과 M (12).txt', 'r')

def recursive(start, used, res):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for idx in range(start, len(numbers)):
        if used[idx] < M:
            used[idx] += 1
            recursive(idx, used, res + [numbers[idx]])
            used[idx] -= 1

N, M = map(int, input().split())
numbers = sorted(list(set(map(int, sys.stdin.readline().split()))))
recursive(0, [0] * len(numbers), [])