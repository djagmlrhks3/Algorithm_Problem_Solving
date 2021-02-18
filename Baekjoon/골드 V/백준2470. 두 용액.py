import sys
sys.stdin = open('백준2470. 두 용액.txt', 'r')

N = int(input())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

left, right = 0, N-1
minimum = abs(numbers[left] + numbers[right])
answer_left, answer_right = left, right

while left < right:
    now = abs(numbers[left] + numbers[right])
    if now == 0:
        answer_left, answer_right = left, right
        break
    if now < minimum:
        answer_left, answer_right = left, right
        minimum = now

    if numbers[left] + numbers[right] < 0: left += 1
    else: right -= 1

print(numbers[answer_left], numbers[answer_right])