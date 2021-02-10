import sys
sys.stdin = open('백준6603. 로또.txt', 'r')
from itertools import combinations

while True:
    k, *numbers = list(map(int, sys.stdin.readline().split()))
    if k == 0: break
    for li in combinations(numbers, 6):
        print(' '.join(map(str, li)))
    print()