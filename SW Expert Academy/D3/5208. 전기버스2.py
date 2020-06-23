import sys
sys.stdin = open('5208. 전기버스2.txt', 'r')
#
# def check(n, cnt):
#     global result
#     if n >= N-1:
#         result = min(result,cnt);return
#     if cnt > result:return
#     # if step > steps:return
#     # if step >= result:return
#     check(n+stops[n], cnt+1) #배터리충전 : cnt / 이동횟수 : step
#     check(n+1, cnt)
# T = int(input())
# for tc in range(T):
#     N, *stops = map(int,input().split())
#     steps = 100000
#     result = 1000000
#     check(0, 0)
#     print('#{} {}'.format(tc+1,result))

def backtrack(idx, remain, cnt):
    global N, min, stops
    remain -= 1  # 다음정류장 도착하면 배터리 감소
    if idx == N:
        if cnt < min:
            min = cnt
        return
    if cnt > min:
        return
    # 배터리를 교환하고 다음 정류장으로 진행
    backtrack(idx + 1, stops[idx], cnt + 1)
    # 배터리를 교환하지 않고 다음 정류장으로 진행
    if remain > 0:
        backtrack(idx + 1, remain, cnt)


T = int(input())
for tc in range(1, T + 1):
    stops = list(map(int, input().split()))
    N = stops[0]  # 정류장의 개수
    min = 1000000
    backtrack(2, stops[1], 0)
    print("#%d" %tc, min)