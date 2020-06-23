import sys
sys.stdin = open('1247. 최적 경로.txt', 'r')

def solution(x, y, n, total):
    global result, N, hi, hj
    if n == N: #고객의 집을 다 방문하면
        total = total + abs(x-hi) + abs(y-hj) #내 집 방문
        if total > result:return #지금까지 방문한 것이 result보다 크면 return
        result = total #아니면 result 초기화
    if total > result:return #만약 지금까지의 총합이 result보다 크면? return(가지치기)
    for i in range(N): #고객의 집을 방문(N)
        if not visited[i]: #방문하지 않으면
            visited[i] = True #방문체크 후 방문한집을 x, y좌표넣어서 재귀 & total계산
            solution(customers[2*i], customers[2*i+1], n+1, total+abs(x-customers[2*i]) + abs(y-customers[2*i+1]))
            visited[i] = False #방문초기화 (순열)

T = int(input())
for tc in range(T):
    N = int(input()) #고객의 수
    ci, cj, hi, hj, *customers = map(int, input().split()) #company / home / customers
    visited = [False] * N #방문여부
    result = float('inf') #결과값을 나타내는 변수(초기화)
    solution(ci, cj, 0, 0)
    print('#{} {}'.format(tc+1, result))