import sys
sys.stdin = open('백준10971. 외판원 순회 2.txt', 'r')

"""백트래킹"""
def backtraking(used, cost):
    global answer
    if len(used) == N:
        if city[used[-1]][used[0]]:
            cost += city[used[-1]][used[0]]
            answer = min(answer, cost)
        return
    if cost >= answer: return
    for node in range(N):
        if node not in used and city[used[-1]][node]:
            backtraking(used + [node], cost + city[used[-1]][node])

N = int(input())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = int(1e9)
for start in range(N):
    backtraking([start], 0)
print(answer)

"""순열"""
# from itertools import permutations
# def moving(li):
#     global answer
#     temp = 0
#     for idx in range(1, N):
#         if city[li[idx-1]][li[idx]]:
#             temp += city[li[idx-1]][li[idx]]
#         else: return # 가는 길이 없을 경우 return
#         if temp >= answer: return # 최소 비용보다 클 경우 return
#     if city[li[-1]][li[0]]: temp += city[li[-1]][li[0]]
#     else: return # 되돌아 가는 길이 없을 경우 return
#     if temp: answer = min(answer, temp)
#
# for li in permutations([i for i in range(N)], N):
#     moving(li)
# print(answer)