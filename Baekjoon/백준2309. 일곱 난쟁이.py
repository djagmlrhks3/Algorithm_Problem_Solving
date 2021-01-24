import sys
sys.stdin = open('백준2309. 일곱 난쟁이.txt', 'r')
from itertools import combinations

candidates = [int(input()) for _ in range(9)]

for li in combinations(candidates, 7):
    if sum(li) == 100:
        for num in sorted(li):
            print(num)
        break