import sys
sys.stdin = open('백준15663. N과 M (9).txt', 'r')

def recursive(used, res):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    check = 0
    for idx in range(len(numbers)):
        if used[idx] and numbers[idx] != check:
            used[idx] = False
            recursive(used, res + [numbers[idx]])
            check = numbers[idx]
            used[idx] = True

N, M = map(int, input().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

appeared = []
recursive([True]*N, [])