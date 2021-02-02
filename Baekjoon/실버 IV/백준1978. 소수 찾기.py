import sys
sys.stdin = open('백준1978. 소수 찾기.txt', 'r')

def check(num):
    if num < 2: return False
    for i in range(2, num):
        if not num % i:
            return False
    return True

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0
for num in numbers:
    if check(num):
        answer += 1
print(answer)
