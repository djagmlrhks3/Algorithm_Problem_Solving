import sys
sys.stdin = open('4613. 러시아 국기 같은 깃발.txt', 'r')

def check(n, change, color):
    global N, M, res, colors
    if n == N:
        if color == 'R' and change < res:
            res = change; return
        else: return

    if color == 'W':
        check(n+1, change+(M-colors[n].count('W')), 'W')
        check(n+1, change+(M-colors[n].count('B')), 'B')
    elif color == 'B':
        check(n+1, change+(M-colors[n].count('B')), 'B')
        check(n+1, change+(M-colors[n].count('R')), 'R')
    else:
        check(n+1, change+(M-colors[n].count('R')), 'R')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    colors = [ input() for _ in range(N) ]
    change = colors[0].count('B') + colors[0].count('R')
    res = 10000000000000
    check(1, change, 'W')
    print('#{} {}'.format(tc+1, res))

