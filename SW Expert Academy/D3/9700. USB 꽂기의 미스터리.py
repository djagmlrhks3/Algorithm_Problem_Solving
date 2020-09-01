import sys
sys.stdin = open('9700. USB 꽂기의 미스터리.txt', 'r')

T = int(input())
for tc in range(T):
    p, q = map(float, input().split())
    res = "YES" if (1-p) < p * (1-q) else "NO"
    print('#{} {}'.format(tc+1, res))