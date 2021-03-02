import sys
sys.stdin = open('백준10819. 차이를 최대로.txt', 'r')

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = 0
# 백트래킹
def calculate(li):
    global N
    temp = 0
    for idx in range(1, N):
        temp += abs(li[idx]-li[idx-1])
    return temp
def backtracking(n, li):
    global answer
    temp = calculate(li)
    answer = max(answer, temp)
    if n == N-1: return
    for idx in range(n+1, N):
        li[n], li[idx] = li[idx], li[n]
        backtracking(n+1, li)
        li[n], li[idx] = li[idx], li[n]
backtracking(0, A)
print(answer)

# 순열을 이용한 방법
# from itertools import permutations
# def calculate(li):
#     global answer
#     temp = 0
#     for idx in range(1, N):
#         temp += abs(li[idx]-li[idx-1])
#     if answer < temp:
#         answer = temp
# for li in permutations(A, N):
#     calculate(li)
# print(answer)
