import sys
sys.stdin = open('백준11504. 가장 긴 바이토닉 부분 수열.txt', 'r')

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

DP = [1] * len(numbers)
reverse_DP = [1] * len(numbers)

for i in range(1, len(numbers)):
    for j in range(i):
        if numbers[i] > numbers[j]:
            DP[i] = max(DP[i], DP[j]+1)

for i in range(-2, -len(numbers), -1):
    for j in range(-1, i, -1):
        if numbers[i] > numbers[j]:
            reverse_DP[i] = max(reverse_DP[i], reverse_DP[j]+1)

answer = 0
for idx in range(len(numbers)):
    answer = max(answer, DP[idx] + reverse_DP[idx])
print(answer-1)