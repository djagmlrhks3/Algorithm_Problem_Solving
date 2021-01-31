import sys
sys.stdin = open('백준11399. ATM.txt', 'r')

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)
answer = 0
for idx in range(len(numbers)):
    answer += sum(numbers[:idx+1])
print(answer)