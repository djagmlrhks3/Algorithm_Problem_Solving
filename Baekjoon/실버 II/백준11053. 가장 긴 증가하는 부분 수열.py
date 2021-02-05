import sys
sys.stdin = open('백준11053. 가장 긴 증가하는 부분 수열.txt', 'r')

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
LIS = [1] * N
for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)

print(max(LIS))