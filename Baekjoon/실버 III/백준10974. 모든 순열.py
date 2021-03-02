import sys
from itertools import permutations
sys.stdin = open('백준10974. 모든 순열.txt', 'r')
N = int(input())
numbers = [i for i in range(1, N+1)]
for li in permutations(numbers, N):
    print(' '.join(map(str, li)))