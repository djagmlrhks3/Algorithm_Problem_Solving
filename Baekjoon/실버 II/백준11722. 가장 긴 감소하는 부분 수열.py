import sys
sys.stdin = open('백준11722. 가장 긴 감소하는 부분 수열.txt', 'r')
N = int(input())
A = list(map(int, sys.stdin.readline().split()))[::-1]

DP = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[j]+1, DP[i])
print(max(DP))