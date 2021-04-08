import sys
from bisect import bisect_left

sys.stdin = open('백준18870. 좌표 압축.txt', 'r')
N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
sort_numbers = sorted(list(set(numbers[::])))
answer = []
for num in numbers:
    answer.append(bisect_left(sort_numbers, num))
print(' '.join(map(str, answer)))