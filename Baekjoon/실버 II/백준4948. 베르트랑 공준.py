import sys
sys.stdin = open('백준4948. 베르트랑 공준.txt', 'r')

def check(num):
    if num < 2:
        return False
    for i in range(2, num):
        if not num % i:
            return False
    return True
numbers = []
while True:
    number = int(input())
    if not number:
        break
    else:
        numbers.append(number)

decimal = [True] * (2 * max(numbers) + 1)
for n in range(2, 2*max(numbers)//2 + 1):
    if decimal[n]:
        for idx in range(2 * n, 2*max(numbers)+1, n):
            decimal[idx] = False
for num in numbers:
    cnt = 0
    for idx in range(num+1, 2*num+1):
        if decimal[idx]:
           cnt += 1
    print(cnt)