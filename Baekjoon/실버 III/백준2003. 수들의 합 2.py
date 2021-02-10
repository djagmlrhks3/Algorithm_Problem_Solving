import sys
sys.stdin = open('백준2003. 수들의 합 2.txt', 'r')

N, M = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
print(numbers)

answer = 0
left, right = 0, 1
while right <= N:
    if sum(numbers[left:right]) == M:
        answer += 1
    if sum(numbers[left:right]) < M:
        right += 1
    else:
        left += 1
print(answer)