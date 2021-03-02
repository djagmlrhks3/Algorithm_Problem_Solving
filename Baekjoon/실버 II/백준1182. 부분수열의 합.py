import sys
sys.stdin = open('백준1182. 부분수열의 합.txt', 'r')

"""백트래킹"""
N, S = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0
def combination(n, li):
    global answer, N
    if sum(li) == S and li:
        answer += 1
    if n == N: return
    for idx in range(n, N):
        combination(idx+1, li + [numbers[idx]])
combination(0, [])
print(answer)

# 순열
# from itertools import combinations
# for k in range(1, N):
#     for li in combinations(numbers, k):
#         if sum(li) == S:
#             answer += 1
# print(answer)