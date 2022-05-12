import sys
from itertools import combinations
sys.stdin = open('백준3040. 백설 공주와 일곱 난쟁이.txt', 'r')
candidates = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
for li in combinations(candidates, 7):
    if sum(li) == 100:
        for num in li:
            print(num)
        break