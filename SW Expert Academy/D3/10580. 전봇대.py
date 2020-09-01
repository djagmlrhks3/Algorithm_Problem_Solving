import sys
sys.stdin = open('10580. 전봇대.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    res = 0
    check = list()
    for n in range(N):
        l, r = map(int, input().split())
        if not len(check):
            check.append((l, r))
        else:
            for c in check:
                if l > c[0] and r < c[1]:
                    res += 1
                elif l < c[0] and r > c[1]:
                    res += 1
            check.append((l, r))
    print('#{} {}'.format(tc+1, res))