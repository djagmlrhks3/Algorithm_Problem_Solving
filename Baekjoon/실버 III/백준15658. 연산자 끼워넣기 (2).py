import sys
sys.stdin = open('백준15658. 연산자 끼워넣기 (2).txt', 'r')

def brute_force(idx, num, orders):
    global N, maximum, minimum
    if idx == N:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        return
    if orders[0]:
        orders[0] -= 1
        brute_force(idx+1, num + numbers[idx], orders)
        orders[0] += 1
    if orders[1]:
        orders[1] -= 1
        brute_force(idx+1, num - numbers[idx], orders)
        orders[1] += 1
    if orders[2]:
        orders[2] -= 1
        brute_force(idx+1, num * numbers[idx], orders)
        orders[2] += 1
    if orders[3]:
        orders[3] -= 1
        if num < 0:
            res = -(-num // numbers[idx])
            brute_force(idx + 1, res, orders)
        else:
            brute_force(idx+1, num // numbers[idx], orders)
        orders[3] += 1

def calculate(li):
    global maximum, minimum
    res = numbers[0]
    for idx in range(N-1):
        if li[idx] == '+':
            res += numbers[idx+1]
        elif li[idx] == '-':
            res -= numbers[idx+1]
        elif li[idx] == '*':
            res *= numbers[idx+1]
        else:
            res //= numbers[idx+1]
    if res > maximum: maximum = res
    if res < minimum: minimum = res

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
orders = list(map(int, sys.stdin.readline().split()))
minimum = int(1e9)
maximum = -int(1e9)
brute_force(1, numbers[0], orders)
print(maximum)
print(minimum)