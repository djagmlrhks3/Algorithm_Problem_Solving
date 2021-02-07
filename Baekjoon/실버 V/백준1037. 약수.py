import sys
sys.stdin = open('백준1037.약수.txt', 'r')

N = int(input())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

if N == 1:
    print(numbers[0] ** 2)
else:
    print(numbers[0] * numbers[-1])