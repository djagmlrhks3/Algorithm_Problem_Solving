import sys
sys.stdin = open('백준14002. 가장 긴 증가하는 부분 수열 4.txt', 'r')
N = int(input())
A = list(map(int, sys.stdin.readline(). split()))
DP = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[j]+1, DP[i])

length = max(DP)
answer = []
for idx in range(-1, -N-1, -1):
    if DP[idx] == length:
        answer.append(A[idx])
        length -= 1

print(len(answer))
print(' '.join(map(str, answer[::-1])))