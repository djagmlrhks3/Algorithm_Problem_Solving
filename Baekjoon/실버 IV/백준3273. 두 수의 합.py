import sys
sys.stdin = open('백준3273. 두 수의 합.txt', 'r')

n = int(input())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

answer = 0
left, right = 0, n-1

while left < right:
    temp = numbers[left] + numbers[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(answer)