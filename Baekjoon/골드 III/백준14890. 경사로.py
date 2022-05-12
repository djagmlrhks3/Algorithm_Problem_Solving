import sys
sys.stdin = open('백준14890. 경사로.txt', 'r')

def check(routes):
    global cnt, L
    for route in routes:
        length = 1
        before = route[0]
        i = 1
        while i < N:
            if before - route[i] == 0:  # 동일 선상
                i += 1
                length += 1
                continue
            elif before - route[i] == 1:  # 내리막길(1칸 차이)
                length = 1
                flag = True # 경사로 설치여부
                while i+1 < len(route):
                    if length == L: break
                    if before - route[i+1] == 1:
                        i += 1
                        length += 1
                        continue
                    else:
                        flag = False
                        break
                if length < L: flag = False
                if flag:
                    before = route[i]
                    i += 1
                    length = 0
                else:
                    break
            elif before - route[i] == -1:  # 오르막길(1칸 차이)
                if length < L: break
                before, length = route[i], 1
                i += 1
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