import sys
sys.stdin = open('백준1292. 쉽게 푸는 문제.txt', 'r')

A, B = map(int, input().split())
numbers = []
num = 1
while len(numbers) <= 1000:
    numbers.extend([num] * num)
    num += 1
print(sum(numbers[A-1:B]))