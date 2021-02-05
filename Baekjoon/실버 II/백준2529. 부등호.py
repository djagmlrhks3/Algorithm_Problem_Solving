import sys
sys.stdin = open('백준2529. 부등호.txt', 'r')

def recursive(n, used, total):
    global  maximum, minimum
    if n == N:
        if int(total) > int(maximum):
            maximum = total
        if int(total) < int(minimum):
            minimum = total
        return
    for num in range(0, 10):
        if not used[num]:
            if order[n] == "<" and int(total[-1]) < num:
                used[num] = 1
                recursive(n+1, used, total + str(num))
                used[num] = 0
            elif order[n] == ">" and int(total[-1]) > num:
                used[num] = 1
                recursive(n+1, used, total + str(num))
                used[num] = 0

N = int(input())
order = list(map(str, sys.stdin.readline().split()))

maximum = '0'
minimum = '9876543210'

for i in range(10):
    used = [0] * 10
    used[i] = 1
    recursive(0, used, str(i))

print(maximum)
print(minimum)