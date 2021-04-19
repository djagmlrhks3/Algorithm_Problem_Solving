import sys
sys.stdin = open('백준11659. 구간 합 구하기 4.txt', 'r')
N, M = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
for idx in range(1, N):
    numbers[idx] += numbers[idx-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        if i == j:
            print(numbers[0])
        else:
            print(numbers[j-1])
    else:
        if i == j:
            print(numbers[j-1]-numbers[i-2])
        else:
            print(numbers[j-1]-numbers[i-2])