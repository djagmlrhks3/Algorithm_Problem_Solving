import sys
sys.stdin = open('백준2521. 예산.txt', 'r')

def check(n):
    global M
    test = M
    for num in numbers:
        if num <= n:
            test -= num
        else:
            test -= n
        if test < 0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
if M >= sum(numbers):
    print(max(numbers))
else:
    left, right = 0, max(numbers)
    middle = (left + right) // 2
    while left <= right:
        if check(middle):
            left = middle+1
            middle = (left + right) // 2
        else:
            right = middle-1
            middle = (left + right) // 2
    print(middle)