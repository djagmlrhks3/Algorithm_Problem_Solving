import sys
from bisect import bisect_left
sys.stdin = open('백준12015. 가장 긴 증가하는 부분 수열 2.txt', 'r')

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
DP = [numbers[0]]

for idx in range(1, N):
    if numbers[idx] > DP[-1]:
        DP.append(numbers[idx])
    else:
        insert_idx = bisect_left(DP, numbers[idx])
        DP[insert_idx] = numbers[idx]
print(len(DP))