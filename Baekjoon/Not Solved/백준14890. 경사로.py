import sys
sys.stdin = open('백준14890. 경사로.txt', 'r')

def check(routes):
    global cnt, L
    for route in routes:
        length = 1
        before = 0
        direction = ''
        for r in range(len(route)):
            if r == 0:
                before = route[r]
            elif before - route[r] == 1: # 내리막
                length += 1
            elif before - route[r] == -1: # 오르막
                if length < L:
                    break
                else:
                    before = route[r]
                    length = 1
                direction = 'up'
            elif not before - route[r]: # 동일 선상
                if direction == 'up' and length < L:
                    break
                length += 1

            else:
                if length >= L:
                    length = 1
                    before = route[r]
                else:
                    break


        else:
            cnt += 1

N, L = map(int,input().split())
routes = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

check(routes)
check(zip(*routes))
print(cnt)
