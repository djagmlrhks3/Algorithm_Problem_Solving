import sys
sys.stdin = open('백준18429. 근손실.txt', 'r')

# 백트래킹
def backtracking(n):
    global answer, weight
    if n == N:
        answer += 1
        return
    for i in range(N):
        if not visited[i]:
            if weight + exercise[i] - K >= 500:
                visited[i] = 1
                weight = weight + exercise[i] - K
                backtracking(n+1)
                weight = weight - exercise[i] + K
                visited[i] = 0


N, K = map(int, input().split())
exercise = list(map(int, sys.stdin.readline().split()))
weight = 500
answer = 0
visited = [0] * N
backtracking(0)
print(answer)

# 순열
from itertools import permutations

def calculate(li):
    global answer
    weight = 500
    for i in li:
        weight = weight + exercise[i] - K
        if weight < 500:
            return
    answer += 1

N, K = map(int, input().split())
exercise = list(map(int, sys.stdin.readline().split()))
answer = 0
visited = [0] * N

for li in permutations(range(N), N):
    calculate(li)
print(answer)