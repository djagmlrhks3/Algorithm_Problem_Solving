import sys
sys.stdin = open('백준15654. N과 M (5).txt', 'r')

def permutation(res):
    if len(res) == M:
        print(' '.join(map(str, res)))
    for idx in range(N):
        if numbers[idx] not in res:
            permutation(res + [numbers[idx]])


N, M = map(int, input().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

permutation([])