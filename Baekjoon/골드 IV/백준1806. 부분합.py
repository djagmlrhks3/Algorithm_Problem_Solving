import sys
sys.stdin = open('백준1806. 부분합.txt', 'r')

N, S = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))

l, r = 0, 1
length = int(1e9)
total = numbers[l] + numbers[r]
while l <= r and r < N:
    if total < S:
        r += 1
        if r == N: break
        total += numbers[r]
    else:
        length = min(length, r - l + 1)
        total -= numbers[l]
        l += 1

print(0) if length == int(1e9) else print(length)