import sys
sys.stdin = open('5209. 최소 생산 비용.txt', 'r')

def solution(idx, total):
    global result
    if idx == N:
        result = min(result, total)
        return
    if total >= result:return
    for i in range(N):
        if not check[i]:
            check[i] = 1 #
            solution(idx+1, total+production[idx][i])
            check[i] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    production = [list(map(int,input().split())) for _ in range(N)]
    check = [0] * N
    result = 1000000000
    solution(0, 0)
    print('#{} {}'.format(tc+1, result))