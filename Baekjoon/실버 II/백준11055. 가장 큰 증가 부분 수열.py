import sys
sys.stdin = open('백준11055. 가장 큰 증가 부분 수열.txt', 'r')
N = int(input())
A = list(map(int, sys.stdin.readline().split()))

DP = A[::]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(A[i]+DP[j], DP[i])
print(max(DP))