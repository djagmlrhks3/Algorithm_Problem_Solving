import sys
sys.stdin = open('백준15664. N과 M (10).txt', 'r')

def recursive(start, res):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    check = 0
    for idx in range(start, N):
        if numbers[idx] != check:
            recursive(idx+1, res + [numbers[idx]])
            check = numbers[idx]

N, M = map(int, input().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
recursive(0, [])