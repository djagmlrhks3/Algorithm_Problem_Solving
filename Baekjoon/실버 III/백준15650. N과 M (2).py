import sys
sys.stdin = open('백준15650. N과 M (2).txt', 'r')

def recursive(start, res):
    global M
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for idx in range(start, N):
        recursive(idx+1, res + [numbers[idx]])


N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
recursive(0, [])
