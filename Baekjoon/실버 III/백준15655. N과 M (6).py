import sys
sys.stdin = open('백준15655. N과 M (6).txt', 'r')

def combination(n, res):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for idx in range(n, N):
        combination(idx+1, res + [numbers[idx]])


N, M = map(int, input().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
combination(0, [])