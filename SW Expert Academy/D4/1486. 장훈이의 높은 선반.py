import sys
sys.stdin = open('1486. 장훈이의 높은 선반.txt','r')

def calc(n, k, cursum):
    global ans
    if cursum >= B:
        if ans > cursum:
            ans = cursum
        return

def powerset(n, k, cursum):
    if ans < cursum: return
    if n == k:
        calc(n, k, cursum)
    else:
        A[k] = 1
        powerset(n, k+1, cursum + h[k])
        A[k] = 0
        powerset(n, k+1, cursum)

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))
    A = [0] * N
    ans = 0xffffff
    powerset(N, 0, 0)

    print("#{} {}".format(tc+1, ans - B))

# def solution(idx, total):
#     global result, N, B
#     #만약 N만큼 순회하였으면
#     if idx == N:
#         #지금까지 더한 값(total)이 기준치 B를 넘으면서 차이가 result 보다 작으면
#         if total >= B and result > total-B:
#             #result값 갱신
#             result = total-B
#         return
#     #인덱스+1 & 값추가 : 넣고
#     solution(idx+1, total+data[idx])
#     #인덱스+1 & 값추가X : 빼고
#     solution(idx+1, total)
#
# T = int(input())
# for tc in range(T):
#     N, B = map(int, input().split())
#     data = list(map(int,input().split()))
#     #결과값을 담을 변수
#     result = float('inf')
#     solution(0, 0)
#     print('#{} {}'.format(tc+1, result))