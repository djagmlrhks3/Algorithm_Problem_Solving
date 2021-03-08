import sys
sys.stdin = open('백준1912. 연속합.txt', 'r')

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
DP = [0] * n
DP[0] = numbers[0]
for idx in range(1, n):
    DP[idx] = max(numbers[idx], numbers[idx] + DP[idx-1])
print(max(DP))