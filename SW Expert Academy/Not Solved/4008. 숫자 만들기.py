from itertools import permutations
import sys
sys.stdin = open('4008. 숫자 만들기.txt', 'r')

def calculate(li):
    start = numbers[0]
    for i in range(0, len(li)):
        if li[i] == '+':
            start += numbers[i+1]
        elif li[i] == '-':
            start -= numbers[i+1]
        elif li[i] == '*':
            start *= numbers[i+1]
        else:
            start = int(start / numbers[i+1])
    return start

T = int(input())
for tc in range(T):
    N = int(input())
    plus, minus, multi, divide = map(int, input().split())
    orders = ['+' for _ in range(plus)] + ['-' for _ in range(minus)] + ['*' for _ in range(multi)] + ['/' for _ in range(divide)]
    numbers = list(map(int, input().split()))
    minimum = 0xfffffff
    maximum = -0xffffff
    for li in permutations(orders, len(orders)):
        result = calculate(li)
        maximum = max(maximum, result)
        minimum = min(minimum, result)
    print('#{} {}'.format(tc+1, maximum - minimum))
